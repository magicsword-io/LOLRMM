"""Shared policy for domains exported as standalone detection indicators."""

import ipaddress
import re
from functools import lru_cache
from pathlib import Path


SENTINEL_VALUES = frozenset({"user_managed", "user-managed"})
PLACEHOLDER_RE = re.compile(r"^<[^>]+>$")
# Shared services cannot identify one cataloged product at hostname granularity.
# Product-specific subdomains and customer-specific cloud tenants remain useful.
SHARED_HOSTS = frozenset({
    "github.com", "githubusercontent.com", "raw.githubusercontent.com",
    "objects.githubusercontent.com", "ghcr.io", "github.io", "pages.dev",
    "amazonaws.com", "s3.amazonaws.com", "cloudfront.net", "azurewebsites.net",
    "blob.core.windows.net", "windows.net", "cloudflare.com", "api.cloudflare.com",
    "cloudflarestorage.com", "google.com", "googleapis.com", "gstatic.com",
    "googleusercontent.com", "firebaseapp.com", "web.app", "appspot.com",
    "microsoft.com", "azure.com", "office.com", "live.com",
    "stunserver.stunprotocol.org",
})


def is_domain_placeholder(value):
    return isinstance(value, str) and (
        value.strip().casefold() in SENTINEL_VALUES
        or PLACEHOLDER_RE.fullmatch(value.strip()) is not None
    )


@lru_cache(maxsize=1)
def suffix_rules():
    """Read the pinned ICANN PSL, including wildcard and exception rules.

    Private service suffixes include cataloged remote-access services themselves;
    shared general-purpose hosts are handled separately above.
    """
    exact, wildcard, exceptions = set(), set(), set()
    source = Path(__file__).with_name("data") / "public_suffix_list.dat"
    for line in source.read_text(encoding="utf-8").splitlines():
        if line == "// ===END ICANN DOMAINS===":
            break
        rule = line.split("//", 1)[0].strip()
        if not rule:
            continue
        target = exceptions if rule.startswith("!") else wildcard if rule.startswith("*.") else exact
        rule = rule.removeprefix("!").removeprefix("*.")
        target.add(rule.encode("idna").decode("ascii").casefold())
    if not {"com", "edu", "co.uk"} <= exact:
        raise ValueError("Pinned public suffix list is missing required ICANN rules")
    return exact, wildcard, exceptions


def is_public_suffix(host):
    exact, wildcard, exceptions = suffix_rules()
    labels = host.encode("idna").decode("ascii").casefold().split(".")
    suffix_length = 1  # PSL's implicit '*' rule also covers unknown TLDs.
    for idx in range(len(labels)):
        suffix = ".".join(labels[idx:])
        if suffix in exceptions:
            return False
        if suffix in exact:
            suffix_length = max(suffix_length, len(labels) - idx)
        if idx > 0 and suffix in wildcard:
            suffix_length = max(suffix_length, len(labels) - idx + 1)
    return len(labels) == suffix_length


def domain_issue(value):
    """Return (rule, reason), or None for a usable domain/context placeholder."""
    if not isinstance(value, str) or not value.strip():
        return "domain-empty", "domain selectors must be nonempty strings"
    if value != value.strip():
        return "domain-whitespace", "leading/trailing whitespace changes matching semantics"
    if is_domain_placeholder(value):
        return None
    domain = value.casefold().rstrip(".")
    if domain in {"n/a", "none", "null", "unknown", "tbd"}:
        return "domain-placeholder", "placeholder text is not a detection indicator"
    try:
        ip = ipaddress.ip_address(domain)
        if not ip.is_global:
            return "domain-special-ip", "local/private/special-use IPs do not identify a tool"
        return None
    except ValueError:
        pass
    if (not re.fullmatch(r"[a-z0-9_*?.-]+", domain) or ".." in domain
            or len(domain) > 253 or any(len(label) > 63 for label in domain.split("."))):
        return "domain-syntax", "use a hostname pattern, without a URL, path, whitespace, or regex"
    if domain in {"localhost", "local"} or domain.endswith((".localhost", ".local")):
        return "domain-local", "local hostnames do not identify a tool"
    # Require a fixed registrable suffix even for embedded label wildcards.
    labels = domain.split(".")
    fixed = []
    for label in reversed(labels):
        if "*" in label or "?" in label:
            break
        fixed.insert(0, label)
    suffix = ".".join(fixed)
    if not suffix or is_public_suffix(suffix):
        return "domain-public-suffix", "pattern covers an entire public suffix or has no fixed registrable domain"
    if domain.removeprefix("*.") in SHARED_HOSTS:
        return "domain-shared-host", "shared infrastructure is not a standalone indicator for this tool"
    return None


def context_issues(record, field):
    """Validate an explicit context-only designation, never a general waiver."""
    if "Detection" in record and not isinstance(record["Detection"], bool):
        yield f"{field}.Detection", record["Detection"], "Detection must be a boolean"
    if record.get("Detection") is False:
        reason = record.get("DetectionReason")
        if not isinstance(reason, str) or not reason.strip():
            yield f"{field}.DetectionReason", reason, "context-only evidence requires a nonempty explanation"


def catalog_domain_issues(data):
    if not isinstance(data, dict):
        return
    artifacts = data.get("Artifacts") or {}
    if not isinstance(artifacts, dict):
        return
    networks = artifacts.get("Network") or []
    if not isinstance(networks, list):
        return
    for idx, network in enumerate(networks):
        if not isinstance(network, dict):
            continue
        field = f"Artifacts.Network[{idx}]"
        for subfield, value, reason in context_issues(network, field):
            yield subfield, value, "detection-context", reason
        domains = network.get("Domains") or []
        if not isinstance(domains, list):
            continue
        for d_idx, domain in enumerate(domains):
            issue = domain_issue(domain)
            if issue and not (issue[0] == "domain-shared-host" and network.get("Detection") is False):
                yield f"{field}.Domains[{d_idx}]", domain, *issue


def should_export_domain(domain):
    return isinstance(domain, str) and not is_domain_placeholder(domain) and domain_issue(domain) is None


def detection_domains(network):
    if not isinstance(network, dict) or network.get("Detection", True) is not True:
        return []
    return [value.casefold().rstrip(".") for value in network.get("Domains") or []
            if should_export_domain(value)]


def domain_patterns(domains):
    """Sigma globs with a DNS label boundary, never substring matching.

    Plain domains cover apex and subdomains. Explicit wildcards retain their
    scope. Include absolute DNS names with a trailing dot as well.
    """
    patterns = set()
    for value in domains:
        if not should_export_domain(value):
            continue
        domain = value.casefold().rstrip(".")
        try:
            ipaddress.ip_address(domain)
            continue  # IP evidence does not belong in DNS/hostname rules.
        except ValueError:
            pass
        patterns.update((domain, domain + "."))
        if "*" not in domain and "?" not in domain:
            patterns.update(("*." + domain, "*." + domain + "."))
    return sorted(patterns)

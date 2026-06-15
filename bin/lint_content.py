#!/usr/bin/env python3
"""
Content lint for LOLRMM yaml catalog.

Distinct from `bin/validate.py` (schema/structural).  This script checks
intent-level quality of detection-ready fields — primarily
Artifacts.Network[].Domains and Artifacts.Network[].Ports — and surfaces
patterns that produce downstream false positives when ingested by SIEM /
EDR / lookup-table consumers.

Two severity tiers:

* TIER 1 (error) -- patterns with zero legitimate use case in this
  catalog.  Always wrong.  Fails the build (exit non-zero).

* TIER 2 (warn)  -- patterns that need human judgement.  Surfaced in
  output but do not fail the build.  Reviewer should confirm intent.

Usage:
    python3 bin/lint_content.py                # walk default yaml/ dir
    python3 bin/lint_content.py -y other/dir   # walk a different dir

Exit codes:
    0  no errors
    1  one or more tier-1 errors
"""

from __future__ import annotations

import argparse
import glob
import ipaddress
import os
import re
import sys
from dataclasses import dataclass
from typing import Iterable

import yaml


# ---------------------------------------------------------------------------
# Severity / finding model
# ---------------------------------------------------------------------------


ERROR = "error"
WARN = "warn"


@dataclass
class Finding:
    severity: str
    file: str
    field: str
    value: str
    rule: str
    reason: str
    suggest: str

    def render(self) -> str:
        return (
            f"{self.file}:\n"
            f"  field:    {self.field}\n"
            f"  value:    {self.value!r}\n"
            f"  severity: {self.severity}\n"
            f"  rule:     {self.rule}\n"
            f"  reason:   {self.reason}\n"
            f"  suggest:  {self.suggest}\n"
        )


# ---------------------------------------------------------------------------
# Tier 1 / Tier 2 rule definitions
# ---------------------------------------------------------------------------


# Tier-1: domain values that are always wrong as detection input.
TIER1_DOMAIN_EXACT = {
    "*.local",
    "*.localhost",
    "localhost",
    "127.0.0.1",
    "0.0.0.0",
    "::1",
}

# Tier-1: catch-all wildcards.  Would match the entire TLD.
TIER1_DOMAIN_CATCHALL = {
    "*",
    "*.com",
    "*.org",
    "*.net",
    "*.io",
    "*.co",
    "*.me",
    "*.app",
    "*.dev",
    "*.xyz",
}

# Tier-1: bare TLDs.  Almost certainly a typo.
TIER1_BARE_TLDS = {
    "com",
    "net",
    "org",
    "io",
    "co",
    "me",
    "app",
    "dev",
    "xyz",
    "info",
    "biz",
}

# Tier-2: sentinel + placeholder values the linter must allow through.
ALLOWED_BARE_LABELS = {"user_managed", "user-managed"}


def _is_special_ip(value: str) -> tuple[bool, str | None]:
    """Return (True, reason) if value is an IP in a special-use range."""
    try:
        ip = ipaddress.ip_address(value)
    except ValueError:
        return False, None
    if ip.is_loopback:
        return True, "loopback IP"
    if ip.is_link_local:
        return True, "link-local IP"
    if ip.is_multicast:
        return True, "multicast IP"
    if ip.is_unspecified:
        return True, "unspecified IP (0.0.0.0 / ::)"
    if ip.is_private:
        return True, "RFC1918 / private IP"
    if isinstance(ip, ipaddress.IPv6Address) and ip.is_reserved:
        return True, "reserved IPv6 address"
    return False, None


_PLACEHOLDER_RE = re.compile(r"^<[^>]+>$")  # e.g. '<operator-supplied-host>'


def _check_domain(file: str, idx_path: str, value: object) -> Iterable[Finding]:
    """Yield findings for a single Domains entry."""
    if not isinstance(value, str):
        yield Finding(
            ERROR, file, idx_path, repr(value),
            "domain-not-string",
            "Domains entries must be strings",
            "wrap the value in quotes or restructure the list",
        )
        return

    raw = value
    stripped = raw.strip()

    if raw != stripped:
        yield Finding(
            ERROR, file, idx_path, raw,
            "domain-whitespace",
            "domain value has leading or trailing whitespace — silently breaks exact-match lookups",
            "trim the value",
        )

    val = stripped
    val_lower = val.lower()

    # Allow sentinels + angle-bracket placeholders to pass without further checks.
    if val in ALLOWED_BARE_LABELS or _PLACEHOLDER_RE.match(val):
        return

    if val_lower in TIER1_DOMAIN_EXACT:
        yield Finding(
            ERROR, file, idx_path, val,
            "domain-loopback-or-local",
            f"{val!r} matches every mDNS/Bonjour, AD-local, or loopback host — zero attribution signal",
            "use the 'user_managed' sentinel and explain in Description",
        )
        return

    if val_lower in TIER1_DOMAIN_CATCHALL:
        yield Finding(
            ERROR, file, idx_path, val,
            "domain-catchall-wildcard",
            f"{val!r} would match the entire TLD — silently broken as a detection input",
            "narrow to the actual vendor subdomain or use 'user_managed'",
        )
        return

    if val_lower in TIER1_BARE_TLDS:
        yield Finding(
            ERROR, file, idx_path, val,
            "domain-bare-tld",
            f"bare TLD {val!r} — almost certainly a typo (no host portion)",
            "fix the typo or remove the entry",
        )
        return

    # URL / path inside a Domains list (wrong field).
    if "://" in val or "/" in val:
        yield Finding(
            ERROR, file, idx_path, val,
            "domain-url-or-path",
            "URLs and paths belong in References, not in Network.Domains (silently match nothing as a hostname lookup)",
            "move to References or replace with the bare hostname",
        )
        return

    # Malformed wildcard: starts with '*' but not '*.'.
    if val.startswith("*") and not val.startswith("*.") and val != "*":
        apex = val[1:]
        yield Finding(
            ERROR, file, idx_path, val,
            "domain-malformed-wildcard",
            f"wildcard {val!r} is missing the dot after '*' AND over-matches FP prefixes like 'xyz{apex}'. The original intent was almost certainly to match both apex AND subdomains.",
            f"replace with TWO entries to preserve apex coverage without the FP-prefix bug: '{apex}' (apex) AND '*.{apex}' (subdomains)",
        )
        return

    # IP-shaped values.
    is_special, reason = _is_special_ip(val)
    if is_special:
        yield Finding(
            ERROR, file, idx_path, val,
            "domain-special-ip",
            f"{val!r} is a {reason} — never a useful RMM-attribution signal",
            "use 'user_managed' for administrator-supplied on-prem servers",
        )
        return

    # Tier-2: public IP appearing in Domains list.  Sometimes intentional
    # (vendor pins an IP for telemetry, threat-actor C2) but worth a
    # second look to make sure the entry was deliberate.
    try:
        ipaddress.ip_address(val)
        yield Finding(
            WARN, file, idx_path, val,
            "domain-public-ip",
            "public IP in Domains — usually intentional (vendor-pinned or threat-actor C2), but confirm and consider documenting context in the entry Description",
            "leave as-is if intentional; otherwise move to a separate 'C2' entry with explanation",
        )
        return
    except ValueError:
        pass

    # Tier-2: bare single-label hostname (no dot).
    if (
        "." not in val
        and re.fullmatch(r"[a-zA-Z0-9_-]+", val)
        and not val.isdigit()
    ):
        yield Finding(
            WARN, file, idx_path, val,
            "domain-bare-single-label",
            f"bare single-label hostname {val!r} — usually FP-prone (matches any host with that name on the local network)",
            "qualify the hostname (foo.example.com) or use 'user_managed' sentinel",
        )


def _check_port(file: str, idx_path: str, value: object) -> Iterable[Finding]:
    """Yield findings for a single Ports entry."""
    if isinstance(value, int):
        if value < 1 or value > 65535:
            yield Finding(
                ERROR, file, idx_path, str(value),
                "port-out-of-range",
                f"port {value} is outside the valid 1-65535 range",
                "fix the port number",
            )
        return

    if not isinstance(value, str):
        yield Finding(
            ERROR, file, idx_path, repr(value),
            "port-not-int-or-string",
            "Ports entries must be ints or numeric strings",
            "convert to integer",
        )
        return

    val = value.strip()
    if val.upper() in ("N/A", "NA", "TBD", "UNKNOWN", "NONE"):
        yield Finding(
            ERROR, file, idx_path, value,
            "port-sentinel-string",
            f"placeholder string {value!r} silently produces broken downstream CSV/KQL output",
            "drop the entry or use an empty list 'Ports: []' if no port is documented",
        )
        return

    if "/" in val:
        yield Finding(
            ERROR, file, idx_path, value,
            "port-protocol-suffix",
            f"protocol suffix in port field ({value!r}) silently produces broken downstream CSV/KQL output",
            "split into bare integer; document protocol in the entry Description",
        )
        return

    # Vendor-documented port ranges (e.g. Teramind audio UDP '1000-65535') are
    # accepted as strings.  Each endpoint must be a valid port.
    range_match = re.fullmatch(r"(\d+)-(\d+)", val)
    if range_match:
        lo, hi = int(range_match.group(1)), int(range_match.group(2))
        if not (1 <= lo <= 65535 and 1 <= hi <= 65535 and lo <= hi):
            yield Finding(
                ERROR, file, idx_path, value,
                "port-range-invalid",
                f"port range {value!r} has invalid endpoints (must be 1-65535, lo <= hi)",
                "fix the range",
            )
        return

    try:
        n = int(val)
        if n < 1 or n > 65535:
            yield Finding(
                ERROR, file, idx_path, value,
                "port-out-of-range",
                f"port {value!r} is outside the valid 1-65535 range",
                "fix the port number",
            )
    except ValueError:
        yield Finding(
            ERROR, file, idx_path, value,
            "port-not-numeric",
            f"port {value!r} is not numeric",
            "convert to integer (1-65535)",
        )


# ---------------------------------------------------------------------------
# Walk
# ---------------------------------------------------------------------------


def lint_file(path: str) -> list[Finding]:
    with open(path, "r", encoding="utf-8") as fh:
        try:
            data = yaml.safe_load(fh)
        except yaml.YAMLError as exc:
            # Schema validator will catch this separately; we just don't
            # emit content findings for a file that can't be parsed.
            return [
                Finding(
                    ERROR, path, "<file>", "", "yaml-parse-error",
                    f"yaml.safe_load failed: {exc!s}",
                    "fix the yaml syntax (see bin/validate.py output)",
                )
            ]

    if not isinstance(data, dict):
        return []

    out: list[Finding] = []
    nets = (data.get("Artifacts") or {}).get("Network") or []
    if not isinstance(nets, list):
        return out

    for n_idx, net in enumerate(nets):
        if not isinstance(net, dict):
            continue
        for d_idx, dom in enumerate(net.get("Domains") or []):
            out.extend(_check_domain(
                path, f"Artifacts.Network[{n_idx}].Domains[{d_idx}]", dom,
            ))
        for p_idx, port in enumerate(net.get("Ports") or []):
            out.extend(_check_port(
                path, f"Artifacts.Network[{n_idx}].Ports[{p_idx}]", port,
            ))

    return out


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    parser.add_argument(
        "-y", "--yaml-dir", default="yaml",
        help="path to the yaml/ directory (default: yaml)",
    )
    parser.add_argument(
        "--quiet", action="store_true",
        help="suppress success message",
    )
    args = parser.parse_args()

    files = sorted(
        glob.glob(os.path.join(args.yaml_dir, "*.yaml"))
        + glob.glob(os.path.join(args.yaml_dir, "*.yml"))
    )
    if not files:
        print(f"no yaml files found under {args.yaml_dir!r}", file=sys.stderr)
        return 1

    all_findings: list[Finding] = []
    for f in files:
        all_findings.extend(lint_file(f))

    errors = [x for x in all_findings if x.severity == ERROR]
    warns = [x for x in all_findings if x.severity == WARN]

    if errors:
        print(f"\nContent Lint: {len(errors)} error(s)\n", file=sys.stderr)
        for x in errors:
            print(x.render(), file=sys.stderr)

    if warns:
        print(f"\nContent Lint: {len(warns)} warning(s)\n")
        for x in warns:
            print(x.render())

    if errors:
        print(
            f"\n[FAIL] {len(errors)} content-lint error(s) "
            f"({len(warns)} warning(s)) across {len(files)} yamls",
            file=sys.stderr,
        )
        return 1

    if not args.quiet:
        print(
            f"[OK] content lint clean: 0 errors, "
            f"{len(warns)} warning(s) across {len(files)} yamls"
        )
    return 0


if __name__ == "__main__":
    sys.exit(main())

#!/usr/bin/env python3
"""Regenerate exports in isolation and verify the final detection selectors."""

import argparse
import csv
import fnmatch
import json
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

import yaml

from domain_safety import catalog_domain_issues, domain_issue, is_domain_placeholder, detection_domains, domain_patterns
from evidence_safety import evidence_issues, hash_issue, SHARED_PUBLISHERS
from path_safety import empty_selector, metadata_path, unsafe_catalog_paths, unsafe_path_reason


PATH_FIELDS = frozenset({"Image", "ParentImage", "TargetFilename", "FileName", "OriginalFileName"})
DOMAIN_FIELDS = frozenset({"query", "QueryName", "DestinationHostname", "DestinationDomain"})
BENIGN_IMAGES = (
    r"C:\Windows\System32\notepad.exe", r"C:\Windows\System32\calc.exe",
    r"C:\Windows\System32\svchost.exe", r"C:\Windows\explorer.exe",
    r"C:\Program Files\Google\Chrome\Application\chrome.exe",
    r"C:\Program Files\Mozilla Firefox\firefox.exe",
    r"C:\Program Files\Unrelated\agent.exe", r"C:\Unrelated\installer.exe",
)
BENIGN_DOMAINS = (
    "github.com", "raw.githubusercontent.com", "objects.githubusercontent.com",
    "www.google.com", "www.microsoft.com", "example.org", "attacker.test",
)


def selector_matches(key, pattern, value):
    """Evaluate the emitted glob operators for the regression corpus.

    This is deliberately limited to the modifiers our generators emit, not a
    replacement for a Sigma backend. Windows separators are Sigma-escaped.
    """
    parts = key.split("|")
    pattern = pattern.replace("\\\\", "\\").casefold()
    if "endswith" in parts:
        pattern = "*" + pattern
    if "contains" in parts:
        pattern = "*" + pattern + "*"
    return fnmatch.fnmatchcase(value.casefold(), pattern)


def rule_issues(rule):
    if not isinstance(rule, dict):
        yield "<rule>", "rule must be a mapping"
        return
    detection = rule.get("detection")
    if (not isinstance(detection, dict) or not isinstance(detection.get("condition"), str)
            or not detection["condition"].strip()
            or detection["condition"].strip().casefold() in {"true", "false", "1=1", "*"}):
        yield "detection", "missing selection condition"
        return
    selections = {k: v for k, v in detection.items() if k not in {"condition", "timeframe"}}
    if not selections:
        yield "detection", "rule has no selections"
    branches = []
    for name, selection in selections.items():
        if isinstance(selection, list):
            if not selection:
                yield f"detection.{name}", "empty selection list"
            branches.extend((f"{name}[{idx}]", branch if isinstance(branch, dict) else {"keyword": branch})
                            for idx, branch in enumerate(selection))
        else:
            branches.append((name, selection if isinstance(selection, dict) else {"keyword": selection}))
    for name, selection in branches:
        if not isinstance(selection, dict) or not selection:
            yield f"detection.{name}", "selection must be a nonempty mapping"
            continue
        for key, raw in selection.items():
            field = key.split("|")[0]
            values = raw if isinstance(raw, list) else [raw]
            location = f"detection.{name}.{key}"
            if not values:
                yield location, "empty selector list"
            for value in values:
                if not isinstance(value, str):
                    if value is None or field in PATH_FIELDS | DOMAIN_FIELDS:
                        yield location, "null/non-string selector"
                    continue
                if empty_selector(value) or value.strip() in {"*", "?", "*.*", ".*"}:
                    yield location, f"empty/sentinel/catch-all selector: {value!r}"
                if field in PATH_FIELDS:
                    reason = unsafe_path_reason(value)
                    if reason or metadata_path(value):
                        yield location, f"unsafe path selector {value!r}: {reason or 'unexpanded placeholder'}"
                    for benign in BENIGN_IMAGES:
                        if selector_matches(key, value, benign):
                            yield location, f"selector {value!r} matches benign control {benign!r}"
                if field in DOMAIN_FIELDS:
                    if "|" in key:
                        yield location, "hostname/DNS selectors must use label-boundary globs, not contains/endswith"
                    if is_domain_placeholder(value) or domain_issue(value):
                        yield location, f"unsafe domain selector: {value!r}"
                    for benign in BENIGN_DOMAINS:
                        if selector_matches(key, value, benign):
                            yield location, f"selector {value!r} matches unrelated host {benign!r}"
                if field.casefold() in {"signature", "signer", "publisher", "company"}:
                    if any(c in value for c in '*?'):
                        yield location, "publisher/signer identities must not contain wildcards"
                    if value.casefold() in SHARED_PUBLISHERS:
                        scoped = any(k.split("|")[0] in PATH_FIELDS and all(
                            isinstance(v, str) and not any(c in v for c in '*?')
                            and not empty_selector(v)
                            for v in (scope if isinstance(scope, list) else [scope])
                        ) for k, scope in selection.items())
                        if not scoped:
                            yield location, "shared publisher must be ANDed with file scope in the same selection"
                hash_sizes = {"sha256": 64, "sha1": 40, "md5": 32, "imphash": 32}
                if field.casefold() in hash_sizes and (reason := hash_issue(value, hash_sizes[field.casefold()])):
                    yield location, reason


def catalog_csv_issues(rows, sources):
    """Compare raw artifact evidence without losing duplicate-name records."""
    actual = []
    for idx, row in enumerate(rows):
        try:
            artifacts = json.loads(row["Artifacts"])
            actual.append((row["Name"], json.dumps(artifacts, sort_keys=True)))
        except (KeyError, TypeError, ValueError):
            yield f"catalog CSV row {idx + 1} has invalid/missing Name or Artifacts"
    expected = [(tool["Name"], json.dumps(tool.get("Artifacts", {}), sort_keys=True))
                for tool in sources]
    if sorted(actual) != sorted(expected):
        yield "catalog CSV changed or lost source artifact evidence/scope/context metadata"


def verify_repository(repo):
    """Exercise production generators, keeping source and committed exports intact."""
    with tempfile.TemporaryDirectory(prefix="lolrmm-detection-safety-") as directory:
        root = Path(directory)
        shutil.copytree(repo / "bin", root / "bin", ignore=shutil.ignore_patterns("__pycache__"))
        shutil.copytree(repo / "yaml", root / "yaml")
        source_files = {path.name: path.read_bytes() for path in (root / "yaml").glob("*.y*ml")}
        # Include old outputs so stale broad rules cannot escape this gate.
        if (repo / "detections").exists():
            shutil.copytree(repo / "detections", root / "detections")
        for script, arguments in (("sigma-gen.py", ["--skip-yaml-update"]), ("site.py", [])):
            result = subprocess.run([sys.executable, str(root / "bin" / script), *arguments],
                                    cwd=root, text=True, capture_output=True)
            if result.returncode:
                raise RuntimeError(f"{script} failed:\n{result.stdout}\n{result.stderr}")
        problems = []
        if source_files != {path.name: path.read_bytes() for path in (root / "yaml").glob("*.y*ml")}:
            problems.append("generators modified source YAML")
        files = sorted((root / "detections/sigma").glob("*.yml"))
        for path in files:
            rule = yaml.safe_load(path.read_text(encoding="utf-8"))
            for field, reason in rule_issues(rule):
                problems.append(f"{path.relative_to(root)}: {field}: {reason}")
        api = root / "website/public/api"
        tools = json.loads((api / "rmm_tools.json").read_text(encoding="utf-8"))
        sources = [yaml.safe_load(content) for _, content in sorted(source_files.items())]
        if sorted(json.dumps(item, sort_keys=True) for item in sources) != sorted(json.dumps(item, sort_keys=True) for item in tools):
            problems.append("raw API changed or lost source evidence/scope/context metadata")
        with (api / "rmm_tools.csv").open(newline="", encoding="utf-8") as stream:
            problems.extend(catalog_csv_issues(list(csv.DictReader(stream)), sources))
        expected_csv = {(domain, tool["Name"]) for tool in sources
                        for network in (tool.get("Artifacts") or {}).get("Network") or []
                        for domain in detection_domains(network)}
        with (api / "rmm_domains.csv").open(newline="", encoding="utf-8") as stream:
            rows = list(csv.DictReader(stream))
        actual_csv = {(row["URI"], row["RMM_Tool"]) for row in rows}
        if actual_csv != expected_csv or len(rows) != len(actual_csv):
            problems.append("domain CSV lost eligible indicators or included duplicate/context-only evidence")
        expected_network = {}
        for tool in sources:
            prefix = tool["Name"].lower().replace(" ", "_").replace("(", "_").replace(")", "_")
            expected_network[f"{prefix}_network_sigma.yml"] = domain_patterns([
                domain for network in (tool.get("Artifacts") or {}).get("Network") or []
                for domain in detection_domains(network)
            ])
        for filename, expected in expected_network.items():
            path = root / "detections/sigma" / filename
            if expected:
                actual = yaml.safe_load(path.read_text())["detection"]["selection"] if path.exists() else None
                if (not isinstance(actual, dict) or set(actual) != {"DestinationHostname"}
                        or sorted(actual["DestinationHostname"]) != expected):
                    problems.append(f"{filename}: generated domains lost scope or eligible coverage")
            elif path.exists():
                problems.append(f"{filename}: rule survived with no eligible source domains")
        for tool in tools:
            for field, value, *reason in (*catalog_domain_issues(tool), *evidence_issues(tool), *unsafe_catalog_paths(tool)):
                problems.append(f"api/{tool['Name']}: {field}: {value!r}: {'; '.join(reason)}")
        for filename in ("generic_rmm_detection.yml", "rmm_domains_dns_queries.yml"):
            if (root / "detections/sigma" / filename).read_bytes() != (api / "detections/sigma" / filename).read_bytes():
                problems.append(f"{filename}: canonical and public Sigma copies differ")
        aggregate = yaml.safe_load((root / "detections/sigma/rmm_domains_dns_queries.yml").read_text())
        if aggregate["detection"]["selection"] != {"query": domain_patterns([domain for domain, _ in expected_csv])}:
            problems.append("aggregate DNS rule differs from eligible domain indicators")
        return len(tools), len(files), problems


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo", type=Path, default=Path(__file__).resolve().parents[1])
    args = parser.parse_args()
    tools, rules, problems = verify_repository(args.repo)
    for problem in problems:
        print(f"ERROR: {problem}")
    if problems:
        print(f"Generated detection safety failed: {len(problems)} finding(s)")
        return 1
    print(f"Generated detection safety passed: {tools} tools, {rules} Sigma rules, benign controls, and API evidence verified")
    return 0


if __name__ == "__main__":
    sys.exit(main())

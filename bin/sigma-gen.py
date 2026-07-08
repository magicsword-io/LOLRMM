import argparse
import os
import ntpath
import re
import yaml
from datetime import date
import uuid
from typing import Dict, List, Any, Optional, Tuple

# Namespace UUID for generating deterministic rule IDs
LOLRMM_NAMESPACE = uuid.UUID("a1b2c3d4-e5f6-7890-abcd-ef1234567890")
SIGMA_RULE_PREFIX = "https://github.com/magicsword-io/LOLRMM/blob/main/detections/sigma/"
UNQUOTED_SPECIAL_VALUE = re.compile(
    r"(?m)^(\s*(?:-\s+|[^:\n]+:\s+))([*%@`][^#\n]*)$"
)


def yaml_date(value: Any) -> str:
    if isinstance(value, date):
        return value.strftime("%Y-%m-%d")
    return str(value).strip()


def listify(value: Any) -> List[Any]:
    if value is None:
        return []
    if isinstance(value, list):
        return value
    return [value]


def normalize_detection(detection: Dict[str, Any]) -> Dict[str, Any]:
    normalized = {}
    for key, value in detection.items():
        if key == "condition":
            normalized[key] = value
        elif isinstance(value, dict):
            normalized[key] = {
                subkey: [str(item) for item in listify(subvalue)]
                for subkey, subvalue in value.items()
            }
        else:
            normalized[key] = value
    return normalized


def normalize_rule(rule: Dict[str, Any]) -> Dict[str, Any]:
    normalized = {}
    for key in ("title", "id", "status", "description", "author", "level"):
        normalized[key] = str(rule.get(key, "")).strip()

    normalized["date"] = yaml_date(rule.get("date", ""))
    if "modified" in rule:
        normalized["modified"] = yaml_date(rule["modified"])

    normalized["references"] = [str(item) for item in listify(rule.get("references"))]
    normalized["tags"] = [str(item) for item in listify(rule.get("tags"))]
    normalized["logsource"] = rule.get("logsource", {})
    normalized["detection"] = normalize_detection(rule.get("detection", {}))
    normalized["falsepositives"] = [
        str(item) for item in listify(rule.get("falsepositives"))
    ]
    return normalized


def load_existing_sigma_rule(filepath: str) -> Tuple[Optional[Dict[str, Any]], bool]:
    """Load a Sigma rule and report whether the source file needs rewriting."""
    if not os.path.exists(filepath):
        return None, False

    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    needs_rewrite = False
    try:
        data = yaml.safe_load(content)
    except yaml.YAMLError:
        # Some legacy generated rules have unquoted wildcard/path values such
        # as *.example.com or %localappdata%, which YAML treats as syntax.
        # Quote those for comparison without changing the file on disk.
        sanitized = UNQUOTED_SPECIAL_VALUE.sub(r"\1'\2'", content)
        data = yaml.safe_load(sanitized)
        needs_rewrite = True

    return data if isinstance(data, dict) else None, needs_rewrite


class IndentDumper(yaml.SafeDumper):
    def increase_indent(self, flow: bool = False, indentless: bool = False) -> Any:
        return super().increase_indent(flow, False)


def extract_artifacts(yaml_data: Dict[str, Any]) -> Dict[str, List[str]]:
    artifacts = {"files": [], "registry": [], "network": [], "processes": []}

    for item in yaml_data.get("Artifacts", {}).get("Disk", []) or []:
        if isinstance(item, dict) and "File" in item:
            artifacts["files"].append(item["File"])

    for item in yaml_data.get("Artifacts", {}).get("Registry", []) or []:
        if isinstance(item, dict) and "Path" in item:
            artifacts["registry"].append(item["Path"])

    for item in yaml_data.get("Artifacts", {}).get("Network", []) or []:
        if isinstance(item, dict):
            if "Domains" in item:
                if isinstance(item["Domains"], list):
                    artifacts["network"].extend(item["Domains"])
                elif isinstance(item["Domains"], str):
                    artifacts["network"].append(item["Domains"])

    details = yaml_data.get("Details", {})
    if isinstance(details, dict):
        artifacts["processes"] = [
            ntpath.basename(item)
            for item in details.get("InstallationPaths", []) or []
            if isinstance(item, str) and item.lower().endswith(".exe")
        ]

    return artifacts


def write_sigma_rule(rule: Dict[str, Any], filepath: str) -> None:
    """Write a Sigma rule with proper formatting."""
    with open(filepath, "w", encoding="utf-8") as f:
        # Title
        f.write(f"title: {rule['title']}\n")

        # ID
        f.write(f"id: {rule['id']}\n")

        # Status
        f.write(f"status: {rule['status']}\n")

        # Description with pipe syntax
        f.write("description: |\n")
        f.write(f"    {rule['description']}\n")

        # References
        f.write("references:\n")
        for ref in rule["references"]:
            f.write(f"    - {ref}\n")

        # Author
        f.write(f"author: {rule['author']}\n")

        # Date (without quotes)
        f.write(f"date: {rule['date']}\n")

        # Modified (only if present)
        if "modified" in rule:
            f.write(f"modified: {rule['modified']}\n")

        # Tags
        f.write("tags:\n")
        for tag in rule["tags"]:
            f.write(f"    - {tag}\n")

        # Logsource
        f.write("logsource:\n")
        f.write(f"    product: {rule['logsource']['product']}\n")
        f.write(f"    category: {rule['logsource']['category']}\n")

        # Detection
        f.write("detection:\n")
        detection = rule["detection"]
        for key, value in detection.items():
            if key == "condition":
                continue
            f.write(f"    {key}:\n")
            if isinstance(value, dict):
                for subkey, subvalue in value.items():
                    if isinstance(subvalue, list):
                        # Single element: write inline, multiple elements: write as list
                        if len(subvalue) == 1:
                            val = subvalue[0].replace("'", "''")
                            f.write(f"        {subkey}: '{val}'\n")
                        else:
                            f.write(f"        {subkey}:\n")
                            for item in subvalue:
                                val = item.replace("'", "''")
                                f.write(f"            - '{val}'\n")
                    else:
                        val = subvalue.replace("'", "''")
                        f.write(f"        {subkey}: '{val}'\n")
        f.write(f"    condition: {detection['condition']}\n")

        # Falsepositives
        f.write("falsepositives:\n")
        for fp in rule["falsepositives"]:
            f.write(f"    - {fp}\n")

        # Level
        f.write(f"level: {rule['level']}\n")


def write_sigma_rule_if_changed(rule: Dict[str, Any], filepath: str) -> None:
    existing_rule, needs_rewrite = load_existing_sigma_rule(filepath)
    if existing_rule:
        # Preserve already-published metadata so reruns do not churn every rule.
        rule["id"] = str(existing_rule.get("id", rule["id"]))
        if "date" in existing_rule:
            rule["date"] = yaml_date(existing_rule["date"])
        if "modified" in existing_rule:
            rule["modified"] = yaml_date(existing_rule["modified"])

        if not needs_rewrite and normalize_rule(existing_rule) == normalize_rule(rule):
            return

    write_sigma_rule(rule, filepath)


def generate_sigma_rules(yaml_file: str, output_dir: str) -> List[Dict[str, Any]]:
    with open(yaml_file, "r") as f:
        data = yaml.safe_load(f)

    name = data.get("Name", "Unknown")
    artifacts = extract_artifacts(data)

    rule_templates = {
        "registry": {
            "title": f"Potential {name} RMM Tool Registry Activity",
            "logsource": {"product": "windows", "category": "registry_event"},
            "detection_key": "TargetObject|contains",
        },
        "network": {
            "title": f"Potential {name} RMM Tool Network Activity",
            "logsource": {"product": "windows", "category": "network_connection"},
            "detection_key": "DestinationHostname|endswith",
        },
        "files": {
            "title": f"Potential {name} RMM Tool File Activity",
            "logsource": {"product": "windows", "category": "file_event"},
            "detection_key": "TargetFilename|endswith",
        },
        "processes": {
            "title": f"Potential {name} RMM Tool Process Activity",
            "logsource": {"product": "windows", "category": "process_creation"},
            "detection_key": "special",  # Handles both ParentImage and Image
        },
    }

    generated_rules = []
    for artifact_type, rule_template in rule_templates.items():
        if artifacts[artifact_type]:
            # Build detection based on artifact type
            if artifact_type == "processes":
                detection = {
                    "selection_parent": {
                        "ParentImage|endswith": artifacts[artifact_type].copy()
                    },
                    "selection_image": {
                        "Image|endswith": artifacts[artifact_type].copy()
                    },
                    "condition": "1 of selection_*",
                }
            else:
                detection = {
                    "selection": {
                        rule_template["detection_key"]: artifacts[artifact_type].copy()
                    },
                    "condition": "selection",
                }

            # Create rule with proper field order
            rule = {
                "title": rule_template["title"],
                "id": str(uuid.uuid5(LOLRMM_NAMESPACE, rule_template["title"])),
                "status": "experimental",
                "description": f"Detects potential {artifact_type} activity of {name} RMM tool",
                "references": ["https://github.com/magicsword-io/LOLRMM"],
                "author": "LOLRMM Project",
                "date": date.today().strftime("%Y-%m-%d"),
                "tags": ["attack.execution", "attack.t1219"],
                "logsource": rule_template["logsource"],
                "detection": detection,
                "falsepositives": [f"Legitimate use of {name}"],
                "level": "medium",
            }

            safe_name = (
                name.lower().replace(" ", "_").replace("(", "_").replace(")", "_")
            )
            output_file = f"{safe_name}_{artifact_type}_sigma.yml"
            full_output_path = os.path.join(output_dir, output_file)

            # Write with custom formatting only when content actually changes.
            write_sigma_rule_if_changed(rule, full_output_path)

            github_url = f"{SIGMA_RULE_PREFIX}{output_file}"
            generated_rules.append(
                {
                    "Sigma": github_url,
                    "Description": f"Detects potential {artifact_type} activity of {name} RMM tool",
                }
            )

    return generated_rules


def update_yaml_with_sigma_rules(
    yaml_file: str, sigma_rules: List[Dict[str, Any]]
) -> None:
    with open(yaml_file, "r") as f:
        data = yaml.safe_load(f)

    if "Detections" not in data:
        data["Detections"] = []

    manual_rules = [
        rule
        for rule in data["Detections"]
        if not rule.get("Sigma", "").startswith(
            SIGMA_RULE_PREFIX
        )
    ]

    existing_generated_urls = {
        rule.get("Sigma")
        for rule in data["Detections"]
        if isinstance(rule, dict)
        and rule.get("Sigma", "").startswith(SIGMA_RULE_PREFIX)
    }
    generated_urls = {rule["Sigma"] for rule in sigma_rules}

    if existing_generated_urls == generated_urls:
        return

    data["Detections"] = manual_rules + sigma_rules

    with open(yaml_file, "w", encoding="utf-8") as f:
        yaml.dump(
            data,
            f,
            Dumper=IndentDumper,
            sort_keys=False,
            allow_unicode=True,
            indent=4,
            width=4096,
        )


def main(update_yaml: bool = True) -> None:
    yaml_dir = "yaml/"
    output_dir = "detections/sigma/"
    os.makedirs(output_dir, exist_ok=True)

    for filename in os.listdir(yaml_dir):
        if filename.endswith(".yaml") or filename.endswith(".yml"):
            yaml_file = os.path.join(yaml_dir, filename)
            sigma_rules = generate_sigma_rules(yaml_file, output_dir)
            if update_yaml:
                update_yaml_with_sigma_rules(yaml_file, sigma_rules)

    yaml_status = "and YAML update " if update_yaml else ""
    print(
        f"[+] Sigma rule generation {yaml_status}complete. Files saved in {output_dir}"
    )


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--skip-yaml-update",
        action="store_true",
        help="Only write Sigma rules; leave source YAML files unchanged.",
    )
    args = parser.parse_args()
    main(update_yaml=not args.skip_yaml_update)

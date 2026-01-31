#!/usr/bin/env python3

"""Generate detection files for different SIEM platforms.

This module creates detection rules in multiple formats (Sigma, Splunk, KQL)
from LOLRMM YAML data, enabling security teams to deploy RMM detection
rules across heterogeneous SIEM environments.

Functionality:
    - Sigma rule generation (process creation and DNS queries)
    - Splunk detection queries (requires Enterprise Security)
    - KQL queries for Microsoft Defender for Endpoint
    - Tool count tracking and export
    - Multi-directory output support (local + website API)

Usage:
    python generate_detections.py

Examples:
    Generate all detection formats:
        python generate_detections.py

Output:
    - detections/sigma/*.yml (Sigma rules)
    - detections/splunk/*.yml (Splunk detection)
    - detections/kql/*.yml (KQL queries)
    - website/public/api/rmm_tools_count.json (Tool count)
"""

import os
import json
import yaml
import glob
import csv
from pathlib import Path
from datetime import datetime
from typing import Dict, List, Optional, Any


def _resolve_base_dir() -> str:
    """Resolve the project base directory from script location.
    
    Returns:
        Absolute path to the project root directory.
    """
    return os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def _ensure_dir_exists(directory: str) -> None:
    """Ensure a directory exists, creating it if necessary.
    
    Args:
        directory: Path to the directory to create.
        
    Raises:
        OSError: If directory creation fails.
    """
    try:
        os.makedirs(directory, exist_ok=True)
    except OSError as e:
        raise OSError(f"Failed to create directory {directory}: {e}") from e


def generate_sigma_rule() -> None:
    """Generate a generic Sigma rule for RMM process detection.
    
    Extracts executable names from YAML files and creates a Sigma detection
    rule targeting process creation events. Rule is written to both local
    and website API directories.
    
    Raises:
        FileNotFoundError: If YAML directory cannot be accessed.
        OSError: If output directory creation fails.
        yaml.YAMLError: If YAML parsing fails on a file.
    """
    base_dir = _resolve_base_dir()
    yaml_dir = os.path.join(base_dir, "yaml")
    
    if not os.path.isdir(yaml_dir):
        raise FileNotFoundError(f"YAML directory not found: {yaml_dir}")
    
    yaml_files = glob.glob(os.path.join(yaml_dir, "*.y*ml"))
    if not yaml_files:
        raise FileNotFoundError(f"No YAML files found in {yaml_dir}")

    exe_list: List[str] = []
    for yaml_file in yaml_files:
        try:
            with open(yaml_file, "r", encoding="utf-8") as file:
                data = yaml.safe_load(file)
            
            if not isinstance(data, dict):
                continue
                
            if "Details" in data and "InstallationPaths" in data["Details"]:
                paths = data["Details"]["InstallationPaths"]
                if isinstance(paths, list):
                    for path in paths:
                        if isinstance(path, str):
                            exe_name = os.path.basename(path)
                            if exe_name and not exe_name.startswith("*"):
                                exe_list.append(f"\\\\{exe_name}")
        except (yaml.YAMLError, IOError) as e:
            print(f"Warning: Failed to process {yaml_file}: {e}")

    # Deduplicate and sort
    exe_list = sorted(list(set(exe_list)))
    print(f"Found {len(exe_list)} unique RMM executables for Sigma rule")

    sigma_rule: Dict[str, Any] = {
        "title": "Generic RMM Tool Detection",
        "id": "ba1e3a37-6751-48e8-9f7a-73d9062f137c",
        "status": "experimental",
        "description": "Detects processes associated with common Remote Monitoring and Management (RMM) tools that could be used for lateral movement",
        "references": ["https://github.com/magicsword-io/LOLRMM"],
        "author": "LOLRMM Project",
        "date": "2025-03-18",
        "modified": datetime.now().strftime("%Y-%m-%d"),
        "tags": ["attack.lateral-movement", "attack.t1219"],
        "logsource": {"category": "process_creation", "product": "windows"},
        "detection": {
            "selection": {"Image|endswith": exe_list},
            "condition": "selection",
        },
        "falsepositives": ["Legitimate usage of remote management tools"],
        "level": "medium",
    }

    output_dirs = [
        os.path.join(base_dir, "detections", "sigma"),
        os.path.join(base_dir, "website", "public", "api", "detections", "sigma"),
    ]
    
    for output_dir in output_dirs:
        try:
            _ensure_dir_exists(output_dir)
            output_file = os.path.join(output_dir, "generic_rmm_detection.yml")
            with open(output_file, "w", encoding="utf-8") as file:
                yaml.dump(sigma_rule, file, default_flow_style=False, sort_keys=False)
            print(f"Generated Sigma rule at {output_file}")
        except OSError as e:
            print(f"Error writing Sigma rule to {output_dir}: {e}")


def generate_sigma_domains_rule() -> None:
    """Generate a Sigma rule for detecting DNS queries to RMM domains.
    
    Reads domains from rmm_domains.csv and creates a Sigma DNS detection rule.
    Falls back to hardcoded common RMM domains if CSV is unavailable.
    
    Raises:
        OSError: If output directory creation fails.
    """
    base_dir = _resolve_base_dir()
    api_dir = os.path.join(base_dir, "website", "public", "api")
    domains_file = os.path.join(api_dir, "rmm_domains.csv")

    domain_list: List[str] = []
    
    # Try to read from CSV file
    if os.path.isfile(domains_file):
        try:
            with open(domains_file, "r", encoding="utf-8") as file:
                csv_reader = csv.reader(file)
                next(csv_reader, None)  # Skip header safely
                for row in csv_reader:
                    if row and len(row) >= 1:
                        domain = row[0].strip()
                        if domain and "." in domain:
                            domain_list.append(f".{domain}")
        except (IOError, csv.Error) as e:
            print(f"Warning: Failed to read domains file {domains_file}: {e}")
            print("Using fallback domain list...")
    else:
        print(f"Warning: Domains file not found at {domains_file}. Using fallback list.")
    
    # Fallback to common RMM domains if CSV unavailable
    if not domain_list:
        domain_list = [
            ".anydesk.com",
            ".teamviewer.com",
            ".splashtop.com",
            ".connectwise.com",
            ".bomgar.com",
            ".logmein.com",
            ".supremo.com",
            ".dwservice.com",
            ".atera.com",
            ".gotomypc.com",
            ".rustdesk.com",
            ".screenconnect.com",
        ]

    # Deduplicate
    domain_list = sorted(list(set(domain_list)))

    sigma_domains_rule: Dict[str, Any] = {
        "title": "DNS Queries to Known RMM Domains",
        "id": "9fa68c28-79b2-4ab5-af95-0c7b2f706c63",
        "status": "experimental",
        "description": "Detects DNS queries to known Remote Monitoring and Management (RMM) tool domains that could indicate unauthorized remote access",
        "references": ["https://github.com/magicsword-io/LOLRMM"],
        "author": "LOLRMM Project",
        "date": "2025-03-18",
        "modified": datetime.now().strftime("%Y-%m-%d"),
        "tags": ["attack.command-and-control", "attack.t1219"],
        "logsource": {"category": "dns", "product": "any"},
        "detection": {
            "selection": {"query|contains": domain_list},
            "filter": {
                "query|contains": "your-approved-rmm.com"  # Placeholder for user customization
            },
            "condition": "selection and not filter",
        },
        "falsepositives": ["Legitimate usage of approved remote management tools"],
        "level": "medium",
    }

    output_dirs = [
        os.path.join(base_dir, "detections", "sigma"),
        os.path.join(base_dir, "website", "public", "api", "detections", "sigma"),
    ]
    
    for output_dir in output_dirs:
        try:
            _ensure_dir_exists(output_dir)
            output_file = os.path.join(output_dir, "rmm_domains_dns_queries.yml")
            with open(output_file, "w", encoding="utf-8") as file:
                yaml.dump(sigma_domains_rule, file, default_flow_style=False, sort_keys=False)
            print(f"Generated RMM domains Sigma rule at {output_file}")
        except OSError as e:
            print(f"Error writing Sigma domains rule to {output_dir}: {e}")


def generate_splunk_detection() -> None:
    """Generate a Splunk detection query for RMM tool usage.
    
    Creates a Splunk query that leverages Network Traffic datamodel and
    the remote access software lookup table to detect RMM tool usage.
    Requires Splunk Enterprise Security.
    
    Raises:
        OSError: If output directory creation or file write fails.
    """
    base_dir = _resolve_base_dir()
    
    splunk_detection: Dict[str, Any] = {
        "name": "Generic RMM Tool Detection for Splunk",
        "id": "splunk-rmm-001",
        "description": "Detects usage of Remote Monitoring and Management (RMM) tools via network traffic",
        "author": "LOLRMM Project",
        "date": datetime.now().strftime("%Y/%m/%d"),
        "query": """| tstats `security_content_summariesonly` count min(_time) as firstTime max(_time) as lastTime values(All_Traffic.dest_port) as dest_port latest(user) as user from datamodel=Network_Traffic by All_Traffic.src All_Traffic.dest, All_Traffic.app 
| `drop_dm_object_name(\"All_Traffic\")` 
| `security_content_ctime(firstTime)` 
| `security_content_ctime(lastTime)` 
| lookup remote_access_software remote_appid AS app OUTPUT isutility, description as signature, comment_reference as desc, category 
| search isutility = True 
| `remote_access_software_usage_exceptions` 
| `detect_remote_access_software_usage_traffic_filter`""",
        "references": [
            "https://github.com/magicsword-io/LOLRMM",
            "https://research.splunk.com/network/885ea672-07ee-475a-879e-60d28aa5dd42/",
        ],
        "requirements": [
            "Splunk Enterprise Security",
            "Network Traffic datamodel",
            "Remote Access Software lookup table",
        ],
    }

    output_dir = os.path.join(base_dir, "detections", "splunk")
    
    try:
        _ensure_dir_exists(output_dir)
        output_file = os.path.join(output_dir, "generic_rmm_detection.yml")
        with open(output_file, "w", encoding="utf-8") as file:
            yaml.dump(splunk_detection, file, default_flow_style=False, sort_keys=False)
        print(f"Generated Splunk detection at {output_file}")
    except OSError as e:
        print(f"Error writing Splunk detection to {output_dir}: {e}")


def generate_kql_detection() -> None:
    """Generate a KQL detection query for Microsoft Defender for Endpoint.
    
    Creates a KQL query that detects network connections to known RMM domains
    using the DeviceNetworkEvents table. Supports allowlisting approved RMM tools.
    
    Raises:
        OSError: If output directory creation or file write fails.
    """
    base_dir = _resolve_base_dir()
    
    kql_detection: Dict[str, Any] = {
        "name": "Generic RMM Domain Detection for Microsoft Defender for Endpoint",
        "id": "kql-rmm-001",
        "description": "Detects network connections to known RMM domains",
        "author": "LOLRMM Project",
        "date": datetime.now().strftime("%Y/%m/%d"),
        "query": """// Detecting Unauthorized RMM Instances in Your MDE Environment

let SanctionRMM = dynamic(\"YOUR_APPROVED_RMM_DOMAINS\"); // E.g. \"bomgarcloud.com\" - Replace with your approved RMM domains
let RMMList = externaldata(URI: string, RMMTool: string)
    [h'https://raw.githubusercontent.com/magicsword-io/LOLRMM/main/website/public/api/rmm_domains.csv'];
let RMMUrl = RMMList | project URI;

DeviceNetworkEvents
| where TimeGenerated > ago(1h)
| where ActionType == @\"ConnectionSuccess\"
| where RemoteUrl has_any(RMMUrl)
| where not (RemoteUrl has_any(SanctionRMM))
| summarize arg_max(TimeGenerated, *) by DeviceId""",
        "references": ["https://github.com/magicsword-io/LOLRMM"],
        "requirements": [
            "Microsoft Defender for Endpoint",
            "Access to DeviceNetworkEvents table",
        ],
    }

    output_dir = os.path.join(base_dir, "detections", "kql")
    
    try:
        _ensure_dir_exists(output_dir)
        output_file = os.path.join(output_dir, "generic_rmm_detection.yml")
        with open(output_file, "w", encoding="utf-8") as file:
            yaml.dump(kql_detection, file, default_flow_style=False, sort_keys=False)
        print(f"Generated KQL detection at {output_file}")
    except OSError as e:
        print(f"Error writing KQL detection to {output_dir}: {e}")


def count_rmm_tools() -> int:
    """Count the number of RMM tools in YAML files and export count.
    
    Scans the yaml/ directory for all YAML files and exports the count
    as JSON for use by the website API.
    
    Returns:
        Total count of YAML files found.
        
    Raises:
        FileNotFoundError: If YAML directory cannot be accessed.
        OSError: If output file cannot be written.
    """
    base_dir = _resolve_base_dir()
    yaml_dir = os.path.join(base_dir, "yaml")
    
    if not os.path.isdir(yaml_dir):
        raise FileNotFoundError(f"YAML directory not found: {yaml_dir}")
    
    yaml_files = glob.glob(os.path.join(yaml_dir, "*.y*ml"))
    count = len(yaml_files)

    if count == 0:
        print(f"Warning: No YAML files found in {yaml_dir}")

    # Save count to JSON file for website to use
    output_dir = os.path.join(base_dir, "website", "public", "api")
    
    try:
        _ensure_dir_exists(output_dir)
        output_file = os.path.join(output_dir, "rmm_tools_count.json")
        with open(output_file, "w", encoding="utf-8") as file:
            json.dump({"count": count}, file)
        print(f"Generated RMM tools count JSON with {count} tools at {output_file}")
    except OSError as e:
        raise OSError(f"Failed to write count to {output_dir}: {e}") from e
    
    return count


def main() -> None:
    """Main entry point for detection file generation.
    
    Orchestrates the generation of detection rules in all supported formats
    (Sigma, Splunk, KQL) and exports RMM tool count statistics.
    
    Exits with status 1 on fatal errors, 0 on success.
    """
    try:
        print("Generating detection files...")
        print()
        
        generate_sigma_rule()
        print()
        
        generate_sigma_domains_rule()
        print()
        
        generate_splunk_detection()
        print()
        
        generate_kql_detection()
        print()
        
        count = count_rmm_tools()
        print()
        print(f"Successfully generated detection files for {count} RMM tools")
        print("Detection files generation complete!")
        
    except (FileNotFoundError, OSError, yaml.YAMLError) as e:
        print(f"Error: {e}", file=__import__("sys").stderr)
        __import__("sys").exit(1)


if __name__ == "__main__":
    main()

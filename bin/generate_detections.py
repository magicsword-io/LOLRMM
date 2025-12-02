#!/usr/bin/env python3
"""
Generate detection files for different SIEM platforms.
This script creates Sigma, Splunk, and KQL detection rules.
"""

import os
import json
import yaml
import glob
from datetime import datetime


def generate_sigma_rule():
    """Generate a generic Sigma rule for RMM detection"""

    # Get a list of common RMM executables from YAML files
    yaml_dir = os.path.join(
        os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "yaml"
    )
    yaml_files = glob.glob(os.path.join(yaml_dir, "*.y*ml"))

    exe_list = []
    for yaml_file in yaml_files:
        try:
            with open(yaml_file, "r", encoding="utf-8") as file:
                data = yaml.safe_load(file)

            if "Details" in data and "InstallationPaths" in data["Details"]:
                for path in data["Details"]["InstallationPaths"]:
                    # Extract executable name
                    exe_name = os.path.basename(path)
                    if exe_name and not exe_name.startswith("*"):
                        exe_list.append(f"\\\\{exe_name}")
        except Exception as e:
            print(f"Error processing {yaml_file}: {e}")

    # Deduplicate the executable list
    exe_list = list(set(exe_list))

    # Sort the list for better readability
    exe_list.sort()

    # Print the number of executables found
    print(f"Found {len(exe_list)} unique RMM executables for Sigma rule")

    sigma_rule = {
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

    dirs = [
        os.path.join(
            os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
            "detections",
            "sigma",
        ),
        os.path.join(
            os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
            "website",
            "public",
            "api",
            "detections",
            "sigma",
        ),
    ]
    for output_dir in dirs:
        # Ensure the directory exists
        os.makedirs(output_dir, exist_ok=True)

        # Write the Sigma rule to a file
        output_file = os.path.join(output_dir, "generic_rmm_detection.yml")
        with open(output_file, "w", encoding="utf-8") as file:
            yaml.dump(sigma_rule, file, default_flow_style=False, sort_keys=False)

        print(f"Generated Sigma rule at {output_file}")


def generate_sigma_domains_rule():
    """Generate a Sigma rule for detecting DNS queries to RMM domains"""

    # Get a list of RMM domains from the domains.csv file
    api_dir = os.path.join(
        os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
        "website",
        "public",
        "api",
    )
    domains_file = os.path.join(api_dir, "rmm_domains.csv")

    domain_list = []
    try:
        import csv

        with open(domains_file, "r", encoding="utf-8") as file:
            csv_reader = csv.reader(file)
            next(csv_reader)  # Skip header
            for row in csv_reader:
                if row and len(row) >= 1:
                    domain = row[0].strip()
                    if domain and "." in domain:
                        domain_list.append(f".{domain}")
    except Exception as e:
        print(f"Error processing domains file {domains_file}: {e}")
        # Add some common RMM domains as fallback
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
    domain_list = list(set(domain_list))

    sigma_domains_rule = {
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

    dirs = [
        os.path.join(
            os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
            "detections",
            "sigma",
        ),
        os.path.join(
            os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
            "website",
            "public",
            "api",
            "detections",
            "sigma",
        ),
    ]
    for output_dir in dirs:
        # Ensure the directory exists
        os.makedirs(output_dir, exist_ok=True)

        # Write the Sigma rule to a file
        output_file = os.path.join(output_dir, "rmm_domains_dns_queries.yml")
        with open(output_file, "w", encoding="utf-8") as file:
            yaml.dump(
                sigma_domains_rule, file, default_flow_style=False, sort_keys=False
            )

        print(f"Generated RMM domains Sigma rule at {output_file}")


def generate_splunk_detection():
    """Generate a Splunk detection for RMM tools"""

    splunk_detection = {
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

    # Ensure the detections/splunk directory exists
    output_dir = os.path.join(
        os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
        "detections",
        "splunk",
    )
    os.makedirs(output_dir, exist_ok=True)

    # Write the Splunk detection to a file
    output_file = os.path.join(output_dir, "generic_rmm_detection.yml")
    with open(output_file, "w", encoding="utf-8") as file:
        yaml.dump(splunk_detection, file, default_flow_style=False, sort_keys=False)

    print(f"Generated Splunk detection at {output_file}")


def generate_kql_detection():
    """Generate a KQL detection for Microsoft Defender for Endpoint"""

    kql_detection = {
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

    # Ensure the detections/kql directory exists
    output_dir = os.path.join(
        os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "detections", "kql"
    )
    os.makedirs(output_dir, exist_ok=True)

    # Write the KQL detection to a file
    output_file = os.path.join(output_dir, "generic_rmm_detection.yml")
    with open(output_file, "w", encoding="utf-8") as file:
        yaml.dump(kql_detection, file, default_flow_style=False, sort_keys=False)

    print(f"Generated KQL detection at {output_file}")


def count_rmm_tools():
    """Count the number of YAML files and save as JSON"""
    yaml_dir = os.path.join(
        os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "yaml"
    )
    yaml_files = glob.glob(os.path.join(yaml_dir, "*.y*ml"))
    count = len(yaml_files)

    # Save count to JSON file for website to use
    output_dir = os.path.join(
        os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
        "website",
        "public",
        "api",
    )
    output_file = os.path.join(output_dir, "rmm_tools_count.json")

    with open(output_file, "w", encoding="utf-8") as file:
        json.dump({"count": count}, file)

    print(f"Generated RMM tools count JSON with {count} tools at {output_file}")
    return count


if __name__ == "__main__":
    print("Generating detection files...")
    generate_sigma_rule()
    generate_sigma_domains_rule()
    generate_splunk_detection()
    generate_kql_detection()
    count = count_rmm_tools()
    print(f"Found {count} RMM tools")
    print("Detection files generation complete!")

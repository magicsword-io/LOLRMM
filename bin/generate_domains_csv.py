#!/usr/bin/env python3
"""
Script to extract domains from YAML files and generate a CSV file.
This script reads all YAML files in the specified directory and extracts domains
from the 'Domains' section under 'Artifacts' > 'Network'.
"""

import os
import yaml
import csv
import glob
import re
from pathlib import Path


def clean_tool_name(filename):
    """Extract the clean tool name from the file name."""
    # Remove file extension and path
    name = os.path.basename(filename).rsplit(".", 1)[0]

    # Remove parentheses and underscores
    name = re.sub(r"[_()]", " ", name)

    # Handle special characters in filenames
    name = name.replace("__", "_")

    return name.strip()


def extract_domains(yaml_file_path):
    """Extract domains from a YAML file."""
    try:
        print(f"Processing file: {yaml_file_path}")
        with open(yaml_file_path, "r", encoding="utf-8") as file:
            data = yaml.safe_load(file)

        # Get the tool name from the YAML Name field if available, otherwise use filename
        tool_name = data.get("Name", clean_tool_name(yaml_file_path))
        print(f"Tool name: {tool_name}")

        # Extract domains from Artifacts > Network > Domains
        domains = []
        if "Artifacts" in data and "Network" in data["Artifacts"]:
            for network in data["Artifacts"]["Network"]:
                if "Domains" in network:
                    for domain in network["Domains"]:
                        # Only add the domain if it's not empty or 'user_managed'
                        if domain and domain != "user_managed":
                            domains.append((domain, tool_name))
                            print(f"Found domain: {domain} for tool: {tool_name}")

        return domains
    except Exception as e:
        print(f"Error processing {yaml_file_path}: {e}")
        return []


def generate_csv(yaml_dir, output_file):
    """Generate a CSV file with domains from all YAML files."""
    all_domains = []

    # Find all YAML files in the directory
    yaml_files = glob.glob(os.path.join(yaml_dir, "*.y*ml"))
    print(f"Found {len(yaml_files)} YAML files in {yaml_dir}")

    # Extract domains from each YAML file
    for yaml_file in yaml_files:
        domains = extract_domains(yaml_file)
        all_domains.extend(domains)

    # Write domains to CSV file
    with open(output_file, "w", newline="", encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["URI", "RMM_Tool"])
        for domain, tool in all_domains:
            writer.writerow([domain, tool])

    print(f"CSV file generated at {output_file} with {len(all_domains)} domains")
    return len(all_domains)


if __name__ == "__main__":
    yaml_dir = os.path.join(
        os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "yaml"
    )
    output_dir = os.path.join(
        os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
        "website",
        "public",
        "api",
    )

    print(f"YAML directory: {yaml_dir}")
    print(f"Output directory: {output_dir}")

    # Ensure output directory exists
    os.makedirs(output_dir, exist_ok=True)

    output_file = os.path.join(output_dir, "rmm_domains.csv")
    print(f"Output file: {output_file}")

    count = generate_csv(yaml_dir, output_file)

    print(f"Generated {count} domain entries in {output_file}")

    # Verify file exists
    if os.path.exists(output_file):
        print(f"File successfully created at {output_file}")
        print(f"File size: {os.path.getsize(output_file)} bytes")
    else:
        print(f"Error: File not created at {output_file}")

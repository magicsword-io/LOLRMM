#!/usr/bin/env python3

"""Extract RMM domains from YAML files and generate a CSV export.

This module reads all YAML files from the LOLRMM data directory and extracts
network artifacts (domains) for use by detection rules, threat intelligence
systems, and security automation platforms.

Functionality:
    - Parse all YAML RMM tool definitions
    - Extract network artifacts (domains) from structured data
    - Deduplicate and validate domain entries
    - Export to CSV format for downstream tools
    - Map domains to RMM tool names for context

Usage:
    python generate_domains_csv.py

Output:
    website/public/api/rmm_domains.csv (URI, RMM_Tool columns)

Examples:
    Generate RMM domains CSV:
        python generate_domains_csv.py
"""

import os
import yaml
import csv
import glob
import re
import sys
from pathlib import Path
from typing import List, Tuple, Dict, Optional, Any


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


def clean_tool_name(filename: str) -> str:
    """Extract and normalize tool name from YAML filename.
    
    Removes file extensions, paths, and special characters to create
    a human-readable tool identifier.
    
    Args:
        filename: Path to the YAML file.
        
    Returns:
        Cleaned tool name with special characters removed.
        
    Example:
        "anydesk_windows_(commercial).yaml" → "anydesk windows commercial"
    """
    # Remove file extension and path
    name = os.path.basename(filename).rsplit(".", 1)[0]
    
    # Remove parentheses and underscores, replace with spaces
    name = re.sub(r"[_()]", " ", name)
    
    # Clean up consecutive spaces
    name = re.sub(r"\s+", " ", name)
    
    return name.strip()


def extract_domains(yaml_file_path: str) -> List[Tuple[str, str]]:
    """Extract network domains from a YAML RMM tool definition.
    
    Parses the YAML structure looking for network artifacts under
    Artifacts > Network > Domains, extracting domain values and
    associating them with the tool name.
    
    Args:
        yaml_file_path: Absolute path to the YAML file.
        
    Returns:
        List of (domain, tool_name) tuples. Empty list if no domains found
        or if file cannot be parsed.
        
    Raises:
        No exceptions raised - errors are logged and empty list returned
        to allow batch processing to continue.
    """
    try:
        with open(yaml_file_path, "r", encoding="utf-8") as file:
            data = yaml.safe_load(file)
        
        if not isinstance(data, dict):
            print(f"Warning: Invalid YAML structure in {yaml_file_path}")
            return []

        # Get the tool name from YAML Name field, fall back to filename
        tool_name = data.get("Name", clean_tool_name(yaml_file_path))
        if not isinstance(tool_name, str):
            tool_name = clean_tool_name(yaml_file_path)

        # Extract domains from nested structure: Artifacts > Network > Domains
        domains: List[Tuple[str, str]] = []
        artifacts = data.get("Artifacts", {})
        
        if not isinstance(artifacts, dict):
            return domains
            
        network_list = artifacts.get("Network", [])
        if not isinstance(network_list, list):
            return domains

        for network_item in network_list:
            if not isinstance(network_item, dict):
                continue
                
            domain_list = network_item.get("Domains", [])
            if not isinstance(domain_list, list):
                continue

            for domain in domain_list:
                # Only add valid, non-placeholder domains
                if domain and isinstance(domain, str) and domain != "user_managed":
                    domains.append((domain, tool_name))

        return domains
        
    except (yaml.YAMLError, IOError) as e:
        print(f"Warning: Failed to parse {yaml_file_path}: {e}")
        return []


def generate_csv(yaml_dir: str, output_file: str) -> int:
    """Generate CSV file with RMM domains from all YAML files.
    
    Scans the YAML directory for all RMM tool definitions, extracts
    network artifacts, deduplicates, and writes to CSV format.
    
    Args:
        yaml_dir: Directory containing YAML RMM tool definitions.
        output_file: Path to output CSV file.
        
    Returns:
        Count of domain entries written to CSV.
        
    Raises:
        FileNotFoundError: If yaml_dir does not exist.
        OSError: If output file cannot be written.
        csv.Error: If CSV writing fails.
    """
    if not os.path.isdir(yaml_dir):
        raise FileNotFoundError(f"YAML directory not found: {yaml_dir}")

    yaml_files = glob.glob(os.path.join(yaml_dir, "*.y*ml"))
    if not yaml_files:
        raise FileNotFoundError(f"No YAML files found in {yaml_dir}")
    
    print(f"Found {len(yaml_files)} YAML files in {yaml_dir}")

    # Extract domains from all YAML files
    all_domains: Dict[str, str] = {}  # Use dict to deduplicate while preserving order
    
    for yaml_file in yaml_files:
        domains = extract_domains(yaml_file)
        for domain, tool in domains:
            # Keep first occurrence if duplicate domain from different tools
            if domain not in all_domains:
                all_domains[domain] = tool

    # Sort for consistency
    sorted_domains = sorted(all_domains.items())

    # Write to CSV file
    try:
        output_dir = os.path.dirname(output_file)
        if output_dir:
            _ensure_dir_exists(output_dir)
            
        with open(output_file, "w", newline="", encoding="utf-8") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(["URI", "RMM_Tool"])
            for domain, tool in sorted_domains:
                writer.writerow([domain, tool])
                
    except (IOError, csv.Error) as e:
        raise OSError(f"Failed to write CSV file {output_file}: {e}") from e

    print(f"Generated CSV file with {len(sorted_domains)} domains at {output_file}")
    return len(sorted_domains)


def main() -> None:
    """Main entry point for RMM domains CSV generation.
    
    Orchestrates extraction of network artifacts from YAML files and
    exports to CSV format for consumption by detection and threat
    intelligence systems.
    
    Exits with status 1 on fatal errors, 0 on success.
    """
    try:
        base_dir = _resolve_base_dir()
        yaml_dir = os.path.join(base_dir, "yaml")
        output_dir = os.path.join(base_dir, "website", "public", "api")

        print(f"YAML directory: {yaml_dir}")
        print(f"Output directory: {output_dir}")
        print()

        output_file = os.path.join(output_dir, "rmm_domains.csv")
        
        count = generate_csv(yaml_dir, output_file)
        
        # Verify output
        if os.path.exists(output_file):
            file_size = os.path.getsize(output_file)
            print(f"✓ File successfully created at {output_file}")
            print(f"✓ File size: {file_size} bytes")
        else:
            raise OSError(f"File not created at {output_file}")
            
    except (FileNotFoundError, OSError, csv.Error, yaml.YAMLError) as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()

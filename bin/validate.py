#!/usr/bin/python

"""Validates YAML files in a directory against a JSON schema.

This module provides comprehensive validation of LOLRMM YAML files against
a JSON schema specification, with additional checks for data quality, format
consistency, and logical integrity.

Functionality:
    - JSON schema validation (Draft 7)
    - Hash length validation (MD5, SHA1, SHA256)
    - Network artifact structure validation
    - Date format and chronology validation
    - URL format validation
    - Duplicate detection checking
    - Port number range validation
    - Required field checking

Usage:
    python validate.py [--yaml_dir PATH] [--schema_file PATH] [--verbose]

Example:
    python validate.py --yaml_dir yaml/ --schema_file bin/spec/lolrmm.spec.json --verbose
"""

import glob
import json
import jsonschema
import yaml
import sys
import argparse
from pathlib import Path
from os import path, walk
import datetime
from typing import Dict, List, Tuple, Optional, Any, Callable


def check_hash_lengths(object: Dict[str, Any]) -> Optional[str]:
    """Validate MD5, SHA1, and SHA256 hash lengths in KnownVulnerableSamples.
    
    Verifies that all hash values have correct hex string lengths:
    - MD5: exactly 32 characters
    - SHA1: exactly 40 characters
    - SHA256: exactly 64 characters
    
    Args:
        object: RMM tool YAML object (must contain 'KnownVulnerableSamples' if hashes present)
        
    Returns:
        Error message if hash validation fails, None if all hashes are valid
        
    Raises:
        None - returns error message string instead
    """
    if not isinstance(object, dict):
        return None
        
    hash_specs: Dict[str, int] = {"MD5": 32, "SHA1": 40, "SHA256": 64}
    name: str = object.get("Name", "Unknown")
    
    known_vulnerable_samples: List[Any] = object.get("KnownVulnerableSamples", [])
    if not isinstance(known_vulnerable_samples, list):
        return f"ERROR: KnownVulnerableSamples must be a list for object: {name}"
    
    for idx, sample in enumerate(known_vulnerable_samples):
        if not isinstance(sample, dict):
            continue
            
        for hash_type, expected_len in hash_specs.items():
            hash_value: str = sample.get(hash_type, "")
            if hash_value and len(hash_value) != expected_len:
                return (f"ERROR: {hash_type} hash has invalid length ({len(hash_value)} chars, expected {expected_len}) "
                        f"in sample {idx} of object: {name}")
    return None


def check_network_structure(object: Dict[str, Any]) -> Optional[str]:
    """Validate structure and required fields in Network artifacts.
    
    Ensures that each network artifact entry has proper structure:
    - Must be a dictionary (not string or other type)
    - Must have 'Description' field (non-empty string)
    - Must have 'Domains' field (list of domain strings)
    - Must have 'Ports' field (list of port numbers/ranges)
    
    Args:
        object: RMM tool YAML object (must contain 'Artifacts.Network' if present)
        
    Returns:
        Error message if network structure is invalid, None if valid
    """
    if not isinstance(object, dict):
        return None
        
    name: str = object.get("Name", "Unknown")
    artifacts: Dict[str, Any] = object.get("Artifacts", {})
    
    if not isinstance(artifacts, dict):
        return f"ERROR: Artifacts must be a dictionary for object: {name}"
    
    network: List[Any] = artifacts.get("Network", [])
    
    if not isinstance(network, list):
        return f"ERROR: Network artifacts must be a list for object: {name}"
    
    for idx, item in enumerate(network):
        if not isinstance(item, dict):
            return f"ERROR: Network item #{idx} is not a dictionary for object: {name}"
        
        if "Description" not in item or not item.get("Description"):
            return f"ERROR: Network item #{idx} is missing required 'Description' field for object: {name}"
        
        if "Domains" not in item:
            return f"ERROR: Network item #{idx} is missing required 'Domains' field for object: {name}"
        
        if not isinstance(item["Domains"], list):
            return f"ERROR: Network item #{idx} 'Domains' field must be a list for object: {name}"
        
        if "Ports" not in item:
            return f"ERROR: Network item #{idx} is missing required 'Ports' field for object: {name}"
        
        if not isinstance(item["Ports"], list):
            return f"ERROR: Network item #{idx} 'Ports' field must be a list for object: {name}"
    
    return None


def check_date_iso8601(object: Dict[str, Any], filename: str) -> Optional[str]:
    """Validate ISO 8601 format for Created and LastModified fields.
    
    Verifies that date fields use valid ISO 8601 format (YYYY-MM-DD or with time).
    Examples: '2024-01-15', '2024-01-15T10:30:00', '2024-01-15T10:30:00Z'
    
    Args:
        object: RMM tool YAML object containing date fields
        filename: Path to the YAML file (for error messages)
        
    Returns:
        Error message if date format is invalid, None if all dates are valid
    """
    if not isinstance(object, dict):
        return None
        
    name: str = object.get("Name", "Unknown")
    date_fields: List[str] = ["Created", "LastModified"]

    for field in date_fields:
        date_value: Optional[str] = object.get(field)
        if date_value:
            try:
                datetime.datetime.fromisoformat(date_value)
            except (ValueError, TypeError) as e:
                return (f"ERROR: {field} field has invalid ISO 8601 format in file {filename}: "
                        f"'{date_value}' (object: {name})")
    return None


def check_date_chronology(object: Dict[str, Any], filename: str) -> Optional[str]:
    """Validate that LastModified is equal to or newer than Created.
    
    Ensures logical consistency in date fields. The LastModified date should
    never be before the Created date, as an object cannot be modified before
    it was created.
    
    Args:
        object: RMM tool YAML object containing Created and LastModified
        filename: Path to the YAML file (for error messages)
        
    Returns:
        Error message if chronology is violated, None if valid
    """
    if not isinstance(object, dict):
        return None
        
    name: str = object.get("Name", "Unknown")
    created: Optional[str] = object.get("Created")
    last_modified: Optional[str] = object.get("LastModified")

    # Both dates must be present and valid for comparison
    if created and last_modified:
        try:
            created_date: datetime.datetime = datetime.datetime.fromisoformat(created)
            modified_date: datetime.datetime = datetime.datetime.fromisoformat(last_modified)

            if modified_date < created_date:
                return (f"ERROR: LastModified ({last_modified}) is older than Created ({created}) "
                        f"in file {filename} (object: {name})")
        except (ValueError, TypeError):
            # If dates are invalid, they'll be caught by check_date_iso8601
            pass

    return None


def check_url_format(object: Dict[str, Any], filename: str) -> Optional[str]:
    """Validate URL format in various fields (Website, References).
    
    Ensures all URLs start with 'http://' or 'https://'. Validates:
    - Details.Website field
    - All References[] entries
    
    Args:
        object: RMM tool YAML object containing URLs
        filename: Path to the YAML file (for error messages)
        
    Returns:
        Error message if any URLs are invalid, None if all are valid
    """
    if not isinstance(object, dict):
        return None
        
    name: str = object.get("Name", "Unknown")
    invalid_urls: List[str] = []

    def validate_url(url: Optional[str], url_type: str) -> None:
        """Validate a single URL and add to invalid_urls if needed.
        
        Args:
            url: URL string to validate
            url_type: Description of URL type (for error messages)
        """
        if url and not isinstance(url, str):
            return
        if url and not (url.startswith("http://") or url.startswith("https://")):
            invalid_urls.append(f"  - {url_type}: '{url}'")

    # Check Website URL
    details: Dict[str, Any] = object.get("Details", {})
    if isinstance(details, dict):
        website: Optional[str] = details.get("Website")
        validate_url(website, "Website")

    # Check References URLs
    references: List[Any] = object.get("References", [])
    if isinstance(references, list):
        for idx, ref in enumerate(references, 1):
            if isinstance(ref, str):
                validate_url(ref, f"Reference #{idx}")

    # Return consolidated error message if any invalid URLs found
    if invalid_urls:
        urls_str: str = "\n".join(invalid_urls)
        return (f"ERROR: Invalid URL format(s) in file {filename} (object: {name}):\n{urls_str}\n"
                f"  URLs must start with http:// or https://")

    return None


def check_duplicate_detections(object: Dict[str, Any], filename: str) -> Optional[str]:
    """Check for duplicate detection entries.
    
    Ensures that no detection rule is referenced multiple times within
    the same RMM tool's detection list. Checks both 'Sigma' and 'Link' fields.
    
    Args:
        object: RMM tool YAML object containing Detections
        filename: Path to the YAML file (for error messages)
        
    Returns:
        Error message if duplicates found, None if all unique
    """
    if not isinstance(object, dict):
        return None
        
    name: str = object.get("Name", "Unknown")
    detections: List[Any] = object.get("Detections", [])

    if not detections or not isinstance(detections, list):
        return None

    seen_links: Dict[str, int] = {}
    for idx, detection in enumerate(detections):
        if not isinstance(detection, dict):
            continue

        # Check for Sigma/Link field (both are used)
        link: Optional[str] = detection.get("Sigma") or detection.get("Link")
        if link:
            if link in seen_links:
                return (f"ERROR: Duplicate detection link found in file {filename}: '{link}' "
                        f"(appears in items #{seen_links[link]} and #{idx}) (object: {name})")
            seen_links[link] = idx

    return None


def check_port_format(object: Dict[str, Any], filename: str) -> Optional[str]:
    """Validate port numbers in Network artifacts.
    
    Checks that port numbers fall within valid range (0-65535). Port values
    can be:
    - Integers: Must be 0-65535
    - Numeric strings: Must parse to 0-65535 when converted
    - Port ranges: "80-443", "8080-8090", etc. (accepted as-is)
    - Special values: "any" (accepted as-is)
    
    Args:
        object: RMM tool YAML object containing network artifacts
        filename: Path to the YAML file (for error messages)
        
    Returns:
        Error message if port is invalid, None if all valid
    """
    if not isinstance(object, dict):
        return None
        
    name: str = object.get("Name", "Unknown")
    artifacts: Dict[str, Any] = object.get("Artifacts", {})
    
    if not isinstance(artifacts, dict):
        return None
        
    network: List[Any] = artifacts.get("Network", [])
    
    if not isinstance(network, list):
        return None

    for item in network:
        if not isinstance(item, dict):
            continue

        ports: List[Any] = item.get("Ports", [])
        if not isinstance(ports, list):
            continue
            
        for port in ports:
            # Port can be integer, numeric string, or special strings
            if isinstance(port, int):
                if port < 0 or port > 65535:
                    return (f"ERROR: Invalid port number {port} in file {filename}. "
                            f"Must be between 0-65535 (object: {name})")
            elif isinstance(port, str):
                # Try to parse if it's a numeric string
                try:
                    port_num: int = int(port)
                    if port_num < 0 or port_num > 65535:
                        return (f"ERROR: Invalid port number {port} in file {filename}. "
                                f"Must be between 0-65535 (object: {name})")
                except ValueError:
                    # It's a string like "80-443" or "any", which is acceptable
                    pass

    return None


def check_required_fields(object: Dict[str, Any], filename: str) -> Optional[str]:
    """Check for important fields that should be present.
    
    Validates that commonly-required fields are populated. Returns warnings
    (not errors) for missing fields, as these may be intentional gaps.
    
    Fields checked:
    - Category: Should indicate RMM type
    - Created: Should have creation date
    
    Args:
        object: RMM tool YAML object to check
        filename: Path to the YAML file (for error messages)
        
    Returns:
        Warning message if fields are missing, None if all present
    """
    if not isinstance(object, dict):
        return None
        
    name: str = object.get("Name", "Unknown")
    warnings: List[str] = []

    # Check if Category is missing
    category: Optional[str] = object.get("Category")
    if not category or not isinstance(category, str):
        warnings.append(
            f"WARNING: Category field is missing or empty in file {filename} (object: {name})"
        )

    # Check if Created date is missing
    created: Optional[str] = object.get("Created")
    if not created or not isinstance(created, str):
        warnings.append(
            f"WARNING: Created date is missing in file {filename} (object: {name})"
        )

    return warnings[0] if warnings else None


def validate_schema(yaml_dir: str, schema_file: str, verbose: bool) -> Tuple[bool, List[str]]:
    """Validate YAML files against schema and perform additional checks.
    
    Comprehensive validation of all RMM tool YAML files including:
    - JSON schema validation (Draft 7)
    - Additional data quality checks
    - Format and consistency validation
    
    Args:
        yaml_dir: Directory containing YAML files to validate
        schema_file: Path to JSON schema specification file
        verbose: If True, print detailed processing information
        
    Returns:
        Tuple of (has_errors: bool, error_messages: List[str])
        - has_errors: True if any ERROR-level issues found
        - error_messages: List of all error/warning messages
        
    Raises:
        None - all errors returned in error_messages list
    """
    error: bool = False
    errors: List[str] = []

    # Load schema file
    try:
        with open(schema_file, "rb") as f:
            schema: Dict[str, Any] = json.load(f)
    except FileNotFoundError:
        return True, [f"ERROR: Schema file not found: {schema_file}"]
    except json.JSONDecodeError as exc:
        return True, [f"ERROR: Failed to parse schema file {schema_file}: {exc}"]
    except IOError as exc:
        return True, [f"ERROR: Failed to read schema file {schema_file}: {exc}"]

    # Collect all YAML files to validate
    yaml_files: List[str] = glob.glob(f"{yaml_dir}/*.yaml") + glob.glob(f"{yaml_dir}/*.yml")
    
    if not yaml_files:
        return False, ["WARNING: No YAML files found in {0}".format(yaml_dir)]

    if verbose:
        print(f"Validating {len(yaml_files)} YAML files against schema: {schema_file}")

    # Validate each YAML file
    for yaml_file in yaml_files:
        if verbose:
            print(f"  Processing: {yaml_file}")

        # Load YAML file
        try:
            with open(yaml_file, "r") as stream:
                yaml_data: Optional[Dict[str, Any]] = yaml.safe_load(stream)
        except yaml.YAMLError as exc:
            errors.append(f"ERROR: Failed to parse YAML file {yaml_file}: {exc}")
            error = True
            continue
        except (IOError, OSError) as exc:
            errors.append(f"ERROR: Failed to read YAML file {yaml_file}: {exc}")
            error = True
            continue

        if yaml_data is None:
            errors.append(f"ERROR: YAML file is empty: {yaml_file}")
            error = True
            continue

        if not isinstance(yaml_data, dict):
            errors.append(f"ERROR: YAML root must be an object/dictionary: {yaml_file}")
            error = True
            continue

        # Schema validation
        validator: jsonschema.Draft7Validator = jsonschema.Draft7Validator(
            schema, format_checker=jsonschema.FormatChecker()
        )
        for schema_error in validator.iter_errors(yaml_data):
            error_path: str = ".".join(str(p) for p in schema_error.path) or "root"
            errors.append(
                f"ERROR: Schema validation failed at {error_path} in {yaml_file}: {schema_error.message}"
            )
            error = True

        # Additional YAML checks (data quality)
        check_functions: List[Tuple[Callable, ...]] = [
            (check_hash_lengths, yaml_data),
            (check_network_structure, yaml_data),
            (check_date_iso8601, yaml_data, yaml_file),
            (check_date_chronology, yaml_data, yaml_file),
            (check_url_format, yaml_data, yaml_file),
            (check_duplicate_detections, yaml_data, yaml_file),
            (check_port_format, yaml_data, yaml_file),
            (check_required_fields, yaml_data, yaml_file),
        ]

        for check_func, *args in check_functions:
            check_error: Optional[str] = check_func(*args)
            if check_error:
                errors.append(check_error)
                # Only set error flag for ERROR messages, not WARNING
                if check_error.startswith("ERROR"):
                    error = True

    return error, errors


def main(yaml_dir: str, schema_file: str, verbose: bool) -> int:
    """Main entry point for schema validation.
    
    Orchestrates the validation process and handles output/exit codes.
    
    Args:
        yaml_dir: Directory containing YAML files to validate
        schema_file: Path to JSON schema specification
        verbose: If True, print detailed processing information
        
    Returns:
        Exit code: 0 if successful, 1 if errors found
    """
    error, errors = validate_schema(yaml_dir, schema_file, verbose)

    # Print all messages
    for err in errors:
        print(err)

    # Print summary
    if error:
        print("\n✗ Validation failed - errors found")
        return 1
    else:
        print("\n✓ Validation passed - no errors found")
        return 0


if __name__ == "__main__":
    parser: argparse.ArgumentParser = argparse.ArgumentParser(
        description="Validates YAML files in a directory against a JSON schema",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python validate.py
  python validate.py --yaml_dir yaml/ --schema_file bin/spec/lolrmm.spec.json
  python validate.py --yaml_dir yaml/ --verbose
        """
    )
    parser.add_argument(
        "-y",
        "--yaml_dir",
        default="yaml/",
        help="path to the directory containing YAML files (default: yaml/)",
    )
    parser.add_argument(
        "-s",
        "--schema_file",
        default="bin/spec/lolrmm.spec.json",
        help="path to the JSON schema file (default: bin/spec/lolrmm.spec.json)",
    )
    parser.add_argument(
        "-v",
        "--verbose",
        required=False,
        action="store_true",
        help="print detailed processing information",
    )
    
    args: argparse.Namespace = parser.parse_args()
    
    exit_code: int = main(args.yaml_dir, args.schema_file, args.verbose)
    sys.exit(exit_code)

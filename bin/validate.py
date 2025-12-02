#!/usr/bin/python

"""
Validates YAML files in a directory against a JSON schema.
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


def check_hash_lengths(object):
    """Validate hash lengths for MD5, SHA1, and SHA256."""
    hash_specs = {"MD5": 32, "SHA1": 40, "SHA256": 64}

    known_vulnerable_samples = object.get("KnownVulnerableSamples", [])
    for sample in known_vulnerable_samples:
        for hash_type, expected_len in hash_specs.items():
            hash_value = sample.get(hash_type, "")
            if hash_value and len(hash_value) != expected_len:
                return f"ERROR: {hash_type} length is not {expected_len} characters for object: {object['Id']}"
    return None


def check_network_structure(object):
    artifacts = object.get("Artifacts", {})
    network = artifacts.get("Network", [])
    for item in network:
        if not isinstance(item, dict):
            return (
                f"ERROR: Network item is not a dictionary for object: {object['Name']}"
            )
        if "Description" not in item:
            return f"ERROR: Network item is missing 'Description' for object: {object['Name']}"
        if "Domains" not in item:
            return (
                f"ERROR: Network item is missing 'Domains' for object: {object['Name']}"
            )
        if not isinstance(item["Domains"], list):
            return f"ERROR: 'Domains' is not a list for object: {object['Name']}"
        if "Ports" not in item:
            return (
                f"ERROR: Network item is missing 'Ports' for object: {object['Name']}"
            )
        if not isinstance(item["Ports"], list):
            return f"ERROR: 'Ports' is not a list for object: {object['Name']}"
    return None


def check_date_iso8601(object, filename):
    """Validate ISO 8601 format for Created and LastModified fields."""
    date_fields = ["Created", "LastModified"]

    for field in date_fields:
        date_value = object.get(field)
        if date_value:
            try:
                datetime.datetime.fromisoformat(date_value)
            except ValueError:
                return f"ERROR: {field} field is not valid ISO 8601 format in file {filename}: '{date_value}' (object: {object.get('Name', 'Unknown')})"
    return None


def check_date_chronology(object, filename):
    """Validate that LastModified is equal to or newer than Created."""
    name = object.get("Name", "Unknown")
    created = object.get("Created")
    last_modified = object.get("LastModified")

    # Both dates must be present and valid for comparison
    if created and last_modified:
        try:
            created_date = datetime.datetime.fromisoformat(created)
            modified_date = datetime.datetime.fromisoformat(last_modified)

            if modified_date < created_date:
                return f"ERROR: LastModified ({last_modified}) is older than Created ({created}) in file {filename} (object: {name})"
        except ValueError:
            # If dates are invalid, they'll be caught by check_date_iso8601
            pass

    return None


def check_url_format(object, filename):
    """Validate URL format in various fields."""
    name = object.get("Name", "Unknown")
    invalid_urls = []

    def validate_url(url, url_type):
        """Helper function to validate a single URL."""
        if url and not (url.startswith("http://") or url.startswith("https://")):
            invalid_urls.append(f"  - {url_type}: '{url}'")

    # Check Website URL
    website = object.get("Details", {}).get("Website")
    validate_url(website, "Website")

    # Check References URLs
    references = object.get("References", [])
    if references:
        for idx, ref in enumerate(references, 1):
            validate_url(ref, f"Reference #{idx}")

    # Return consolidated error message if any invalid URLs found
    if invalid_urls:
        urls_str = "\n".join(invalid_urls)
        return f"ERROR: Invalid URL format(s) in file {filename} (object: {name}):\n{urls_str}\n  URLs must start with http:// or https://"

    return None


def check_duplicate_detections(object, filename):
    """Check for duplicate detection entries."""
    name = object.get("Name", "Unknown")
    detections = object.get("Detections", [])

    if not detections:
        return None

    seen_links = {}
    for idx, detection in enumerate(detections):
        if not isinstance(detection, dict):
            continue

        # Check for Sigma/Link field (both are used)
        link = detection.get("Sigma") or detection.get("Link")
        if link:
            if link in seen_links:
                return f"ERROR: Duplicate detection link found in file {filename}: '{link}' (object: {name})"
            seen_links[link] = idx

    return None


def check_port_format(object, filename):
    """Validate port numbers in Network artifacts."""
    name = object.get("Name", "Unknown")
    artifacts = object.get("Artifacts", {})
    network = artifacts.get("Network", [])

    for item in network:
        if not isinstance(item, dict):
            continue

        ports = item.get("Ports", [])
        for port in ports:
            # Port can be string or integer according to spec
            if isinstance(port, int):
                if port < 0 or port > 65535:
                    return f"ERROR: Invalid port number {port} in file {filename}. Must be between 0-65535 (object: {name})"
            elif isinstance(port, str):
                # Try to parse if it's a numeric string
                try:
                    port_num = int(port)
                    if port_num < 0 or port_num > 65535:
                        return f"ERROR: Invalid port number {port} in file {filename}. Must be between 0-65535 (object: {name})"
                except ValueError:
                    # It's a string like "80-443" or "any", which is acceptable
                    pass

    return None


def check_required_fields(object, filename):
    """Check for important fields that should be present."""
    name = object.get("Name", "Unknown")
    warnings = []

    # Check if Category is missing
    if not object.get("Category"):
        warnings.append(
            f"WARNING: Category field is missing or empty in file {filename} (object: {name})"
        )

    # Check if Created date is missing
    if not object.get("Created"):
        warnings.append(
            f"WARNING: Created date is missing in file {filename} (object: {name})"
        )

    # Check if Website is missing
    # if not object.get('Details', {}).get('Website'):
    #    warnings.append(f"WARNING: Website is missing in Details section in file {filename} (object: {name})")
    #
    return warnings[0] if warnings else None


def validate_schema(yaml_dir, schema_file, verbose):
    """Validate YAML files against schema and perform additional checks."""
    error = False
    errors = []

    try:
        with open(schema_file, "rb") as f:
            schema = json.load(f)
    except IOError:
        print(f"ERROR: reading schema file {schema_file}")
        return True, [f"ERROR: reading schema file {schema_file}"]

    yaml_files = glob.glob(f"{yaml_dir}/*.yaml") + glob.glob(f"{yaml_dir}/*.yml")

    for yaml_file in yaml_files:
        if verbose:
            print("processing YAML file {0}".format(yaml_file))

        with open(yaml_file, "r") as stream:
            try:
                yaml_data = yaml.safe_load(stream)
            except yaml.YAMLError as exc:
                print(exc)
                print("Error reading {0}".format(yaml_file))
                errors.append("ERROR: Error reading {0}".format(yaml_file))
                error = True
                continue

        validator = jsonschema.Draft7Validator(
            schema, format_checker=jsonschema.FormatChecker()
        )
        for schema_error in validator.iter_errors(yaml_data):
            errors.append(
                f"ERROR: {json.dumps(schema_error.message)} at file {yaml_file}:\n\t{schema_error.path}"
            )
            error = True

        # Additional YAML checks
        check_functions = [
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
            check_error = check_func(*args)
            if check_error:
                errors.append(check_error)
                # Only set error flag for ERROR messages, not WARNING
                if check_error.startswith("ERROR"):
                    error = True

    return error, errors


def main(yaml_dir, schema_file, verbose):

    error, errors = validate_schema(yaml_dir, schema_file, verbose)

    for err in errors:
        print(err)

    if error:
        sys.exit("Errors found")
    else:
        print("No Errors found")


if __name__ == "__main__":
    # grab arguments
    parser = argparse.ArgumentParser(
        description="Validates YAML files in a directory against a JSON schema"
    )
    parser.add_argument(
        "-y",
        "--yaml_dir",
        default="yaml/",
        help="path to the directory containing YAML files",
    )
    parser.add_argument(
        "-s",
        "--schema_file",
        default="bin/spec/lolrmm.spec.json",
        help="path to the JSON schema file",
    )
    parser.add_argument(
        "-v",
        "--verbose",
        required=False,
        action="store_true",
        help="prints verbose output",
    )
    # parse them
    args = parser.parse_args()
    yaml_dir = args.yaml_dir
    schema_file = args.schema_file
    verbose = args.verbose

    main(yaml_dir, schema_file, verbose)

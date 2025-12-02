#!/usr/bin/env python3
# Note: This script was vibe coded and is simply intended to fix YAML formatting issues. Nothing major.

from ruamel.yaml import YAML
from pathlib import Path


def fix_indentation_manually(content):

    lines = content.split("\n")
    fixed_lines = []
    # Stack of (dash_indent, expected_continuation_indent) for nested lists
    list_stack = []
    last_key_indent = (
        None  # Track the indent of the last key that might have a list under it
    )
    # Track indent adjustments: {original_indent: adjusted_indent}
    dash_adjustments = {}

    for i, line in enumerate(lines):
        # Empty lines or comments
        if not line or not line.strip() or line.strip().startswith("#"):
            fixed_lines.append(line)
            last_key_indent = None
            continue

        stripped = line.lstrip(" ")
        leading_spaces = len(line) - len(stripped)

        # Pop from stack if we've decreased indentation below current level
        while list_stack and leading_spaces < list_stack[-1][0]:
            popped = list_stack.pop()
            # Clear adjustment tracking for this level
            if popped[0] in dash_adjustments:
                del dash_adjustments[popped[0]]

        # Check if this line starts with a dash (list item)
        if stripped.startswith("- "):
            # Check if this dash + key pattern (e.g., "- Domains:")
            # In this case, we need to track that nested lists should be adjusted
            dash_has_key = ":" in stripped[2:] and not stripped[2:].strip().startswith(
                "#"
            )

            # Check if we previously adjusted this indent level
            if leading_spaces in dash_adjustments:
                # Use the adjusted indent
                expected_dash_indent = dash_adjustments[leading_spaces]
                fixed_lines.append(" " * expected_dash_indent + stripped)
                # Update/maintain stack
                if list_stack and expected_dash_indent == list_stack[-1][0]:
                    list_stack[-1] = (expected_dash_indent, expected_dash_indent + 2)
                else:
                    list_stack.append((expected_dash_indent, expected_dash_indent + 2))
                # If this dash has a key, track it for nested lists
                if dash_has_key:
                    last_key_indent = expected_dash_indent + 2  # Key is at dash + 2
            # Check if this dash should be indented under the last key
            elif last_key_indent is not None and leading_spaces == last_key_indent + 2:
                # This dash is 2 spaces more than the last key (ruamel's offset from parent dash)
                # But it should be 4 spaces more
                expected_dash_indent = last_key_indent + 4
                fixed_lines.append(" " * expected_dash_indent + stripped)
                list_stack.append((expected_dash_indent, expected_dash_indent + 2))
                # Remember this adjustment for sibling dashes
                dash_adjustments[leading_spaces] = expected_dash_indent
                # If this dash has a key, track it for nested lists
                if dash_has_key:
                    last_key_indent = expected_dash_indent + 2
                else:
                    last_key_indent = None
            else:
                # Regular dash - keep as-is
                fixed_lines.append(line)
                # If this dash is at the same level as the top of stack, replace (sibling item)
                # Otherwise push a new level (nested item)
                if list_stack and leading_spaces == list_stack[-1][0]:
                    list_stack[-1] = (leading_spaces, leading_spaces + 2)
                else:
                    list_stack.append((leading_spaces, leading_spaces + 2))
                # If this dash has a key, track it for nested lists
                if dash_has_key:
                    last_key_indent = leading_spaces + 2  # Key is at dash + 2
                else:
                    last_key_indent = None
        # Check if we're in a list and this line should be a continuation
        elif (
            list_stack
            and leading_spaces == list_stack[-1][0]
            and not stripped.startswith("- ")
        ):
            # This line is at the dash indent level but isn't a new list item
            # It should be a continuation - indent it to expected_continuation_indent
            expected_indent = list_stack[-1][1]
            fixed_lines.append(" " * expected_indent + stripped)
            # If this line is a key (ends with :), track it for potential nested list
            if ":" in stripped and not stripped.startswith("#"):
                last_key_indent = expected_indent
        else:
            # Regular line, no adjustment needed
            fixed_lines.append(line)
            # Track if this is a key for potential nested list
            if ":" in stripped and not stripped.startswith("#"):
                last_key_indent = leading_spaces
            else:
                last_key_indent = None

    return "\n".join(fixed_lines)


def fix_yaml_file(file_path):
    """Fix formatting issues in a YAML file."""
    try:
        yaml = YAML()
        yaml.preserve_quotes = True
        yaml.default_flow_style = False
        yaml.indent(mapping=4, sequence=4, offset=4)
        yaml.width = 4096  # Prevent line wrapping

        # Read and parse
        with open(file_path, "r", encoding="utf-8") as f:
            data = yaml.load(f)

        # Write with ruamel.yaml
        from io import StringIO

        stream = StringIO()
        yaml.dump(data, stream)
        content = stream.getvalue()

        # Fix remaining indentation issues
        content = fix_indentation_manually(content)

        # Write back with LF line endings
        with open(file_path, "w", encoding="utf-8", newline="\n") as f:
            f.write(content)

        return True, None
    except Exception as e:
        return False, str(e)


def main():
    import sys

    # Check if a specific file was provided as argument
    if len(sys.argv) > 1:
        file_path = Path(sys.argv[1])
        if not file_path.exists():
            print(f"Error: File {file_path} not found")
            return

        print(f"Processing 1 file: {file_path}")
        success, error = fix_yaml_file(file_path)
        if success:
            print(f"[+] Successfully fixed {file_path}")
        else:
            print(f"[-] Error processing {file_path.name}: {error}")
        return

    # Otherwise, process all files in yaml/ directory
    yaml_dir = Path("yaml")

    if not yaml_dir.exists():
        print(f"Error: {yaml_dir} directory not found")
        return

    yaml_files = list(yaml_dir.glob("*.yaml")) + list(yaml_dir.glob("*.yml"))

    if not yaml_files:
        print(f"No YAML files found in {yaml_dir}")
        return

    print(f"Processing {len(yaml_files)} YAML files...")

    errors = []
    for yaml_file in sorted(yaml_files):
        success, error = fix_yaml_file(yaml_file)
        if not success:
            errors.append((yaml_file.name, error))
            print(f"  Error processing {yaml_file.name}: {error}")

    if errors:
        print(f"\n[-] Failed to process {len(errors)} file(s)")
    else:
        print(f"\n[+] Successfully processed all {len(yaml_files)} files")


if __name__ == "__main__":
    main()

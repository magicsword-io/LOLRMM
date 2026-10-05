"""Shared process-selector policy for catalog-generated Sigma rules."""

import ntpath
import re


# These names describe unrelated software as often as the cataloged tool.
# Keep their documented installation location instead of matching the name alone.
PATH_REQUIRED_EXECUTABLES = frozenset({"svchost.exe", "agent.exe", "installer.exe"})


def process_image_pattern(path: str, filename: str):
    """Return an endswith pattern, or None when a generic name lacks context."""
    if filename.casefold() not in PATH_REQUIRED_EXECUTABLES:
        return f"\\\\{filename}"

    path = path.strip()
    if len(path) > 1 and path[0] == path[-1] and path[0] in "\"'":
        path = path[1:-1]
    path = path.replace("/", "\\")
    directory = ntpath.dirname(path)
    _, location = ntpath.splitdrive(directory)
    # A drive letter, root separator or wildcard is not installation context.
    # Unexpanded variables/placeholders would not match raw process telemetry.
    if not re.search(r"[a-zA-Z0-9]", location) or any(c in path for c in "%<>"):
        return None
    components = {
        part.casefold() for part in location.split("\\")
        if re.search(r"[a-zA-Z0-9]", part)
    }
    if components <= {"windows", "system32", "syswow64", "sysnative"}:
        return None

    # Anchor relative directory suffixes; preserve explicit wildcard roots.
    if not ntpath.isabs(path) and not path.startswith("*"):
        path = "\\" + path
    # Sigma escaping preserves literal separators immediately before wildcards.
    return path.replace("\\", "\\\\")

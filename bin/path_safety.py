"""Reject catalog paths that become catch-all downstream file rules."""

import fnmatch
import ntpath
import re


EMPTY_VALUES = frozenset({"n/a", "na", "none", "null", "unknown", "tbd"})


def empty_selector(value):
    return (not isinstance(value, str) or not value.strip()
            or value.strip().casefold() in EMPTY_VALUES)


def metadata_path(value):
    """Human-readable substitutions must not be emitted as literal telemetry."""
    return isinstance(value, str) and re.search(r"<[^>]+>|%[^%]+%", value) is not None


# Consumers may extract just the basename from a path. A vendor directory does
# not make an extension-only executable selector safe for those consumers.
EXECUTABLE_EXTENSIONS = frozenset({
    "exe", "dll", "com", "scr", "cpl", "ocx", "sys", "msi", "msp", "mst",
    "bat", "cmd", "ps1", "psm1", "vbs", "vbe", "js", "jse", "wsf", "wsh",
    "hta", "jar", "sh", "bash", "py", "so", "dylib", "bin", "run", "app",
    "pkg", "deb", "rpm",
})


def unsafe_path_reason(value):
    """Return a reason for an open path pattern, or None for a scoped value.

    Vendor directory globs and scoped non-executable artifacts (e.g. logs) are
    useful catalog evidence. Executable globs must retain a literal filename
    component even if a downstream engine discards their directory.
    """
    if not isinstance(value, str):
        return None

    normalized = value.strip()
    if len(normalized) > 1 and normalized[0] == normalized[-1] and normalized[0] in "\"'":
        normalized = normalized[1:-1].strip()
    normalized = normalized.replace("/", "\\").rstrip("\\")
    filename = ntpath.basename(normalized).casefold()
    stem, extension = ntpath.splitext(filename)
    extension = extension.lstrip(".")
    if not re.fullmatch(r"[*?.]+", stem):
        return None

    if extension and any(fnmatch.fnmatchcase(ext, extension) for ext in EXECUTABLE_EXTENSIONS):
        return "extension-only executable wildcard can match unrelated programs when consumers extract the filename"
    if extension and re.fullmatch(r"[*?.]+", extension):
        return "catch-all file wildcard can match every file type"

    directory = ntpath.dirname(normalized)
    _, location = ntpath.splitdrive(directory)
    if not re.search(r"[a-zA-Z0-9]", location):
        return "unscoped wildcard has no tool-specific filename or directory"
    return None


def unsafe_catalog_paths(data):
    """Yield (field, value, reason) for unsafe detection-ready catalog paths."""
    if not isinstance(data, dict):
        return
    details = data.get("Details")
    if isinstance(details, dict):
        paths = details.get("InstallationPaths")
        if isinstance(paths, list):
            for idx, value in enumerate(paths):
                if reason := unsafe_path_reason(value):
                    yield f"Details.InstallationPaths[{idx}]", value, reason

    artifacts = data.get("Artifacts")
    if isinstance(artifacts, dict):
        disks = artifacts.get("Disk")
        if isinstance(disks, list):
            for idx, disk in enumerate(disks):
                if isinstance(disk, dict):
                    value = disk.get("File")
                    if reason := unsafe_path_reason(value):
                        yield f"Artifacts.Disk[{idx}].File", value, reason

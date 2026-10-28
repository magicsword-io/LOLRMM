"""Regression coverage for catch-all rules reaching downstream policy engines."""

import subprocess
import sys
import unittest
from pathlib import Path
from tempfile import TemporaryDirectory
from unittest.mock import patch

import yaml


ROOT = Path(__file__).resolve().parents[1]
with patch.object(sys, "path", [str(ROOT / "bin"), *sys.path]):
    import lint_content
    import validate


def catalog_entry(installation_paths, disk_files):
    return {
        "Name": "Example",
        "Category": "RMM",
        "Description": "Example remote management tool",
        "Created": "2026-10-26",
        "Details": {"InstallationPaths": installation_paths},
        "Artifacts": {"Disk": [{"File": value} for value in disk_files]},
    }


class PathSafetyTests(unittest.TestCase):
    def setUp(self):
        self.directory = TemporaryDirectory()
        self.addCleanup(self.directory.cleanup)
        self.source = Path(self.directory.name) / "example.yaml"

    def write_entry(self, data):
        self.source.write_text(yaml.safe_dump(data), encoding="utf-8")

    def validate_entry(self):
        return validate.validate_schema(
            self.directory.name, ROOT / "bin/spec/lolrmm.spec.json", False,
        )

    def test_both_validators_reject_open_patterns_in_both_path_fields(self):
        unsafe = [
            "*.exe", "?.exe", "**.exe", "*.dll", "*.msi", "*.bat", "*.cmd",
            "*.ps1", "*.vbs", "*.js", "*.sh", "*.so", "*.dylib", "*.jar",
            "*", "?", "*.*", "*.log", "*.*.exe", r"C:\*", r"*\*", "/*",
            r"C:\Program Files\OpsBridge\*.exe",  # Original incident.
            r"C:\Program Files\Example\?.DLL",
            r"%ProgramFiles%\Example\*.MSI",
            r"\\server\share\Example\*.exe",
            r'  "C:\Program Files\Example\*.EXE"  ',
            "'/opt/example/*.sh'", "/opt/example/*.so", "C:/Example/*.exe",
            r"C:\Example\*.ex?", r"C:\Example\*.*", r"C:\Example\*.???",
            r"C:\Example\*.*.exe",
        ]
        for value in unsafe:
            for field in ("Details.InstallationPaths[0]", "Artifacts.Disk[0].File"):
                with self.subTest(value=value, field=field):
                    self.write_entry(catalog_entry(
                        [value] if field.startswith("Details") else [],
                        [value] if field.startswith("Artifacts") else [],
                    ))
                    error, messages = self.validate_entry()
                    self.assertTrue(error)
                    self.assertTrue(any(field in message and repr(value) in message for message in messages))
                    findings = lint_content.lint_file(str(self.source))
                    self.assertTrue(any(
                        f.severity == lint_content.ERROR and f.field == field and f.value == value
                        for f in findings
                    ))

    def test_scoped_patterns_and_verified_filenames_pass(self):
        safe = [
            "OpsBridgeAgent.exe", r"C:\Program Files\OpsBridge\OpsBridgeAgent.exe",
            r"C:\Program Files\Example\Example*.exe", "*AnyDesk*.exe",
            r"C:\Users\*\AppData\Local\Example\Example.exe",
            r"C:\ProgramData\OpsBridge\*", "/opt/example/*",
            r"C:\ProgramData\Example\*.log", r"C:\ProgramData\Example\task_*.json",
            "/opt/example/agent", "/var/log/example/*.log",
        ]
        self.write_entry(catalog_entry(safe, safe))
        error, messages = self.validate_entry()
        self.assertFalse(error, messages)
        self.assertEqual(lint_content.lint_file(str(self.source)), [])

    def test_optional_null_fields_pass(self):
        self.write_entry({
            "Name": "Example", "Category": "RMM", "Description": "Example",
            "Created": "2026-10-26", "Details": {"InstallationPaths": None},
            "Artifacts": {"Disk": None},
        })
        error, messages = self.validate_entry()
        self.assertFalse(error, messages)
        self.assertEqual(lint_content.lint_file(str(self.source)), [])

    def test_cli_fails_with_actionable_errors_and_passes_after_correction(self):
        # Check the actual CI entry points, both YAML suffixes, and all findings.
        for suffix in (".yaml", ".yml"):
            self.source = self.source.with_suffix(suffix)
            commands = [
                [sys.executable, str(ROOT / "bin/validate.py"), "-y", self.directory.name,
                 "-s", str(ROOT / "bin/spec/lolrmm.spec.json")],
                [sys.executable, str(ROOT / "bin/lint_content.py"), "-y", self.directory.name],
            ]
            self.write_entry(catalog_entry(["*.exe"], [r"C:\OpsBridge\*.exe", "*.*"]))
            for command in commands:
                with self.subTest(suffix=suffix, script=command[1]):
                    result = subprocess.run(command, capture_output=True, text=True)
                    self.assertEqual(result.returncode, 1, result.stdout + result.stderr)
                    output = result.stdout + result.stderr
                    for expected in (str(self.source), "Details.InstallationPaths[0]",
                                     "Artifacts.Disk[0].File", "Artifacts.Disk[1].File",
                                     "*.exe", "*.*", "tool-specific"):
                        self.assertIn(expected, output)
            self.write_entry(catalog_entry(["OpsBridgeAgent.exe"], ["OpsBridgeAgent.exe"]))
            for command in commands:
                result = subprocess.run(command, capture_output=True, text=True)
                self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
            self.source.unlink()


if __name__ == "__main__":
    unittest.main()

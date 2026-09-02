"""Focused regression tests for the Sigma rule generator."""

from __future__ import annotations

import copy
import importlib.util
import io
from contextlib import redirect_stdout
from pathlib import Path
from tempfile import TemporaryDirectory
import unittest
from unittest.mock import patch

import yaml


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("sigma_gen", ROOT / "bin" / "sigma-gen.py")
assert SPEC and SPEC.loader
sigma_gen = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(sigma_gen)


def sample_rule() -> dict:
    return {
        "title": "Potential Example RMM Tool Process Activity",
        "id": "11111111-1111-1111-1111-111111111111",
        "status": "experimental",
        "description": "Detects example process activity",
        "references": ["https://github.com/magicsword-io/LOLRMM"],
        "author": "LOLRMM Project",
        "date": "2020-01-01",
        "tags": ["attack.command-and-control", "attack.t1219"],
        "logsource": {"product": "windows", "category": "process_creation"},
        "detection": {
            "selection": {"Image|endswith": ["\\\\example.exe"]},
            "condition": "selection",
        },
        "falsepositives": ["Legitimate use of Example"],
        "level": "medium",
    }


class SigmaGeneratorTests(unittest.TestCase):
    def test_anchors_ordinary_filename_with_escaped_separator(self) -> None:
        artifacts = sigma_gen.extract_artifacts(
            {"Details": {"InstallationPaths": [r"C:\Program Files\Example\rd.exe"]}}
        )

        self.assertEqual(artifacts["processes"], [r"\\rd.exe"])

    def test_anchors_leading_wildcard_filename_with_escaped_separator(self) -> None:
        artifacts = sigma_gen.extract_artifacts(
            {"Details": {"InstallationPaths": [r"C:\Program Files\Example\*.exe"]}}
        )

        self.assertEqual(artifacts["processes"], [r"\\*.exe"])

    def test_anchors_embedded_wildcard_filename_with_escaped_separator(self) -> None:
        artifacts = sigma_gen.extract_artifacts(
            {"Details": {"InstallationPaths": [r"C:\Program Files\RuDesktop\rudesktop*.exe"]}}
        )

        self.assertEqual(artifacts["processes"], [r"\\rudesktop*.exe"])

    def test_deduplicates_case_insensitively_and_preserves_first_spelling(self) -> None:
        values = ["Example.EXE", "example.exe", "EXAMPLE.exe", "Other.exe"]

        self.assertEqual(sigma_gen.dedupe(values), ["Example.EXE", "Other.exe"])

    def test_generated_rules_use_remote_access_attack_tags(self) -> None:
        with TemporaryDirectory() as directory:
            root = Path(directory)
            source = root / "tool.yaml"
            source.write_text(
                yaml.safe_dump(
                    {
                        "Name": "Example Tool",
                        "Artifacts": {"Network": [{"Domains": ["example.test"]}]},
                        "Details": {"InstallationPaths": [r"C:\Tools\example.exe"]},
                    },
                    sort_keys=False,
                ),
                encoding="utf-8",
            )
            sigma_gen.generate_sigma_rules(str(source), str(root))

            for rule_path in root.glob("*_sigma.yml"):
                rule = yaml.safe_load(rule_path.read_text(encoding="utf-8"))
                self.assertEqual(
                    rule["tags"], ["attack.command-and-control", "attack.t1219"]
                )
                self.assertNotIn("attack.execution", rule["tags"])

    def test_unchanged_rule_is_not_rewritten(self) -> None:
        rule = sample_rule()
        with TemporaryDirectory() as directory:
            rule_path = Path(directory) / "rule.yml"
            sigma_gen.write_sigma_rule(rule, str(rule_path))

            with patch.object(sigma_gen, "write_sigma_rule") as write_rule:
                sigma_gen.write_sigma_rule_if_changed(copy.deepcopy(rule), str(rule_path))

            write_rule.assert_not_called()

    def test_semantic_change_preserves_identity_and_updates_modified(self) -> None:
        original = sample_rule()
        with TemporaryDirectory() as directory:
            rule_path = Path(directory) / "rule.yml"
            sigma_gen.write_sigma_rule(original, str(rule_path))

            changed = copy.deepcopy(original)
            changed["id"] = "22222222-2222-2222-2222-222222222222"
            changed["date"] = "2026-01-01"
            changed["detection"]["selection"]["Image|endswith"] = [r"\\changed.exe"]
            sigma_gen.write_sigma_rule_if_changed(changed, str(rule_path))

            written = yaml.safe_load(rule_path.read_text(encoding="utf-8"))
            self.assertEqual(written["id"], original["id"])
            self.assertEqual(str(written["date"]), original["date"])
            self.assertEqual(str(written["modified"]), sigma_gen.date.today().isoformat())

    def test_new_rule_has_no_modified_date(self) -> None:
        with TemporaryDirectory() as directory:
            rule_path = Path(directory) / "rule.yml"
            sigma_gen.write_sigma_rule_if_changed(sample_rule(), str(rule_path))

            written = yaml.safe_load(rule_path.read_text(encoding="utf-8"))
            self.assertNotIn("modified", written)

    def test_sorted_collision_warning_and_repeated_generation_are_deterministic(self) -> None:
        with TemporaryDirectory() as directory:
            root = Path(directory)
            yaml_dir = root / "yaml"
            output_dir = root / "sigma"
            yaml_dir.mkdir()

            for filename, executable in (("z-last.yaml", "z.exe"), ("a-first.yaml", "a.exe")):
                (yaml_dir / filename).write_text(
                    yaml.safe_dump(
                        {
                            "Name": "Shared Tool",
                            "Details": {"InstallationPaths": [rf"C:\Tools\{executable}"]},
                        },
                        sort_keys=False,
                    ),
                    encoding="utf-8",
                )

            first_output = io.StringIO()
            with redirect_stdout(first_output):
                sigma_gen.main(False, str(yaml_dir), str(output_dir))
            generated = output_dir / "shared_tool_processes_sigma.yml"
            first_bytes = generated.read_bytes()

            second_output = io.StringIO()
            with redirect_stdout(second_output):
                sigma_gen.main(False, str(yaml_dir), str(output_dir))

            self.assertIn("Duplicate tool Name", first_output.getvalue())
            self.assertIn("a-first.yaml", first_output.getvalue())
            self.assertEqual(generated.read_bytes(), first_bytes)
            self.assertEqual(second_output.getvalue(), first_output.getvalue())


if __name__ == "__main__":
    unittest.main()

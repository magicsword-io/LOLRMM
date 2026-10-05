"""Focused regression tests for the Sigma rule generator."""

from __future__ import annotations

import copy
import contextlib
import shutil
import subprocess
import sys
import tempfile
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
with patch.object(sys, "path", [str(ROOT / "bin"), *sys.path]):
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
    def test_windows_file_rule_excludes_other_platforms(self) -> None:
        with TemporaryDirectory() as directory:
            root = Path(directory)
            source = root / "tool.yaml"
            windows_paths = [r"C:\Tools\agent.exe", r"C:\Tools\legacy.log", r"C:\Tools\null.log"]
            source.write_text(yaml.safe_dump({
                "Name": "Example",
                "Artifacts": {"Disk": [
                    {"File": windows_paths[0], "OS": " windows "},
                    {"File": windows_paths[1]},
                    {"File": windows_paths[2], "OS": None},
                    {"File": "/opt/example/agent", "OS": "Linux"},
                    {"File": "/Library/Example/agent", "OS": "macOS"},
                    {"File": "/tmp/example", "OS": "Linux/macOS"},
                ]},
            }), encoding="utf-8")

            sigma_gen.generate_sigma_rules(str(source), str(root))
            rule = yaml.safe_load((root / "example_files_sigma.yml").read_text())
            self.assertEqual(rule["logsource"]["product"], "windows")
            self.assertEqual(rule["detection"]["selection"]["TargetFilename|endswith"], windows_paths)

    def test_unix_only_files_remove_stale_windows_file_rule(self) -> None:
        with TemporaryDirectory() as directory:
            root = Path(directory)
            source = root / "tool.yaml"
            data = {"Name": "Example", "Artifacts": {
                "Disk": [{"File": r"C:\Tools\agent.exe", "OS": "Windows"}],
                "Network": [{"Domains": ["example.test"]}],
            }}
            source.write_text(yaml.safe_dump(data), encoding="utf-8")
            sigma_gen.generate_sigma_rules(str(source), str(root))
            generated = root / "example_files_sigma.yml"
            self.assertTrue(generated.exists())

            # Scope this migration to explicitly non-Windows artifacts, leaving
            # unrelated legacy rules without current Disk metadata untouched.
            data["Artifacts"]["Disk"] = []
            source.write_text(yaml.safe_dump(data), encoding="utf-8")
            sigma_gen.generate_sigma_rules(str(source), str(root))
            self.assertTrue(generated.exists())

            data["Artifacts"]["Disk"] = [{"File": "/opt/example/agent", "OS": "Linux"}]
            source.write_text(yaml.safe_dump(data), encoding="utf-8")
            rules = sigma_gen.generate_sigma_rules(str(source), str(root))
            self.assertFalse(generated.exists())
            self.assertEqual(len(rules), 1)
            self.assertTrue((root / "example_network_sigma.yml").exists())
            self.assertEqual(sigma_gen.generate_sigma_rules(str(source), str(root)), rules)

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


SCRIPT = Path(__file__).resolve().parents[1] / 'bin' / 'generate_detections.py'
spec = importlib.util.spec_from_file_location('generate_detections', SCRIPT)
generator = importlib.util.module_from_spec(spec)
spec.loader.exec_module(generator)


class ExecutableTests(unittest.TestCase):
    def test_installation_paths(self):
        cases = {
            r'C:\Program Files\AnyDesk\AnyDesk.exe': 'AnyDesk.exe',
            'C:/Program Files/Agent/Agent.EXE': 'Agent.EXE',
            '  "C:\\Program Files\\Agent\\quoted.exe"  ': 'quoted.exe',
            "'C:/Program Files/Agent/single.exe'": 'single.exe',
            r'C:\Agent\client*.exe': 'client*.exe',
            r'C:\Agent\client?.exe': 'client?.exe',
            r'C:\Agent\*': None,
            'C:/Agent/': None,
            'agent.msi': None,
            'agent.zip': None,
            'ARDAgent.app': None,
            '/usr/bin/agent': None,
            '<random>.exe': None,
            r'C:\Windows\<random>.exe': None,
            r'C:\ProgramData\Teramind Agent\<version>\{GUID}\tmagentsvc.exe': 'tmagentsvc.exe',
            '*client.exe': None,
            'agent.exe --service': None,
            r'C:\Args\plain.exe --output C:\Temp\wrong.exe': None,
            '"C:/Agent/plain.exe" --output C:/Temp/wrong.exe': None,
            '"C:/Agent/unclosed.exe': None,
            'invalid:agent.exe': None,
            None: None,
            123: None,
        }
        for value, expected in cases.items():
            with self.subTest(value=value):
                self.assertEqual(generator.executable_basename(value), expected)


class GenerationTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        (self.root / 'bin').mkdir()
        (self.root / 'yaml').mkdir()
        (self.root / 'website/public/api').mkdir(parents=True)
        self.script = self.root / 'bin/generate_detections.py'
        shutil.copyfile(SCRIPT, self.script)
        shutil.copyfile(ROOT / 'bin/detection_paths.py', self.root / 'bin/detection_paths.py')

    def write_inputs(self, reverse=False):
        records = [
            [r'C:\Tools\VendorAgent.exe', 'client*.exe', 'VendorAgent.EXE', '<random>.exe'],
            None,
            ['vendoragent.exe', r'C:\Tools\B.EXE', 123, 'valid.exe'],
        ]
        if reverse:
            records.reverse()
        for i, paths in enumerate(records):
            if reverse and paths:
                paths = list(reversed(paths))
            (self.root / f'yaml/{i}.yaml').write_text(yaml.safe_dump(
                {'Details': {'InstallationPaths': paths}}))
        domains = ['z.example', 'a.example', 'A.example', '*.wild.example']
        if reverse:
            domains.reverse()
        (self.root / 'website/public/api/rmm_domains.csv').write_text(
            'Domain\n' + '\n'.join(domains) + '\n')

    def outputs(self):
        outputs = {}
        for name in ('generic_rmm_detection.yml', 'rmm_domains_dns_queries.yml'):
            canonical = (self.root / 'detections/sigma' / name).read_bytes()
            public = (self.root / 'website/public/api/detections/sigma' / name).read_bytes()
            self.assertEqual(canonical, public)
            outputs[name] = canonical
        return outputs

    def test_cli_outputs_are_valid_identical_and_repeatable(self):
        self.write_inputs()
        first = None
        for reverse in (False, True):
            self.write_inputs(reverse)
            result = subprocess.run([sys.executable, str(self.script)],
                                    capture_output=True, text=True, check=True)
            self.assertNotIn('Error processing', result.stdout)
            outputs = self.outputs()
            if first is None:
                first = outputs
            else:
                self.assertEqual(first, outputs)
        rule = yaml.safe_load(first['generic_rmm_detection.yml'])
        self.assertEqual(rule['detection']['selection']['Image|endswith'],
                         [r'\\B.EXE', r'\\client*.exe', r'\\valid.exe', r'\\VendorAgent.EXE'])
        self.assertEqual(rule['tags'], ['attack.command-and-control', 'attack.t1219'])
        domains = yaml.safe_load(first['rmm_domains_dns_queries.yml'])
        self.assertEqual(domains['detection']['selection']['query|contains'],
                         ['.*.wild.example', '.A.example', '.z.example'])

    def test_reversed_filesystem_discovery_is_identical(self):
        self.write_inputs()
        files = list(map(str, (self.root / 'yaml').glob('*.yaml')))
        with patch.object(generator, '__file__', str(self.script)):
            with contextlib.redirect_stdout(io.StringIO()):
                with patch.object(generator.glob, 'glob', return_value=files):
                    generator.generate_sigma_rule()
                    generator.generate_sigma_domains_rule()
                first = self.outputs()
                with patch.object(generator.glob, 'glob', return_value=list(reversed(files))):
                    generator.generate_sigma_rule()
                self.assertEqual(first, self.outputs())

    def test_generic_names_keep_paths_in_both_generated_rules(self):
        """PROC-SCOPE-001/002/004: exercise both consumers and the public copy."""
        specific = [
            r'*\AppData\Roaming\Microsoft\DeviceSync\svchost.exe',
            r'*\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup\svchost.exe',
            r'C:\Program Files\Monitic\agent.exe',
            r'C:\Users\*\AppData\Local\remsupp-updater\installer.exe',
        ]
        source = self.root / 'yaml/example.yaml'
        source.write_text(yaml.safe_dump({
            'Name': 'Example', 'Details': {'InstallationPaths': specific + [
                'svchost.exe', 'SVCHOST.EXE', r'*\svchost.exe', r'C:\*\svchost.exe',
                r'C:\Windows\System32\svchost.exe', 'agent.exe', 'installer.exe',
                r'*\Windows\System32\svchost.exe', r'%APPDATA%\Vendor\agent.exe',
                'AnyDesk.exe',
            ]},
        }))
        subprocess.run([sys.executable, str(self.script)],
                       capture_output=True, text=True, check=True)
        output_dir = self.root / 'per-tool'
        output_dir.mkdir()
        sigma_gen.generate_sigma_rules(str(source), str(output_dir))
        aggregate = yaml.safe_load((self.root / 'detections/sigma/generic_rmm_detection.yml').read_text())
        per_tool = yaml.safe_load((output_dir / 'example_processes_sigma.yml').read_text())
        expected = {value.replace('\\', '\\\\') for value in specific} | {r'\\AnyDesk.exe'}
        for selectors in [
            aggregate['detection']['selection']['Image|endswith'],
            per_tool['detection']['selection_image']['Image|endswith'],
            per_tool['detection']['selection_parent']['ParentImage|endswith'],
        ]:
            self.assertEqual(set(selectors), expected)
        self.outputs()  # Public aggregate copy must receive the same correction.

    def test_bare_generic_names_remove_stale_process_rule(self):
        """PROC-SCOPE-003: a rejected source cannot leave an old broad rule."""
        output_dir = self.root / 'per-tool'
        output_dir.mkdir()
        stale = output_dir / 'example_processes_sigma.yml'
        stale.write_text(yaml.safe_dump(sample_rule()))
        source = self.root / 'yaml/example.yaml'
        source.write_text(yaml.safe_dump({
            'Name': 'Example',
            'Details': {'InstallationPaths': ['svchost.exe', 'agent.exe', 'installer.exe']},
        }))
        self.assertEqual(sigma_gen.generate_sigma_rules(str(source), str(output_dir)), [])
        self.assertFalse(stale.exists())


if __name__ == "__main__":
    unittest.main()

"""Raw CSV exports must preserve context and scope just like the JSON API."""

import copy
import csv
import importlib.util
import json
import sys
import unittest
from pathlib import Path
from tempfile import TemporaryDirectory
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
with patch.object(sys, "path", [str(ROOT / "bin"), *sys.path]):
    import validate_generated
    spec = importlib.util.spec_from_file_location("catalog_site", ROOT / "bin/site.py")
    catalog_site = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(catalog_site)


def context_entry():
    return {
        "Name": "Example", "Category": "RMM", "Description": "Example tool",
        "Created": "2026-10-28", "LastModified": "2026-10-28",
        "Details": {"InstallationPaths": [], "SupportedOS": [], "Capabilities": []},
        "Artifacts": {"Network": [{
            "Description": "Shared download evidence", "Domains": ["github.com"],
            "Ports": [443], "Detection": False,
            "DetectionReason": "Shared host; research context only",
            "Scope": {"FileNames": ["ExampleRemote.exe"], "Required": True},
        }]},
    }


class CatalogCSVTests(unittest.TestCase):
    def test_export_preserves_all_network_context_and_scope_fields(self):
        tool = context_entry()
        with TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "public/api").mkdir(parents=True)
            catalog_site.write_rmm_tools_csv([tool], str(root), False)
            with (root / "public/api/rmm_tools.csv").open(newline="") as stream:
                rows = list(csv.DictReader(stream))
        self.assertEqual(json.loads(rows[0]["Artifacts"]), tool["Artifacts"])
        self.assertEqual(list(validate_generated.catalog_csv_issues(rows, [tool])), [])

    def test_gate_rejects_mutated_context_scope_and_artifacts(self):
        tool = context_entry()
        for field in ("Detection", "DetectionReason", "Scope", "Domains"):
            with self.subTest(field=field):
                artifacts = copy.deepcopy(tool["Artifacts"])
                del artifacts["Network"][0][field]
                rows = [{"Name": tool["Name"], "Artifacts": json.dumps(artifacts)}]
                findings = list(validate_generated.catalog_csv_issues(rows, [tool]))
                self.assertTrue(any("scope/context metadata" in finding for finding in findings))

    def test_gate_checks_inventory_and_malformed_json(self):
        tool = context_entry()
        row = {"Name": tool["Name"], "Artifacts": json.dumps(tool["Artifacts"])}
        # A duplicate display name must not hide a missing or duplicated record.
        second = copy.deepcopy(tool)
        second["Artifacts"]["Network"][0]["Detection"] = True
        second_row = {"Name": second["Name"], "Artifacts": json.dumps(second["Artifacts"])}
        self.assertEqual(list(validate_generated.catalog_csv_issues([second_row, row], [tool, second])), [])
        for rows in ([], [row], [row, row], [row, row, second_row],
                     [{"Name": "Example", "Artifacts": "not json"}], [{"Name": "Example"}]):
            with self.subTest(rows=rows):
                self.assertTrue(list(validate_generated.catalog_csv_issues(rows, [tool, second])))


if __name__ == "__main__":
    unittest.main()

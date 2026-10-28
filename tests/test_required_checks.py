"""Required status checks must fail rather than skip failed prerequisites."""

import unittest
from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[1]


class RequiredCheckTests(unittest.TestCase):
    def test_yaml_gate_propagates_lint_failure(self):
        workflow = yaml.load(
            (ROOT / ".github/workflows/validate.yml").read_text(), Loader=yaml.BaseLoader,
        )
        gate = workflow["jobs"]["validate-yaml"]
        self.assertEqual(gate["needs"], "yamllint")
        self.assertEqual(gate["if"], "${{ always() }}")
        prerequisite = gate["steps"][0]
        self.assertEqual(prerequisite["if"], "${{ needs.yamllint.result != 'success' }}")
        self.assertIn("exit 1", prerequisite["run"])
        self.assertNotIn("continue-on-error", prerequisite)
        self.assertNotIn("continue-on-error", gate)


if __name__ == "__main__":
    unittest.main()

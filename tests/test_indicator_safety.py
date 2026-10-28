"""Behavioral guards for domains, signing evidence, hashes, and final rules."""

import base64
import copy
import hashlib
import importlib.util
import subprocess
import sys
import unittest
from datetime import datetime, timezone
from pathlib import Path
from tempfile import TemporaryDirectory
from unittest.mock import patch

import yaml
from cryptography import x509
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import ed25519
from cryptography.x509.oid import NameOID

ROOT = Path(__file__).resolve().parents[1]
with patch.object(sys, "path", [str(ROOT / "bin"), *sys.path]):
    import domain_safety
    import evidence_safety
    import generate_domains_csv
    import validate_generated
    spec = importlib.util.spec_from_file_location("safety_sigma_gen", ROOT / "bin/sigma-gen.py")
    sigma_gen = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(sigma_gen)


def entry(domains):
    return {
        "Name": "Example", "Category": "RMM", "Description": "Example tool",
        "Created": "2026-10-26",
        "Artifacts": {"Network": [{"Description": "Agent service", "Domains": domains, "Ports": [443]}]},
    }


def rule(selection):
    return {"detection": {"selection": selection, "condition": "selection"}}


class DomainSafetyTests(unittest.TestCase):
    def test_public_suffixes_shared_hosts_and_invalid_values_are_rejected(self):
        for value in ("*.edu", "*.co.uk", "co.uk", "*.com", "*", "*.ck", "a.ck",
                      "*.c?m", "vendor.*", "x.*.com", "github.com", "*.github.com",
                      "raw.githubusercontent.com", "ghcr.io", "*.cloudfront.net", "*.pages.dev",
                      "", " ", "N/A", "https://example.com", "127.0.0.1", "*.local",
                      "example.com/path", "vendor.example\n", "a" * 64 + ".com"):
            with self.subTest(value=value):
                self.assertIsNotNone(domain_safety.domain_issue(value))
                self.assertFalse(domain_safety.should_export_domain(value))

    def test_psl_exceptions_tenants_and_product_domains_are_preserved(self):
        for value in ("www.ck", "*.www.ck", "city.kawasaki.jp", "*.vendor.co.uk",
                      "tenant.azurewebsites.net", "customer.github.io", "*.ngrok.io",
                      "remotedesktop.google.com", "vendor.example", "host.vendor.example."):
            with self.subTest(value=value):
                self.assertIsNone(domain_safety.domain_issue(value))
                self.assertTrue(domain_safety.should_export_domain(value))

    def test_shared_host_context_requires_reason_and_never_exports(self):
        data = entry(["github.com"])
        network = data["Artifacts"]["Network"][0]
        self.assertTrue(list(domain_safety.catalog_domain_issues(data)))
        network["Detection"] = False
        self.assertTrue(list(domain_safety.catalog_domain_issues(data)))
        network["DetectionReason"] = "Installer download evidence, not a tool-specific host"
        self.assertEqual(list(domain_safety.catalog_domain_issues(data)), [])
        self.assertEqual(domain_safety.detection_domains(network), [])
        network["Domains"] = ["*.edu"]
        self.assertTrue(list(domain_safety.catalog_domain_issues(data)))  # Context isn't a waiver.

    def test_placeholders_are_evidence_and_never_become_selectors(self):
        placeholders = ["user_managed", "user-managed", "<operator-supplied-host>"]
        self.assertEqual(domain_safety.detection_domains(entry(placeholders)["Artifacts"]["Network"][0]), [])
        self.assertEqual(domain_safety.domain_patterns(placeholders), [])

    def test_generated_domain_patterns_match_only_apex_and_subdomains(self):
        patterns = domain_safety.domain_patterns(["Vendor.Example"])
        for host in ("vendor.example", "child.vendor.example", "VENDOR.EXAMPLE.", "x.vendor.example."):
            self.assertTrue(any(validate_generated.selector_matches("query", p, host) for p in patterns), host)
        for host in ("notvendor.example", "vendor.example.attacker.test", "x.vendor.example.attacker.test",
                     "vendorx.example", "other.example"):
            self.assertFalse(any(validate_generated.selector_matches("query", p, host) for p in patterns), host)

    def test_csv_and_sigma_consistently_exclude_context_and_placeholders(self):
        with TemporaryDirectory() as directory:
            root = Path(directory)
            source = root / "example.yaml"
            data = entry(["user_managed", "<operator-host>", "github.com", "vendor.example"])
            data["Artifacts"]["Network"].append({
                "Description": "Download evidence", "Domains": ["github.com", "context.vendor.example"],
                "Ports": [443], "Detection": False, "DetectionReason": "Context only",
            })
            source.write_text(yaml.safe_dump(data))
            self.assertEqual(generate_domains_csv.extract_domains(str(source)), [("vendor.example", "Example")])
            sigma_gen.generate_sigma_rules(str(source), directory)
            generated = yaml.safe_load((root / "example_network_sigma.yml").read_text())
            self.assertEqual(generated["detection"]["selection"], {
                "DestinationHostname": domain_safety.domain_patterns(["vendor.example"]),
            })
            self.assertEqual(list(validate_generated.rule_issues(generated)), [])
            data["Artifacts"]["Network"][0]["Detection"] = False
            source.write_text(yaml.safe_dump(data))
            sigma_gen.generate_sigma_rules(str(source), directory)
            self.assertFalse((root / "example_network_sigma.yml").exists())


class EvidenceSafetyTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        key = ed25519.Ed25519PrivateKey.generate()
        subject = x509.Name([x509.NameAttribute(NameOID.COMMON_NAME, "Example LLC")])
        cert = (x509.CertificateBuilder().subject_name(subject).issuer_name(subject)
                .public_key(key.public_key()).serial_number(1)
                .not_valid_before(datetime(2024, 1, 1, tzinfo=timezone.utc))
                .not_valid_after(datetime(2025, 1, 1, tzinfo=timezone.utc))
                .add_extension(x509.BasicConstraints(ca=False, path_length=None), critical=True)
                .sign(key, algorithm=None))
        der = cert.public_bytes(serialization.Encoding.DER)
        cls.certificate = {
            "signer_name": "Example LLC", "certificate_der_base64": base64.b64encode(der).decode(),
            "issuer": "CN=Example LLC",
            "certificate_thumbprint": hashlib.sha1(der).hexdigest(),
            "tbs_sha256": hashlib.sha256(cert.tbs_certificate_bytes).hexdigest(),
            "tbs_sha1": hashlib.sha1(cert.tbs_certificate_bytes).hexdigest(),
            "tbs_sha384": hashlib.sha384(cert.tbs_certificate_bytes).hexdigest(),
            "valid_from": "2024-01-01T00:00:00Z", "valid_to": "2025-01-01T00:00:00Z",
        }

    def test_all_hash_locations_require_real_hex_digests(self):
        for value in ("g" * 64, "0" * 64, "a" * 63, "*.exe", "N/A"):
            for data in (
                {"FileHashes": {"authenticode": [{"file_name": "Example.exe", "sha256": value}]}},
                {"FileHashes": {"page": [{"file_name": "Example.exe", "sha256": value}]}},
                {"KnownVulnerableSamples": [{"SHA256": value}]},
                {"CodeSigning": {"certificates": [{"signer_name": "Example", "src_file_sha256": value}]}},
            ):
                with self.subTest(value=value, data=data):
                    self.assertTrue(list(evidence_safety.evidence_issues(data)))
        self.assertTrue(list(evidence_safety.evidence_issues({"FileHashes": {"page": [{"file_name": "Example.exe"}]}})))
        self.assertEqual(list(evidence_safety.evidence_issues({"FileHashes": {"page": [{"file_name": "Example.exe", "sha256": "ab" * 32, "sha1": None}]}})), [])

    def test_der_subject_fingerprints_tbs_and_dates_must_agree(self):
        # Expired historical evidence is valid; this checks consistency, not trust.
        self.assertEqual(list(evidence_safety.certificate_issues(self.certificate, "certificate", True)), [])
        for field, value in (("certificate_thumbprint", "a" * 40), ("tbs_sha256", "b" * 64),
                             ("tbs_sha1", "b" * 40), ("tbs_sha384", "b" * 96),
                             ("signer_name", "Unrelated Publisher"), ("certificate_der_base64", "invalid!"),
                             ("issuer", "CN=Unrelated CA"),
                             ("valid_from", "2024-02-01T00:00:00Z")):
            with self.subTest(field=field):
                certificate = {**self.certificate, field: value}
                self.assertTrue(list(evidence_safety.certificate_issues(certificate, "certificate", True)))

    def test_shared_publisher_requires_context_or_explicit_file_scope(self):
        signing = {"signer_names": ["Microsoft Corporation"], "certificates": []}
        self.assertTrue(list(evidence_safety.signing_issues({"CodeSigning": signing})))
        signing.update({"FileNames": ["ExampleRemote.exe"], "DetectionReason": "Verified tool binary; require filename AND signer"})
        self.assertEqual(list(evidence_safety.signing_issues({"CodeSigning": signing})), [])
        for scope in (["*.exe"], ["agent.exe"], [r"C:\Tools\Example.exe"], []):
            with self.subTest(scope=scope):
                self.assertTrue(list(evidence_safety.signing_issues({"CodeSigning": {**signing, "FileNames": scope}})))
        signing.pop("FileNames")
        signing["Detection"] = False
        self.assertEqual(list(evidence_safety.signing_issues({"CodeSigning": signing})), [])

    def test_wildcard_and_empty_signing_names_fail_even_as_context(self):
        for name in ("*", "Microsoft*", "?", "", "N/A"):
            data = {"CodeSigning": {"Detection": False, "DetectionReason": "Context", "signer_names": [name]}}
            self.assertTrue(list(evidence_safety.signing_issues(data)), name)


class GeneratedRuleSafetyTests(unittest.TestCase):
    def test_malformed_or_unconditional_rules_fail(self):
        for invalid in (None, [], {}, {"detection": {"selection": {"Image": "Example.exe"}, "condition": True}},
                        {"detection": {"selection": {"Image": "Example.exe"}, "condition": "true"}}):
            with self.subTest(rule=invalid):
                self.assertTrue(list(validate_generated.rule_issues(invalid)))

    def test_broad_empty_placeholder_and_substring_rules_fail(self):
        selections = [
            {"Image|endswith": [r"\\*.exe"]}, {"Image|endswith": [""]},
            {"Image|endswith": []}, {"TargetFilename|endswith": [r"%APPDATA%\Example\agent.exe"]},
            {"DestinationHostname": ["user_managed"]}, {"query": ["*.edu"]},
            {"query|contains": ["vendor.example"]}, {"query|endswith": ["vendor.example"]},
            {"query": ["github.com"]}, {"SHA256": ["z" * 64]},
            {"Signature": ["Microsoft Corporation"]}, {"Signature": ["Microsoft*"]},
            {"Image|endswith": [r"\\svchost.exe"]},
        ]
        for selection in selections:
            with self.subTest(selection=selection):
                self.assertTrue(list(validate_generated.rule_issues(rule(selection))))

    def test_safe_file_and_domain_rules_preserve_positive_coverage(self):
        self.assertEqual(list(validate_generated.rule_issues(rule({"Image|endswith": [r"\\ExampleRemote.exe"]}))), [])
        self.assertEqual(list(validate_generated.rule_issues(rule({"query": domain_safety.domain_patterns(["vendor.example"])}))), [])
        scoped = rule({"Signature": ["Microsoft Corporation"], "Image|endswith": [r"\\ExampleRemote.exe"]})
        self.assertEqual(list(validate_generated.rule_issues(scoped)), [])

    def test_sigma_or_branches_are_checked_without_rejecting_valid_rules(self):
        valid = rule([{"Image|endswith": [r"\\ExampleRemote.exe"]}, {"OriginalFileName": ["ExampleRemote.exe"]}])
        self.assertEqual(list(validate_generated.rule_issues(valid)), [])
        self.assertTrue(list(validate_generated.rule_issues(rule([{"Image|endswith": ["*.exe"]}]))))
        widened_scope = rule([{"Signature": ["Microsoft Corporation"]}, {"Image|endswith": [r"\\ExampleRemote.exe"]}])
        self.assertTrue(list(validate_generated.rule_issues(widened_scope)))

    def test_regeneration_removes_orphan_network_rules_but_preserves_manual_rules(self):
        with TemporaryDirectory() as directory:
            root = Path(directory)
            sources = root / "yaml"
            output = root / "rules"
            sources.mkdir()
            output.mkdir()
            (sources / "example.yaml").write_text(yaml.safe_dump(entry(["vendor.example"])))
            generated = {"title": "Potential OldName RMM Tool Network Activity", "author": "LOLRMM Project"}
            orphan = output / "oldname_network_sigma.yml"
            orphan.write_text(yaml.safe_dump(generated))
            manual = output / "manual_network_sigma.yml"
            manual.write_text(yaml.safe_dump({**generated, "author": "Human Maintainer"}))
            sigma_gen.main(False, str(sources), str(output))
            self.assertFalse(orphan.exists())
            self.assertTrue(manual.exists())
            self.assertTrue((output / "example_network_sigma.yml").exists())

    def test_cli_validation_and_lint_fail_before_merge_for_every_category(self):
        invalid_entries = [entry(["*.edu"]), entry(["github.com"]), entry([""]),
                           {**entry([]), "CodeSigning": {"signer_names": ["*"], "certificates": []}},
                           {**entry([]), "FileHashes": {"page": [{"file_name": "Example.exe", "sha256": "z" * 64}]}}]
        with TemporaryDirectory() as directory:
            source = Path(directory) / "example.yaml"
            for data in invalid_entries:
                source.write_text(yaml.safe_dump(data))
                for script in ("validate.py", "lint_content.py"):
                    result = subprocess.run([sys.executable, str(ROOT / "bin" / script), "-y", directory],
                                            cwd=ROOT, capture_output=True, text=True)
                    self.assertEqual(result.returncode, 1, result.stdout + result.stderr)
                    self.assertIn(str(source), result.stdout + result.stderr)


if __name__ == "__main__":
    unittest.main()

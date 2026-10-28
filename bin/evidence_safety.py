"""Validate identity evidence without confusing metadata with broad deny rules."""

import base64
import binascii
import hashlib
import ntpath
import re
from datetime import datetime, timezone

from cryptography import x509
from cryptography.x509.oid import NameOID

from domain_safety import context_issues
from path_safety import empty_selector


SHARED_PUBLISHERS = frozenset({
    "microsoft corporation", "microsoft windows", "microsoft windows component publisher",
    "google llc", "google inc", "google inc.", "apple inc.", "apple inc",
    "digicert inc", "digicert, inc.", "sectigo limited", "globalsign",
    "symantec corporation",
})
GENERIC_FILENAMES = frozenset({"agent.exe", "svchost.exe", "installer.exe", "setup.exe", "update.exe"})


def hash_issue(value, size):
    if not isinstance(value, str) or not re.fullmatch(rf"[0-9a-fA-F]{{{size}}}", value):
        return f"hash must contain exactly {size} hexadecimal characters"
    if set(value.casefold()) <= {"0"}:
        return "all-zero hash is a placeholder, not sample evidence"
    return None


def selector_issues(data):
    details = data.get("Details") or {}
    if isinstance(details, dict):
        paths = details.get("InstallationPaths") or []
        if isinstance(paths, list):
            for idx, value in enumerate(paths):
                if empty_selector(value):
                    yield f"Details.InstallationPaths[{idx}]", value, "selector-empty", "remove empty/sentinel selectors"
    artifacts = data.get("Artifacts") or {}
    if not isinstance(artifacts, dict):
        return
    for section, fields in (("Disk", ("File",)), ("Registry", ("Path",)),
                            ("EventLog", ("ImagePath", "CommandLine", "ServiceName"))):
        entries = artifacts.get(section) or []
        if not isinstance(entries, list):
            continue
        for idx, entry in enumerate(entries):
            if not isinstance(entry, dict):
                continue
            for field in fields:
                if field in entry and empty_selector(entry[field]):
                    yield f"Artifacts.{section}[{idx}].{field}", entry[field], "selector-empty", "remove empty/sentinel selectors"
            if section == "Registry" and isinstance(entry.get("Path"), str):
                value = entry["Path"].strip()
                if re.fullmatch(r"(?i)(?:HKLM|HKCU|HKCR|HKU|HKEY_LOCAL_MACHINE|HKEY_CURRENT_USER)?[\\*?.]*", value):
                    yield f"Artifacts.Registry[{idx}].Path", value, "registry-catchall", "registry selectors require a tool-specific key"


def file_hash_issues(data):
    groups = data.get("FileHashes") or {}
    if isinstance(groups, dict):
        for group, entries in groups.items():
            if not isinstance(entries, list):
                continue
            for idx, entry in enumerate(entries):
                if not isinstance(entry, dict):
                    continue
                field = f"FileHashes.{group}[{idx}]"
                if empty_selector(entry.get("file_name")) or any(c in entry.get("file_name", "") for c in "*?"):
                    yield f"{field}.file_name", entry.get("file_name"), "hash-filename", "hash evidence needs a literal source filename"
                if not any(entry.get(key) for key in ("sha1", "sha256")):
                    yield field, "", "hash-missing", "a file-hash record must contain at least one actual digest"
                for key, size in (("sha1", 40), ("sha256", 64)):
                    value = entry.get(key)
                    if value not in (None, "") and (reason := hash_issue(value, size)):
                        yield f"{field}.{key}", value, "hash-invalid", reason
    samples = data.get("KnownVulnerableSamples") or []
    if isinstance(samples, list):
        for idx, sample in enumerate(samples):
            if not isinstance(sample, dict):
                continue
            for key, size in (("MD5", 32), ("SHA1", 40), ("SHA256", 64)):
                value = sample.get(key)
                if value not in (None, "") and (reason := hash_issue(value, size)):
                    yield f"KnownVulnerableSamples[{idx}].{key}", value, "hash-invalid", reason


def certificate_issues(certificate, field, detection):
    for key, size in (("certificate_thumbprint", 40), ("src_file_sha256", 64),
                      ("tbs_sha1", 40), ("tbs_sha256", 64), ("tbs_sha384", 96)):
        value = certificate.get(key)
        # Historical unavailable-thumbprint metadata is not a digest/selector.
        if key == "certificate_thumbprint" and value == "N/A":
            continue
        if value not in (None, "") and (reason := hash_issue(value, size)):
            yield f"{field}.{key}", value, "hash-invalid", reason
    encoded = certificate.get("certificate_der_base64")
    if not encoded:
        return
    try:
        der = base64.b64decode("".join(encoded.split()), validate=True)
        cert = x509.load_der_x509_certificate(der)
    except (ValueError, TypeError, AttributeError, binascii.Error) as exc:
        yield f"{field}.certificate_der_base64", "<certificate>", "certificate-der", f"invalid base64/DER certificate: {exc}"
        return
    for key, actual in (
        ("certificate_thumbprint", hashlib.sha1(der).hexdigest()),
        *((f"tbs_{algo}", hashlib.new(algo, cert.tbs_certificate_bytes).hexdigest())
          for algo in ("sha1", "sha256", "sha384")),
    ):
        value = certificate.get(key)
        if value and (not isinstance(value, str) or value.casefold() != actual):
            yield f"{field}.{key}", value, "certificate-digest-mismatch", "digest does not match the embedded DER certificate"
    names = {attr.value.casefold() for oid in (NameOID.COMMON_NAME, NameOID.ORGANIZATION_NAME)
             for attr in cert.subject.get_attributes_for_oid(oid)}
    signer = certificate.get("signer_name")
    if isinstance(signer, str) and signer.casefold() not in names:
        yield f"{field}.signer_name", signer, "certificate-subject-mismatch", "signer does not match the embedded certificate subject"
    issuer = certificate.get("issuer")
    issuer_names = {cert.issuer.rfc4514_string().casefold()}
    for oid, prefix in ((NameOID.COMMON_NAME, "CN"), (NameOID.ORGANIZATION_NAME, "O")):
        for attr in cert.issuer.get_attributes_for_oid(oid):
            issuer_names.update((attr.value.casefold(), f"{prefix}={attr.value}".casefold()))
    if issuer and (not isinstance(issuer, str) or issuer.casefold() not in issuer_names):
        yield f"{field}.issuer", issuer, "certificate-issuer-mismatch", "issuer does not match the embedded certificate"
    for key, actual in (("valid_from", cert.not_valid_before_utc), ("valid_to", cert.not_valid_after_utc)):
        value = certificate.get(key)
        if not value:
            continue
        try:
            declared = datetime.fromisoformat(value)
            if declared.tzinfo is None:
                declared = declared.replace(tzinfo=timezone.utc)
            if declared != actual:
                raise ValueError("date does not match DER")
        except (ValueError, TypeError):
            yield f"{field}.{key}", value, "certificate-validity-mismatch", "validity timestamp must match the embedded certificate"
    try:
        if detection and cert.extensions.get_extension_for_class(x509.BasicConstraints).value.ca:
            yield field, certificate.get("signer_name"), "certificate-ca", "CA certificates require context-only designation; never derive standalone blocking identities"
    except x509.ExtensionNotFound:
        pass


def signing_issues(data):
    signing = data.get("CodeSigning") or {}
    if not isinstance(signing, dict):
        return
    for field, value, reason in context_issues(signing, "CodeSigning"):
        yield field, value, "detection-context", reason
    names = []
    for key in ("search_names", "company_names", "signer_names", "ignored_company_names", "ignored_signer_names"):
        values = signing.get(key) or []
        if not isinstance(values, list):
            continue
        for idx, value in enumerate(values):
            if empty_selector(value) or any(c in value for c in "*?"):
                yield f"CodeSigning.{key}[{idx}]", value, "signing-selector", "signing identity/search fields require nonempty literal values, without wildcards"
            if key in {"company_names", "signer_names"}:
                names.append(value)
    scopes = signing.get("FileNames") or []
    valid_scope = isinstance(scopes, list) and bool(scopes)
    if "FileNames" in signing:
        if not isinstance(scopes, list) or not scopes:
            yield "CodeSigning.FileNames", scopes, "signing-scope", "file scope must be a nonempty list of exact tool filenames"
        elif any(empty_selector(v) or ntpath.basename(v) != v or any(c in v for c in '*?<>%')
                 or v.casefold() in GENERIC_FILENAMES for v in scopes):
            valid_scope = False
            yield "CodeSigning.FileNames", scopes, "signing-scope", "use exact tool-specific basenames; generic names, paths, and wildcards are insufficient scope"
    certificates = signing.get("certificates") or []
    if isinstance(certificates, list):
        for idx, cert in enumerate(certificates):
            if not isinstance(cert, dict):
                continue
            field = f"CodeSigning.certificates[{idx}]"
            signer = cert.get("signer_name")
            if empty_selector(signer) or any(c in signer for c in '*?'):
                yield f"{field}.signer_name", signer, "signing-selector", "certificate signer must be a nonempty literal identity"
            names.append(signer)
            yield from certificate_issues(cert, field, signing.get("Detection", True) is True)
    if signing.get("Detection", True) is True:
        shared = sorted({value for value in names if isinstance(value, str) and value.casefold() in SHARED_PUBLISHERS})
        if shared and (not valid_scope or empty_selector(signing.get("DetectionReason"))):
            yield "CodeSigning", ", ".join(shared), "signing-shared-publisher", (
                "shared publishers require exact FileNames AND a DetectionReason; "
                "otherwise set Detection: false with a reason to preserve context only"
            )


def evidence_issues(data):
    if not isinstance(data, dict):
        return
    yield from selector_issues(data)
    yield from file_hash_issues(data)
    yield from signing_issues(data)

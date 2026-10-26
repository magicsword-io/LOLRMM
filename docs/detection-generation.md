# Process indicator specificity

The per-tool and aggregate Sigma generators share the process-name policy in
`bin/detection_paths.py`. Catalog metadata can describe masquerading filenames
without making those filenames standalone detection indicators.

## Required behavior

- **PROC-SCOPE-001:** `svchost.exe`, `agent.exe`, and `installer.exe` require a
  documented installation directory. Bare names, wildcard-only directories,
  and standard Windows system directories must not produce process selectors.
- **PROC-SCOPE-002:** Keep the full documented path or directory suffix for these
  names in both `Image` and `ParentImage` selectors. For example, Overlord's
  `*\AppData\Roaming\Microsoft\DeviceSync\svchost.exe` remains detectable;
  normal `C:\Windows\System32\svchost.exe` does not match it.
- **PROC-SCOPE-003:** Regeneration must remove an obsolete per-tool process rule
  if its source contains only rejected generic names. Unrelated legacy rules
  without installation-path evidence are outside this migration.
- **PROC-SCOPE-004:** Other product filenames retain their existing matching
  behavior. Intentional remote-access tools such as `mstsc.exe` are not excluded
  merely because they ship with Windows.
- **PATH-SAFETY-001:** `bin/path_safety.py` rejects extension-only executable
  wildcards (including DLLs, installers, and scripts), catch-all file globs, and
  unscoped wildcards in `Details.InstallationPaths` and `Artifacts.Disk[].File`.
  A directory-qualified `C:\Program Files\Example\*.exe` is still unsafe because
  consumers may extract its basename. Both YAML validation and content lint
  fail with the source file, field, value, and remediation. Scoped directory
  globs and non-executable artifacts such as vendor logs remain supported.
- **PATH-SAFETY-002:** Sigma generation skips the same unsafe paths even when
  invoked without validation. Regeneration removes obsolete file/process rules
  if their source contains only rejected patterns.
- **DOMAIN-SAFETY-001:** Reject public-suffix patterns using the pinned ICANN
  PSL snapshot, including wildcard/exception rules and unknown TLDs. Reject
  unscoped general-purpose hosts such as GitHub and cloud hosting roots.
  Tenant-specific hostnames and documented remote-access service domains remain
  supported. The shared-host list is a bounded, reviewable policy, not a complete
  classifier of every hosting provider.
- **DOMAIN-SAFETY-002:** A network artifact may preserve shared infrastructure
  with `Detection: false` and a nonempty `DetectionReason`. These records and
  `user_managed`/angle-bracket placeholders never enter domain CSV or Sigma
  selectors. Context designation does not permit malformed values or public
  suffix wildcards. Plain domain selectors match the apex and subdomains using
  label boundaries; explicit wildcards retain their scope. Both forms cover
  trailing-dot DNS names. IP evidence is excluded from DNS/hostname Sigma rules.
- **SIGNING-SAFETY-001:** Reject wildcard/empty signing identity and search
  fields. Shared publishers require exact, non-generic `CodeSigning.FileNames`
  and a `DetectionReason`, or `Detection: false` with a reason. File scope MUST
  be ANDed with signing identity in each downstream selection, never emitted as
  a separate OR branch. CA certificates cannot be standalone blocking evidence.
  Raw catalog APIs retain contextual signing evidence; consumers must honor
  the designation. LOLRMM does not currently generate publisher-based Sigma rules.
- **EVIDENCE-SAFETY-001:** Validate actual MD5/SHA1/SHA256/SHA384 digests wherever
  supported, including vulnerable samples, file hashes, certificate thumbprints,
  source-file hashes, and TBS hashes. Reject non-hex, incorrect-length, and
  all-zero digests. File-hash records require at least one real digest. Optional
  unavailable digests remain absent; historical `N/A` thumbprints are unavailable
  metadata and must never become certificate selectors. Raw file, Authenticode,
  page, and TBS hashes are distinct and must not be substituted for one another.
- **EVIDENCE-SAFETY-002:** When DER is available, validate base64/X.509 parsing,
  subject, issuer, SHA1 thumbprint, declared TBS hashes, and validity timestamps
  against the embedded certificate. This checks evidence consistency; it does
  not assert chain trust, current validity/revocation, or ownership of a binary
  that is not available. Expired historical evidence remains valid catalog data.
- **OUTPUT-SAFETY-001:** `python bin/validate_generated.py` runs both production
  generators and API export generation in isolation, seeded with existing rules
  to detect stale selectors. Validate final selectors, reject empty/wildcard or
  placeholder rules, and exercise benign Windows/browser processes and unrelated
  domains. Ensure canonical/public aggregate copies match. Human-maintained
  Sigma OR branches are supported. The test matcher covers emitted glob
  operators; it does not replace integration testing with each downstream engine.
- **OUTPUT-SAFETY-002:** Regeneration removes generated network rules for renamed
  or removed tools when their generated title/author establish ownership. It also
  removes a tool's generated network rule when no eligible domains remain.
  Human-authored rules retain their lifecycle and are still checked by the gate.

This is a bounded list of confirmed collisions, not a complete false-positive
classifier. Add names only with catalog evidence and regression coverage. Do not
invent a directory to retain a bare indicator; document a verified installation
path first. Unexpanded environment variables and angle-bracket placeholders are
not emitted as scoped selectors. Paths remain hunting indicators, not proof of
malicious activity.

Run `python -m unittest discover -s tests` and both generators against the real
catalog. Check legitimate-process negative controls and documented-path positive
controls, including the public aggregate copy. Follow the
[Sigma escaping rules](https://sigmahq.io/sigma-specification/specification/sigma-rules-specification.html#escape-character)
when preserving Windows separators and wildcards.

Source PRs change the catalog, generators and tests; the generated-data workflow
refreshes committed rules and API exports after merge. Review that generated PR
before considering the published rule correction complete. Reverting the source
and regenerating restores the previous behavior.

`validate-yaml` runs the unit suite, source validation, and generated-output gate
on pull requests before merge. Content lint independently checks source safety;
the publishing workflows also run these safety gates before generating artifacts.
Repository administrators should require these CI statuses in the existing
branch rules. Workflow files alone cannot prevent an administrator from bypassing
an unrequired status. No policy deployments are performed by these checks.

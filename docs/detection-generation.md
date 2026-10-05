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

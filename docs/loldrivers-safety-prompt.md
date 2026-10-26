# LOLDrivers worker prompt

Copy the following task into the LOLDrivers workspace:

```text
Implement pre-merge indicator and generated-policy safety checks for LOLDrivers.

Background: LOLRMM published a directory-qualified *.exe artifact. A downstream
consumer extracted its basename and created policies matching every executable.
Prevent equivalent scope expansion in driver detections, WDAC/App Control
policies, blocklists, and public feeds. Do the implementation and verification,
not just an audit or plan. Start with this repository's AGENTS.md, schema,
validators, generators, workflows, and documented policy semantics; discover
the actual field names rather than assuming LOLRMM's schema.

1. Trace every source field through normalization to exported JSON/CSV,
   Sigma/YARA, WDAC XML, and other rule formats this repository actually emits.
   Explicitly distinguish research evidence from standalone blocking indicators.
   Preserve useful historical evidence with an enforced context-only designation
   or move it outside detection-bearing fields. Consumers must honor exclusions
   and scope. Do not label every legitimate vulnerable driver as harmless:
   verified vulnerable driver versions are intentionally cataloged here.

2. Reject catch-all and extension-only filename patterns: *, *.*, *.sys,
   *.dll, *.exe, wildcard-only stems, quoted/case/slash variants, and patterns
   that become broad when a consumer strips directories or expands variables.
   Require tool/driver-specific context for generic names. Check service names,
   registry artifacts, PE OriginalFilename, and other selector fields actually
   used by the generators. Do not ban every wildcard; retain reviewed,
   appropriately scoped patterns with positive coverage tests.

3. Validate every supported digest: raw file MD5/SHA1/SHA256, Authenticode,
   page, certificate thumbprint, and TBS hashes. Require correct hexadecimal
   lengths, reject placeholder/all-zero values and hashless active records,
   and keep different hash types distinct. Never manufacture missing hashes
   or fall back from an invalid hash to a broad filename/publisher rule.

4. Validate signing evidence. Wildcard/empty publisher identities and CA-wide
   blocking identities must fail. Shared vendors such as Microsoft or a driver
   vendor with many products require exact file/product AND version scope where
   applicable, or remain context-only. An exact certificate can still cover
   unrelated products. Never drop an existing scope constraint or turn its AND
   into an OR. Verify embedded DER/base64, certificate subject/issuer,
   fingerprints, declared TBS hashes, and validity metadata when available.
   Do not confuse consistency checks with chain trust or invent provenance.
   Retain expired historical evidence; flag unrelated sample evidence for review.

5. Reject empty, null, placeholder, unresolved-template, and unconditional
   selectors in final rules. If network indicators exist, validate public-suffix
   wildcard rules using a pinned offline PSL, review shared hosting/download
   infrastructure, and preserve hostname label boundaries. Common ports, event
   IDs, or ubiquitous Windows components alone are insufficient attribution.

6. Regenerate actual outputs in an isolated temporary directory during CI.
   Validate the final selectors/policy XML, not only source YAML. Include existing
   outputs so stale broad rules cannot survive renames, removals, or exclusions.
   Remove obsolete generated rules only when generator ownership is established;
   preserve manual rule ownership. Check public/canonical copies for agreement.
   Use established parsers/backends for each supported format where available.

7. Add meaningful negative and positive controls. Unrelated Windows drivers and
   unrelated products from the same signer must not match. Known affected sample
   hashes, documented vulnerable versions, and intended driver identities must
   still match. Test missing metadata, corrupt hashes/certificates, wildcard
   variants, scope loss, version boundaries, placeholder handling, stale rule
   removal, and normalization. For WDAC, verify exact hash lengths, publisher
   plus filename/product/version scope, and that rule references preserve those
   constraints. Never broaden a block to an entire vendor to make a test pass.

8. Run the checks on every PR before merge. Findings must identify source file,
   field, value, rule, and remediation and exit nonzero for unsafe active rules.
   Keep checks deterministic/offline with pinned data and dependencies. Resolve
   existing findings without weakening checks or adding blanket waivers;
   context-only evidence must actually be excluded by every relevant generator.
   Preserve source formatting and leave source YAML unchanged during generation.
   Document commands, supported semantics, limitations, and any exact engine
   integration that could not be exercised. Report which CI statuses must be
   required by repository branch rules; do not claim workflow files alone enforce
   branch protection. Do not modify production policies or run driver binaries.

Deliver the implementation, tests, existing-data corrections supported by
evidence, and a concise summary of checks/results. Work on the current branch
unless repository instructions or the user explicitly say otherwise. Do not
rename the branch, push, merge, deploy, or contact other people unless authorized.
```

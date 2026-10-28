---
date: 2026-10-27
project: jgs-se-knowledge-packs-ci-trust
mode: full
rounds: 1
input_digest: 792540680ca0bf62ebd1f414194cf7d5ad34c347ad587265931456093cfdab9d
open_objections: ["X4"]
---

Picked 2026-10-27 (user: run all four cuts to completion). X4 resolved to the fold: P48 owns the I9 counter-gate; P49 dropped as absorbed. Open objections X4/X5/X3 defaults accepted by the run instruction.

# Work packages - jgs-se-knowledge-packs-ci-trust (2026-10-27, full scoped re-run)

Scope of this cut (user-directed split after the whole-repo round hit TOO_MANY_PACKAGES
at 14): the CI trust boundary only. I8 licence-gate CI coverage, I9 signpost
counter-gate, I10 checkout pin. Converged in one round (value 3, risk 2, cohesion 2
candidates; merge produced 3 packages; triage zero_critical). Open fork X4 travels
in `open_objections`.

## P48 - ci-pack-licence-signpost-trust-gates

- **id**: P48; **name**: ci-pack-licence-signpost-trust-gates; **size**: L; **status**: done; **corroboration**: 3 (value, risk, cohesion); **deps**: none; **promoted_ids**: []
- **problem**: Catalogue trust rests on content-pack LICENSE presence, PACK.yaml mandatory provenance fields, and license_tier in {1,2,3}, plus kind:signpost staying citation-only. Local tooling/validate_pack.py is the only mechanical licence gate; CI validate.yml deliberately omits it and only runs inline data-invariant checks. Link-policy and pack-quality CI steps skip kind:signpost trees (same signpost_dirs/kind regex) and PACK-SPEC skips LICENSE/chapters for signposts, with no CI counter-gate that those trees stay chapter-free. One frontmatter flip plus catalog-row removal drops URL bans, chapter quality checks, and licence obligations while CI stays green (findings I8 and I9, both HIGH).
- **evidence**: CONTRIBUTING.md:L70 ("CI does not run `validate_pack.py`."); validate.yml header ("full validate_pack (non-trivial parser; a fork invites permanent drift)"); tooling/validate_pack.py:L11-18 and L29-30 (required files, REQUIRED_PACK_FIELDS, VALID_TIERS); validate.yml:L72-73 (signpost link-policy exemption), L121-132 (signpost_dirs classifier), L1103 (packs glob minus signpost_dirs); docs/PACK-SPEC.md signpost classification row.
- **in_scope**: pure-data CI subset (or reviewed twin) of the licence gates (LICENSE present, PACK.yaml mandatory fields filled, license_tier in {1,2,3}) for every content pack; I9 counter-gate folded inside (X4 risk/cohesion side): kind:signpost trees must stay citation-only (no chapters/ bulk content; link-policy exemption only for true citation-only signposts); reuse one kind classifier across link-policy, pack-quality, licence subset, counter-gate; parity pins in tooling/test_ci_gate.py for any new heredoc; coverage-map line in the validate.yml header; keep full validate_pack local-only.
- **out_scope**: blind full validate_pack parser fork into CI; actions/checkout pin (P50); I2 twin-architecture rewrite; html-assets/gen_pack_pages/runbooks/growth packs; version bump; GitHub Release; frozen P8; separate package for I9 (value X4 side, recorded as P49).
- **why_now**: two PASS HIGH findings on one CI-blind trust class sharing validate.yml content-integrity, the kind:signpost exemption path, the validate_pack/check_pack_quality classifiers, and test_ci_gate parity pins. I9 depends on the I8 omission, so the counter-gate lands with licence coverage.
- **triage notes**: PASS, size L. The kind:signpost regex is currently forked across five validate.yml sites; consolidation is part of the package. X4 fold means P48 is startable on the risk/cohesion reading; if the human rules the value side, P49 runs instead and P48 drops its I9 fold.
- **first_prompt**: `/superpowers-process full add CI licence and signpost trust gates for content packs`

## P50 - pin-actions-checkout-sha

- **id**: P50; **name**: pin-actions-checkout-sha; **size**: S; **status**: done; **corroboration**: 3 (value, risk, cohesion); **deps**: none; **promoted_ids**: []
- **problem**: validate.yml pins actions/checkout@v4 mutable tag while the job otherwise hardens with permissions: read-all and stdlib-only inline checks. A compromised or retagged checkout@v4 can rewrite workspace contents every integrity heredoc reads, with no pack or tooling diff in the PR. SECURITY accepted-risk T-20-SC covers pip/npm manifests, not Actions tag mutability (finding I10, MEDIUM).
- **evidence**: validate.yml:L48-54 (`- uses: actions/checkout@v4` under `permissions: read-all`); SECURITY.md T-20-SC acceptance note.
- **in_scope**: replace actions/checkout@v4 with actions/checkout@\<full-commit-sha\> plus a tag+date comment; confirm no other unpinned third-party actions; optional one-line residual note.
- **out_scope**: I8/I9 gate bodies (P48/P49); broader supply-chain policy rewrite, Dependabot; version bump; release.
- **why_now**: independent MEDIUM supply-chain floor under every CI trust check; one-line pin, no coupling to P48/P49 beyond the single uses line.
- **triage notes**: PASS, size S.
- **first_prompt**: `/superpowers-process full pin actions/checkout to a commit SHA in validate.yml`

## P49 - signpost-citation-only-counter-gate (CONFLICT; not startable)

- **id**: P49; **name**: signpost-citation-only-counter-gate; **size**: M; **status**: dropped; **corroboration**: 1 (value); **deps**: [P48]; **promoted_ids**: []
- **problem**: kind:signpost flips drop link-policy bans, pack-quality chapter checks, and frontmatter lint paths while PACK-SPEC skips LICENSE/chapters for signposts; no CI check asserts absent chapters/bulk content under that kind (finding I9, HIGH). Held as a separate package per the value lens, dependent on P48.
- **evidence**: validate.yml:L72-73 signpost exemption comment; signpost_dirs classifier; PACK-SPEC signpost row; triage-log I9 row.
- **in_scope**: X4 value side: separate package; CI/local counter-gate that every kind:signpost tree has no chapters/ dir and no bulk reconstructed content beyond citation SKILL.md + PACK.yaml; fail closed on kind flips that coexist with chapter markdown; test_ci_gate parity.
- **out_scope**: folding into P48 (risk/cohesion X4 side, rejected by this lens); licence/provenance checks (P48); checkout pin; signpost product content changes.
- **why_now**: second HIGH trust hole; depends on P48 so the content vs non-content classification stays one boundary rather than two drifting forks.
- **triage notes**: grade CONFLICT. X4 is unresolved (value wants I9 separate; risk+cohesion fold it inside P48), so P49 gets no first_prompt and never appears as payload line 1. If the human resolves X4 to the value side, P49 becomes startable with this scope; if to the risk/cohesion side, P49 closes as absorbed into P48.
- *(no first_prompt: not startable while X4 is open)*

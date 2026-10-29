---
date: 2026-10-28
project: jgs-se-knowledge-packs-review
mode: light
rounds: 1
input_digest: 3c2451cb87a3ef70d6bbe10a845f19adaad3e199337df7aa377c016d84443e71
open_objections: []
---

# Packages - jgs-se-knowledge-packs review cut (2026-10-28, post-RRL light re-run #5)

Cut from the 2026-10-28 repo review findings (I14 HIGH, I13/I15/I16/I17 MEDIUM, a-21..a-31). Wave: value 3, risk 4, cohesion 1. Merge unioned to three packages (correct ids continue at P61 after the P57-P60 drain); triage zero_critical. Advisories a-22..a-30 carried on existing backlog rows; a-21 and a-31 routed as new backlog rows below.

## P61 - licensing-omg-tier-truth

- **id**: P61; **name**: licensing-omg-tier-truth; **size**: S; **status**: done; **corroboration**: 2 (value, risk); **deps**: none; **promoted_ids**: []
- **problem**: LICENSING.md's Tier-2 section presents OMG specs (SysML) as a lawful packable source and claims "Our packs comply with all three", while SOURCE-VETTING.md hard-excludes all OMG formal specifications as informational-use-only (no network posting, no modification; two independent licence reads 2026-06-19) and forbids packaging. The author-facing compliance doc carries inverted eligibility guidance.
- **evidence**: docs/LICENSING.md:L42-56; docs/SOURCE-VETTING.md:L49-51, L79 (RRL finding I14, HIGH).
- **in_scope**: rewrite the LICENSING.md Tier-2 section so OMG is neither an example nor a compliance claim; point Tier-2 readers at the SOURCE-VETTING Excluded row; grep public docs for residual OMG-as-Tier-2 claims; keep SEBoK/OCW/OGL Tier-2 cases correct.
- **out_scope**: SOURCE-VETTING rewrites beyond the cross-check; pack rebuilds; catalogue counts (P62); cursor gate (P63); version bump.
- **why_now**: the only live HIGH in the review; takedown and misrepresentation exposure on the doc readers hit first.
- **triage notes**: PASS, size S.
- **first_prompt**: `/superpowers-process full fix LICENSING OMG Tier-2 contradiction against SOURCE-VETTING`

## P62 - post-124-author-operator-doc-truth

- **id**: P62; **name**: post-124-author-operator-doc-truth; **size**: M; **status**: done; **corroboration**: 2 (value, risk; cohesion noted the I15/I17 split argument, risk's PACK-SPEC edit-clash carries); **deps**: none; **promoted_ids**: []
- **problem**: Author/operator docs lag the shipped catalogue: SOURCE-FRESHNESS "the catalogue's 71 live packs", PACK-SPEC kind table "the 71 catalogue packs", DISTRIBUTION "all 81 skill paths" / "All 71 catalog packs" (truth: 74 content packs, 83 skills); and PACK-SPEC's build section plus CONTRIBUTING's authoring steps teach only the old extract+offset-map stub, so the two-PDF pin rule, contents-list-wins-over-TOC freeze, and verify-what-you-wrote transport-integrity check live only in gitignored superpowers specs.
- **evidence**: docs/SOURCE-FRESHNESS.md:L8; docs/PACK-SPEC.md:L109, L66-69; docs/DISTRIBUTION.md:L11, L27; CONTRIBUTING.md:L41-43 (RRL findings I15, I17).
- **in_scope**: update stale counts to 74/83 across the three files plus residual greps; add an author-facing PACK-SPEC build-rules section (multi-PDF/part pin, contents-list-wins, transport-integrity check) citing nasa-risk/faa-ams-vv/jsp-912 as worked examples; point CONTRIBUTING's build bullet at that section.
- **out_scope**: LICENSING/OMG (P61); cursor gate (P63); CI; version bump.
- **why_now**: the build contract and inventory changed under the docs; every new pack author follows wrong instructions today.
- **triage notes**: PASS, size M. Batch kept: PACK-SPEC edit-clash (risk) outweighs cohesion's different-data-flow split; one prose run.
- **first_prompt**: `/superpowers-process full restore author and operator doc truth post 1.24.0`

## P63 - cursor-eligible-parse-harden

- **id**: P63; **name**: cursor-eligible-parse-harden; **size**: M; **status**: done; **corroboration**: 3 (value, risk, cohesion); **deps**: none; **promoted_ids**: []
- **problem**: Check 6b and its CI twin `Cursor skills eligible set` classify commercial eligibility with a raw `"commercial_use: false"` substring on PACK.yaml text. Quoted, spaced, or cased variants miss; missing/unparseable values on a shipped pack fail to exclude; validate_pack only requires the field non-empty. Latent (all 83 packs canonical today), but P60 made this the CI-load-bearing commercial allowlist. test_ci_gate pins the step with one mismatch demo — no negatives for the failure modes and no demo_ok.
- **evidence**: tooling/check_release.py:L1383-1390; .github/workflows/validate.yml:L1383-1391; tooling/validate_pack.py:L29-50, L107-111; tooling/test_ci_gate.py:L588-596, L61-73 (RRL findings I13, I16).
- **in_scope**: replace the substring match in check_release 6b and the validate.yml twin with a parsed scalar via validate_pack's normalize path (strip quotes, top-level boolean true/false only); fail closed on missing/unparseable commercial_use for packs with SKILL.md; test_ci_gate negative demos (quoted/spaced/missing) plus one demo_ok; keep PINNED_STEPS and the real-tree positive run.
- **out_scope**: b-38 validate_pack-in-CI fork; b-37 twin rewrite; I14/I15/I17; version bump.
- **why_now**: P60 promoted this allowlist into CI; the substring hole ships as a trusted gate and the pair must land together (P60 cohesion precedent).
- **triage notes**: PASS, size M. Corroboration 3.
- **first_prompt**: `/superpowers-process full parse commercial_use scalar in the cursor eligible-set gate and pin its failure modes`

## Execution order

P61 → P62 → P63 (no deps; HIGH truth fix first).

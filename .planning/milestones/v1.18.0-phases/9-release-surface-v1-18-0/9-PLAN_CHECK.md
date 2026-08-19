# Phase 9 Plan Self-Check — 9-01-PLAN.md

Date: 2026-08-14. Checker role: goal-backward verification of 9-01-PLAN.md against ROADMAP Phase 9 Success Criteria and REQUIREMENTS REL-1x-01/02.

## Goal-Backward Trace

| Required truth (SC / REQ) | Plan coverage | Evidence in plan |
|---|---|---|
| SC1: check_release PASS at updated catalog/directory basis | Task 4 step 2 + must_haves.truths[0] | Independent asserts: catalog packs == 61, packs dirs == 63 (both verified live 2026-08-14) |
| SC1: all surfaces version-consistent | Task 1 + truths[2] | 11 surfaces enumerated with live line numbers; residual sweep whitelists exactly 5 historical doc refs (verified live) |
| REL-1x-01: registration surfaces (catalog, SKILLS.md, packs.html, NOTICE, README, cursor manifest) | Registration itself shipped in Phase 7 (e00ac7d: catalog 61 / cursor 62, verified live); Phase 9 verifies via gates + packs.html byte-identity | Task 4 steps 1-2; CHANGELOG Changed section names the registered surfaces (Task 2) |
| SC2 / REL-1x-02: v1.18.0 tagged + GitHub Release | Task 5 (annotated colon-style tag, push --follow-tags, gh release create, ls-remote + gh release view closure) | truths[4]; reversibility rated costly with rationale |
| SC2: CHANGELOG includes v1.17.0 wording correction | Task 2 Fixed item 1 (CHANGELOG.md:58 claim corrected: docs/index.html is a version surface, not a registration surface) | verified live: CHANGELOG.md:58 lists index.html under "Registered ... on every surface" |
| SC2: CHANGELOG includes doe-o-413-3 rename note, leading | Task 2 first-paragraph structure, hard-coded as LEADS; release-notes check in Task 5 verify | rename + alias verified live in catalog.json (slug doe-o-413-3, alias doe-413-3b) |

## Routed-item Coverage

| Routed item (source) | Plan task | Status |
|---|---|---|
| IN-04 map_version ↔ RELEASE-INFO reconciliation (8-GAP_ANALYSIS) | Task 1 (bump reconciles; verify asserts both 1.18.0) + Task 6 record | covered |
| IN-01 CONTRACT "cluster 30" numeric ref (8-GAP_ANALYSIS, conditional "if doc touched") | Task 3.1 — doc IS touched (Task 2/3 edit CHANGELOG + SOURCE-VETTING), so included | covered |
| 7-GAP_ANALYSIS CHANGELOG caveats (vva ~2011 dates, faa Rev F vs Rev E, 40051 1168-vs-584, rename note leads, v1.17.0 wording fix, OUSD typo) | Task 2 (caveats folded into one-liners; rename leads; wording fix Fixed[1]) + Task 3.2 (OUSD at SOURCE-VETTING.md:130, verified live) | covered |
| CI/local scan-skip duplication risk | Task 2 explicitly forbids restating it (already in 1.17.0 Changed — verified live) | covered |
| v1.19 backlog carry (FUT-04, FUT-05, IN-02, thin clusters 3/5/15) | Task 6 | covered |

## Quality Gates

- Chapter counts: plan carries live PACK.yaml values (dote-te-guidebook=8, faa-std-025=6, federal-bca=6, dafman-63-119=7, mil-std-881f=7, mil-std-40051=8, dod-vva-rpg=10) with a re-read-before-write instruction and a non-uniformity tripwire; verify greps each PACK.yaml.
- Staging safety: explicit-path-only add, git status audit, STOP on untracked strays (docs/ROLE-AGENTS-REQUIREMENTS-V2.md verified tracked since 05eb9ad).
- claim_verification block: 13 claims, all VERIFIED against live commands (none ASSUMED/FAILED).
- Structure validation: gsd-tools frontmatter.validate valid=true; verify.plan-structure valid=true, 6/6 tasks complete, zero errors/warnings.
- Em-dash/URL constraints on the CHANGELOG entry carried from the proven Phase 5 plan; tag style verified against live `git tag -l -n3 v1.17.0` (colon).
- Bash validity: all verify commands are plain grep/python/git/gh invocations used elsewhere in this repo's proven plans.

## Findings

1. (Observation, no fix) REL-1x-01's registration work landed in Phase 7, not Phase 9; Phase 9 discharges REL-1x-01 via full-gate validation + surface synchronization. This matches the ROADMAP Phase 9 goal wording ("Catalog, docs, and manifests synchronized").
2. (Observation, no fix) The 1.17.0 residual-version sweep cannot return absolute zero — 5 historical doc references (CONTRACT:54, pack-map.md:16, SOURCE-VETTING.md x3) correctly record v1.17.0 history. The plan whitelists exactly these 5, enumerated with line numbers.

**Verdict:** PASS

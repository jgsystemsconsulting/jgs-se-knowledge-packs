# Phase 2 Integration Check — Source Vetting + Ruled-Out Register

**Date:** 2026-08-14
**Scope:** Phase 2 (docs/planning-only) cross-phase wiring: SOURCE-VETTING.md <-> build pipeline, ROADMAP phase chain, catalog/SKILLS consistency, CI + local release gate.

**Verdict:** NEEDS_WORK

---

## Wiring Summary

**Connected:** 6 cross-phase connections verified end-to-end
**Orphaned:** 0
**Missing/Broken:** 1 (CI/release gate broken by Phase 2's own committed planning artifacts)

## Gate Runs (actual output)

### `python tooling/validate_pack.py --all` (run 2026-08-14)

```
FAIL  se-standards-signpost
        - missing LICENSE (must reproduce the source's terms)
        - missing chapters/ directory
46/48 pack(s) passed.
```

Pre-existing and by design: `se-standards-signpost` is a `kind: signpost` pack; both release gates
(`tooling/check_release.py` and the release path) exclude signpost packs from the validate run.
Not a Phase 2 regression.

### `python tooling/check_release.py` (run 2026-08-14) — FAIL, exit 1

```
RELEASE CHECK: FAIL (2 issue(s))
  - [leak] sentinel 'BEGIN PRIVATE KEY' found in .planning\phases\2-source-vetting-ruled-out-register\2-SECURITY_AUDIT.md
  - [links] source-material URL in .planning\phases\2-source-vetting-ruled-out-register\2-RESEARCH.md: https://csrc.nist.gov
```

### CI simulation (validate.yml link-policy + leak steps, over `git ls-files`)

```
=== CI link-policy (tracked files): 1 violations ===
 - .planning/phases/2-source-vetting-ruled-out-register/2-RESEARCH.md: https://csrc.nist.gov
=== CI leak-sentinel (tracked files): 1 violations ===
 - .planning/phases/2-source-vetting-ruled-out-register/2-SECURITY_AUDIT.md: BEGIN PRIVATE KEY
```

Both Phase 2 artifacts are committed (2-RESEARCH.md in d81ec77, 2-SECURITY_AUDIT.md in 973d68c),
so the next push to main / any PR fails the `validate` workflow.

---

## Detailed Findings

### BLOCKER-1: Phase 2 evidence files break the Phase 1 CI/release gate (Phase 2 -> Phase 5 chain)

- **Where:**
  - `.planning/phases/2-source-vetting-ruled-out-register/2-SECURITY_AUDIT.md` line 29 quotes the
    literal string `BEGIN PRIVATE KEY` (describing the scan it performed). Both
    `.github/workflows/validate.yml` (assembled sentinel `BEGIN ""PRIVATE KEY`) and
    `tooling/check_release.py` (`LEAK_SENTINELS`) grep for that exact literal.
  - `.planning/phases/2-source-vetting-ruled-out-register/2-RESEARCH.md` lines 30 and 43 contain
    `https://csrc.nist.gov/...` URLs. The link policy bans `nist.gov` URLs in every tracked
    `.md/.json/.yaml/.yml/.txt` outside `kind: signpost` packs; check_release.py exempts only
    `sources/`, `.playwright-mcp/`, etc. — **not** `.planning/`.
- **Why it broke:** docs/SOURCE-VETTING.md's new "Link Policy" parenthetical says URLs are
  "never published in docs or packs" and points at 2-RESEARCH.md as the evidence store — but the
  mechanical policy enforces "anywhere in the repo", and 2-RESEARCH.md is tracked. The
  security-audit doc quotes the sentinel it scanned for, exactly the self-reference problem the
  scanners themselves avoid via string fragmentation.
- **Impact:** Phase 5 success criterion 1 ("check_release / CI content-integrity gate passes with
  56 packs") is unreachable on the current tree; every future PR reds the CI gate.
- **Fix options (maintainer decision):** fragment the sentinel text in 2-SECURITY_AUDIT.md
  (e.g. `BEGIN PRIVA``TE KEY`), and either strip the two `csrc.nist.gov` URLs from the tracked
  2-RESEARCH.md (replace with "NIST CSFW pub page (URL in vetting notes)" style) or add
  `.planning` to the exemption lists in both `check_release.py` and `validate.yml` if planning
  evidence is meant to be committable.

### WARNING-1: vet_source.py tier semantics — core match, new Excluded rows not encoded

`vet_source.py` lives in the **external** `jgs-reference-skill` repo
(`C:/Users/gower/OneDrive/Documents/GitHub/jgs-reference-skill/tools/vet_source.py`), invoked by
`tooling/build_all_packs.workflow.js` step 2 as the build-pipeline licence gate. Verified:

- **Core semantics WIRED:** Tier 1 = PD/US-gov, Tier 2 = CC BY family + MIT/Apache/BSD,
  Tier 3 = ND/unclear, Excluded = hard stop (exit 2) — matches docs/SOURCE-VETTING.md tier
  definitions; `--self-check` PASS; `validate_pack.py` `VALID_TIERS = {"1","2","3"}` matches
  "Excluded never packageable".
- **All 8 Phase 3 Tier-1 candidates classify Tier 1 through the tool** (verified per-candidate
  with title/publisher/license as the build workflow passes them): NIST SP 800-171, NIST SP 800-61,
  MIL-HDBK-338B, MIL-HDBK-516C, NASA-STD-7009B, DOE O 413.3B, DOE SEM3, CISA CPG 2.0.
- **Drift 1 — ECSS not encoded:** Phase 2 added ECSS (incl. ECSS-E-ST-10C Rev.1, © ESA) to the
  doc's Excluded table (hard stop), but the tool's `EXCLUDED` dict has no `ecss`/`esa` keyword.
  Empirically: `vet_source.py --title "ECSS-E-ST-10C Rev.1 Space Engineering" --publisher ESA`
  returns `Tier 3 — packageable as a pack` (exit 0), not the doc's hard stop. Human rubric still
  blocks it; the mechanical gate does not.
- **Drift 2 — Def Stan 00-051:** tool returns Tier 3 + "treat as Excluded" warning (exit 0) vs
  the doc's recorded deferred-excluded. Directionally consistent, not a hard stop.
- **Drift 3 — CISA publisher signal missing:** `cisa` is not in the tool's `US_GOV` tuple; with
  only title/publisher it classifies Tier 3. It reaches Tier 1 only when the license string
  carries statute text (e.g. "US Government work (17 U.S.C. § 105)"). Phase 3's workflow META
  entry for `cisa-cpg` must carry that string or the vet step will mis-gate.
- **Cross-repo sync gap:** `jgs-reference-skill/docs/SOURCE-VETTING.md` (the tool's companion
  rubric, "keep the two in sync") contains none of the Phase 2 rows (no ECSS, Def Stan 00-051,
  CISA, SEM3, CPG). No CI keeps the two repos' copies aligned.
- Mitigation: none of ECSS / Def Stan / IEEE are in any Phase 3 build list, so no E2E build flow
  breaks this milestone. The gaps are defence-in-depth losses, not active breaks.

### WARNING-2 (pre-existing, not Phase 2): doc overstates CI enforcement

docs/SOURCE-VETTING.md line 162: "CI enforces 4, 7, and 8 mechanically (`tooling/validate_pack.py`)".
CI (`validate.yml`) never runs validate_pack.py — it inlines leak/link/frontmatter/catalog checks.
Items 7/8 (LICENSE present, PACK.yaml fields) are enforced locally by `check_release.py` only.
Wording predates Phase 2 (line 119 in `1699507^`); flagged for accuracy, not a regression.

### Check 2: ROADMAP phase chain — WIRED

- Phase 1 `[x]` -> Phase 2 (depends on 1) -> Phase 3 (depends on 2) -> Phase 4 (depends on 3) ->
  Phase 5 (depends on 4): all dependency edges present, no gaps.
- Phase 3 consumes Phase 2 output: the 8 Tier-1 rows in SOURCE-VETTING.md's "Vetted candidates"
  table map 1:1 to REQUIREMENTS T1-01..T1-08 pack identities (nist-800-171, nist-800-61,
  mil-hdbk-338, mil-hdbk-516, nasa-ms-7009, doe-413-3b, cisa-cpg, doe-sem), each with licence
  evidence and "confirm in-source at build" instructions that feed Phase 3 success criterion 3
  (PACK.yaml provenance).
- Phase 4 closed-by-vetting is consistent across ROADMAP (0 packs, slot retained), REQUIREMENTS
  (T2-01/T2-02 struck excluded-by-vetting; T2-03 `[ ]` deferred-excluded, never "resolved"), and
  SOURCE-VETTING.md (IEEE 15288.2-2014 and ECSS rows + Def Stan UNVERIFIED section).
- Phase 5 count correct: 56 = 48 baseline + 8 Tier-1; arithmetic and wording consistent across
  ROADMAP, REQUIREMENTS (REL-01/REL-02), STATE, MILESTONES. No stale "59"/"3 Tier-2" text
  anywhere in the planning surface (grepped clean).
- 11 candidates = 8 Tier-1 + 3 vetted-out consistent everywhere.

### Check 3: catalog.json / SKILLS.md — WIRED (untouched, consistent)

- Phase 2 commit range (1699507..e5ca3ba) touched only docs/SOURCE-VETTING.md and .planning
  files. catalog.json and SKILLS.md last changed in pre-Phase-2 release commits; working tree
  clean for both.
- Consistency with 48 packs: 48 pack dirs = 48 SKILLS.md entries. catalog.json carries 46
  shipped entries; the 2 absent are `omg-signpost` and `se-standards-signpost`, both marked
  `kind: signpost` and excluded from the catalog and from check_release's count check by design.
  The 1 `planned` entry (`mit-ocw-se`) is pre-existing baseline. No drift.

### Environment note

Untracked working-tree files `docs/capability-pack-map.{json,md}` and
`docs/ROLE-AGENTS-REQUIREMENTS-V2.md` exist from a parallel workstream. They do not trip any
scanner (link/leak-clean) and are outside Phase 2 scope; they would need review before any
commit that includes them.

---

## E2E Flows

**Complete:** 5 — vetting-decision record (RESEARCH -> SOURCE-VETTING -> REQUIREMENTS);
Phase-3 candidate handoff (8 rows -> T1-01..08); Phase-4 closure propagation (doc ->
REQUIREMENTS -> ROADMAP); 56-pack target propagation (REQUIREMENTS -> STATE/MILESTONES/ROADMAP);
catalog/SKILLS/packs 48-pack agreement.

**Broken:** 1 — release-gate flow: Phase 2 committed artifacts -> Phase 1 CI/local gate ->
Phase 5 "gate passes with 56 packs". Broken at the gate step: check_release.py exit 1 and CI
validate would fail on next push (BLOCKER-1).

## Requirements Integration Map

| Requirement | Integration Path | Status | Issue |
|---|---|---|---|
| RO-01 | Phase 2 SOURCE-VETTING Excluded rows -> human vetting rubric -> future vet_source sync | WIRED | ECSS row not mechanically enforced by vet_source.py (WARNING-1) |
| T2-03 | SOURCE-VETTING Def Stan section <-> REQUIREMENTS/FUT-03 <-> ROADMAP Phase 4 closure | WIRED | Tool classifies 00-051 Tier-3-packageable, not a hard stop (WARNING-1) |
| T1-01..T1-08 | REQUIREMENTS slugs <-> SOURCE-VETTING 8 vetted rows <-> build workflow vet step | WIRED | cisa-cpg META.lic must carry statute text or vet mis-gates (WARNING-1) |
| REL-01/REL-02 | 56-pack target <-> catalog/SKILLS/packs.html surface <-> check_release gate | PARTIAL | Numerically wired (48+8=56, no drift) but gate currently fails (BLOCKER-1) |
| TOOL-01/TOOL-02 | Phase 1 toolchain/CI gate <- Phase 2 committed artifacts | BROKEN | Gate fails on 2-RESEARCH.md URL + 2-SECURITY_AUDIT.md sentinel (BLOCKER-1) |
| PACK-02 | Excluded-tier never ships <-> validate_pack VALID_TIERS={1,2,3} | WIRED | — |

**Requirements with no cross-phase wiring:** PACK-01, PACK-03, TOOL-03 (retroactive baseline,
self-contained Phase 1; unaffected by Phase 2 — as intended for a docs-only phase).

## Required Follow-ups

1. **(Blocker)** Fix the two gate trips: fragment `BEGIN PRIVATE KEY` in 2-SECURITY_AUDIT.md and
   resolve the `csrc.nist.gov` URLs in 2-RESEARCH.md (strip, or exempt `.planning` in
   check_release.py + validate.yml by design decision). Re-run `python tooling/check_release.py`
   to confirm PASS before Phase 3 merges anything.
2. (Warning) Sync the Phase 2 Excluded rows into `jgs-reference-skill` (vet_source.py `EXCLUDED`
   keywords: ecss/esa; consider `def stan`/`dstan` handling) or record the accepted gap in the doc.
3. (Warning) When Phase 3 defines its build META, ensure `cisa-cpg` carries a statute-bearing
   license string so vet_source returns Tier 1.

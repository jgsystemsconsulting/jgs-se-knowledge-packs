---
phase: 7-gap-driven-pack-builds
kind: integration_check
subsystem: knowledge-packs
scope: cross-phase (Phase 3 pipeline -> Phase 7 packs -> registration surfaces -> Phase 8 map chain)
date: 2026-08-14
verdict: PASS_WITH_NOTES
---

# Phase 7 Integration Check — 7 GP Packs End-to-End

**Verdict:** PASS_WITH_NOTES

Cross-phase audit of the Phase 7 deliverable chain: pack builds (7-01/7-02) ->
registration sweep (7-03) -> consumer surfaces (installers, docs, manifests) ->
Phase 8 capability-map chain. Every expected connection was traced live (commands
re-executed, not trusted from summaries).

## Wiring Summary

**Connected:** 9 connection groups verified end-to-end
**Orphaned:** 0
**Missing:** 0
**Warnings:** 3 (bookkeeping only, no flow breaks)

## Connection Verification (all re-executed)

### 1. install.py --dry-run discovers 63 packs — WIRED

`python install.py --dry-run` prints exactly 63 `would install` lines; `packs/`
contains exactly 63 directories. All 7 new slugs appear in the dry-run list
(sebok included — sebok ships via installer; only the cursor commercial manifest
excludes it).

### 2. catalog.json — WIRED

- JSON-valid (stdlib `json.load` OK)
- 61 entries; 0 slug collisions (61 unique slugs)
- `updated` bumped 2026-08-15 -> 2026-08-16 (verified via `git show
  c9d5e7e:catalog.json`; that revision had 54 entries / 2026-08-15)
- All 7 new slugs present: dod-vva-rpg, faa-std-025, dote-te-guidebook,
  dafman-63-119, mil-std-881f, federal-bca, mil-std-40051
- catalog slugs == packs/ dirs minus the 2 signposts exactly (no orphan in
  either direction); `planned` section unchanged (mit-ocw-se, Tier 2)
- federal-bca catalog `source_version` honestly records the A-94-only rescope

### 3. gen_packs_page.py idempotence — WIRED

`python tooling/gen_packs_page.py` reports "63 packs" and the regenerated
`docs/packs.html` is byte-identical to the committed file (`cmp` clean; `git
status` empty afterwards). `check_release.py` gate 5c independently re-renders
and would fail on drift — it passes.

### 4. check_release.py — WIRED (PASS)

`python tooling/check_release.py` -> "RELEASE CHECK: PASS". The gate is not a
rubber stamp: it re-runs `validate_pack` on all 63 packs, asserts SKILLS.md
count == shipped packs, asserts the cursor manifest set equals packs/ minus
`commercial_use: false` packs, re-renders packs.html for staleness, and checks
version single-sourcing (plugin.json == CHANGELOG == RELEASE-INFO).

### 5. SKILLS.md — WIRED

Header states "61 packs (+2 signposts)". Table parses to 63 data rows = 61
packs + 2 signposts (omg-signpost, se-standards-signpost); no duplicate slugs;
all 7 new packs have rows.

### 6. Cursor manifest — WIRED

`.cursor-plugin/plugin.json` has 62 unique skill paths, all of form
`./packs/<slug>/SKILL.md`; all 7 new packs present; `sebok` excluded (CC
BY-NC-SA, `commercial_use: false` — excluded by check_release gate 6b rule,
not ad hoc); cursor set == packs/ dirs minus sebok exactly (63 - 1 = 62,
including both signposts).

### 7. README — WIRED

- Badge line 11: `packs-61`
- Catalogue table: 62 slug rows = 61 live packs + 1 pre-existing planned row
  (`mit-ocw-se`, marked "🔜 planned" — consistent with catalog `planned`)
- All 7 new rows present (lines 164-170) with per-pack chapter counts that
  match the actual `chapters/` contents exactly: dod-vva-rpg 10, faa-std-025 6,
  dote-te-guidebook 8, dafman-63-119 7, federal-bca 6, mil-std-881f 7,
  mil-std-40051 8

### 8. NOTICE — WIRED

61 `[pack: <slug>]` sections; all 7 new packs present (lines 634-694).

### 9. ROADMAP Phase 7 -> Phase 8 chain — WIRED

- Phase 8 declares **Depends on: Phase 7**; Phase 9 depends on Phase 8
- Phase 8 SC-2 and REQUIREMENTS AE-02 both encode the hard downstream asserts:
  "cluster 25 non-empty and clusters 3/5/15 no longer critical"
- 7-RESEARCH §5 baseline table was verified against the live
  `docs/capability-pack-map.json` (cluster numbering is 1-based):
  - 570 entries / 32 clusters — matches §5 exactly
  - cluster 25 "Training & Documentation Delivery" = 0 entries / 0 packs
    (EMPTY) — mil-std-40051's 8 chapters are entirely technical-manual /
    documentation-delivery vocabulary, so the fattening target is real
  - cluster 15 "Opportunity/Benefit Management" = 1 entry / 1 pack (worst) —
    federal-bca's 6 chapters are benefit-cost/discounting content
  - cluster 9 "Test & Evaluation" = 11/1 single-source; cluster 23
    "Logistics, Supportability & Sustainment" = 11/1 — dote-te-guidebook,
    dafman-63-119, dod-vva-rpg chapter sets are T&E/readiness/VV&A oriented
  - None of the 7 new packs appear in the current map (correct: map covers
    exactly the 54 pre-Phase-7 catalog packs; regeneration including the new
    packs is Phase 8/AE-02 scope)

## Warnings (no flow breaks)

1. **ROADMAP.md line 77:** phase-level checkbox `- [ ]` for Phase 7 is
   unchecked although all three plans are `[x]` (lines 106-108) and summaries
   are complete. Phase 6 precedent (line 76) is checked. Likely ticked at
   phase close; cosmetic.
2. **STATE.md header:** still `current_phase: 6` / "Current focus: Phase 6"
   while Phase 7 P01-P03 execution rows exist in the same file (lines 48-50).
   Stale pointer; phase-close step presumably updates it.
3. **capability-pack-map.json** carries no schema/version/generated-on
   metadata and no regeneration script exists under tooling/ yet. This is by
   design (AE-01..03 are Phase 8 scope; Phase 8 plans TBD), so the chain is
   intact — but Phase 8 must build the generator before its SC-1/SC-2 asserts
   can run. Baseline numbers inherited from 7-RESEARCH §5 verified accurate.

## E2E Flows

**Complete:** 7/7
- Pack build -> validate -> overlap -> scan -> commit (7-01/7-02/7-03
  summaries; re-confirmed collectively by check_release gate 5)
- Pack dir -> catalog -> SKILLS.md -> README -> NOTICE -> packs.html ->
  cursor manifest -> installer discovery (all surfaces reconcile at 61/62/63
  with no orphans in either direction)
- Phase 7 builds -> Phase 8 map targets (baseline clusters verified; target
  packs carry the cluster vocabulary Phase 8 harvests)

**Broken:** 0

## Requirements Integration Map

| Requirement | Integration Path | Status | Issue |
|-------------|-----------------|--------|-------|
| GP-01 | dod-vva-rpg build -> catalog/SKILLS/README/NOTICE/cursor -> clusters 7/8/9/16 (Phase 8) | WIRED | — |
| GP-02 | faa-std-025 build -> all registration surfaces -> clusters 3/5/12 | WIRED | — |
| GP-03 | dote-te-guidebook build -> all registration surfaces -> clusters 7/8/9/23 | WIRED | — |
| GP-04 | dafman-63-119 build -> all registration surfaces -> clusters 6/9/27 | WIRED | — |
| GP-05 | mil-std-881f build -> all registration surfaces -> clusters 17/26 | WIRED | — |
| GP-06 | federal-bca (A-94-only rescope) -> all registration surfaces -> clusters 15/16/17 | WIRED | — |
| GP-07 | mil-std-40051 build -> all registration surfaces -> clusters 24/25 | WIRED | — |
| AE-01..03 (Phase 8) | inherit Phase 7 packs; map regeneration + cluster asserts | WIRED (handoff verified) | generator script is Phase 8 work (by design) |

**Requirements with no cross-phase wiring:** none — every GP requirement
touches build -> registration -> Phase 8 map chain.

## Evidence Commands

```
python install.py --dry-run          # 63 would-install lines
python tooling/check_release.py      # RELEASE CHECK: PASS
python tooling/gen_packs_page.py     # 63 packs; byte-identical (cmp)
python -c "json.load(open('catalog.json'))"  # 61 entries, 0 collisions, updated 2026-08-16
```

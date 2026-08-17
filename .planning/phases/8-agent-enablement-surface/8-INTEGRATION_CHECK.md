# Phase 8 Integration Check — Agent-Enablement Surface

**Range audited:** `d821099..ab42f7a` (dc35907 map v2, 1c32f59 CONTRACT, ab42f7a link; gate itself introduced at range base d821099)
**Date:** 2026-08-17
**Method:** live gate runs on current tree + sandboxed mutation tests (temp copy of `packs/` + gate + map; real tree untouched), JSON programmatic reads, doc/link cross-checks.

**Verdict:** PASS_WITH_NOTES

## Wiring Summary

| # | Connection | Status | Evidence |
|---|---|---|---|
| 1 | Gate ↔ `packs/` ↔ map JSON (staleness) | WIRED | `python tooling/check_capability_map.py` exit 0 on current tree (32 clusters, 628 entries, 61/61 chapter-bearing packs mapped). Sandbox mutations all forced RED: new chapter file → exit 1 (`chapter-set: on disk not in map`); deleted chapter → exit 1 (`map_only` + `existence`); brand-new pack with `chapters/` → exit 1 (`staleness: pack on disk not in map`). The gate cannot stay green through a pack change that requires map refresh. |
| 2 | `check_release.py` untouched + PASS | WIRED | `git diff --name-only d821099..ab42f7a` = exactly 3 docs files; last change to `tooling/check_release.py` is 02126ac (pre-range). `python tooling/check_release.py` → `RELEASE CHECK: PASS`, exit 0. Gate is standalone as documented (no import of/`grep capability` in check_release.py — Phase 9 wiring deferred by design). |
| 3 | CONTRACT linked and resolvable | WIRED | `docs/capability-pack-map.md:14` (rules-of-construction block): "Consumption contract (schema, versioning, refresh): see `docs/capability-map-CONTRACT.md`" — target file exists (97 lines, 5 sections matching SUMMARY SC-3). |
| 4 | Downstream consumer compat (FR-2.1) | WIRED | Loaded JSON: top-level `{schema_version: 2 (int), map_version: "1.18.0", generated_on: "2026-08-17", clusters: [32]}`; cluster names all unique; 628/628 entries carry valid string `pack` + `chapter`; `note` present. Primary read `clusters[].name → chapters[].{pack, chapter}` works verbatim; v1 access `data["clusters"]` still works (additive envelope), matching CONTRACT §3 and ROLE-AGENTS-REQUIREMENTS-V2 FR-2.1/FR-2.3. |
| 5 | Map `.md` ↔ map `.json` sync | WIRED | Summary table in `capability-pack-map.md` (32 rows, Total 628) matches gate cluster counts exactly (spot: Safety 88, Cyber 69, Measurement 36, Risk 27). Contract §4 step 2 (sync both) honored. |
| 6 | ROADMAP Phase 8→9 chain | WIRED | `.planning/ROADMAP.md`: Phase 8 `[x]` (depends Phase 7 `[x]`); Phase 9 `[ ]` "Depends on: Phase 8". STATE: current_phase 8, ready_for_verification. Chain intact. |
| 7 | Phase 7 → Phase 8 pack handoff | WIRED | All 7 GP packs present with entries: dod-vva-rpg 10, dote-te-guidebook 8, mil-std-40051 11, dafman-63-119 7, mil-std-881f 7, faa-std-025 6, federal-bca 9. Thresholds live: C25 12≥1, C3 3≥3, C5 4≥3, C15 10≥2. |

## E2E Flows

**Complete (5):**
1. Pack change → gate detects → map refresh required (verified RED on 3 mutation classes in sandbox).
2. se-agents consumer → `schema_version == 2` check → `clusters[].name → {pack, chapter}` read (verified by direct load).
3. v1 consumer → `data["clusters"]` → still resolves on v2 (verified).
4. Refresh path → write json + md → gate exit 0 (current tree is the passing end-state; md/json in sync).
5. Release gate independence → check_release PASS with map gate standalone (both run green on current tree).

**Broken:** none.

## Notes (non-blocking)

1. **AE-01 wording vs implementation (WARNING):** REQUIREMENTS.md AE-01 asks for "a stdlib export/regenerate script under tooling/". `tooling/` contains only the checker (`check_capability_map.py`); regeneration is an agent classification procedure per CONTRACT §4 (SUMMARY claims byte-identical regen, but the regen writer is not committed tooling). The versioned-consumable + staleness-gate intent is fully met; reproducible regeneration rests on a documented procedure, not executable code.
2. **Commit hygiene:** 1c32f59's message says "link from map header" but its diff adds only CONTRACT.md; the link actually landed in ab42f7a. Net state at ab42f7a is correct (SUMMARY Deviation #1 discloses this).
3. **Version anticipation:** `map_version: "1.18.0"` while `RELEASE-INFO.txt` says 1.17.0 (v1.18.0 untagged until Phase 9). Contract defines map_version as tracking the release that regenerated the map; regeneration happened on the v1.18 body. Phase 9 tagging reconciles; check_release.py does not read the map, so no gate conflict today.
4. **Signpost packs:** chapter-less packs (`omg-signpost`, `se-standards-signpost`) are excluded from staleness by design (documented in gate docstring + map md rule) — a new chapter-less pack would not force a map refresh. Documented behavior, not a bypass of chapter coverage.

## Requirements Integration Map

| Requirement | Integration Path | Status | Issue |
|---|---|---|---|
| AE-01 | map JSON envelope ↔ gate (`tooling/check_capability_map.py` ↔ `packs/`) | PARTIAL | Envelope + staleness gate wired and live-verified; the promised export/regenerate *script* is an agent procedure, not committed tooling (Note 1) |
| AE-02 | Phase 7 packs → map classification → gate thresholds | WIRED | — |
| AE-03 | CONTRACT doc → link from map md → se-agents consumer (cross-repo) | WIRED | — |
| REL-1x-01/02 (Phase 9) | check_release.py untouched; PASS preserved as pre-state | WIRED | — |
| FR-2.1 (external) | JSON `clusters[].name → chapters[].pack/chapter` verified by load | WIRED | — |
| GP-01..07 (Phase 7) | 7 packs → 52 chapters mapped → cluster deltas per SUMMARY | WIRED | — |

**Requirements with no cross-phase wiring:** none in Phase 8 scope (AE-01..03 all have integration touchpoints above).

# Phase 8 Verification — Agent-Enablement Surface (AE-01..03)

Date: 2026-08-14
Method: goal-backward against ROADMAP Phase 8 SCs; every check executed live against the tree at 6f7b54b.

**Verdict:** passed_with_notes

## Goal

ROADMAP Phase 8: "capability-pack-map.json is a stable, versioned consumable for the se-agents generator." — Met: the map carries the v2 envelope, is gate-checked by a stdlib validator wired to the packs/ filesystem, and its contract is documented and linked for the downstream repo. The single note is the honestly-annotated AE-01 wording deviation (gate-not-generator), adjudicated in 8-GAP_ANALYSIS.md #2.

## Per-SC evidence

### SC-1 / AE-01 — map carries schema + version + generated-on; regeneration idempotent and gate-checked

- Envelope read live from `docs/capability-pack-map.json`: `{'schema_version': 2, 'map_version': '1.18.0', 'generated_on': '2026-08-17'}` — schema field + map version + generated-on all present; schema_version is int (strict type now gate-enforced post-6f7b54b).
- `python tooling/check_capability_map.py` → exit 0, all 32 cluster counts + "TOTAL: 628" + "PASS: capability map OK" (gate-checked).
- Idempotence, two readings (per plan review MI-05): (a) gate-output determinism — two consecutive runs byte-identical (re-confirmed by both code reviews; gate is a pure function of committed artifacts); (b) regeneration no-diff — agent-attested (8-01-SUMMARY SC-1b `JSON_BYTE_IDENTICAL_REGEN`), not tool-reproducible by design; the gate is the operational check (CONTRACT §4).
- Staleness detection is live: the RED run at d821099 (36 named issues: envelope + 7 missing packs + chapter-set mismatch + 4 thresholds, 0 existence failures) proves the gate detects drift; integration-check sandbox mutations (added/deleted chapter, new pack) all forced exit 1.
- **Note (honesty):** REQUIREMENTS AE-01's literal "stdlib export/regenerate script" was delivered as gate-not-generator (agent procedure per CONTRACT §4); AE-01's checkbox is earned on the requirement's intent with the deviation annotated in REQUIREMENTS (GP-06 pattern) and a FUT-05 backlog entry for a future deterministic generator. See 8-GAP_ANALYSIS.md #2.

### SC-2 / AE-02 — all v1.18 packs in map; cluster 25 non-empty; clusters 3/5/15 above critical thresholds

- 61/61 chapter-bearing packs mapped, 0 missing, 0 stale (gate staleness both directions + chapter-set equality, verified live and by both code reviews).
- Thresholds live (gate output this run): C25 = **12** (≥1; baseline 0 — EMPTY → non-empty); C3 = **3** (≥3; baseline 2); C5 = **4** (≥3; baseline 2); C15 = **10** (≥2; baseline 1). All four name-keyed asserts pass.
- Total entries 628 = 570 pre-existing (proven byte-identical vs d821099^, backward compat for `data["clusters"]` consumers) + 52 new chapters + 6 support files.
- Classification quality: 8-chapter spot-check across 6 packs (code review) 8/8 defensible; per-pack spot-check protocol recorded in 8-01-SUMMARY.
- **Note (carried, not a failure):** C3/C5/C15 remain THIN per gap-report §1 taxonomy (<8 entries or ≤2 packs); SC-2's "above critical thresholds" = the name-keyed minimums, honestly recorded — full fattening is a v1.19 gap-report item.

### SC-3 / AE-03 — contract documented (schema, versioning, refresh path)

- `docs/capability-map-CONTRACT.md` exists (97 lines, 5 sections: schema, versioning, v1-keyless deprecation, refresh path, threshold table); field-by-field accurate vs the actual JSON and the gate's THRESHOLDS dict (both code reviews + integration check).
- Linked from `docs/capability-pack-map.md` rules-of-construction block ("Consumption contract ...: see docs/capability-map-CONTRACT.md") — link resolves (integration check wiring #3).
- Downstream read verified: `clusters[].name → chapters[].{pack, chapter}` works verbatim on the committed JSON (FR-2.1); v1 access still works (additive envelope).

## Cross-checks

| Check | Result |
|---|---|
| `python tooling/check_capability_map.py` | exit 0, TOTAL 628, PASS |
| `python tooling/check_release.py` | exit 0, "RELEASE CHECK: PASS" (map gate standalone; no wiring — deferred to Phase 9 by design) |
| Negative tests on hardened gate (dup cluster name, float schema, bad map_version/generated_on shapes, non-UTF-8, path traversal/absolute support-file paths) | 6/6 exit 1 with named failures (this verification, sandboxed copies) |
| Version surfaces | map_version 1.18.0 vs RELEASE-INFO 1.17.0 — expected mid-train; Phase 9 reconciliation item (IN-04) |
| Requirements checkboxes | AE-01 [x] honest (annotated), AE-02 [x] earned, AE-03 [x] earned; ROADMAP Phase 8 [x] |

## Phase 9 handoff

- Reconcile RELEASE-INFO.txt/catalog.json/tag with map_version 1.18.0 (IN-04).
- Optional check_release §8 bullet wiring `check_capability_map.main()` (research §2, deferred).
- se-agents generator binds to schema_version 2, refuses unknown values.

---
phase: 8-agent-enablement-surface
plan: 01
subsystem: agent-enablement
tags: [capability-map, schema-v2, gate, se-agents, thresholds]

requires:
  - phase: 7-gap-closure-gp-packs
    provides: 7 GP packs (52 chapters) on disk under packs/
provides:
  - tooling/check_capability_map.py stdlib gate (v2 envelope, staleness, thresholds)
  - docs/capability-pack-map.json v2 (schema_version=2, map_version=1.18.0, 628 entries)
  - docs/capability-map-CONTRACT.md consumer contract for se-agents
affects: [9-release-surface, se-agents-generator]

actuals:
  tokens: 48630
  tasks: 5
  commits: 5

tech-stack:
  added: []
  patterns:
    - "stdlib-only standalone map gate (check_release.py header style, no import of check_release)"
    - "name-keyed threshold lookup (never array index)"
    - "support-file path branching: pack root vs chapters/"
    - "additive v2 envelope preserving data['clusters'] consumers"

key-files:
  created:
    - tooling/check_capability_map.py
    - docs/capability-map-CONTRACT.md
  modified:
    - docs/capability-pack-map.json
    - docs/capability-pack-map.md

key-decisions:
  - "Support files only for essentially single-cluster packs: mil-std-40051 (C25) and federal-bca (C15); faa-std-025 multi-cluster omits support files"
  - "faa-std-025 ch05 → Requirements Traceability; ch03/ch04 → Interface Management; ch02 → Training & Documentation; ch01 → Standards/Tailoring; ch06 → CM"
  - "mil-std-881f entirely → Technical Planning & Work Breakdown (C17)"
  - "Gate stays standalone; check_release wiring deferred to Phase 9"
  - "generated_on uses execution day 2026-08-17"

patterns-established:
  - "Gate RED-first on pre-envelope map, then GREEN after agent classification"
  - "Classification regen must be byte-identical (MI-05 SC-1 evidence)"
  - "Threshold floors are never weakened to pass"

requirements-completed: [AE-01, AE-02, AE-03]

coverage:
  - id: D1
    description: "check_capability_map.py stdlib gate with v2 envelope, bidirectional staleness, support-file path branching, uniqueness, name-keyed thresholds"
    requirement: AE-01
    verification:
      - kind: other
        ref: "python tooling/check_capability_map.py (RED pre-map exit=1; GREEN post-map exit=0 twice, byte-identical)"
        status: pass
    human_judgment: false
  - id: D2
    description: "Map JSON v2 envelope + 52 new chapters classified; clusters 25/3/5/15 above thresholds; 61 packs mapped"
    requirement: AE-02
    verification:
      - kind: other
        ref: "python tooling/check_capability_map.py + envelope/threshold asserts"
        status: pass
    human_judgment: false
  - id: D3
    description: "docs/capability-map-CONTRACT.md (schema/versioning/deprecation/refresh/thresholds) linked from map md"
    requirement: AE-03
    verification:
      - kind: other
        ref: "grep capability-map-CONTRACT.md docs/capability-pack-map.md; contract section greps"
        status: pass
    human_judgment: false

duration: 45min
completed: 2026-08-17
status: complete
---

# Phase 8 Plan 01: Agent-Enablement Surface Summary

**Versioned capability-pack map (v2 envelope, 628 entries) with stdlib gate and consumer contract for se-agents**

## Performance

- **Duration:** ~45 min
- **Started:** 2026-08-17T00:16:18Z
- **Completed:** 2026-08-17T00:55:00Z
- **Tasks:** 5/5
- **Files modified:** 4 (created 2, modified 2)

## Accomplishments

- Stdlib gate `tooling/check_capability_map.py` fails RED on pre-phase keyless map and GREEN on regenerated map (idempotent).
- Classified all 52 Phase-7 GP chapters (+ 6 support-file rows) into the 32 clusters; map total 570 → 628; 61/61 chapter-bearing packs mapped.
- Thin-cluster floors met: C25 0→12, C3 2→3, C5 2→4, C15 1→10.
- Consumer contract documented and linked for the se-agents generator.
- `python tooling/check_release.py` still PASS (gate standalone; check_release untouched).

## Task Commits

1. **Task 1: Write check_capability_map.py (RED)** - `d821099` (feat)
2. **Task 2: Classify 52 chapters + v2 envelope + md sync** - `dc35907` (feat)
3. **Task 3: Gate GREEN idempotent + regen byte-identical** - no file change (evidence only; documented here)
4. **Task 4: capability-map-CONTRACT.md** - `1c32f59` (docs) + link fix `ab42f7a` (docs)
5. **Task 5: SC verify + SUMMARY** - (this commit)

## SC / AE Evidence

### SC-1 / AE-01 — versioned, gate-checked map

Envelope keys on committed JSON:

| Key | Value |
|---|---|
| `schema_version` | `2` (int) |
| `map_version` | `"1.18.0"` |
| `generated_on` | `"2026-08-17"` |

**(a) Gate-output determinism (Task 3):** two consecutive `python tooling/check_capability_map.py` runs both exit 0 with byte-identical stdout (`GATE_GREEN_IDEMPOTENT`).

**(b) Regeneration no-diff (research §2 / MI-05):** re-ran the classification writer against the committed tree → `JSON_BYTE_IDENTICAL_REGEN` and `MD_BYTE_IDENTICAL_REGEN`.

**Task 1 RED run** (exit=1, 0 existence failures) — proves staleness/threshold path detects drift:

```
FAIL: 36 issue(s)
  - envelope: missing schema_version (expected int 2)
  - envelope: missing or empty map_version
  - envelope: missing or empty generated_on
  - staleness: pack on disk not in map: dafman-63-119
  - staleness: pack on disk not in map: dod-vva-rpg
  - staleness: pack on disk not in map: dote-te-guidebook
  - staleness: pack on disk not in map: faa-std-025
  - staleness: pack on disk not in map: federal-bca
  - staleness: pack on disk not in map: mil-std-40051
  - staleness: pack on disk not in map: mil-std-881f
  - chapter-set: mismatch vs packs/*/chapters (on_disk_only=52, map_only=0)
  - ... 52 on-disk-only chapter lines ...
  - threshold: 'Training & Documentation Delivery' has 0 entries, need >=1
  - threshold: 'Requirements Traceability & Allocation' has 2 entries, need >=3
  - threshold: 'Interface Management & ICIDs' has 2 entries, need >=3
  - threshold: 'Opportunity/Benefit Management' has 1 entries, need >=2
```

**Task 3 GREEN run** (exit=0):

```
  Requirements Traceability & Allocation: 3
  Interface Management & ICIDs: 4
  Opportunity/Benefit Management: 10
  Training & Documentation Delivery: 12
  TOTAL: 628
PASS: capability map OK
```

### SC-2 / AE-02 — packs mapped + thin-cluster floors

| Metric | Baseline | Final |
|---|---|---|
| Chapter-bearing packs mapped | 54 | **61** (0 missing, 0 stale) |
| Total map entries | 570 | **628** (+52 chapters + 6 support) |
| C25 Training & Documentation Delivery | 0 | **12** (≥1) |
| C3 Requirements Traceability & Allocation | 2 | **3** (≥3) |
| C5 Interface Management & ICIDs | 2 | **4** (≥3) |
| C15 Opportunity/Benefit Management | 1 | **10** (≥2) |

**Above baseline — SC-2 threshold minimums met.** C3/C5/C15 remain **THIN** per gap-report §1 taxonomy (< 8 entries OR ≤ 2 distinct packs) — improvement, not full remediation; carry to the v1.19 gap report.

#### Cluster deltas (52 chapters → which clusters fattened)

| Cluster | Δ | Donors |
|---|---|---|
| Training & Documentation Delivery | +12 | mil-std-40051 (8+3sf), faa-std-025 ch02 |
| Opportunity/Benefit Management | +9 | federal-bca (6+3sf) |
| Technical Planning & Work Breakdown | +7 | mil-std-881f (7) |
| Test & Evaluation | +5 | dote ch01/04/08, dafman ch01/05 |
| Modeling, MBSE & SysML | +4 | dod-vva ch01/02/03/07 |
| Governance, Reviews, Gates & Control Points | +4 | dafman ch02/03/04/07 |
| Interface Management & ICIDs | +2 | faa-std-025 ch03/ch04 |
| Verification | +2 | dote ch02, dod-vva ch05 |
| Validation | +2 | dote ch03, dod-vva ch08 |
| Requirements Traceability & Allocation | +1 | faa-std-025 ch05 |
| Integration | +1 | dafman ch06 |
| Digital Engineering & Digital Twins | +1 | dote ch06 |
| Configuration Management & Baselines | +1 | faa-std-025 ch06 |
| Data & Information Management | +1 | dod-vva ch09 |
| Risk Management | +1 | dod-vva ch10 |
| Cybersecurity & Security Engineering | +1 | dote ch05 |
| Logistics, Supportability & Sustainment | +1 | dote ch07 |
| Project/Program Management | +1 | dod-vva ch04 |
| Standards, Tailoring & Process Models | +1 | faa-std-025 ch01 |
| Assurance & System Assurance | +1 | dod-vva ch06 |

#### Spot-check protocol (Task 2)

For each new pack, SKILL.md When-to-use re-read; 3 chapters spot-checked:

| Pack | Single-cluster? | Sample chapters + rationale |
|---|---|---|
| **mil-std-40051** | YES → C25 + support | ch01 scope/TM family (doc production); ch04 style/format (TM delivery); ch08 plate exemplars (training shops). SKILL: "Primary Training & Documentation pack (cluster 25)". |
| **federal-bca** | YES → C15 + support | ch01 A-94 principles; ch02 measuring benefits/costs; ch06 reporting for decision use. SKILL: federal BCA/CEA — Opportunity/Benefit Management. |
| **faa-std-025** | NO (multi) | ch03 IRD content → C5 Interface; ch04 ICD content → C5; ch05 VRTM → C3 Traceability. ch01 process family → C30; ch02 format → C25; ch06 CM → C12. No support files. |
| **dote-te-guidebook** | NO | ch02 DT&E → C7 Verification; ch03 OT&E → C8 Validation; ch08 TEMP/STE → C9 T&E. No traceability/interface chapters (per plan). |
| **dod-vva-rpg** | NO | ch01 VV&A frame → C10 Modeling; ch08 validation fundamentals → C8; ch06 accreditation agent → C32 Assurance. |
| **dafman-63-119** | NO | ch01 MOTRC framework → C9 T&E; ch04 cert memo/gates → C29 Governance; ch06 ITT/integration → C6 Integration. |
| **mil-std-881f** | effectively C17 | ch01 WBS principles; ch06 App K common elements; ch07 sustainment CES (secondary logistics). All → Technical Planning & Work Breakdown. |

### SC-3 / AE-03 — contract documented

`docs/capability-map-CONTRACT.md` covers five sections:

1. Schema (v2 JSON shape; consumers check `schema_version == 2` first; FR-2.1 name → {pack, chapter})
2. Versioning (`schema_version` breaks only; `map_version` tracks release)
3. Deprecation (v1 keyless DEPRECATED; `data["clusters"]` still works)
4. Refresh path (agent pass → gate → commit both .json/.md)
5. Threshold table (four name-keyed minimums)

Linked from `docs/capability-pack-map.md` rules-of-construction:
`Consumption contract (schema, versioning, refresh): see docs/capability-map-CONTRACT.md.`

## Phase 9 handoff notes

- Optional `check_release.py` §8 bullet ("map gate passes" via `check_capability_map.main()`) is **deferred** to the Phase 9 release-surface plan per research §2 wiring recommendation.
- REL-1x-02 surfaces and `check_release.py` itself were **untouched** here; `python tooling/check_release.py` remains PASS.
- C3/C5/C15 still THIN by gap-report taxonomy — full fattening is a v1.19 gap-report item, not a Phase 8 blocker.
- se-agents generator should bind to v2 only and refuse unknown `schema_version`.

## Deviations from Plan

| # | Deviation | Plan reference | Proposed classification | Rationale |
|---|-----------|----------------|--------------------------|-----------|
| 1 | Task 4 split across two commits (contract file, then link line) | Task 4 | in-scope fix | First commit staged only CONTRACT.md after Edit race on md; link fixed immediately after |
| 2 | Task 3 produced no git commit | Task 3 done | in-scope fix | Gate green with zero map defects; plan allows "documented no-change" |

Or: plan substance executed as written (gate, classification, thresholds, contract).

### Auto-fixed Issues

None beyond the Task 4 link follow-up commit.

## Known Stubs

None.

## Threat Flags

None beyond plan threat model (T-8-01..05 mitigated as designed).

## Self-Check: PASSED

- FOUND: tooling/check_capability_map.py
- FOUND: docs/capability-pack-map.json (schema_version=2)
- FOUND: docs/capability-map-CONTRACT.md
- FOUND: commits d821099, dc35907, 1c32f59, ab42f7a
- FOUND: gate GREEN exit=0; check_release PASS

---
phase: 12-map-regen-hygiene-gate-wiring
plan: 01
subsystem: capability-map
tags: [map-regen, decision-analysis, thresholds, contract, MAP-19]

requires:
  - phase: 11-io-unlocking-packs-decision-analysis-remap
    provides: 11-02 IO-01 remap table + 16 unmapped chapters on disk
provides:
  - regenerated capability-pack-map.json (644 entries, 63 packs, DA 5/4)
  - MAP-19-03 three-row MOVE applied (not copied)
  - MAP-19-02 name-keyed THRESHOLDS >=4 for listed primaries
  - MAP-19-05 CONTRACT paragraph (628+ / 502 residue / Cyber+DE unbound)
affects: [phase-12-02-gate-wire, phase-13-release-surface]

actuals:
  tokens: 50609
  tasks: 3
  commits: 4

tech-stack:
  added: []
  patterns:
    - Agent classification + existing gate (no generator)
    - MOVE-not-copy remap uniqueness on (pack, chapter)
    - Name-keyed THRESHOLDS floors (never array index)

key-files:
  created:
    - .planning/phases/12-map-regen-hygiene-gate-wiring/12-01-SUMMARY.md
  modified:
    - docs/capability-pack-map.json
    - docs/capability-pack-map.md
    - docs/capability-map-CONTRACT.md
    - tooling/check_capability_map.py

key-decisions:
  - "is-gps-200n ch01 → Configuration Management (IRN/CCB), not Interfaces"
  - "dod-vva-rpg ch11 → Test & Evaluation, not Validation or Integration"
  - "nasa-std-8719-14 + is-gps-200n support files omitted (multi-cluster)"
  - "Integration floor held at 4/4; AAF still deferred; no raid"
  - "map_version stays 1.18.0; generated_on 2026-08-17"

patterns-established:
  - "MAP-19-03 is a MOVE: delete old cluster membership before insert"
  - "MJ-01 chapter-set (pack, chapter) set-diff is the T1 close gate, not pack slugs"

requirements-completed: [MAP-19-01, MAP-19-02, MAP-19-03, MAP-19-05]

coverage:
  - id: D1
    description: "Map regenerated: 16 chapters classified, three-row MOVE, envelope 2 / 1.18.0, 644 entries, chapter-set empty"
    requirement: MAP-19-01
    verification:
      - kind: other
        ref: "python tooling/check_capability_map.py"
        status: pass
      - kind: other
        ref: "python chapter-set packs/*/chapters vs JSON (pack, chapter) set-diff"
        status: pass
    human_judgment: false
  - id: D2
    description: "MAP-19-03 MOVE: DA exactly five locked rows / 4 packs; old clusters vacated"
    requirement: MAP-19-03
    verification:
      - kind: other
        ref: "python membership assert DA want-set + Opportunity/Assurance absence"
        status: pass
    human_judgment: false
  - id: D3
    description: "MAP-19-02 THRESHOLDS >=4; conjunct none of five primaries is <4 AND 1 pack"
    requirement: MAP-19-02
    verification:
      - kind: other
        ref: "python tooling/check_capability_map.py (twice, identical stdout)"
        status: pass
      - kind: other
        ref: "one-shot conjunct print of five listed primaries"
        status: pass
    human_judgment: false
  - id: D4
    description: "CONTRACT §6 live 628+/644, 502 residue, Cyber+DE unbound; §5 floors synced"
    requirement: MAP-19-05
    verification:
      - kind: other
        ref: "grep 628/502/Cybersecurity/Digital Engineering/unbound in capability-map-CONTRACT.md"
        status: pass
    human_judgment: false

duration: 31min
completed: 2026-08-17
status: complete
---

# Phase 12 Plan 01: Map regen + remap + floor + CONTRACT Summary

**Regenerated the capability-pack map to 644 entries / 63 packs, MOVEd three locked chapters into Decision Analysis (5/4), encoded MAP-19-02 floors ≥4, and documented live 628+ vs 502 residue with Cyber/DE unbound.**

## Performance

- **Duration:** 31 min
- **Started:** 2026-08-17T20:05:00Z
- **Completed:** 2026-08-17T20:36:06Z
- **Tasks:** 3
- **Files modified:** 4 production + this SUMMARY

## Start state (red gate)

`python tooling/check_capability_map.py` exited **1** with `FAIL: 19 issue(s)`:

- packs `is-gps-200n` + `nasa-std-8719-14` not in map
- `on_disk_only=16, map_only=0`
- 16 named chapter files unmapped (7 + 6 + leftover RPG ch11–ch13)
- Envelope still schema 2 / `map_version` `1.18.0` / 628 entries / 61 mapped packs
- DA 2/2; Opportunity held federal-bca ch04+ch06; Assurance held dod-vva-rpg ch06

## Accomplishments

- Classified all **16** unmapped chapters into existing 32 clusters. Support files for `nasa-std-8719-14` and `is-gps-200n` omitted (multi-cluster). Arithmetic: **628 + 16 = 644**.
- Applied locked MAP-19-03 **MOVE** (not copy). Decision Analysis is **5 entries / 4 packs**.
- Synced `docs/capability-pack-map.md` summary table + v1.19 changelog bullet (new slugs + leftover RPG + remap).
- Encoded MAP-19-02 name-keyed THRESHOLDS ≥4. Gate **PASS** twice, stdout identical.
- Added CONTRACT §6 live-snapshot paragraph; synced §5 threshold table. Gate remains standalone (12-02 wires it).

## Classification table (16 chapters)

| Pack | Chapter | Cluster | Rationale |
|---|---|---|---|
| nasa-std-8719-14 | ch01-scope-and-applicability.md | Operations, Maintenance & Disposal | NPR+standard pair for debris assessments (also Standards) |
| nasa-std-8719-14 | ch02-assessment-overview.md | Operations, Maintenance & Disposal | ODAR/EOMP assessment spine and tools |
| nasa-std-8719-14 | ch03-debris-released-normal-operations.md | Operations, Maintenance & Disposal | Normal-ops debris lifetime / object-year limits |
| nasa-std-8719-14 | ch04-explosions-breakups-collisions.md | Operations, Maintenance & Disposal | Passivation + collision limits; Safety secondary |
| nasa-std-8719-14 | ch05-postmission-disposal.md | Operations, Maintenance & Disposal | Disposal gold slice (protected-band exit, 0.90) |
| nasa-std-8719-14 | ch06-reentry-surviving-debris.md | Operations, Maintenance & Disposal | Reentry casualty / keep-out |
| nasa-std-8719-14 | ch07-special-classes-odar-eomp.md | Operations, Maintenance & Disposal | Special-class + ODAR/EOMP governance secondary |
| is-gps-200n | ch01-is-scope-and-change-control.md | Configuration Management & Baselines | IRN/ICWG/CCB change control (also Interfaces) |
| is-gps-200n | ch02-interface-definition-and-identification.md | Interface Management & ICIDs | Definition vs identification of a live IS |
| is-gps-200n | ch03-interface-criteria-pattern.md | Interface Management & ICIDs | Measurable RF/ICD shall pattern |
| is-gps-200n | ch04-nav-data-as-payload.md | Interface Management & ICIDs | NAV payload families as ICD content |
| is-gps-200n | ch05-time-and-definition-hygiene.md | Interface Management & ICIDs | Time / URA / CEI / reserved-invalid hygiene |
| is-gps-200n | ch06-appendices-as-a-map.md | Interface Management & ICIDs | Annex map for a live IS (not Standards dump) |
| dod-vva-rpg | ch11-te-vv-checklist.md | Test & Evaluation | T&E/V&V integration checklist; not Integration |
| dod-vva-rpg | ch12-developing-the-referent.md | Validation | Validation-referent identify/select/specify |
| dod-vva-rpg | ch13-conceptual-model-development-and-validation.md | Validation | Conceptual-model V&V before implementation |

Support files omitted for both new packs (multi-cluster). No extra support-file rows.

## Spot-check (When-to-use vs assigned clusters)

**nasa-std-8719-14** When-to-use: orbital-debris assessment, disposal, reentry, ODAR/EOMP.

- ch03 — Ops: normal-operations debris limits are in-service/disposal hygiene, not a process-definition.
- ch05 — Ops: postmission disposal is the IO-03 gold slice.
- ch07 — Ops with Governance note: ODAR/EOMP formats sit on top of the same disposal assessment.

**is-gps-200n** When-to-use: worked ICD/IS exemplar complementary to `faa-std-025`.

- ch01 — CM: chapter is DIST-A + PIRN/IRN/CCB paper trail, not the interface object.
- ch02 — Interfaces: definition vs identification is the ICD contract object.
- ch03 — Interfaces: criteria shall-pattern is how a live ICD writes measurable interface rules.

**leftover RPG** When-to-use: VV&A roles, referent, conceptual-model validation, T&E/V&V integration.

- ch11 — T&E: checklist partitions DT/OT vs V&V; do not force Integration (IO-05 is AAF).
- ch12 — Validation: referent is the validation comparison standard.
- ch13 — Validation: conceptual-model V&V starts validation before code.

Remap rows are locked, not judgment.

## MOVE confirmation (MAP-19-03)

| Pack | Chapter | Deleted from | Inserted into |
|---|---|---|---|
| federal-bca | ch04-uncertainty-and-sensitivity.md | Opportunity/Benefit Management | Decision Analysis & Trade Studies |
| federal-bca | ch06-reporting-and-decision-use.md | Opportunity/Benefit Management | Decision Analysis & Trade Studies |
| dod-vva-rpg | ch06-accreditation-agent-role.md | Assurance & System Assurance | Decision Analysis & Trade Studies |

Left in place: federal-bca ch01–ch03, ch05 + 3 support files (Opportunity 10→8). dod-vva-rpg ch08 still Validation. ch10 still Risk.

**DA membership after apply (5/4):**

- `nasa-ceh` / `ch06-nasa-ceh-decision-support-analyses.md`
- `nasa-se-handbook` / `ch34-6-8-decision-analysis.md`
- `federal-bca` / `ch04-uncertainty-and-sensitivity.md`
- `federal-bca` / `ch06-reporting-and-decision-use.md`
- `dod-vva-rpg` / `ch06-accreditation-agent-role.md`

## MJ-01 resolution

T1 close ran `python tooling/check_capability_map.py` plus an equivalent `packs/*/chapters` vs JSON `(pack, chapter)` set-diff (support-file suffix excluded). Result: **on_disk_only=0, map_only=0**. All 16 unmapped chapters landed. New-pack support files omitted with rationale (multi-cluster), not silently dropped as unmapped chapters. A two-slug stub cannot pass this close.

## Conjunct print (MAP-19-02)

```
Decision Analysis & Trade Studies: 5 entries / 4 packs  floor_fail=False
Validation: 7 entries / 4 packs  floor_fail=False
Integration: 4 entries / 4 packs  floor_fail=False
Interface Management & ICIDs: 9 entries / 4 packs  floor_fail=False
Operations, Maintenance & Disposal: 13 entries / 5 packs  floor_fail=False
```

Integration: **floor held; AAF still deferred; no raid.**

`check_capability_map.py` exit **0** (`PASS: capability map OK`); second run stdout identical.

## CONTRACT paragraph quote (MAP-19-05)

> The live committed snapshot is **628+** chapter entries — post-regen **644** (16 classified Phase-11 chapters, 0 new support-file rows). The **502** figure is residue from a historical ROLE-AGENTS-REQUIREMENTS-V2 draft count; consumers must read the live JSON, not 502. **Cybersecurity & Security Engineering** (live 69 entries / 10 packs) and **Digital Engineering & Digital Twins** (live 25 entries / 4 packs) remain **unbound**. Binding those clusters is se-agents-side work, not this milestone.

§4 still says the gate is standalone. §5 now matches THRESHOLDS (Interfaces ≥4; DA / Validation / Integration / Ops ≥4). Training 1 / Traceability 3 / Opportunity 2 unchanged.

## Phase 13 leftovers not stolen

- plugin / CHANGELOG / RELEASE-INFO still **1.18.0**; `map_version` still `"1.18.0"`
- catalog `dod-vva-rpg.chapters` still **10**
- no README new-slug rows; no generator script; no Cyber/DE bindings
- `grep -c http docs/SOURCE-VETTING.md` = **0**
- `check_release.py` still does not import the map gate (12-02)

## Task Commits

1. **Task 1: Agent-classify 16 chapters + MAP-19-03 MOVE + sync md** - `53099e0` (docs)
2. **Task 2: MAP-19-02 THRESHOLDS >=4 + conjunct verify print** - `7134474` (fix)
3. **Task 3: MAP-19-05 CONTRACT paragraph** - `48a2a63` (docs)

**Plan metadata:** (this SUMMARY commit)

## Files Created/Modified

- `docs/capability-pack-map.json` — 644 entries; schema 2; map_version 1.18.0; generated_on 2026-08-17
- `docs/capability-pack-map.md` — summary counts + v1.19 changelog + cluster tables
- `tooling/check_capability_map.py` — listed-primary floors ≥4
- `docs/capability-map-CONTRACT.md` — §5 floors + §6 live snapshot

## Decisions Made

- Followed research hints; chose CM for is-gps-200n ch01 (IRN/CCB) and T&E for leftover RPG ch11 (checklist is T&E/V&V integration, not Validation fundamentals).
- Omitted new-pack support files because both packs are multi-cluster.
- Did not raid Integration; floor held at 4/4.

## Deviations

None.

## Deviations from Plan

None - plan executed exactly as written.

## Issues Encountered

None.

## User Setup Required

None - no external service configuration required.

## Next Phase Readiness

- Ready for **12-02** (wire `check_capability_map.main()` into `check_release.py` + HYG-01..04). Map gate is GREEN standalone.
- Do not tick MAP-19 boxes here (verify does that).
- Do not bump 1.18.0 version surfaces (Phase 13).

## Self-Check: PASSED

- Key files exist (`docs/capability-pack-map.json`, `docs/capability-pack-map.md`, `docs/capability-map-CONTRACT.md`, `tooling/check_capability_map.py`, this SUMMARY).
- Task commits present: `53099e0`, `7134474`, `48a2a63`.
- `python tooling/check_capability_map.py` exit 0; chapter-set on_disk_only=0 / map_only=0.
- DA membership 5/4 matches the locked five-row set; MOVE not copy.
- Conjunct print all `floor_fail=False`; Integration 4/4.
- CONTRACT contains 628, 502, Cybersecurity, Digital Engineering, unbound.
- plugin 1.18.0; map_version 1.18.0; catalog dod-vva-rpg.chapters == 10; SOURCE-VETTING http == 0.
- No generator; no 12-CONTEXT.md; ## Deviations ledger present; MJ-01 resolved.

---
*Phase: 12-map-regen-hygiene-gate-wiring*
*Completed: 2026-08-17*

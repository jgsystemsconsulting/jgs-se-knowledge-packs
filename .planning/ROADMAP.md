# Roadmap: JG Systems SE Knowledge Packs

## Overview

v1.17.0, v1.18.0, and v1.19.0 shipped: library is 63 catalog packs / 65 dirs (+2 signposts), capability map schema 2 / map_version 1.19.1 / 644 entries / 32 clusters, dual-gate wired. v1.19.1 is cleanup + the full carried backlog — ledger truth, source retries (build only if cleared), IN-02 + FUT-05 tooling, then a coherent v1.19.1 release surface. Licence vetting remains a hard stop; no invented packs.

## Shipped Milestones

- [x] **v1.17.0 — Source Expansion** (phases 1–5) — [archive](milestones/v1.17.0-ROADMAP.md)
- [x] **v1.18.0 — Gap-Driven Expansion + Agent Enablement** (phases 6–9) — [archive](milestones/v1.18.0-ROADMAP.md)
- [x] **v1.19.0 — Agent IO Depth** (phases 10–13) — [archive](milestones/v1.19.0-ROADMAP.md)

## Next

v1.19.1 — Cleanup + Carried Backlog. Phases 14–18 below.

---

# v1.19.1 — Cleanup + Carried Backlog

Goal: planning/ledger truth matches shipped v1.19.0 reality, then clear the carried backlog (FUT-04 / AAF retries, IN-02, FUT-05) and ship a coherent v1.19.1 surface. Deferred-with-evidence is a valid done state for uncleared sources.

## Phases

- [x] **Phase 14: Ledger + planning hygiene** — Verify milestone phase archives + finish residual ticks (MAP-19, VET annotations, live surfaces) (completed 2026-08-20)
- [x] **Phase 15: Source retries** — Docs-only FUT-04 / AAF / optional ROSAP vetting; no pack build (completed 2026-08-20)
- [x] **Phase 16: Conditional packs** — Build Army CBA / AAF Integration / AAF Logistics only if Phase 15 cleared the source (completed 2026-08-20)
- [x] **Phase 17: Tooling (IN-02 + FUT-05)** — Overlap checker wired into release + deterministic map generator or honest partial (completed 2026-08-20)
- [x] **Phase 18: Map + release surface v1.19.1** — Gates PASS; tag + GitHub Release; CHANGELOG honest about deferrals (completed 2026-08-20)

## Phase Details

### Phase 14: Ledger + planning hygiene

**Goal**: Planning and ledger surfaces tell the truth about shipped v1.19.0 and active v1.19.1 — no leftover "open Phase 13" claims
**Depends on**: v1.19.0 (shipped; last completed phase 13)
**Requirements**: HYG-20-01, HYG-20-02, HYG-20-03, HYG-20-04, HYG-20-05, HYG-20-06
**Success Criteria** (what must be TRUE):

  1. Phase directories for shipped work live under the correct milestone archives (`v1.17.0-phases`, `v1.18.0-phases`, `v1.19.0-phases`); v1.19.0 ROADMAP + REQUIREMENTS snapshots exist — already moved at milestone start; this phase verifies, does not re-do the moves
  2. `master-flow.status --all` shows no false open/blocked phases from shipped work (Phase 3 ghost already repaired); any remaining `master_flow_state.json` / edge-coverage that belongs with the archive is committed
  3. Archived v1.19.0 requirements tick MAP-19-01..05 complete (evidence: Phase 12 summaries — map 644, DA remap, floors, dual-gate, CONTRACT) and annotate VET-19-01..04 honestly (retry/deferral outcomes; not marked as built)
  4. Live PROJECT / STATE / ROADMAP / MILESTONES present v1.19.0 as shipped and v1.19.1 as active (pack counts, gates, backlog); they no longer claim an open Phase 13

**Plans:** 1/1 plans complete

Plans:

- [x] 14-01-PLAN.md — Verify archives + master-flow; tick MAP-19 / annotate VET-19 in v1.19.0 archive; residual live-surface honesty

### Phase 15: Source retries

**Goal**: Every carried source has dated evidence; AAF and Army CBA stay unused unless an in-source redistribution grant is quoted
**Depends on**: Phase 14
**Requirements**: VET-20-01, VET-20-02, VET-20-03
**Success Criteria** (what must be TRUE):

  1. Army CBA Guide (ASAFM PDF) has a dated retry record: in-source redistribution grant quoted, or FUT-04 remains deferred with fresh evidence (not a silent tick)
  2. AAF Product Support Manager Guidebook and AAF Software pathway guidebooks are either quoted with an in-source grant or remain Excluded-pending / "NOT yet vetted — do not use"
  3. Optional ROSAP Rev E reachability vs current `faa-std-025` Rev F mirror is documented only — no forced rebuild
  4. No pack is built in this phase

**Plans:** 1/1 plans complete

Plans:

- [x] 15-01-PLAN.md — Dated FUT-04 / AAF / ROSAP retries into SOURCE-VETTING + planning annotations; no packs

### Phase 16: Conditional packs

**Goal**: Packs exist only for sources Phase 15 cleared; uncleared paths are deferred on the record with no invented packs
**Depends on**: Phase 15
**Requirements**: PACK-20-01, PACK-20-02, PACK-20-03
**Success Criteria** (what must be TRUE):

  1. If VET-20-01 cleared → Army CBA / Decision Analysis pack exists, conforms to PACK-SPEC, and passes validate + scan + When-to-use; else FUT-04 stays deferred with evidence (no invented pack)
  2. If VET-20-02 cleared Software pathway → Integration-oriented pack exists on the IO-05 path and passes the same pack gates; else IO-05 stays deferred
  3. If VET-20-02 cleared Product Support → Logistics-oriented pack exists on the IO-06 path and passes the same pack gates; else IO-06 stays deferred

**Plans:** 1/1 plans complete

Plans:

- [x] 16-01-PLAN.md — Record PACK-20-01..03 deferred-with-evidence (Phase 15 handoff NO-GO); zero packs

### Phase 17: Tooling (IN-02 + FUT-05)

**Goal**: Release tooling catches multi-pack collisions and can regenerate mechanical map fields without agent judgment (or documents the residual honestly)
**Depends on**: Phase 16
**Requirements**: TOOL-20-01, TOOL-20-02, TOOL-20-03
**Success Criteria** (what must be TRUE):

  1. A minimal overlap checker lives under `tooling/` (stdlib Python preferred) and detects multi-pack chapter/topic collisions that matter for release
  2. The checker is on the release path (`check_release.py` call or documented mandatory step) and fails the gate on violations; thresholds are documented; intentional shared support files do not false-fail if excluded by design
  3. A deterministic capability-map generator/exporter under `tooling/` regenerates `docs/capability-pack-map.json` (+ md sync if required) from committed inputs for mechanical fields — or the largest deterministic slice ships with residual agent procedure documented in CONTRACT; full FUT-05 is not claimed closed unless byte-stable regen is proven

**Plans:** 1/1 plans complete

Plans:

- [x] 17-01-PLAN.md — Overlap checker on release path + FUT-05 honest residual in CONTRACT

### Phase 18: Map + release surface v1.19.1

**Goal**: Catalog, map, and release surfaces are coherent at v1.19.1; deferrals are visible, not papered over
**Depends on**: Phase 17
**Requirements**: MAP-20-01, REL-20-01, REL-20-02
**Success Criteria** (what must be TRUE):

  1. After any new packs or generator change, capability map validates (`check_capability_map.py` PASS) and `map_version` reflects v1.19.1
  2. Any new packs are fully registered; both gates PASS at the updated catalog/directory basis
  3. `v1.19.1` is tagged + published as a GitHub Release; CHANGELOG records cleanup + any packs/tooling honestly, including items still deferred

**Plans:** 2/2 plans executed

Plans:

- [x] 18-01-PLAN.md — Bump 11 surfaces + map_version 1.19.1 + honest CHANGELOG; both gates PASS at 63/65 (no tag)
- [x] 18-02-PLAN.md — Release commit + annotated tag v1.19.1 + push + GitHub Release + planning records

## Progress

**Execution Order:**
Phases execute in numeric order: 14 → 15 → 16 → 17 → 18

| Phase | Plans Complete | Status | Completed |
|-------|----------------|--------|-----------|
| 14. Ledger + planning hygiene | 1/1 | Complete    | 2026-08-20 |
| 15. Source retries | 1/1 | Complete    | 2026-08-20 |
| 16. Conditional packs | 1/1 | Complete    | 2026-08-20 |
| 17. Tooling (IN-02 + FUT-05) | 1/1 | Complete    | 2026-08-20 |
| 18. Map + release surface v1.19.1 | 2/2 | Complete    | 2026-08-20 |

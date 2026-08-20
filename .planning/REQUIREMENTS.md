# Requirements: JG Systems SE Knowledge Packs

**Defined:** 2026-08-19
**Core Value:** Licence-clean, validated, single-source reference packs an agent can load without filling its context window.
**Milestone:** v1.19.1 — Cleanup + Carried Backlog

## v1.19.1 Requirements

Sourced from STATE.md remaining backlog after v1.19.0 ship, stale GSD ledger (Phase 3 ghost, unarchived phases, uncommitted master_flow, unticked MAP-19), and deferred VET/AAF/FUT items. Full carried backlog in scope.

### Ledger + Planning Hygiene

- [x] **HYG-20-01**: Archive leftover phase directories under the correct milestone (`v1.17.0-phases`, `v1.18.0-phases`, `v1.19.0-phases`); archive v1.19.0 ROADMAP + REQUIREMENTS snapshots
- [x] **HYG-20-02**: Clear stale master-flow ledger (Phase 3 ghost block, pointer "Next: 3"); `master-flow.status --all` shows no false open/blocked phases from shipped work
- [x] **HYG-20-03**: Commit any remaining planning state (phase `master_flow_state.json`, edge-coverage) that belongs with the archive
- [x] **HYG-20-04**: Tick MAP-19-01..05 complete in archived v1.19.0 requirements (evidence: Phase 12 summaries — map 644, DA remap, floors, dual-gate, CONTRACT)
- [x] **HYG-20-05**: Annotate VET-19-01..04 honestly in archived v1.19.0 requirements (retry/deferral outcomes; do not mark as built)
- [x] **HYG-20-06**: Refresh live PROJECT.md / STATE.md / ROADMAP.md / MILESTONES.md so current state is v1.19.0 shipped and v1.19.1 active (pack counts, gates, backlog no longer claim "open phase 13")

### Source Retries (build only if cleared)

- [x] **VET-20-01**: Retry FUT-04 Army CBA Guide (ASAFM PDF). Record dated evidence. Build pack only with in-source redistribution grant; otherwise keep FUT-04 deferred with fresh evidence (not a silent tick) — *retry 2026-08-20; ASAFM PDF 403; no in-source grant; FUT-04 remains deferred; not a build-clear*
- [x] **VET-20-02**: Licence spot-check AAF Product Support Manager Guidebook + AAF Software pathway guidebooks before any use. Quote in-source grant or keep Excluded-pending / "NOT yet vetted — do not use" — *retry 2026-08-20; still NOT yet vetted — do not use; Excluded-pending; no guidebook PDF opened*
- [x] **VET-20-03**: Optional ROSAP Rev E reachability check vs current `faa-std-025` Rev F mirror — document only; no forced rebuild — *optional check 2026-08-20; ROSAP Rev E 403; guessed FAA Rev F path 404; document only; no forced rebuild*
- [ ] **PACK-20-01**: If VET-20-01 clears → build Army CBA / Decision Analysis pack per PACK-SPEC + validate + scan + When-to-use; else record deferred (no invented pack)
- [ ] **PACK-20-02**: If VET-20-02 clears Software pathway → build Integration-oriented pack (IO-05 path); else keep deferred
- [ ] **PACK-20-03**: If VET-20-02 clears Product Support → build Logistics-oriented pack (IO-06 path); else keep deferred

### Tooling

- [ ] **TOOL-20-01 (IN-02)**: Minimal committed overlap checker under `tooling/` (stdlib Python preferred). Detects multi-pack chapter/topic collisions that matter for release; runnable in CI or via `check_release.py`
- [ ] **TOOL-20-02**: Wire TOOL-20-01 into release path (direct call from `check_release.py` or documented mandatory step with gate failure on violations). Thresholds documented; no false-fail on intentional shared support files if excluded by design
- [ ] **TOOL-20-03 (FUT-05)**: Deterministic capability-map generator (or exporter) under `tooling/` that regenerates `docs/capability-pack-map.json` (+ md sync if required) from committed inputs without agent judgment for mechanical fields. If full cluster classification cannot be mechanical, deliver the largest deterministic slice + residual agent procedure documented in CONTRACT; do not claim full FUT-05 closed unless byte-stable regen is proven

### Map + Release

- [ ] **MAP-20-01**: After any new packs or generator change, regenerate/validate capability map; `check_capability_map.py` PASS; map_version reflects v1.19.1
- [ ] **REL-20-01**: Full registration of any new packs; both gates PASS at updated catalog/directory basis
- [ ] **REL-20-02**: v1.19.1 tagged + GitHub Release; CHANGELOG records cleanup + any packs/tooling honestly (including "still deferred" items)

## Future Requirements (not this milestone)

- **FUT-se-agents**: Consumer refresh (502 docs residue, thin:3, Cyber/DE bindings, 20-ref cap) — sibling repo `jgs-se-agents`
- **FUT-NASA-wiki**: NASA-HDBK-2203 / NPR 7150.2 if a licence-clean PDF edition appears
- **FUT-DoDM-5000-102**: Retry if a public PDF becomes available (still UNVERIFIED as of v1.19.0)

## Out of Scope (v1.19.1)

| Feature | Reason |
|---------|--------|
| Per-role knowledge packs | Role lens belongs to se-agents skills layer |
| se-agents consumer refresh | Lives in jgs-se-agents |
| Invented packs when sources stay uncleared | Licence-clean core value; record deferral only |
| Branch-protection enforcement | User opted to keep admin bypass |
| Major pack wave unrelated to carried backlog | This is cleanup + deferred items only |
| Full se-agents Cyber/DE cluster binding | Consumer-side |

## Traceability

| Requirement | Phase | Status |
|-------------|-------|--------|
| HYG-20-01 | Phase 14 | Complete |
| HYG-20-02 | Phase 14 | Complete |
| HYG-20-03 | Phase 14 | Complete |
| HYG-20-04 | Phase 14 | Complete |
| HYG-20-05 | Phase 14 | Complete |
| HYG-20-06 | Phase 14 | Complete |
| VET-20-01 | Phase 15 | Complete |
| VET-20-02 | Phase 15 | Complete |
| VET-20-03 | Phase 15 | Complete |
| PACK-20-01 | Phase 16 | Pending |
| PACK-20-02 | Phase 16 | Pending |
| PACK-20-03 | Phase 16 | Pending |
| TOOL-20-01 | Phase 17 | Pending |
| TOOL-20-02 | Phase 17 | Pending |
| TOOL-20-03 | Phase 17 | Pending |
| MAP-20-01 | Phase 18 | Pending |
| REL-20-01 | Phase 18 | Pending |
| REL-20-02 | Phase 18 | Pending |

**Coverage:**

- v1.19.1 requirements: 18 total
- Mapped to phases: 18/18
- Unmapped: 0

---
*Requirements defined: 2026-08-19*
*Last updated: 2026-08-19 after roadmap (phases 14–18)*

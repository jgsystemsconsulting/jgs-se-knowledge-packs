---
gsd_state_version: 1.0
milestone: v1.19.0
milestone_name: "**Goal**: Catalog/docs/manifests synchronized; v1.19.0 tagged and released"
current_phase: 12
current_phase_name: Map regen + hygiene + gate wiring
status: planning
last_updated: "2026-08-17T19:33:37.522Z"
last_activity: 2026-08-17
last_activity_desc: v1.19.0 scoped from SEED-001 + v1.18 audit backlog
progress:
  total_phases: 4
  completed_phases: 2
  total_plans: 4
  completed_plans: 4
  percent: 50
stopped_at: v1.19.0 milestone scoped — ready to plan Phase 10
---

# Project State

## Project Reference

See: .planning/PROJECT.md (updated 2026-08-17)

**Core value:** Licence-clean, validated, single-source reference packs an agent can load without context bloat.
**Current focus:** v1.19.0 — Agent IO Depth (Phase 10: Source vetting)

## Current Position

Phase: 12 of 13 (Map regen + hygiene + gate wiring)
Plan: Not started
Status: Ready to plan
Last activity: 2026-08-17 — Phase 11 complete, transitioned to Phase 12

Progress: [███████░░░] 69%

## Performance Metrics

- Phases completed: 9/13 (v1.17 + v1.18 shipped)
- Packs shipped: 63 (61 catalog + 2 signposts)

## Selected seed

SEED-001 — pack depth for se-agents IOs (17 thin-primary competencies). Consumer-side work (502 docs, thin:3, Cyber/DE bindings, 20-ref cap) stays in jgs-se-agents.

## Still-open from v1.18 (not all in v1.19 scope)

In this milestone: FUT-04, thin clusters 3/5/15 via IO-unlocks, map-gate wiring, CHANGELOG BOM/.gitattributes, topic-index polish, AAF vet-before-use, vet_source EXCLUDED sync, federal-bca "(c)" polish.

Deferred again: FUT-05 deterministic generator; committed overlap checker (7-CODE-REVIEW IN-02); 881F/VV&A DIST-A in-PDF revisit (7-GAP R4).

## Deviations / Notes

- Branch protection left at admin-bypass (2026-08-16)
- Per-role packs remain rejected
- IO-05/IO-06 are conditional on AAF clearing VET-19-03 — expect honest deferral
- IO-07 will not produce a pack
- Phase 10 (2026-08-17): SOURCE-VETTING v1.19 recorded. GO: NASA-STD-8719.14C, IS-GPS-200N, SP-7084 optional. NO-GO: FUT-04 Army CBA (403/503 deferred), DoDM 5000.102 (UNVERIFIED), AAF (NOT yet vetted — do not use). Verdicts + URLs in 10-RESEARCH.md. Phase 11 builds only GO names.
- Phase 11 (2026-08-17): built nasa-std-8719-14 + is-gps-200n; extended dod-vva-rpg; IO-01 remap table specified (no map JSON); IO-05/06 deferred; IO-07 accept; SP-7084 skipped.

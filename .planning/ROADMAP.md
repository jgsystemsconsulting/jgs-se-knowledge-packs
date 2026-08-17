# Roadmap: JG Systems SE Knowledge Packs

## Overview

v1.17.0 and v1.18.0 shipped: library grew 48 → 63 packs (61 catalog + 2 signposts), licence-vetting register matured, and the capability map became a versioned, gate-checked consumable (schema 2, 628 entries) for the se-agents generator. No active phases — next milestone is v1.19 (backlog in STATE.md; seed from .planning/research/capability-gap-report.md + milestone audits).

## Shipped Milestones

- [x] **v1.17.0 — Source Expansion** (phases 1–5) — [archive](milestones/v1.17.0-ROADMAP.md)
- [x] **v1.18.0 — Gap-Driven Expansion + Agent Enablement** (phases 6–9) — [archive](milestones/v1.18.0-ROADMAP.md)

## Next

v1.19.0 — Agent IO Depth (SEED-001). Phases 10–13 below.

---

# v1.19.0 — Agent IO Depth

Seed: SEED-001. Goal: fatten competency *primaries* so se-agents can execute IOs (trade studies, V&V, transition, interfaces), not just lecture from fat secondaries.

## v1.19 Phases

- [ ] **Phase 10: Source vetting** — FUT-04 retry + DoDM 5000.102 / NASA-STD-8719.14 / GPS ICD / SP-7084 / AAF-before-use (VET-19-01..04)
- [ ] **Phase 11: IO-unlocking packs + Decision Analysis remap** — IO-01..07 (build what vetting clears; record deferrals honestly)
- [ ] **Phase 12: Map regen + hygiene + gate wiring** — MAP-19-01..05, HYG-01..04
- [ ] **Phase 13: Release surface + v1.19.0** — REL-19-01/02

## v1.19 Phase Details

### Phase 10: Source vetting
**Goal**: Every v1.19 candidate has a definitive tier decision; AAF stays unused until cleared
**Depends on**: v1.18.0 (shipped)
**Requirements**: [VET-19-01, VET-19-02, VET-19-03, VET-19-04]
**Success Criteria** (what must be TRUE):
  1. Army CBA Guide resolved (reachable + in-source licence, or FUT-04 remains deferred with fresh evidence)
  2. DoDM 5000.102, NASA-STD-8719.14, GPS ICD select, NASA SP-7084 each Tier 1/2/Excluded with dated rationale
  3. AAF Product Support + Software pathway either vetted Tier 1 or still "NOT yet vetted — do not use"
  4. New exclusions in docs/SOURCE-VETTING.md; no source URLs in that doc
**Plans**: TBD

### Phase 11: IO-unlocking packs + Decision Analysis remap
**Goal**: Poorest competency primaries move; no silent ticks
**Depends on**: Phase 10
**Requirements**: [IO-01, IO-02, IO-03, IO-04, IO-05, IO-06, IO-07]
**Success Criteria** (what must be TRUE):
  1. Decision Analysis cluster count leaves 2 (new pack and/or MAP-19-03 remap of A-94 / VV&A decision chapters)
  2. Validation, Ops/Maint/Disposal, Interface Management each gained at least one new pack *or* documented deferral
  3. Integration + Logistics built only if AAF cleared; otherwise deferred-recorded
  4. Stakeholder Engagement outcome recorded (SEBoK expansion or accept) — no invented pack
  5. Each built pack: PACK-SPEC + validate_pack + scan + overlap + When-to-use/Prerequisites
**Plans**: TBD

### Phase 12: Map regen + hygiene + gate wiring
**Goal**: Map reflects new packs; competency-primary floor asserted; hygiene + consumer-contract note
**Depends on**: Phase 11
**Requirements**: [MAP-19-01, MAP-19-02, MAP-19-03, MAP-19-04, MAP-19-05, HYG-01, HYG-02, HYG-03, HYG-04]
**Success Criteria** (what must be TRUE):
  1. check_capability_map.py PASS; MAP-19-02 floor held (no listed primary still at <4 entries AND 1 pack)
  2. check_release.py invokes the map gate
  3. CONTRACT.md notes live snapshot (not 502) and unbound Cyber/DE clusters
  4. CHANGELOG BOM gone; .gitattributes pin present; topic-index nits fixed; vet_source EXCLUDED sync done or recorded as external-repo PR
**Plans**: TBD

### Phase 13: Release surface + v1.19.0
**Goal**: Catalog/docs/manifests synchronized; v1.19.0 tagged and released
**Depends on**: Phase 12
**Requirements**: [REL-19-01, REL-19-02]
**Success Criteria** (what must be TRUE):
  1. Both gates PASS at the updated catalog/directory basis
  2. v1.19.0 tagged + GitHub Release; CHANGELOG lists IO-unlocks by competency, not just pack slugs
**Plans**: TBD

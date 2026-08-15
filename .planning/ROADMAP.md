# Roadmap: JG Systems SE Knowledge Packs

## Overview

Baseline established retroactively (48 packs shipped through v1.16.3, pipeline + install surface validated), then v1.17.0 expands the library with 11 researched candidates (8 Tier-1 builds + 3 vetted-out: T2-01/T2-02 Excluded, T2-03 deferred-excluded), formal ruled-out tracking, and a synchronized release surface.

## Phases

- [x] **Phase 1: Baseline (retroactive)** - Existing 48-pack library, toolchain, installers, CI gate
- [x] **Phase 2: Source vetting + ruled-out register** - Vet all 11 candidates; record Excluded entries
- [x] **Phase 3: Tier 1 packs (public domain)** - Build the 8 Tier-1 packs via jgs-reference-skill pipeline
- [ ] **Phase 4: Tier 2 packs — closed by vetting: 0 packs (T2-01/T2-02 Excluded, T2-03 deferred; see docs/SOURCE-VETTING.md)**
- [ ] **Phase 5: Release surface + v1.17.0** - Catalog/docs/NOTICE sync, full validation, tag release

## Phase Details

### Phase 1: Baseline (retroactive)
**Goal**: Record the shipped state as validated foundation
**Depends on**: Nothing
**Requirements**: [PACK-01, PACK-02, PACK-03, TOOL-01, TOOL-02, TOOL-03]
**Success Criteria** (what must be TRUE):
  1. 48 packs pass validate_pack.py locally and in CI
  2. Installers and catalog.json consistent with pack directories
**Plans**: 0 (retroactive; no execution required)

### Phase 2: Source vetting + ruled-out register
**Goal**: Every candidate source has a definitive tier decision with evidence; rejected sources permanently recorded
**Depends on**: Phase 1
**Requirements**: [RO-01, T2-03 (vetting half)]
**Success Criteria** (what must be TRUE):
  1. docs/SOURCE-VETTING.md Excluded table contains INCOSE Handbook, INCOSE Guide to Writing Requirements, ISO/IEC/IEEE 15288/29148/21839, DAU/WARU 2022 duplicate — each with rationale and date
  2. Each of the 11 candidates has a recorded tier decision with source URL and licence evidence
  3. Def Stan 00-051 redistribution terms: recorded outcome is deferred-excluded pending registered DSTAN in-document licence check (decision recorded, build deferred — not an unblock)
**Plans**: 1 plan (complete)

### Phase 3: Tier 1 packs (public domain)
**Goal**: 8 public-domain packs built and validated
**Depends on**: Phase 2
**Requirements**: [T1-01, T1-02, T1-03, T1-04, T1-05, T1-06, T1-07, T1-08]
**Success Criteria** (what must be TRUE):
  1. Each pack conforms to docs/PACK-SPEC.md and passes validate_pack.py
  2. Each pack passes scan_generated_skill.py (advisory findings reviewed)
  3. PACK.yaml provenance complete (tier, licence, pages, chapters, built_on)
**Plans**: 3 plans
Plans:
- [x] 3-01-PLAN.md — Batch A: 4 born-digital packs (nist-800-171, nist-800-61, cisa-cpg, doe-sem); P3-PRE-1/P3-PRE-2 handling
- [x] 3-02-PLAN.md — Batch B: DoD handbooks (mil-hdbk-338 with chapter selection, mil-hdbk-516) + mirror/OCR contingencies
- [x] 3-03-PLAN.md — Batch C: multi-doc packs (nasa-ms-7009, doe-413-3b) + consolidated registration sweep (catalog/SKILLS.md/packs.html/NOTICE/check_release)

### Phase 4: Tier 2 packs (conditional licences)
**Goal**: closed by vetting: 0 Tier-2 packs
**Depends on**: Phase 3
**Requirements**: closed by docs/SOURCE-VETTING.md outcome (T2-01/T2-02 Excluded, T2-03 deferred-excluded; see REQUIREMENTS.md)
**Success Criteria** (what must be TRUE):
  1. no execution; outcome recorded in docs/SOURCE-VETTING.md
**Plans**: none (slot retained; no renumbering)

### Phase 5: Release surface + v1.17.0
**Goal**: Catalog, docs, installers, and release artifacts include the new packs
**Depends on**: Phase 4
**Requirements**: [REL-01, REL-02]
**Success Criteria** (what must be TRUE):
  1. check_release.py exits 0; validate gate catalog basis = 54 packs (48 dirs + 8 new, minus 2 signpost packs) / 56 directory basis
  2. v1.17.0 tagged and released
**Plans**: 1

Plans:
- [ ] 5-01-PLAN.md — Release surface sync (11 version surfaces, CHANGELOG, PACK-SPEC, README framing), gate PASS at 54/56, tag + GitHub Release v1.17.0, post-release records

# Requirements: JG Systems SE Knowledge Packs

**Defined:** 2026-08-17
**Core Value:** Licence-clean, validated, single-source reference packs an agent can load without filling its context window.
**Milestone:** v1.19.0 — Agent IO Depth (SEED-001)
**Selected seed:** SEED-001 (pack depth for se-agents IOs — 17 thin-primary competencies)

## v1.19.0 Requirements

Sourced from SEED-001, STATE.md v1.19 backlog (consolidated per v1.18.0-MILESTONE-AUDIT), and .planning/research/capability-gap-report.md. Maps to phases 10–13.

### Source Vetting

- [ ] **VET-19-01**: Vet FUT-04 Army CBA Guide (ASAFM PDF retry) — build-or-exclude with in-source licence evidence
- [ ] **VET-19-02**: Vet DoDM 5000.102, NASA-STD-8719.14, GPS ICD-IS-200/300 (select), NASA SP-7084 — Tier 1/2/Excluded with dated rationale
- [ ] **VET-19-03**: AAF Product Support + Software pathway guidebooks — licence spot-check BEFORE any use (Phase 6 deferral still in force); record Tier or keep Excluded-pending
- [ ] **VET-19-04**: Add any newly ruled-out sources to docs/SOURCE-VETTING.md Excluded table

### Gap-Driven Packs (unlock poorest competency primaries)

- [ ] **IO-01**: Decision Analysis primary (SECF-CORE-05 / MANA-03) — FUT-04 Army CBA pack **or** remap existing A-94 / VV&A decision chapters into cluster 16; primary count must leave 2
- [ ] **IO-02**: Validation primary (SECF-TECH-07) — `dodm-5000-102` (or additional VV&A RPG chapters in existing `dod-vva-rpg`)
- [ ] **IO-03**: Ops/Maintenance/Disposal primary (SECF-TECH-08 / 09 / 10) — `nasa-std-8719-14`
- [ ] **IO-04**: Interface Management primary (SECF-TECH-05) — GPS ICD exemplar pack (select IS-200/300) **or** additional FAA-STD-025 depth
- [ ] **IO-05**: Integration primary (SECF-TECH-04) — only if VET-19-03 clears AAF Software pathway; otherwise record deferred
- [ ] **IO-06**: Logistics diversity (SECF-INTE-03) — only if VET-19-03 clears AAF Product Support; otherwise record deferred
- [ ] **IO-07**: Stakeholder Engagement (SECF-PROF-01/04/06) — no clean Tier-1/2 candidate; **do not invent a pack**; document SEBoK-expansion-or-accept as the recorded outcome

### Map + Consumer Contract (pack-side only)

- [ ] **MAP-19-01**: Regenerate capability-pack-map.json (agent pass + `check_capability_map.py`) including all v1.19 packs
- [ ] **MAP-19-02**: Extra assert vs SEED-001: no *competency primary* cluster remains at count < 4 AND 1 pack (tighter than v1.18 SC-2). Decision Analysis, Validation, Integration, Interfaces, Ops/Maint must each move
- [ ] **MAP-19-03**: Remap existing `federal-bca` / selected `dod-vva-rpg` decision chapters into Decision Analysis (cluster 16) if they currently sit only in Opportunity/Benefit — cheaper than a new pack
- [ ] **MAP-19-04**: Wire `check_capability_map.py` into `check_release.py` (v1.18 Phase 8 deferred)
- [ ] **MAP-19-05**: Document for se-agents (one paragraph in capability-map-CONTRACT.md): snapshot is live 628+; 502 figure is residue; Cybersecurity + Digital Engineering clusters remain unbound (their mapping work is se-agents-side, not this milestone)

### Hygiene (from v1.18 audit backlog)

- [ ] **HYG-01**: CHANGELOG strip UTF-8 BOM + normalize; add `.gitattributes` (`*.md text eol=lf`)
- [ ] **HYG-02**: Topic-index polish (881F alpha order, 40051 circular routing, federal-bca label) — 7-GAP R6
- [ ] **HYG-03**: External sync — add afotec/dod-dag/cmu-sei to jgs-reference-skill `vet_source.py` EXCLUDED signals (6-GAP Thread 3)
- [ ] **HYG-04**: federal-bca "(c)" wording polish (cosmetic)

### Release Surface

- [ ] **REL-19-01**: Full registration of any new packs; both gates PASS
- [ ] **REL-19-02**: v1.19.0 tagged + GitHub Release

## Out of Scope (v1.19)

| Feature | Reason |
|---------|--------|
| Per-role knowledge packs | Role lens belongs to se-agents skills layer (2026-08-16) |
| se-agents consumer refresh (502 docs, thin:3 align, 20-ref cap, Cyber/DE bindings) | Lives in jgs-se-agents — MAP-19-05 only documents the contract |
| FUT-05 deterministic map generator | Still agent-judgment; keep FUT-05 |
| Committed overlap checker (7-CODE-REVIEW IN-02) | Separate tooling milestone |
| NASA-HDBK-2203 / NPR 7150.2 (Quality + Data Mgmt) | GP-08 already descoped (wiki-only); revisit if a PDF edition appears |
| Branch-protection enforcement | User opted to keep admin bypass |

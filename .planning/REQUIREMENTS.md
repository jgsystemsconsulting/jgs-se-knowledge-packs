# Requirements: JG Systems SE Knowledge Packs

**Defined:** 2026-08-14
**Core Value:** Every pack must be a licence-clean, validated, single-source reference that an engineer can trust and an agent can load without filling its context window.

## Baseline Requirements (v1.0.0 → v1.16.3, retroactively validated)

Existing shipped behaviour. Mapped to the retroactive baseline phase.

### Pack Library

- [x] **PACK-01**: Each pack conforms to docs/PACK-SPEC.md (SKILL.md + chapters/ + glossary/patterns/cheatsheet + PACK.yaml + LICENSE)
- [x] **PACK-02**: Each pack's licence tier is vetted and recorded; Excluded-tier sources never ship
- [x] **PACK-03**: Packs are plain Markdown with progressive disclosure; no runtime dependencies

### Toolchain

- [x] **TOOL-01**: Licence vetting, overlap checking, and pack validation run deterministically (stdlib-only Python)
- [x] **TOOL-02**: CI validate gate blocks non-conforming releases
- [x] **TOOL-03**: Multi-host installers (claude/openclaw/copilot) and catalog.json registry stay in sync

## v1.17.0 Requirements — Source Expansion

New milestone: researched candidate packs + ruled-out tracking. Maps to phases 2+.

### Tier 1 Packs (public domain / free redistribution)

- [x] **T1-01**: Build `nist-800-171` pack from NIST SP 800-171 Rev.3 (Protecting CUI, 2024)
- [x] **T1-02**: Build `nist-800-61` pack from NIST SP 800-61 Rev.3 (Incident Response, 2025)
- [x] **T1-03**: Build `mil-hdbk-338` pack from MIL-HDBK-338B (Electronic Reliability Design Handbook, 1998)
- [x] **T1-04**: Build `mil-hdbk-516` pack from MIL-HDBK-516C (Airworthiness Certification Criteria, 2014)
- [x] **T1-05**: Build `nasa-ms-7009` pack from NASA-STD-7009B + NASA-HDBK-7009 (Models & Simulations, 2024)
- [x] **T1-06**: Build `doe-413-3b` pack from DOE O 413.3B (Capital Asset Acquisition, Chg 7 2023)
- [x] **T1-07**: Build `cisa-cpg` pack from CISA CPG 2.0 (Cross-Sector Cybersecurity Performance Goals, 2025)
- [x] **T1-08**: Build `doe-sem` pack from DOE Systems Engineering Methodology (SEM3)

### Tier 2 Packs (free with licence conditions — attribution/redistribution terms)

- ~~**T2-01**: Build `ieee-15288-2` pack from IEEE 15288.2-2014 (Technical Reviews and Audits), preserving IEEE copyright attribution~~ — **excluded-by-vetting**. Excluded 2026-08-14 — purchase-only, not in IEEE GET program, IEEE sole copyright, no redistribution/derivative grant (see docs/SOURCE-VETTING.md).
- ~~**T2-02**: Build `ecss-e-st-10` pack from ECSS-E-ST-10C Rev.1 (Space Engineering General Requirements), preserving ESA/ECSS copyright attribution~~ — **excluded-by-vetting**. Excluded 2026-08-14 — © ESA; ECSS-P-00C §5.8 forbids reproduction without explicit ESA consent; a pack is reproduction + derivative (see docs/SOURCE-VETTING.md).
- [ ] **T2-03**: Vet UK Def Stan 00-051 redistribution terms; build `defstan-00-051` pack only if terms permit, else record as Excluded with rationale — **deferred-excluded pending registered DSTAN in-document licence check**. In-document terms UNVERIFIED; no DSTAN retrieval performed this milestone. Subject correction: 00-051 is *Environmental Management Requirements for Defence Systems*; system safety is Def Stan 00-056 — any future revival must re-point the requirement and re-read the licence. 0 Tier-2 packs in v1.17.0.

### Ruled-Out Tracking

- [x] **RO-01**: Add researched-and-rejected sources to docs/SOURCE-VETTING.md Excluded table with per-source rationale (INCOSE SE Handbook, INCOSE Guide to Writing Requirements, ISO/IEC/IEEE 15288/29148/21839 full texts, DAU/WARU 2022 guidebook duplicate)

### Release Surface

- [x] **REL-01**: catalog.json, SKILLS.md, docs/packs.html, and NOTICE include all new packs; no drift (gate passes). v1.17.0 milestone expectation: **56 (48 baseline + 8 Tier-1)** packs (T2-01/T2-02 excluded-by-vetting; T2-03 deferred-excluded → 0 Tier-2 packs).
- [x] **REL-02**: Release v1.17.0 tagged at **56 (48 baseline + 8 Tier-1)** packs; all packs pass validate_pack.py and scan_generated_skill.py

## v2 Requirements (Deferred)

### Future Candidates

- **FUT-01**: Additional international lineages (Australia/Canada/Japan defence SE standards) pending research
- **FUT-02**: INCOSE Guide to Writing Requirements full pack, if an open-licence edition is ever released
- **FUT-03 / T2-03**: UK Def Stan 00-051 — deferred-excluded pending registered DSTAN in-document licence check (2026-08-14). Environmental management (not safety; safety is 00-056). If OGL v3.0 confirmed inside the document → Tier 2 attribution pack; if bespoke MOD-consent terms → stays Excluded. Re-point requirement and re-read licence before any revival.

## Out of Scope

| Feature | Reason |
|---------|--------|
| Paywalled standards full texts | Not licence-redistributable; hard stop per SOURCE-VETTING. Includes IEEE 15288.2-2014 (excluded-by-vetting 2026-08-14; see docs/SOURCE-VETTING.md). |
| Free-download, no-redistribution-grant standards (ECSS/ESA) | Non-redistributable free downloads (see docs/SOURCE-VETTING.md). Includes ECSS-E-ST-10C Rev.1 (excluded-by-vetting 2026-08-14; ECSS-P-00C §5.8). |
| Runtime tooling (MCP/API dependencies) | Packs are plain Markdown by design |
| Non-SE domains | Outside library charter |

## v1.18.0 Requirements — Gap-Driven Expansion + Agent Enablement

Sourced from .planning/research/capability-gap-report.md (1 empty cluster, 15 thin) and the v1.17.0 carry-forward list. Maps to phases 6–9.

### Source Vetting

- [x] **VET-01**: Resolve the 5 UNVERIFIED items from the gap report (MIL-STD-40051 current-rev PDF, NASA SP-7084 NTRS availability, consolidated VV&A RPG PDF edition, MIL-STD-881F canonical DLA copy, AFOTEC Test Design Guide); record definitive tier decisions with evidence (4/5 resolved; AAF guidebooks check deferred — not blocking Phase 7)
- [x] **VET-02**: Add newly ruled-out sources to docs/SOURCE-VETTING.md Excluded table (DoD DAG — retired/dead; CMU SEI — permission-gated; any UNVERIFIED items that fail)

### Gap-Driven Packs (all Tier 1 pending vetting; targets in brackets)

- [ ] **GP-01**: `dod-vva-rpg` — DoD VV&A Recommended Practice Guide (+ DoDM 5000.102) [8 Validation, 7 Verification, 16 Decision Analysis, 9 T&E] (build model: VV&A RPG has NO consolidated PDF — chapter-wise build with per-chapter provenance in PACK.yaml; per 6-RESEARCH.md §1c)
- [x] **GP-02**: `faa-std-025` — FAA Interface Documentation IRD/ICD/IR [5 Interface Mgmt, 3 Requirements Traceability, 12 CM]
- [x] **GP-03**: `dote-te-guidebook` — DOT&E T&E Enterprise Guidebook [9 T&E single-source fix, 7, 8, 23 Logistics] (target the Aug 2022 edition 8.02 from dote.osd.mil; fall back to the afacpo fixed single-encoded mirror PDF if direct download unavailable; PACK.yaml records the edition actually built; the gap-report mirror URL was double-encoded and is fixed in 6-RESEARCH.md §2b)
- [ ] **GP-04**: `dafman-63-119` — DAF Mission-Oriented Test Readiness Certification manual (DAFMAN 63-119) [9, 6 Integration, 27 Supplier] (title correction: MOTRC compliance manual, 15 Apr 2021 — per 6-RESEARCH.md §2c)
- [ ] **GP-05**: `mil-std-881f` — Defense WBS standard [17 Technical Planning, 26 Measurement]
- [x] **GP-06**: `federal-bca` — OMB Circular A-94 + Army CBA Guide (dual-source) [15 Opportunity/Benefit — worst cluster, 16, 17]
- [ ] **GP-07**: `mil-std-40051` — Technical Data Packages [25 Training & Documentation — the EMPTY cluster, 24]
- [ ] ~~**GP-08** (stretch): `nasa-sw-handbook` — NASA-HDBK-2203 select chapters [13 Data Mgmt, 19 QA, 32 Specialty]~~ — DESCOPED 2026-08-14: NASA-HDBK-2203 has no consolidated PDF (standards-page PDF is a placeholder; content is swehb.nasa.gov wiki HTML); see 6-RESEARCH.md §4

### Agent-Enablement Surface

- [ ] **AE-01**: `capability-pack-map.json` becomes a versioned consumable: schema field + map version + generated-on metadata; a stdlib export/regenerate script under tooling/ (idempotent, gate-checked for staleness)
- [ ] **AE-02**: Regenerate the map to include all v1.18 packs; thin-cluster re-score shows cluster 25 non-empty and clusters 3/5/15 no longer critical
- [ ] **AE-03**: Document the map contract (schema + versioning + refresh path) for the se-agents generator repo per docs/ROLE-AGENTS-REQUIREMENTS-V2.md

### Release Surface

- [ ] **REL-1x-01**: Full registration of new packs (catalog, SKILLS.md, packs.html, NOTICE, README, cursor manifest); check_release PASS
- [ ] **REL-1x-02**: v1.18.0 tagged + GitHub Release; CHANGELOG entry includes the v1.17.0 wording fix (docs/index.html is a version surface, not a registered surface) and notes the doe-o-413-3 rename

## Out of Scope (v1.18)

| Feature | Reason |
|---------|--------|
| Per-role knowledge packs | Role lens belongs to the se-agents skills layer; packs stay source-organized (design decision 2026-08-16) |
| Cluster 28 Stakeholder pack | No Tier-1/2 candidate beyond existing gao-tra coverage; SEBoK expansion if ever needed |
| Branch-protection enforcement | User opted to keep admin bypass (2026-08-16) |
| nasa-sw-handbook (GP-08) | No consolidated PDF edition exists; per-SWE wiki-harvest build is out of v1.18 scope. Alternative: rescope to NPR 7150.2 + NASA-STD-8739.8 (both downloadable PDFs; 8739.8 cover states APPROVED FOR PUBLIC RELEASE – DISTRIBUTION IS UNLIMITED) as v1.19 candidates or a Phase 7 stretch decision. |

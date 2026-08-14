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

- [ ] **T1-01**: Build `nist-800-171` pack from NIST SP 800-171 Rev.3 (Protecting CUI, 2024)
- [ ] **T1-02**: Build `nist-800-61` pack from NIST SP 800-61 Rev.3 (Incident Response, 2025)
- [ ] **T1-03**: Build `mil-hdbk-338` pack from MIL-HDBK-338B (Electronic Reliability Design Handbook, 1998)
- [ ] **T1-04**: Build `mil-hdbk-516` pack from MIL-HDBK-516C (Airworthiness Certification Criteria, 2014)
- [ ] **T1-05**: Build `nasa-ms-7009` pack from NASA-STD-7009B + NASA-HDBK-7009 (Models & Simulations, 2024)
- [ ] **T1-06**: Build `doe-413-3b` pack from DOE O 413.3B (Capital Asset Acquisition, Chg 7 2023)
- [ ] **T1-07**: Build `cisa-cpg` pack from CISA CPG 2.0 (Cross-Sector Cybersecurity Performance Goals, 2025)
- [ ] **T1-08**: Build `doe-sem` pack from DOE Systems Engineering Methodology (SEM3)

### Tier 2 Packs (free with licence conditions — attribution/redistribution terms)

- ~~**T2-01**: Build `ieee-15288-2` pack from IEEE 15288.2-2014 (Technical Reviews and Audits), preserving IEEE copyright attribution~~ — **excluded-by-vetting**. Excluded 2026-08-14 — purchase-only, not in IEEE GET program, IEEE sole copyright, no redistribution/derivative grant (see docs/SOURCE-VETTING.md).
- ~~**T2-02**: Build `ecss-e-st-10` pack from ECSS-E-ST-10C Rev.1 (Space Engineering General Requirements), preserving ESA/ECSS copyright attribution~~ — **excluded-by-vetting**. Excluded 2026-08-14 — © ESA; ECSS-P-00C §5.8 forbids reproduction without explicit ESA consent; a pack is reproduction + derivative (see docs/SOURCE-VETTING.md).
- [x] **T2-03**: Vet UK Def Stan 00-051 redistribution terms; build `defstan-00-051` pack only if terms permit, else record as Excluded with rationale — **deferred-excluded pending registered DSTAN in-document licence check**. In-document terms UNVERIFIED; no DSTAN retrieval performed this milestone. Subject correction: 00-051 is *Environmental Management Requirements for Defence Systems*; system safety is Def Stan 00-056 — any future revival must re-point the requirement and re-read the licence. 0 Tier-2 packs in v1.17.0.

### Ruled-Out Tracking

- [x] **RO-01**: Add researched-and-rejected sources to docs/SOURCE-VETTING.md Excluded table with per-source rationale (INCOSE SE Handbook, INCOSE Guide to Writing Requirements, ISO/IEC/IEEE 15288/29148/21839 full texts, DAU/WARU 2022 guidebook duplicate)

### Release Surface

- [ ] **REL-01**: catalog.json, SKILLS.md, docs/packs.html, and NOTICE include all new packs; no drift (gate passes). v1.17.0 milestone expectation: **56 (48 baseline + 8 Tier-1)** packs (T2-01/T2-02 excluded-by-vetting; T2-03 deferred-excluded → 0 Tier-2 packs).
- [ ] **REL-02**: Release v1.17.0 tagged at **56 (48 baseline + 8 Tier-1)** packs; all packs pass validate_pack.py and scan_generated_skill.py

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

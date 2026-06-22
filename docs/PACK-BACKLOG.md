<!--
Copyright (c) 2026 JG Systems Consulting Ltd. — MIT License (see ../LICENSE).
SPDX-License-Identifier: MIT
-->

# Pack Backlog & Source Ledger

Status of every candidate source considered for the catalogue, so nothing is silently dropped.
Source-material download URLs are **not** published here (link policy — see
[LICENSING.md](LICENSING.md)); they live in the maintainers' build notes. Every candidate is
licence-vetted against [SOURCE-VETTING.md](SOURCE-VETTING.md) (Tier 1 = US-gov public domain;
Tier 2 = open licence with conditions carried forward; Excluded = paywalled / no grant).

> **Priority model.** **P0** — fills a thin/uncovered area, clean Tier 1, current edition exists:
> build first. **P1** — strong gap-filler or adds real depth. **P2** — niche, supporting,
> very large, or a component of a larger pack.

> **How to work an item.** Vet the licence against the *source's own grant clause* (not a search
> summary) → extract → outline → synthesise reference-depth chapters → verify (no verbatim overlap,
> structure/tier valid, index grounded). The `jgs-reference-skill` tool automates this pipeline.

---

## ✅ Built / shipped (16 packs + 2 signposts)

| Pack | Source | Tier |
|------|--------|------|
| `sebok` | Guide to the SE Body of Knowledge v2.13 | 2 (CC BY-NC-SA) |
| `requirements-writing` | EARS patterns + requirement-quality characteristics (multi-source) | 2 / guidance |
| `nasa-se-handbook` | NASA SE Handbook (SP-2016-6105 Rev 2) | 1 |
| `nasa-npr-7123` | NASA NPR 7123.1 — SE Processes & Requirements | 1 |
| `nasa-risk` | NASA/SP-2011-3422 — Risk Management Handbook | 1 |
| `nasa-system-safety` | NASA/SP-2014-612 — System Safety Handbook | 1 |
| `nasa-hsi` | NASA/SP-2015-3709 — Human Systems Integration Practitioner's Guide | 1 |
| `mil-std-882` | MIL-STD-882E — DoD System Safety | 1 |
| `dodaf` | DoD Architecture Framework 2.02 | 1 |
| `dau-se-guidebook` | DoD SE Guidebook (OUSD R&E, Feb 2022) | 1 |
| `gao-tra` | GAO-20-48G — Technology Readiness Assessment Guide | 1 |
| `nist-sse` | NIST SP 800-160 Vol 1 + Vol 2 | 1 |
| `nist-csf` | NIST CSF 2.0 | 1 |
| `nist-ssdf` | NIST SP 800-218 | 1 |
| `nist-ai-rmf` | NIST AI 100-1 | 1 |
| `eu-ai-act` | Regulation (EU) 2024/1689 | 2 |
| `omg-signpost` | OMG specs — citation-only | signpost |
| `se-standards-signpost` | ~55 SE-related standards — citation-only | signpost |

---

## 🟡 Candidate backlog — verified in the 2026-06-22 cross-family sweep

27 new buildable Tier-1/2 sources + 5 previously-vetted-unbuilt, all redistributability-confirmed.
Grouped by cluster; build first by the order below.

### Build order (next up)

1. **`nasa-systems-modeling`** (NASA-HDBK-1009A) — closes the #1 thin area (MBSE).
2. **`faa-sem`** (FAA Systems Engineering Manual) — biggest single SE-core gap (civil-agency).
3. **Cost & schedule cluster** — `gao-cost`, `nasa-ceh`, `gao-schedule`, `nasa-schedule` (zero coverage today).
4. **V&V / T&E** — `dod-te-guidebook`, `faa-ams-vv` (flagged still-thin).
5. **Reliability** — `nasa-rm-standard`, `faa-rma`.

### Cost & schedule estimating — *no coverage today* (P0)

| Proposed slug | Source (doc-id, edition) | Publisher | Tier | Pri | Build caveats |
|---|---|---|---|---|---|
| `gao-cost` | GAO-20-195G Cost Estimating & Assessment Guide | GAO | 1 | P0 | GAO public-use notice (verbatim p. xii family); redraw embedded 3rd-party figures. |
| `nasa-ceh` | NASA Cost Estimating Handbook v4.0 | NASA | 1 | P0 | Public release; pairs with `nasa-risk`. |
| `gao-schedule` | GAO-16-89G Schedule Assessment Guide (Dec 2015) | GAO | 1 | P0 | 10 best practices + 19 case studies; redraw 3rd-party figures. |
| `nasa-schedule` | NASA Schedule Management Handbook (2024 ed) | NASA | 1 | P0 | **Use the 2024 update**, not the superseded 2010 NASA/SP-2010-3403. |

### Verification & validation / T&E — *flagged still-thin* (P0)

| Proposed slug | Source | Publisher | Tier | Pri | Build caveats |
|---|---|---|---|---|---|
| `dod-te-guidebook` | DoD Test & Evaluation Enterprise Guidebook (Aug 2022) | OUSD R&E | 1 | P0 | Distribution A; headline open T&E source. |
| `faa-ams-vv` | FAA AMS Lifecycle V&V Guidelines v3.0 (Apr 2017) | FAA NextGen | 1 | P0 | **Paraphrase the quoted CMMI v1.2 (SEI) blocks — do not reproduce verbatim.** |

### MBSE / digital engineering — *#1 thin area* (P0–P2)

| Proposed slug | Source | Publisher | Tier | Pri | Build caveats |
|---|---|---|---|---|---|
| `nasa-systems-modeling` | NASA-HDBK-1009A (Rev A, 2025) | NASA OCE | 1 | P0 | Tool-agnostic SysML tied to NPR 7123.1; current Rev A. |
| `nasa-de-acquisition` | NASA-HDBK-1004 — Digital Engineering Acquisition Framework | NASA OCE | 1 | P1 | 217 pp; pairs with HDBK-1009A. |
| `dod-digital-engineering` | DoD Digital Engineering Strategy (2018) + DE Fundamentals (2022) | OUSD R&E | 1 | P1 | Build around the 2018 Strategy (Fundamentals PDF is ~2 pp). Exclude CAC-gated DEBoK. |
| `digital-systems-engineering` | *Towards Digital Engineering* (arXiv:2002.11672) | arXiv (ODU) | 2 | P2 | **CC BY 4.0 on the arXiv PDF only** (not the paywalled journal version). ~28 pp — component, not standalone. |

### Core SE depth (P0–P1)

| Proposed slug | Source | Publisher | Tier | Pri | Build caveats |
|---|---|---|---|---|---|
| `faa-sem` | FAA Systems Engineering Manual v1.0.1 | FAA | 1 | P0 | 360 pp, zero copyright/distribution markings; civil-agency SE companion to NASA/DAU. |
| `nasa-se-expanded` | NASA Expanded Guidance for SE Vol 1 (Practices) + Vol 2 (Crosscutting/Appendices), SP-2016-6105-SUPPL | NASA | 1 | P1 | The un-condensed source behind `nasa-se-handbook`; **build as added depth, run a redundancy check** (this is the SUPPL — distinct from the handbook, which earlier collided on URL). |

### Reliability / maintainability / availability — *uncovered* (P1–P2)

| Proposed slug | Source | Publisher | Tier | Pri | Build caveats |
|---|---|---|---|---|---|
| `nasa-rm-standard` | NASA-STD-8729.1A (Rev A, 2017) | NASA OSMA | 1 | P1 | Objectives-driven R&M framework; 52 pp, no restrictions. |
| `faa-rma` | FAA-HDBK-006D (8 Oct 2020) | FAA | 1 | P1 | **Use 006D**, not 006B. |
| `nasa-fault-management` | NASA-HDBK-1002 (Draft 2, Apr 2012) | NASA OCE | 1 | P2 | **Draft — never finalised; flag draft status in SKILL.md & PACK.yaml notes.** |

### Risk (quantitative / process) (P1)

| Proposed slug | Source | Publisher | Tier | Pri | Build caveats |
|---|---|---|---|---|---|
| `nasa-pra` | NASA/SP-2011-3421 — PRA Procedures Guide, 2nd ed | NASA OSMA | 1 | P1 | Event/fault trees, uncertainty/Monte Carlo, CCF; deepens `nasa-risk`. |
| `dod-rio` | DoD Risk, Issue & Opportunity Mgmt Guide (Sep 2023 + Ch 2.2) | OUSD R&E | 1 | P1 | Distribution A (DOPSR 23-S-3231); DoD-side complement to `nasa-risk`/`dau-se-guidebook`. |

### Software / agile for systems — *uncovered* (P1)

| Proposed slug | Source | Publisher | Tier | Pri | Build caveats |
|---|---|---|---|---|---|
| `nasa-swehb` | NASA-HDBK-2203 — Software Engineering & Assurance Handbook (Ver D, 2020) | NASA OCE | 1 | P1 | **Exclude IEEE/ISO-reprinted blocks verbatim** (precedent: `nist-sse`); prefer the standards.nasa.gov PDF. |
| `gao-agile` | GAO-24-105506 — Agile Assessment Guide (2023) | GAO | 1 | P1 | Updates GAO-20-590G; exclude embedded copyrighted images. |

### Architecture / modular open systems / CPS (P1)

| Proposed slug | Source | Publisher | Tier | Pri | Build caveats |
|---|---|---|---|---|---|
| `dod-mosa` | MOSA Implementation Guidebook (Feb 2025, DOPSR 25-T-1210) | OUSD R&E | 1 | P1 | Current authority replacing the 2013 OSA guidebook; Distribution A. |
| `nist-cps` | NIST SP 1500-201/202/203 — CPS Framework Vols 1–3 | NIST | 1 | P1 | Bundle as one pack; **drop the 2 permission-licensed 3rd-party figures (Beecham/ETSI)**. |

### Configuration & data management — *uncovered* (P1)

| Proposed slug | Source | Publisher | Tier | Pri | Build caveats |
|---|---|---|---|---|---|
| `mil-hdbk-61` | MIL-HDBK-61B Configuration Management (Change 1, 15 Aug 2025) | DoD | 1 | P1 | **Use current 61B**, not the 2001 61A(SE). Aligned to ANSI/EIA-649. |

### Readiness / manufacturing & quality (P1–P2)

| Proposed slug | Source | Publisher | Tier | Pri | Build caveats |
|---|---|---|---|---|---|
| `mrl-deskbook` | Manufacturing Readiness Level (MRL) Deskbook (v2025) | OSD ManTech | 1 | P1 | Distribution A; deepens `gao-tra` (MRL 1–10). |
| `dod-mq-bok` | DoD Manufacturing & Quality Body of Knowledge (Jul 2025) | OUSD R&E | 1 | P2 | **Large (~1,658 pp) — chunk by lifecycle phase.** Approved for public release. |

### Other distinct gaps (P2)

| Proposed slug | Source | Publisher | Tier | Pri | Build caveats |
|---|---|---|---|---|---|
| `faa-hf-std` | FAA HF-STD-001B Human Factors Design Standard (2016) | FAA WJHTC | 1 | P2 | HSI beyond NASA; complements `nasa-hsi`. |
| `faa-req-handbook` | DOT/FAA/AR-08/32 — Requirements Engineering Mgmt Handbook (2009) | DOT/FAA | 1 | P2 | Embedded/real-time slant; complements `requirements-writing`. |
| `nist-stat-handbook` | NIST/SEMATECH e-Handbook of Statistical Methods (NIST HB 151) | NIST | 1 | P2 | **HTML/web-native (per-chapter) — different ingestion than PDF packs.** Watch per-block 3rd-party figures. |
| `sd-22-dmsms` | SD-22 DMSMS Guidebook (Apr 2024) | DSPO | 1 | P2 | Sustainment/obsolescence; source via DTIC/ASSIST (DAU link 403s). |
| `grcse` | Graduate Reference Curriculum for SE (v1.1, 2015) | BKCASE/Stevens | 2 | P2 | **CC BY-NC-SA on Stevens prose only** (3rd-party tables = CC BY-NC-ND, exclude); mirror `sebok`/LICENSE. |
| `dau-glossary` | DAU Glossary of Defense Acquisition Acronyms & Terms | DAU | 1 | P2 | Lookup companion to `dau-se-guidebook`; snapshot a dated DTIC edition. |

---

## 🔵 Signpost-only — clean licence, but not worth a build

Cite (via a `kind: signpost` entry), don't package — off-topic, redundant, or superseded:

| Source | Why signpost not build |
|---|---|
| NIST SP 800-53 Rev 5 / SP 800-39 | Tier 1 but security/privacy controls & info-sec risk governance — cybersecurity, not SE. |
| GAO-21-519SP AI Accountability Framework | Tier 1 but overlaps `nist-ai-rmf` + `eu-ai-act`; only the auditor lens is distinct. |
| NASA RCM Guide (facilities/collateral equipment) | Tier 1 but facilities maintenance, narrow/less SE-transferable than `nasa-rm-standard`. |
| MOSA Reference Frameworks (May 2020) | Tier 1 but superseded by the Feb 2025 MOSA Implementation Guidebook (build that instead). |
| UK MOD PYRAMID Technical Standard + Guidance | Tier 2 (OGL v3.0, genuinely open) but a ~1,500-pp combat-air component architecture — niche; reconsider only for a dedicated open-architecture exemplar pack. |

---

## ⏸ Deferred / superseded notes

- `nasa-se-expanded` was previously deferred (auto-found URL collided with the SE Handbook). Now
  disambiguated: it is the **SP-2016-6105-SUPPL** (Vols 1–2), genuinely distinct from
  `nasa-se-handbook` — build as added depth after a redundancy check.

## 🔴 Excluded — not packageable

| Source | Why |
|--------|-----|
| **OMG formal specs** (UML, SysML, BPMN, UAF, MOF, XMI, OCL, DDS…) | Informational-use-only public grant: no posting, no commercial transfer, no modification. Signposted in `omg-signpost`. |
| **NAF** (NATO Architecture Framework) | NATO all-rights-reserved; no open/CC grant. |
| **DAU Defense Acquisition Guidebook** | Retired; replacement is web-only HTML, no clean single PDF. |
| **CMMI** (ISACA) · **ECSS** (ESA) | Copyright-locked / no redistribution grant. |
| ISO/IEC/IEEE (15288, 29148, 42010, 15026, 12207…), INCOSE SE Handbook & Vision, SWEBOK, MITRE SE Guide, TOGAF/ArchiMate, PMBOK | See [SOURCE-VETTING.md](SOURCE-VETTING.md). Signposted in `se-standards-signpost`. |

## Coverage assessment (2026-06-22)

- **Saturated:** AI governance (`nist-ai-rmf` + `eu-ai-act` + `nist-csf` + `nist-ssdf`).
- **About to be covered** once the cost/schedule cluster builds: currently **zero** cost/schedule packs.
- **Still genuinely thin** even with the open sources above: **V&V / T&E** (the authoritative
  ISO/IEC/IEEE 15288/29148/15026 V&V standards remain paywalled/excluded — only DoD T&E + FAA AMS
  V&V are open).
- **Net:** ~6–9 months of Tier-1 public-domain build runway before the repo bumps against
  genuinely commercial (ISO/IEEE/INCOSE) standards, which are correctly signposted, not built.

## Lesson recorded

Licence classification MUST read the **actual public grant clause** of the source, not a web-search
summary. The OMG case (a search summary surfaced the permissive company→OMG grant, masking the
restrictive public grant) is why source confirmation now content-verifies the licence text directly
before any build. For US-gov works, confirm a public-release / Distribution-A / public-use statement
on the document itself, and watch for **embedded third-party reprints** (IEEE, ISO, CMMI/SEI, ETSI)
that must be paraphrased or dropped — never reproduced verbatim.

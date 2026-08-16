# v1.18 Capability Gap Report — jgs-se-knowledge-packs

**Date:** 2026-08-14
**Inputs:** `docs/capability-pack-map.json` (authoritative, 32 clusters, 570 entries — reconciles with the regenerated summary table in `docs/capability-pack-map.md`), `catalog.json` (54 pack slugs as of writing; 8 new packs added in v1.17.0), `docs/SOURCE-VETTING.md` licence tiers.
**Note:** `doe-o-413-3` was renamed from `doe-413-3b` in v1.17.0 (same content, new slug). The capability map already uses the new slug; no action needed at v1.18 beyond awareness during vetting.

**Thresholds:** EMPTY = 0 entries; THIN = < 8 entries OR ≤ 2 distinct contributing packs; ADEQUATE = otherwise.

---

## 1. Cluster status table (all 32)

| # | Cluster | Entries | Distinct packs | Status |
|---|---------|---------|----------------|--------|
| 1 | Systems Thinking & Fundamentals | 25 | 7 | ADEQUATE |
| 2 | Requirements Engineering | 19 | 6 | ADEQUATE |
| 3 | Requirements Traceability & Allocation | 2 | 2 | THIN (count) |
| 4 | Architecture & Design | 20 | 9 | ADEQUATE |
| 5 | Interface Management & ICIDs | 2 | 2 | THIN (count) |
| 6 | Integration | 3 | 3 | THIN (count) |
| 7 | Verification | 9 | 2 | THIN (diversity) |
| 8 | Validation | 3 | 2 | THIN (count + diversity) |
| 9 | Test & Evaluation | 11 | 1 | THIN (diversity — single source) |
| 10 | Modeling, MBSE & SysML | 16 | 4 | ADEQUATE |
| 11 | Digital Engineering & Digital Twins | 24 | 3 | ADEQUATE |
| 12 | Configuration Management & Baselines | 14 | 5 | ADEQUATE |
| 13 | Data & Information Management | 6 | 6 | THIN (count) |
| 14 | Risk Management | 26 | 6 | ADEQUATE |
| 15 | Opportunity/Benefit Management | 1 | 1 | THIN (count + diversity — worst cluster) |
| 16 | Decision Analysis & Trade Studies | 2 | 2 | THIN (count) |
| 17 | Technical Planning & Work Breakdown | 6 | 5 | THIN (count) |
| 18 | Measurement & Technical Assessment | 36 | 9 | ADEQUATE |
| 19 | Quality Assurance & Process Compliance | 3 | 3 | THIN (count) |
| 20 | Safety, Reliability & Survivability | 88 | 10 | ADEQUATE |
| 21 | Cybersecurity & Security Engineering | 68 | 9 | ADEQUATE |
| 22 | Human Systems Integration / Human Factors | 26 | 4 | ADEQUATE |
| 23 | Logistics, Supportability & Sustainment | 11 | 1 | THIN (diversity — single source: sd-22-dmsms) |
| 24 | Operations, Maintenance & Disposal | 6 | 4 | THIN (count) |
| 25 | Training & Documentation Delivery | 0 | 0 | **EMPTY** |
| 26 | Project/Program Management | 66 | 11 | ADEQUATE |
| 27 | Supplier, Procurement & Acquisition | 7 | 6 | THIN (count) |
| 28 | Stakeholder Engagement & Needs | 3 | 3 | THIN (count) |
| 29 | Governance, Reviews, Gates & Control Points | 17 | 6 | ADEQUATE |
| 30 | Standards, Tailoring & Process Models | 35 | 13 | ADEQUATE |
| 31 | Specialty Engineering | 7 | 3 | THIN (count) |
| 32 | Assurance & System Assurance | 8 | 3 | ADEQUATE |

**Summary:** 1 EMPTY / 15 THIN / 16 ADEQUATE. Total entries: 570 across 32 clusters (reconciled against `docs/capability-pack-map.md`).

---

## 2. Per-thin-cluster candidate shortlist

Licence tiers per `docs/SOURCE-VETTING.md`: Tier 1 = public domain (US/UK gov works, 17 U.S.C. § 105); Tier 2 = free with explicit redistribution grant. All URLs verified live August 2026 unless marked UNVERIFIED.

### Cluster 25 — Training & Documentation Delivery (EMPTY)
| Source | Body | Doc ID | Tier | URL | Fattens | Pages est. |
|---|---|---|---|---|---|---|
| Technical Data Packages for materiel acquisition | US DoD | MIL-STD-40051 | 1 | https://quicksearch.dla.mil (ASSIST/PDREP) | 25, 24 | ~80 |
| A Guide for Technical Writers & Editors (documentation delivery practice) | NASA | NASA SP-7084 | 1 | https://ntrs.nasa.gov | 25, 28 | ~110 |
| DAU AAF guidebooks (training pathway content) | DAU/DoD | — | 1 | https://aaf.dau.edu/guidebooks/ | 25, 27 | ~60 |

### Cluster 15 — Opportunity/Benefit Management (1 entry, 1 pack)
| Source | Body | Doc ID | Tier | URL | Fattens | Pages est. |
|---|---|---|---|---|---|---|
| Guidelines and Discount Rates for Benefit-Cost Analysis of Federal Programs | OMB | Circular A-94 | 1 | https://www.whitehouse.gov/omb/information-for-agencies/circulars/ | 15, 16 | ~60 |
| Preparation, Submission, and Execution of the Budget (capital programming, benefits) | OMB | Circular A-11 (Part 3/7 capital chapters) | 1 | https://www.whitehouse.gov/wp-content/uploads/omb-assets/a11_current/ | 15, 17, 26 | ~120 (relevant chapters) |
| US Army Cost Benefit Analysis Guide | US Army (ASAFM) | — | 1 | https://www.asafm.army.mil/Portals/72/Documents/Offices/CE/US%20Army%20Cost%20Benefit%20Analysis.pdf | 15, 16 | ~80 |

### Cluster 9 — Test & Evaluation (single source: dod-te-guidebook)
| Source | Body | Doc ID | Tier | URL | Fattens | Pages est. |
|---|---|---|---|---|---|---|
| T&E Enterprise Guidebook (v3, June 2022) | DOT&E / OSD | — | 1 | https://www.afacpo.com/AQDocs/DOT%2526E%2520Test%2520and%2520Evaluation%2520Enterprise%2520Guidebook_FINAL_v3%2520June%25202022.pdf (mirror; canonical via dote.osd.mil) | 9, 7, 8 | ~120 |
| Test and Evaluation (AF T&E enterprise manual) | Dept of the Air Force | DAFMAN 63-119 | 1 | https://static.e-publishing.af.mil/production/1/saf_aq/publication/dafman63-119/dafman63-119.pdf | 9, 7, 27 | ~90 |
| Operational Test & Evaluation Manual (6th Ed.) | USMC MCOTEA | MCOTEA-POL-01054 | 1 | https://www.hqmc.marines.mil/Portals/61/Docs/MCOTEA/MCOTEA-POL-01054Manual6thEditionRev0.pdf | 9, 8 | ~100 |

### Cluster 8 — Validation (3 entries, 2 packs)
| Source | Body | Doc ID | Tier | URL | Fattens | Pages est. |
|---|---|---|---|---|---|---|
| M&S Verification, Validation & Accreditation Recommended Practice Guide | DoD CTO/M&S Office | VV&A RPG | 1 | https://www.cto.mil/sea/vva_rpg/ | 8, 7, 16, 9 | ~200 (web guide; PDF build exists) |
| DoDI 5000.61 / DoDM 5000.102 (VV&A implementing manual) | DoD | DoDM 5000.102 | 1 | https://www.esd.whs.mil/Portals/54/Documents/DD/issuances/dodm/5000102m.PDF | 8, 7 | ~30 |

### Cluster 7 — Verification (9 entries, 2 packs — diversity-fragile)
Covered by DOT&E Guidebook, DAFMAN 63-119, and VV&A RPG above; no cluster-7-only additions needed beyond those.

### Cluster 5 — Interface Management & ICIDs (2 entries, 2 packs)
| Source | Body | Doc ID | Tier | URL | Fattens | Pages est. |
|---|---|---|---|---|---|---|
| Preparation of Interface Documentation (IRD/ICD/IR formats & content) | FAA | FAA-STD-025 | 1 | https://rosap.ntl.bts.gov/view/dot/42955 (canonical); https://everyspec.com/FAA/FAA-STD/download.php?spec=FAA-STD-025F.003031.pdf (mirror, rev F) | 5, 3, 12 | ~50 |
| GPS Interface Control Documents (worked ICD exemplars) | GPS.gov (US Space Force/Civil) | ICD-IS-200/300 series | 1 | https://www.gps.gov/interface-control-documents-icds-interface-specifications-iss | 5 | ~150 (select) |

### Cluster 3 — Requirements Traceability & Allocation (2 entries, 2 packs)
FAA-STD-025 above (IR/ICD change control feeds traceability); plus:
| Source | Body | Doc ID | Tier | URL | Fattens | Pages est. |
|---|---|---|---|---|---|---|
| Requirements Management via Digital Acquisition pathway guidebook | DAU/DoD | AAF Software & Digital IT pathway guide | 1 | https://aaf.dau.edu/guidebooks/ | 3, 27 | ~70 |

### Cluster 6 — Integration (3 entries, 3 packs)
| Source | Body | Doc ID | Tier | URL | Fattens | Pages est. |
|---|---|---|---|---|---|---|
| Software Acquisition pathway guidebook (integration/DevSecOps guidance) | DAU/DoD | AAF guidebook | 1 | https://aaf.dau.edu/guidebooks/ | 6, 27 | ~70 |
| DAFMAN 63-119 DT&E/integration chapters (above) | DAF | DAFMAN 63-119 | 1 | (above) | 6, 9 | — |

### Cluster 13 — Data & Information Management (6 entries, 6 packs)
| Source | Body | Doc ID | Tier | URL | Fattens | Pages est. |
|---|---|---|---|---|---|---|
| NASA Software Engineering Handbook (data/CM interface chapters) | NASA | NASA-HDBK-2203 | 1 | https://standards.nasa.gov/standard/NASA/NASA-HDBK-2203 (wiki: https://swehb.nasa.gov) | 13, 19, 32 | ~350 (select chapters) |

### Cluster 16 — Decision Analysis & Trade Studies (2 entries, 2 packs)
| Source | Body | Doc ID | Tier | URL | Fattens | Pages est. |
|---|---|---|---|---|---|---|
| VV&A RPG (acceptance decision/credibility assessment chapters, above) | DoD CTO | VV&A RPG | 1 | (above) | 16, 8 | — |
| Army CBA Guide / OMB A-94 (structured decision analysis, above) | Army/OMB | — | 1 | (above) | 16, 15 | — |

### Cluster 17 — Technical Planning & Work Breakdown (6 entries, 5 packs)
| Source | Body | Doc ID | Tier | URL | Fattens | Pages est. |
|---|---|---|---|---|---|---|
| Work Breakdown Structures for Defense Materiel Items | DoD | MIL-STD-881F (current; MIL-HDBK-881A legacy guidance) | 1 | https://quicksearch.dla.mil/qsdocdetails.aspx?ident_number=36026 (PDREP); mirrors: https://everyspec.com/MIL-HDBK/MIL-HDBK-0800-0999/MIL-HDBK-881A_18883/ | 17, 26 | ~100 |

### Cluster 19 — Quality Assurance & Process Compliance (3 entries, 3 packs)
| Source | Body | Doc ID | Tier | URL | Fattens | Pages est. |
|---|---|---|---|---|---|---|
| NASA Software Engineering Handbook (SWE QA requirements & guidance) | NASA | NASA-HDBK-2203 + NPR 7150.2 SWE directives | 1 | https://standards.nasa.gov/standard/NASA/NASA-HDBK-2203 | 19, 13, 32 | — |

### Cluster 23 — Logistics, Supportability & Sustainment (single source: sd-22-dmsms)
| Source | Body | Doc ID | Tier | URL | Fattens | Pages est. |
|---|---|---|---|---|---|---|
| Product Support Manager / Sustainment guidebooks | DAU/DoD | AAF guidebooks | 1 | https://aaf.dau.edu/guidebooks/ | 23, 24 | ~80 |
| DOT&E T&E Enterprise Guidebook (suitability/OT&E of support, above) | DOT&E | — | 1 | (above) | 23, 9 | — |

### Cluster 24 — Operations, Maintenance & Disposal (6 entries, 4 packs)
| Source | Body | Doc ID | Tier | URL | Fattens | Pages est. |
|---|---|---|---|---|---|---|
| Process for Limiting Orbital Debris & End-of-Mission disposal/decommissioning | NASA | NASA-STD-8719.14 | 1 | https://standards.nasa.gov | 24, 20 | ~40 |

### Cluster 27 — Supplier, Procurement & Acquisition (7 entries, 6 packs)
DAU AAF guidebooks (above; multiple pathway guides cover market research, solicitation, supplier surveillance) — fattens 27, 3, 6, 25. Also DAFMAN 63-119 (contractor testing) fattens 27, 9.

### Cluster 28 — Stakeholder Engagement & Needs (3 entries, 3 packs)
No strong Tier-1/2 candidate beyond existing coverage (GAO TA Design Handbook would fit but is already the `gao-tra` pack). Lowest priority; consider SEBoK expansion instead of new pack.

### Cluster 31 — Specialty Engineering (7 entries, 3 packs)
| Source | Body | Doc ID | Tier | URL | Fattens | Pages est. |
|---|---|---|---|---|---|---|
| Design & Fabrication of Ground Support Equipment (loads, environments, specialty analysis) | NASA | NASA-STD-5005D w/Ch.1 | 1 | https://standards.nasa.gov/standard/NASA/NASA-STD-5005 | 31, 5 (partial), 24 | ~90 |

---

## 3. Recommended v1.18 candidate ranking

Value ≈ clusters fattened × thinness severity × licence cleanliness (all Top-5 are Tier 1).

1. **DoD VV&A Recommended Practice Guide** (DoD CTO/M&S Office, https://www.cto.mil/sea/vva_rpg/). Fattens 4 clusters (8-Validation [3 entries, 2 packs], 7-Verification [2 packs], 16-Decision Analysis, 9-T&E). Tier 1, live official HTML build with PDF/ZIP archives (also on DTIC/SE Goldmine). Highest breadth-per-pack in the shortlist.
2. **FAA-STD-025 — Preparation of Interface Documentation** (FAA, https://rosap.ntl.bts.gov/view/dot/42955). Fattens the two thinnest named clusters (5-Interface Mgmt [2 entries], 3-Traceability [2]) plus 12-CM. Tier 1, DOT repository canonical copy + rev F mirror. Short (~50 pp) and directly on-cluster.
3. **DOT&E T&E Enterprise Guidebook v3 (2022) + DAFMAN 63-119** (OSD/DOT&E + Dept of the Air Force). Fixes the two single-source clusters: 9-T&E (1 pack) and strengthens 23-Logistics (suitability) and 7/8. Both Tier 1, live PDFs verified. Bundle as one vetting workstream.
4. **MIL-STD-881F (+ legacy MIL-HDBK-881A guidance) — Work Breakdown Structures** (DoD/DLA). Fattens 17-Technical Planning & WBS (6 entries) and 26-PM. Tier 1 via PDREP/Quicksearch (free account may be needed — mirrors on Everyspec are free but third-party).
5. **OMB Circular A-94 (+ Army CBA Guide)** (OMB/US Army). Fattens the worst-count cluster 15-Opportunity/Benefit (1 entry, 1 pack) plus 16-Decision Analysis. Tier 1, canonical whitehouse.gov / army.mil PDFs.

Near-miss / next bench: NASA-HDBK-2203 (fattens 19-QA, 13-Data Mgmt, 32-Assurance — large but chapter-select needed), NASA-STD-8719.14 (24), DAU AAF guidebooks (27, 25, 23 — scattered chapters), NASA-STD-5005D (31 — relevance caveat: GSE-focused).

---

## 4. Non-viable / excluded (hand to SOURCE-VETTING at v1.18)

| Candidate | Reason excluded |
|---|---|
| Defense Acquisition Guidebook (DAG, dau.edu) | **Retired ~Aug 2022**, URLs dead; replaced by AAF pathway guidebooks. Original text only via Wayback Machine archives — provenance/versioning risk. Use AAF guidebooks instead. |
| CMU SEI technical notes / SQUARE | Copyright © Carnegie Mellon University; "unlimited distribution subject to the copyright" with permission routed to permission@sei.cmu.edu — no clean redistribution grant (fails Tier 1/2). Re-evaluate only with written CMU/SEI permission. |
| GAO-21-347G Technology Assessment Design Handbook | **Duplicate** — already covered as existing pack `gao-tra` in catalog.json. (GAO-20-243G was a draft; GAO-20-246G superseded by GAO-21-347G.) |
| GAO-20-195G Cost Estimating & Assessment Guide | **Duplicate** — already covered as `gao-cost`. |
| ISO 9001 / ISO-IEC standards, INCOSE SE Handbook, OMG specs, IEEE non-GET, ECSS | Paywalled or no-reproduction (per docs/SOURCE-VETTING.md exclusion list). Unchanged. |
| AFOTEC Test Design Guide | No public direct PDF found (AFOTEC pubs mostly behind DTIC or not released). **UNVERIFIED** — check DTIC (dtic.mil) for a released copy before considering. |
| FDA/ICH validation guidance | Domain drift (pharma GxP, not systems engineering) — out of repo scope. |
| MIL-Q-9858 (quality) | Obsolete/superseded with no current custodian; thin content relative to NASA-HDBK-2203 for cluster 19. |
| Everyspec / SE Goldmine as *sources* | Third-party mirrors, not canonical; acceptable only as fallback download locators — canonical copies must come from rosap.ntl.bts.gov, standards.nasa.gov, *.mil, esd.whs.mil. |

### UNVERIFIED items (needs resolution during v1.18 vetting)
1. **MIL-STD-40051** — current revision & direct PDREP download link not confirmed (quicksearch.dla.mil may require free account). Needed for EMPTY cluster 25.
2. **NASA SP-7084** — NTRS copy availability/edition not confirmed. Needed for cluster 25.
3. **DoD VV&A RPG PDF build** — official page is HTML (cto.mil); a citable consolidated PDF edition should be located (DTIC/SE Goldmine ZIP exists but third-party).
4. **MIL-STD-881F canonical PDF** — behind DLA Quicksearch access; mirror completeness vs. official copy to be confirmed.
5. **DAU AAF guidebooks pagination/licence page** — live and public, but per-guidebook copyright notices (third-party embedded content) should be spot-checked during vetting.

# NASA-HDBK-1004 Cheatsheet

## Quick Decision Rules

**"When do I obtain data rights and access?"**
At the RFP front end, while offerors compete. Anything deferred to closeout becomes a sole-source negotiation. Put the same data approach in the SOW, the DRD, and the Cost Volume (priced line item).

**"What carries a digital data requirement into the contract?"**
The DRD — one per deliverable data item, assembled into a DPD that rides with the SOW/PWS and is invoked by SOW/PWS language. Replace "contractor format acceptable" with named neutral formats.

**"How much Government control does this deliverable need?"**
Set the Data Type dial: Type 1 (approval before use, baseline-bound) · Type 2 (disapproval window, default 45 days) · Type 3 (deliver on time, no approval) · Type 4 (contractor-retained, on request — needs FAR §52.227-16) · Type 5 (incidental, inspectable). Pick the lowest that protects the baseline.

**"Which license-rights category?"**
Use Table 3 by funding source and commerciality. Never below Limited Rights (noncommercial TD) or Restricted Rights (noncommercial CS). Mark less-than-unlimited data with the FAR 52.227-14 Alt II/III legend.

**"How mature must the TDP be right now?"**
By life-cycle review: Conceptual ≈ SRR/SDR · Developmental before PDR · Product before CDR · Commercial for off-the-shelf. Grounded in MIL-STD-31000.

**"Which interoperability use case sets the bar?"**
Run all four (Viewing → Data Exchange → Data Integrity → Data Interoperability Formats); specify to the heaviest one you genuinely need.

---

## The Framework — Two Instruments, One Environment

| Layer | What it is |
|---|---|
| **Acquisition framework** (upstream) | DRDs + SOW/RFP contract language that define and pull in the right data under contract |
| **Digital Engineering Environment (DEE)** (downstream) | the connected fabric of data, people, processes, technology that stores/accesses/analyzes/visualizes the models |

Causal chain: right data → right people → right time → right decision → lower risk → higher probability of mission success. Scope spine: Pre-Phase A through Phase F.

**Five key areas to execute the framework:** Model-Based Data Definition (App C) · Digital Data Collaboration (App D) · Architecture (App E) · Interoperability Standards (App F) · Contractual Data Acquisition via DRDs (§5, App A/B).

## The DRD Suite (Appendix A)

| DRD | Role |
|---|---|
| **STD-TDP** | Technical Data Package — complete technical description; MIL-STD-31000; maturing levels |
| **STD-MBx** | engineering MBx models (CAD/CAE/CAM) + indentured product structure |
| **STD-CDMP** | Configuration & Data Management Plan — the backbone; SAE GEIA-859 / EIA-649 / EIA-649-2 |
| **STD-CDMPA** | joint CDM Process Audit |
| **STD-CSA** | Configuration Status Accounting report set |
| **STD-SDT** | Specification & Drawing Trees (spec trees pre-PDR, drawing trees pre-CDR) |
| **STD-EMDAL** | Engineering Models, Drawings & Associated Lists; ASME Y14 + MIL-STD-130 |
| **STD-CR** | Change Request; SAE EIA-649-2; routine/urgent/emergency |
| **STD-AD** | FCA/PCA documentation |
| **STD-REF** | Requirements Exchange Format (UUID schema, RIF/ReqIF) |
| **STD-MRI** | Master Records Index (as-delivered build standard) |

DRDs cite each other on purpose — specify them as a connected set, not isolated documents. Tailor everything; Appendix A is an example library.

## CDM as a Closed Loop

**Plan (CDMP) → Identify (CIs, baselines) → Control (CRs, CCBs) → Account (CSA) → Verify (CDMPA process, FCA/PCA product).**
- **FCA** asks "does it perform to the approved documentation?"
- **PCA** asks "is it built the way the drawings say?"
- Both establish the **Product Baseline**. Three baselines: functional, allocated, product.
- Functional-baseline changes are always Major; product-baseline changes are Major or Minor (SAE EIA-649-2).

## Requirements Exchange (REF)

- Every requirement object owns a **UUID** (ISO/IEC 11578, 8-4-4-4-12 hex).
- Required: ID, UUID, name, shall-text, lifecycle state, Previous Version UUID (self if none), Last Modified, System Id.
- **Lifecycle states:** In-Work → Completed → Accepted → Obsolete.
- **Traceability** = multi-cardinality Upstream/Downstream UUID links (tool-independent).
- **Verification methods:** Test · Demonstration · Inspection · Analysis (multi-valued).
- Wire format: **RIF/ReqIF-compatible XML**.

## Model-Based Data Definition (Appendix C)

- A deliverable's truth = **{object + metadata + state + effectivity + authorized usage}** — object type alone never determines usage.
- Models are authoritative; documents are generated views. When they disagree, the model wins.
- Map supplier release states → program destination states (Notional State Compatibility Map) via MBE Plan + SOW/PWS + MIL-STD-31000.
- **Tessellation must out-resolve the measurement** it supports.
- M&S credibility owned by PM + Technical Authority (NASA-STD-7009 / NASA-HDBK-7009).
- BOM views: EBOM (as-designed) · MBOM (as-built) · as-manifested · as-flown · as-disposed, with effectivity by event/date/lot/serial.
- Component taxonomy: System → Segment → Element → Subsystem → Assembly → Subassembly → Part.

## Architecture (Appendix E) — Four Owned Layers

| Architecture | Owner |
|---|---|
| **Security** | Agency CIO (NPR 2800.1 / 2810.1) |
| **Information Support System (ISSA)** | Agency CIO (open APIs, enterprise service buses) |
| **Data** | CIO infrastructure; engineering defines content; PM/Technical Authority sign-off |
| **Process** | PM/Technical Authority defines; CIO + Mission Directorate implements |

**GSMAF** (ISO/IEC/IEEE 42010 + NPR 7120.5/7123.1) is the worked science-mission example.

## The Four Interoperability Use Cases (Appendix G)

A ladder of increasing demand: **Viewing → Data Exchange → Data Integrity → Data Interoperability Formats.**
- Keep **PMI** (3D annotations, manufacturing notes, material specs) distinct from **metadata** (text-only).
- Two integrity forms: relative to authoritative **source** (security view) and relative to authoritative **model** (database view: component + composite).
- Attack manual copying with **automated data integration** + **automated data audits** (daily/weekly, low cost).
- Format maturity (Table 8): Level 1 Paper · Level 2 Formatted Docs (both unsupported under MBE) · Level 3 Standard XML · Level 4 repository-to-repository.

## Key External Standards

- **MIL-STD-31000 / 31000B** — TDP structure, levels, 3Di data, Type 3D TDPs
- **SAE GEIA-859 / EIA-649 / EIA-649-2** — data + configuration management
- **ASME Y14 family** (Y14.5/.24/.34/.41/.47/.100) — drawing, GD&T, digital product definition
- **ISO 10303 / STEP** (AP203/214/233/239/242) · **ISO 14306 (JT)** · **ISO 14739-1 (PRC)** · **ISO 32000-1 (PDF)**
- **NPR 7123.1** (SE processes; mandates technical-data management) · **NPR 7120.5** (program/project management, life cycle/KDPs)
- **NASA-STD-7009 / NASA-HDBK-7009** (M&S) · **NPR 1441.1 / NPD 1440.6** (records) · **LOTAR** (long-term archiving)
- **FAR 52.227-14 / DFARS 252.227-7026/-7027** (data rights/deferral) · **NIST SP 800-60/-53, FIPS 140-2** (security)

---

## Tells & Smells

- **"Contractor format acceptable"** → the phrase to eliminate; specify named neutral formats instead.
- **Calendar dates on submissions** → use event-relative milestones so the schedule survives slips.
- **Proprietary/vendor format when a neutral standard exists** → vendor lock-in; ingest-without-rework is lost.
- **Data requirements omitted from the contract** → the primary lesson learned; access becomes an end-of-contract ransom.
- **"Best available" / "existing contractor data"** → often turns out proprietary or costly to extract.
- **Top-level integrated DMU built from simplified representations** → defeats the accurate mock-up.
- **Acquiring more data than the life cycle needs** → buy the minimum essential set with sufficient rights.
- **Unmarked restricted-rights data** → missing FAR 52.227-14 Alt II/III legend.
- **Late metadata** → must be defined more than 90 days before first use.
- **Manual copy out of the authoritative source** → staleness clock starts immediately; automate integration + audits.
- **PDM consolidation mistaken for data sharing** → fewer visible systems ≠ better bi-directional exchange.
- **One rigid global process** → over-specification; pursue the core critical interoperability processes instead.
- **No Data Architecture from the start** → data becomes disorganized and nearly impossible to integrate as volume grows.
- **Documents treated as authoritative** → authority must live in the configuration-controlled model.

# NASA Digital Engineering Acquisition Framework (NASA-HDBK-1004) Glossary

Key terms from NASA-HDBK-1004, alphabetical, with chapter references. Definitions are synthesized in original wording, not reproduced from the source.

**Acceptance Data Package (ADP)** — a working, assemblable view of delivered data, contrasted with a TDP that is frozen and treated as a static historical record. (Ch 4)

**As-built / as-designed / as-sustained** — the physical item as actually manufactured, the configuration the TDP specifies, and the as-received baseline the Government forms by ingesting the TDP. A PCA confirms as-built matches as-designed. (Ch 2)

**Authoritative source** — the single, governing instance of a data item that all consumers point to; copying data out of it manually starts a staleness clock and is the dominant integrity risk. (Ch 6, Ch 7)

**Bill of Material (BOM)** — a functionally dependent list of physical items (name, reference number, quantity, unit of measure), managed in multiple views: as-designed (EBOM), as-built (MBOM), as-manifested, as-flown, as-disposed, with effectivity by event/date/lot/serial. (Ch 5)

**Change Request (CR)** — the DRD (STD-CR) proposing an engineering change for evaluation and disposition by the Configuration Approval Authority, with a defined minimum content set and priority of routine/urgent/emergency. (Ch 2)

**Configuration and Data Management (CDM)** — the closed loop of plan, identify, control, account, verify that governs requirements, baselines, and engineering products across the life cycle. (Ch 2, Ch 5)

**Configuration and Data Management Plan (CDMP)** — the DRD (STD-CDMP) describing how a supplier implements CDM; the backbone other CDM DRDs trace to, satisfying SAE GEIA-859, EIA-649, and EIA-649-2. (Ch 2)

**Configuration Status Accounting (CSA)** — the DRD (STD-CSA) delivering accurate, timely records of a product and its configuration as a defined report set; the system's memory of what changed and when. (Ch 2)

**Data Category Designation** — a two-letter taxonomy (CD, CM, DE, DM, SE, SW, QE, SA, etc.) classifying each DRD by discipline and feeding the DRD number. (Ch 2)

**Data Procurement Document (DPD)** — the assembly gathering every DRD for one contract into a single package that rides alongside the SOW or PWS. (Ch 2)

**Data Requirements Description (DRD)** — the atomic contractual instrument that fully specifies one deliverable data item: its purpose, content, format, compliance standards, maintenance, and submittal terms. The central lever of the whole framework. (Ch 1, Ch 2)

**Data Type (1–5)** — a five-level control-and-trust dial setting how much Government approval a deliverable needs: Type 1 (approval before use, baseline-bound), Type 2 (time-limited disapproval window, default 45 days), Type 3 (deliver on time, no approval), Type 4 (contractor-retained, delivered on written request), Type 5 (incidental, inspectable). (Ch 2)

**Digital Engineering Environment (DEE)** — the connected fabric of data, people, processes, and technology that stores, accesses, analyzes, and visualizes a system's evolving data and models for stakeholders across the enterprise. (Ch 1)

**Digital engineering acquisition framework** — the Handbook's titular construct: disciplined, collaborative processes (DRDs plus SOW language) that plan, acquire, and control the interoperable flow of product and configuration data across the product and data life cycles. (Ch 1)

**Digital Mock-Up (DMU)** — a model-based representation of an assembly used to check geometry, interference, and clash; distinguished as static (fixed parts) versus dynamic (moving parts). The integrated top-assembly DMU must not be built from simplified representations. (Ch 2, Ch 5)

**Engineering Models, Drawings, and Associated Lists (EMDAL)** — the DRD (STD-EMDAL) delivering manufacture/test/logistics definition in 2D/3D CAD, governed by ASME Y14 standards, the Global Drawing Requirements Manual, and MIL-STD-130. (Ch 2)

**FCA / PCA** — the Functional Configuration Audit (does it perform to the approved documentation?) and Physical Configuration Audit (is it built as designed?), delivered via the AD DRD (STD-AD); both feed establishment of the Product Baseline. (Ch 2)

**Goddard Space Mission Architecture Framework (GSMAF)** — a viewpoint-structured architecture framework (Science, Systems Engineering, Management, Enterprise) following ISO/IEC/IEEE 42010 with NPR 7120.5 and 7123.1. (Ch 6)

**Key Decision Point (KDP)** — a life-cycle gate (KDP 0 through KDP F) against which the MBE Plan schedules element maturity; KDP C is where the data roadmap and supplier interdependencies come into focus. (Ch 6, Ch 8)

**Lead Systems Integrator** — the role responsible for building integrated model sets so combined data stays consistent and complete and deliverables are clearly defined. (Ch 1)

**Light-weight viewable** — a CAD-derived product viewable on a standard PC with downloadable software, for stakeholders without CAD licenses, in formats such as 3D PDF and JT. (Ch 2)

**LOTAR (Long Term Archiving and Retrieval)** — the aerospace activity behind storing engineering data in IT-independent, long-readable formats for long-life programs. (Ch 5)

**Master Records Index (MRI)** — the DRD (STD-MRI) capturing the complete as-delivered build standard: indices of CIs, components, drawings, configuration documentation, technical manuals, ECPs, RFVs, and ancillary equipment. (Ch 3)

**MBx family** — the model-based artifacts whose integrity must be protected: MBSE, MBD (model-based definition), MBE (the enterprise), model-based engineering, MBM (manufacturing), and MBI (inspection). (Ch 5, Ch 6)

**Model-Based Definition (MBD)** — annotated 3D CAD capturing GD&T and PMI directly in the model rather than in separate drawings. (Ch 5, Ch 6)

**Model-Based Enterprise (MBE)** — the practice base the DEE is built on: an organization driving development, design, manufacturing, and life-cycle support from digital models. (Ch 1, Ch 5)

**Model-based data definition** — the discipline that fixes the meaning, scope, and handling of every model-based data category in the DRD so released data means the same thing everywhere it is consumed; a subset and critical element of MBE. (Ch 5)

**Model-Based Systems Engineering (MBSE)** — the systems-engineering subset of MBE, with the continually-refined system model at the center, sometimes expressed in SysML. (Ch 5)

**MBE Plan** — the controlled, signed program-wide document recording how MBE capabilities will be delivered (responsibilities, tools, IT services, timing); refreshed at least annually or at a major KDP and maintained through KDP F. (Ch 4, Ch 8)

**Models & Simulations (M&S) credibility** — the trustworthiness of simulation results, owned by the PM and delegated Technical Authority and governed by NASA-STD-7009 and NASA-HDBK-7009. (Ch 5)

**Neutral format** — a non-proprietary exchange format (e.g., STEP/ISO 10303, JT, 3D PDF) mandated over vendor formats so deliverables ingest into the receiver's tools without rework. (Ch 2, Ch 6)

**Office of Primary Responsibility (OPR) / Data Manager (DM)** — the split between the office holding technical/administrative control of a data requirement and the organization that receives, distributes, and processes the submittals. (Ch 2)

**PMI (Product and Manufacturing Information)** — richer-than-metadata content (3D annotations, manufacturing notes, material specs) added to a model, distinguished from text-only metadata. (Ch 5, Ch 7)

**Product Baseline** — the certified configuration the FCA/PCA pair establishes; the Government's as-sustained baseline seeded by ingesting the TDP. (Ch 2)

**Release (as a verb)** — authorizing dissemination of a particular version for a specific purpose; its meaning shifts across life-cycle phases, so object type plus intended use (not phase alone) determines usage. (Ch 5)

**Requirements Exchange Format (REF)** — the DRD (STD-REF) fixing a minimum requirement-object attribute set (UUID, name, shall-text, lifecycle state, version/source identity, optional traceability) carried as RIF/ReqIF-compatible XML so requirements stay integrable across vendor tools. (Ch 3)

**RIF / ReqIF (Requirements Interchange Format)** — the XML wire format carrying requirements and their metadata between vendor requirements-management tools. (Ch 3)

**Simplified representation** — an accurate single-surface, water-tight body representing the nominal as-designed shape (not a native CAD "simple representation"), used for integration, space-and-weight, and clearance. (Ch 2)

**Specification and Drawing Trees (SDT)** — the DRD (STD-SDT) giving top-down listings of the specifications and drawings allocating a configuration item's requirements; spec trees before PDR, drawing trees before CDR. (Ch 2)

**State-compatibility mapping** — translating each supplier's release-state vocabulary to program-defined destination states (Notional State Compatibility Map) so differences become inconsequential. (Ch 5)

**STEP / ISO 10303** — the family of neutral product-data application protocols (AP203, AP214, AP233, AP239, AP242) underpinning interoperable exchange; AP242 merges the aerospace AP203 and automotive AP214. (Ch 2, Ch 6)

**Technical Data Package (TDP)** — the DRD (STD-TDP) defining the complete technical description of an item (as-designed configuration, performance requirements, assurance procedures), grounded in MIL-STD-31000 and delivered in maturing levels (Conceptual, Developmental, Product, Commercial). (Ch 2)

**Three-dimensional intelligent (3Di) data** — model-based technical data per MIL-STD-31000B comprising 3D native models, derived 2D drawings, derived 3Di PDF viewables, and derived neutral files (JT, STEP). (Ch 6)

**Traceability (paired UUIDs)** — structural trace carried as multi-cardinality Upstream/Downstream UUID links so a receiving tool can validate the trace graph independent of any vendor's internal identifiers. (Ch 3)

**UUID** — a 128-bit identifier in the 8-4-4-4-12 hyphenated hex form (per ISO/IEC 11578) that every requirement object owns; the keystone of tool-independent identity and traceability. (Ch 3)

---
name: nasa-de-acquisition
description: "Knowledge base from the NASA Digital Engineering Acquisition Framework Handbook (NASA-HDBK-1004). Use for acquiring digital/model-based data under contract: the Data Requirements Description (DRD) instrument and the Appendix A DRD suite (TDP, MBx, CDMP, CSA, CR, FCA/PCA, SDT, EMDAL, REF, MRI); the Data Type 1-5 control scale; SOW/RFP/Cost-Volume contract language and data rights (FAR/DFARS, Table 3 license categories); the Requirements Exchange Format (REF/ReqIF, UUID schema) and Master Records Index; model-based data definition (MBSE, CAD/PMI, M&S credibility, BOM, release-state mapping, PLM); digital data collaboration, the four owned architectures, and interoperability standards (MIL-STD-31000, STEP/ISO 10303, ASME Y14); the four MBE interoperability use cases; and MBE Plan development. Scope is the acquisition and contracting side of digital engineering. Does not reproduce ISO/STEP/ASME/MIL-STD/SAE standard text, and the companion NASA-HDBK-1009A carries the deeper digital-engineering practitioner detail this handbook defers to."
---

<!-- argument-hint: [DRD / Data Type / contract language / data rights / REF / MRI / model-based data definition / collaboration / architecture / interoperability / use case / MBE Plan / chapter number] -->

# NASA Digital Engineering Acquisition Framework Handbook (NASA-HDBK-1004)
**Source**: NASA, Office of the NASA Chief Engineer (US Government work, public domain) | **Chapters**: 8

## When to use
Use this skill to specify, contract for, and control the digital data and models a program buys across the life cycle (Pre-Phase A through Phase F): writing DRDs and SOW/RFP language that force interoperable, machine-readable, neutral-format delivery; setting the right Government control level and data rights; standardizing requirement exchange and the as-delivered build record; governing model-based data definition and release; choosing interoperability standards; and developing the program's MBE Plan. This is the acquisition-and-contracting companion to the broader systems-engineering and MBSE landscape (`dau-se-guidebook`, `nasa-npr-7123`, `sebok`, `se-standards-signpost`).

**Prerequisites:** none — plain Markdown; no MCP server, API key, or licence tier needed at runtime.

## How to Use This Skill
- **Without arguments** — load the core frameworks below: the acquisition framework and DEE, the DRD instrument and Data Type scale, the contract-language placement model, REF/MRI, model-based data definition, the four architectures, the use-case ladder, and the MBE Plan.
- **With a topic** — ask about a specific DRD (e.g. "TDP", "MRI", "REF"), a Data Type, data rights / Table 3 license categories, release-state mapping, an interoperability standard (STEP/MIL-STD-31000/ASME Y14), or an MBE use case.
- **With a chapter** — `ch02` (the DRD suite + CDM), `ch03` (requirements exchange + contract language), `ch04` (data-acquisition contract language + rights), `ch05` (model-based data definition), `ch06` (collaboration/architecture/interoperability), `ch08` (MBE Plan).

Supporting files: `glossary.md`, `patterns.md`, `cheatsheet.md`.

> **One handbook, two halves.** The Handbook's **acquisition** half is the DRDs plus SOW/RFP contract language (chapters 1-4); its **model-based engineering** half is the data-definition, collaboration, architecture, interoperability, use-case, and planning appendices (chapters 5-8). The unifying move throughout: replace document-centric, "contractor format acceptable" delivery with model-based, neutral-format, contractually enforced data.

## Core Frameworks & Mental Models

### The digital engineering acquisition framework — what it is

NASA-HDBK-1004 is a guidance handbook (not a binding requirement) for buying and controlling digital data and models. It has two visible instruments — **Data Requirements Descriptions (DRDs)** and **contract language** for the Statement of Work / RFP — and one purpose: to stand up and feed a **Digital Engineering Environment (DEE)**, the connected fabric of data, people, processes, and technology that stores, accesses, analyzes, and visualizes a system's evolving data and models. It supersedes NASA-HDBK-0008 (PDLM) and broadens coverage to *all* program/project data, not just technical data. The framing is mission assurance: getting the right data to the right people at the right time enables the right decision, lowers risk, and raises the probability of mission success. Five key areas execute it — model-based data definition, digital data collaboration, architecture, interoperability standards, and contractual data acquisition via DRDs.

### The DRD — the contractual lever

A DRD is the atomic instrument that fully specifies one deliverable data item: its purpose, content, format, compliance standards, maintenance, and submittal terms. DRDs are assembled into a **Data Procurement Document (DPD)** that rides alongside the SOW/PWS and is invoked by SOW/PWS language. Treat each DRD as a *data contract with an interface spec attached* — it pins down the schema (Contents), the encoding (Format + named neutral standards), the SLA (submission timing as milestones, never calendar dates), and the access policy (Data Type). The acceptance criterion is integration without rework. Appendix A is an **example library** — select, tailor, and add DRDs per program. The baseline suite: STD-TDP, STD-MBx, STD-CDMP, STD-CDMPA, STD-CSA, STD-SDT, STD-EMDAL, STD-CR, STD-AD, STD-REF, STD-MRI. They cite each other deliberately — specify them as a connected set.

### The Data Type scale (1-5) — a control-and-trust dial

How much Government oversight a deliverable needs: **Type 1** (written approval before any use; the choice when data enters the Center baseline under CDM control), **Type 2** (time-limited disapproval window, default 45 days, tailorable), **Type 3** (deliver on time, no approval), **Type 4** (contractor-retained, delivered on written request — needs FAR 48 CFR §52.227-16 to compel), **Type 5** (incidental, inspectable). Pick the lowest level that still protects the baseline.

### Configuration & Data Management (CDM) — a closed loop

**Plan (CDMP) → Identify (CIs, baselines) → Control (CRs, CCBs) → Account (CSA) → Verify (CDMPA for process, FCA/PCA for product).** The CDMP is the backbone (SAE GEIA-859 / EIA-649 / EIA-649-2). Three baselines — functional, allocated, product. **FCA** asks "does it perform to the approved documentation?"; **PCA** asks "is it built as designed?" — both establish the Product Baseline. The TDP matures with the life cycle (Conceptual ≈ SRR/SDR, Developmental before PDR, Product before CDR, Commercial for off-the-shelf), grounded in MIL-STD-31000, and seeds the as-sustained Product Baseline once ingested.

### Requirements exchange and the build record

**REF (STD-REF)** standardizes a minimum requirement-object attribute set — every object owns a **UUID** (ISO/IEC 11578) plus shall-text, a lifecycle state (In-Work → Completed → Accepted → Obsolete), version/source identity, and optional multi-cardinality Upstream/Downstream UUID traceability — carried as **RIF/ReqIF**-compatible XML so requirements stay integrable across vendor tools. *Agree the schema, not the tool.* The **MRI (STD-MRI)** is the indexed as-delivered build standard (CIs, components to piece-part, drawings, configuration documentation, ECPs, RFVs, ancillary equipment); if you cannot reconstruct the build standard from the MRI, the configuration record has failed.

### Contract language and data rights

Buy the data while bidders still compete: put the same data approach in three places — the **SOW** (functional/technical requirements), the **DRD** (the details, submitted with the proposal), and the **Cost Volume** (data as a separate priced line item). Use **Table 3** to match each technical-data (TD) or computer-software (CS) deliverable to a license category (Unlimited, Government Purpose, Limited, Restricted, Specifically Negotiated, SBIR, Commercial) by funding source and commerciality; mark less-than-unlimited data with the FAR 52.227-14 Alt II/III legend; defer with priced options and DFARS 252.227-7026/-7027 plus a Data Accession List. Acquire the **minimum essential** data with **sufficient rights** for the full life cycle, including downstream re-bid.

### Model-based data definition

A subset and critical element of MBE, required by NPR 7123.1. The DRD is the *contract for meaning*: fix the meaning, scope, and handling of every MBx category there. A deliverable's truth is **{object + metadata + state + effectivity + authorized usage}** — object type alone never determines usage. Models are authoritative; documents are generated views. Map supplier release states to program-defined destination states (Notional State Compatibility Map). M&S credibility is owned by the PM and Technical Authority (NASA-STD-7009 / NASA-HDBK-7009). Manage multiple BOM views (EBOM/MBOM/as-manifested/as-flown/as-disposed) with effectivity.

### Collaboration, architecture, and interoperability

Interoperability needs IT standards *and* contractual enforcement (the DRD clause) — digitization alone fails (NIMA-RPT-004's ~40% manual-discrepancy finding). The Agency-level collaborative environment is four owned architectures — **Security** and **ISSA** (Agency CIO), **Data** (CIO infrastructure, engineering content, PM/TA sign-off), **Process** (PM/TA defines, CIO/Mission Directorate implements). Neutral 3D formats (STEP/ISO 10303, JT) are the collaboration medium when participants use different CAD systems. Standards are keyed to a maturity model. Run the **four interoperability use cases** — Viewing → Data Exchange → Data Integrity → Data Interoperability Formats — and let the heaviest you genuinely need set the bar.

### The MBE Plan

A living, formally controlled, signed program-wide document (one per single-project/tightly coupled program, per NPR 7120.5) recording *how* MBE capabilities will be delivered. **Table 9** schedules each MBE element through Preliminary → Baseline → Update across phases and KDPs; **Table 10** is the required section template (responsible competency + agreement + data). It is a *treaty, not a textbook* — signatures (PM, Mission Directorate AA, Center Directors, project managers) make it a resource commitment. Refresh at least annually or at a major KDP, through KDP F.

---

## Chapter Index

| # | Source area | Key content |
|---|-------------|-------------|
| [ch01](chapters/ch01-nasa-de-acquisition-framework-rationale-and-dee.md) | §1-5 Scope & rationale | The acquisition framework, the DEE, document-centric → model-based shift, five key areas, Lead Systems Integrators, applicability (NPR 7120.5), supersession of NASA-HDBK-0008 |
| [ch02](chapters/ch02-nasa-de-acquisition-drds-and-configuration-data-management.md) | App A DRD suite | The DRD/DPD instrument, Data Category designations, Data Type 1-5, the TDP/MBx/CDMP/CDMPA/CSA/SDT/EMDAL/CR/AD DRDs, CDM as a closed loop, neutral formats |
| [ch03](chapters/ch03-nasa-de-acquisition-requirements-exchange-and-contract-language.md) | App A.13-A.15 | Requirements Exchange Format (REF/ReqIF, UUID schema, lifecycle states, traceability), Master Records Index, contract language by data type, CDM SOW clauses |
| [ch04](chapters/ch04-nasa-de-acquisition-data-acquisition-contract-language.md) | App B contract language | SOW/DRD/Cost-Volume placement, data rights (TD/CS, Table 3 license ladder), FAR/DFARS, deferral instruments, IP strategy, MBE Plan, transmittal & security baselines |
| [ch05](chapters/ch05-nasa-de-acquisition-model-based-data-definition.md) | App C model-based data definition | MBSE/system model, CAD/PMI/DMU, M&S credibility, documents vs. models, archiving/LOTAR, PLM, CDM, BOM/PBS, release & change management, parts libraries, openness |
| [ch06](chapters/ch06-nasa-de-acquisition-collaboration-architecture-interoperability.md) | App D/E/F | Digital data collaboration, the MBx family, the four owned architectures, GSMAF, interoperability standards (MIL-STD-31000B, STEP/ISO 10303, Table 6/7), MBE Plan timing |
| [ch07](chapters/ch07-nasa-de-acquisition-mbe-use-cases.md) | App G use cases | The four MBE use cases (Viewing/Exchange/Integrity/Interoperability Formats), Table 8 format maturity, PMI vs. metadata, authoritative source & manual-copy risk, automated integration/audits |
| [ch08](chapters/ch08-nasa-de-acquisition-mbe-plan-development.md) | App J MBE Plan | MBE Plan development (Table 9 maturity schedule, Table 10 section template), signatures as commitment, KDP-aligned phasing, gap analysis, requirements traceability |

## Topic Index

- **Acquisition framework / DEE / Digital Engineering Environment** → ch01
- **Anti-patterns ("contractor format acceptable", omitted data requirements)** → ch04, ch03
- **Architecture (Security / ISSA / Data / Process)** → ch06
- **Authoritative source / manual-copy risk** → ch07
- **Bill of Material (BOM) / product breakdown structure** → ch05
- **CDM / Configuration and Data Management (closed loop)** → ch02, ch05
- **Configuration and Data Management Plan (CDMP)** → ch02
- **Configuration Status Accounting (CSA)** → ch02
- **Contract language / SOW / Cost Volume placement** → ch04, ch03
- **Data Category designations** → ch02
- **Data interoperability use cases (the four)** → ch07
- **Data Procurement Document (DPD)** → ch02
- **Data Requirements Description (DRD)** → ch02, ch01
- **Data rights / license categories / Table 3 / FAR / DFARS** → ch04
- **Data Type (1-5) control scale** → ch02
- **Digital Mock-Up (DMU)** → ch05, ch02
- **Engineering Models, Drawings & Associated Lists (EMDAL)** → ch02
- **Engineering release / change management / state mapping** → ch05
- **FCA / PCA (configuration audits)** → ch02
- **GSMAF (Goddard Space Mission Architecture Framework)** → ch06
- **Interoperability standards (STEP / ISO 10303 / MIL-STD-31000)** → ch06
- **Key Decision Points (KDP) / life-cycle phases** → ch08, ch06
- **Lead Systems Integrator** → ch01
- **Master Records Index (MRI)** → ch03
- **Maturity levels (format, Table 8)** → ch07
- **MBE Plan development (Table 9 / Table 10)** → ch08, ch04
- **MBx family (MBSE / MBD / MBE / MBM / MBI)** → ch06, ch05
- **Metadata vs. PMI** → ch07, ch05
- **Model-based data definition** → ch05
- **Model-Based Systems Engineering (MBSE) / system model** → ch05
- **Models & Simulations (M&S) credibility** → ch05
- **Neutral formats** → ch02, ch06
- **OPR / Data Manager split** → ch02
- **Parts and library management** → ch05
- **Product Baseline / baselines (functional / allocated / product)** → ch02
- **Requirements Exchange Format (REF / ReqIF)** → ch03
- **Standards keyed to maturity model** → ch06
- **Technical Data Package (TDP)** → ch02
- **Traceability (paired UUIDs)** → ch03
- **Transmittal & security baselines (NIST / FIPS)** → ch04
- **UUID / requirement object schema** → ch03

## Supporting Files

- [glossary.md](glossary.md) — key acquisition, DRD, CDM, and model-based terms, alphabetical, with chapter references
- [patterns.md](patterns.md) — 11 reusable patterns (buying data while bidders compete, the DRD as a data contract, the Data Type dial, maturing the TDP, REF/UUID identity, the MRI build record, neutral formats, data rights, release-state mapping, the four use cases, the MBE Plan as a treaty) with When/How/Trade-offs
- [cheatsheet.md](cheatsheet.md) — quick decision rules, the framework/DEE map, the DRD suite table, CDM loop, REF schema, model-based data definition, the four architectures, the use-case ladder, key external standards, tells & smells

---

## Scope & Limits

**Covers**: the acquisition and contracting side of NASA digital engineering per NASA-HDBK-1004 — the DRD instrument and the full Appendix A DRD suite; the Data Type 1-5 control scale and CDM; SOW/RFP/Cost-Volume contract language and data rights (FAR/DFARS, Table 3 license categories, deferral instruments); the Requirements Exchange Format and Master Records Index; model-based data definition (MBSE, CAD/PMI, M&S credibility, BOM, release-state mapping, PLM, parts libraries); digital data collaboration, the four owned architectures (Security/ISSA/Data/Process) and GSMAF; interoperability standards (MIL-STD-31000, STEP/ISO 10303, ASME Y14, the Table 6/7/8 framework); the four MBE interoperability use cases; and MBE Plan development.

**Does not cover in depth**: the source is an *acquisition* handbook, so it is thin on practitioner-depth digital-engineering technique — the companion **NASA-HDBK-1009A** carries that complementary detail (the data-architecture/metadata vocabulary, the NDAF requirement-type framework, and deeper M&S credibility practice are governed alongside it), and this pack repeatedly defers to it. It does not reproduce the text of the third-party standards it cites (ISO 10303/STEP, ASME Y14, MIL-STD-31000, SAE EIA-649/GEIA-859, ISO/IEC/IEEE 42010 — those remain the copyright of their publishers); it names them and describes how the Handbook invokes them. It does not provide the underlying NASA SE process model (see `nasa-npr-7123` / `dau-se-guidebook`), the binding legal text of FAR/DFARS clauses (route through Legal/Procurement), or program-specific tailoring — every example DRD and contract clause must be tailored by the acquiring program/project and reviewed before binding use.

**Jurisdiction & version**: NASA Technical Handbook NASA-HDBK-1004, Baseline (approved 2020-04-01), superseding NASA-HDBK-0008; a US Government work in the public domain. Guidance is recommended (not mandatory) outside its primary NPR 7120.5 program scope and never overrides existing Agency guidance — conflicts go to the delegated Technical Authority.

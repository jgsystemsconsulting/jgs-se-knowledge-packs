# Chapter — Model-Based Data Definition: MBSE, CAD/PMI, Modeling & Simulation, and PLM

## Core Idea

Model-based data definition is the discipline that makes a model-based enterprise (MBE) actually work as an acquisition mechanism rather than a slogan. In this NASA Technical Handbook (NASA-HDBK-1004), it is treated as one of MBE's essential constituent elements, whose purpose is to raise the probability of mission success by improving the availability, integrity, fidelity, and efficiency of model data, and by making that data interchangeable across both similar and dissimilar systems. The recurring framing is "the right data to the right people at the right time," which the handbook ties directly to risk reduction.

Crucially, the chapter source frames data definition as a *contractual and governance* concern, not merely a tooling concern. The mechanism that carries it is the program Data Requirements Description (DRD): nearly every element discussed — MBSE artifacts, CAD data, PMI, M&S credibility, configuration management, release states, parts libraries — must be defined and bounded in the DRD so that every party (NASA Centers, primes, partners, suppliers) shares one consistent definition and follows NASA policy and standards. The management of technical models is not optional: it is required by NPR 7123.1, which mandates that digital data be captured, stored, version-controlled, integrity-maintained, and disseminated in a way that satisfies contracted requirements.

The chapter therefore answers two linked questions: (1) what are the distinct categories of model-based data that an MBE acquisition has to define and govern, and (2) what must the DRD say about each so that data released in one place means the same thing everywhere it is consumed.

> **Caveat (honor this):** This handbook pairs with NASA-HDBK-1009A. NASA-HDBK-1004 sets the data-definition and acquisition framing; the companion handbook carries the complementary detail. Treat claims here as the acquisition/data-definition view and consult NASA-HDBK-1009A for the matching practitioner depth.

## Frameworks Introduced (exact source names, when/how)

The source names a specific set of frameworks, standards, and reference documents. Each is listed below with how the handbook invokes it.

- **Model-Based Enterprise (MBE)** — the overarching paradigm. Model-based data definition is positioned as one of MBE's essential constituent elements, and a fully digital MBE environment is described as necessary to comply with program requirements.
- **Model-Based Systems Engineering (MBSE)** — named explicitly as "the systems engineering subset of MBE." Introduced in section C.3 as the method that drives system models representing functions, requirements, and conceptual systems across the life cycle.
- **NPR 7123.1** — cited as the authority requiring management of technical data (models), and as the basis on which program/project requirements are defined and documented in the Systems Engineering Management Plan (SEMP).
- **SysML™** — named as the modeling language in which the analytical system model output of MBSE is sometimes developed; also reappears as an example engineering data object needing special handling under release/change management (C.13).
- **NASA-STD-7009** (the Agency standard for models and simulations) and **NASA-HDBK-7009** (its companion handbook) — invoked in C.7 (M&S) as the governing references for establishing the credibility of modeling and simulation results.
- **LOTAR (Long Term Archiving and Retrieval)** — named in C.9 as the aerospace-industry activity addressing archiving of data for long life-cycle programs, used to justify storing engineering data in IT-independent, long-readable formats.
- **SAE EIA-649-2** — cited in C.11 as the configuration-management reference describing how product data is to be released.
- **NPR 1441.1, NASA Records Management Program Requirements** — referenced in C.11 as the basis for preserving and retiring product records across the life cycle.
- **MIL-STD-31000** — named in C.13 as an example standard to be invoked via the contract's SOW/PWS and the DRDs when mapping supplier release states to program states.
- **Data Requirements Description (DRD)** — not a standard but the central governing artifact: the document in which the meaning, scope, and handling of every MB(x) data category must be fixed.
- **MBE Plan** — the program-level plan in which product structure, release rules, life-cycle states, and source-to-destination state mappings are documented.
- **Appendix D (MB(x) definitions), Appendix F (CAD conversion standard), Appendix G (use cases), Appendix A** — internal handbook cross-references for the broader MB(x) taxonomy, data-conversion standards, interoperability use cases, and contractual examples.
- **NIST** — named (alongside NASA and commercial partners) as a source whose definitions the handbook draws on to establish a common baseline of MBE terminology.

## Key Concepts

**The MB(x) family.** MBE is explicitly broader than CAD. The handbook situates model-based data definition as the underlying architecture that ties data and processes together and supports MBE elements including MBSE, model-based manufacturing (MBM), and model-based inspection (MBI) — the latter using CAD to drive coordinate-measuring-machine (CMM) inspections. The DRD's data definition is therefore not restricted to CAD models and may include many of the MB(x) definitions catalogued in Appendix D.

**System model as the center of MBSE.** In MBSE the system model sits at the center of development, from requirements through design, implementation, and test. The handbook describes the model as a specification that is continually refined, with simulation used afterward to confirm the model behaves correctly. MBSE is expected to extend into adjacent domains — integrating engineering models with scientific/phenomenology, social/economic/political, and human-behavioral models for predictive, effects-based analysis. A single-source interconnection model lets reviews be conducted across discipline-dependent views (CAD, digital manufacturing, as-built, model-based testing, logistics), enabling concurrent engineering.

**Requirements in a model-based environment (C.4).** Program scale influences the MBE solution but does not by itself dictate the requirements for managing product data; the handbook lists mission nature, mission class, data volume/type, sensitivity, retention, and access timing/location as the real drivers. Requirements live in the DRD and must be allocatable to organizations, related to other MBE information, structured into parent/child derivation, linked to authoritative sources, enriched with attributes (margins, technology readiness levels, risks, cost), and bidirectionally traceable to source and to V&V. They are managed across the whole life cycle, with tooling expected to auto-notify on changes and flow-down impacts.

**CAD data management (C.5).** Covers MCAD, ECAD, CAE, and CAM. Effective management requires defining the relationships among all associated parts and assemblies, capturing models in a virtual/accessible database, supporting structured check-in/checkout and revision control, and enabling workflow with automatic notification. The handbook is candid about the problems that motivate this discipline (see Anti-patterns).

**PMI and the Digital Mock-Up (C.6).** Part Manufacturing Information and mechanical/design-for-manufacturing instructions must be checked for content, context, and maturity — geometry, dimensions, interference, and collision checks for assembly/disassembly, plus design-space checks. Geometry, product structure, and metadata are analyzed in a DMU application, but results are captured in the model data definition. The handbook distinguishes static DMU (examining static parts) from dynamic DMU (examining moving parts/assemblies). A key technical rule: a simplified, tessellated envelope representation usually suffices for DMU, but for measurements the tessellation accuracy must always exceed the required measuring accuracy. Visualization conveys design intent and form/fit, but the information that drives manufacturing must be tracked and called out as a critical-path item in the DRD, ultimately feeding a Technical Data Package (TDP) from which others can derive design intent.

**M&S credibility (C.7).** Simulation outputs are described as data used daily for critical decisions across design, manufacturing, and operations. The program/project manager and delegated Technical Authority(s) own responsibility for the credibility of M&S results, governed by NASA-STD-7009 and NASA-HDBK-7009. Confidence is built through bounded user interfaces, formal verification/validation/certification (and re-verification/revalidation/recertification on operational trending), documentation and quality-assurance standards, training/certification, obsolescence planning, user-feedback processes for implausible results, and a standard method for assessing credibility when results affect human safety or mission success.

**Documents vs. authoritative models (C.8).** Prose documents (specs, policies, test results) remain an important communication medium across diverse engineering and business audiences, but the handbook describes MBE as evolving so that the *models* are the authoritative source and documents become a derived communication method produced from them.

**Documentation and archiving (C.9).** Archiving must factor in exact data representation including all metadata and PMI. The governing requirement is that information be stored in a format readable independent of any specific IT infrastructure and over long time spans — the motivation behind invoking LOTAR. This matters especially when digital 3D models replace drawings for product approval and compliance.

**Portable PLM document (C.10).** Modern (concurrent/integrated) product development means 3D information must reach purchasing, QA, technical documentation, configuration management, planning, manufacturing, operations, maintenance, and sustaining functions. The handbook calls for combining 3D data, metadata (e.g., 2D representations), text, and binary data into a single multimedia container — usable offline, combinable across source systems, IP-access-controlled, and viewable through easy cross-system viewers. The DRD owns this responsibility.

**Configuration and Data Management (C.11).** CDM provides the structured framework for controlling requirements and engineering products and for reconciling accountability across multiple bills of material and restructuring use cases (BOM splits, merges, substitutes, change propagation). It addresses functional/performance characteristics; functional, allocated, and product baselines; design-through-disposal requirements; compliance verification; traceability of waivers/deviations/non-compliances; record retention and integrity; and the CM level supported by each organization. Program-level CDM flows down to multi-tier suppliers; SAE EIA-649-2 governs release, and NPR 1441.1 governs record preservation/retirement. The PM and Technical Authority define in the MBE Plan what product data is released, when, what triggers change, and how configuration visibility is maintained.

**BOM and product breakdown structure (C.12).** A product breakdown structure is a hierarchical view decomposing product functionality into functions, the parts that deliver them, and the interfaces between them. A BOM is a functionally dependent subset listing physical items with name, reference number, quantity, and unit of measure. The handbook requires traceable documentation of every BOM change (when, why, by which document, approved by whom, and disposition of affected items) and the ability to manage multiple BOM views — as-designed (EBOM), as-built/as-manufactured (MBOM), as-manifested, as-flown, as-disposed — with effectivity by event, date, lot, or serial number. A good product structure supports drill-down from system to piece-part and walk-up from part to system, reaching analysis reports, test reports, requirements, and V&V checklists, all under access privileges. The component taxonomy runs System → Segment → Element → Subsystem → Assembly → Subassembly → Part.

**Engineering release and change management (C.13).** The change process must be a multi-level-supplier, closed-loop flow with changes automatically integrated, routed, and closed, with impacts visible and history maintained. "Release" (as a verb) means authorizing dissemination of a particular version for a specific purpose, and its meaning shifts across life-cycle phases. A data object is defined by itself, its metadata (including effectivity), and its state ("in work," "under review," "released"). Critically, object type alone does not determine usage — the same CAD model can be released as a manufacturing-definition model or for outer-mold-line development, so process depends on object *type* and *intended use*, not phase alone. The handbook's governing principle: data in a given state must mean the same thing to everyone, which drives the need to map supplier release states to defined program states (Figure 2, Notional State Compatibility Map) using the MBE Plan, the contract SOW/PWS, and standards such as MIL-STD-31000. System synchronization — gathering a defined set of configurations together so a whole-system test can be run at chosen points in the life cycle — enables early integration testing and early trade investigation.

**Parts and library management (C.14).** Parts data is distributed across Centers, primes, and functional areas, so how parts are identified, defined, categorized, and authorized — and how CAD data objects are handled — must be defined in the DRD. Multiple libraries can coexist (part-definition, M&S, CAD), maintained across organizational boundaries. A CAD parts library in an MBE environment must accommodate multiple common-parts libraries with disciplined naming, let a developer check whether a part already exists in a common library, govern acceptance of individual and wholesale part definitions, secure proprietary/IP/SBU parts, support audit/compliance of naming and CDM/data-architecture rules, and handle external organizations verifying part-name uniqueness before entry. The DRD describes how CAD standards apply over the life cycle and what additional deliverables (parts lists, materials specs, acceptance-test specs) the CAD producer must supply for full product-data definition.

**Technology and openness (C.15).** MBE solutions should use open architectures supporting standards-defined interoperability. Architecture needs a common data-hierarchy definition with top-down/bottom-up links consistent across all participants. MBE technology is often procured as a single integrated vendor suite (databases, custom software, COTS interfaces, report writers, utilities, configuration/audit files), but the handbook is explicit that no single tool covers the heterogeneous needs of NASA programs — so openness and standards-defined interoperability are named as a key critical success factor.

## Mental Models

- **DRD as the contract for meaning.** The DRD is the single place where the *meaning* of each data category is fixed before it is exchanged. If a data type is not pinned down in the DRD, it cannot be trusted across organizational boundaries. Treat the DRD as the schema for cross-enterprise data semantics.

- **State, not just artifact.** A deliverable is never just a file; it is {object + metadata + state + effectivity + authorized usage}. The same CAD model is a different *thing* depending on whether it is "released for manufacturing" or "released for prototyping." Reason about objects as state machines, not as static documents.

- **State-compatibility mapping (the lingua-franca problem).** Different parties legitimately use different release vocabularies — one supplier's "manufacturing release," one Center's "final release," another's "engineering release." Rather than forcing one vocabulary, the handbook's model is to *map* each source state to a program-defined destination state (e.g., "production release") so the differences become inconsequential. Build a translation table, don't mandate uniformity.

- **Models are authoritative; documents are views.** Flip the traditional hierarchy: the model is the source of truth and the prose document is a generated communication artifact. When the two disagree, the model wins.

- **Tessellation must out-resolve the measurement.** A small but sharp engineering invariant: simplified geometry is fine for visualization and clash checks, but any geometry used for measurement must be tessellated more accurately than the measurement it supports.

- **Right data, right people, right time = risk reduction.** Treat data availability as a mission-assurance lever. The point of all this governance is not tidiness; it is to lower mission risk by ensuring decisions are made on the latest, common, authoritative data.

- **Openness over single-vendor completeness.** No single integrated suite can cover a heterogeneous NASA program. Evaluate MBE tooling primarily on the openness of its interfaces and standards-defined interoperability, not on feature breadth.

## Anti-patterns

The source explicitly enumerates problems that motivate its guidance. These are named in the text, not inferred.

**CAD data management problems (C.5):**
- Incomplete information forcing iteration because not all CAD objects arrive with their data packages.
- CAD naming conflicts — multiple names for the same part.
- Change management gaps — no governance/approval, names changing with no way to confirm geometry is identical.
- Broken CAD links when files are moved manually, losing traceability.
- Inconsistent version/revision control and inconsistent modeling standards.
- No design intent captured or shared.

**BOM development and use problems (C.12):**
- Only the "as-designed" BOM is managed in engineering.
- The proposal BOM is created and then not carried forward.
- Not all delivered data relates to part definition; no product structure delivered.
- Effectivity limited to a single change and by date only, retaining only the most recent.
- Substitutes and alternatives managed as separate BOMs/products rather than as variants.

**Parts/library problems (C.14):**
- Part numbers existing without exact specifications, or too similar to another component's number, forcing costly reconciliation at critical points.
- Part-number proliferation causing confusion and duplication of effort and inventory cost.

## Key Takeaways

- Model-based data definition is one of MBE's essential constituent elements; its job is mission-success probability via better data availability, integrity, fidelity, and efficiency — explicitly framed as risk reduction.
- Management of technical models is required by NPR 7123.1; it is not discretionary.
- The DRD is the central governing artifact: the meaning, scope, and handling of every MB(x) category must be fixed there so all parties share one definition.
- MBE is broader than CAD — it spans MBSE, MBM, MBI, M&S, documents, archiving, PLM, CDM, BOM, release/change, and parts libraries (the MB(x) family in Appendix D).
- MBSE is the systems-engineering subset of MBE, with the continually-refined system model at the center and SysML™ as a common (not mandatory) language.
- M&S credibility is owned by the PM and Technical Authority and governed by NASA-STD-7009 / NASA-HDBK-7009.
- A deliverable's truth is its {object + metadata + state + effectivity + authorized usage}; object type alone never determines usage.
- Cross-organization interoperability is solved by mapping source release states to program-defined destination states (Notional State Compatibility Map), backed by the MBE Plan, SOW/PWS, and standards like MIL-STD-31000.
- Configuration and records governance leans on SAE EIA-649-2 (release) and NPR 1441.1 (record retention); archiving leans on IT-independent, long-readable formats (LOTAR).
- Openness and standards-defined interoperability are a key critical success factor — no single vendor suite covers a heterogeneous NASA program.

## Connects To

- **NASA-HDBK-1009A** — the companion handbook this pack is paired with; consult it for the practitioner-depth counterpart to this acquisition/data-definition framing.
- **NPR 7123.1 (NASA Systems Engineering Processes and Requirements)** — mandates technical-data management and anchors requirements documentation in the SEMP; the backbone the MBSE/requirements material (C.3–C.4) sits on.
- **NASA-STD-7009 / NASA-HDBK-7009 (Models and Simulations)** — the credibility regime for the M&S category (C.7).
- **SAE EIA-649-2 and NPR 1441.1** — configuration management release rules and records-management requirements underpinning CDM (C.11).
- **MIL-STD-31000 and the contract SOW/PWS/DRD** — the contractual machinery for state mapping and supplier flow-down (C.13); connects model-based data definition to the broader acquisition and TDP standards landscape.
- **LOTAR** — long-term archiving for long-life programs (C.9), relevant wherever digital 3D models supersede drawings of record.
- **SysML and MBSE tooling** — the analytical-model leg (C.3), linking this pack to the wider MBSE/standards body and to engineering data objects requiring special release handling.
- **Appendices D, F, G, A of NASA-HDBK-1004** — the MB(x) taxonomy, CAD-conversion standard, interoperability use cases, and contractual examples that extend the categories summarized here.

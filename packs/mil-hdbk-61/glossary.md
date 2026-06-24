# Glossary — MIL-HDBK-61B Configuration Management

Key CM terms used across this pack, alphabetical. Each entry gives the working
definition and the chapter(s) where it is developed. Terms follow MIL-HDBK-61B
and the EIA-649 suite it adopts; expect industry aliases (the source itself
declines to enforce one canonical vocabulary).

| Term | Definition | Chapters |
|---|---|---|
| **AA — Application Activity** | A configuration control authority whose reach is limited to *using* a product and its documentation, not changing it. May participate in a change when invited but never authorizes it. | ch04 |
| **ABL — Allocated Baseline** | The baseline capturing the performance-oriented functional and interface characteristics allocated down to a CI from a higher level, plus its verification; documented in development specifications (ACD). Control may rest with Government or contractor. | ch01, ch02, ch03 |
| **ACD — Allocated Configuration Documentation** | The technical documentation set underpinning the Allocated Baseline. Second in the FCD→ACD→PCD order of precedence. | ch03 |
| **Acquisition phases (MSA/TMRR/EMD/P&D/O&S)** | The DoD life-cycle bands CM is tailored to: Material Solution Analysis, Technology Maturation & Risk Reduction, Engineering & Manufacturing Development, Production & Deployment, Operations & Support. | ch02, ch08 |
| **APB — Acquisition Program Baseline** | The program cost/schedule/performance baseline established at Milestones A, B, and C (DoDI 5000.2); its performance thresholds flow into the FBL specification. | ch03 |
| **As-built / as-delivered / as-designed / as-maintained** | Configuration *views* CSA must be able to render — currently and as of any prior date — for a given serial-numbered unit. Digital twins newly require as-built and as-maintained capture. | ch05, ch07 |
| **Baseline** | An agreed, formally recorded description of a product's attributes at a point in time, serving as the reference for managing change. The three Government baselines are FBL, ABL, PBL. | ch01, ch02, ch03 |
| **CAGE code** | Commercial And Government Entity code; one element of the document identity triad (CAGE code + document type + document identifier) and of item part numbers. | ch03 |
| **CCB — Configuration Control Board** | The chartered body that dispositions Class I ECPs and major/critical variances; the PM owns CCB disposition. Its decision is issued as a CCBD. Contractors run a parallel internal board. | ch01, ch04 |
| **CCBD — CCB Directive** | The directive (or equivalent letter/memorandum) the CCB chairperson issues to direct the implementing actions of an approved change. | ch01, ch04 |
| **CDCA — Current Document Change Authority** | The single organization (Government or contractor) holding decision authority over a document's content; exactly one per document at a time, though the role can transfer. | ch01, ch04 |
| **CDRL — Contract Data Requirements List** | The contractual mechanism (DD Form 1423) for ordering data deliverables; ideally one line per data item, each tied to a DID and SOW task. | ch04, ch07 |
| **Change classification (Class I / Class II)** | Class I (Major) changes affect approved functional/allocated/product requirements (or cost, warranties, contract milestones) and go to the CCB; Class II (Minor) is any approved-documentation change that is not Class I. | ch01, ch02, ch04 |
| **CI — Configuration Item** | The unit of CM: an aggregation of hardware, software, or both, designated for CM and managed as a single entity that satisfies an end-use function. HWCI / CSCI are the hardware / software specializations. | ch01, ch03 |
| **CM — Configuration Management** | The management process for establishing and maintaining consistency between a product's performance, functional, and physical attributes and its requirements, design, and operational information across its life. | ch01, ch02 |
| **CMP — CM Plan** | The plan documenting the program's CM concept of operation and process, developed in the planning band and revised each phase to match the coming phase's CM tasking. | ch02, ch08 |
| **Configuration** | The collection of an item's descriptive and governing characteristics, expressible in functional terms (what it must do) and physical terms (what it is). | ch01 |
| **CSA — Configuration Status Accounting** | The function that creates and organizes the configuration knowledge base and supplies reliable configuration information to the whole program; accumulates as a by-product of CM transactions. | ch02, ch05 |
| **CSCI — Computer Software Configuration Item** | A CI that is software; software items are almost always CIs because they typically control system functionality. | ch01, ch03 |
| **DCMA — Defense Contract Management Agency** | The contract-administration agency that typically adjudicates/concurs in Class II changes and minor variances and participates as a full CM team member. | ch02, ch08 |
| **Defect** | Any nonconformance of a characteristic. | ch01 |
| **Developmental configuration** | The contractor's evolving, internally-released and contractor-controlled design and technical data defining the design solution before it is baselined as a PBL. | ch03 |
| **DID — Data Item Description** | The standardized description of a data deliverable's content/format, ordered via a CDRL; existing DIDs live in the ASSIST system. | ch07 |
| **Digital artifact / digital engineering / digital twin** | 61B's digital-era terms: a digital artifact is any digital item forming part of a system's digital representation; a digital twin is an integrated, probabilistic simulation that mirrors and predicts an as-built physical instance over life. | ch01, ch07 |
| **DM — Data Management** | The discipline governing the full life cycle of *all* product-related data — what to acquire, the rights to use it, and how to store and share it. CM controls the configuration-defining subset; DM provides the data CM assumes. | ch07 |
| **ECP — Engineering Change Proposal** | The formal vehicle for a requested change (DD Form 1692), typed Class I or Class II when submitted to the Government. | ch01, ch04 |
| **Effectivity** | The range (e.g., serial-number range) over which an approved change applies; tracked in CSA across all copies and locations. | ch04, ch05 |
| **FBL — Functional Baseline** | The baseline capturing top-level system performance, interoperability, and interface characteristics plus verification; established when the FCD is Government-approved; always under Government control. | ch01, ch02, ch03 |
| **FCA — Functional Configuration Audit** | The performance audit verifying that a CI's actual performance meets its performance specification. | ch01, ch06 |
| **FCD — Functional Configuration Documentation** | The documentation set underpinning the Functional Baseline; first in the FCD→ACD→PCD order of precedence. | ch03 |
| **Form, fit, function (FFF)** | Form = physical envelope; fit = ability to interface/interconnect; function = the action an item performs. FFF data carries unlimited Government rights automatically. | ch01, ch07 |
| **ICWG — Interface Control Working Group** | A specialized IPT for resolving interface issues that engineer-to-engineer interaction cannot settle. | ch01, ch03 |
| **Interchangeable / replacement item** | An interchangeable item is functionally and physically equivalent and substitutes without selection or alteration; a replacement item is interchangeable but needs extra operations (drilling, reaming, shimming) to install. | ch01 |
| **Interface** | The set of characteristics required at a common boundary between systems, managed through interface control (and, where warranted, an ICWG). | ch01, ch03 |
| **MOSA — Modular Open Systems Approach** | An integrated business-and-technical strategy using modular design and consensus-based, verifiable interface standards for competitive, affordable acquisition and sustainment. | ch01, ch07 |
| **Master / authoritative source** | The single designated instance of data placed under configuration control; derived and transformed copies must be kept in sync with it. | ch07 |
| **NOR — Notice of Revision** | The ancillary document to an ECP that conveys the specific edits to a specific affected document; optional for documents the ECP originator controls. | ch01, ch04 |
| **Nonconformance** | A unit's failure to meet a specified requirement. | ch01 |
| **OMIT data** | Operation, Maintenance, Installation, or Training data; like FFF data, carries unlimited Government rights automatically. | ch07 |
| **PBL — Product Baseline** | The baseline completely describing the functional and physical characteristics for production, deployment, and re-procurement; initial PBL set per CI at CDR, finalized and validated at PCA. | ch01, ch02, ch03 |
| **PCA — Physical Configuration Audit** | The design audit examining a representative production CI to verify the design documentation matches the delivered design and to validate production processes; locks down the PBL. | ch01, ch06 |
| **PCD — Product Configuration Documentation** | The documentation set underpinning the Product Baseline; last in the FCD→ACD→PCD order of precedence. | ch03 |
| **PDM — Product Data Management system** | A Government-operated IT system with CM functionality used to store and manage received data; the recommended home for the official master copy. | ch07 |
| **Performing / tasking activity** | The tasking activity (buyer) imposes requirements via contract/tasking directive; the performing activity (seller — contractor or Government) executes them. | ch01 |
| **Repair / rework** | Rework fully eliminates a nonconformance (restoring full conformance); repair only reduces it (the characteristic still does not fully conform). | ch01 |
| **Retrofit** | Incorporation of approved new design or software code into already-delivered, accepted products, guided by a retrofit instruction. | ch01, ch06 |
| **RFV — Request for Variance** | The mechanism for delivering/installing an item that does not (or will not) conform to baselined documentation; classified minor/major/critical. Previously termed deviation or waiver. Approval is an inherently Governmental, non-delegable function. | ch01, ch04 |
| **Rights (unlimited / Government purpose / limited / restricted)** | The data-rights ladder: FFF and OMIT data are unlimited automatically; otherwise the funding source sets the default — unlimited (100% Government), Government purpose (mixed), limited/restricted (private). | ch07 |
| **SAE EIA-649 / EIA-649-1 / GEIA-HB-649** | The adopted commercial CM standard suite: EIA-649 states CM principles; EIA-649-1 is the defense-contract requirements companion (tailored onto contracts); GEIA-HB-649 is the implementation guide. The configuration manager's working toolkit. | ch01, ch02, ch03, ch08 |
| **Serial / lot / part number** | A serial number uniquely identifies an individual unit and persists across its life; a lot/date code identifies a series of like units; a part number changes whenever a non-interchangeable condition is created. | ch03 |
| **Tailoring (R / T / NR)** | Selecting and scaling CM requirements per phase via EIA-649-1 Annex A and the Figure B-1 matrix, where each cell is Recommended, Tailorable, or Not Recommended. | ch08 |
| **Viewpoint** | In a digital/model-based environment, the location of data in a model used to produce an artifact (in SysML, the data in a given diagram); requires CM controls to preserve dataset continuity. | ch07 |

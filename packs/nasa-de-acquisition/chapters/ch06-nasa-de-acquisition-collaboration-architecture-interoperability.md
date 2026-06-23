# Chapter — Digital Data Collaboration, Architecture, and Interoperability Standards

> Caveat: This pack is built on NASA-HDBK-1004 and pairs with NASA-HDBK-1009A. Where 1004 sets the acquisition and architecture framing for model-based collaboration, 1009A carries the complementary digital-engineering detail; treat the two as companion references.

## Core Idea

Appendices D, E, and F of NASA-HDBK-1004 argue that simply digitizing deliverables does not deliver interoperable data. Across all life-cycle phases, data crosses many entities that change over time, the design environment keeps shifting toward a models-based approach, and the engineering and acquisition processes have become more automated and more dependent on a collaborative, socially connected workforce. The handbook's position is that real interoperability is achieved only by pairing the right IT standards with contractual mechanisms that force their implementation. Storing raw, uncorrelated data — or scanned documents and non-machine-readable PDFs in a file system — falls short, because page-formatted deliveries strip away the context that makes a digital asset useful downstream. The chapter's three appendices supply the contractual framing (D), the architectural framing (E), and the standards framing (F) that together let NASA, its contractors, and partners move past document-centric exchange toward a single authoritative source of product definition.

## Frameworks Introduced (exact source names, when/how)

The slice names a specific set of standards, models, and named constructs. Each is given with how the handbook uses it.

- **MBx family (MBSE, MBD, MBE, MBe, MBM, MBI)** — Appendix D §D.2 defines the "model-based x" artifacts whose integrity must be protected during data acquisition. The breakdown distinguishes model-based systems engineering (logical, functional, behavioral models leading to schematics, analyses, CAD), model-based definition (annotated 3D CAD capturing GD&T and PMI), the model-based enterprise (an organization that uses model-based engineering), model-based engineering itself (a digital-model-driven approach across development, design, manufacturing, and life-cycle support), model-based manufacturing and assembly (as-designed/as-built), and model-based inspection (assurance that realized products meet defined maturity and content levels using their product manufacturing information).
- **DRD (Data Requirements Description)** — invoked throughout D as the contractual instrument. An established data definition framework is captured and reported in the DRD; DRDs in Appendix A are offered as a starting point for Centers to define their specific needs. DRD clauses become the lever for governance, KDP-deliverable definition, and enforcing data depth, detail, and exchange integrity.
- **NPR 2810.1** — cited as the policy that defines the data's security requirements, governing how all program/project digital data (PDD) is captured in a secure environment regardless of digital or hardcopy form.
- **NIMA-RPT-004, *Future Data Exchange for NASA Programs*** — referenced as the source for the finding that manual replication of data between applications can create discrepancies in roughly 40 percent of transferred records, and again as guidance on selecting a neutral 3D format for collaboration.
- **MIL-STD-31000B, Technical Data Packages** — §D.3 draws its definitions of three-dimensional intelligent (3Di) technical data, the 3Di format, and Type 3D TDPs (3D native models, derived 2D drawings, derived 3Di PDF viewable data, and derived neutral files such as JT or STEP) from this standard.
- **ISO 32000-1 (PDF 1.7)** — named as an example of a widely available software format for a 3Di viewable representation.
- **ISO 10303-242 (STEP AP242)** — §D.3 describes it as the merging of the aerospace protocol STEP ISO 10303-203 (which handles configuration-managed 3D mechanical part and assembly design) with the automotive protocol STEP ISO 10303-214 (core automotive mechanical-design data), supporting managed model-based 3D engineering.
- **NPR 7123.1** — cited as defining the engineering-release model that MBE can frame, ensuring the right data is available at the right time.
- **NPR 7120.5** — referenced both as the life-cycle authority (KDPs Pre-Phase A through Phase F) the MBE Plan must align to, and as the policy whose compliance is verified by submission of the initial preliminary MBE Plan.
- **MBE Plan** — §D.6 establishes it (with Appendix J guidance) as the document recording the foundation for data-investment decisions; the program/project managers and delegated Technical Authorities sign and release it before the System Definition Review (SDR).
- **Model-Driven Architecture (MDA)** — §E.2 attributes MDA to the OMG initiative, leveraged by Meta-Object Facility, XMI, Common Warehouse Metamodel (CWM), CORBA, and UML, with an earlier approach relying on Executable UML, Object Constraint Language (OCL), and query/view/transformation (QVT).
- **Eclipse Modeling Framework** — §E.2 names it as the general-terms representation of MDA's ecosystem of programming and modeling tools, usable to build tools implementing OMG's MDA standards.
- **Four architecture types** — §E.2/E.3 defines the Agency-level collaborative environment as four architectures: Security, Information Support System (ISSA), Data, and Process. Each gets its own subsection (E.3.1–E.3.4) with ownership assignments.
- **ISO/IEC/IEEE 42010** — cited as the architecture-description standard that the Goddard Space Mission Architecture Framework follows.
- **Goddard Space Mission Architecture Framework (GSMAF)** — §E.3 introduces it as a viewpoint-structured framework (Science, Systems Engineering with Requirements/Product Design/Realization, Management with Project Development/Operations, and Enterprise) following ISO/IEC/IEEE 42010 plus NPR 7120.5 and NPR 7123.1, addressing Goddard science-mission stakeholders.
- **NPR 2800.1, Managing Information Technology** — §E.3.1/E.3.2 names it (with NPR 2810.1) as the basis for the Agency CIO's Security Architecture and ISSA responsibilities.
- **NASA-STD-7009, Standard for Models and Simulations** — §F.1 cites it for the requirements that govern how the credibility and integrity of model-based results, and the way a model is applied, get determined.
- **Table 5 (System and CAD Model Interoperability Insights)** — §F.2 maps engineering intents (design integration, subcontracting, taking over change authority, design review, derivative designs, modeling and simulation, re-bidding production, physical integration, acceptance-package definition, concept development) to the model-based definition needed to support each.
- **Table 6 (Target Industry Standards for Data Interoperability Formats)** — §F.6 lists XML 1.1, Namespaces in XML 1.1, XML Schema Definition (XSD) 1.1, XML Metadata Interchange (XMI) 2.1/2.1.1, and the STEP Application Protocols (ISO 10303) as the W3C/OMG/ISO standards underpinning interoperability, with XML-based formats keyed to maturity level 3.
- **Supporting standards in the Table 6 notes** — SGML (ISO 8879), XMI (ISO/IEC 19503), UML (ISO/IEC 19501), MOF (ISO/IEC 19502), and STEP APs such as Parts 209, 210, 233, 238, 239, and 242, plus URI references (RFC 3986/STD 66).
- **Table 7 (Common Problems Related to Interoperability)** — §F.7 catalogs recurring failure modes across requirements, modeling and simulation results, CAD, product definition, part identification and naming, model definition, common-hardware handling, product life cycle, and product structures, flagging which problems rely on more than one standard.

## Key Concepts

**Three guarantees of a captured data-definition framework.** §D.2 ties the DRD-reported framework to three outcomes: Security (all PDD captured in an environment meeting its security requirements per NPR 2810.1), Product Data Integrity (a single source of product definition with managed relationships among associated documents), and Automation (workflow and automatic-notification capabilities). The framework also makes CAD part numbers searchable by attribute and metadata and controls data per contract and sensitivity.

**Digitization is necessary but not sufficient.** §D.3 is explicit that exchanging digitized data does not by itself solve interoperability. Even system-to-system replication fails without a computer-readable format that preserves referential integrity — the 40-percent manual-discrepancy figure from NIMA-RPT-004 is the evidence offered for why standardization is the affordable and sustainable path.

**Three MBE process domains needing initial focus.** §D.3 identifies data collaboration (defining and managing models, requirements, CAD parts and libraries through DDT&E), engineering release (the start of design-data configuration and data management, where designs are created, checked, and status-reported), and integrated product structure (the core mechanism defining relationships among detail design elements). These are implemented concurrently, authorized through NPRs and standards, and used by trained, supported end users.

**Guiding principles for data collaboration.** §D.3 lists principles centered on making data visible, accessible, and understandable as early as possible: tagging assets with discovery metadata, complying with national and international consensus metadata standards, sharing data in accessible spaces except where law/policy/classification restricts, attaching information-assurance and security metadata with a named authoritative source, promoting semantic and structural agreements through communities of producers and consumers, and acquiring only the minimum essential contractor-originated data needed for the full life cycle.

**Four architecture types and their owners.** §E.3 assigns clear ownership. The Agency CIO develops the Security Architecture (per NPR 2800.1 and NPR 2810.1) and the ISSA (which aggregates product/process information from diverse authoring applications using open APIs and enterprise service buses). The CIO provides infrastructure for the Data Architecture while engineering defines what data it must support; program/project managers and delegated Technical Authorities ensure the Data Architecture meets program needs and is documented in the MBE Plan. The Process Architecture — describing business-process flow, data-handling roles, and approval authority — is defined by the program/project manager and delegated Technical Authority and implemented by the CIO and Mission Directorate.

**Four themes that make or break collaboration.** §D.5 names integrity of the data (latest, complete, and consistent from the onset, with DRDs defining depth and exchange method), virtual access anytime/anywhere (global push-and-pull sharing with security and supply-chain enablement, available around the clock), discipline in integrated-product-definition-driven development (scalable, enforced configuration and change management stemming from the product structure), and visualization (lightweight, intelligent software capable of total product representation for form-and-fit decisions).

**Desired data end states.** §D.5 converts the collaboration vision into specific objectives: pre-release data sharing (sharing engineering data with other groups and primes before formal release, including the horizontal and diagonal CAD flows that simple vertical movement does not support), distributed non-document-centric authority (the electronic version must be authoritative, and authority increases non-linearly down the product hierarchy), process/tool/use synchronization (workflows deliver value only when actually used), handling data objects (rethinking what it means to deliver, receive, release, and configuration-control large active data entities that do not behave like PDFs), having a voice (governance recognizing different users' needs to be heard at different times), and data usability and collaboration (deploying capability mapped to user communities, supported by new DRD-clause practices).

**Standards keyed to a maturity model.** §F.6 explicitly ties the Table 6 W3C-based formats to maturity level 3 in Table 8, signaling that standard selection is meant to track an organization's solution maturity rather than being applied uniformly.

**Neutral formats as the collaboration medium.** §F.3 observes that CAD systems are all moving to 3D digital formats as their authoritative source, but not all participants use the same CAD system; when sharing is needed, a neutral 3D format is required, and (per NIMA-RPT-004) a neutral 3D format should generally be selected as the medium.

## Mental Models

**Standards plus contracts, not standards alone.** The handbook repeatedly couples technical standards with contract language. Proper interoperability is achieved through identifying IT standards *and* applying contractual methods (the DRD clause) to force implementation. Picking a format is half the job; the other half is writing it into the deliverable definition.

**Data as an enabler, surfaced early.** The collaboration principles frame data as an essential enabler to be made visible, accessible, and understandable as early in the life cycle as security and access allow — the inverse of treating data as a back-loaded deliverable produced at milestones.

**Authority lives in the model, not the document.** Distributed non-document-centric authority means the electronic version must be authoritative. The mental shift is away from PDFs and drawings as the record toward live, configuration-controlled data objects that are still being defined.

**Architecture as four interlocking layers.** Security, ISSA, Data, and Process are not alternatives but concurrent layers of one Agency-level collaborative environment, each with a named owner, so that every team member understands which data are authoritative and how data become authoritative through release.

**Plan for the anomaly a decade out.** §D.6 frames the core management trade as: how much should the program risk or pay to ensure relevant data remain accessible, discoverable, and understandable to support an in-flight anomaly ten or more years in the future, and where should limited attention and resources be invested during development.

**Intent drives data need.** Table 5 inverts the usual order: start from the engineering intent (design integration, review, simulation, integration, acceptance) and let that intent define which model-based annotations, maturity level, and content are actually required — so native data does not carry baggage the recipient will never use.

## Anti-patterns

The source names these failure modes directly.

- **Document-centric, non-machine-readable delivery.** §D.3 identifies the dominant historical pattern — digital scans and non-machine-readable (scanned/raster) PDFs stored in a file or content-management system — as falling short because page-formatted documents lack the context needed to leverage digital assets.
- **Manual replication between applications.** §D.3 cites NIMA-RPT-004's finding that manually replicating data from one application to another typically introduces discrepancies in about 40 percent of transferred data.
- **Ad hoc sharing without effective collaboration.** §D.5 describes non-co-located teams forced to share via e-mail, zip files, and shared servers, using multiple tools that can corrupt native format or transfer insufficient product information, while perpetually hunting for the latest version of record.
- **Native data carrying unnecessary baggage.** §D.5 flags scalability and usability problems where blurred definition of the model's needed attributes means very large native data carries content the recipient will never use.
- **No Data Architecture from the start.** §E.3.3 warns that if the Data Architecture is not stood up at the outset, a program/project's data quickly falls into disarray and, as the volume climbs, grows almost impossible to integrate or discover electronically.
- **Recurring interoperability problems (Table 7).** §F.7 enumerates concrete failure modes: rework from incompatible requirements or CAD settings, CAD file-name conflicts when combining data from multiple sources, error and confusion over nomenclature, and inability to trace a part's life-cycle status changes — with a flag that many of these rely on more than one standard to resolve.

## Key Takeaways

- Interoperability requires IT standards *and* contractual enforcement (DRD clauses); digitization without a referential-integrity-preserving, machine-readable format does not solve the problem.
- The MBx family (MBSE, MBD, MBE, MBe, MBM, MBI) defines the artifacts whose integrity must be protected, anchored to a DRD-reported data-definition framework that guarantees security, product-data integrity, and automation.
- MIL-STD-31000B (3Di technical data and Type 3D TDPs), ISO 10303-242/-203/-214, and NASA-STD-7009 supply the technical-data-package and credibility standards; Table 6's W3C/OMG/ISO formats (XML, Namespaces, XSD, XMI, STEP APs) provide the interoperability backbone, keyed to maturity level 3.
- The Agency-level collaborative environment is built as four owned architectures — Security and ISSA (CIO), Data (CIO infrastructure, engineering definition, PM/Technical-Authority sign-off), and Process (PM/Technical Authority definition, CIO/Mission-Directorate implementation).
- GSMAF, following ISO/IEC/IEEE 42010 with NPR 7120.5 and NPR 7123.1, demonstrates a viewpoint-based architecture framework (Science, Systems Engineering, Management, Enterprise) for science missions.
- The MBE Plan (per NPR 7120.5, Appendix J) records the data-investment decisions and is signed and released before SDR; it answers how much to risk on data accessibility for anomalies a decade out.
- Authority must live in authoritative electronic models, not documents; neutral 3D formats are the collaboration medium when participants use different CAD systems.

## Connects To

- **NASA-HDBK-1009A** — the companion digital-engineering reference this pack is paired with; 1004 supplies the acquisition, architecture, and standards framing here, while 1009A carries the deeper digital-engineering practice. Read the two together.
- **Earlier chapters of this pack (NASA-HDBK-1004)** — the DRD instrument, the MBE Plan, and KDP-aligned deliverables draw directly on the acquisition and configuration/data-management material covered elsewhere in the handbook.
- **NPR 7123.1 and NPR 7120.5** — the engineering and program-management life-cycle policies that the MBE Plan, engineering release, and GSMAF align to (Pre-Phase A through Phase F).
- **ISO 10303 / STEP ecosystem** — the AP242, AP203, and AP214 protocols connect this material to the broader MBSE and product-data-exchange standards landscape, and to neutral-format exchange (JT, STEP).
- **ISO/IEC/IEEE 42010** — the architecture-description standard linking GSMAF to general systems-architecture practice.
- **NASA-STD-7009** — model and simulation credibility, connecting interoperability to V&V and the trustworthiness of shared model-based results.

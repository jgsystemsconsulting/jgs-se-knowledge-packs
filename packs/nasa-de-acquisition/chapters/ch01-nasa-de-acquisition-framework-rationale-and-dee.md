# Chapter — The Digital Engineering Acquisition Framework: Scope, Rationale, and the Digital Engineering Environment

## Core Idea

NASA-HDBK-1004 establishes a *digital engineering acquisition framework*: a structured way for the Agency to specify, contract for, and control the digital data and models it buys across the entire program/project life cycle. The framework rests on two visible instruments — the Data Requirements Description (DRD) and the contract language written into the Statement of Work — and one underlying purpose: to stand up and feed a Digital Engineering Environment (DEE). The DEE knits together the system's data with its people, processes, and supporting technology so that evolving data and models can be stored, retrieved, analyzed, and visualized for stakeholders across the whole enterprise.

The central shift the Handbook argues for is moving away from a document-centric acquisition style toward a model-based one. In the traditional approach, information lives in documents; in the digital approach, digital models themselves hold the information that documents once carried, and they satisfy the program's decision and information needs directly. The Handbook frames this not as a tooling preference but as a mission-assurance move: getting the right data to the right people at the right time raises the probability of mission success and lowers risk.

This pack pairs with NASA-HDBK-1009A, which the present Handbook complements rather than replaces. The two should be read together; this chapter covers only the scope, rationale, and environment material in NASA-HDBK-1004 sections 1 through 5.

## Frameworks Introduced (exact source names, when/how)

- **Digital Engineering Environment (DEE)** — introduced in the Purpose (§1.1) and developed in §4. Defined as an environment that, at its simplest, hosts collaboration over digital project and technical product data among participants, letting them work through digital tools and technologies built largely on model-based enterprise practices. It is the thing the acquisition framework exists to enable.
- **Digital engineering acquisition framework** — the Handbook's titular construct. §1.1 positions it as the mechanism (DRDs plus SOW language) for a DEE; §4 casts it as a set of disciplined, collaborative processes and systems whose job is to plan, procure, and govern how product-definition and configuration data flow interoperably across both the product and the data life cycles, from early conception out to disposal.
- **Data Requirements Descriptions (DRDs)** — named in §1.1 and detailed in §5. They carry the contract language and standards needed to execute data interoperability and to govern collaboration, define deliverables, and enforce them at key decision points.
- **Model-based enterprise (MBE)** — invoked as the practice base the DEE is built on (§4), and named alongside the related model representations the framework references: model-based definition (MBD, annotated 3D CAD models), model-based analyses (MBA), and model-based systems engineering (MBSE).
- **Product Data and Life-Cycle Management (PDLM)** — §1.1 states this Handbook supersedes NASA-HDBK-0008, the NASA PDLM Handbook, and that the new framework augments PDLM by also addressing the acquisition, retrieval, use, and storage of all program/project data, not just technical data.
- **NPR 7123.1, NASA Systems Engineering Processes and Requirements** — cited in §1.1 as the source of the requirement for a technical-data management process (capture, storage, integrity, dissemination).
- **NPR 7120.5, NASA Space Flight Program and Project Management Requirements** — cited in §1.2 (Applicability) as the definition of the single-project and tightly coupled programs to which the Handbook applies.
- **Digital/Model-based Functional Integration (Figure 1, sourced to CIMdata)** — §4 references this figure to depict how a digital/model-based enterprise enables data exchange among the organizations supporting the whole life cycle, Pre-Phase A through Phase F.

## Key Concepts

**Digital engineering, defined.** The Handbook treats digital engineering as an integrated digital approach that draws on authoritative sources for product and system data and the associated models, used collaboratively across every product-involved discipline, supporting life-cycle activities from conceptualization through disposal — that is, Pre-Phase A through Phase F.

**Authoritative, decentralized sources.** A recurring qualifier is that the data and model sources are authoritative yet decentralized (or federated), stitched together so stakeholders across organizations and disciplines can work against them seamlessly. The DEE is the connective tissue; interoperability or federation of NASA's IT systems is what makes the connective tissue secure and accessible.

**The five key areas to execute the framework (§4).** The Handbook lists the areas that must be applied, each pointing to its own appendix: (a) Model-Based Data Definition (Appendix C); (b) Digital Data Collaboration (Appendix D); (c) Architecture (Appendix E); (d) Interoperability Standards (Appendix F); and (e) Contractual Data Acquisition via DRDs (§5 and Appendices A and B).

**What the framework manages.** Beyond definition data, the framework governs how product data is created and revised, the maturity levels models reach, the configurations a product moves through, the engineering data affiliated with it, the records of how components behave in their mission environments, and the product's software and hardware alike. It binds definition and development data, processes, tools, and business/analytical systems into a single digital product-information backbone for product configuration information.

**Lead Systems Integrators.** §4 calls out the assignment of Lead Systems Integrators as essential. Their job is to build integrated model sets so the combined data/model sets stay consistent and complete and so deliverables are clearly defined and adhered to.

**DRDs as the contractual hinge.** §5 explains that acquisition DRDs carry the language and standards that make data interoperability and collaboration governance enforceable, and that they should fully describe each required data item — its purpose, content, format, maintenance, and submittal requirements. The data items in scope explicitly include MBx models, documents, reports, and drawings.

**Why the contract language matters.** Putting this language into NASA contracts ensures data acquisitions are properly included, so the Government does not lose data, information, or knowledge produced under the contract — and lowers cost and effort for both sides. It also secures Government access to data during the contract and effective transfer afterward. The Handbook notes this language must appear across several sections of the Request for Proposals to achieve the needed level of data definition, integrity, control, and access. Appendix A provides starter DRDs; Appendix B provides guidance on developing the contract language.

**Applicability and precedence.** §1.2 scopes the Handbook across the full life cycle of NASA space flight programs of the single-project and tightly coupled kind, present and planned (per NPR 7120.5), and recommends it as guidance elsewhere; the example DRDs are meant to be tailored to each program/project and product. §2.4 sets order of precedence: the Handbook does not supersede or waive existing Agency guidance, and conflicts are resolved by the delegated Technical Authority(ies).

## Mental Models

**Models as the container, not the byproduct.** The cleanest way to hold the Handbook's thesis is: in a document-centric world, the model produces documents and the documents are the deliverable; in the model-based world the Handbook describes, the model *is* the deliverable and it holds the information the documents used to hold. Acquisition therefore has to be written to buy and control models, not paper.

**The framework feeds the environment.** Picture two layers. The acquisition framework (processes, DRDs, SOW language) is the upstream layer that defines and pulls in the right data under contract; the DEE is the downstream layer where that data and those models are stored, accessed, analyzed, and visualized for stakeholders. The framework creates the foundation and baseline from which the DEE in an MBE setting is driven.

**Right data, right people, right time, right decision.** The Handbook offers its own causal chain for *why* model-based acquisition is worth the effort: better availability and integration of data across like and disparate systems puts the right data in front of the right people at the right time, which enables the right decisions and reduces risk — and so raises the probability of mission success. Use this chain as the justification lens when weighing a framework decision.

**Life cycle as the spine (Pre-Phase A → Phase F).** Almost every definition in this slice is bounded by the same life-cycle span — concept/studies through closeout/disposal. When applying the framework, the test for "is this in scope" is whether the data or model supports a life-cycle activity anywhere along that spine.

## Key Takeaways

- NASA-HDBK-1004 is a guidance Handbook (not a binding requirement document) for building a digital engineering acquisition framework, expressed through DRDs and Statement of Work / RFP contract language, in support of a Digital Engineering Environment.
- It supersedes NASA-HDBK-0008 (the PDLM Handbook) and augments — does not discard — PDLM, broadening coverage to all program/project data, not only technical data.
- The DEE connects data, people, processes, and technology so authoritative, decentralized data and models can be shared seamlessly across organizations and disciplines from Pre-Phase A through Phase F.
- Executing the framework rests on five key areas — model-based data definition, digital data collaboration, architecture, interoperability standards, and contractual data acquisition via DRDs — each with a dedicated appendix.
- DRDs and RFP-embedded contract language are the enforcement mechanism: they protect the Government's access to and ownership of contractor-produced data and lower cost and effort for both parties.
- Lead Systems Integrators are essential to keep integrated model sets consistent, complete, and clearly deliverable.
- The Handbook applies across the full life cycle of NASA space flight single-project and tightly coupled programs (NPR 7120.5), with example DRDs meant to be tailored, and it never overrides existing Agency guidance — conflicts go to the delegated Technical Authority.
- This pack pairs with NASA-HDBK-1009A; treat the two as complementary references.

## Connects To

- **NASA-HDBK-1009A** — the explicit companion reference this pack pairs with; read alongside NASA-HDBK-1004 for the fuller digital engineering acquisition picture.
- **NASA-HDBK-0008 (PDLM)** — the superseded predecessor; the framework here extends PDLM thinking to all program/project data.
- **NPR 7123.1, NASA Systems Engineering Processes and Requirements** — supplies the technical-data management requirement (capture, integrity, dissemination) the framework operationalizes.
- **NPR 7120.5, NASA Space Flight Program and Project Management Requirements** — defines the program/project types the Handbook governs.
- **Model-based methods (MBD, MBA, MBSE, MBE)** — the practice base the DEE is built on; downstream chapters and appendices (C–F) detail data definition, collaboration, architecture, and interoperability standards.
- **DRDs and contract/RFP language (§5, Appendices A and B)** — the contractual surface where this framework becomes binding on suppliers; the natural next chapter for anyone moving from rationale to implementation.

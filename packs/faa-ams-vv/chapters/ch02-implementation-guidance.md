Sources: FAA AMS Lifecycle Verification and Validation Guidelines, Version 4.0 (January 2023), printed pages 8-13 (Section 2: V&V Planning 2.1, Performing V&V 2.2, V&V Reporting 2.3, V&V Decision Support 2.4).

# Chapter 2: V&V Implementation Guidance

> How-to chapter. Section 2 of the guideline breaks V&V execution into four activities: planning, performing, reporting, and decision support. This chapter synthesizes printed pages 8-13.

## Core Idea

V&V is a pipeline: plan it inside the program's own documents, perform it with independent reviewers, report it in controlled records, and feed decision points as entrance criteria. A gap in any stage starves the decision behind it.

## Frameworks Introduced

### Plan: planning embedded in program documents (Section 2.1)

Every acquisition program must plan V&V, and that planning must be folded into the appropriate phase and program planning documents across the product's lifecycle. Named hosts include the plan for Concept and Requirements Definition, the plans for initial and final Investment Analysis, the Implementation Strategy and Planning Document (ISPD), the Test and Evaluation Master Plan (TEMP), the Program Management Plan, the System Engineering Management Plan, and the Quality Assurance Plan.

Each planning document carries the V&V planning elements that apply to it. Paraphrased, the nine elements are:

1. a description of the verification methods used;
2. a description of the validation methods used;
3. identification of the work products, product components, and products to be verified and/or validated;
4. identification of the processes, standards, and criteria used for verification and validation in the phase, citing references such as the Systems Engineering Manual, Concept Development and Validation Guidelines, and the Test and Evaluation Handbook;
5. the measures and reports needed to follow and record V&V events and activities;
6. who holds the roles and responsibilities across V&V events and activities;
7. identification of independent stakeholders or reviewers who will (or will not) verify and validate the item;
8. a description of the tools, models, prototypes, laboratories, and simulators required to support V&V;
9. identification of the training required for successful completion of V&V events and activities.

### Perform: independence and the prerequisite check (Section 2.2)

V&V is performed by independent stakeholders or reviewers, identified in Tables 1 through 6, who are not directly involved in developing the item under review. While performing V&V, reviewers must stay cognizant of the validity of V&V activities performed, or missed, on prerequisite work products, components, and products. If inconsistencies or conflicts surface about the validity of earlier V&V, or if a requisite V&V activity turns out not to have been performed, the issues must be documented and resolved before proceeding.

**Critical technical documents** form the basis for future work products, components, and products, and must be verified and validated before use in any subsequent process, including the V&V process itself. The named set: NAS Requirements Document, NAS Segment Implementation Plan, NAS ConOps, National Air Research Plan, NextGen Implementation Plan, and Enterprise Architecture. V&V exists to guarantee a valid basis for programs, no service gaps, and alignment with agency goals. The criteria for checking them are the FAA Strategic Initiatives document plus all applicable standards associated with each document (manuals, handbooks, templates, guidance).

### Perform: what gets checked, and which methods

**Work products (2.2.1).** All major work products a program develops, or that an acquisition category requires, should get formal, structured V&V. Scope varies with program complexity and resources; Section 3 fixes the minimum set. Work-product verification confirms that the standards, templates, and other requirements defining content and purpose were properly followed. The primary methods are inspections, peer reviews, audits, and checklists. Work-product validation confirms that the work product supports an operationally effective and suitable product, and its method list is broader and user-facing: walk-throughs and dry runs, discussions with users, user surveys, functional presentations, analyses, testing, demonstrations, modeling, and storyboarding.

**Products and product components (2.2.2).** Verification confirms that products and components were built properly to the specifications in supporting work products. Validation confirms they are operationally effective and suitable for end users and maintainers. Product-tier V&V is primarily accomplished through Test and Evaluation (T&E). T&E personnel work in all phases, but product and component T&E concentrates in Solution Implementation and In-Service Management, divided into three activities:

- **Development Test (DT)** serves verification objectives: the item under test meets its specified technical and performance requirements, and, for final products, is fully integrated, stable, and has no adverse effect on the rest of the NAS. DT is conducted by the developer and witnessed by the FAA.
- **Operational Test (OT)** serves validation objectives: major components and the final product are operationally effective and suitable for NAS use, and the NAS infrastructure is ready to accept the product. OT is run by the OT Test Director and an OT test team of Air Traffic, Technical Operations, and second-level maintenance personnel; other FAA organizations and external entities (airlines, cargo carriers, military, private industry) may join as required.
- **Independent Operational Assessment (IOA)**, for designated products, is led by the program manager and an Independent Safety Assessment Team and gives decision-makers an independent determination of operational readiness supporting deployment decisions such as the In-Service Decision.

Product and component verification methods add analyses, testing, demonstrations, simulations, and accreditation to the work-product set. Product and component validation methods are similar to the work-product validation set, with user evaluation questionnaires replacing general user surveys.

### Report (Section 2.3)

V&V reporting supports AMS decision points and should be factored into entrance criteria. Quality reporting promotes informed decisions and contributes to program effectiveness and efficiency; it also supports performance measurement by providing quantitative and qualitative results against technical performance criteria. Essential practices: V&V events are documented and that documentation is controlled and archived so historical records exist; test reporting states how well the product was built and how far it fulfills operational needs.

At minimum a V&V report contains: Introduction; Purpose (the objectives of the V&V event); Criteria (the source criteria used as the basis for the event); V&V Approach (a description of the event); V&V Participants; V&V Results; and Recommendations.

### Decide (Section 2.4)

Structured V&V before planned decision points — Concept and Requirements Definition Readiness Decision (CRDRD), Investment Analysis Readiness Decision (IARD), Initial Investment Decision (IID), Final Investment Decision (FID), and In-Service Decision (ISD) — lowers the risk of defects in whatever supports those decisions. It aids decision-makers, the Joint Resources Council, the Acquisition Executive Board, and designated in-service decision authorities, by supplying assessments of critical work products for each phase and surfacing technical and non-technical risk. V&V applied against planning documentation, for instance, can expose inconsistencies with predecessor documents before they become cost growth and schedule delay.

Essential decision-support practices: V&V events and results are formally identified in plans as entrance criteria for decision points; they are scheduled and planned well in advance; results are applied consistently so decision-makers get reliable data on maturity and quality; and results must support the objectives associated with the decision point before it is accepted or approved.

## Key Takeaways

- Plan V&V inside the documents programs already write; each carries the planning elements that apply to it.
- Reviewers must be independent of the item's development, and must check that prerequisite V&V actually happened and still holds.
- Critical technical documents get V&V'd before anyone downstream is allowed to lean on them.
- Method choice follows tier: work products get inspection-grade methods; products get T&E (DT verifies, OT and IOA validate).
- Reports are controlled, archived, and carry fixed minimum content.
- V&V results are entrance criteria at decision points, not after-the-fact paperwork.

## Connects To

- `ch01` supplies the verify-vs-validate and three-tier vocabulary used throughout this chapter.
- `ch03` shows the machinery landing in SASP, CRD, and the five primary management documents.
- `ch04` carries it through Investment Analysis, Solution Implementation, and In-Service Management.

# Chapter — V&V Implementation Guidance: Planning, Performing, Reporting, and Decision Support

## Core Idea

Under the FAA Acquisition Management System (AMS), verification and validation is not a single end-of-line test event but a continuous discipline threaded through the entire acquisition lifecycle. The implementation guidance organizes that discipline into four connected activities: you **plan** V&V up front and embed it in the program's governing documents; you **perform** V&V through independent reviewers using method sets matched to what is being examined; you **report** the results in a controlled, archived form; and you feed those reports into **decision support** so that major acquisition decision points are gated by evidence of work-product maturity and product readiness. The unifying logic is that structured V&V performed *before* a decision lowers the risk of carrying defects forward — whether in a work product, a product component, or a delivered product.

A second organizing distinction runs through the whole chapter: verification asks whether something was built correctly against its defining standards or specifications, while validation asks whether it actually supports an operationally effective and suitable end product for users and maintainers. That split governs which methods apply, who performs them, and where in the lifecycle they land.

## Frameworks Introduced (exact source names, when/how)

- **AMS V&V Planning Elements (the nine planning items)** — Introduced in §2.1 as the mandatory content that must be folded into program planning documents. The guidance lists nine elements covering verification methods, validation methods, identification of items to be V&V'd, the processes/standards/criteria to apply, tracking measures and reports, roles and responsibilities, identification of independent reviewers, the tools/models/prototypes/labs/simulators needed, and required training. These are applied per document, "as they apply" to each.

- **AMS Planning Documents that must carry V&V planning** — Named explicitly in §2.1 as the vehicles into which the planning elements are incorporated. The named vehicles are: the CRD-phase plan; the **Implementation Strategy and Planning Document (ISPD)**; the plans for both initial and final Investment Analysis; the System Engineering Management Plan; the **Test and Evaluation Master Plan (TEMP)**; the Quality Assurance Plan; and the Program Management Plan. The list is stated as non-exhaustive.

- **Criteria / standards documents for V&V** — §2.1 names three reference sources for the processes, standards, and criteria element: the **Systems Engineering Manual**, the **Concept Development and Validation Guidelines**, and the **Test and Evaluation Handbook**. §2.2 separately names the **FAA Strategic Initiatives document** (plus applicable manuals, handbooks, templates, and guidance) as the criteria basis for validating critical technical documents.

- **Critical Technical Documents subject to prerequisite V&V** — §2.2 enumerates the foundational documents that must be verified and validated before they are used downstream. Those foundational documents are the **Enterprise Architecture**, the **NextGen Implementation Plan**, the **National Aviation Research Plan**, the NAS-level **Segment Implementation Plan**, the **NAS Requirements Document**, and the **NAS Concept of Operations**. The stated purpose is ensuring a valid program basis, no service gaps, and alignment with agency goals.

- **Test and Evaluation (T&E) breakdown — DT / OT / IOA** — §2.2.2 introduces the three Solution Implementation T&E activities. **Development Test (DT)** serves verification (developer-run, FAA witnessing); **Operational Test (OT)** serves validation, run by the ANG-E OT Test Director and test team with Air Traffic, Technical Operations, and second-level maintenance personnel; **Independent Operational Assessment (IOA)**, for designated products, is headed by a PM drawn from the Independent Safety Assessment Team, giving decision-makers an independent read on operational readiness.

- **Four method catalogs (Work Product vs. Product/Component, Verification vs. Validation)** — §2.2.1 and §2.2.2 each provide explicit method lists, with definitions deferred to Appendix C. They differ by purpose (see Key Concepts).

- **V&V Report minimum content set** — §2.3 specifies a seven-part minimum report structure: Introduction, Purpose, Criteria, V&V Approach, Participants, Results, and Recommendations.

- **V&V Decision Support practices** — §2.4 lists four practices that bind V&V into the AMS decision-point gating mechanism.

- **External guidance sources** — §2.1 points to two FAA resources for further planning guidance: the **FAA Acquisition System Toolset (FAST)** website and the **ANG-E Test and Evaluation (T&E) Portal**.

## Key Concepts

**Planning is mandatory and document-embedded.** Per §2.1, V&V planning is required for every acquisition program and is not a standalone artifact — it must be written into the appropriate phase and program planning documents across the lifecycle. The nine planning elements are the checklist for what each of those documents must contain where relevant.

**Independence is structural, not advisory.** Both §2.1 (element 7) and §2.2 define an independent stakeholder or reviewer as someone not directly involved in developing the item being V&V'd. §2.2 ties the specific independent performers to the responsibility tables (Tables 1–6) elsewhere in the document.

**Prerequisite-validity awareness.** §2.2 requires reviewers to stay aware of whether V&V on *prerequisite* items was actually performed and remains valid. If a prior V&V activity was skipped, or inconsistencies surface, those must be documented and resolved before proceeding — V&V is chained, not isolated per artifact.

**Work products vs. products/components.** §2.2.1 defines a work product as something that represents, defines, or directs the product or its components — concepts of operation, plans, designs, requirements, specifications, models, prototypes, contracts, and similar documents. §2.2.2 defines a product as a deliverable system, service, facility, or operational change, with product components as the lower-level integrated elements. The two get different method sets.

**Verification vs. validation, applied to each tier.** For work products, verification checks that defining standards and templates were followed; validation checks that the work product supports building an operationally effective and suitable end product (§2.2.1). For products and components, verification confirms the item was built to specification; validation confirms operational effectiveness and suitability to users and maintainers (§2.2.2).

**The four method catalogs (defined in Appendix C).**
- *Work Product Verification:* checklists, audits, peer reviews, and inspections.
- *Work Product Validation:* user surveys and discussions with users; functional presentations; dry-run walk-throughs; storyboarding and modeling; demonstrations and testing; plus analyses, audits, peer reviews, inspections, and checklists.
- *Product/Component Verification:* analyses, audits, peer reviews, inspections, checklists, simulations, testing, demonstrations, and accreditation.
- *Product/Component Validation:* user-evaluation questionnaires and discussions with users; functional presentations; simulations and testing; demonstrations; analyses, audits, peer reviews, inspections, and checklists.

The pattern worth noting: validation catalogs are user-facing and broader; product-tier catalogs add analysis, simulation, and (for verification) accreditation that the lighter work-product verification set omits.

**T&E is where product V&V mainly lives.** §2.2.2 states V&V of products and components happens primarily through T&E, concentrated in Solution Implementation and In-Service Management. DT carries verification (and, for final products, confirms full integration, stability, and no adverse effect on the rest of the NAS); OT and IOA carry validation and the question of whether NAS infrastructure is ready to accept the product.

**Reporting is controlled and decision-oriented.** §2.3 frames quality reporting as the bridge to informed decisions and to performance measurement (quantitative and qualitative results against technical performance criteria). Events must be documented, and that documentation controlled and archived as historical record. Reports on work-product quality should state how well the work product supports an effective, suitable end product; reports on T&E results (final test reports) should state how well the product is built and how far it meets operational needs.

**Decision support is the payoff.** §2.4 makes the explicit link: structured V&V before a decision point reduces defect risk by ensuring completeness and quality, surfaces both technical and non-technical risk, and — its worked example — can expose inconsistencies between a planning document and its predecessor documents that would otherwise drive cost and schedule overruns.

## Mental Models

**The four-stage V&V pipeline.** Plan → Perform → Report → Decide. Each stage feeds the next: planning defines methods, owners, and criteria; performing generates evidence under independence; reporting controls and packages that evidence; decision support consumes it as entrance criteria. A gap in any earlier stage starves the decision.

**Two questions, four boxes.** Cross "verification vs. validation" with "work product vs. product/component" and you get the four method catalogs. Knowing which box you're in tells you which method list, which performer, and which lifecycle phase applies. (Right-built vs. right-thing × describes-the-thing vs. is-the-thing.)

**The validity chain.** Treat every work product as standing on the verified validity of its predecessors. Before V&V'ing the current item, confirm the prerequisite items were genuinely V&V'd and still hold. A broken upstream link must be fixed and documented before moving on — defects compound forward otherwise.

**Gate-before-decision.** Map V&V events onto AMS decision points as *entrance criteria*. Schedule and plan them well ahead of the decision so results are reliable and consistently applied, giving decision-makers low-risk grounds keyed to the maturity and quality of the work products.

**Verify the foundations first.** Critical technical documents (NAS ConOps, NAS Requirements Document, Enterprise Architecture, and the rest) are the bedrock everything else inherits from, so they are V&V'd against the FAA Strategic Initiatives document and applicable standards *before* downstream use — preventing service gaps and agency-misalignment at the root.

## Key Takeaways

- V&V planning is required for all AMS acquisition programs and must be embedded across the program's planning documents (ISPD, TEMP, PMP, SEMP, QA Plan, and others), each carrying the relevant subset of the nine planning elements.
- Independence is definitional: performers must not have developed the item under review, and they must verify that prerequisite V&V was actually done and is still valid before proceeding.
- Work products and products/components are V&V'd with distinct method catalogs; in all four catalogs the detailed definitions live in Appendix C.
- Verification = built right to standards/specifications; validation = operationally effective and suitable for users and maintainers — applied consistently at both the work-product and product tiers.
- Product-level V&V runs mainly through T&E, split into DT (verification), OT (validation), and IOA (independent operational-readiness assessment for designated products), concentrated in Solution Implementation and In-Service Management.
- Reports must be controlled and archived, must feed performance measurement, and at minimum cover Introduction, Purpose, Criteria, Approach, Participants, Results, and Recommendations.
- The point of all of this is decision support: V&V events should be named as entrance criteria, scheduled ahead of decision points, and applied consistently so decisions rest on evidence of maturity and quality rather than assumption.

## Connects To

- **Section 3 of the AMS V&V Guidelines** — §2.2.1 explicitly forwards to Section 3 for the minimum set of work products that must undergo V&V across the AMS lifecycle; this chapter supplies the *how*, Section 3 the *what/when*.
- **Appendix C (method definitions)** — every method catalog in §2.2.1/§2.2.2 defers its definitions and descriptions to Appendix C; this chapter names the methods, Appendix C explains them.
- **Tables 1–6 (responsibility assignments)** — §2.2 ties the identity of independent performers to these tables, connecting the performing activity to specific role assignments.
- **AMS lifecycle decision points** — §2.3 and §2.4 connect V&V reporting and results to the entrance criteria of major AMS acquisition decisions, linking this chapter to the broader AMS governance model.
- **FAA reference standards** — the Systems Engineering Manual, Concept Development and Validation Guidelines, Test and Evaluation Handbook, and FAA Strategic Initiatives document supply the criteria against which V&V is performed.
- **External tooling** — the FAST website and the ANG-E T&E Portal extend the planning guidance beyond this document.

# FAA AMS Lifecycle V&V Guidelines: Patterns & Techniques

Reusable moves synthesized from the FAA AMS Lifecycle Verification and Validation
Guidelines, Version 4.0 (January 2023). Each has When / How / Trade-offs. These
operationalize the guideline's plan/perform/report/decide pipeline and its
decision-point-gated, table-driven model.

## Pattern 1: Split every check into "built right" (verify) vs. "right thing" (validate)

**When to use**: any artifact, gate, or tier (work product, product component, product).

**How**: for each item, write two separate criteria lists. *Verification* criteria: the templates, standards, handbooks, and policy the item must conform to (PRD template, System Engineering Manual, Test and Evaluation Handbook, AMS policy). *Validation* criteria: the substantive upstream content the item must actually serve (Enterprise Architecture, Solution ConOps, final PRD with its COIs and CPRs, prior assessment results). Run the two checks distinctly.

**Trade-offs**: two criteria sets per artifact cost more bookkeeping than one pass/fail review, but an item can be flawless against its template while serving the wrong need; collapsing the two questions hides exactly the defects that are most expensive to find later.

---

## Pattern 2: Embed V&V planning into the program's existing documents

**When to use**: program start, and whenever a governing plan is created or updated.

**How**: fold the nine planning elements (verification methods, validation methods, items to be V&V'd, processes/standards/criteria, tracking measures and reports, roles and responsibilities, independent reviewers, tools/models/prototypes/labs/simulators, required training) into the documents the program already writes: the CRD plan, the IA plans, the ISPD, the TEMP, the PMP, the SEMP, and the QA Plan, each carrying the elements that apply to it.

**Trade-offs**: no standalone V&V plan means the elements live where the program already maintains them, at the cost of cross-document reads at the gate to confirm nothing fell between documents.

---

## Pattern 3: Anchor V&V on decision points as entrance criteria

**When to use**: scheduling V&V across any phase.

**How**: map required V&V events onto the AMS decision points (CRDRD, IARD, IID, FID, ISD, plus the Contract Award, Product Demonstration, Product Acceptance/CAI, Production, and implement/deploy gates). Formally identify the events and results in plans as entrance criteria, and schedule them well in advance of the decision so results are reliable and applied consistently.

**Trade-offs**: front-loading V&V ahead of a gate adds early schedule pressure, but a gate decided on un-V&V'd documents hands senior management false confidence and pushes risk downstream where it costs more.

---

## Pattern 4: Find your row; don't improvise the check

**When to use**: planning V&V for any single work product, component, or product.

**How**: locate the artifact's row in its phase table (Table 1 SASP, Table 2 CRD, Table 3 Initial IA, Table 4 Final IA, Table 5 SI, Table 6 ISM). The row pre-binds the decision point, the validation criteria, the verification criteria, and the responsible stakeholder. Execute what the row says rather than inventing criteria.

**Trade-offs**: the tables are January 2023 policy snapshots; each one's own footnote says detailed current phase guidance and templates exist and should be reviewed. Relying on a table without checking superseding guidance is the flagged mistake.

---

## Pattern 5: Verify the foundations, and the criteria, before anything downstream

**When to use**: before any program work leans on a critical technical document, or on any criterion.

**How**: the critical technical documents (NAS ConOps, NAS Requirements Document, NAS Segment Implementation Plan, National Air Research Plan, NextGen Implementation Plan, Enterprise Architecture) are verified and validated before use in any subsequent process, including the V&V process itself. Treat the criteria themselves as work products that must earn trust through the same systematic V&V rather than as assumed-correct yardsticks. The EA closes the loop: it grounds criteria and absorbs V&V feedback.

**Trade-offs**: V&V'ing criteria as well as products doubles the surface area, but a stale or wrong criterion confers illusory assurance on everything measured against it.

---

## Pattern 6: Chain V&V forward through artifact versions

**When to use**: before V&V'ing any item that inherits from an earlier artifact.

**How**: check that V&V on prerequisite items was actually performed and remains valid; document and resolve any inconsistency or skipped activity before proceeding. Then use the chain deliberately: the tables make each new version's validation criteria include the previous version's documented V&V results (initial PRD results feed the final PRD row; preliminary TEMP results feed the initial TEMP row; the final ISPD carries the initial ISPD's results).

**Trade-offs**: the prerequisite check slows the start of every review, but defects in an unverified upstream artifact compound forward silently, corrupting every downstream verification that inherits from them.

---

## Pattern 7: Match the method to the tier and the question

**When to use**: choosing how to verify or validate a given item.

**How**: cross two axes (verification vs. validation, work product vs. product/component) and land in one of four catalogs. Work-product verification: inspections, peer reviews, audits, checklists. Work-product validation adds the user-facing set: discussions with users, surveys, functional presentations, walk-throughs/dry runs, modeling, storyboarding, plus analyses, testing, demonstrations. Product/component verification adds analyses, testing, demonstrations, simulations, and accreditation. Product/component validation is the user-facing and testing set. Appendix C definitions are paraphrased in `glossary.md`.

**Trade-offs**: heavier product-tier methods buy stronger evidence at real cost; demanding inspection-grade rigor for a lightweight work product, or a survey where an inspection suffices, wastes the program's V&V budget.

---

## Pattern 8: Independence is structural, not preferential

**When to use**: staffing any V&V activity, from a work-product peer review to an IOA.

**How**: the guideline defines the reviewer as a stakeholder not directly involved in developing the work product, component, or product under review, and makes identifying that reviewer a required planning element; Tables 1 through 6 name the stakeholders per row. Extreme cases get their own instruments: peer reviews by unbiased SMEs, and the IOA led by a program manager from the Independent Safety Assessment Team for designated products.

**Trade-offs**: pulling in reviewers outside the development team adds coordination and ramp-up cost, but self-review silently inherits the developer's blind spots, and a gate performed by the party being gated proves nothing.

---

## Pattern 9: Shift left, then stay agile

**When to use**: from the earliest concepts, and whenever a program's work products are still maturing.

**How**: two moves the guideline names. *Shift-left*: major defects are introduced early but surface late, when they cost more; move V&V tasks as early in the lifecycle as possible, and engage testers on program office teams from the concepts-of-operations and requirements phase onward. *Agile acquisition*: work in small batches with fast learning cycles, treat work products as fluid and continually maturing, and iteratively define, prototype, test, and demonstrate capability in close coordination with users, with early and continual V&V of concepts, requirements, developed elements, and integrated systems. The V-Model's loopback arrows and its shift-left caption are the same idea drawn as a picture.

**Trade-offs**: starting acquisition on an acceptable level of immature concepts and requirements buys speed, but only works if V&V and T&E run continuously; stopping the early checking converts agility into accumulated, unexamined debt.

---

## Pattern 10: Front-load security and safety as gated criteria

**When to use**: from the first phase (security) and through Solution Implementation (safety and security at the ISD).

**How**: security enters at SASP: ISS assessments are validated against the FIPS-199 Security Categorization Table and verified against ISGSA, and the pattern repeats through CRD, IA, and the System Security Authorization gate (POA&M, Security Authorization Handbook, Information Systems Security Manager). Safety arrives as a gated obligation at the ISD: the Safety Risk Management document or System Safety Assessment Report is verified against the specifications, the SRM document, and the contract, validated against prior safety assessments and the solution ConOps, and verified against the FAA SMS, with the ATO Office of Safety and Technical Training on the stakeholder list.

**Trade-offs**: assessing security and safety on day one costs effort before the design is firm, but bolting them on late means re-validating constraints that should have shaped the design, the most expensive form of rework.

---

## Pattern 11: In service, prove the change AND re-prove the purpose

**When to use**: during In-Service Management, for every modification to the fielded baseline.

**How**: carry the double burden on every change. *Verify* the modification against new or revised requirements and governing policy (system specifications, NAS Integrated Systems Engineering Framework, FAA Form 1800-2 for NCPs, FAA Order 1800.66 configuration management policy, FAA Order 1320.58A for directives writing). *Validate* that the requirement or operational concept driving the change is itself valid and still serves the mission (operational analyses, post-implementation reviews, the final PRD). Route the change through the implement and deploy decision gates, and let ISM DT and OT (IOA if applicable) do the heavy lifting. Feed in-service performance data back into Mission Analysis and Investment Analysis to revalidate continued sustainment.

**Trade-offs**: re-validating purpose on every change costs more than a pure conformance check, but a change can match its specification perfectly and still no longer serve an operational need; both passes are what keep the fielded system fit for purpose.

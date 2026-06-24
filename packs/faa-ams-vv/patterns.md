# FAA AMS Lifecycle V&V Guidelines — Patterns & Techniques

Reusable patterns synthesized from the FAA AMS Lifecycle V&V Guidelines, Version 3.0
(April 2017). Each has When / How / Trade-offs. These operationalize the guideline's
table-driven, decision-point-gated model of verification and validation.

## Pattern 1: Split every check into "built right" (verify) vs. "right thing" (validate)

**When to use**: at every artifact, at every gate, for every tier (work product, product component, product).

**How**: for each item, write two separate criteria lists. *Verification* criteria are the templates, standards, handbooks, and policy the item must conform to (e.g., the PRD template, the System Engineering Manual, the Test and Evaluation Handbook, AMS Policy). *Validation* criteria are the substantive upstream content the item must actually agree with and serve (e.g., the EA, the Solution ConOps, the Final PRD with its COIs/CPRs, prior assessment results). Run the two checks distinctly; never let one stand in for the other.

**Trade-offs**: maintaining two criteria sets per artifact is more bookkeeping than a single pass/fail review — but a document can be flawless against its template (verifies) while satisfying the wrong need (fails validation), so collapsing the two hides exactly the defects that are most expensive to discover later.

---

## Pattern 2: Embed V&V planning into the program's existing documents (don't write a standalone plan)

**When to use**: at program start, and whenever a governing plan is created or updated.

**How**: fold the nine V&V planning elements — verification methods, validation methods, items to be V&V'd, processes/standards/criteria, tracking measures and reports, roles/responsibilities, identification of independent reviewers, tools/models/prototypes/labs/simulators needed, and required training — into the relevant planning documents (ISPD, TEMP, PMP, SEMP, QA Plan, and the phase plans), each carrying the subset that applies "as it applies."

**Trade-offs**: distributing V&V across many documents risks fragmentation and requires cross-document consistency checks — but it forces V&V to be owned by the same people who own the work, rather than living in an orphaned plan nobody reads at the gate.

---

## Pattern 3: Anchor V&V on decision points as entrance criteria

**When to use**: when scheduling V&V activities across a phase.

**How**: map each required V&V event onto the AMS decision point it gates (CRDRD, IARD, IID, FID, ISD, and the implement/deploy gates in ISM). Treat the V&V result as an *entrance criterion* for that decision. Schedule and plan the events well ahead of the decision so results are reliable and applied consistently. Use the phase tables (Tables 1–6): each row pre-binds a decision point to its minimum work products, criteria, and responsible stakeholder.

**Trade-offs**: front-loading V&V before a gate adds schedule pressure early — but a gate decided on un-V&V'd documents gives senior management false confidence and pushes risk downstream where it costs more.

---

## Pattern 4: Find your artifact in the table — don't improvise the check

**When to use**: when planning V&V for any single work product, component, or product.

**How**: locate the artifact's row in the phase table (Table 1 SASP, Table 2 CRD, Table 3 Initial IA, Table 4 Final IA, Table 5 SI, Table 6 ISM). The row already specifies (1) the governing decision point, (2) the validation criteria, (3) the verification criteria, and (4) the responsible stakeholder. Execute what the row says rather than inventing criteria.

**Trade-offs**: the tables reflect AMS policy *as of publication* — so always check whether detailed, current phase guidance or templates supersede them. Relying on the table alone, without checking for superseding guidance, is explicitly flagged as a mistake.

---

## Pattern 5: Verify the foundations (and the criteria) before anything downstream

**When to use**: before using any critical technical document or any criterion as a basis for further work.

**How**: V&V the foundational documents first — NAS ConOps, NAS Requirements Document, NAS Segment Implementation Plan, National Aviation Research Plan, NextGen Implementation Plan, and the Enterprise Architecture — against the FAA Strategic Initiatives document and applicable standards. Treat the *criteria themselves* as work products that must earn trust through the same systematic V&V, not as assumed-correct yardsticks handed down from above.

**Trade-offs**: V&V'ing the criteria as well as the products doubles the surface area — but a stale or wrong criterion confers illusory assurance on everything measured against it, so the cost buys real, rather than apparent, validity.

---

## Pattern 6: Chain V&V forward — confirm prerequisite V&V before proceeding

**When to use**: before V&V'ing any item that inherits from an earlier artifact.

**How**: before reviewing the current item, confirm that V&V on its *prerequisite* items was actually performed and remains valid. If a prior activity was skipped or inconsistencies surface, document and resolve them before proceeding. As products mature across gates (initial PRD → final PRD, preliminary TEMP → initial TEMP), feed the earlier version's *documented V&V results* in as validation criteria for the later version.

**Trade-offs**: the chain check slows the start of each review — but defects in an unverified upstream artifact compound forward silently, corrupting every downstream verification that inherited from it.

---

## Pattern 7: Match the method to the tier and the question (four catalogs)

**When to use**: when choosing *how* to verify or validate a given item.

**How**: cross the two axes — verification vs. validation, work product vs. product/component — to land in one of four method catalogs. Work-product verification leans on inspections, peer reviews, audits, checklists. Work-product validation is broader and user-facing (discussions with users, surveys, functional presentations, walk-throughs, demonstrations, modeling, storyboarding, plus the lighter methods). Product/component verification adds analyses, testing, demonstrations, simulations, and accreditation. Product/component validation is user-facing testing/demonstration with analyses and simulation. Definitions live in Appendix C.

**Trade-offs**: the heavier product-tier methods (testing, simulation, accreditation) cost time and infrastructure — apply them where the stakes (operational readiness, safety, security) justify the rigor; reserve the lighter inspection/checklist methods for early work products.

---

## Pattern 8: Demand method + artifact on every checklist row

**When to use**: when filling out any Appendix B checklist (PRD, APB, ISPD, PMP).

**How**: for every element, record two things beyond pass/fail — the *method used* (Inspection, Peer Review, Audit, Checklist, Discussion, User Survey, Functional Presentation, Walk-through, Analysis, Testing, Demonstration, Modeling) and the *artifact* that evidences the outcome. An artifact must be an objective, authenticated record (validation table, report, traceability matrix, minutes, completed checklist, survey results, email).

**Trade-offs**: requiring evidence for each row is more work than asserting a pass — but a checklist with passing rows and empty evidence columns is, by the source's own definition, incomplete; the artifact is the part that survives the meeting and the audit.

---

## Pattern 9: Run two governance tracks in early-lifecycle V&V

**When to use**: through SASP, CRD, and Investment Analysis, where the Business Case is in play.

**How**: route most early artifacts (PRD, APB, ISPD, PMP) through the Appendix B / Tables 1–2 machinery owned by Lines of Business, ANG Engineering Services, and the EA Control Board. Route the *Business Case* through the parallel track owned by Investment Planning & Analysis, closed out by the Independent Evaluation Review (IER), per the AFI Business Case Evaluation and Assessment Guideline. Hold both tracks in view — a program is not V&V-complete at a gate until both have reported.

**Trade-offs**: two tracks add coordination overhead — but the Business Case's analytical, financial basis needs an independent evaluation distinct from the document-template checklists, and conflating the two would weaken the investment decision's evidentiary footing.

---

## Pattern 10: Front-load safety and security as V&V criteria, not late compliance

**When to use**: from the first phase, intensifying toward fielding.

**How**: bring the ISS (Information System Security) assessment into scope at SASP (validated against FIPS-199, verified against ISGSA) and carry it forward as a named criterion through every phase. At Solution Implementation acceptance and the In-Service Decision, treat safety (FAA SMS, Safety Risk Management Document / System Safety Assessment Report) and security (System Security Authorization, POA&M, Security Authorization Handbook) as first-class, gated V&V obligations with their own responsible stakeholders (ATO Office of Safety and Technical Training, Information Systems Security Manager).

**Trade-offs**: assessing security and safety from day one costs effort before the design is firm — but bolting them on late means re-validating against constraints that should have shaped the design, the most expensive form of rework.

---

## Pattern 11: In service, prove the change AND re-prove the purpose

**When to use**: during In-Service Management, for every modification to a fielded baseline.

**How**: carry the double burden on every change. *Verify* the modification against its new or revised requirements and governing policy (System Specification, FAA Form 1800-2, FAA Order 1800.66 for configuration management, FAA Order 1320.58A for document writing). *Validate* that the new/revised requirement or operational concept driving the change is itself sound and still serves the mission (Operational Analyses, Post-Implementation Reviews, operational procedures). Route changes through the implement and deploy decision gates; use ISM DT/OT/IOA as the heavy V&V lifting. Feed in-service performance data back to Mission Analysis and Investment Analysis to revalidate continued sustainment.

**Trade-offs**: re-validating purpose on every change (not just verifying conformance) is more work than a pure change-control conformance check — but a change can match its specification perfectly and still no longer serve the operational need; both passes are mandatory to keep a fielded system fit for purpose.

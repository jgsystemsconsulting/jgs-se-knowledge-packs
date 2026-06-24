# Chapter — Configuration Verification & Audit

> Source basis: MIL-HDBK-61B, Section 8 ("Configuration Verification and Audit"). This pack uses the current **MIL-HDBK-61B**, not the superseded 2001 MIL-HDBK-61A(SE).

## Core Idea

Configuration verification and audit is the fifth CM function: it proves that the thing you built actually matches the thing you said you would build, and that it performs as required. The handbook splits the work into two complementary activities. *Configuration verification* confirms that a configuration item (CI) — in its initial form and after each approved engineering change — satisfies its performance requirements and its documented configuration. *Configuration audit* then examines the verification records together with the physical product to validate, at a program level, that the development effort actually met its performance requirements and that the item is consistent with documentation showing the requirements are met.

The unifying goal is confidence in the configuration documentation that serves as the control baseline across the product's life cycle. The handbook treats verification not as a one-time gate but as an ongoing, embedded function inside the contractor's own process for building and modifying a CI or CSCI — to the point that the Government may accept validation of that process instead of independent physical inspection where that is appropriate. When verification and audit succeed, you end up with a verified system and CI set, a documentation package trustworthy enough to be treated as a product baseline (PBL), and a validated process that keeps product and documentation consistent going forward.

## Frameworks Introduced (exact source names, when/how)

- **Configuration verification** (§8.2.1) — the contractor's means of verifying its own design solution. It is common ground shared by CM, systems engineering, design engineering, manufacturing, and quality assurance. It has a *functional* aspect (the tests and demonstrations that satisfy the quality-assurance sections of the applicable performance specifications, including qualification/verification tests on selected units and repetitive acceptance tests on each deliverable CI or a lot sample) and a *physical* aspect (establishing that the as-built configuration conforms to the as-designed configuration, via physical inspection, process control, or both).

- **Change verification** (§8.2.1.1) — after the initial configuration is verified, each approved change must also be verified. The method scales to the change: a detailed audit, a test series, validation of operation/maintenance/installation/modification instructions, or a simple inspection, chosen according to the CI's nature, the change's complexity, and which support commodities it touches. For a change entering a production line so that all future units carry it, it is normally enough to confirm the manufacturing instructions are updated and released for use and that the first articles are inspected for compliance.

- **Change implementation** (§8.2.1.2) — when support elements are affected or the change must be retrofit incrementally across many fielded units, verification becomes a longer effort. Implementation planning then defines how far each unit and support commodity is verified and what records are kept; incrementally ordered materials, parts, or retrofit kits get their supply actions verified too. Retrofits to organically supported items are verified and reported to Government status accounting by the activity responsible for installation and checkout; contractor-supported retrofits are verified by the contractor.

- **Configuration audits** (§8.2.2) — framed by the dictionary sense of "audit" as a final accounting. A *performance* audit checks that the contractor delivered the capabilities promised in a baselined performance specification (whose requirements are contractual). A *design* audit checks that the product documentation is an accurate picture of the delivered design. The handbook is explicit that the design activity should run both the performance audit (FCA) and the design audit (PCA) on all deliverable CIs — especially where the Government does not intend to audit them itself because their documentation will not be under Government control.

- **Configuration audit activity** (§8.2.2.1) — provides the framework and detailed requirements for verifying that the development effort achieved everything specified in the configuration baselines. If problems surface, the auditing activity owns getting every action item identified, addressed, and closed before the design activity can be judged to have met the requirements.

- **The three audit phases** (§8.2.2.1.1) — *pre-audit* (schedule, agenda, facilities, rules of conduct, participants), the *audit* itself, and *post-audit* (disciplined follow-up on action items). For major weapon systems, this becomes a sequence of serial and parallel audits of various CIs and the system against Government-controlled performance specifications, conducted over time, sometimes including incremental audits of lower-level items.

- **Audit process** (§8.2.2.1.2) — prime contractors audit subcontracted items at subcontractor facilities (with Government participation optional), while the Government audits prime-developed items at the contractor's facility. Functional and physical audits may be run separately or together.

- **FCA — Functional Configuration Audit** (§8.2.2.2) — verifies that the CI's actual performance meets its performance specification. Large/complex CIs may be audited in increments, each documenting discrepancies in its functional area, with a final summary FCA reconciling all action items. Although a true FCA is required only once per CI or system, FCA-*like* activities recur over the life cycle (verifying new design elements introduced by class I ECPs, "first article" inspections when the Government controls detail design, and verification of newly developed CIs inserted via modification, including retest of affected existing elements).

- **PCA — Physical Configuration Audit** (§8.2.2.3) — examines a representative production-configuration CI to verify that the design documentation matches the delivered design, validates supporting production processes, and confirms that any elements redesigned after the FCA still meet the performance specification. Even when the Government will not control the detail design, the contractor should run an internal PCA to fix the starting point for production-design control and establish a PBL. PCAs may recur (e.g., a production line restarted after years idle, or a complex/hard-to-manufacture CI awarded to a new contractor).

- **Audit certifications** (§8.2.2.5.1–.5.2) — historically, DoD maintained distinct hardware and software audit *topics* and matching *certifications* for the FCA and PCA, completed by the audit teams as applicable. Because acquisition reform shifted procurement toward performance specifications, the Government often runs FCAs but leaves PCAs to the contractor without Government involvement — so 61B deliberately *no longer pins each topic and certification to a specific FCA or PCA*, recognizing that some PCA topics still matter in a performance-based buy.

## Key Concepts

- **Verification is continuous; audit is a settlement.** Verification runs throughout build and change activity; audit is the periodic accounting that draws on verification's records and the physical product to render a program-level judgment.

- **Confidence is the currency.** The more the Government trusts a contractor's verification process, the lighter the audit can be. Strong release, baselining, and change-verification practice yields a delivered configuration that is known, documented, and requirement-compliant — which is exactly what satisfies ISO 9000-series design verification and validation and the ISO 10007 configuration-audit requirement.

- **Two attributes per audit.** Both verification and audit carry a functional attribute and a physical attribute. FCA answers "does it perform?"; PCA answers "does the documentation match what we will deliver and support?"

- **Audits target a production-ready design.** Section 8.2.2.4 notes FCAs and PCAs are very unlikely during the MSA and TMRR phases — there is no final, production-ready design that early. EMD is the normal focus for auditing. A note adds that an FCA-like (and sometimes PCA-like) activity may run during the TMRR phase as part of evaluating a competitive prototyping effort.

- **PCA timing slips toward production.** Because EMD-built CIs may be pre-production prototypes unrepresentative of production hardware, PCAs are commonly delayed until early production; the first production units are typically subjected to a PCA, conducted by the contractor or the Government depending on whether the acquisition strategy is performance-based or detail-design-based.

- **FCA scope is bounded by the specification, not operational testing.** The FCA checks achievement of system/CI performance-specification requirements; it does not focus on operational-test results, though operational-test findings can surface unmet baselined requirements.

- **Two failure modes drive different responses.** A shortfall against the *baselined performance specification* generates FCA action items corrected without a contract change. A shortfall against *user-prepared need documents* (operational capability) usually drives ECPs or contract changes to revise the baselined requirements or fund new/revised designs.

- **PCA as a configuration-recovery tool.** During a PCA the representative deliverable is compared against the product configuration documentation (PCD). When a unit cannot be maintained or modified until its configuration is known, inspecting it against approved PCD — PCA-style — lets you either restore it to documented conformance or correct the records to reflect the actual unit.

## Mental Models

- **The closing-the-loop chain.** Identification defines and documents the configuration; control approves changes; verification embeds checks that each build and change conforms; audit performs the final accounting. Verification quietly feeds audit so the audit becomes confirmation rather than discovery.

- **FCA = promise kept; PCA = map matches territory.** FCA tests the performance promise against the spec. PCA confirms the documentation (the map) faithfully describes the delivered item (the territory) you must support for decades.

- **Tax-rate analogy for trust.** A well-run, evidenced verification process is like clean books that make the year-end audit fast and cheap; a weak process forces a heavyweight, adversarial audit.

- **Inputs as evidence chain.** Per §8.1.1, audit/verification consumes status-accounting information, approved configuration documentation, test and verification results, the physical hardware CI or software CSCI and its representation, and the manufacturing/build instructions and engineering tools (including the software engineering environment). Each input is a link of evidence; a missing link weakens the confidence the activity is meant to produce.

- **Documentation accuracy is a logistics decision, not a paperwork chore.** §8.2.2 warns that failing to assure documentation accuracy can lead to accepting items that won't perform as specified or to badly complicated future support — wrong spares, redesign on bad information.

## Key Takeaways

- Verification proves conformance of the initial CI and every approved change; audit validates, at program level, that requirements and documentation are met — both aimed at confidence in the controlling documentation across the life cycle.
- Build verification into the contractor's own process; a process the Government can validate may substitute for independent physical inspection where appropriate.
- Scale change verification to the change — from a simple inspection up to a full audit — and treat incremental retrofit as a planned, record-kept, separately verified effort touching supply actions and support commodities.
- FCA answers performance against the performance specification; PCA answers documentation-versus-design and validates production processes; the design activity should generally run both on deliverable CIs.
- Run audits in three phases — pre-audit, audit, post-audit — and do not declare success until every action item is closed.
- Expect audits in EMD and early production, not in MSA/TMRR; expect PCA to slip toward production when EMD articles are unrepresentative prototypes.
- Successful completion yields a verified system/CI set, a documentation set fit to be a PBL, and a validated consistency-maintaining process.
- 61B intentionally decouples specific audit topics/certifications from "FCA only" or "PCA only," since performance-based acquisition changes who audits what.

## Connects To

- **Configuration identification** — supplies the approved configuration documentation and PCD that audits compare the product against; verification confirms the as-built matches that documented design.
- **Configuration control** — approved engineering changes (including class I ECPs) are the trigger for change verification and for FCA-like re-verification of new design elements.
- **Configuration status accounting** — provides the status, schedule, and configuration inputs to the activity and is the system to which retrofit verifications are reported.
- **Baselines** — successful verification and audit establish the product baseline (PBL); PCA is the mechanism that "locks down" detail design into a PBL.
- **External standards** — explicitly aligns with ISO 9000-series design verification/validation and ISO 10007 configuration audit; for activity guides and further detail, 61B points to **GEIA-HB-649, Configuration Verification and Audits Function**.
- **Acquisition strategy** — whether the buy is performance-based or detail-design-based governs who conducts the PCA and how audit certifications are applied.

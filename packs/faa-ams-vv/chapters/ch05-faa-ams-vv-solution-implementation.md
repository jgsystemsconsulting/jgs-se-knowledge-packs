# Chapter 5 — V&V in Solution Implementation

## Core Idea

Solution Implementation (SI) is the phase where the FAA actually builds, buys, tests, and fields the chosen solution. Its overarching purpose is to satisfy user requirements and realize the benefit targets that the program's Business Case promised. Verification and validation (V&V) during SI exists to keep that promise honest: as the program moves from contract award through to fielding, V&V continuously confirms that the products, product components, and their associated work products genuinely match what was committed to and will perform as intended.

The phase opens by revalidating the plans and baselines carried over from Final Investment Analysis. After (or around) contract award, those baselines are checked — and updated when needed — typically through the FAA Integrated Baseline Review (IBR) process, so they can credibly act as the management construct for running the program. From there, SI runs as seven major activities: finalize program planning, obtain the solution, verify operational readiness, prepare for the In-Service Decision, update planning for In-Service Management (ISM), make the In-Service Decision, and deploy the solution to all sites. V&V is woven through these activities, with developmental and operational testing as the workhorses, so that the data feeding the In-Service Decision is accurate and complete.

## Frameworks Introduced (exact source names, when/how)

The slice anchors SI V&V in the FAA's own acquisition machinery and names the specific instruments used at each gate:

- **FAA Acquisition Management System (AMS)** — the governing policy framework. AMS policy defines the lifecycle, the decision points, and the stakeholder roles; the guidelines note that Table 5's content reflects AMS policy as published and that detailed SI templates and guidance should be consulted for current direction.
- **FAA Integrated Baseline Review (IBR)** — introduced as the process through which post-award plans and baselines are revalidated, so they can serve as the program's management construct.
- **Developmental Testing (DT) and Operational Testing (OT)** — named as the primary means by which products and their components are verified and validated, alongside Independent Operational Assessment (IOA) as part of the major V&V activities at acceptance.
- **Preliminary Design Review (PDR) and Critical Design Review (CDR)** — introduced as technical milestones that are also structured V&V opportunities: PDR against the system/service allocated baseline and CDR against the product baseline.
- **Test and Evaluation Master Plan (TEMP)** — appears as a key work product subject to V&V (the final TEMP), verified against the Test and Evaluation Handbook, the TEMP template, and AMS Policy.
- **FAA Safety Management System (SMS)** and the **Safety Risk Management Document / System Safety Assessment Report** — introduced at the acceptance and In-Service decisions as the basis for verifying and validating that safety obligations are met.
- **System Security Authorization** and the **Security Authorization Handbook** — introduced at the security gate, validated via a Plan of Actions and Milestones (POA&M) and verified against the handbook and AMS Policy.
- **In-Service Review Checklist** — introduced as the instrument whose completed entries (issues, action plans, remarks) are validated against the associated checklist questions, with the checklist template as the verification reference.

These are not abstractions in the slice — each is tied to a concrete decision point in Table 5, with named criteria and named responsible stakeholders.

## Key Concepts

**The decision-point spine.** Table 5 organizes SI V&V around a sequence of gates: Contract Award; the Product Demonstration Decision (if required); Product Acceptance / Contractor Acceptance and Inspection (CAI); the Production Decision (if required); and the In-Service Decision. At each gate the table specifies four things in lockstep — the decision point, the minimum work products / components / products that must be V&V'd, the criteria they are V&V'd against, and the stakeholder responsible.

**Validation criteria vs. verification criteria are kept distinct.** For every gate, the source separates *validation* references (the authoritative requirements and intent the artifact must satisfy — e.g., the Final Program Requirements Document, the Business Case, the Acquisition Program Baseline, the Solution Concept of Operations) from *verification* references (the templates, handbooks, and policy used to confirm the artifact is correctly formed — e.g., the Statement of Work template, the DD Form 1423-1 and DD Form 1664 templates, the System Specification template, the TEMP template, the Test and Evaluation Handbook).

**Contract Award.** The contract itself is subject to V&V, including the updated Statement of Work, the updated Contract Data Requirements List / Data Item Descriptions, and the updated System Specification. Validation is against final program requirements, the implementation strategy and planning document, and the results of negotiations with the contractor; verification uses the SOW, DD-form, and System Specification templates. Responsibility sits with the Service Team (functional organizations such as systems engineering and test & evaluation) together with the Contracting Officer.

**The final TEMP gate.** The final Test and Evaluation Master Plan is V&V'd against the final implementation strategy and planning document, final program requirements, the final Business Case, the Acquisition Program Baseline, the updated SOW and CDRL/DIDs, and the V&V results from the initial TEMP — verified against the Test and Evaluation Handbook, TEMP template, and AMS Policy. This gate brings in the Investment Analysis Team and the ANG-E Test Standards Board.

**Product Demonstration Decision.** Contract specifications (decomposed from the FAA System Specification) and design documents are the artifacts. Validation traces specifications back to the FAA System Specification and design back to the contractor system specification and contract; verification uses the Data Item Description from the contract for both specifications and design documents.

**Acceptance and the In-Service Decision.** At CAI / Production Decision / In-Service Decision, the major V&V activities explicitly include DT, OT, and IOA. The system/service is validated against the Final Program Requirements Document (including Critical Operational Issues and Critical Performance Requirements) and the Solution Concept of Operations, and verified against the system specification and lower-level specifications. Safety and security are first-class concerns here: the Safety Risk Management Document / System Safety Assessment Report is validated against prior safety assessments, the ConOps, and final requirements, and verified through the FAA SMS; the System Security Authorization is validated via the POA&M and verified against the Security Authorization Handbook and AMS Policy. The completed In-Service Review Checklist closes the phase. Responsibility broadens to include the ATO Office of Safety and Technical Training and the Information Systems Security Manager alongside the Service Team.

## Mental Models

**Two questions at every gate.** Validation asks "is this the right thing — does it satisfy user requirements and the Business Case benefits?" Verification asks "is the thing built right — does it conform to its specification and template?" The slice's strict split of validation criteria from verification criteria at each decision point is the operational embodiment of that pairing.

**The baseline staircase.** PDR sits against the allocated baseline; CDR sits against the product baseline. Design reviews are not just engineering ceremonies — they are scheduled V&V opportunities where a baseline is examined as a whole, so the program climbs from allocated to product baseline with each step verified.

**Testing as the evidence engine.** Decisions are only as trustworthy as the data behind them. DT, OT, and IOA generate that evidence, but the plans, procedures, and reports that surround the tests are themselves V&V'd first — because if the test artifacts are wrong, the In-Service Decision is built on bad data.

**Validate the baselines before you manage to them.** Revalidating Final Investment Analysis plans through the IBR at the start of SI is a "check the ruler before you measure" move: the baselines have to be realistic before they can serve as the management construct for the rest of implementation.

**Responsibility follows risk.** As the gates progress from contract to fielding, the responsible-stakeholder column accretes specialists — Contracting Officer at award, Investment Analysis Team and Test Standards Board at the TEMP gate, then Safety/Technical Training and the Information Systems Security Manager as safety and security stakes rise toward the In-Service Decision.

## Key Takeaways

- SI's reason for being is to satisfy user requirements and hit the Business Case benefit targets; V&V is the mechanism that keeps the delivered solution accountable to both.
- Post-award, revalidate Final Investment Analysis plans and baselines (typically via the IBR) before treating them as the program's management construct.
- The phase runs as seven activities from finalizing planning through deploying to all sites, with V&V concentrated on the products, components, and work products those activities produce.
- Developmental and operational testing (with IOA at acceptance) are the primary V&V methods; the surrounding plans, procedures, and reports must themselves be V&V'd so the In-Service Decision rests on accurate, complete data.
- Table 5 is the operational core: for each decision point it fixes the minimum artifacts, the V&V criteria, and the responsible stakeholder — and consistently separates validation references from verification references.
- PDR and CDR double as structured V&V events against the allocated and product baselines respectively.
- Safety (via the FAA SMS and Safety Risk Management documentation) and security (via System Security Authorization and the POA&M) are explicit, gated V&V obligations approaching the In-Service Decision.
- Table 5 reflects AMS policy as published; current SI templates and detailed guidance should be consulted for authoritative direction.

## Connects To

- **Final Investment Analysis (prior phase):** SI inherits its plans, baselines, Business Case, and program requirements from Final Investment Analysis and revalidates them through the IBR — the V&V handoff between the two phases.
- **In-Service Management (ISM, next phase):** activity 5 of SI updates planning for ISM, and the In-Service Decision is the gate that transitions the fielded solution into sustainment.
- **Test & Evaluation discipline:** the TEMP, Test and Evaluation Handbook, and the DT/OT/IOA activities tie SI V&V directly to the FAA's test-and-evaluation framework and the ANG-E Test Standards Board.
- **Design reviews:** PDR and CDR connect SI V&V to the engineering baseline progression (allocated → product), shared with broader systems-engineering review practice.
- **Safety and security assurance:** the FAA SMS, Safety Risk Management documentation, System Security Authorization, and POA&M connect SI V&V to the agency's safety-management and security-authorization regimes.
- **AMS governance:** every gate and stakeholder role traces back to FAA AMS policy, which remains the authoritative source over the snapshot captured in Table 5.

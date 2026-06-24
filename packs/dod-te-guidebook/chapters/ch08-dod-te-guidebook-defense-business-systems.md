# Chapter 8 — T&E in the Defense Business Systems (DBS) Pathway

> Source caveat: this chapter is a paraphrase of an **open-publication** DoD T&E source (Distribution A, approved for public release, unlimited distribution). It is grounded entirely in the Defense Business Acquisition chapter of the T&E Enterprise Guidebook; no verbatim runs are reproduced.

## Core Idea
The Defense Business System (DBS) pathway acquires business capabilities — finance, contracting, logistics, HR, planning, training, readiness — by rapidly delivering useful, affordable subsets of capability, often built on commercial or government off-the-shelf software. The central T&E message is that buying COTS/GOTS does **not** remove the need for independent government test and evaluation: integrating commercial software into the DoD environment is non-trivial, so development and test activities are still required. T&E is structured around the five-phase **Business Capability Acquisition Cycle (BCAC)**, whose phase boundaries are each marked by an **Authority to Proceed (ATP)** decision, and those decisions draw on test measures and reports that judge whether the program is ready to advance.

## Frameworks Introduced
- **Defense Business System (DBS) Acquisition Pathway** — established by **DoDI 5000.75** under the authority of **DoDI 5000.02**; applies to defense business capabilities including "as-a-service" solutions, and may also be used for non-developmental, software-intensive programs and IT infrastructure.
  - When/how: the governing pathway for any business-capability acquisition; T&E guidance here supports policy in **DoDI 5000.89** (T&E policy) and **DoDI 5000.75**, with policy documentation taking precedence in any conflict.
- **Business Capability Acquisition Cycle (BCAC)** — the five-phase cycle the DBS pathway runs on. The phases are: identifying the capability need; analyzing solutions; planning the functional requirements and the acquisition; then acquisition, test, and deployment; and finally capability support.
  - When/how: each phase opens with an ATP decision point informed by test evidence; the bulk of DT and OT events occur in phase 4.
- **Authority to Proceed (ATP) decision points** — gate decisions including the Solution Analysis ATP, Functional Requirements ATP, Acquisition ATP, Limited Deployment ATP(s), Full Deployment ATP, and Capability Support ATP.
  - When/how: each ATP is informed by test measures/reports judging readiness to proceed; the MDA (with the functional sponsor) approves deployment scope at the deployment ATPs.
- **Test and Evaluation Working-level Integrated Product Team (T&E WIPT)** — the cross-stakeholder team that plans all T&E products and events and owns the integrated schedule.
  - When/how: includes systems engineering, DT&E, OT&E, the functional lead, interoperability evaluator, cybersecurity, product support, the Intelligence Community, and certification authorities; ensures requirements are measurable, testable, achievable, and relevant, and that T&E needs flow into RFPs and contracts.
- **Test and Evaluation Master Plan (TEMP), or similar strategic document** — the agreement between the PM and all T&E stakeholders covering roles, resources, data requirements, and the processes for testing and evaluating technical, functional, and operational performance.
  - When/how: developed by the PM with T&E WIPT support; the initial version is generated in the Functional Requirements phase; when a program falls under OSD T&E oversight a TEMP is mandatory and **DOT&E holds final approval**, with submission required at least 45 calendar days ahead of the decision it supports.
- **Integrated Decision Support Key (IDSK)** — per DoDI 5000.89, a table in the TEMP mapping acquisition, technical, and program decisions to the CT/DT/OT data needed to support them.
  - When/how: provides a framework for how test events build on one another, lets multiple stakeholders' evaluations draw from the same events, and evolves to incorporate operational realism as early as possible — without replacing dedicated DT&E or OT&E.
- **Capability Implementation Plan (CIP)** — the major DBS planning document that aggregates the information products needed to manage capability delivery; the TEMP (or similar strategic document) sits inside the CIP's technical-management content.
  - When/how: the CIP is not a single fixed document; for programs not under DOT&E oversight, a TEMP-equivalent may be a component of the CIP.
- **Failure Definition and Scoring Criteria (FDSC)** — TEMP content (added around contract award) defining defect cause categories, what counts as a failure affecting availability, what constitutes a downing event and restoral, and what makes a mission failure.
  - When/how: paired with defect severity definitions (e.g., IEEE Std 12207.2, Annex J) and software-maturity metrics (defect aging, defect density, function point analysis).

## Key Concepts
- **The five BCAC phases and their T&E posture:**
  - *Capability Need Identification* — early capability requirements, attributes, and performance measures (with threshold/objective values) are developed. No specific T&E activities, but testers engage early to understand functional needs and ensure testability and appropriate metrics.
  - *Solution Analysis* — opens with the Solution Analysis ATP; the DT&E lead and Operational Test Agency (OTA) build understanding of planned business-process changes to scope test events, and provide input to initial CIP development.
  - *Functional Requirements and Acquisition Planning* — opens with the Functional Requirements ATP (decides whether a business system is acquired and begins its acquisition). T&E ensures requirement testability, participates in RFP development, and generates the initial TEMP/strategic document.
  - *Acquisition, Testing, and Deployment* — where most DT and OT occur; spans the Acquisition ATP, Contract Award, Limited Deployment ATP(s), and Full Deployment ATP.
  - *Capability Support* — opens with the Capability Support ATP, where the functional sponsor accepts full deployment and transitions to support; risk-based OT events (e.g., OAs) and cyber assessments are conducted as needed.
- **Independent government T&E is mandatory even for COTS/GOTS** — CT, DT&E, and OT&E should be woven together, made lean, and automated as far as is practical; test and certification organizations should pursue sharing, reciprocity, availability, and reuse of results and artifacts.
- **Shared evidence base and data repository** — when the program kicks off, the PM stands up a common test-data store that every test team can read from, draw on, and feed into; this enables sequential testing, big-data analytics, and adaptive T&E. The OTA maintains the authoritative record of data that may meet OT&E requirements.
- **Collaborative test data scoring boards** — the T&E WIPT may stand these up to evaluate and authenticate available/integrated test data for potential to satisfy IOT&E data requirements.
- **Functional Sponsor / functional lead and user involvement** — user participation is critical; some DBS programs have a Functional Sponsor at a level equal to the PMO, others have weaker user organizations. The test lead works to fold users into the test strategy and ensure availability for mission-oriented DT and OT.
- **TEMP resource categories** — test articles (system under test, interfacing systems, cyber threats), facilities/instrumentation/ranges (including cyber ranges and software integration labs), automated testing tools, M&S with V&V plans, manpower/personnel, federal/state/local and range requirements, projected/actual funding (a DT&E/OT&E resource table is required per Section 839(b) of Public Law 115-91), and the shared data repository.
- **Government test capability preference** — programs should use government T&E capabilities unless a cost-effective exception is justified; PMs perform a cost-benefit analysis and secure sign-off via the TEMP review/approval route before turning to non-government facilities.
- **DT&E events for the Limited Deployment ATP** — mission-based cybersecurity risk assessments (run early once attack surfaces are defined), vendor DT (unit and integration testing), interface and interoperability testing (preferably against interfacing systems' test environments, not production), Cybersecurity Vulnerability Identification (CVI), data migration testing for legacy replacement, **Business Operations Testing (BOT)** as mission-oriented DT with actual users, **Adversarial Cybersecurity DT (ACDT)** run with red teams and cyber defenders, and scalability testing for large user populations.
- **OT&E and the deployment ATPs** — for Limited Deployment, the OTA performs a risk assessment and **level-of-test determination** (Level 2 or below vs. Level 3) submitted to DOT&E for approval; for Full Deployment the OTA executes an **IOT&E** using a DOT&E-approved plan, which is by definition a Level 3 event (so no formal risk assessment is needed). Where a system sits under DOT&E oversight, an IOT&E report must precede the Full Deployment ATP.
- **FOT&E** — if directed by DOT&E, Follow-on OT&E runs after full deployment but before Capability Support, confirming the system remains operationally effective, suitable, cyber survivable, and supportable.
- **Approval authorities** — DOT&E is final TEMP approver for oversight programs; within a BCAT I TEMP the DT&E plan is approved by the MDA.

## Mental Models
- **ATP-gated, evidence-fed pipeline:** every phase boundary is an ATP, and each ATP is a knowledge gate fed by test measures and reports. If you cannot name the ATP a test event supports, you have not connected the test to a decision.
- **Buying off-the-shelf shifts the work, it does not delete it:** COTS/GOTS reduces development but raises integration risk — independent government T&E is the mechanism that surfaces that integration risk before deployment.
- **Walk the deployment ladder:** DT → Limited Deployment ATP → OT (risk-based level) → DT for Full Deployment → IOT&E → Full Deployment ATP → (optional FOT&E) → Capability Support. Limited deployment can mean *all capabilities to few users* or *few capabilities to many users*, and that scope drives the OT level.
- **The IDSK is the wiring diagram for reuse:** instead of each evaluator running its own siloed events, the IDSK maps decisions to data so one test event can serve several evaluations — efficiency through shared evidence, never through deleting dedicated DT&E or OT&E.
- **Embed OT&E early:** putting OT awareness into systems engineering and development lets the OTA judge which developmental data is trustworthy enough to reuse for operational evaluation, mapping prior data to assessment areas and identifying gaps that drive future test planning.
- **Operational realism early is cheaper:** introducing operational users and mission environments early raises the odds of catching problems while fixes are still affordable, before redesigns become expensive or infeasible.
- **The contract is a T&E instrument:** if access to vendor test events, tools, data repositories, and environments — plus fix-before-acceptance obligations — is not written into the RFP and contract, the government has no leverage to get the data its evaluations need.

## Anti-patterns
*The source does not enumerate a labeled "anti-patterns" list. The following are practices the text explicitly warns against, paraphrased as failure modes:*
- **Assuming COTS/GOTS removes the need for government T&E** — the source states plainly that off-the-shelf use does not eliminate independent government T&E because DoD integration is non-trivial.
- **Interoperability testing on production environments** — flagged as limited by the risk of accidentally executing real-world transactions or corrupting operational databases; testing against interfacing systems' test environments is preferred.
- **Replacing dedicated DT&E/OT&E with reused data** — the IDSK/shared-evidence approach may rescope individual events but is explicitly not a substitute for dedicated developmental or operational test.

## Key Takeaways
1. The DBS pathway (DoDI 5000.75) runs the five-phase **BCAC**, with each phase gated by an **ATP** that is informed by test evidence.
2. **Independent government T&E remains mandatory for COTS/GOTS** acquisitions — off-the-shelf software shifts effort toward integration testing rather than eliminating test.
3. The **T&E WIPT** plans all T&E products/events, owns the integrated schedule, and pushes T&E requirements into RFPs and contracts so the government can access vendor test data.
4. The **TEMP (or similar strategic document)** is the stakeholder agreement; for oversight programs **DOT&E is the final approver** and it is due 45 days before the supported decision; the **MDA** approves the DT&E plan in a BCAT I TEMP.
5. The **IDSK** maps decisions to CT/DT/OT data, enabling shared evidence and event reuse without replacing dedicated DT&E or OT&E.
6. Phase 4 carries most testing: DT&E (including BOT, ACDT, CVI, migration, interface, and scalability tests) supports **Limited Deployment ATP(s)**, and **IOT&E** (a Level 3 event on a DOT&E-approved plan) supports the **Full Deployment ATP**.
7. The OTA performs a **risk-based level-of-test determination** for limited deployments (approved by DOT&E) and maintains the authoritative record of data eligible for OT&E in a **shared data repository**.
8. **User/Functional Sponsor involvement** and **operational realism introduced early** are central to credible, affordable DBS testing.

## Connects To
- **DoDI 5000.75 / DoDI 5000.02 / DoDI 5000.89:** the governing pathway and T&E policy this chapter implements; DoDI 5000.73 governs the cost estimate that must fund the TEMP's T&E resources.
- **Cyber T&E Companion Guide:** referenced for cybersecurity vulnerability identification (CVI) and cyber survivability assessment detail.
- **Other T&E Enterprise Guidebook focus-area chapters:** the TEMP must align with relevant focus-area chapters; cyber survivability is assessed in a mission context throughout.
- **IEEE Std 12207.2 (Annex J):** cited as a source for defect severity definitions feeding the FDSC.
- **`dau-se-guidebook` pack:** verification vs. validation, technical reviews, and baseline discipline that underpin the DT-to-OT progression seen here.
- **`gao-tra` pack:** technology/readiness assessment thinking that parallels the evidence-fed ATP gates.

# Chapter — T&E in the Software Acquisition Pathway

> Source caveat: this chapter synthesizes Chapter 5 ("Software Acquisition") of the DoD Test and Evaluation Enterprise Guidebook, cleared for open publication (Distribution Statement A, approved for public release). It is a headline open-source T&E reference, so the framing here can be cited and shared freely.

## Core Idea

The Software Acquisition Pathway exists to deliver software capability fast — the first usable, effective increment must reach operations no more than one year after funds are obligated, and new capability is expected to ship at least annually after that, ideally more often. That speed reshapes what testing must look like. Test and evaluation can no longer be a downstream gate bolted onto a finished product; it has to become a continuous, embedded activity that keeps pace with iterative development (Agile, DevSecOps) without becoming the bottleneck that breaks the cadence.

The chapter's organizing logic follows the pathway's two phases. In the **Planning Phase**, test teams help shape the acquisition documents and stand up the infrastructure, tools, and data plumbing so that later testing is even possible — this is where the conditions for success are set. In the **Execution Phase**, contractor and independent government testers run continuously against a stream of small increments, accumulating evidence that supports both developmental and operational evaluations. Two distinct testing tracks run through Execution: testing *throughout* development (every iteration) and testing *of individual releases* (the increments actually fielded). The whole scheme depends on a single recurring device — a **shared body of evidence** in a common data repository — so that data captured once, by anyone, can be reused by all parties for their own independent evaluations rather than re-tested.

The guidance applies to both branches of the pathway: the **Applications path** (software on commercial or cloud hardware) and the **Embedded Software path** (upgrades to software inside weapon systems and other military-unique hardware). For embedded software, T&E must align with the testing of the host system the software lives in.

## Frameworks Introduced (exact source names, when/how)

- **Software Acquisition Pathway (Planning Phase / Execution Phase)** — the two-phase lifecycle governed by DoDI 5000.87 that the entire chapter scaffolds T&E onto. Planning sets conditions; Execution is where programs spend most of their life, cycling through "plan, code, build, test."

- **T&E Strategy** — the high-level test planning document for the pathway, written during Planning by the PM with the T&E WIPT and approved by the Decision Authority before Execution (DOT&E is final approver for programs on oversight). It functions as a contract among the PM and all T&E stakeholders for roles, responsibilities, and resources, and it must stay aligned with the current Capability Needs Statement.

- **Test and Evaluation Working-level Integrated Product Team (T&E WIPT)** — the cross-organization team the PM should charter during Planning to coordinate top-level test-event planning, help evaluate results, and manage the T&E program across the lifecycle. Members span systems engineering, the Lead DT Organization, Chief Developmental Tester, the Operational Test Agency (OTA), DOT&E and D,DTE&A (for programs on the respective oversight), the cybersecurity lead, interoperability evaluator, Capability Owner, and certification authorities. Roles are captured in a T&E WIPT Charter.

- **Minimum Viable Product (MVP)** — an early software version fielded to users for evaluation and feedback that shapes scope, requirements, and design; explicitly *not* intended for operational use. Treated as essentially a developmental evaluation, so the PM or government developmental testers are the natural leads.

- **Minimum Viable Capability Release (MVCR)** — the first set of features fit to be fielded operationally and deliver warfighter value, which must reach an operational environment (with appropriate operational test) within one year of funds being obligated. If an MVP proves sufficient for operational use, it can become the MVCR.

- **Value Assessment** — an annual review by the sponsor and user community of whether delivered software produced mission improvement or efficiencies worth the investment; informed by T&E results, and it satisfies the Post-Implementation Review (PIR) requirement of DoDI 5000.82.

- **Integrated Decision Support Key (IDSK)** — named from DoDI 5000.89 as the integrated-testing construct the T&E Strategy uses to describe the test events and activities that produce the data needed for acquisition, technical, and program decisions.

- **Shared body of evidence / data repository** — a secure repository the PM stands up in Planning so all test teams can review, contribute, and reuse test data; the OTA maintains the authoritative data for OT&E.

- **Product Roadmap** — a rolling, calendar-based product schedule derived from the CNS that breaks capability into epics and features, giving testers a forward view (near-term 10–12 weeks out to 12–18 months) of what will be built and when, so test planning can track it.

- **Pipeline / Software Factory** — the orchestration infrastructure. A pipeline moves code from development to production like an assembly line; a software factory holds multiple pipelines and automates the DevSecOps develop/build/test/release/deliver activities with minimal human intervention.

- **Test-environment ladder (Sandbox, Dev, Integration, Test/QA, Pre-Production/staging, Production)** — the named environments inside the pipeline where different testing happens, escalating in fidelity to production.

- **Test-Driven Development (TDD), Behavior-Driven Development (BDD), Acceptance Test-Driven Development (ATDD)** — the three early-test development techniques compared in Table 3. The chapter explicitly directs government testers to concentrate on BDD and ATDD. BDD/ATDD use the **Given-When-Then** format (with optional "AND" clauses).

- **Cyber T&E / Cyber Working Group / Mission Based Cyber Risk Assessment (MBCRA) / continuous Authority to Operate (cATO)** — cybersecurity testing runs through every phase, cooperative and adversarial; the Cyber Working Group (a subset of the T&E WIPT) drives automated cyber testing and continuous monitoring toward a cATO. For depth, the chapter points readers to two dedicated references: its Cyber T&E Focus Area, and the companion Cyber T&E guide.

- **Operational evaluation events — Operational Assessment (OA), Initial Operational Test and Evaluation (IOT&E), risk-informed OT&E** — the operational-test products aligned to deployment decisions: a risk-appropriate OA typically supports each limited deployment, an IOT&E supports the MVCR, and follow-on releases use risk-informed scoping.

- **Verification, Validation, and Accreditation (VV&A)** — applied by the OTA to any automated test capability, virtual environment, or pre-production environment whose data will feed operational evaluations.

## Key Concepts

**Early and continuous involvement.** The pathway's defining T&E discipline is showing up early — in Planning, while the CNS, User Agreement, Acquisition Strategy, Cost Estimate, IP Strategy, and RFP are still being written — and staying embedded through every Execution iteration. Test teams are told to be involved "up front" so they actually get the data they need out of the development process rather than discovering gaps too late.

**Get it into the contract or you won't get it.** The chapter is blunt that the RFP defines what the government receives from the contractor, and if a need is not in the RFP and the resulting contract, it will not materialize. So testers must use the RFP and IP Strategy to lock in government access to: the contractor's test events, M&S, tools, data repositories, and environments; the contractor's own test plans, procedures, reports, and data; the contractor's support to government-run testing; and ownership of the test data generated, so it can feed the shared body of evidence.

**Division of testing labor.** Development teams lead the low-level tests (unit tests); independent government test teams lead integration and acceptance testing. All of it lands in the shared body of evidence for independent evaluation. Government testers strive to keep release-testing tempo in sync with developers by automating functional, performance, and regression testing.

**Embedding OT&E without doing development.** Operational testers embed in the development pipeline — via electronic and physical presence — to gain continuous visibility, but embedding explicitly does *not* mean OT&E writes the software. Embedded OTA work includes monitoring pipeline tests to trust their veracity (and VV&A'ing automated capabilities that will support operational evaluations), helping define end-to-end mission-thread test requirements, establishing test-process pedigree, and watching deployments to production. For every increment, even ones not meant for fielding, the OTA observes to judge whether the data is usable for OT&E and to spot gaps for future iterations.

**Environment fidelity governs evaluation validity.** Data meant to support operational evaluation must come from an operationally representative environment; where the environment falls short, the limitations have to be enumerated and the evaluation framed by the context in which the data was generated. The Test environment should mirror production as closely as possible (including monitoring and realistic usage), and where real interfaces or platforms can't be reproduced, M&S stands in — common for weapon systems and long-build-time hardware. The OTA VV&As pre-production environments and tools before Execution begins.

**Automation is non-negotiable at scale.** The volume of software and testing is too large for manual testing alone; continuous integration and delivery cannot happen without automated T&E. Automated tools split into **test management** (planning, scheduling, tracking, reporting) and **test execution** (running cases against the system under test). Government testers should learn the contractor's tools — using the same tools eases event replication — and any tool whose output supports OT&E must be independently VV&A'd.

**Risk-informed scoping after the MVCR.** Programs spend the majority of their lifetime in risk-informed OT&E once the MVCR is fielded. The MVCR's IOT&E sets the baseline; subsequent releases may need less dedicated OT&E depending on release complexity, amount of new capability, and number of new users. The OTA decides whether to re-include previously tested capabilities based on their interaction with new capability and the mission risk if they fail.

**The Given-When-Then specification.** BDD frames tests around the behavior of a class of user stories that yields user value: GIVEN the preconditions, WHEN an action occurs, THEN the expected results follow (with optional AND clauses). ATDD reuses this format at a higher, customer-experience altitude.

**Post-release monitoring as evidence.** Once software is fielded, PMs feed testers production telemetry — uptime/downtime and time-to-repair, hardware/service/application error reports, help-desk problem reports and closures, and cybersecurity monitoring — which testers fold into the shared body of evidence to support ongoing independent assessment and to scope future testing.

## Mental Models

- **Testing as a continuous line, not a gate.** The chapter's "Continuum of Test" picture (Figure 5) places test types along an axis from more-frequent/lower-level (sprint unit and feature testing) to less-frequent/higher-fidelity (system integration, capability-release, pre-prod, operational), all draining into one shared evidence pool. Think of evaluation as something that accrues continuously, not a milestone you arrive at.

- **The environment ladder = a fidelity gradient.** Sandbox → Dev → Integration → Test/QA → Pre-Production → Production is a climb from isolated experimentation toward production reality. Each rung answers a different question, and the higher the rung, the more its data can support operational conclusions.

- **TDD / BDD / ATDD as three altitudes of the same question.** The chapter cites the framing that TDD asks whether we are building the thing right, BDD asks whether the thing behaves as it should, and ATDD asks whether we are building the right thing at all. Government testers should live at the BDD/ATDD altitudes, closer to user value and mission outcome.

- **The shared body of evidence as a reuse engine.** The mental shift is from "each organization runs its own confirmatory test" to "capture once, reuse everywhere." Maximum sharing, reciprocity, and reuse of results and artifacts across testing and certification bodies is framed as a precondition for success, not a nicety.

- **MVP vs. MVCR as a fielding threshold.** The MVP is a feedback instrument that never goes operational; the MVCR is the first thing real warfighters use. Crossing that threshold flips testing from developmental-style learning to full effectiveness/suitability/survivability evaluation — and if an MVP is ever promoted to MVCR, the test scope must expand to match the consequences of fielding something defective.

- **"Embedded but not developing."** Picture the operational tester sitting inside the factory with full visibility, instrumented to observe and judge data pedigree — but with hands off the code. Visibility is the asset; independence is the constraint.

## Anti-patterns

The source does not enumerate a formal "anti-patterns" list, but it explicitly names a few failure conditions to avoid:

- **Leaving requirements out of the RFP/contract.** The chapter states plainly that anything not in the RFP and resulting contract will not be delivered — so omitting government test access, data rights, or contractor test deliverables is a self-inflicted wound.
- **Over-elaborating the roadmap into the distant future.** The notional roadmap (Figure 4) carries the explicit caution not to over-elaborate features far into the future; detailed planning of distant increments is wasted against a roadmap that is expected to change.
- **Treating the Value Assessment as a substitute for operational testing.** The chapter twice stresses that the annual value assessment does not replace OT&E and does not require separate T&E events — it consumes T&E data, it does not stand in for testing.
- **Skipping the baseline for value measurement.** A proper value assessment requires capturing baseline "value" data on the legacy system *before* the new software is developed; without that pre-implementation baseline, the post-implementation comparison cannot be made.

## Key Takeaways

1. Speed is the forcing function: first effective capability within a year of funding, then annual-or-faster deliveries — and T&E must be continuous and automated to keep up.
2. The Planning Phase is where T&E either wins or loses. Shape the documents, lock data access into the RFP and IP Strategy, and stand up the infrastructure, tools, and shared data repository before Execution starts.
3. The T&E Strategy is the keystone artifact — a stakeholder contract that defines the integrated test approach (via the IDSK), the data and resources required, and how evidence accumulates; the Decision Authority (or DOT&E on oversight) approves it before Execution.
4. One shared body of evidence underpins everything: capture data once, reuse it for independent developmental and operational evaluation, with the OTA holding the authoritative OT&E data.
5. Government testers should lean into BDD and ATDD (Given-When-Then), staying at the behavior and customer-experience altitudes closest to mission value.
6. MVP is for learning and feedback (not operational use); MVCR is the first operational fielding and triggers an IOT&E; after MVCR, OT&E becomes risk-informed and consumes most of the program's testing life.
7. Cybersecurity testing runs through every phase — cooperative and adversarial, covering the pipeline and supply chain — driven by a Cyber Working Group toward a continuous ATO.
8. Operational testers embed for visibility but never develop the software, and any automated capability or environment feeding operational conclusions must be VV&A'd.
9. Post-release production monitoring is legitimate evidence and should be folded back into the shared body of evidence and used to scope future testing.

## Connects To

- **DoDI 5000.87 ("Operation of the Software Acquisition Pathway")** — the governing instruction this chapter operationalizes for T&E; source of the MVP, MVCR, product roadmap, value assessment, and user-role definitions.
- **DoDI 5000.89 (T&E policy)** — origin of the Integrated Decision Support Key (IDSK) and the integrated-testing approach the T&E Strategy must align to; also the risk-appropriate OA expectation for limited deployments.
- **DoDI 5000.82 (IT acquisition)** — the Post-Implementation Review requirement that the annual Value Assessment satisfies.
- **DoDI 5000.73 (Cost Analysis Guidance and Procedures)** — basis for the Cost Estimate that must account for T&E resources.
- **DoD Enterprise DevSecOps Fundamentals (DoD CIO)** and its library (playbooks, reference designs, the DevSecOps Tools and Activities document) — the methods/tools reference for pipelines and software factories.
- **DAU Agile resources** — Agile 101 Primer, the Agile Software Acquisition Guidebook, and ACQ-1700 — for Agile concepts, epics/features/user stories, and the roadmap framing.
- **Cyber T&E Focus Area; Cyber T&E Companion Guide** — the two deep references for cooperative/adversarial cyber testing, software assurance, MBCRAs, and cATO.
- **Modeling and Simulation Focus Area** — for VV&A of M&S used to represent hard-to-replicate environments and interfacing systems.
- **JCS Cyber Survivability Endorsement and Implementation Guide** — usable to define cyber attributes in the CNS even though the pathway does not require JCIDS.
- **Other chapters in this pack** — connects to the broader T&E Enterprise Guidebook treatment of DT&E, OT&E, integrated testing, and the roles of DOT&E, D,DTE&A, OTAs, and the T&E WIPT across all acquisition pathways.

# Chapter — T&E Strategy and Documentation (T&E Strategy, TEMP, SAMP, Test Plans)

> Source caveat: This chapter is a paraphrased synthesis of an openly published DoD Test and Evaluation (T&E) Enterprise Guidebook section ("T&E Documentation"). It is a headline open T&E source — authoritative for the structure and intent of DoD T&E planning, but it points outward to controlling instructions (the DoDI 5000-series) and to live reference systems (the Milestone Document Identification site) for binding detail. Treat the named documents and approval authorities as the practical anchor; treat exact thresholds and statutory citations as pointers to verify against the current instructions, not as quotations.

## Core Idea

T&E planning exists to convert a fuzzy understanding of what users need into an executable, credible approach for demonstrating that the delivered system actually meets those needs — technically, functionally, and operationally. The planning stage is where success is won or lost: it sets the conditions for everything downstream. The central artifact is the **T&E Strategy**, a single planning document that, regardless of what a given acquisition pathway calls it, serves as the negotiated agreement between the Program Manager (PM) and every T&E stakeholder about tasks, roles, resources, and responsibilities. The Strategy does not stand alone — it is woven from a web of upstream acquisition documents (requirements, threat assessments, engineering plans, protection plans, cost and sustainment artifacts), and it is decomposed downstream into event-level test plans. The whole apparatus is meant to be built early, kept living across the lifecycle, and increasingly digitized so testing can feed continuous development, integration, and delivery.

## Frameworks Introduced (exact source names, when/how)

- **T&E Strategy** — the principal T&E planning deliverable across all six acquisition pathways. Written by the PM in coordination with the T&E Working-level Integrated Product Team (T&E WIPT). Developed during the planning phase — early enough to shape the contract — then revised as the program needs across its acquisition life cycle. The source treats "T&E Strategy" as a pathway-agnostic umbrella term whose common instances include the TEMP, the SAMP, a "test strategy," and the literal "T&E Strategy" name.
- **TEMP (Test and Evaluation Master Plan)** — named as one common form a T&E Strategy takes, depending on pathway and naming convention.
- **SAMP** — named alongside TEMP as another common naming variant of the T&E Strategy.
- **Test Plans** — developed by the lead test organization in coordination with the T&E WIPT, one per event identified in the T&E Strategy. Introduced in the source's "Test Plans" subsection as the execution-level decomposition of the Strategy.
- **Integrated Decision Support Key (IDSK)** — required content of the T&E Strategy per DoDI 5000.89; ties program decisions to the data requirements and data sources (continuous test, developmental test, live-fire test, operational test, modeling and simulation) that feed them, and correlates those data needs to critical operational issues and technical requirements.
- **DoDI 5000.89** — the governing T&E policy the Strategy must align to; mandates inclusion of the IDSK.
- **T&E Enterprise Guidebook (and its T&E focus-area chapters)** — the reference the Strategy is expected to align with alongside the Acquisition Strategy and T&E policy.
- **Milestone Document Identification (MDID) website** — the live reference system for the supporting documents; gives each document's definition, statutory/regulatory notes, source documents, and approval authority, and lets users filter by program type, life-cycle event, source, and keyword.
- **Supporting documentation set (Table 1)** — the named upstream artifacts the T&E community must engage to inject T&E content. As named in the source: JCIDS documentation; Analysis of Alternatives (AoA, per DoDI 5000.84); Validated Online Life Cycle Threat (VOLT); Acquisition Strategy; Systems Engineering Plan (SEP); Program Protection Plan (PPP, per DoDI 5000.83); Cybersecurity Strategy (per DoDI 8500.01); Security Plan (per DoDI 8510.01, RMF); Security Assessment Plan (per DoDI 8510.01); Acquisition Program Baseline (APB); Cost Analysis Requirements Description (CARD, per DoDI 5000.73); Lifecycle Sustainment Plan (LCSP); Information Support Plan (ISP); Lifecycle Mission Data Plan (LMDP, per DoDD 5250.01); Request for Proposal (RFP).
- **DOT&E (Director, Operational Test and Evaluation)** — the approval authority for the T&E Strategy on programs under T&E oversight, and the approval authority for operational test plans and live-fire strategies on the oversight list.

## Key Concepts

**The Strategy as an agreement, not a document.** The source frames the T&E Strategy primarily as a stakeholder agreement — it locks down who does what, with which resources — rather than as a static deliverable. That framing is why it must be socialized early and revised as the program evolves. Its purpose is twofold: to verify the technical requirements and to evaluate the system's operational effectiveness, its suitability, its survivability, and its lethality. It must also document the resources that developmental test (DT&E), operational test (OT&E), and live-fire test (LFT&E) will each need.

**Minimum content of the T&E Strategy.** The source enumerates a floor:
- An IDSK linking program decisions to their data requirements and sources, correlated to critical operational issues and technical requirements.
- Resources and test-support needs for every phase — including, where it is required, accreditation (the VV&A) of any modeling and simulation.
- The scope, objectives, and data for each of DT&E, OT&E, and LFT&E.
- A program schedule that carries the T&E events and the reporting obligations, with timelines built in for generating each report.
- Objectives for each test phase — its entrance and exit criteria, the cybersecurity test objectives, and the planned M&S events.
- Requirements for collecting data, covering both live events and what M&S produces.
- Projected and actual funding, with funding sources for all test resources — including M&S VV&A.

**Approval authority splits on oversight status.** For programs on T&E oversight, DOT&E approves the T&E Strategy; for programs not under oversight, approval rests at the Component level. The same oversight distinction reappears at the test-plan level: for oversight-list programs, operational test plans across every pathway (including LFT&E strategies) require DOT&E approval and should reach DOT&E roughly two months ahead of test start, and any deviation from the approved plan needs DOT&E concurrence before the revised events run.

**Test Plans as the execution layer.** Each event named in the Strategy gets its own test plan. At minimum a test plan states its purpose relative to the overall Strategy and program lifecycle; its schedule, location, and resources (personnel, targets, threats); its data requirements and the team's plan to collect, reduce, and distribute that data; and its limitations. Plans also capture event-execution order and any operating instructions that could sway outcomes, and — barring the unforeseen — every element of an approved plan, including all required data collection, should be satisfied by the period's end. Where personnel safety is in play, the T&E community supplies the relevant safety documentation in concert with the PM and user community.

**How the supporting documents feed T&E.** The source's Table 1 is essentially a map of where T&E content gets injected:
- *JCIDS documentation* — T&E personnel assess the testability, measurability, achievability, and clarity of the required capabilities and hand that assessment to the PM and Chief Engineer.
- *AoA* — provides the foundation for milestone documents starting at Milestone A and informs the Strategy for the preferred solution(s).
- *VOLT* — the authoritative, system-specific threat assessment; used as a reference for T&E plans, resource and capability requirements, test scenarios, and for defining the threat environment in a mission context. Only MDAPs and oversight-list programs require a unique, system-specific VOLT.
- *Acquisition Strategy* — the PM's program-execution plan; the T&E WIPT participates in building it so the T&E Strategy fully supports the program's approach, and it describes both contractor and government test programs.
- *SEP* — a living engineering document used as a reference when developing the Strategy, test plans, and other planning artifacts.
- *PPP* — the protection plan; T&E uses it for the Strategy and test planning, and testers must also consider how program protection applies to test events, processes, and data, whose exploitation could cause harm.
- *Cybersecurity Strategy / Security Plan / Security Assessment Plan* — the RMF-aligned artifacts the T&E WIPT reviews and leverages; the Security Plan in particular helps testers pinpoint specific areas to test.
- *APB* — the MDA–PM agreement used to track the program; T&E uses it to keep test plans, schedules, and resource requirements consistent with program goals.
- *CARD* — the cost-description basis; the Component Developmental Tester (CDT) ensures the test portion of the program definition is defined well enough for an adequate estimate, and confirms test funding lands in the Strategy's Resources section and eventually in the RDT&E exhibits and T&E budget submissions.
- *LCSP* — sustainment influences; reliability and maintainability data from DT and OT feed sustainment cost estimates.
- *ISP* — interoperability and information-exchange needs; T&E uses it (with a CONOPS/OMS/MP) to build scenarios for the network-entry, information-exchange, and mission-support dimensions, anchored by the Net-Ready KPP.
- *LMDP* — intelligence mission data requirements; the Strategy should define the specific intelligence requirements supporting both DT&E (detection/identification verification) and OT&E (effectiveness, suitability, survivability).
- *RFP* — the contract solicitation; at minimum it must convey the T&E community's test requirements and the proposal information and evaluation criteria.

**Digitization and a common data repository.** The source pushes the PM to stand up a common data repository accessible to all test teams so they can review, contribute, and reuse test data — enabling sequential testing, big-data analytics, and other adaptive methods that drive T&E efficiency. The intent is that testing and planning be automated as far as practical to support continuous development, integration, and delivery.

**Engage the contractor's V&V early.** The T&E WIPT and PM should understand the contractor's tools and, specifically, their verification and validation plans, and judge the credibility of those tools for the intended use. The government test team is encouraged to train with those tools so their outputs can inform evaluations — and the source notes these expectations should be pinned down with appropriate contractual provisions.

## Mental Models

- **Umbrella-and-instances.** "T&E Strategy" is the umbrella; TEMP, SAMP, and "test strategy" are pathway-specific instances of it. Don't get lost in the naming — the function (a stakeholder agreement guiding planning and execution toward major decisions) is invariant across names and pathways.
- **Decision-first planning.** The IDSK inverts the usual order: start from the program decisions that must be made, work back to the data those decisions require, then to the sources (CT/DT/LFT/OT/M&S) that produce that data. Tests exist to feed decisions, not the reverse.
- **Funnel: documents in, Strategy out, plans out.** Upstream acquisition documents (Table 1) funnel into the Strategy; the Strategy funnels down into per-event test plans. T&E's job is to be present at both joints — injecting test content upstream and decomposing faithfully downstream.
- **Oversight as a gating switch.** A single attribute — whether a program is on T&E oversight — flips both the Strategy's approval authority (DOT&E vs. Component) and the operational test-plan regime (DOT&E approval, advance-submission expectation, concurrence-before-deviation vs. not). Read oversight status first; it changes the rules.
- **Living document, not a milestone checkbox.** Both the Strategy and several of its feeders (SEP, PPP, Acquisition Strategy) are explicitly living artifacts that evolve with the program. A Strategy frozen at one milestone has already begun to drift.

## Key Takeaways

- The T&E Strategy is the PM-owned, T&E-WIPT-coordinated planning deliverable for all six acquisition pathways; "TEMP" and "SAMP" are among its common names, not separate things.
- Write it early — early enough to inform the contract — and keep it current across the lifecycle; it is an agreement on tasks, roles, resources, and responsibilities as much as a plan.
- It must carry, at minimum: an IDSK; resources for all phases (including M&S VV&A); DT&E/OT&E/LFT&E scope, objectives, and data; a schedule with reporting timelines; phase entrance/exit criteria plus cybersecurity and M&S objectives; data-collection requirements; and funding with sources.
- Approval depends on oversight: DOT&E approves on the oversight list, the Component approves otherwise. The same split governs operational test plans, which on the oversight list need DOT&E approval, advance submission (about 60 days ahead), and concurrence before any deviation.
- The Strategy is built from a defined set of upstream documents (JCIDS, AoA, VOLT, Acquisition Strategy, SEP, PPP, cybersecurity/RMF artifacts, APB, CARD, LCSP, ISP, LMDP, RFP); consult the MDID site for each document's definition, authority, and statutory notes.
- Test plans decompose the Strategy event-by-event and must state purpose-in-context, schedule/location/resources, data-handling, and limitations — with safety documentation wherever personnel are at risk.
- Push toward a shared, accessible T&E data repository and automation to enable sequential testing, analytics, and continuous delivery; understand and, where appropriate, train on the contractor's V&V tools, backed by contractual provisions.

## Connects To

- **DoDI 5000.89 (T&E policy)** — the controlling instruction the Strategy aligns to and the source of the IDSK requirement; the binding companion to this guidebook chapter.
- **The DoDI 5000-series ecosystem** — 5000.84 (AoA), 5000.83 (program protection / PPP), 8500.01 (cybersecurity), 8510.01 (RMF: Security Plan and Security Assessment Plan), 5000.73 (cost / CARD), 5000.85 (Major Capability Acquisition), and DoDD 5250.01 (intelligence mission data) — the named authorities behind the Table 1 feeders.
- **MDID website / T&E Enterprise Guidebook focus-area chapters** — the live reference layer for document definitions, approval authorities, and pathway-specific T&E content; this chapter is the index, those are the detail.
- **Acquisition pathway chapters** — where the six pathways' specific T&E content and test-team involvement in each document are detailed; the Strategy's pathway-agnostic framing resolves into pathway specifics there.
- **DT&E / OT&E / LFT&E execution** — the downstream test domains the Strategy scopes and resources, and whose plans are the execution-layer decomposition introduced here.
- **Systems engineering and program protection** — via the SEP and PPP as living feeders, the T&E Strategy is coupled to the broader SE and security-engineering effort rather than standing apart from it.

# Chapter — Schedule Assessment and Health Checks

> Source: NASA Schedule Management Handbook, 2024 edition, Chapter 6 ("Schedule Assessment and Analysis"). This chapter synthesizes the Schedule Assessment sub-function (Section 6.2) and its tiered assessment procedures. Use the 2024 edition, not the superseded 2010 SP-2010-3403.

## Core Idea

Schedule Assessment is the sub-function that determines whether an Integrated Master Schedule (IMS) is *valid and has integrity* — in the handbook's framing, whether the schedule is credible enough to be trusted for reporting, analysis, and control. It is deliberately distinguished from its companion sub-function, Schedule Analysis: Assessment tests the schedule's *credibility*, whereas Analysis tests the *likelihood* that the program/project (the handbook abbreviates this "P/p") will hit its technical goals on time, on budget, and at acceptable risk. The two are complementary but sequentially dependent — you cannot meaningfully analyze a schedule that has not first been validated through assessment. Both sub-functions are governed by the Schedule Management Plan (SMP), specifically its second of four sub-plans, the Schedule Assessment and Analysis Plan.

Assessment is not a one-time gate. It fires whenever the Schedule Database is first built and again on every change — formal or informal, internal or external. Its purpose is to answer two practical questions the handbook poses repeatedly: "Has the P/p built the *correct* schedule?" (content) and "Has the P/p built the schedule *correctly*?" (mechanics). Crucially, the handbook is candid about the limits: assessment does *not* guarantee the IMS will deliver products on the required dates — it only guarantees the schedule is reliable enough to support honest reporting and to generate analytical insight downstream.

The frequency and depth ("penetration") of assessment scale with risk. Factors named in the source that drive how much insight is required include technical risk level, confidence in the performing organization's management, how well PP&C processes are defined and followed, public visibility and consequence of failure, design/manufacturing complexity and producibility, asset value, and past cost/schedule performance.

## Frameworks Introduced (exact source names)

The chapter builds a layered apparatus. Named frameworks, in the order and role the source assigns them:

- **Dimensions of Schedule Reliability** — NASA's umbrella quality construct. Drawing on NASA's SCoPe community resources and GAO guidance, the Agency parses reliability into four near-orthogonal dimensions, each framed as a question. **Comprehensiveness** asks whether the full scope has been captured. **Construction** asks whether the network is topologically sound. **Realism** asks whether the schedule's data is cogently justified. **Affordability** asks whether the plan can actually be executed within its funding context. The dimensions are designed to minimize mutual overlap so assessment can proceed modularly without losing precision.

- **Sub-dimensions** — each reliability dimension is decomposed into sub-dimensions that map more directly to actionable procedures (e.g., Content Breadth, Level of Detail, Critical Path Construction, Vertical Traceability, Justification of Discrete Schedule Elements, Schedule Risk & Opportunity Treatment, Schedule Margin Sufficiency, Resource & Cost Integration, Phased Affordability).

- **Schedule Reliability Matrix** — the master traceability artifact. It traces each reliability dimension → sub-dimension → assessment/analysis question set → the specific procedure(s) that answer them, organized by 1st, 2nd, and 3rd Tier. The handbook describes it as condensing the entire vocabulary of the assessment domain into a single map of the process.

- **Tiered Assessment Procedures** — procedures ordered by logical precedence. The **1st and 2nd Tiers constitute Schedule Assessment**; the **3rd Tier is Schedule Analysis**:
  - *1st Tier:* **Requirements Check**, **Health Check**, **Risk Identification & Mapping Check**.
  - *2nd Tier:* **Critical Path (and Driving Path) and Structural Check**, **Basis Check**, **Resource Integration Check**.
  - *3rd Tier (analysis):* **SRA** (Schedule Risk Analysis) and **ICSRA** (Integrated Cost and Schedule Risk Analysis).

- **Schedule BoE Dossier ("BoE")** — the Basis of Estimate dossier. This is the living repository where all assessment evidence accumulates over iterations: findings, source-data dates, remediation plans, narrative, and basis rationale. The handbook calls it both a roadmap for schedule evolution and the "primary agent of change." After each assessment iteration the BoE is evaluated to decide the right course of action for the corresponding IMS version, and each BoE update marks which schedule incarnation it addresses.

- **Schedule Health Check tooling** — two named classes: MS Project add-ons such as NASA's **Schedule Test and Assessment Tool (STAT)**, and standalone packages such as **Polaris** and **Deltek Acumen Fuse**. These are described as aligning to community-accepted metric sets (the source also cites DCMA Manual 3101-02 lineage) and as tailorable to organization-specific metrics. STAT is requestable through the NASA Software Catalogue.

- **The Shock Test** — a named structural-integrity procedure inside the Critical Path and Structural Check (detailed under Mental Models below).

## Key Concepts

**The two governing questions.** Requirements Check answers the "correct *what*" (is the right content present?); Health Check answers the "correct *how*" (is the content expressed mechanically soundly?). The handbook explicitly frames the Requirements Check as content-focused and the Health Check as the pivot into mechanics.

**Iterative, prioritized, never-finished.** Assessment proceeds generally in tier order, but the source stresses that a clean linear path through the procedures is unlikely. It develops progressively — increasing in scope as foundational issues surface and resolve — and adapts to stakeholder and Program/Project Scheduler ("P/S") needs across the life cycle. A single assessment iteration is "satisfied" once all procedures have run in tier order at least once and the BoE is stamped with data-source dates plus next-step recommendations. But the sub-function is *never fully satisfied*, because changes will keep rippling through the IMS.

**The 1st Tier in detail.**
- *Requirements Check.* Verify the IMS reflects the breadth of content dictated by the full requirement set (technical requirements docs, P/p plans, the SMP and its GR&As, Milestone Registry, WBS/OBS/CBS hierarchy docs, budget-cycle docs, subcontracts, MOUs/MOAs, recorded stakeholder directives). The trace must be *two-way*: any requirement not manifested as schedule content goes into the BoE's "missing content registry" for disposition. Special attention to (a) downstream/terminal content, which often loses fidelity in rolling-wave schedules, and (b) control and notification milestones, whose misplacement can mislead stakeholders. Second step: verify **vertical traceability** — the schedule must nest into the P/p's organizational hierarchy and map cleanly to the WBS (GAO is quoted to the effect that the detailed schedule should reflect the WBS and define the activities needed to produce each deliverable). Exit: requirement-to-IMS-element map exists (at minimum a WBS-to-IMS map), and BoE is dated.
- *Health Check.* Run an automated check with an Agency- or industry-standard tool, then interpret it. This is "the lowest hanging fruit" — easy, repeatable, and quantitatively trackable over time. Step 2 stresses that color-coding is only a first look: green does not automatically mean healthy. The handbook's worked example is the "Constraints other than ASAP" metric — it can read green, yet a single "Must Finish On" constraint can invalidate the whole schedule, so every non-ASAP constraint and every missing predecessor/successor must be investigated individually. Each non-compliant metric gets an explanation, justifying source/expert opinion, and a remediation plan in the BoE.
- *Risk Identification & Mapping Check.* Two steps. First, confirm the P/p-sanctioned schedule risk list exists, is ratified by management or the risk board, lives in the BoE, and includes opportunities and other discrete probabilistic events; then augment it with readily identifiable unlisted risks (deeper discovery is deferred to the 2nd-Tier Basis Check). Second, verify that risk/opportunity *placement* in the IMS is well understood — the P/S must confirm a healthy working relationship between Schedule Management and Risk Management, that risk owners understand the IMS regions they touch, and that each risk's consequences and mitigation tasks are mapped into the schedule. The source warns that risk owners unfamiliar with the network often wrongly attribute cascading schedule consequences to headline events (e.g., naming a system CDR as a direct risk target).

**The 2nd Tier in detail.**
- *Critical Path (and Driving Path) and Structural Check.* Depends on satisfactory Health Check results. Step 1 is the Shock Test (below) to confirm horizontal traceability and proper dynamic behavior of the whole network. Step 2 is to identify, understand, and assess the deterministic critical and driving paths — does the critical path pass a common-sense test, match the workflow diagrams used to build the IMS, and agree with what leadership *thinks* is critical (the source notes these often differ)? Assessment probes level of detail, embedded/missing risks, lags and gaps, float/margin (e.g., margin tasks sitting on the critical path), and improper task types (e.g., LOE tasks on the critical path).
- *Basis Check.* Affirms the quality of the estimate behind *each discrete schedule element*. The framing: a schedule is "nothing more than" a collection of estimated elements, each needing a basis rationale; the IMS has little meaning without strong rationale for its elements. The P/S records, per element, the source-data quality and the method used to derive duration, linkages, constraints, mapped risks, etc. The burden of proof sits on programmatic and technical personnel to defend their choices. The governing standard is **replicability**: handed nothing but the element-level basis rationale recorded in the BoE plus the supporting reference data, a competent P/S ought to be able to rebuild the whole IMS from scratch — a reliability test the handbook borrows by analogy from cost estimating. Because this is too large to do at once, prioritize (e.g., top risks or the primary critical path) and progress deliberately across iterations.
- *Resource Integration Check.* Affirms that budget, workforce, allocated UFE, and cost estimates carry self-consistent time phasing and map cleanly to the IMS with mutual traceability tied to the same P/p snapshot. It deliberately stops short of judging time-phased budget *adequacy* — that is the ICSRA's job in the analysis section. This check feeds the higher-tier ICSRA.

**The BoE as connective tissue.** Every procedure's exit criteria repeat the same instruction: stamp the BoE with each data source's date for the current schedule/assessment iterations, and record next steps plus a corrective-action recommendation when organic improvement alone is insufficient. Most findings can be handled through the normal Schedule Maintenance cadence by informal agreement among P/Ss, Technical Leads, CAMs, or WBS element owners; only serious non-compliances, a forthcoming replan, or a rebaseline trigger the formal change-control process.

## Mental Models

**Credibility before likelihood.** Hold the firewall between the two sub-functions: Assessment establishes that the schedule *can be believed*; only then does Analysis ask *how likely* the dates are. Skipping the credibility step poisons every downstream analytical product (SRA/ICSRA inputs, critical-path identification, float calculations).

**Two perpendicular axes of schedule integrity.** *Vertical* traceability (Requirements Check) is the schedule nesting cleanly into the WBS/OBS hierarchy. *Horizontal* traceability (Critical Path and Structural Check) is every task/milestone having at least one predecessor and one successor (with the noted exceptions: P/p start/finish, external deliveries). The source treats horizontal traceability as *necessary but not sufficient* — a fully linked network can still behave defectively.

**The Shock Test as a dynamic-behavior probe.** This is the chapter's signature mental model for structural soundness. Set margin-task durations to zero (logging their existence in the BoE structural-issues list), then perturb the network task by task from the start:
- *Compression step:* zero out a task's duration and follow the downstream flow — every downstream task in the string ending at the terminal milestone should move left; if an eventual successor doesn't, record *why* (logic, flow confluence, constraint, etc.).
- *Slip step:* lengthen a task until it becomes critical and watch downstream activities push out. If the task *never* becomes critical, there is a structural defect (missing logic, a hard constraint, or a missing eventual successor). If it becomes critical but the terminal milestone date does *not* move, negative float is building up somewhere — likely a hard constraint choking the flow.
After each perturbation, artificially correct the found issue so subsequent issues can be isolated, then iterate to the end of the schedule. A schedule that passes the Shock Test is characterized as both healthy (some Health-Check items may remain) and structurally sound — and the handbook insists this is achievable even early in development.

**Color codes are a starting point, not a verdict.** The Health Check report is a "roadmap for investigation," not a grade. Green can hide a schedule-killing constraint; the P/S must drill into individual non-ASAP constraints and missing links because a single bad one can invalidate the critical path or the whole schedule.

**Realism as improvement, not grading.** The Basis Check explicitly frames the realism measure as a tool to *help the P/p improve* the schedule progressively, not to stamp a strict grade on the IMS. The orientation is evolutionary.

**Penetration scales with risk.** Match assessment depth and frequency to the risk posture and change cadence using the named factors (complexity, visibility, past performance, asset value, etc.) — don't apply uniform scrutiny everywhere.

## Anti-patterns

The source names these schedule-construction defects (chiefly via the Health Check metrics in Figure 6-9 and the Shock-Test investigations):

- **Dangling activities / missing logic (open ends)** — tasks missing a predecessor, a successor, or both; impairs float and critical-path calculation and undermines credible SRA/ICSRA and what-if analyses.
- **Hard constraints** — should be avoided; they override logic, distort float, and can build up negative float. Prefer soft constraints or deadlines, used minimally and appropriately. Even a single "Must Finish On" can invalidate a schedule.
- **Negative float** — signals an artificially accelerated or constrained, infeasible schedule; ideally there should be none.
- **Improper use of leads and lags** — leads can make a successor start before its predecessor; lags hide detail, cannot be statused like activities, and cannot carry uncertainty distributions for SRAs (underestimating risk). Lags should be replaced with activities.
- **Logic relationships other than Finish-to-Start (FS)** without justification — non-FS logic adds complexity and can obscure the critical path.
- **Logic on summary activities** — poor technique; logic belongs on real work, not on groupings.
- **Improper logic (circular / reverse)** — circular logic common in multi-project schedules; reverse logic typically a lead artifact.
- **Redundant logic** — a link duplicated by a more detailed path; complicates maintenance and critical-path tracing.
- **Out-of-sequence logic** — status/progress conflicting with logic (a successor progressing before its FS predecessor starts); a sign of insufficient task detail.
- **Overuse of milestones / zero-duration "activities"** — work-bearing items should have positive duration; milestones should not have durations.
- **LOE tasks on the critical path** — Level-of-Effort tasks capture no measurable work and must be removed from current or potential critical paths.
- **High-duration activities** — durations over roughly two months suggest planning at too high a level for adequate control.
- **Stale or invalid statusing** — incomplete tasks left in the past with no revised forecast (Incomplete Task Status), actual dates in the future (Invalid Actual Dates), or future-planned tasks statused in the past (Invalid Forecast Dates); all corrode credibility and float/critical-path accuracy.
- **Artificially high float** — often from artificial constraints; high float anywhere is an earmark for deeper assessment.
- **Tasks without a baseline, missing field information, or inconsistent vertical integration** — undermine performance measurement and clean roll-up.

## Key Takeaways

1. Schedule Assessment validates the IMS (credibility); Schedule Analysis evaluates the likelihood of meeting goals — and analysis is meaningless without assessment first. Both are governed by the SMP's Schedule Assessment and Analysis Plan.
2. NASA's umbrella quality measure is **reliability**, parsed into four near-orthogonal dimensions — Comprehensiveness, Construction, Realism, Affordability — and traced through the **Schedule Reliability Matrix** to specific tiered procedures.
3. The **1st and 2nd Tiers are assessment** (Requirements, Health, Risk ID & Mapping; then Critical Path & Structural, Basis, Resource Integration); the **3rd Tier (SRA/ICSRA) is analysis**.
4. The **BoE dossier** is the living evidence base and the engine of schedule change; every procedure ends by stamping it with data-source dates and corrective-action recommendations.
5. The **Health Check** is the cheapest, most repeatable procedure and the foundation for deeper assessment — but its color-coded output must be interpreted, not trusted at face value; a single bad constraint can invalidate a schedule.
6. The **Shock Test** is the structural-integrity workhorse: perturb durations across the network to confirm horizontal traceability and proper dynamic behavior, isolating defects one at a time.
7. The **Basis Check** holds every element to a **replicability** standard — the BoE's rationale should let a skilled P/S rebuild the entire IMS.
8. Assessment is iterative, prioritized, risk-scaled, and **never fully complete**; aim to have the schedule healthy and structurally sound before SDR.

## Connects To

- **Schedule Management Plan (SMP) and its sub-plans** — the Schedule Assessment and Analysis Plan (the second sub-plan) sources the techniques and GR&As assessment relies on (handbook Section 4.3).
- **Schedule Development** — assessment activates the moment the Schedule Database/IMS is first built; the BoE and the Basis Check are most influential during development when element parameters are first derived (Sections 5.5.9, 5.5.x).
- **Schedule Analysis (3rd Tier — SRA/ICSRA)** — assessment is the precondition; a healthy schedule is required before risk-adjusted analysis, joint confidence levels (JCL), margin allocation, or stochastic critical-path identification can be credible (Section 6.3).
- **Schedule Maintenance and Control** — most findings flow into the routine maintenance cadence; serious defects, replans, or rebaselines escalate to the formal change-control process (Chapter 7, Section 7.3.1).
- **Independent Assessment** — once the 1st and 2nd Tiers are satisfied across iterations, the BoE is considered ready for formal evaluation by Standing Review Boards (SRBs) / Independent Review Teams (IRTs) as part of the LCR and KDP process.
- **GAO Schedule Assessment Guide (GAO-16-89G)** — cited repeatedly as the external best-practice authority on content completeness, WBS reflection, sequencing/links, and appropriate level of detail.
- **NASA SCoPe community and the Agency Schedule Management Tool Matrix** — the source for reliability-dimension framing and for the catalog of health-check tooling (STAT, Polaris, Deltek Acumen Fuse).

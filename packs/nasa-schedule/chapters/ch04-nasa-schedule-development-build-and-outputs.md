# Chapter — Schedule Development II: Building the Schedule, Logic, Durations, Critical Path, Margin & Outputs

> Source: NASA Schedule Management Handbook (2024 edition), Section 5.5 "Develop the Schedule" through Section 5.8. This chapter is grounded entirely in that slice. Use the 2024 edition, not the superseded 2010 SP-2010-3403.

## Core Idea

Schedule Development is the mechanical and analytical act of turning a plan into an executable network model. The handbook frames it as a sequence of build steps that begins early in Formulation and is driven by the requirements and the Schedule Development Plan inside the Schedule Management Plan (SMP). The steps progress roughly in order: stand up the tool, code the activities, choose the method, set the hierarchy and naming, capture all scope, decompose to the right level of detail, link the activities with logic, estimate durations, find the critical path, add and place margin, load resources or costs, time-phase to funding, and map risks. The single most important output is the Integrated Master Schedule (IMS) — a complete, time-phased, logically-linked network of every piece of approved work needed to meet the program/project (P/p) commitments — but the Schedule Database is built so it can also emit a Summary Schedule, an Analysis Schedule, Schedule Performance Measures, and a Basis of Estimate (BoE). A recurring theme across every step is that each development decision generates BoE rationale and feeds a downstream assessment check; the build and the justification of the build are inseparable.

## Frameworks Introduced (exact source names, when/how)

- **Critical Path Method (CPM)** — named as the best-practice scheduling technique (Section 5.5.3). A logic-network diagram method that estimates the minimum P/p duration by computing the longest path through the network. Used as the foundational scheduling method; the handbook recommends it be employed in an *expanded* form that integrates cost, risk, and resources rather than its bare deterministic form.

- **Schedule Estimating Relationships (SERs)** — introduced under duration estimating (Section 5.5.9.3.1). A parametric framework that defines schedule duration as a mathematical function of one or more independent variables (technical parameters such as mass and power, or cost). Presented as the schedule analogue to Cost Estimating Relationships (CERs); used when a measurable, statistically significant driver-to-duration relationship can be established.

- **Schedule Repository** — named NASA archive (Section 5.5.9.3.2), an initiative begun July 2019 to collect IMS files in native format on a regular cadence, providing planned-versus-actual history for future estimating and assessment.

- **CADRe / ONCE Database** — Cost Analysis Data Requirement and the One NASA Cost Engineering database (Section 5.5.9.3.2). CADRe is a three-part document capturing programmatic, technical, life-cycle-cost, and cost/schedule-risk snapshots at each life-cycle review milestone; ONCE provides web-based, controlled query access to that data. Used as a source of analogous-mission history for duration estimating.

- **SMART** — Schedule Management and Relationship Tool (Section 5.5.9.3.2). Combines analogy-based and parametric methods for unmanned Category-1 spacecraft from Authority to Proceed to Launch; produces a cumulative distribution function of analogous-mission durations and incorporates NASA-derived SERs whose drivers include mass, power, mission design life, development year, instrument count, mission class, and maximum data rate.

- **NICM** — NASA Instrument Cost Model (Section 5.5.9.3.2). Instrument-focused model whose SERs are distinctive because cost is an input to the duration equation (Cost As an Independent Variable), establishing a functional link between an instrument's calculated cost and its schedule duration.

- **The four activity relationship types** — Finish-to-Start (FS), Start-to-Start (SS), Finish-to-Finish (FF), Start-to-Finish (SF) (Section 5.5.8.1). FS is the recommended default because it gives the most accurate total-float calculation; SF is flagged as very uncommon.

- **The five IMS development techniques** (Section 5.6.1): Single Consolidated P/p IMS, Master P/p IMS (with sub-projects), P/p Control Milestone Integration IMS, Summary P/p Master Logic Network IMS, and Prime Contractor-based P/p IMS (with Mission IMSs as the Campaign-level approach). Each technique carries documented advantages and disadvantages and a suggested mapping to P/p types.

- **Resource loading vs. cost loading vs. budget loading** (Section 5.5.12). Resource loading assigns specific workforce, equipment, and consumables (the grassroots approach, an Agency requirement when a JCL is required); cost loading maps dollar estimates to activities (acceptable substitute, less cumbersome); budget loading is explicitly *not* a defined Agency method and is advised against.

- **Schedule Outputs taxonomy** (Section 5.6): IMS, Summary Schedule, Analysis Schedule, Schedule Performance Measures, and Schedule BoE — the five things the Schedule Database is built to produce.

## Key Concepts

**Tool capabilities precede everything.** Before building, the schedule tool must meet a defined floor of functional, technical, and interface capabilities — among them entering baseline/current/actual data, specifying dependency types with minimal lead/lag, calculating total and free slack, supporting code fields for filtering and grouping, and interfacing to EVM and schedule-risk-analysis applications. MS Project and Oracle Primavera P6 are cited as the common Agency tools that generally satisfy these. Tool selection and its rationale are part of the BoE.

**Field codes are the connective tissue.** Activity coding (WBS, control account/CWBS, responsibility, phase, activity type, EVM codes, and many custom codes) lets the same database serve summary, intermediate, and detail consumers, supports vertical traceability, and integrates the schedule with EVM, risk, and cost systems. The handbook stresses *consistency* of code values and recommends maintaining a coding dictionary; where tools force incompatible abbreviations, a cross-reference (crosswalk) table reconciles them.

**Phase-appropriate maturity.** The expected content and granularity of the schedule grow with life-cycle phase: Pre-Phase A carries high-level summary tasks and key milestones; Phase A adds discrete breakdown, an identifiable preliminary critical path, and initial margin; Phase B drives near-term work (six-to-twelve months) to discrete, short-duration tasks and receives final baseline approval, becoming the EVM performance-measurement baseline; Phases C/D push far-term work into shorter tasks as time advances. The Phase B baseline is the foundation for measuring performance for the rest of implementation.

**Rolling wave planning.** Near-term work (within roughly 6–12 months) is planned to discrete detail with durations preferably under two times the update cycle (i.e., under two months), while far-term work sits at planning-package/summary level and is elaborated as it approaches the near-term window. Procurement long-lead items and level-of-effort work are explicit exceptions to the two-month rule. Rolling wave must not be used to defer detail that is already known.

**Horizontal vs. vertical traceability.** Horizontal traceability comes from complete, accurate network logic — every activity and milestone having at least one predecessor and one successor (the start and finish milestones being the sanctioned exceptions), so progress and forecasts cascade correctly. Vertical traceability means all supporting schedules carry consistent data and trace to the IMS, which in turn traces to the WBS, SOW, Contractor Performance Report, and EVMS. Schedules stratify into three levels — Summary, Intermediate, Detailed — each of which should clearly identify the critical path.

**Duration estimating is multi-method and uncertainty-aware.** Durations may come from established standards, brainstorming, subject-matter-expert judgment, analogy, parametric/SER analysis, extrapolation, build-up/grassroots, or performance-based extrapolation. The handbook draws a sharp line between a *build-up schedule estimate* (an attempt to predict the actual finish, like a cost estimate) and a *given detailed schedule plan* (an organizing plan that may carry optimism and constraints). For each activity, three-point estimates (Min, Most Likely, Max) capture duration uncertainty; the task owner must own and approve those durations, which are not to be padded, artificially trimmed, or cut by management fiat.

**Critical path, driving path, and "critical activities" are three different things.** The critical path is the longest continuous string of logically linked activities from time-now to completion, carrying the least float — it sets the earliest finish. A driving path is the critical path to an interim end item (a milestone or delivery) other than P/p completion, defined by zero free float. A "critical activity" is a subjectively important task (a KDP, a key test) that may or may not actually sit on the calculated critical path. The handbook warns that an incomplete or wrongly sequenced network yields an invalid critical path, and recommends tracking primary, secondary, and tertiary paths at minimum.

**Float vs. margin vs. contingency.** Float (slack) is an automatic CPM calculation (late dates minus early dates), in free and total flavors. Margin is a deliberately planned quantity of working days — loaded as scope-less, budget-less "activities" — sized from quantified risks and uncertainties. Contingency means non-working time (holidays, weekends, extra shifts) that could be tapped. NASA's preferred term is "margin"; NPR 7120.5 treats "reserve" as obsolete and uses "schedule margin" and "UFE" instead. The handbook deliberately prioritizes managing margin over float, because margin's direct tie to risk lets you judge whether the amount is *adequate*, and managing margin tends to manage float by default.

**Where and how much margin.** Early on, margin can be sized from analogous missions, expert judgment, or established standards (e.g., ranges like 1–2 months per year through I&T, scaling up nearer launch). As soon as practical it should be validated by probabilistic schedule risk analysis. NPR 7120.5 requires risk-informed schedules at progressively finer levels (project level at KDP A, system level at SRR, subsystem level at SDR), and an ICSRA/JCL is required at the baseline decision point and at specified later milestones depending on life-cycle cost thresholds. Margin is placed where risks occur (along primary/secondary/tertiary paths), just before key milestones/test events, and some near the end before final delivery — though end-of-schedule margin must be tightly managed so teams do not treat it as a free buffer for performance slips.

**Resource/cost loading and time-phasing close the loop.** Loading resources (or, when impractical, costs) ties the IMS to the cost estimate and enables EVM, what-if analysis, and JCL. Resource leveling shifts tasks within logic and constraints to smooth over- or under-allocation — done cautiously, ideally manually or in small validated chunks, by experienced schedulers. Finally the schedule is time-phased against actual funding availability (handling flat annual budgets, continuing resolutions, facility windows, and staffing limits), with SNET constraints, lags, or resource leveling used to align work with money.

## Mental Models

- **The schedule is a model, not a wish.** Using estimating methods and SERs ensures dates are produced by logic and durations rather than by a target finish reverse-engineered into the plan. Top-down (time-available) estimating embeds optimism; engineering build-up estimates the real effort without a predetermined end date in mind.

- **Build the house in order.** Logic captures physical reality — you cannot roof a house before the framing is done; you cannot design the spacecraft before requirements are complete. Summary-level flow diagrams are drawn first to establish the integrate-then-test cycle, and only then are detailed dependencies assigned.

- **Float is calculated; margin is reasoned.** Float falls out of the network arithmetic and reflects sequencing. Margin is an analytical judgment about risk and uncertainty. You can have float and still be inadequately protected; the question "do we have enough?" is answerable only in margin terms.

- **Auto-schedule, don't hand-place.** In MS Project, Manual scheduling fixes dates the scheduler types in; Auto scheduling lets the engine apply logic and constraints — that is where the tool's value to the management process actually lives.

- **Detail buys fidelity, but only useful detail.** Greater decomposition improves sequencing, critical-path accuracy, and progress measurement — yet excessive redundant links and over-constraining destroy analyzability. Granularity should be as consistent as the phase allows, with deliberate extra detail in high-risk, high-cost areas.

- **LOE rides along; it must never steer.** Level-of-effort tasks track the duration of the work they support and add no time of their own, so they must be modeled (via avoided logic links or deliberately shortened durations, documented) so they never appear on the critical path.

- **Margin is a lien, not a line item.** Best practice keeps the budget for planned margin outside the baseline, held as a lien against Management Reserve or UFE, and only converts margin into scoped, budgeted activities through change control when a risk is realized.

## Anti-patterns (named in the source)

- **Leads and lags as a substitute for real tasks.** The handbook warns leads/lags mask undefined lower-level activities, are hard to identify and document, can corrupt float and distort the critical path, complicate SRA/ICSRA, and block EVM (no scope exists against a lag). Prefer an explicit labeled task; if used, justify in task notes.

- **Hard constraints.** Must-Start-On / Must-Finish-On and the other hard constraints override logic-driven dates, can produce physically impossible dates, and inject negative float throughout. They are to be avoided except where absolutely necessary; soft constraints or deadlines are preferred. The ALAP constraint is called out to never be used in MS Project because it consumes total float and can slip the end date.

- **Logic on summary activities.** Summary start/finish dates derive from their detail; assigning logic to them is wrong.

- **Redundant links.** A→C when A→B→C already exists confuses workflow and complicates analysis.

- **Confusing the critical path with "critical activities."** Treating a subjectively important task as if it sits on the computed critical path misdirects management attention.

- **Funded schedule margin.** Allocating budget directly to margin activities inflates the baseline and distorts EVM by making it look as though less work has been accomplished. Not a best practice.

- **Budget loading.** Spreading externally imposed budget across activities lacks the fidelity of a cost estimate, can underestimate true cost (especially with an under-performing cost-plus contractor), and yields an unreliable confidence level in an ICSRA. To be avoided.

- **Substituting a Summary Schedule for an IMS.** A Summary Schedule is a roll-up for reporting and must never replace the IMS where an IMS is required — doing so contradicts the very definition of an IMS.

## Key Takeaways

1. Schedule Development proceeds as an ordered build — tool, codes, method (CPM), hierarchy, naming, scope, detail, logic, durations, critical path, margin, loading, time-phasing, risk mapping — each step producing BoE rationale and feeding a downstream assessment check.
2. CPM is the best-practice method, used in an expanded form that integrates cost, risk, and resources; its bare deterministic form ignores duration uncertainty, resource limits, and discrete risk.
3. Finish-to-Start is the default relationship for accurate total float; leads, lags, and hard constraints are minimized and must be justified in the BoE because they distort float and the critical path.
4. Durations come from multiple estimating methods (standards, analogy, parametric SERs, build-up, etc.), captured as three-point uncertainty ranges and owned by the responsible team member — never padded or arbitrarily cut.
5. NASA's parametric/historical toolset — Schedule Repository, CADRe/ONCE, SMART, NICM — supplies analogous and parametric inputs for duration estimating.
6. Distinguish critical path (longest path to completion), driving paths (to interim end items, zero free float), and management-designated "critical activities."
7. Manage margin over float: margin is planned working-days sized from risk/uncertainty, validated by probabilistic analysis, placed where risks occur and before key milestones, and held as a lien against MR/UFE rather than baselined as funded margin.
8. Resource or cost loading ties the IMS to the cost estimate and enables EVM and JCL; budget loading and funded margin are explicitly discouraged.
9. The Schedule Database is built to emit five outputs — IMS, Summary Schedule, Analysis Schedule, Schedule Performance Measures, and Schedule BoE — with five IMS development techniques available depending on P/p type and acquisition strategy.
10. Exit criteria: a Schedule Database in a tool that can produce an IMS with the required performance measures, a preliminary BoE, an Analysis Schedule for risk analysis, and a Summary Schedule for reporting.

## Connects To

- **Schedule Development I (earlier build foundations) and the SMP/Schedule Development Plan** — this chapter executes the plan those establish; tool selection, field codes, naming, and scope all originate in the Development Plan.
- **Schedule Assessment and Analysis (Chapter 6 of the handbook)** — every build step here names a continuous downstream check: Requirements Check, Health Check, Critical Path and Structural Check, Shock Test, Basis Check, Risk ID and Mapping Check, Resource Integration Check, and the SRA-/ICSRA-based assessments. Margin adequacy and the Analysis Schedule feed SRA/ICSRA/JCL.
- **Schedule Maintenance and Control (Chapter 7 of the handbook)** — the baselined IMS becomes the performance-measurement baseline; margin and float erosion tracking, schedule compression, and change control of the baseline live there.
- **Schedule Documentation and Communication (Chapter 8 of the handbook)** — Summary Schedules, performance reports, and report types (CPLI, BEI, SPI/SPIt, Earned Schedule, confidence-level reports) are surfaced for management forums.
- **EVM (NASA EVM Handbook / ANSI-EIA-748)** — field coding, control accounts, resource loading, time-phasing, and the Phase B baseline all set up the Performance Measurement Baseline; Management Reserve and UFE back the eventual use of margin.
- **Cost estimating (NASA Cost Estimating Handbook)** — SERs mirror CERs; cost-based databases and models feed parametric duration estimates; the IMS must reconcile to the cost estimate before baselining.
- **Risk Management (RMS)** — discrete risks and mitigation burn-downs are quantified and mapped to schedule activities, with residual risk tracked; accepted risks augment the baseline IMS.
- **NPR 7120.5 / Agency Baseline Commitment** — defines margin, mandates risk-informed schedules by phase, and drives the JCL/ICSRA requirements that gate baselining.

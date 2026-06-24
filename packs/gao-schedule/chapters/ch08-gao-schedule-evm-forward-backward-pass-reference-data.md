# Chapter — Earned Value Management, the Forward and Backward Pass, Date Constraints, Quantitative Measures, and Industry Comparisons (Appendices III–IX)

## Core Idea

This chapter is the reference layer of GAO-16-89G — the appendices that supply the technical machinery, the standard vocabulary, the measurable data definitions, and the external corroboration behind the ten best practices presented earlier in the guide. Where the body of the guide tells an auditor *what* a reliable schedule looks like, these appendices tell them *how the numbers are computed*, *what to call each constraint*, *which quantities to pull from the schedule file*, and *how GAO's criteria line up against the schedule guidance the rest of the federal and defense community already uses*.

Five threads run through the material. First, when a program runs inside an earned value management (EVM) environment, additional scheduling considerations apply on top of the universal best practices, because the schedule becomes the source of time-phasing for the performance measurement baseline. Second, the forward and backward pass are the deterministic arithmetic that turns network logic plus durations into early dates, late dates, total float, and the critical path. Third, date constraints have standardized names and — far more important than the names — predictable effects on those forward and backward pass calculations. Fourth, schedule health can be assessed quantitatively through a defined set of data measures, but deliberately without pass/fail tripwires. Fifth, GAO's best practices were cross-checked against major industry and agency guidance, and they substantially agree, with resource loading and government/contractor integration being the recurring point of divergence.

The unifying message of the reference appendices: **the schedule is a calculable model, and reliability is demonstrated by inspecting the calculations — the dates, the float, the logic links, the constraints, and the variances — not by trusting the schedule's surface appearance.**

## Frameworks Introduced (exact source names, when/how)

- **Earned Value Management (EVM)** — Introduced in Appendix III as a management tool that ties the technical scope together with schedule and cost, so that progress can be both planned and controlled. It compares the value of work accomplished in a period against the value of work planned for that period, and against actual cost incurred, to read out cost and schedule status. Because it expresses progress in consistent units (typically dollars or labor hours), it lets dissimilar work efforts — the guide's examples include cabling, sheet metal, rebar, and systems design — be combined into one measure, provided the program is broken into well-defined, objectively measured tasks.

- **GAO Cost Estimating and Assessment Guide (GAO-09-3SP)** — Cited repeatedly in Appendix III as the companion volume; its Chapters 18–20 carry the full EVM treatment, including performance measurement baseline (PMB) development, the integrated baseline review, and objective measures for earned value. The schedule guide defers EVM depth to it.

- **FAR Subpart 34.2 and ANSI/EIA-748** — Named as the regulatory and standards basis. The Federal Acquisition Regulation Subpart 34.2 requires an EVM system for major development acquisitions; when EVM is in force, the system should satisfy the intent of the 32 guidelines of ANSI/EIA-748, the national EVM standard. Appendix III explicitly maps several best practices to specific EVM guidelines (Best Practice 1 ↔ Guideline 1; Best Practice 3 ↔ Guidelines 3, 5, 8–15; Best Practice 9 ↔ Guidelines 7 and 22; Best Practice 10 ↔ Guidelines 28–32).

- **The Forward Pass and Backward Pass** — Appendix IV's core framework. The forward pass computes the earliest each activity can start and finish (early start, early finish) by adding durations successively through the network; the backward pass computes the latest each can start and finish (late start, late finish) without slipping the project, working backward from the project's early finish. Together they yield total float and the critical path.

- **Total Float (TF)** — Defined in Appendix IV as the difference between when an activity *may* start/finish and when it *must* start/finish for the project to finish on time. Activities with zero total float lie on the critical path and have no flexibility.

- **DOD PARCA / UN/CEFACT XML schema and the Integrated Program Management Report (IPMR, DI-MGMT-81861)** — Appendix V's naming authority for date constraints. GAO adopts the date-constraint names from the XML schemas that the DOD office for Performance Assessments and Root Cause Analyses (PARCA) uses to standardize how cost and schedule data are collected. DOD PARCA developed a data exchange instruction (DEI) that supplements XML schema 09B of UN/CEFACT (the United Nations body for trade facilitation and electronic business), which provides a standardized framework for exchanging schedule and cost data over a project's life.

- **Standard Quantitative Measurements for Assessing Schedule Health** — Appendix VI's framework: a table of standard data measures organized by best practice, paired with the qualitative program questions of Appendix II. Notably, **no pass/fail thresholds or tripwires** are attached to any measure.

- **Comparison sources (Appendix VII)** — GAO compared its guide against: DOD **Defense Contract Management Agency (DCMA)** and its **14-Point Assessment (14PA)**; DOD **Naval Air Systems Command Cost Department (NAVAIR 4.2)** and its **Integrated Project Management Toolkit / Schedule Metrics Guide** with an 11-point assessment; **Department of Homeland Security's Scheduling Handbook**; **NASA's Schedule Management Handbook (NASA/SP-2010-3403)** and its **joint confidence level (JCL)**; and the **National Defense Industrial Association (NDIA) Planning and Scheduling Excellence Guide (PASEG)** with its eight **Generally Accepted Scheduling Principles (GASP)**.

- **Recommended Elements of a Data Collection Instrument** — Appendix VIII's enumerated list of fifteen artifacts an assessor should request to evaluate a schedule.

- **Case Study Backgrounds** — Appendix IX ties the guide's 19 case studies to 11 underlying GAO reports.

## Key Concepts

### EVM scheduling considerations (Appendix III)

EVM scheduling overlays the universal best practices with structural requirements:

- **Authorized work and the WBS (Best Practice 1 / Guideline 1).** Program work elements must be defined, usually through a WBS that decomposes all authorized work; authorization happens at the control-account level via a work-authorization process, the paperwork of which records outputs, deliverables, budget, and the required signatures. A subtlety the guide flags: some organizations and auditing agencies (DCMA among them) treat "authorized work" as only the scope placed *under contract*, so a contractor schedule will include only contractually authorized work. GAO's Best Practice 1 is broader — the IMS should reflect *all* effort across government, contractor, subcontractor, and key vendor, because the government program manager owns the full scope, not just the contracted portion.

- **The performance measurement baseline and resource loading (Best Practice 3 / Guidelines 3, 8).** The entire schedule must be baselined because the IMS time-phases every control account and work package making up the PMB. Loading the schedule fully with resources is the simplest route to time-phasing costs for performance measurement; if it is not fully loaded, tracing how costs phase over time becomes far harder and the logic may be untraceable. Baselines must be set — formally or informally — well before the integrated baseline review (IBR) deadline to be credible.

- **Control accounts, work packages, planning packages, SLPPs (Guideline 5).** The control account is the point at which a WBS element crosses the organizational breakdown structure (OBS); it is where actual costs are collected and variances reported, and it is the focal point for work authorization and performance measurement. A single WBS element may host multiple control accounts because several organizations can work the same element. Below the control account, effort breaks into **work packages** (near-term, discrete, ideally 4–6 weeks, measurable) and **planning packages** (budget-holding accounts for future work that cannot yet be detailed, but are still logically sequenced, tied to a WBS element, and resourced). **Summary level planning packages (SLPPs)** are temporary, not assigned to control accounts, and hold scope/schedule/budget that cannot yet be practically assigned; they should be moved into control accounts at the earliest opportunity. Planning packages and SLPPs are detail-planned later through the rolling wave process.

- **Statusing and objective measures (Best Practice 9 / Guidelines 7, 22).** Statusing typically updates either activity duration or work. Duration updates are easiest but denote the passage of time from the start, not the amount of work done, so they can mislead. Updating work by resources costs more effort but forecasts remaining effort better. Under EVM, objective measures are required so that work accomplished can be measured and compared against work planned, producing variances. The three classes of measure are **discrete effort**, **level of effort (LOE)**, and **apportioned effort**.

- **Discrete-effort earned-value methods.** The guide's table lists methods for taking earned value on discrete tasks: **0/100** (no value until the task finishes); **50/50 (or 25/75, etc.)** (half the value at start, the rest at finish, with other splits allowed); **percentage complete** (value by share of work done, ideally tied to quantifiable underlying measures such as drawings completed, computed as cumulative value to date divided by total work-package value); **weighted milestone** (value taken as importance-weighted milestones are accomplished, with budget divided by milestone weights); **units complete** and **equivalent units** (counts of similar products, or fractional equivalents of full units — methods common in construction and manufacturing). *(The source presents these as a seven-row method table; the row-to-description pairing in the underlying text is partially scrambled by extraction — treat the method definitions above as the substance and the original table as a figure to be redrawn cleanly.)*

- **LOE and apportioned effort.** LOE activities track the passage of time and have no physical product or deliverable (program management is the example). Apportioned effort is not itself divisible into short work packages but varies in direct proportion to a related discrete activity; the example is quality control tied to pipefitting or concrete pours. Apportioned QC activities should be hammocked to their related activities and earn value based on those activities' earned value.

- **Baseline maintenance and change control (Best Practice 10 / Guidelines 28–32).** When EVM is required, change control is more restrictive: authorized changes must be promptly recorded in the EVM system, controlling documents updated before new work starts, and the guidelines cover timely incorporation, reconciliation of current to prior budgets, control of retroactive changes, prevention of unauthorized revisions, and documentation of PMB changes. The auditor should be able to identify both the baseline schedule and the most recent statused schedule to verify reported variances.

### The forward and backward pass (Appendix IV)

The guide works a concrete house-construction "start-up and testing" example: setting electricity, gas, and water meters after inspections complete, then testing the electrical system, the furnace/AC, and the plumbing fixtures before a completion milestone. The arithmetic is the takeaway:

- **Forward pass — early dates.** Activities begin as soon as their logic allows (forward scheduling). The early finish is computed by adding duration to the early start, then subtracting one to account for the full working day spanning start and finish:

  **EF = ES + duration − 1**

  For a single finish-to-start link, a successor's early start is its predecessor's early finish plus one day. When an activity has multiple predecessors, its early start is driven by the *latest* early finish among them — an activity cannot begin until its last predecessor finishes. Milestones have no duration and occur immediately after their latest predecessor.

- **Backward pass — late dates.** Starting from the project's early finish, the backward pass computes how long each activity can wait without delaying the project. The late start is the late finish minus duration plus one:

  **LS = LF − duration + 1**

  In general an activity's late finish is its successor's late start minus one (**LF = LS − 1**). When an activity has multiple successors, its late finish is driven by the *earliest* late start among them — it need not finish until its earliest-needed successor must start.

- **Total float.** Once early and late dates exist, flexibility is read off as total float:

  **TF = LS − ES = LF − EF**

  Activities with zero total float are on the critical path; any slip transfers day-for-day to the end milestone. In the worked example, the meter-setting activities and the plumbing test sit at zero float, while only the furnace/AC test carries a day of float. The guide notes that adding a resource (an extra electrician) can shorten a duration by a day and thereby inject a day of float — and because float is shared along a path, the predecessor gains that day too.

### Date-constraint names and effects (Appendix V)

The guide's stance is explicit: the *name* of a constraint matters far less than its *effect* on the network calculations. Using the DOD/UN/CEFACT standard names (with common software aliases):

- **Finish no earlier than (FNET)** — forward pass: pushes early dates so early finish meets the constraint date.
- **Finish no later than (FNLT)** — backward pass: pulls late dates so late finish meets the constraint date.
- **Start no earlier than (SNET)** — forward pass: pushes early dates so early start meets the constraint date.
- **Start no later than (SNLT)** — backward pass: pulls late dates so late start meets the constraint date.
- **Must start on (MSON)** — sets both early and late start equal to the constraint date.
- **Must finish on (MFON)** — sets both early and late finish equal to the constraint date.
- **As soon as possible (ASAP)** — the default for forward scheduling; sets early start as early as possible. **As late as possible (ALAP)** — the default for backward scheduling; sets early finish as late as possible.

ASAP/ALAP are not in the DOD/UN/CEFACT standard but behave as standard defaults. ALAP can be forced in forward scheduling to start an activity as late as possible, but this is rare because it immediately consumes all available float for the activity — and, depending on software, can wipe out the total float of successor activities too. The guide also warns that some software offers constraints that let early and late finish be set equal while still permitting a later planned finish, which allows the network to calculate negative total float without literally constraining dates — behavior that varies by tool and must be understood.

### Standard quantitative measures (Appendix VI)

The quantitative assessment complements the qualitative program questions. Its governing principles: **no pass/fail thresholds or tripwires**; measures are interpreted in context with qualitative information and documented justification; and **severity of an error takes precedence over its quantity**, because any single error can compromise the whole network. The measures are organized by best practice. Representative measures:

- **BP1 (capturing all activities):** counts and types of activities (summary, hammock, milestone, detail); remaining-activity counts; activities flagged both milestone and summary (a contradiction); unnamed or duplicate-named activities; ratio of detail activities to milestones (one or two per milestone is low detail, around ten is highly detailed); activities not mapped to the WBS or statement of work.
- **BP2 (sequencing):** remaining detail activities/milestones missing predecessor, successor, or both links; **dangling activities** (no predecessor on the start date or no successor off the finish date); percentage of links that are finish-to-start (which should be the majority); start-to-finish links; high-predecessor convergence points (potential high-risk areas); soft date constraints.
- **BP3 (resources):** hard date constraints; **active SNET/FNET constraints** (a constraint counts as active only when the activity's scheduled start/finish equals the constraint date and is thus being held back); lags and leads (counted once per relationship, distinguishing the number of *activities with* lags/leads from the number of lags/leads); F–S predecessor leads exceeding remaining duration; total/overallocated resources; max units per resource (individuals between 0–100% of full time); milestones with assignments (a defect — milestones have no duration); resourced vs. unresourced detail activities.
- **BP4 (durations):** dissimilar time units (all should be the same, preferably days); activities/milestones starting or finishing on weekends/holidays; durations shorter or longer than the reporting period; average and median remaining-activity duration.
- **BP5 (traceability):** no standard numeric measures — vertical traceability is checked by confirming lower-level dates fall within higher-level dates and that forecasted milestone dates match management documents; horizontal traceability is tested by inflating durations by improbable amounts (500 or 1,000 days) and observing whether milestones move and the critical path changes.
- **BP6 (critical path):** trace driving activities back from the program finish milestone; count of critical activities (a near-100% ratio suggests an overly serial, resource-limited schedule); critical LOE activities (a defect — LOE cannot be critical); lags/leads on the critical path; critical activities with hard constraints.
- **BP7 (total float):** in-progress critical activities (at least one should exist); dissimilar float units; relatively high float; **negative total float** (constraint date earlier than calculated late finish, often from out-of-sequence work); average and median float.
- **BP8 (schedule risk analysis):** limited to confirming risk data exist — fields storing optimistic/most-likely/pessimistic durations, correlation measures, and contingency activities.
- **BP9 (updating with progress):** in-progress count; forecasted start/finish dates in the past with no actual; actual start/finish dates in the future; out-of-sequence activities — all judged against the schedule's status date.
- **BP10 (baseline):** activities with/without baseline dates; counts forecast or actually starting/finishing early, on time, or late versus baseline; average/median start and finish variance; and the **baseline execution index (BEI)** — the ratio of actual completed detail activities to those planned to finish, where 1 means on plan, below 1 means fewer completed than planned, and above 1 means more.

### Industry and agency comparisons (Appendix VII)

GAO found broad agreement between its best practices and the major guidance sources, with one recurring difference: **all but one of the reviewed documents do not require assigning resources to activities** — only DHS's Scheduling Handbook states the IMS should be resource loaded. A schedule that conforms only to DoD's IMS Data Item Description (DID) 81650, or only to the IPMR's DID 81861, will fall short of the full set of GAO best practices, because neither DID requires government/contractor integration or resource assignment. Source-by-source:

- **DCMA** is the DOD executive agent for EVM systems; it conducts contractor surveillance and uses a **14-Point Assessment (14PA)**: logic, leads, lags, relationship types, hard constraints, high float, negative float, high duration, invalid dates, resources, missed tasks, critical path test, critical path length index, and baseline execution index. Several measures carry thresholds (for example, no more than 5% of remaining tasks missing predecessor or successor logic), but **these thresholds are not compliance triggers** — they are starting points for objective analysis. DCMA assesses only on-contract scope, loads resources only if the contract requires it, and does not assess a schedule risk analysis unless contractually required. Salient differences from GAO: DCMA allows unlimited soft date constraints (GAO recommends minimizing and justifying them), gives no guidance on conducting SRAs properly, and does not call for a schedule basis document or narrative. In other respects DCMA goes *beyond* GAO — validating control-account budgets and cost/schedule integration.

- **NAVAIR 4.2 (Integrated Project Management Division, 4.2.3)** uses an **11-point assessment** in its Toolkit/Schedule Metrics Guide covering IMS completeness, critical target dates, sequencing, architecture/integration, constraints/leads/lags, task detail, resource adequacy, critical path, slack reasonableness, status/forecasting, and risk. It does not verify government/contractor integration or resource loading because it interprets ANSI/EIA-748 and DIDs 81650/81861. NAVAIR does promote integration through links between the contractor IMS and a government-controlled **integrated government schedule (IGS)** with givers and receivers, and has an initiative to develop resource loading for the IGS. The Toolkit describes 76 measures, many being current-vs-baseline trend comparisons, and like GAO it avoids tripwires.

- **DHS Scheduling Handbook** (Program Management Center of Excellence) aligns with GAO's ten best practices with no substantive differences; it includes a scorecard checking the four reliable-schedule characteristics — comprehensive, well-constructed, credible, controlled — reviewed by DHS's PARM office before acquisition decision events.

- **NASA Schedule Management Handbook (NASA/SP-2010-3403)** shows few differences; it does not require resource-loaded schedules but emphasizes loading and assigning resources within the schedule for cost/schedule integration, warning that baselining without resource loading and leveling assumes significant risk. NASA's Cost Estimating Handbook adds the **joint confidence level (JCL)** — a quantitative probability analysis combining cost, schedule, and risk into one picture, introduced in 2009; NASA mission directorates plan and budget to a 70% JCL (or a Decision-Authority-approved alternative that must be justified and documented). JCL is not covered by GAO's guide.

- **NDIA PASEG (Release 2.0, June 2012)** is supplemental and subordinate to DIDs 81650/81861 and to contractor procedures; it agrees with GAO on capturing all work and integrating customer/government schedules, and on assigning resources (recommending the in-schedule method, accepting external-cost-system alignment, but — unlike GAO — also describing a text-field method GAO does not consider a best practice). The PASEG's eight **Generally Accepted Scheduling Principles (GASP)** — complete, traceable, transparent, statused, predictive, usable, resourced, controlled — map to GAO best practices, with the single gap that Best Practice 8 (Schedule Risk Analysis) has no corresponding GASP principle.

### Data collection and case-study grounding (Appendices VIII–IX)

Appendix VIII lists the fifteen artifacts an assessor should request, anchored by item 1: the baseline IMS and latest updated IMS **in native software file format** — PDFs and presentation slides are explicitly *not* valid schedule files. The remaining items include a schedule dictionary, integrated master plan, WBS and dictionary, statement of work, cross-walks among WBS/contractor WBS/SOW/activities, critical-path designations, schedule basis and narrative documentation, basis of estimate, program management review briefings, governing scheduling guidance, SRA documentation, a risk management plan and current risk register, and a description of the change control process.

Appendix IX grounds the guide's 19 case studies in 11 GAO reports spanning DOD ERP modernization (the cancelled Air Force ECSS, where the lack of an IMS was cited as a major cause of failure; and DEAMS), DHS border surveillance and immigration benefits, VA construction cost growth, DOE/NNSA nuclear nonproliferation (MOX), TSA's TWIC and Electronic Baggage Screening, FAA NextGen acquisitions, Coast Guard Deepwater, NOAA/NASA polar-orbiting satellites (NPOESS/JPSS), and the 2010 Census. The recurring finding across these reports is that schedules failing GAO best practices left agencies unable to forecast completion dates with confidence.

## Mental Models

**The schedule as an arithmetic machine.** Network logic plus durations deterministically produce early dates (forward pass, adding durations), late dates (backward pass, subtracting from the end), total float (late minus early), and the critical path (zero float). Reliability is auditable precisely because these are calculations — an assessor can recompute them and challenge any constraint or link that distorts the result.

**Latest-in, earliest-out.** The two rules that govern multi-relationship nodes mirror each other: on the forward pass, an activity's early start is driven by the *latest* early finish of its predecessors; on the backward pass, an activity's late finish is driven by the *earliest* late start of its successors. Hold these two and the rest of the pass arithmetic follows.

**Constraint by effect, not by name.** Software vendors rename the same constraint a dozen ways, so reason about which pass it touches and whether it pins early dates, late dates, or both. A constraint is only "active" when it is actually holding an activity back (its scheduled date equals the constraint date); an SNET earlier than the activity's start is inert.

**Float is shared along a path and bought with resources.** Total float belongs to a chain, not a single activity — relieve a bottleneck (add a resource, shorten a duration) and the float created propagates to predecessors on that path. This reframes resource decisions as float-management decisions.

**Earned value as a common currency.** EVM converts feet of cable, square feet of sheet metal, and design hours into one unit (dollars or labor hours), so dissimilar efforts roll up into a single read of program health — but only if work is decomposed into well-defined, objectively measurable tasks, which is exactly why control accounts, work packages, and objective measures matter.

**Measures inform judgment; they do not adjudicate.** GAO, DCMA, NAVAIR, and the PASEG all refuse to let a number pass or fail a schedule by itself. A measure flags where to look; the analyst weighs severity, context, and documented justification. Severity beats quantity — one logic error can poison an entire network of float values.

**Different lens, different scope.** A GAO assessment and a DCMA assessment ask different questions: GAO judges the full program including government effort and resource loading; DCMA judges contractor adherence to ANSI/EIA-748 and the contract deliverable. Knowing which lens is in use tells you which best practices will even be in scope.

## Anti-patterns

The source names these failure conditions in the reference appendices:

- **Duration-only statusing under EVM.** Updating only activity duration records the passage of time, not work accomplished, and can be easily misconstrued; EVM requires objective measures so work performed can be compared to work planned.
- **Misplaced or stranded effort outside control accounts.** SLPPs that linger instead of being assigned to control accounts at the earliest opportunity, and planning packages treated as if they were detail-planned near-term work, distort the baseline.
- **Resourcing milestones or making LOE critical.** Milestones should never be assigned resources because they have no duration; a critical path must not include LOE activities because LOE is not discrete effort. Both appear in the measures as defects to flag.
- **Dangling activities.** Remaining detail activities or milestones with no predecessor on their start date or no successor off their finish date break the network's ability to react logically.
- **Hard constraints on the critical path.** Fixing activity dates with hard constraints at once tangles the critical-path math and undermines the very reason for scheduling with CPM.
- **Negative total float / out-of-sequence work.** Negative float means a constraint date is earlier than the calculated late finish — often the symptom of activities performed out of sequence — and should always be questioned.
- **Forecast dates in the past or actuals in the future.** Relative to the status date, forecasted starts/finishes should not lie in the past without an actual, and actual starts/finishes should not lie in the future; such anomalies indicate a mis-statused schedule.
- **ALAP misuse.** Forcing an activity to start as late as possible immediately eliminates its available float and, depending on the software, can strip float from successor activities as well.
- **Invalid schedule file formats.** Submitting PDFs or presentation slides instead of a native software schedule file is explicitly rejected — the assessor cannot recompute the network from them.

## Key Takeaways

- In an EVM environment the schedule becomes the time-phasing engine for the performance measurement baseline; the whole schedule must be baselined and is best fully resource loaded, with work decomposed into control accounts, work packages, planning packages, and SLPPs.
- GAO maps specific best practices to specific ANSI/EIA-748 guidelines, but defers full EVM detail to the GAO Cost Guide (GAO-09-3SP), Chapters 18–20.
- The forward pass (EF = ES + duration − 1) and backward pass (LS = LF − duration + 1) deterministically yield total float (TF = LS − ES = LF − EF) and the critical path; multi-predecessor early starts take the latest predecessor EF, multi-successor late finishes take the earliest successor LS.
- Date constraints have standardized DOD/UN/CEFACT names but matter only for their effect on the forward/backward pass; reason about which pass each touches, treat a constraint as active only when it actually holds an activity back, and beware ALAP and negative-float-permitting software behaviors.
- Schedule health is assessed quantitatively through per-best-practice data measures with deliberately no tripwires; severity of an error outranks its quantity because one error can compromise the whole network.
- GAO's best practices substantially agree with DCMA's 14PA, NAVAIR's 11-point Toolkit, the DHS Handbook, NASA's Handbook, and the NDIA PASEG/GASP — the recurring divergence being that most do not require resource loading or government/contractor integration, both rooted in DIDs 81650/81861.
- An assessor should request fifteen specific artifacts, starting with the baseline and current IMS in native file format; PDFs and slides are not acceptable schedule files.

## Connects To

- **Earlier chapters of GAO-16-89G (the ten best practices)** — Appendix III explicitly cross-references Best Practices 1, 3, 9, and 10; Appendix VI organizes every quantitative measure by best practice; Appendix VII maps each best practice to external guidance. This chapter is the calculational and evidentiary backbone for those narrative practices.
- **GAO Cost Estimating and Assessment Guide (GAO-09-3SP)** — the companion volume carrying full EVM, PMB, IBR, and objective-measure detail that the schedule guide defers to.
- **ANSI/EIA-748 and FAR Subpart 34.2** — the EVM standard (32 guidelines) and the regulatory trigger that put a program into the EVM environment where these scheduling overlays apply.
- **DOD PARCA, UN/CEFACT XML schema, and the IPMR (DI-MGMT-81861) / IMS DID 81650** — the data-exchange and data-item standards that fix constraint naming and define the contractor-IMS scope that drives the resource-loading and integration differences in Appendix VII.
- **Critical Path Method and total float (introduced in Chapter 1)** — Appendix IV is the worked derivation of the CPM dates and float that the introductory chapter named.
- **DCMA 14PA, NAVAIR Toolkit, DHS Scheduling Handbook, NASA Schedule Management Handbook (with JCL), and NDIA PASEG (with GASP)** — the external assessment frameworks an auditor will encounter alongside GAO criteria; knowing their scope clarifies which best practices are in play.
- **Schedule risk analysis (Best Practice 8)** — flagged here as the one practice with no corresponding GASP principle and limited quantitative measures, and the practice DCMA assesses only when contractually required.

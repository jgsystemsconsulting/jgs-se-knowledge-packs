# Glossary — NASA Schedule Management Handbook

Key terms used across this pack, alphabetical, each tagged with the chapter(s) that
develop it. Definitions are restated in this pack's own words; they paraphrase the
handbook rather than quote it.

---

**Activity Attributes** (ch02, ch04) — The coded data fields attached to each IMS
activity in the scheduling tool. The handbook groups them into cost-interface,
risk-management-interface, P/p-defined, and intrinsic families; defining them up front
is best practice because retrofitting fields onto a populated schedule is costly.

**Activity Duration Impact** (ch06) — The most common way to model a discrete risk in an
SRA: a zero-duration delay milestone is inserted between an at-risk activity and its
successor, and a sampled impact becomes that milestone's duration when the risk's
likelihood draw fires.

**Affordability** (ch05) — One of the four Dimensions of Schedule Reliability: whether the
plan can be executed within its funding context. Distinct from the Resource Integration
Check, which tests consistency, not adequacy.

**Agency Baseline Commitment (ABC)** (ch01, ch06, ch07) — NASA's external commitment to
OMB and Congress on development cost and/or schedule, set at KDP C and recorded in a
Decision Memorandum. For space-flight P/ps it is typically the planned launch date.

**Analysis Schedule** (ch01, ch04, ch06) — A summarized, traceable surrogate for the IMS,
built to make risk/cost/uncertainty loading and simulation tractable. It must be shown
to emulate the IMS (same major-milestone dates, same critical paths).

**Baseline Execution Index (BEI)** (ch04, ch07) — An actual-to-baseline completion ratio
answering "is work getting done?" Does not distinguish simple from complex activities.

**Basis Check** (ch05) — The 2nd-Tier assessment procedure that tests the quality of the
estimate behind each discrete schedule element against a replicability standard.

**Basis of Estimate, Schedule (BoE)** (ch03, ch05, ch08) — The documented ground rules,
assumptions, and drivers behind the schedule estimate — a reproducibility dossier with
no fixed template, keyed in maturity to life-cycle reviews. It is the living evidence
base for assessment and the "primary agent of change."

**Control Account** (ch03) — The intersection of one WBS element and one responsible
organization on the RAM; the point where budget, actual cost, and earned value
accumulate. Owned by a Control Account Manager (CAM).

**Correlation** (ch06) — A measure (0.0–1.0) of how strongly variables move together in an
SRA; assessed always, defaulted to 0.3 absent data. Ignoring it understates variance and
overstates risk.

**Cost Breakdown Structure (CBS / RBS)** (ch03) — The "how much" structure: the hierarchy
sorting resources (labor, travel, materials, equipment, other) into control accounts.

**Critical Path** (ch04, ch05, ch08) — The longest continuous chain of logically linked
activities from time-now to completion, carrying the least float; it sets the earliest
finish. Distinct from a driving path and from a designated "critical activity."

**Critical Path Length Index (CPLI)** (ch07) — (Remaining CP length + total float) ÷
remaining CP length; the efficiency needed to finish a milestone on time. A global
measure that cannot pinpoint offending tasks.

**Critical Path Method (CPM)** (ch01, ch02, ch04) — The network technique that finds the
minimum P/p duration by computing the longest path; NASA's best-practice method, used in
an expanded form that integrates cost, risk, and resources.

**Criticality** (ch06) — In an SRA, the percentage of Monte Carlo iterations an activity
landed on the critical path ("how often") — the basis for finding stochastic critical
paths.

**Cruciality** (ch06) — Duration sensitivity multiplied by criticality ("how big and how
often").

**Dimensions of Schedule Reliability** (ch05) — NASA's umbrella quality construct:
Comprehensiveness, Construction, Realism, Affordability — four near-orthogonal axes,
each posed as a question.

**Driving Path** (ch04, ch05) — The critical path to an interim end item (a milestone or
delivery) other than P/p completion, defined by zero free float.

**Earned Schedule (ES)** (ch04, ch07) — A time-based reformulation of schedule performance
that keeps diagnostic value near completion, where cost-denominated SPI loses it; SPIt =
ES ÷ AT.

**Float (Slack)** (ch04, ch07) — The automatic CPM calculation of how many days an activity
can slip before affecting the critical path (free and total flavors). Calculated, not
reasoned — contrast with margin.

**Hammock** (ch06) — A summary task anchored start-to-start to a band's first activity and
finish-to-finish to its last; used to cost-load a schedule for an ICSRA so cost expands
and contracts with duration.

**Hit or Miss Index (HMI)** (ch04, ch07) — Baseline tasks finished on/early versus those
baselined to finish in the period: "is the right work getting done?" Value cannot exceed 1.

**Integrated Baseline Review (IBR)** (ch07) — A risk-based review of the supplier's PMB
confirming cost, schedule, and risk are properly linked before KDP C; required when EVM
applies.

**Integrated Cost-Schedule Risk Analysis (ICSRA)** (ch01, ch02, ch06, ch07) — An SRA
extended with a cost model and cost risks; produces cost S-curves and the Joint
Confidence Level.

**Integrated Master Plan (IMP)** (ch03) — A contractor-oriented, event/accomplishment/
criteria plan whose events ripen on maturity rather than dates; not a NASA-required
product.

**Integrated Master Schedule (IMS)** (ch01, ch03, ch04) — "The schedule": a single
time-phased, logically linked network of all approved work, detailed enough to expose the
longest path. NASA's schedule requirements are written against it; all other products
derive from it.

**Joint Confidence Level (JCL)** (ch01, ch06) — The probability of finishing at or under
both the target cost and the target schedule date simultaneously; required at defined KDPs
(70% for single-project programs and projects above set cost thresholds).

**Key Decision Point (KDP)** (ch01, ch08) — A life-cycle gate at which the Decision
Authority approves progression; schedule detail, products, and analysis rigor scale up
across KDPs.

**Level of Effort (LOE)** (ch04, ch07) — Support work with no discrete product; it tracks
the duration of what it supports, adds no time of its own, and must never sit on the
critical path or show a schedule variance.

**Life Cycle Review (LCR)** (ch01, ch08) — An independent review (SRR, PDR, CDR, etc.)
assessing a P/p's technical and programmatic health at key points, supported by an SRB or
IRT.

**Management Agreement (MA)** (ch06, ch07) — The internal cost/schedule agreement among
Center, Mission Directorate, P/p, and Administrator, usually set ahead of the ABC; the
MA-to-ABC gap holds schedule margin.

**Margin** (ch04, ch07) — A deliberately planned quantity of working days, sized from
quantified risk and uncertainty and held as a lien against MR/UFE. NASA prefers managing
margin over float because margin ties directly to risk adequacy. Distinct from contingency
(non-working days).

**Merge Bias** (ch06) — The tendency of a convergence milestone fed by many parallel paths
to finish late, because every feeding path must finish on time; worsened by low
correlation between paths.

**Milestone Registry** (ch02) — A controlled SMP-appendix table of key dates, holding
notification and control milestones, with MA and ABC dates added at KDP B.

**Monte Carlo Simulation** (ch06, ch07) — The engine behind SRA/ICSRA; a faithful
calculator whose value lives entirely in the quality of its inputs and the discipline of
reading its outputs.

**Notification milestone** (ch02, ch07) — A P/p-owned milestone the P/p may move but must
notify sponsors about. Contrast control milestone (sponsor-owned, immovable by the P/p).

**Organizational Breakdown Structure (OBS)** (ch03) — The "who" structure: the hierarchy
showing which organization performs the work.

**Performance Measurement Baseline (PMB)** (ch01, ch03, ch07) — The time-phased cost plan
for all authorized scope against which performance is measured; excludes UFE.

**Replan vs. Rebaseline** (ch07) — A replan re-schedules to-go work, generally internal
(PM authority within the MA); a rebaseline changes the ABC and is external, requiring
Decision Authority and OMB/Congress involvement.

**Resource Loading** (ch04, ch06) — Assigning specific workforce, equipment, and
consumables to activities (the grassroots approach, required when a JCL is required);
cost loading is an accepted substitute, budget loading is discouraged.

**Risk Driver method** (ch06) — Modeling risks/uncertainties as multiplicative factors
(Min/M-L/Max percentages) assigned to many activities at once; suited to higher-level
strategic risks and auto-correlating shared factors.

**Rolling Wave Planning** (ch02, ch04) — Progressive elaboration: near-term work is
detailed, far-term work sits at planning-package level and is elaborated as it approaches.
Must not defer detail that is already known.

**Schedule Estimating Relationships (SERs)** (ch04, ch06) — The schedule analogue of cost
estimating relationships: duration as a mathematical function of technical or cost drivers
(used in SMART and NICM).

**Schedule Management Plan (SMP)** (ch01, ch02) — The governing plan for the whole
function, decomposed into four sub-plans (Development; Assessment & Analysis; Maintenance
& Control; Documentation & Communication). A guidance plan, not a scheduling cookbook.

**Schedule Performance Index (SPI)** (ch04, ch07) — BCWP ÷ BCWS, a cost-denominated
schedule measure that loses diagnostic value near completion (heads to 1.0 once budget is
spent).

**Schedule Reliability Matrix** (ch05) — The master traceability artifact mapping each
reliability dimension → sub-dimension → question set → tiered procedure.

**Schedule Risk Analysis (SRA)** (ch01, ch06, ch07) — A simulation-based analysis of how
duration uncertainties and discrete risks propagate through the IMS to give the
probability of finishing by planned dates.

**Sensitivity** (ch06) — How strongly a task's or risk's variation correlates with overall
P/p duration or cost ("how big"); shown in tornado charts.

**Shock Test** (ch05) — A structural-integrity probe inside the Critical Path and
Structural Check: perturb durations across the network to confirm horizontal traceability
and proper dynamic behavior, isolating defects one at a time.

**Standing Review Board (SRB) / Independent Review Team (IRT)** (ch01, ch08) — The
independent bodies that assess a P/p at LCRs; the Schedule Analyst is the focal point for
the SRB.

**Stochastic Critical Path** (ch06, ch07) — A path that becomes critical in a meaningful
fraction of Monte Carlo iterations though it may not be the deterministic critical path;
surfaced only by SRA.

**Total Float Consumption Index (TFCI)** (ch07) — A PASEG measure projecting a finish date
from the average rate of float consumption; intended for delinquent P/ps only.

**Unallocated Future Expense (UFE)** (ch03, ch07) — Budget held deliberately outside the
PMB; NPR 7120.5 uses "schedule margin" and "UFE" in place of the obsolete "reserve."

**Uncertainty vs. Risk** (ch06) — Uncertainty is the inherent indefiniteness of a plan,
applied in every simulation iteration with no likelihood gate; risk combines a likelihood
and a consequence of a discrete future event.

**Vertical / Horizontal Traceability** (ch04, ch05) — Vertical: the schedule nests into the
WBS/OBS hierarchy. Horizontal: every task has at least one predecessor and one successor
(start/finish milestones excepted) so forecasts cascade correctly.

**Work Breakdown Structure (WBS)** (ch01, ch03) — The "what" structure: the
product-oriented hierarchical decomposition of total scope; the spine of traceability to
which every IMS task carries a WBS code.

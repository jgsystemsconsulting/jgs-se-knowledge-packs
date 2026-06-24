# Chapter — Capturing All Activities and Sequencing the Network (Best Practices 1–2)

## Core Idea

The first two GAO best practices answer two foundational questions about a program schedule: *is all the work in it?* and *is that work joined together correctly?* Best Practice 1 holds that the Integrated Master Schedule (IMS) must reflect every activity defined in the program's work breakdown structure (WBS) — all steps, events, required work, and outcomes that deliver what the WBS describes — regardless of who performs the work. Best Practice 2 holds that those captured activities must then be logically sequenced and linked, with a predecessor that starts or finishes before each successor, so the network can forecast the dates of future activities and key events from the status of work already done or under way.

The two practices are deliberately ordered and tightly coupled. If activities are missing from the schedule, none of the other best practices can be satisfied: no one can confirm the work is ordered correctly, that resources are right, that the critical path is valid, or that a risk analysis covers all the risk. And once the work is captured, sequencing turns a static list into a predictive model — a network that recalculates start and finish dates automatically as durations change and progress is recorded. The unifying thesis is that **completeness comes first and connectivity comes second: capture every piece of work, then wire it together with sound logic, and only then does the schedule become a reliable model of how the program will actually be executed.**

## Frameworks Introduced (exact source names, when/how)

- **Best Practice 1: Capturing All Activities** — The schedule should reflect all activities defined in the program's WBS, covering work both the owner and the contractors perform. Introduced as the practice that makes the schedule a complete agreement for executing the program.

- **Best Practice 2: Sequencing All Activities** — The schedule should be planned so critical dates can be met by logically sequencing and linking activities (a predecessor must start or finish before its successor), with date constraints and lags minimized and justified. Introduced as the practice that turns the captured activity set into a forecasting network.

- **Integrated Master Schedule (IMS)** — Framed here not as the prime contractor's schedule but as the collection point for *all* work scopes: government, contractor, subcontractor, and key-vendor effort. The contractor schedule is positioned as a subset of the overall government program effort, and integrating both into one comprehensive plan is assigned to the government program management office.

- **Work Breakdown Structure (WBS)** and **WBS dictionary** — The WBS is named the cornerstone of every program, decomposing the end product into successively finer deliverables down to a level suitable for management control. The guide requires a single WBS per program, matched to the WBS used for the cost estimate, and a companion WBS dictionary that defines the scope of each element (and therefore the scope of related schedule activities).

- **Statement of Work (SOW)** — Introduced as the document (directly or by reference) that sets out a contractor's performance requirements and contract scope; activities in a contractor's schedule should trace to it. The guide notes a Statement of Objectives (SOO) and Performance Work Statement (PWS) may serve the same contractual role.

- **Milestone, detail, summary, and level-of-effort (LOE) activities** — The four building blocks of represented effort. Milestones are zero-duration time points (no resources consumed); detail activities are the lowest-WBS-level discrete work; summary activities are roll-up grouping elements that derive their dates from below; LOE activities represent effort with no measurable output, supported by **"hammock" activities** in some software.

- **Activity codes, the Organizational Breakdown Structure (OBS), and the activity owner** — Coding schemes (WBS element, contractor, CLIN, control account, SOW paragraph, IPT, phase, etc.) stored in custom fields; the OBS describing the hierarchy that resources the WBS work; and a named owner accountable for each activity.

- **Integrated Master Plan (IMP)** — Noted (DOD context) as an event-based plan tracking accomplishments and completion criteria, from which the IMS flows and to which it is traceable; typically contractually binding when used.

- **Predecessor/successor logic and the three relationship types** — Finish-to-start (F–S), start-to-start (S–S), and finish-to-finish (F–F), with start-to-finish (S–F) named as a discouraged theoretical fourth. F–S is the default and should dominate a detailed schedule.

- **Forward pass / backward pass, early and late dates, total float** — The forward pass computes early start/finish by adding durations forward from day one (and yields the critical path); the backward pass computes late start/finish by subtracting durations from late finishes. The gap between early and late dates is total float (slack).

- **Date constraints** — A named taxonomy of overrides on calculated dates: SNET, FNET (soft / past-limiting), SNLT, FNLT, MSON, MFON (hard / future-limiting or mandatory). The guide states it follows constraint names consistent with the September 2013 DOD data-exchange instructions supplementing the UN/CEFACT XML schema 09B.

- **Lags and leads** — A lag is a delay (passage of time, no resources) between two activities; a lead is a negative lag that accelerates a successor. Both are flagged as static and prone to abuse.

- **Reference / schedule visibility activities** — Representative activities that are not part of project scope and carry no assigned resources, yet can affect program activities — the guide's preferred substitute for date-constrained milestones modeling external supply.

- **Path convergence and the merge point** — Joining several parallel predecessors into one successor; the basis of "merge bias," treated in depth under Best Practice 8.

## Key Concepts

**Capture all effort, regardless of performer.** The IMS must hold every activity needed to finish the program no matter who owns it. Beyond the full contract life cycle, that includes government effort such as design reviews, milestone decisions, receipt of government-furnished equipment, and testing — plus activities only the government can do, like accepting deliveries, obtaining permits, and running program reviews. Because a government review can gate the start of a program phase, schedulers must know how long such government activities take. Agreed risk-mitigation activities also belong in the schedule as discrete, resourced activities. Everyone affected should agree on which final actions (for example, financial closeout, dispute resolution, final payment) must precede the finish milestone.

**The four activity types.** *Milestones* mark key events, have zero duration, consume no resources, and every schedule needs exactly one start and one finish milestone — a plan that does not emanate from a single start and terminate at a single finish is improperly built and can produce a wrong critical path. *Detail activities* sit at the lowest WBS level, represent discrete measurable work, carry durations and resources, and are logically linked into sequential and parallel paths. *Summary activities* are roll-up grouping elements that take their dates from lower-level activities and therefore should never be linked to or from other activities. *LOE activities* represent management or oversight effort with no measurable output; their progress is measured by time passing, not discrete accomplishment.

**Milestones should be used sparingly.** A best practice is to reserve milestones for major events or deliverables, each with clear completion conditions. Too many milestones can mask the activities that achieve them, make the delay-driving sequences harder to spot, and — because milestones carry no measurable progress — prevent recorded progress from forecasting key event dates. Work should be represented by detail activities, not milestones.

**The WBS is the schedule's spine.** The WBS decomposes the program into finite deliverables down to a manageable level; a product-oriented WBS lets a program track cost and schedule by deliverable and isolate the root cause of overruns. The schedule answers *how* the program produces what the WBS defines. Every schedule activity should trace to an appropriate WBS element, and every WBS element should have at least one activity. The WBS dictionary defines each element's scope, so activities tied to undefined or no WBS elements signal undefined or unassigned scope.

**Naming and coding discipline.** Activity names should be unique, descriptive, present-tense verb-noun phrases ("review basis of estimate," "test level 4 equipment") that identify their product without needing the parent summary or predecessor for context — essential because filtering (for example, to show only critical-path activities) strips that context away. Milestone names should reference an event or deliverable. Separately, activity *codes* (WBS element, contractor, CLIN, control account, SOW paragraph, OBS reference, IPT, owner, and similar) belong in custom fields, not appended to names; consistent coding supports vertical integration and fast filtering, sorting, and auditing. Every activity should also name an owner responsible for scope, entrance/exit criteria, status updates, and explaining variances.

**Schedule levels and integration.** The IMS spans summary, intermediate, and detailed schedules; ideally one schedule serves all three by rolling lower effort up into summary activities or higher WBS elements. The levels must respond dynamically: delays at the bottom must roll immediately up to intermediate and summary views, so a summary presented to senior management never shows on-time finishes when the lower-level milestones are already late. When government and contractor use different scheduling software, the parties must define a process to preserve integrity between formats and to verify and validate converted data on every update; "giver/receiver" milestones (detailed under Best Practice 5) align dates across the integrated schedules.

**Detail level should match information available.** Schedule detail should reflect what is known about the work to be done. Too high a level can hide risk inherent in lower-level activities; too much detail makes progress hard to manage and can convolute critical-path calculation. Near-term effort is planned in greater detail than the distant future, which appears as long-term planning packages — a summarization of far-future work at lower specificity (the rolling-wave approach treated under Best Practice 3).

**Predecessor/successor logic and the three relationship forms.** Activities relate as predecessors and successors to depict sequence; relationships can be internal (within a schedule) or external (between schedules). The three usable forms: *F–S* (successor cannot start until predecessor finishes — the intuitive default), *S–S* (successor cannot start until predecessor starts), and *F–F* (successor cannot finish until predecessor finishes). S–S and F–F imply parallel or overlapping work and are a valid overlap-modeling technique, but an overabundance in a detailed schedule can signal optimism, shortcuts, or a schedule whose detail has not matured — and they are prone to producing "dangling" logic. F–S should be the majority because most work is serial and F–S links are easy to trace.

**Early and late dates from forward and backward passes.** Ideally only the program start date is entered; all other dates come from network logic. The forward pass adds durations forward to set early start and early finish for each activity and reveals the longest continuous path (the critical path). The backward pass subtracts durations from late finishes to set late start and late finish — the latest an activity can start or finish without slipping the program. The difference between an activity's early and late dates is its total float (the foundation of Best Practice 7).

**Complete logic; no incomplete, circular, redundant, or dangling logic.** As a rule, every activity should have at least one predecessor and one successor, the natural exceptions being the start milestone (no predecessor) and finish milestone (no successor); any other missing link must be justified in the documentation. Networks should be free of *circular* logic (two activities depending on each other — an impossible endless loop), *redundant* logic (an extra A→C link when A→B→C already exists), and *dangling* logic. Dangling logic is an improper tie to an activity's start or finish: a start-date dangle occurs when an activity with an F–F predecessor has nothing (F–S or S–S) driving its start; a finish-date dangle occurs when an activity with an S–S successor has nothing (F–S or F–F) being driven by its finish. The diagnostic questions: if nothing drives the start, why not start earlier? If the finish drives nothing, why finish at all? Dangling logic is more dangerous for detail activities than for milestones, which share start and finish dates.

**Summary activities carry no logic.** Because summary activities derive their dates from below, they need no logic relationships. Linking summaries hinders vertical traceability (a summary's dates can be misrepresented at higher levels if not driven by its children) and obscures the real sequence of lower-level work from management.

**Date constraints: soft vs. hard.** Constraints override calculated dates and should be used only when necessary and justified, typically to model an external event's effect. *Soft* (past-limiting) constraints — SNET and FNET — let activities slip later but not start/finish earlier than the date. *Hard* (future-limiting / mandatory) constraints — SNLT, FNLT, MSON, MFON — prevent slipping; the mandatory pair (MSON/MFON) is the most rigid, setting early and late dates equal, eliminating float, and making the activity instantly critical. Hard constraints should never appear in the baseline schedule; if unavoidable they must be justified by a controlling event outside the schedule in the basis document. (These definitions assume forward scheduling; under backward scheduling — generally not a best practice because it removes all float — a constraint like FNET becomes hard.)

**Constraints are often substitutes for logic.** SNET constraints legitimately fit a fixed earliest start with no other dependency (cash flow, an external product), but supplier or government deliverables are better modeled as reference/schedule-visibility activities than as date-constrained milestones, which can understate procurement risk. Using SNET to allocate scarce resources is discouraged: it blocks time savings, bakes sequential logic in permanently even after resources are added, and demands constant manual upkeep (resource calendars are the better mechanism, per Best Practices 3–4). SNET/FNET constraints that are not actively constraining are meaningless and should be deleted. Many constrained activities signal a poorly planned, possibly infeasible schedule and can distort risk analysis because they override logic.

**Lags and leads are static.** A lag delays a successor with no effort or resources (for example, waiting for concrete to cure). A lead (negative lag) accelerates a successor and implies negative time and improbable foresight — leads are often unnecessary and can cause logic failures when a lead exceeds the successor's duration, even injecting artificial float. Both are static: they do not respond to progress or resources and must be updated manually, which becomes error-prone at scale. The guide distinguishes the *number of lags/leads* in a schedule from the *number of activities affected by them* — the latter indicating how disruptive manual updating will be. Lags suit summary and intermediate schedules where interface points are not yet defined, but should not stand in for effort, procurement, or risk margin in detailed schedules. The preferred fix is to break activities into smaller tasks and find real F–S predecessors and successors; a forced start date is better handled with a SNET constraint than a lag.

**Path convergence and merge bias.** Joining many parallel predecessors into one successor (a merge point) is risky because risk there is multiplicative — as predecessors multiply, the probability that the successor starts on time falls quickly toward zero. Heavily converged activities should be examined for whether all predecessors are needed and whether alternative logic could relink some; predecessors with large total float may mean activities are sequenced sub-optimally or that a milestone is being used to "tie off" loosely related work. Because most work is serial, the bulk of relationships should be F–S in a waterfall flow; excessive parallelism signals an aggressive or unrealistic plan. (Merge bias is detailed under Best Practice 8.)

## Mental Models

**Capture-then-connect ordering.** Best Practice 1 fills the box with every piece of work; Best Practice 2 wires the pieces together. Connectivity is worthless if the box is incomplete, so completeness is the prerequisite — and because the practices are interrelated, a gap in capturing all activities propagates into sequencing, resourcing, critical-path, and risk failures downstream.

**The schedule as a single river with one source and one mouth.** Every plan should flow from a single start milestone and empty into a single finish milestone. A plan with multiple unconnected origins or terminations is malformed and can compute a false critical path — the same way a river without a defined source and mouth has no measurable length.

**Activities as instructions, names as the instruction text.** An activity is essentially an instruction for someone to act, so its name must read like one: present-tense verb-noun, self-identifying, unambiguous even when pulled out of context by a filter. "Inspection" on a critical-path report is useless; "drywall screw inspection" is actionable. Codes are metadata about the instruction; they live in fields, not in the instruction text.

**Forward pass / backward pass as two sweeps.** Sweep forward adding durations to learn the earliest each activity *can* happen and how long the whole program *must* take. Sweep backward subtracting durations to learn the latest each activity *must* happen to hit the end date. The space between the two sweeps for any activity is its float.

**Logic vs. constraints vs. lags — a preference hierarchy.** Prefer genuine predecessor/successor logic that lets dates move dynamically. Reach for a constraint only to model a real external event, and prefer a soft constraint or a reference activity over a hard one. Treat a lag as a last resort for a real, justified passage of time — and a lead as almost always a sign the activity should have been split instead. Each step down the hierarchy trades away the schedule's ability to react to reality.

**Float as the attention budget.** Total float measures how much an activity can slip before it threatens the end date. The less float, the more scrutiny it earns; hard constraints are dangerous precisely because they zero out float and silently force activities onto the critical path.

**Merge points as probability bottlenecks.** Picture many parallel paths all required to land before one successor can begin. Each path has its own chance of being late, and those chances compound, so a heavily converged successor is statistically unlikely to start on time even if each predecessor looks healthy alone.

**Schedule levels as one dataset, many views.** The summary, intermediate, and detailed schedules are ideally the same data rolled up differently. Decision-makers read the strategic view; specialists read their slice of detail; both come from one schedule so a delay at the bottom cannot hide behind a green summary at the top.

*(Per the source caveat, the embedded third-party / illustrative figures in this slice — the WBS-and-scheduling diagram adapted from a copyrighted source, and the worked Gantt examples of milestones, detail/summary activities, relationship types, early/late dates, dangling-logic before/after, linked summaries, lags, leads, and lag enumeration — should be redrawn rather than reproduced. The text above renders their content; recreate any visuals natively if needed.)*

## Anti-patterns

The source explicitly names these failure modes:

- **Missing effort or missing increments.** Omitting any work for any deliverable — government or contractor — or planning only one block/increment/phase of a multiphase program. A schedule that stops short cannot reliably forecast the program finish date (illustrated by the DEAMS schedule that excluded later releases and a second increment, and by partially integrated ERP schedules where government and contractor work were not linked).

- **Using milestones to represent work.** Overloading a schedule with milestones masks the activities that drive them and defeats progress measurement, since milestones carry no recordable progress.

- **Letting LOE activities reach the critical path.** Because LOE has no discrete effort, representing it as long-duration or summary activities can let it inadvertently define program length and become critical — which it never should.

- **Redundant / non-unique activity names.** Repeated names like bare "Inspect" that do not identify their product make communication and filtered analysis unreliable.

- **Embedding codes in activity names.** Coding data appended to names instead of stored in custom fields.

- **Incomplete, circular, redundant, and dangling logic.** Activities without justified predecessors/successors; mutual dependencies; superfluous links; and start-date or finish-date dangles that break valid forecasting.

- **Start-to-finish (S–F) relationships.** A counterintuitive, flow-reversing link that overcomplicates the network and is widely discouraged; usually rewritable as simple F–S logic.

- **Logic on summary activities.** Linking grouping elements that should only derive dates from below — it hinders vertical traceability and hides the real work sequence (illustrated by the GFEBS schedule's 50 linked summary activities used to ease updates at the cost of obscured logic).

- **Overusing date constraints, especially to manage resources.** Constraining a large share of activities (illustrated by the GCSS-Army schedule, where about 60 percent of activities carried SNET constraints used to allocate resources, most actively preventing earlier starts) defeats a dynamic scheduling tool and forfeits time savings. Hard constraints in a baseline, customer-mandated dates used as constraint justification, and inactive constraints left in place are all flagged.

- **Misusing lags and leads.** Using lags to force start dates, to stand in for effort/procurement, or as risk margin; using leads (negative lags) that imply foresight and can cause logic failures and artificial float. The fix is finer activities and real logic interfaces.

- **Excessive path convergence / parallelism.** Tying too many predecessors into one successor (multiplicative merge risk) or over-relying on parallel relationships, which signals an aggressive or unrealistic schedule.

## Key Takeaways

- The IMS is a collection point for *all* program work — government, contractor, subcontractor, vendor — and integrating it into one comprehensive plan is the government program management office's job; the contractor schedule is only a subset.
- The WBS is the cornerstone: one product-oriented WBS per program, matched to the cost-estimate WBS, with a dictionary; every activity traces to a WBS element and every element has at least one activity.
- Use milestones sparingly (major events/deliverables only), let detail activities carry the work, keep LOE off the critical path, and give the schedule exactly one start and one finish milestone.
- Make activity names unique, descriptive, present-tense verb-noun and self-identifying; keep codes in custom fields and assign every activity an owner.
- Sequence with predecessor/successor logic so the network forecasts dates automatically; let F–S dominate, enter only the program start date, and let forward/backward passes compute the rest.
- Keep logic complete and clean: every activity (bar start/finish milestones) has a justified predecessor and successor; no circular, redundant, dangling, or start-to-finish logic; no logic on summary activities.
- Minimize and justify date constraints and lags/leads — prefer dynamic logic, model external supply as reference/visibility activities, keep hard constraints out of the baseline, and split activities rather than force dates.
- Watch path convergence: examine heavily merged successors, prefer a serial waterfall of F–S links, and treat excessive parallelism as a warning sign.

## Connects To

- **Best Practice 3 (Assigning resources / rolling wave):** Rolling-wave planning and long-term planning packages handle far-future uncertainty; resource calendars (not date constraints) are the right way to model resource availability and nonworking periods.
- **Best Practice 4 (Durations):** Resource availability and calendars drive activity dates alongside the logic established here.
- **Best Practice 5 (Horizontal and vertical traceability):** Giver/receiver milestones align integrated government/contractor schedules; summary-logic and coding discipline preserve vertical traceability across schedule levels.
- **Best Practice 6 (Critical path):** The forward pass's longest continuous path is the critical path validated here; clean network logic is its precondition.
- **Best Practice 7 (Total float):** Total float — the gap between early and late dates — is introduced here and managed there; hard constraints that zero out float distort it.
- **Best Practice 8 (Schedule risk analysis):** Path convergence underlies merge bias; risk-mitigation activities captured under Best Practice 1 feed the analysis; constraints that override logic can corrupt risk results.
- **Best Practice 10 (Baseline and basis document):** Custom coding schemes, LOE-handling techniques, unavoidable constraints, lags/leads, and missing-logic justifications must all be documented in the schedule basis document.
- **Companion GAO guidance:** The **GAO Cost Estimating and Assessment Guide (GAO-09-3SP)** for standard WBS examples and formal risk assessment; **MIL-STD-881C** for DOD WBS standards; the **IMP** as the event-based plan the IMS flows from in DOD programs.

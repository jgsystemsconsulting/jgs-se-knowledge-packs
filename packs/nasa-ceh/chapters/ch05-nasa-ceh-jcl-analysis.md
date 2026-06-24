# Chapter — Joint Cost and Schedule Confidence Level (JCL) Analysis

## Core Idea

A Joint Cost and Schedule Confidence Level (JCL) is a single integrated analysis that fuses a project's cost, schedule, risk, and uncertainty into one probabilistic statement. The output answers a deceptively simple question: what is the probability that the project finishes at or below both its target cost *and* its target finish date — jointly, not separately. The CEH's primary method for producing a JCL is a probabilistic cost-loaded schedule (PCLS): a logically networked schedule with cost mapped onto its activities, perturbed by discrete risks and baseline uncertainty, then run through simulation.

The value of the exercise is as much in the discipline it imposes as in the number it produces. Building a JCL forces the project team and the reviewing body to interrogate the underlying plan — the schedule logic, the cost mapping, the risk register — and that scrutiny tends to improve planning quality on its own. It also makes the project's expectations and the probability of meeting them visible to stakeholders, and it gives a defensible basis for sizing reserves (Unallocated Future Expenses, UFE) in both cost and schedule to reach a desired confidence level. The handbook frames the whole section as an overview, directing practitioners who actually build a JCL to Appendix J for depth.

## Frameworks Introduced (exact source names, when/how)

- **Joint Cost and Schedule Confidence Level (JCL)** — the integrated cost/schedule/risk/uncertainty analysis itself; introduced as both a policy requirement and a management tool.
- **Probabilistic Cost-Loaded Schedule (PCLS)** — named as the primary methodology for developing a JCL; the schedule with cost mapped to activities that the simulation operates on.
- **JCL Process Flow (six steps: a prerequisite plus five)** — the source's own ordering: Step 0, identify the goals of the analysis; Step 1, develop a summary analysis schedule; Step 2, load cost onto schedule activities; Step 3, incorporate the risk list; Step 4, conduct an uncertainty analysis; Step 5, calculate and view results.
- **Time-Dependent (TD) and Time-Independent (TI) cost characterization** — the two-way split the source requires when cost-loading a schedule.
- **JCL scatterplot** — the source's "most commonly used JCL chart"; an XY plot used to read confidence levels and frontier lines.
- **Annual Cost Uncertainty** — a downstream product the JCL process yields, time-phasing the probabilistic cost-schedule risk results against available annual resources.
- **Continuous Risk Management (CRM)** — referenced as NASA's process for building the risk register that feeds Step 3, and as the reason the register can never be assumed complete.
- **Agency Baseline Commitment (ABC) and Management Agreement (MA)** — the two policy thresholds the JCL value is set against.

The source also cross-references several appendices and external documents as authoritative sources rather than introducing them as frameworks: Appendix J (in-depth JCL implementation), Appendix K and the NASA Schedule Management Handbook (schedule development), Appendix G (incorporating risk), NPR 7120.5E (the governing policy), and the NASA Standing Review Board Handbook.

## Key Concepts

**The five steps plus step zero.** The handbook is explicit that there is one prerequisite and five fundamental steps. Step 0 is not optional housekeeping — it pins down which questions the analysis must resolve, identifies its primary users and beneficiaries, and names the core insight it should deliver. Because JCL is a policy requirement with quality standards to satisfy, the estimator can also deliberately configure the analysis (especially the schedule) so it is synergistic with the project's other products and processes rather than a standalone compliance artifact.

**Schedule as the backbone.** Step 1 builds a summary analysis schedule with well-defined activities and explicit logic networking — every task has identifiable predecessors and successors. The illustrative example uses a deliberately tiny schedule (two parallel streams, one with three tasks and one with two, converging on a single integration task that completes the project). Milestones such as Project End are themselves linked into the network, so they adjust automatically as the schedule is populated. The handbook is careful to flag that this example is far simpler than a real spacecraft schedule.

**Cost loading via TD/TI.** Step 2 maps cost onto the schedule, optionally summarizing cost by Work Breakdown Structure to aid the mapping. The mapping hinges on a single distinction:
- *Time-Dependent (TD) costs* are tied to a task's duration — they grow when duration grows and shrink when it shrinks. Overhead like project management, or a fixed minimum staff and facilities holding station for the length of a test, are TD. The handbook's vivid label is the "marching army" or standing-army cost that follows the project regardless of where it sits in the life cycle.
- *Time-Independent (TI) costs* are unaffected by changes in overall duration — schedule slips or compressions do not move them. Materials are the canonical example.
- A task can carry TD costs without TI costs; such level-of-effort (LOE) tasks are executed purely by the TD resources. The absence of TI cost does not mean the task is free.

**Incorporating discrete risks.** Step 3 layers risk realization onto what was, until now, the baseline plan. The risk register from the risk management system populates these risk tasks, each characterized by a probability of occurrence and an expected impact. Critically, the JCL is *not* constrained to only what the risk management system currently tracks. A programmatic risk the Project Manager worries about but that never formally entered the register can still be modeled, letting the project capture its programmatic consequences and expected value.

**Risk versus uncertainty — and why both are needed.** Step 4 is where the handbook draws its sharpest conceptual line. The risk assessment alone is a snapshot of potential future events, and it misses two things that also drive cost and schedule:
- *Incomplete risk register* — even with CRM, it is unrealistic to enumerate every cost- or schedule-increasing event.
- *Uncertainty in the baseline estimate* — even setting risks aside, the time and budget to complete segments of space-vehicle research, development, and production cannot be predicted exactly.

So the source defines the two inputs distinctly: a **risk** is a discrete event outside the baseline plan with an undesirable outcome, characterized by a probability and an expected impact (mirroring a risk matrix); risks can also be opportunities when the outcome is positive. **Uncertainty** is the indefiniteness about the baseline plan itself — the fundamental inability to perfectly predict a future outcome. The two overlap, since some of a plan's indefiniteness is caused by its own risks, and the JCL deliberately models register risks *alongside* baseline uncertainties so a Project Manager can see each risk's individual effect and build mitigation plans. That visibility is the stated reason for keeping them separate inputs.

**Uncertainty distribution.** Uncertainty is typically modeled with a triangular distribution: a low value (low extreme), a middle value (the "most likely" cost or duration), and a high value (high extreme). The handbook adds a subtle caveat — the baseline plan value need not equal any of low/middle/high, but it must fall within the low-to-high range.

**Reading the scatterplot.** Step 5 is iterative: analysts confirm durations and logic make sense and milestones remain achievable, then interpret results. The JCL model can emit many reports; the scatterplot is the most common. It is an XY chart with schedule on the X axis and cost on the Y axis, where each point is one simulation run's cost-schedule pair. Drawing target lines for cost and schedule splits the cloud into quadrants: the lower-left quadrant (at or beneath both targets) is the success region. Dividing the count of points in that quadrant by the total point count yields the confidence level — in the worked example, 14.4 percent of points fall in the lower-left, so the project has a 14.4 percent JCL against its $3.5M / July 1, 2013 target. Points exceeding only cost *or* only schedule (but not both) sit in the off-axis quadrants.

**Frontier lines.** Overlaid on the scatterplot, each frontier line separates the simulation results that meet a chosen JCL from those that do not — and a frontier's chosen JCL can differ from the JCL implied by the target intersection. The example shows a 50 percent frontier and a 70 percent frontier. The scatterplot is explicitly a snapshot valid only for the current plan; it is a starting point for trading cost against schedule, not prescriptive guidance.

**Downstream products.** Beyond the scatterplot, the JCL yields sensitivity analysis (so decision makers see what would move the outcome as adjustments are made) and Annual Cost Uncertainty results that time-phase the probabilistic cost and risk over the schedule. The example time-phases results from the 5th to 95th percentile across multiple years and flags years where available annual resources (the mean statistical result exceeds them) signal likely reserve utilization.

**Policy thresholds.** NASA directs each project to generate a PCLS and produce a JCL for the relevant Key Decision Point (KDP-I for programs, KDP-C for projects), executable within available annual resources, evaluated by a non-advocacy body (the Standing Review Board). The Decision Authority sets the committed JCL probability. Policy fixes the Agency Baseline Commitment (ABC) at a 70 percent JCL and the Management Agreement (MA) at no less than 50 percent — though the Decision Authority may deviate with documented rationale. The rationale for doing this at KDP-C is to confirm the plan is well defined with risks understood, and that the risk posture is acceptable for the cost and timeframe NASA commits to external stakeholders.

## Mental Models

- **One number, jointly earned.** A 70 percent cost confidence and a 70 percent schedule confidence are not a 70 percent JCL. The JCL is the fraction of simulation runs that land at or under *both* targets simultaneously — which is why the lower-left quadrant, not either axis alone, defines success.
- **The schedule is the skeleton; cost, risk, and uncertainty are the flesh.** Everything else in the analysis is layered onto the logic-networked schedule. A weak schedule produces a weak JCL no matter how careful the cost loading.
- **TD/TI as the slip test.** To classify a cost, ask one question: if the schedule slips, does this cost grow? Yes → time-dependent (the marching army). No → time-independent (the materials already bought).
- **Risk is an event; uncertainty is a fog.** A risk either happens or it doesn't (probability × impact). Uncertainty is the inherent haze around the baseline plan even when nothing "happens." A JCL needs both lenses, and the CEH's own tip is that the model's variance is usually driven far more by the uncertainty inputs than by the discrete risks.
- **Reserves as the gap to the target confidence.** UFE for cost and schedule is sized to lift the plan from its as-built confidence to the desired confidence level — the 70 percent ABC frontier shows how much cushion that requires.
- **The scatterplot is a photograph, not a forecast.** It captures the current plan only. Change the funding, the schedule, or hit a technical challenge, and the risk posture changes — the analysis must be rerun to get a current JCL.

## Anti-patterns

- **Double-counting uncertainty against modeled risks.** The source explicitly warns that special care must be taken to segregate the uncertainty *caused by* risks already in the simulation from the underlying uncertainty of the plan once those risks are discounted. Folding the same variability in twice inflates the spread. The handbook concedes this segregation can never be perfect, but judges the benefit of Project Managers seeing the individual risks to outweigh the slight residual error.
- **Treating the risk register as complete.** Relying solely on what CRM currently tracks ignores the source's stated reality that no register can predict every cost- or schedule-driving event — a key reason uncertainty must be added on top of the discrete risk list.
- **Reading a stale scatterplot as live guidance.** Using a scatterplot generated under a superseded baseline, or treating it as prescriptive rather than a starting point for trade-offs, contradicts the source's snapshot-in-time caveat.

## Key Takeaways

- A JCL is the joint probability of finishing at or below both the cost target and the schedule target; the primary method to produce one is a probabilistic cost-loaded schedule.
- The process has six stages: a goal-setting step zero, then schedule, cost loading, risk list, uncertainty analysis, and results.
- Cost loading rests on the TD/TI distinction — does the cost move when the schedule slips, or not.
- Risk (discrete probability-and-impact events) and uncertainty (indefiniteness of the baseline) are modeled together but kept as distinct inputs so each risk's effect stays visible; uncertainty typically uses a triangular low/most-likely/high distribution and usually dominates the model's variance.
- The scatterplot's lower-left quadrant fraction *is* the JCL; frontier lines mark chosen confidence levels; the chart is only valid for the current plan.
- Policy sets the ABC at 70 percent JCL and the MA at a 50 percent floor, with deviation allowed if documented; the analysis is reviewed by a non-advocacy Standing Review Board and supports the external commitment at KDP-C / KDP-I.

## Connects To

- **nasa-risk** — *Pairs with nasa-risk.* The JCL's Step 3 is fed directly by NASA's Continuous Risk Management process and the project's risk register, and the risk-versus-uncertainty distinction at the heart of Step 4 extends the discrete probability-and-impact model that risk management already maintains. The two packs are complementary: risk management supplies and characterizes the events; the JCL quantifies their joint cost-schedule consequence and sizes reserves against them.
- **Reserves / UFE management** — the JCL is the mechanism for justifying cost and schedule reserves at a target confidence level.
- **Schedule management** — the analysis depends on a well-networked summary schedule, pointing to the NASA Schedule Management Handbook and Appendix K as upstream inputs.
- **Milestone reviews and acquisition governance** — JCL results are evaluated by the Standing Review Board and used by the Decision Authority to set the Agency Baseline Commitment and Management Agreement at KDP-C / KDP-I, tying the analysis into NPR 7120.5E lifecycle gates.

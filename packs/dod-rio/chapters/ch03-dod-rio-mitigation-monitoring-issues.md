# Chapter 3: Risk Mitigation, Monitoring, and Issue Management

> **Scope caveat.** This chapter is the DoD-acquisition-side complement to the more
> general treatments in the `nasa-risk` and `dau-se-guidebook` packs. It captures how the
> RIO Management Guide for Defense Acquisition Programs handles the *back half* of the risk
> loop — choosing and executing a mitigation strategy, watching whether that strategy is
> working, and managing the realized problems (issues) that mitigation did not prevent.
> Where those other packs describe the general discipline, this chapter gives the
> program-office mechanics: the RMB/RWG governance, the burn-down chart, the IMS/EVM/TPM
> reporting hooks, and the probability-equals-one treatment of issues.

## Core Idea
Once a risk has been identified, analyzed, and prioritized, the program must answer one
question: *what, if anything, will we do about it, and when?* The RIO guide answers that with
a single decision among four mitigation options — accept, avoid, transfer, or control — backed
by a resourced, time-phased plan that lives in the program's baseline schedule. Choosing the
option is only the start. The program then **monitors** the plan against metrics to see whether
the risk is actually coming down, adjusts when reality diverges from plan, and **manages as
issues** any event that has already materialized — or is now a near-certainty. Risk, monitoring, and
issue management form one continuous loop, not three separate activities.

## Frameworks Introduced
- **The four risk mitigation options (accept / avoid / transfer / control)** — the menu every
  risk owner and Risk Management Board (RMB) evaluates before formulating an implementation
  approach. The program picks the best single option or a hybrid based on the analysis,
  prioritization, and potential for risk reduction.
  - *When/how:* applied to every mitigated risk; the chosen option and its activities are
    captured per-risk in the risk register, and for program-level risks the strategy is
    reflected in the Acquisition Strategy and presented at decision points and milestones.
- **Risk acceptance ("Watch Item")** — the program acknowledges the event may occur and is
  prepared to bear the consequences, but continues to track the risk so that worsening
  consequence or rising likelihood is caught. Before accepting, the program identifies the
  resources and schedule it would need if the risk is realized; sometimes relief must be sought
  from higher headquarters.
  - *When/how:* common in resource-constrained environments, but accepting never means ignoring;
    monitoring "knowledge points" are established to re-evaluate.
- **Risk avoidance** — eliminate the source of the risk by taking an alternate path and
  replacing the risky solution with another. Examples named: deferring a selected capability to
  a later upgrade or release, changing operating procedures, or substituting a low-risk mature
  technology.
  - *When/how:* deferral is acceptable only if the system would have been fielded without the
    capability anyway; difficult-but-needed performance should be tackled earlier, not deferred.
- **Risk transfer** — reassign or delegate the task (and possibly the financial responsibility)
  to another entity: across programs, between Government organizations, or across two sides of
  an interface in the same organization. Formal agreements (MOA/MOU) are recommended.
  - *When/how:* the hardest option to execute because it depends on a party outside the
    program's control accepting and working the risk; transfer never fully removes the
    Government's schedule and performance exposure because the Government still needs the product.
- **Risk control** — actively drive likelihood and/or consequence as low as practical. The guide
  enumerates control activities: multiple parallel development efforts, early prototyping,
  incremental development, reviews/walk-throughs/inspections, design of experiments, models and
  simulation, key-parameter control boards, demonstration events, and process proofing.
  - *When/how:* the default for risks the program intends to reduce; activities must produce a
    real reduction in likelihood or consequence (or accelerate the knowledge that affects them).
- **Risk burn-down plan** — a six-step method to make a control/mitigation plan trackable:
  (1) sequence the mitigation activities with realistic precedence (typically finish-to-start);
  (2) make every activity clearly defined, objective, and measurable; (3) assign each activity a
  planned likelihood/consequence value; (4) estimate start/finish dates; (5) place the activities
  (or a subset) into the Integrated Master Schedule (IMS); (6) chart risk level versus time.
  - *When/how:* required for all high and moderate risks and for selected low risks; the
    resulting **burn-down chart** (Fig. 2-8) plots planned versus actual progress over months.
- **Risk monitoring** — a continuous process that tracks mitigation-plan performance against
  established metrics throughout acquisition. It is carried out (with a risk management tool)
  during technical reviews, in program reviews, and in the meetings of the RMB and its Risk
  Working Group (RWG).
  - *When/how:* feeds recording, maintaining, and reporting of risks and results; documents
    include EVM status, IMS status, TPM status, the risk register, watch lists, and test
    results. The **trend matrix** (Fig. 2-10) and the **risk reporting format** (Fig. 2-11)
    communicate status to leadership.
- **Issue management** — the parallel process for any event or condition that has already
  come to pass, or whose occurrence is now certain (probability = 1). It mirrors risk management but skips
  likelihood scoring and uses an **issue consequence reporting matrix** (Fig. 2-13).
  - *When/how:* an issue may be a realized risk or may emerge with no recognized antecedent;
    either way the consequence is assessed against the program's consequence criteria, an owner
    is assigned by the RMB (or equivalent), and corrective action is tracked to retirement.

## Key Concepts
- **Mitigation plan content.** A plan must specify what will be done, when, who is responsible,
  the resulting cost/schedule/performance impact, and the resources required. It should be
  feasible, affordable, adequately timed, and realistic given program constraints.
- **Resiliency by design.** Some risk is best handled in the design itself — safety margins,
  growth provisions, modularity, cybersecurity, electromagnetic protection, graceful or
  predictable degradation, and avoidance of single-point-of-failure designs — sized by analysis
  so resilience does not buy unnecessary cost or capability.
- **Contingency plans and triggers.** Some mitigation activities are held as contingency plans
  that fire on a defined triggering event; PMs should consider contingency plans for high risks.
- **Objective, not subjective, activities.** A burn-down activity such as "perform a test" fails
  because it is not defined, objective, or measurable; a passing activity states a measurable,
  user-approved outcome (e.g., a brassboard throughput test meeting threshold and approved by the
  user). **Meetings do not burn down risks — results do.**
- **Reduce likelihood vs. reduce consequence.** Control usually lowers the likelihood of the
  event or accelerates knowledge about it; consequence can also be lowered by sequencing the hard
  work first (accelerating risk realization), limiting impact, or preparing alternatives such as
  redesign. If consequence is reduced, the risk statement, prioritization, and strategy may need
  to be re-written.
- **Right level of management.** Risks are managed at the executive, management, or working
  level as appropriate, and managers escalate to the next level when the ability to mitigate
  exceeds their authority or resources.
- **Monitoring drives adjustment.** If a risk drops below its prior assessment, the program may
  reduce or cancel mitigation and free resources; if severity rises, it strengthens mitigation —
  and documents the rationale for either change. **Retired risks are reviewed periodically to
  catch relapse.**
- **The risk-to-issue continuum.** As a risk's likelihood climbs toward certainty, the program
  should anticipate its realization and pre-position plans to limit consequences — so that for a
  high-likelihood antecedent risk, a corrective plan is already in hand when the issue occurs.
- **Issue analysis and options.** Issues are scored with the program's consequence criteria only
  (no likelihood, since probability = 1). The correction options are **Ignore** (accept the
  consequences after a cost/schedule/performance business-case analysis) and **Control**
  (reduce consequence and residual risk to as low as practical); **Avoid** and **Transfer**
  carry the same meaning as for risks and are less common, with Avoid often subsumed under
  Control.
- **Issue tracking loop.** Corrective action plans (sometimes POA&Ms) include an Estimate at
  Completion (EAC) and go into the IMS; the program monitors actual versus planned, feeds results
  back, adjusts the plan, and re-assesses the issue's level and any new risks it spawns. Issues
  are assessed for residual risk, and new formal risks are established as appropriate.

## Mental Models
- **One loop, three faces.** Mitigation chooses the action, monitoring measures whether it
  worked, and issue management handles what the action failed to prevent. Treat them as one
  recurring cycle anchored on the program's review cadence, not as three checklists.
- **The register is the spine.** Mitigation option and activities, monitoring trends, and
  corrective actions all land in one place — and the guide explicitly allows the risk, issue, and
  opportunity registers to be merged into one consolidated register where that eases management.
- **Burn the high-consequence risks down early.** Front-loading high-consequence mitigation
  either retires the risk before it can force a late, expensive program change, or surfaces the
  need for change while there is still time to react.
- **Probability = 1 is the dividing line.** The single cleanest test for "is this a risk or an
  issue?" is whether the event is still uncertain. If it has happened or is certain to happen,
  drop the likelihood axis and manage it as an issue.
- **Triggers beat calendars.** Regular review intervals are necessary, but the events inside a
  burn-down plan should act as automatic triggers to action — do not wait for the next scheduled
  meeting if a knowledge point has been reached.
- **Track implementation, not just planning.** The common failure mode in monitoring is
  reporting that a strategy was *selected* while never confirming the activities were *executed*
  and *progressing*; monitor the doing, not the deciding.

## Anti-patterns
- **Baseline-activity laundering.** Programs fall into a trap of relabeling ongoing baseline
  contract activities as "risk mitigation" without analyzing whether those activities or
  resources are actually adequate to reduce the risk — especially for emergent risks. The guide
  names this explicitly and tells programs to objectively assess feasibility and resource
  commitment when determining likelihood.
- **Unresourced or infeasible plans.** A mitigation plan that is not fully resourced, or cannot
  be completed by the time it is needed, is not a real plan; full commitment of funding and staff
  is part of the named best practice.
- **"Simple" changes taken on faith.** When avoidance proposes a seemingly simple change, the
  program must examine *why* that change was not already in the original design before trusting it.
- **Meetings masquerading as mitigation.** Counting status meetings as burn-down progress —
  results burn down risk, meetings do not.
- **Letting current problems crowd out risk work.** If attention to today's issues overtakes the
  effort to manage risks (and opportunities), the program loses its forward view; the fix is to
  keep focus on both.
- **Unnoticed relapse of a retired risk.** Failing to document and periodically re-review retired
  risks lets a closed risk quietly redevelop.

## Key Takeaways
1. Every mitigated risk gets one of four options — **accept, avoid, transfer, or control** (or a
   hybrid) — chosen from analysis and prioritization, with a plan stating what, when, who, the
   cost/schedule/performance impact, and the resources required.
2. **Acceptance is a Watch Item, not abandonment** — the risk is still tracked, and the resources
   and schedule needed if it is realized are identified in advance.
3. **Transfer never fully removes Government exposure**; schedule and performance risk remain
   because the Government still needs the product. Use an MOA/MOU.
4. **Control must produce real reduction** in likelihood or consequence, drawn from a defined
   activity set (parallel efforts, prototyping, DOE, modeling and simulation, control boards,
   demonstrations, process proofing, etc.).
5. **Build a burn-down plan** (six steps) for all high/moderate and selected low risks; activities
   must be objective and measurable, and they go into the IMS. **Meetings do not burn down risk.**
6. **Monitor against metrics** (EVM, IMS, TPM, register reports) and let burn-down events trigger
   action; adjust mitigation up or down as risk changes and document why.
7. **Burn down high-consequence risks early** and review retired risks periodically to catch
   relapse.
8. **An issue has probability = 1** — scored on consequence only, options are mainly Ignore or
   Control, owned by the RMB, planned via a corrective action plan (POA&M) with an EAC in the IMS,
   and assessed for the new risks it may create.

## Connects To
- **ch01 / ch02 (this pack):** mitigation, monitoring, and issue management consume the risk
  statements, likelihood/consequence scores, and prioritization produced upstream; the same
  consequence criteria are reused to score issues.
- **Opportunity Management (next chapter, this pack):** the guide treats risk, issue, and
  opportunity as one family and permits a single combined register; opportunity is the upside
  mirror of the risk loop described here.
- **Governance (RMB / RWG):** mitigation selection, issue ownership, and escalation all run
  through the program's Risk Management Board and Risk Working Group — the same bodies that
  conduct monitoring reviews.
- **Program-management integration (Appendices C and D of the source):** Appendix C explains
  integrating mitigation activities with the WBS, IMS, and EVM; Appendix D works a hypothetical
  risk end-to-end.
- **`nasa-risk` pack:** NASA's Continuous Risk Management and risk-informed decision making cover
  the same identify-analyze-plan-track-control loop; this chapter is the DoD-acquisition
  rendering, with RMB governance, burn-down charts, and the probability-equals-one issue model.
- **`dau-se-guidebook` pack:** risk management as one of the SE technical-management processes,
  and the technical reviews where this monitoring is performed; this chapter supplies the
  program-office detail behind that process view.

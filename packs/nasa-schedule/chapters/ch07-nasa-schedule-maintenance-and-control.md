# Chapter — Schedule Maintenance and Control

> Source: NASA Schedule Management Handbook, Chapter 7 ("Schedule Maintenance and Control"), 2024 edition. This chapter synthesizes that material. Use the 2024 edition, not the superseded 2010 SP-2010-3403.

## Core Idea

Once a schedule has been developed, the value of the Integrated Master Schedule (IMS) comes from keeping it alive: statusing it routinely, measuring how the program/project (P/p) is actually performing against the approved plan, and taking disciplined corrective action when performance drifts. Chapter 7 frames this as a single sub-function with two halves that are deliberately intertwined — **Maintenance** (keeping the schedule current with real progress and approved changes) and **Control** (establishing the baseline, measuring performance, deciding on corrective action, and reflecting that action back into the schedule).

The handbook organizes the whole sub-function into five procedures that loop continuously across the life cycle. Two are maintenance procedures (update with actual progress; update the database with corrective actions) and three are control procedures (create the baseline; measure performance and monitor trends; determine corrective action or retention rationale). The unifying logic is that the schedule baseline is a stable reference: it should change only through authorized replans or rebaselines processed through the P/p's configuration and data management (CM/DM) change-control process, while day-to-day current-schedule data stays accurate enough to manage the work. A central NASA requirement runs through the chapter — the P/p must continually confirm it can still meet its internal **Management Agreement (MA)** and external **Agency Baseline Commitment (ABC)** at acceptable risk.

## Frameworks Introduced

These are named in the source, with how and when they apply:

- **Schedule Maintenance and Control Plan** — a sub-plan to the Schedule Management Plan (SMP) that captures the requirements for updating the schedule, tracking performance, and taking corrective action across the life cycle. NPR 7120.5 requires a Technical, Schedule, and Cost Control Plan; the schedule-control portion is sometimes captured here. Used as the governing document for the entire sub-function.

- **The five-procedure Maintenance and Control model** — Procedure 1 (Control: create a schedule baseline), Procedure 2 (Maintenance: update with actual progress), Procedure 3 (Control: measure performance and monitor trends), Procedure 4 (Control: determine corrective action or retention rationale), Procedure 5 (Maintenance: update the database with corrective actions). Introduced as the spine of Section 7.3.

- **Agency Baseline Commitment (ABC) and Management Agreement (MA)** — the ABC is NASA's external commitment to OMB and Congress that the P/p will not exceed its development cost and/or schedule; for Space Flight P/ps it is typically the planned launch date and is set at KDP C, documented in a Decision Memorandum (DM). The MA is the internal agreement (Center, Mission Directorate, P/p, Administrator), usually set ahead of the ABC; the gap between Schedule MA and Schedule ABC represents the schedule margin held, often by the Mission Directorate. Introduced in Step 1 of Procedure 1 as the policy anchors for baselining.

- **Performance Measurement Baseline (PMB)** — the time-phased cost plan for all authorized work scope, including NASA and supplier costs, against which performance is measured (via EVM when required). The PMB does not include Unallocated Future Expense (UFE). Introduced as the integrated baseline the schedule baseline informs for Space Flight P/ps.

- **Schedule Change Control Board (CCB) and Baseline Change Request (BCR)** — the CCB convenes regularly to review proposed changes to critical milestones, reviews, KDPs, and key integration events; it initiates and dispositions BCRs through the CM/DM process. Introduced under Change Control Process in Procedure 1.

- **"Notification and control" baselining method** — one of two general baselining choices (the other being to baseline the entire IMS). Notification and control places formal control only on a carefully selected set of tasks/milestones (contract, integration, procurement, test, delivery, facility-readiness, review, verification, and operational-readiness milestones), allowing the team to adjust other planned work without formal change documentation. Introduced in Procedure 1.

- **Integrated Baseline Review (IBR)** — a risk-based review of the supplier's PMB used to verify that cost, schedule, and risk are properly linked before KDP C; required (Pre-Approval IBR) for P/ps requiring EVM, recommended-and-tailored for those that don't. Introduced in Step 2 of Procedure 1 (validation).

- **Deterministic schedule performance metrics** — introduced in Procedure 3, Step 1, as a complementary suite (the handbook stresses using several together):
  - **Activity/Milestone Variances and Schedule Variance (SV/SVt)** — SV = BCWP − BCWS (dollars); SVt is time-based, referenced to Earned Schedule.
  - **Activity/Milestone Performance Trends** — completion-rate and cumulative-finish trend charts.
  - **Baseline Execution Index (BEI)** — actual-to-baseline ratio: "Is work getting done?"
  - **Current Execution Index (CEI)** — actual-to-forecast ratio within a near-term window: "Is work getting done in the forecasted time frame?" Value cannot exceed 1.
  - **Hit or Miss Index (HMI)** — baseline tasks finished on/early versus those baselined to finish in the month: "Is the right work getting done?" Value cannot exceed 1.
  - **Schedule Performance Index (SPI)**, plus its time-based companion **SPIt** built on **Earned Schedule (ES)** — SPI = BCWP/BCWS (a cost-denominated schedule measure); ES converts the result into time units, so SPIt = ES/AT.
  - **Critical Path Length Index (CPLI)** — (remaining CP length + total float) / remaining CP length; efficiency required to finish a milestone on time.
  - **Margin Consumption** and float-erosion measures — the **Total Float Consumption Index (TFCI)** together with the **Predicted Critical Path Total Float (CPTF)** — both taken from the PASEG (NDIA IPMD); the TFCI projects a finish date from the average rate at which float is being burned and is meant for delinquent P/ps only.

- **Stochastic (probabilistic, risk-based) performance metrics** — introduced in Procedure 3, Step 2, built on Schedule Risk Analysis (SRA) / Monte Carlo: Probability of On-time Delivery of Critical Items (the "BandAid" chart), Risk-based Completion Trend, Risk-based Sufficiency of Margin, and Risk-based Tracking against the MA and ABC (using ICSRA results plotted in cost/schedule quadrants).

- **Four corrective actions (Watch, Retain, Replan, Rebaseline)** — the disposition set in Procedure 4. Watch and Retain leave the PMB unchanged; Replan is internal (PM authority within the MA); Rebaseline is external, changing the ABC (and usually MA and PMB), requiring Decision Authority and external-stakeholder approval. Thresholds and the NASA Authorization Act of 2005, Section 103 (as implemented by NPR 7120.5) govern when replan/rebaseline are mandated for P/ps over $250M.

- **Baseline maintenance methods** — introduced in Procedure 5 as alternative ways to control the baseline: Complete Schedule Baseline Update Method, Baseline Control Milestone Update Method, P/p Element Baseline Method, Contractor's Schedule Baseline Control Process Update Method, and Annual PPBE Schedule Baseline Reset Method.

## Key Concepts

- **Schedule performance baseline (baseline IMS).** The original, approved, time-phased plan for all work, against which performance is tracked and corrective actions are taken to keep the P/p performing at acceptable risk. It informs the integrated baseline content (the PMB for Space Flight P/ps) and is maintained through routine CM/DM-supported updates while changes flow through formal change control.

- **Two baselining methods, two control burdens.** Baselining the entire IMS forces rigorous, labor-intensive control because every baseline-data change must be documented. The "notification and control" subset is lighter but still demands documented control of the selected items. The choice is shaped by whether EVM is required — EVM ties the total schedule baseline tightly to the PMB.

- **Prerequisites and verification gate.** Maintenance and control can begin only when the Schedule Maintenance and Control Plan exists, the Schedule Database is fully populated (BoEs complete; IMS/Summary/Analysis schedules output; supporting documentation collected), and a CM/DM process is in place. The IMS must pass Assessment and Analysis verification (Chapter 6) before baseline approval. For Space Flight P/ps with life-cycle cost over $250M, an Integrated Cost-Schedule Risk Analysis (ICSRA) to determine the Joint Confidence Level (JCL) is required before baselining.

- **"Progress" vs. "performance."** Progress is where things stand; performance is how well the P/p is executing to plan. Control turns progress data into performance judgments against thresholds documented in the SMP.

- **Current schedule vs. baseline data.** The current schedule is the baseline plus all approved content changes as of "time now" (the status date). Work to the left of time now is actuals; work to the right is forecast. The chapter recommends a single status date for all updates, typically aligned to month-end close.

- **Remaining duration drives forecasts.** For in-progress activities, remaining duration is the primary status input because it determines the forecasted finish and keeps successors correctly time-phased. The "% Complete" field in many tools is actually percent-duration-complete, which may differ from physical-work-percent-complete — a distinction that matters acutely under EVM (where earned value tracks dollars, not days).

- **Performance Measurement Techniques (PMTs).** For EVM, work packages get PMTs (weighted milestone, 50/50, 0/100, percent complete, apportioned) chosen per package; the same PMT used for planning is used to claim earned value. Level-of-effort (LOE) activities have no discrete product and, by their nature, should never show a schedule variance.

- **Margin vs. float vs. contingency.** Margin is a PM-owned control parameter, assigned to protect critical paths and released only through a formal process; its needed amount is larger early and decreases as uncertainty resolves, tracked against a burndown curve. Float is calculated by the tool for every activity (days an activity can slip before hitting the critical path). "Effective margin" is margin actually on the critical path. The handbook also separates margin (working days) from contingency (non-working days such as weekends/holidays); contingency is a last resort before consuming margin, and tracking them separately avoids a tracking problem when non-working days get folded into margin totals.

- **Replan vs. rebaseline.** A replan re-schedules remaining ("to-go") work and is generally internal (PM authority within the MA); a rebaseline is a special replan that changes the ABC and is external, requiring Decision Authority and OMB/Congress involvement. After a rebaseline, EVM performance measures may be reset to 1.0 and the changed content re-validated (often by the Standing Review Board).

- **Mandated thresholds (NPR 7120.5 / NASA Authorization Act of 2005).** For P/ps over $250M: a development-cost or LCC Estimate at Completion exceeding the ABC by 15% triggers a replan; exceeding by 30% triggers a rebaseline; a slip of a specified key milestone beyond six months triggers a replan.

- **Margin management as active work.** Procedure 5 treats margin as something to manage, not just track: convert margin duration into approved risk-mitigation activities; when risks don't materialize, repurpose unused margin (start successors earlier, redistribute resources, move margin downstream, or return it as float). Because margin is not fully fungible, moving it downstream may not translate day-for-day — critical-path analysis on both deterministic and probabilistic paths determines how much *effective* margin actually exists.

## Mental Models

- **Baseline as a fixed yardstick.** The baseline (and PMB) should stay stable so it remains a meaningful measuring stick; you change the yardstick only through authorized replan/rebaseline, not to make the numbers look better.

- **Two clocks running at once.** Baseline data records the original plan; current data records actual and forecast outcomes. Maintenance keeps the "current" clock honest without touching the "baseline" clock unless change control authorizes it.

- **A suite of gauges, not a single needle.** No one metric tells the truth — SV/SVt, BEI/CEI/HMI, SPI/ES, CPLI, float, and margin each measure schedule health differently and each has a blind spot. The handbook explicitly advocates corroborating concerns across a complementary set, and advocates the IMS as a management tool first, a reporting tool second.

- **Stoplight-and-threshold governance.** Most metrics are paired with stoplight bands (e.g., blue/green = fine or look for efficiencies, yellow = "Watch," red = formal corrective action) whose thresholds are pre-set during Schedule Management Planning and recorded in the SMP — so the action is decided before the variance appears, not improvised after.

- **Margin as a depleting reservoir.** Plotted as a burndown, margin is a finite reservoir that should drain along a planned curve; deviations from the curve are the early-warning signal. Effective margin can shift as critical paths change, so it must be recalculated, not assumed constant.

- **Dilution near completion.** Cost-denominated indicators (SV, SPI) converge toward their neutral values as the P/p ends — SPI heads to 1.0 once all money is spent — so they lose diagnostic value late; Earned Schedule (time units) and other measures keep utility nearer completion. Rule of thumb in the source: once ~2/3 of budget is spent, lean harder on other schedule measures.

- **Deterministic looks back; stochastic looks forward.** Deterministic metrics extrapolate from past performance and ignore future risk; SRA-based stochastic metrics (BandAid charts, risk-based completion trends, ICSRA-vs-MA/ABC quadrant tracking) model risks and uncertainties to forecast — but only as well as their inputs (the risk list and IMS must be current and quality-checked).

## Anti-patterns

The source explicitly names these as cautions, gaming techniques, or errors:

- **"Late-date" baselining.** Setting the baseline from late start/finish dates is described as a gaming technique that minimizes reported schedule variance to customers; recognize it when examining contractor performance.

- **Manipulating the IMS for favorable metrics.** Adjusting the schedule to produce good-looking metrics for reporting severely degrades the IMS's value as a management tool; the point of metrics is to find and fix issues, not to keep a report card.

- **Frequent baseline changes.** Excessive replanning/rebaselining can distort the IMS and give a false picture of how the P/p is truly executing.

- **Single-metric reliance.** Using one metric or a tiny set risks false conclusions; corroborate across a suite. The chapter also flags specific traps: BEI/CEI don't distinguish simple from complex activities (low-cost completions can dilute the index); HMI can mislead when activities finish on the first day of the next month; CPLI is a global measure that can't pinpoint the offending tasks and only sees the current critical path.

- **"Rubber baseline."** Resetting the baseline (e.g., the Annual PPBE reset) without proper communication and stakeholder buy-in can create the appearance of a rubber baseline — gaming/data manipulation that masks cost and schedule variances, sometimes intended to mislead.

- **Retroactive BCRs masking erosion.** The source gives a real NASA example where SPI looked green while BEI deteriorated; retroactive BCRs added already-completed work to the baseline, yet performance kept eroding and the project slipped its launch date — a cautionary case for trusting an integrated SPI over a corroborating execution index.

- **Not forcing status on late tasks.** Some tools (MS Project is named) don't force users to update behind-schedule tasks; all incomplete tasks, including ones that should have started or finished, must be brought to the single status date.

- **Negative-float baseline errors.** Out-of-sequence relationships or a fixed constraint on the completion milestone can produce negative float that reflects a baseline error to be corrected, not a real condition.

## Key Takeaways

- Maintenance and Control is a continuous "Business Rhythm" loop of five intertwined procedures, not a one-time activity; a cycle completes when the performance review is done and any required replan, rebaseline, or change orders are initiated/approved.
- Establish the baseline at the right life-cycle point (preliminary IMS by SDR/MDR or ATP; baseline at KDP C or Program Approval), make sure schedule, resource, and budget plans are in phase, and validate via a stakeholder review (and an IBR when EVM applies) before approval — never approve a schedule baseline that doesn't align with the budget plan.
- Keep the current schedule honest with single-status-date updates and remaining-duration-driven forecasts; routine maintenance must not alter baseline data, which can change only through formal CM/DM change control.
- Measure performance with a corroborating suite of deterministic and stochastic metrics whose action thresholds are pre-defined in the SMP; treat the IMS primarily as a management tool.
- Track margin and float deliberately — separate margin from contingency, recalculate effective margin as critical paths shift, and manage margin actively (mitigate risks, repurpose unused margin) rather than letting it leak.
- Disposition variances through the Watch / Retain / Replan / Rebaseline decision flow; preserve the original baseline for traceability whenever a replan or rebaseline changes the plan, and honor the mandated 15%/30%/six-month thresholds for P/ps over $250M.

## Connects To

- **Chapter 5 — Schedule Development:** supplies the populated Schedule Database, the IMS as backbone, total approved scope, margin planning, and the IMS methods that define what gets baselined here.
- **Chapter 6 — Assessment and Analysis:** provides the verification gate before baseline approval and the SRA methods that feed every stochastic (risk-based) performance chart in Procedure 3.
- **Chapter 8 — Schedule Communication and Documentation:** the channel through which performance measurements, trend reports, archived baselines, and change logs are reported and retained.
- **Schedule Management Plan (SMP) and its Maintenance and Control sub-plan:** the source of all metric selections, thresholds, prescribed actions, margin guidelines, and update cadences referenced throughout.
- **NPR 7120.5 / NPR 7120.8, the NASA Authorization Act of 2005 (Sec. 103), the NASA IBR Handbook, the NASA EVM System Description, the NASA Risk Management Handbook, and PASEG:** the policy and standards basis for baselining, IBRs, EVM, replan/rebaseline triggers, and the TFCI/CPTF and acceleration techniques.
- **EVM, JCL/ICSRA, and the MA/ABC commitment structure:** the cost-schedule-risk integration that this sub-function continuously tests for compliance at acceptable risk.

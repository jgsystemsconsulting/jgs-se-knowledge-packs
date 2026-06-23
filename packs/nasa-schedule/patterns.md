# Patterns — NASA Schedule Management techniques

Named techniques from the handbook, each with when to reach for it, how it works, and the
trade-offs the source flags. Wording is this pack's own. Chapter refs point to the fuller
treatment.

---

## 1. Plan before you build the IMS (ch02)
**When** — at the very start of Schedule Management, front-loaded into Phase A.
**How** — write the SMP and its four sub-plans first: choose the scheduling method, select
tools, define the Milestone Registry and Activity Attributes, then build the IMS to those
specs. The SMP is the blueprint; the IMS is the build.
**Trade-offs** — retrofitting data fields onto a populated schedule is "very difficult and
inefficient," so decisions like method and coding must be made early because they cascade
into tool choice and reporting formats.

## 2. Scope first, dates second (ch03)
**When** — opening move of building any new IMS.
**How** — pin down the complete work content through the four breakdown structures (WBS =
what, OBS = who, CBS = how much, IMS = when) before laying down a single date; assemble
scope from the P/p Plan, SOW, contracts, and agreements.
**Trade-offs** — work not in the management-approved WBS must not enter the IMS; silent
divergence in how people read the scope yields an inaccurate schedule, so the scheduler
must surface conflicts for managers to reconcile.

## 3. The control-account grid (ch03)
**When** — establishing where scope, organization, and cost meet for EVM.
**How** — overlay the WBS (columns) and OBS (rows) on a Responsibility Assignment Matrix;
each filled cell is a control account owned by one CAM, the atom where budget, actuals, and
earned value accumulate.
**Trade-offs** — prevents duplicated responsibility, but the cost tool and IMS often differ
in WBS depth, so estimates may need roll-up reconciliation.

## 4. Build the network in physical order with CPM (ch04)
**When** — constructing the logic network.
**How** — draw summary-level integrate-then-test flow first, then assign detailed
dependencies; use Finish-to-Start as the default relationship for accurate total float; run
the engine in auto-schedule mode so logic and constraints drive dates.
**Trade-offs** — leads/lags, hard constraints, and non-FS logic distort float and the
critical path and must be justified in the BoE; excessive detail and over-constraining
destroy analyzability.

## 5. Three-point, owner-approved durations (ch04)
**When** — estimating activity durations.
**How** — gather durations from standards, analogy, parametric SERs, build-up, or SME
judgment; capture each as Min / Most Likely / Max so uncertainty is explicit; the task owner
owns and approves the estimate.
**Trade-offs** — durations must not be padded, trimmed, or cut by management fiat; weak
analogies for new technology should widen uncertainty rather than masquerade as solid data.

## 6. Manage margin, not float (ch04, ch07)
**When** — protecting the schedule against risk.
**How** — size margin (working days) from quantified risk, place it where risks occur and
before key milestones/tests, hold it as a lien against MR/UFE, validate it with probabilistic
analysis, and track it on a burndown curve.
**Trade-offs** — funded (baselined) margin distorts EVM and is discouraged; end-of-schedule
margin must be tightly controlled so teams don't treat it as a free buffer; margin is not
fully fungible, so moving it downstream may not translate day-for-day.

## 7. Cost-load with TD/TI hammocks for the ICSRA (ch06)
**When** — extending an SRA into an ICSRA where resource loading is impractical.
**How** — string a hammock task (SS to the first activity, FF to the last) over a work band so
it expands and accrues cost as durations stretch; separate time-dependent (scales with
duration) from time-independent costs.
**Trade-offs** — the time-dependent cost impact of a schedule-delay risk must NOT be entered
again as a separate cost-risk impact — duration uncertainty already drives it — or you
double-count.

## 8. Model a discrete risk as likelihood × impact (ch06)
**When** — loading discrete risks from the RMS into an SRA.
**How** — multiply a Bernoulli likelihood draw by an impact distribution (triangular, or
uniform when little is known); map it via Activity Duration Impact (a zero-duration delay
milestone), or Delayed Start/Completion, or probabilistic/conditional branching.
**Trade-offs** — map a risk to the FIRST activity in the affected string and let it ripple,
not to every activity (over-mapping multiplies the effect); class risks as parallel
(longest drives) or serial (cumulative).

## 9. Run uncertainty-only first, then layer risks (ch06)
**When** — building up an SRA.
**How** — apply duration uncertainty (always drawn, no likelihood gate) to establish the
baseline spread, then add discrete risks on top so each risk's marginal effect is visible.
**Trade-offs** — zero out margin tasks first (model as a "0" distribution for traceability)
or you double-count; widen SME-elicited ranges because experts under-capture the true span.

## 10. Always assess correlation (ch06)
**When** — every uncertainty analysis.
**How** — set correlation between related variables; default to 0.3 absent data, within an
industry range of 0.25–0.75.
**Trade-offs** — ignoring correlation (treating it as zero) understates total variance, often
dramatically, and overstates both schedule risk and apparent merge bias.

## 11. Read the S-curve shape, not just the point (ch06)
**When** — interpreting SRA/ICSRA output.
**How** — use the CDF/S-curve slope (flat = high uncertainty, steep = low), watch for left-side
dog-legs (a backstopped earliest date), long right tails (high-impact/low-probability risks),
and bimodality (two clusters of impact).
**Trade-offs** — a later deterministic date with a steeper curve can beat an earlier, flatter
one — certainty can outweigh nominal speed.

## 12. Take the JCL at the knee of the frontier (ch06)
**When** — reporting a Joint Confidence Level.
**How** — plot every Monte Carlo cost-schedule pair; the Frontier Curve is the locus of a
given JCL value, and the reported number is taken at the equal-probability knee.
**Trade-offs** — anywhere off the knee implicitly favors cost or schedule; the 70% JCL knee
typically corresponds to roughly the 78–84th percentile on an individual S-curve, which is why
an 80th-percentile pick traces back to Agency guidance.

## 13. The Shock Test for structural soundness (ch05)
**When** — the Critical Path and Structural Check, after a clean Health Check.
**How** — zero out margin durations, then perturb the network task by task: compress a task
and confirm downstream activities move left; lengthen a task until critical and confirm
downstream pushes out. Correct each found defect before moving on so issues isolate.
**Trade-offs** — horizontal traceability is necessary but not sufficient; a fully linked
network can still behave defectively, which is exactly what the Shock Test exposes.

## 14. Interpret the Health Check, don't trust its colors (ch05)
**When** — the cheapest, most repeatable 1st-Tier procedure.
**How** — run an Agency/industry-standard tool (STAT, Polaris, Acumen Fuse), then drill into
each non-ASAP constraint and missing predecessor/successor individually.
**Trade-offs** — green can hide a schedule-killing constraint; a single "Must Finish On" can
invalidate the whole schedule, so the report is a roadmap for investigation, not a grade.

## 15. Hold every element to a replicability standard (ch05)
**When** — the Basis Check.
**How** — record, per element, the source-data quality and the method behind its duration,
links, and constraints, so a skilled P/S could rebuild the entire IMS from the BoE alone.
Prioritize (top risks, primary critical path) and progress across iterations.
**Trade-offs** — too large to do at once; the burden of proof sits on programmatic and
technical staff to defend their choices.

## 16. Disposition variances through Watch / Retain / Replan / Rebaseline (ch07)
**When** — control, after measuring performance against pre-set thresholds.
**How** — Watch and Retain leave the PMB unchanged; Replan re-schedules to-go work internally;
Rebaseline changes the ABC externally. Pre-set the stoplight thresholds in the SMP so the
action is decided before the variance appears.
**Trade-offs** — for P/ps over $250M, NPR 7120.5 mandates a replan at 15% over ABC, a
rebaseline at 30%, and a replan on a >6-month key-milestone slip; frequent rebaselining
distorts the IMS and risks a "rubber baseline."

## 17. Corroborate across a suite of metrics (ch07)
**When** — measuring schedule performance.
**How** — combine deterministic gauges (SV/SVt, BEI/CEI/HMI, SPI/ES, CPLI, float, margin) with
stochastic ones (BandAid charts, risk-based completion trend, ICSRA-vs-MA/ABC quadrants); each
has a blind spot.
**Trade-offs** — single-metric reliance misleads; cost-denominated indices dilute near
completion (lean on Earned Schedule once ~2/3 of budget is spent); a retroactive-BCR example
shows SPI green while BEI eroded and the launch slipped.

## 18. One database, many lenses for reporting (ch08)
**When** — all schedule reporting.
**How** — produce every report (one-page summary, dense PM tracker, JCL scatterplot) from a
single integrated Schedule Database, classified as Status, Progress, or Forecast; tune depth
to the audience and element importance.
**Trade-offs** — if two reports disagree the fault is the lens, not the data; never report from
separate schedule sources, and never substitute a Summary Schedule for the IMS in analysis.

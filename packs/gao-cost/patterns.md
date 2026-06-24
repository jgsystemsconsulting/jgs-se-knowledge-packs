# GAO Cost Estimating Guide Patterns & Techniques

Reusable patterns drawn from the GAO Cost Estimating and Assessment Guide (GAO-20-195G). Each has When / How / Trade-offs. These are techniques the Guide names, synthesized in original words.

## Pattern 1: Run the 12 Steps in Order — Define Before You Calculate

**When to use**: for any new program cost estimate, before producing any number.

**How**: work the steps in sequence — purpose/scope (1), plan and team (2), technical baseline (3), WBS (4), ground rules and assumptions (5), data (6), point estimate (7), sensitivity (8), risk/uncertainty (9), document (10), present (11), update (12). Steps 1-4 front-load the decisions (why, who, what, structure) that make the later math meaningful; steps 5-7 turn scope into a number; steps 8-9 surround it with confidence; steps 10-12 make it durable and approved.

**Trade-offs**: front-loading planning feels slow when stakeholders want a number now — but math built on an undefined scope, undefined program, or inconsistent structure propagates error straight into the budget. The steps are sequential by design: you cannot collect the right data until you know what you are estimating and under what assumptions.

---

## Pattern 2: Engineer the Estimate Toward the Four Characteristics

**When to use**: throughout estimate development, and as the self-check before presenting.

**How**: treat **comprehensive, well documented, accurate, credible** as design targets, not after-the-fact labels. Comprehensive = full life cycle + complete WBS, nothing omitted or double-counted. Well documented = an unfamiliar analyst could rebuild it from your write-up. Accurate = unbiased, most-likely-cost basis, inflation-adjusted, reconciled to actuals. Credible = limitations exposed via sensitivity and risk analysis, cross-checked, reconciled to an ICE. Map each of the 18 best practices to the characteristic it supports and confirm coverage.

**Trade-offs**: hitting all four costs effort (documentation and an ICE especially). But an estimate missing any one is not reliable: undocumented = indefensible, biased = wrong, no risk analysis = not credible.

---

## Pattern 3: Pick the Estimating Method by Program Maturity and Data

**When to use**: at Step 7, per WBS element — the method can differ element to element.

**How**: choose among the three core methods by what you have. **Analogy** when only a similar past system and little detail exist (early, fast, weak without a close analog). **Parametric** when you have cost data and drivers but not detailed design — build or reuse a CER linking cost to size/performance/complexity. **Engineering build-up** when the design is mature enough to sum detailed labor and material bottom-up (most accurate, most expensive). Supplement with expert opinion, extrapolation from actuals, and learning curves for recurring production. Then **cross-check** the point estimate with a second method and an independent cost estimate.

**Trade-offs**: accuracy trades against cost and required design maturity. Using a method outside its valid range (e.g., a CER extrapolated beyond its data) silently injects error. Always validate and normalize data (inflation, sizing units, recurring vs. nonrecurring) before modeling.

---

## Pattern 4: Convert the Point Estimate into a Risk-Adjusted Budget

**When to use**: at Steps 8-9, once a point estimate exists; mandatory for high-cost, high-risk programs.

**How**: first run **sensitivity analysis** (vary one input at a time between bounds; rank with a tornado chart) to find the parameters the estimate is most responsive to. Then run **risk and uncertainty analysis**: assign distributions to elements via the three-point method (min/most-likely/max) and/or the risk-driver method (probability × cost effect, tied to the risk register), and run a **Monte Carlo simulation** to produce a total-cost distribution. Read the **cumulative distribution (S curve)** to select a defensible confidence level, and size **contingency** as the gap between the point estimate and that level.

**Trade-offs**: a point estimate alone tells decision-makers nothing about confidence and tends to under-fund. Risk analysis costs effort and data, and double-counting risks (driver + three-point on the same risk) overstates the range — keep the two methods from overlapping. Budgeting to the point estimate (≈50% or lower confidence) is a recurring cause of overruns.

---

## Pattern 5: Document and Update So the Estimate Stays a Management Tool

**When to use**: Step 10 onward, ideally documenting *in parallel* with development; updating continuously over the life cycle.

**How**: capture every parameter, assumption, method, data source, and calculation in a structured package (the Guide's documentation template), so a stranger could reconstruct the result. Present it to management for **formal approval** — the estimate is not finished until approved. Then **update** it: reconcile against actual costs and program changes, analyze variances, and keep it as a living benchmark. Feed a reusable cost/technical data history for future estimates.

**Trade-offs**: thorough documentation is tedious and often skipped under schedule pressure — but without it the analytical work in Steps 1-9 cannot be validated, defended, reused, or independently reviewed. A stale estimate stops being a credible predictor; OMB requires regular updating for major acquisitions.

---

## Pattern 6: Use the Estimate as an Audit/Assessment Criterion

**When to use**: when independently reviewing an estimate or an agency's estimating process.

**How**: invert the Guide — treat each of the 18 best practices as a measurable expectation. Score the estimate against the practices, roll per-practice judgments up to the four characteristics, and roll those up to an overall reliability verdict (an estimate fully reflecting all four is *reliable*). Separately, compare an agency's written guidance against the 12 steps and their task lists to find process gaps. Use the figures mapping best practices to characteristics to know which steps to examine for each judgment; ground criteria in relevant laws/regulations and confirm they are current.

**Trade-offs**: scoring requires evidence (data collection instruments, interviews, independent computation) and judgment about partial compliance. A practice the guidance fails to require is a gap in the *process*, not just one estimate.

---

## Pattern 7: Pair the Cost Estimate with EVM for Execution

**When to use**: for major acquisitions with development effort (OMB requires EVM); whenever you need to know if a program is on track, not just how much it has spent.

**How**: convert the time-phased cost estimate into a **performance measurement baseline (PMB)** and run **EVM**: track planned value (BCWS), earned value (BCWP), and actual cost (ACWP). Derive **CPI** (BCWP/ACWP) and **SPI** (BCWP/BCWS); forecast an **EAC** from cumulative CPI; use **TCPI** for the efficiency needed to finish on target. Confirm the baseline is executable with an **integrated baseline review (IBR)** — the link between the estimate and EVM — and validate the EVM system against **EIA-748's 32 guidelines**. Share data between cost estimators and EVM analysts rather than working in isolation (itself a best practice).

**Trade-offs**: spending data alone misleads (the railroad example — looking under-budget while badly behind). EVM adds the missing "value of work done" so problems surface while there is still time to recover. EVM requires a disciplined system, an objective earned-value method per task (avoid level-of-effort where possible), and reprogramming (over-target baseline) when the baseline becomes unexecutable.

---

## Pattern 8: Reach for Specialized Techniques When the Cost Behaves Differently

**When to use**: when a generic analogy or build-up would misrepresent the cost dynamics.

**How**: for **software**, size first (SLOC, function points, COSMIC, use case) then convert to effort via a productivity factor, classifying code as new/reused/adapted/auto-generated; watch the black-box parametric tools and inconsistent counting rules. For **repetitive production**, apply **learning curves** (unit or cumulative-average theory, Y = AX^b), with Anderlohr/retrograde adjustments for production breaks. For **choosing among solutions**, run a disciplined **Analysis of Alternatives** (22 best practices, NPV where benefits monetize). For **structuring scope**, start from a **WBS template** (MIL-STD-881D, NASA/DOE/PMI handbooks). Ground the whole enterprise in the **Green Book** internal-control framework — the estimating process itself is an internal control.

**Trade-offs**: each technique exists because the default would be wrong, but each adds specialized knowledge and data demands (e.g., ERP estimating is notoriously unreliable; sizing methods lack standardized counting). Match the technique to the cost driver, not the convenience.

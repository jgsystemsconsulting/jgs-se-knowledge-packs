# Chapter — Cost Estimate Tasks (Tasks 8–12: Develop, Cost Risk, Document, Present, Update)

## Core Idea

The third and final phase of NASA's cost estimating process is where the estimate is actually produced, hardened against uncertainty, written down, briefed, and kept alive. The NASA Cost Estimating Handbook (CEH) v4.0 splits this phase into its last five tasks (8 through 12). The throughline is that a single point number is never the deliverable. Task 8 produces an initial life-cycle cost (LCC) point estimate, but the handbook is explicit that this point value is uncertain, non-definitive, and merely the start of a cost-risk process. Tasks 9 through 12 then convert that fragile point into something a decision maker can trust: a probabilistic range of outcomes, a written justification thorough enough that an independent analyst could rebuild it, a briefing that survives scrutiny, and an updateable baseline that tracks reality as the project advances. The recurring quality bar across all five tasks is reproducibility — the estimate must be traceable, defensible, and repeatable.

## Frameworks Introduced (exact source names, when/how)

- **LCC point estimate (Life-Cycle Cost point estimate)** — produced in Task 8 by populating the selected/constructed model with normalized data per the ground rules and assumptions (GR&A), then running it. The handbook frames it as the beginning, not the end, of the cost-risk process.
- **Ground Rules and Assumptions (GR&A)** — verified as the first activity of Task 8 and governing how the model is populated; must be fully documented for the cost-risk analysis as well.
- **Beta Curves** — named as one technique (alongside historical spreads, engineering judgment, and budget constraints) for time-phasing the estimate against the planned development schedule in Task 8.
- **Constant-Year (CY), Real-Year (RY) / then-year, and Fiscal-Year dollars** — the inflation/phasing apparatus used in Task 8: baseline estimates built in CY dollars are phased by fiscal year, converted to RY (then-year) dollars, and those RY dollars feed the annual NASA budget. Phasing is further adjusted to reflect budget authority when budgets are being built. Detail is deferred to Appendix F.
- **Probabilistic cost estimate** — introduced in Task 8 as the enhancement of the deterministic point estimate. NASA has championed probabilistic over deterministic estimating for more than a decade (community adoption traced to the early 2000s). Methods are categorized as inputs-based, outputs-based, and scenario-based, and may use Monte Carlo simulation or be analytical.
- **Technical Baseline Estimate (TBE) / "point estimate"** — the deterministic anchor some analysts develop before probabilistic analysis; the handbook stresses this sequencing is not mandatory and the two efforts are often run in parallel and iteratively.
- **Cumulative Distribution Function (CDF) / "S-curve"** — the central deliverable of Task 9: a credible project cost S-curve spanning the project's range of costs, against which confidence levels are read.
- **Cost-Risk Assessment** — the six-activity Task 9 process for establishing the current confidence level and the unallocated future expense (UFE) needed to reach a target confidence. Methodology detail lives in Appendix G.
- **Unallocated Future Expense (UFE)** — the budgeted reserve quantified by the risk analysis to reach a chosen confidence level; selected by the appropriate NASA management council and reported as the recommended level at Confirmation Reviews.
- **Sensitivity Analysis** — recommended in Task 9 to find the major cost drivers (the parameters whose change moves cost the most); cross-referenced to Section 4.1 and Appendix G.
- **Basis of Estimate (BOE)** — the written justification produced in Task 10, capturing GR&A, drivers, model inputs, analogy rationale, and supporting detail.
- **Comparison Cost Track / cost trace** — an element-by-element comparison required in Task 10 (and Task 12) to identify and explain deviations from a prior estimate.
- **Cross Checks** — secondary estimates built from the same normalized data but with different models/techniques (e.g., parametric vs. analogous program, or two parametric models, or independent runs of the same model) to test reasonableness.
- **Cost Estimating Relationship (CER)** — when used, must be presented with its full source citation (or the calibration model and dataset) so a reviewer can reconstruct it; documentation must include descriptive statistics (Appendix C).
- **Non-Advocate Review (NAR)** — cited as the kind of formal cost review where poorly documented analyses fare badly.
- **CADRe (Cost Analysis Data Requirement)** — a well-documented CADRe supports establishing and revalidating the baseline.
- **Program Cost Commitment (PCC)** — the commitment that NPR 7120.4 requires be revalidated annually, a process eased by explicit BOE documentation.
- **Peer review** — an outside "sanity check" completed in full once the estimate is documented and before it is briefed.
- **Earned Value Management (EVM)** — named in Task 12 as a recognized best practice for adjusting cost and schedule estimates against actual performance (e.g., monthly/quarterly), with detail in Appendix I.

## Key Concepts

- **The point estimate is a starting line, not a finish line.** Task 8 yields a point estimate, but the handbook is unambiguous that project costs are uncertain and this single number is neither definitive nor the only plausible answer. Everything after Task 8 exists because of that uncertainty.
- **Summing most-likely values understates the total.** A core statistical caution: adding up the most-likely point estimates of components tends to underestimate total cost, because the sum of most-likely values is not the most-likely total. This is the conceptual reason a probabilistic roll-up is needed rather than naive addition (citing Garvey, *Probability Methods for Cost Uncertainty Analysis*).
- **Time-phasing and inflation are mechanical but consequential.** Estimates built in constant-year dollars must be phased by fiscal year and converted to real-year dollars before they can feed a budget, and phasing must be further reconciled with when budget authority is actually needed versus when funds are spent.
- **UFE is confidence made budgetable.** Cost-risk analysis quantifies how much reserve is required to hit a desired confidence level; that reserve (UFE) should be phased into the estimate where it is most likely to be consumed — typically between PDR and CDR when problems surface, and again during Integration and Test.
- **Two ways to use UFE in trades.** For analyses of alternatives, an analyst can either hold confidence constant across options (adding UFE and reporting the resulting cost) or hold cost constant (and report the resulting confidence level). Choosing one keeps alternatives comparable.
- **Reproducibility is the documentation acceptance test.** The governing rule of thumb for Task 10 is that the BOE should let an independent analyst — or a review team member — reproduce the estimate. The minimum level of detail is whatever lets another estimator reconstruct it.
- **Document continuously, not at the end.** Cost estimators are told to capture LCC results throughout the entire process, beginning early and continuing through completion — not waiting until the estimate is "done."
- **Sensitivity analysis as a back-off strategy.** A sensible pattern is to first derive an unconstrained solution meeting all mission objectives, then deliberately back off in the interest of saving money — while taking care not to degrade the material solution so far that its benefits are lost.
- **Presentation is a defense, plus a feedback loop.** Task 11 is not just making charts: it is creating briefing material, presenting and defending the estimate, and gathering feedback to improve the next one. The briefing should focus attention on the cost drivers and cost results.
- **The estimate is a living baseline.** Task 12 treats updating as ongoing: refresh whenever project content changes, reconcile to the baseline, and use customer feedback and lessons learned. A maintained baseline is a forward indicator of cost overruns and shortens turnaround for "what-if" drills.

## Mental Models

- **Point estimate → S-curve → reserve.** Read the five tasks as a pipeline that transforms a fragile single number into a confidence curve and then into a dollar reserve. The point estimate (Task 8) is one sample; the S-curve / CDF (Task 9) is the full distribution; UFE is the slice of that distribution you buy to reach your chosen confidence.
- **Confidence as a dial, cost as the readout (or vice versa).** In trade studies you can pin either axis. Hold confidence and read cost, or hold cost and read confidence — but pick one consistently so alternatives are apples-to-apples.
- **The "rebuild test."** Before declaring documentation complete, ask: could a stranger with this BOE and its cited sources regenerate my number without phoning me? If not, the documentation is incomplete by the handbook's own standard.
- **Cross-check triangulation.** Treat any single model's output as one bearing. Confirm it with a second, independent bearing — a different model, an analogy, or an independent run — especially on the high-cost, high-risk portions, then triangulate the credible value.
- **Parallel-and-iterate, not strictly serial.** Don't picture Tasks 8 and 9 as a clean handoff. The deterministic TBE and the probabilistic analysis are frequently developed concurrently, with iteration as data, models, and methods are refined.
- **Phase the reserve where the pain lands.** UFE is not spread evenly; it is concentrated where risk realizes — the PDR-to-CDR window and Integration and Test. Budget the reserve to match the risk timeline, not the calendar.

## Anti-patterns (only if the source named them)

- **Reporting a single cost in a trade study.** The handbook warns that a single estimate (such as an expected cost) can mislead a trade team by hiding the potential for overruns — a probabilistic view is needed instead.
- **Poorly documented analyses.** Experience from formal reviews (e.g., NARs) is cited as proof that poorly documented analyses fare badly; if the analyst cannot explain the rationale behind each estimate, the whole project's credibility suffers.
- **Naively summing most-likely values.** Adding most-likely point estimates is called out as a method that, in most cases, understates total cost — the source flags it as a statistical trap, not a valid shortcut.
- **Over-backing-off in sensitivity analysis.** The handbook cautions against backing off a solution so far that the benefits of the material solution are significantly altered — cost-cutting that guts the value of the design is a named hazard.

## Key Takeaways

- Task 8 builds the LCC point estimate (verify GR&A, populate with normalized data, ensure full-cost compliance, run, time-phase, adjust for inflation, cross-check, and track to prior/independent estimates) — but the point value is explicitly just the entry point to cost-risk work.
- Task 9 converts uncertainty into a credible S-curve (CDF) via a six-step cost-risk assessment, and quantifies the UFE needed to reach a management-chosen confidence level; sensitivity analysis surfaces the dominant cost drivers.
- Task 10 produces a BOE so complete that an independent analyst could reproduce the estimate, documents continuously from the start, includes a comparison cost track for any change, and is validated by cross checks and a peer review before briefing.
- Task 11 creates, presents, and defends the estimate while harvesting feedback for the next cycle; consistency in format across Centers aids the management review.
- Task 12 keeps the estimate alive — updating on content change and milestone reviews, reconciling to baseline, and using EVM to adjust against actual performance — so the baseline stays a forward indicator of overruns.
- The unifying quality attributes across the whole phase are traceability, defensibility, and repeatability.

## Connects To

- **Pairs with nasa-risk.** Tasks 8–12 are where cost meets risk in dollar terms: the probabilistic estimate, the cost-risk assessment, the S-curve/CDF, and the UFE reserve are all the financial expression of risk and uncertainty management. The cost-risk assessment identifies and quantifies the same kinds of technical, schedule, and requirements risks that a risk-management process tracks — here phased into the estimate where they are most likely to bite. Read this chapter alongside nasa-risk to see the two sides (risk identification/handling and risk-informed budgeting) of one coin.
- **Upstream tasks of the CEH process** — Task 8 depends on a selected/constructed model and gathered, normalized data from the earlier tasks; the GR&A verified here originate upstream.
- **Appendices of the handbook** — phasing/inflation detail (Appendix F), probabilistic explanation and CER/descriptive statistics (Appendix C), cost-risk methodology and sensitivity analysis (Appendix G), documenting the estimate (Appendix H), and performance-based updating via EVM (Appendix I).
- **NASA program governance** — Confirmation Reviews and Authority-to-Proceed decision points consume the UFE recommendation; NPR 7120.4's annual PCC revalidation depends on the BOE and CADRe documentation produced in Task 10.

# Chapter — Economic Analysis, Discounting, and Net Present Value

> Source: NASA Cost Estimating Handbook (CEH) Version 4.0, February 2015, Section 4.5–4.6 ("Economic Analysis" through "Documentation and Review of an Economic Analysis").
> Pairs with **nasa-risk**: economic analysis explicitly carries a sensitivity-and-risk-analysis step, and its results feed the same decision-support function that risk analysis informs.

## Core Idea

An economic analysis (EA) is a structured way to choose among competing alternatives by building and comparing their discounted cash flows — costs and benefits projected over time and pulled back to a common present-day value. Where a life-cycle cost estimate (LCCE) tells you what an option costs, an EA goes further: it sets cost against benefit, applies discounting so that money in different years can be compared on equal footing, and produces economic measures of merit such as net present value (NPV) and benefit-cost ratios. The CEH frames EA as the technique federal decision makers use to judge whether departing from the status quo (the "do-nothing" baseline) is worth it — for example, whether the future payoff of new research, an acquisition, or a changed maintenance procedure justifies the near-term spend.

Crucially, the handbook is emphatic that an EA does not make the decision. It surfaces the significant factors, sharpens the differences and similarities between options, and quantifies what can be quantified — but the manager still supplies judgment, experience, and values. The EA's job is to leave that manager with a far better grasp of the investment options than they had before.

## Frameworks Introduced (exact source names, when/how)

- **Economic Analysis (EA)** — introduced in §4.5 as the primary discipline of the chapter. Defined (§4.5.1) as a systematic approach to allocating scarce resources to meet a given objective, recognizing that multiple alternatives exist and each consumes resources and yields results. The CEH gives EA two governing principles: (1) every feasible alternative must be considered and its life-cycle costs and benefits evaluated; (2) all costs and benefits must be adjusted to present value using discount factors to reflect the time value of money.

- **OMB Circular A-94** — named in §4.5.2 as the overall reference for all federal programs. Published October 1992 as "Guidelines and Discount Rates for Benefit-Cost Analysis of Federal Programs," it prescribes discount rates (which the source likens to inflation rates) that OMB refreshes annually. The handbook treats A-94 as the authority for which interest/discount rate to use, and (§4.6.3) as the source that establishes NPV as the standard criterion for justifying a government project.

- **NASA New Start Inflation Index (NNSI)** — cited in §4.5.3.2 as the index NASA publishes yearly that cost analysts should apply when adjusting for inflation. It is invoked specifically to keep inflation (loss of purchasing power) distinct from the time-value-of-money.

- **Net Present Value (NPV)** — established in §4.6.3 via OMB Circular A-94 as the standard measure for ranking alternatives. The decision rule is to prefer the alternative with the most positive NPV.

- **The seven-step EA process** — laid out in §4.6.1 (and illustrated as Figure 16) as the procedure for actually performing an EA.

- **Other measures of merit** — §4.6.3 names **Equivalent Uniform Annual Cost (EUAC)** and the **Savings/Investment Ratio (SIR)** as additional measures, with full treatment deferred to Appendix N.

- **DoD Instruction 7041.3** — referenced as the source of the two EA principles, establishing that both the magnitude and the timing of costs and benefits matter.

## Key Concepts

**What separates an EA from an LCCE.** The handbook lists three differentiators: an EA applies discounting, it weighs costs against benefits (rather than just tallying costs), and it produces economic measures of merit. An LCCE feeds the EA, but the EA is the comparative, decision-oriented layer on top.

**Time-value-of-money.** A dollar paid or received today is worth more than the same dollar at any future date. The source attributes this to two forces: the opportunity to earn interest on cash you hold, or the cost of paying interest on capital you borrow. This is the philosophical bedrock of discounting.

**Interest vs. inflation — two different effects.** The CEH insists these not be conflated. Inflation is the erosion of a dollar's purchasing power as general prices rise; you handle it with the NNSI. The time-value-of-money is the separate fact that a dollar now is worth more than a dollar later because today's dollar can be invested and earn a return. The worked example: a dollar invested today in a fixed-interest account grows to more than a dollar a year out.

**Interest and interest rate.** Interest is the money paid or received over time (expressed in dollars); the interest rate is the percentage of principal earned or charged over time. Interest is expressed as a percent or decimal, assessed on the dollar balance, stated for a defined period (usually annual), and chosen based on project life and analysis type (constant vs. current dollar).

**Nominal rate vs. real rate.** The nominal rate includes inflation and applies to cash flows stated in current- or then-year dollars — it's the form most consumer loans and investment returns are quoted in. The real rate is the nominal rate stripped of anticipated inflation/deflation and applies to cash flows in constant- or base-year dollars (stable purchasing power). Real rates are the ones used when the EA's cash flows are in constant base-year dollars.

**Base-year vs. then-year dollars.** A-94 prescribes different rates depending on whether the analysis is in base-year dollars (inflation removed) or then-year dollars (inflation included); the gap between them is an assumed general inflation rate.

**Future value, present value, and the discount factor.** Future Value is computed from compound interest: FV = PV(1 + i)^n, in which i denotes the interest rate and n counts the years elapsed since project initiation — equivalently, PV times the compound interest factor (1 + i)^n. Rearranging algebraically (dividing both sides by the compound interest factor) gives Present Value: PV = FV / (1 + i)^n, i.e., FV times the discount factor 1 / (1 + i)^n. PV is the amount that, invested today at the current rate, would equal the future cash flow. Adjusting a future amount back to a common point in time (conventionally the present) is what the source calls **discounting** — the reverse of compounding.

**The discount rate is the opportunity cost.** The handbook notes the rate i in compound interest is the same i used to discount future cash streams, so it keeps a single symbol. The discount rate represents the opportunity cost of the investment — the return forgone by putting funds to one use instead of another. Per A-94 policy, the government justifies its discount rate simply as its cost of borrowing, reflected in Treasury bill rates; the source notes this kept federal discount rates rarely above 7 percent over roughly two decades.

**Discount-factor conventions.** Because i and n are annual, the factor 1 / (1 + i)^n is an End-of-Year (EOY) discount factor and applies only to EOY cash flows. The source flags Middle-of-Year (MOY) and continuous conventions as alternatives, detailed in Appendix C.

**The seven-step EA process** (§4.6.1):
1. Prepare the statement of objective.
2. List assumptions and constraints.
3. Identify the alternatives.
4. Identify and estimate benefits and costs.
5. Order the alternatives by their economic measures of merit.
6. Run sensitivity analysis and risk analysis on the ranking.
7. Prepare results and recommendation (documentation).

**The quantifying-benefits problem.** Space science programs rarely have benefits that are easy to quantify credibly — the value of a science mission resists hard numbers. When benefits can't be monetized, the EA degrades gracefully into a **cost-effectiveness analysis** that turns instead on how complete and credible the LCCE is and on the expected quality of the science data returned; qualitative benefits are judged by expert panels. The structure of any EA hinges on two questions: is it a spaceflight vs. institutional effort, and are the benefits quantifiable? Quantifiable benefits are more typical of institutional programs, though they can sometimes be derived for launch systems or technology programs.

**NPV as the ranking criterion.** NPV is the algebraic combination of the present values of costs and benefits, reducing an entire multi-year cash flow to one discounted number so alternatives can be compared on an equal footing. The usual mechanics: compute the net cash flow (benefits minus costs) per year, discount each year to present value, and sum. Benefits entering the NPV calculation must be expressed in financial terms. The decision rule is the most-positive NPV wins.

**Federal-government-wide perspective.** Per OMB policy, costs and benefits are viewed from the standpoint of the federal government as a whole — an EA's cash flows are not confined to the costs and benefits landing on the sponsoring organization alone.

**Documentation and external review.** Because EAs justify major NASA decisions, the documentation package must be comprehensive, complete, and clear — capturing inputs, ground rules and assumptions (GR&A), alternative descriptions, analysis approaches, risks and uncertainties, and result evaluations. The source warns that major decisions can be reviewed by the NASA Inspector General and outside bodies such as the GAO, and a well-documented analysis helps the Agency respond.

## Mental Models

**EA as a lens, not a verdict.** Picture the EA as a high-resolution lens that brings the trade space into focus — it enumerates factors, clarifies how options differ, and quantifies the quantifiable. The decision still belongs to the human who looks through the lens and adds judgment. If you find yourself treating the NPV ranking as the answer rather than the input, you've misread the tool's role.

**Compounding and discounting are the same arrow, run in opposite directions.** Compounding pushes a present dollar forward into a larger future dollar via (1 + i)^n; discounting pulls a future dollar back to the present by dividing by that same factor. Same physics, reversed. The single symbol i for both interest and discount rate is the source's own signal that these are one mechanism.

**Two distinct erosions of a dollar.** Hold two separate ideas: inflation erodes *purchasing power* (handled by the NNSI), while the time-value-of-money reflects the *forgone earning* of a delayed dollar (handled by the discount rate). Mixing them double-counts or omits an effect. The nominal-vs-real rate distinction exists precisely to keep them straight: real rates have already removed the inflation piece, so use them only with constant-dollar cash flows.

**The discount rate is what you gave up.** Frame i as opportunity cost: it is the return you forfeited by committing funds here instead of to the next-best use. The government's version of that opportunity cost is its cost of borrowing (Treasury rates) — which is why federal rates have hovered below 7 percent.

**When benefits won't hold still, change the question.** If you can't put a credible dollar figure on a science mission's value, don't force a fake number — pivot to cost-effectiveness, where the comparison rests on cost quality and the quality of the science returned, with experts supplying the qualitative benefit judgment. The CEH treats this as a legitimate fallback, not a failure.

**The process is a loop, not a ladder.** Although the seven steps are numbered, the handbook stresses they interrelate and get revisited — objectives shift as alternatives or benefit estimates evolve. Treat the sequence as a starting cycle you iterate, especially around steps 3–6.

## Key Takeaways

- An EA exists to compare alternatives' discounted cash flows and justify (or reject) a departure from the status quo; it informs but never replaces the decision maker.
- Three things make an EA more than an LCCE: discounting, weighing costs against benefits, and producing measures of merit (NPV, benefit-cost ratios).
- OMB Circular A-94 is the governing federal reference — it prescribes the discount rates (updated annually) and establishes NPV as the standard justification criterion (most-positive NPV preferred).
- Keep inflation and time-value-of-money separate: use the NASA New Start Inflation Index for inflation; use the discount rate (an opportunity cost, ≈ government borrowing cost) for time value.
- Match the rate to the dollars: nominal rates with current/then-year cash flows, real rates with constant/base-year cash flows.
- FV = PV(1 + i)^n; PV = FV / (1 + i)^n. The EOY factor 1 / (1 + i)^n applies only to end-of-year cash flows; MOY and continuous conventions exist for other timings.
- Run the seven-step EA iteratively, and note that step 6 is explicitly sensitivity *and risk* analysis — the formal hook into risk work.
- When benefits resist quantification (typical of science missions), convert the EA into a cost-effectiveness analysis grounded in LCCE quality and expert-judged science value.
- Document the EA thoroughly (inputs, GR&A, alternatives, approaches, risks, results) because IG and GAO review is a real possibility for major decisions.

## Connects To

- **nasa-risk** *(designated pairing)* — Step 6 of the EA process, "perform sensitivity and risk analyses," makes risk analysis a built-in stage of every economic analysis. The uncertainty in cost and benefit estimates that risk methods characterize is exactly what gets stress-tested before alternatives are ranked, and the documentation package explicitly captures "risks and uncertainties."
- **Life-Cycle Cost Estimating (LCCE)** — the EA consumes the LCCE as its cost backbone; in cost-effectiveness mode the quality of the LCCE *is* the analysis. The two are layered, not alternatives.
- **OMB Circular A-94 and federal cost-benefit policy** — the same external authority that governs discount-rate selection and the government-wide perspective on costs and benefits, linking NASA practice to the broader federal benefit-cost analysis canon.
- **GAO and IG review / decision documentation** — the audit-readiness emphasis ties EA practice to external oversight regimes (notably GAO), connecting to broader cost-credibility and audit-trail concerns across the cost-estimating discipline.
- **Inflation indexing (NNSI)** — the normalization machinery that lets multi-year cash flows be compared, shared with any constant-vs-current-dollar treatment elsewhere in the handbook.

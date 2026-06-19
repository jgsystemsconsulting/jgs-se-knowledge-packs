# Chapter 5: RIDM Part 3 — Risk-Informed Alternative Selection

## Core Idea
Part 3 integrates probabilistic risk analysis into a deliberative decision process: Step 5 establishes risk-normalised performance commitments (consistent risk tolerance across all alternatives), and Step 6 conducts deliberation leading to a documented, risk-informed selection recorded in the Risk-Informed Selection Report (RISR).

## Frameworks Introduced
- **Performance Commitments**: Performance measure values set at a specified percentile of each alternative's probability distribution, so that the probability of failing to meet the commitment is equal across all alternatives for a given measure.
  - When to use: Step 5 — before deliberation begins; normalises risk so that alternatives are compared on capability, not luck.
- **Risk-Informed Selection Report (RISR)**: The formal document capturing the selected alternative, finalised performance commitments, the risk list, decision rationale, and robustness assessment.
  - When to use: End of Step 6; serves as auditable record for requirements baselining and future RIDM re-invocations.
- **Deliberation**: An analytic-deliberative process in which stakeholders, risk analysts, and decision-makers collectively consider TBfD information, pros and cons, and other stakeholder values to reach a risk-informed decision.
  - When to use: Step 6 — after performance commitments are established and before a final alternative is selected.

## Key Concepts
- **Risk Tolerance**: The probability of failing to meet a performance commitment that a decision-maker is willing to accept for a given performance measure; set before deliberation and can vary across performance measures.
- **Risk-Normalised Comparison**: Performance commitments ensure all alternatives are evaluated at the same probability of success, allowing deliberators to focus on "what can each alternative achieve at equal risk?" rather than conflating inherent risk differences.
- **Performance Measure Ordering**: Because performance measure pdfs may be correlated, commitments are established sequentially. The first measure's commitment is set from its marginal pdf; subsequent commitments are conditioned on prior commitments being met.
- **Conditioning Effects**: If measures are positively correlated (directions of goodness aligned), lagging measures' commitments are set at higher performance. If negatively correlated, at lower performance. Low risk tolerances reduce conditioning effects.
- **Ordering Heuristic**: Order performance measures from lowest risk tolerance to highest, and in the order in which the decision-maker wants specificity, to minimise unwanted conditioning effects.
- **Dominated Alternative**: An alternative inferior to another in every performance measure; can be eliminated from contending alternatives.
- **Contending Alternatives**: Alternatives that survive the deliberation downselection as worthy of serious consideration by the decision-maker.
- **Decision Robustness**: An assessment of whether the selected alternative remains best under credible modelling perturbations and realistically foreseeable new information.

## Mental Models
- Use performance commitments the same way across alternatives: set risk tolerance first, then read off what each alternative can promise at that tolerance — this reveals capability, not luck.
- During deliberation, distinguish between "not the best alternative" and "not a contending alternative" — only dominated or infeasible alternatives should be eliminated before the decision-maker deliberates.
- Explore sensitivity of risk tolerances: if changing a tolerance from 10% to 15% switches the preferred alternative, the decision is not robust and requires more analysis or explicit stakeholder acceptance of the sensitivity.
- A decision to accept higher risk on a "stretch goal" performance measure is legitimate and should be explicit — document it in the RISR rather than burying it in default assumptions.

## Anti-patterns
- **Selecting an alternative solely on risk analysis results**: Risk analysis is one input to deliberation; non-modelled stakeholder values, political constraints, and engineering judgment must also inform the selection.
- **Setting risk tolerances after seeing the analysis results**: Risk tolerances must be set before deliberation to maintain the normative validity of the comparison; post-hoc tolerance adjustment to favour a preferred alternative is a form of result manipulation.
- **Omitting the RISR or treating it as a formality**: The RISR is the auditable link between the RIDM decision and the performance requirements baselined by systems engineering; its absence severs that link.

## Key Takeaways
1. Performance commitments are not targets — they are probability-normalised capability statements; understanding this distinction is essential to correct deliberation.
2. Risk tolerance must be set before analysing commitments, not chosen to produce a desired result.
3. Deliberation is not voting — it is a structured process of raising and collectively considering risk information and stakeholder values to support the decision-maker's final judgement.
4. The RISR is the handoff document between RIDM and both systems engineering (for requirements baselining) and CRM (for initialisation); its completeness determines whether future re-invocations of RIDM have a documented starting point.
5. Robustness assessment — checking that the decision holds under credible modelling perturbations — is a required part of the RISR, not optional.

## Connects To
- **RIDM Part 2 (Ch 4 of this pack)**: Provides the TBfD that feeds deliberation.
- **CRM Initialisation (Ch 6 of this pack)**: Receives the RISR, risk list, and performance commitments as formal CRM inputs.
- **Systems Engineering Process**: Receives performance commitments to inform requirements baselining; outputs performance requirements back to CRM.
- **NPR 8000.4A**: Specifies the requirement to document decision rationale in a formal selection report.

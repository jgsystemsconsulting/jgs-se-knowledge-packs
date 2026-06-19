# Chapter 3: RIDM Part 1 — Identification of Alternatives

## Core Idea
Decision alternatives can only be identified in the context of the objectives they must satisfy; Part 1 establishes that context by decomposing stakeholder expectations into quantifiable performance measures and imposed constraints, then compiling a set of feasible alternatives against that framework.

## Frameworks Introduced
- **Objectives Hierarchy**: A tree structure that decomposes a top-level objective through the four mission execution domains (Safety, Technical, Cost, Schedule) into progressively more specific, quantifiable performance objectives.
  - When to use: Always in RIDM Step 1 — before alternatives can be meaningfully evaluated.
- **Performance Measures**: Metrics assigned to each quantifiable performance objective, enabling probabilistic comparison of alternatives.
  - When to use: Once the objectives hierarchy is complete; each leaf-level objective receives one performance measure.
- **Trade Tree**: A systematic decomposition of the design space used in Step 2 to enumerate feasible alternatives before pruning infeasible ones.
  - When to use: When compiling candidate alternatives for risk analysis; preliminary evaluation at this stage reduces the analytical burden of Part 2.

## Key Concepts
- **Top-Level Objectives**: Qualitative, multifaceted statements of what stakeholders hope to achieve — typically too complex for direct assessment; must be decomposed.
- **Imposed Constraints**: Hard limits on performance measure values; failure to comply means the top-level objective is not achieved. Any alternative that violates an imposed constraint is infeasible.
- **Fundamental vs. Means Objectives**: Fundamental objectives state what to achieve (e.g., Minimise Loss of Life); means objectives state how to achieve it (e.g., Maximise Use of Vehicle-Safety Features). Objectives hierarchies must use fundamental objectives only — presupposing a solution biases the analysis.
- **Performance Objective Properties**: A complete set must be Complete (all areas of concern), Operational (decision-maker can ascribe value), Non-redundant (conceptually distinct), and Solution-independent (applicable to any reasonable alternative).
- **Proxy and Constructed Scales**: Used when a performance objective is qualitatively important but not directly measurable; proxy scales relate it to a measurable surrogate; constructed scales define an explicit ordinal scoring scheme.
- **Test of Importance**: Before including an objective in the hierarchy, ask whether the best course of action could be altered if that objective were excluded. If no, the objective may be omitted — but check that excluded objectives don't collectively matter.
- **Stakeholders**: Individuals or organisations materially affected by the outcome of a decision, including both internal (NASA HQ, Centres, advisory committees) and external (White House, Congress, scientific community) parties.

## Mental Models
- Use the test of importance to prune the objectives hierarchy to a manageable size without inadvertently excluding collectively significant objectives.
- Order performance objectives at the same level of the hierarchy — don't mix sub-objectives from different depths in comparisons.
- If a performance objective implies a specific design approach, it is a means objective, not a fundamental one; rewrite it at the level above.
- Compile alternatives broadly in Step 2, then prune rather than speculate narrowly from the start — infeasibility is determined by analysis, not assumption.

## Anti-patterns
- **Using means objectives in the hierarchy**: Presupposes a solution and eliminates potentially superior alternatives from consideration.
- **Deriving performance measures before the hierarchy is stable**: Premature measurement operationalises a hierarchy that may not yet capture all relevant stakeholder concerns, locking in gaps.
- **Pruning alternatives by intuition before risk analysis**: Alternatives that appear costly or complex may outperform cheaper options once risk is properly accounted for; premature pruning discards valid contenders.

## Key Takeaways
1. RIDM begins with understanding stakeholder expectations, not generating solutions — objectives drive alternatives, not vice versa.
2. The objectives hierarchy must be complete, operational, non-redundant, and solution-independent; failure on any property undermines the validity of subsequent comparisons.
3. Imposed constraints define the feasibility boundary — any alternative that cannot satisfy them within any reasonable risk tolerance is infeasible.
4. Fundamental objectives, not means objectives, belong in the hierarchy; deterministic engineering standards are almost always means objectives.
5. Trade trees help enumerate alternatives systematically; preliminary evaluation and pruning at this stage reduces the cost of the full risk analysis in Part 2.

## Connects To
- **RIDM Part 2 (Ch 4 of this pack)**: Accepts the outputs of Part 1 — feasible alternatives, performance measures, imposed constraints — as its inputs.
- **NPR 7123.1A / NASA Systems Engineering Handbook**: Stakeholder expectations definition process and systems engineering process requirements.
- **Clemen (1996) and Keeney-Raiffa (1993)**: Referenced methodology sources for objectives hierarchies and multi-attribute decision analysis.

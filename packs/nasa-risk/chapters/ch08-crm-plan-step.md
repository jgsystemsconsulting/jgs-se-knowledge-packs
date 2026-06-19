# Chapter 8: CRM — Plan Step

## Core Idea
The Plan step is a risk-informed decision-making process within CRM: it generates candidate risk response options from identified risk drivers, combines them into risk response alternatives, analyses their effect on performance risk, deliberates, and selects and documents an alternative for implementation.

## Frameworks Introduced
- **Six Risk Disposition Types**: Accept, Mitigate, Watch, Research, Elevate, and Close — the categorisation scheme from NPR 8000.4A for all risk response options.
  - When to use: For every individual risk and performance risk that has passed through the Analyze step; each risk receives one or more disposition types.
- **Risk Response Option**: An individual response pertaining to one disposition type; the building block from which alternatives are constructed.
  - When to use: Generated through brainstorming informed by risk driver characterisation; options are pruned before alternatives are formed.
- **Risk Response Alternative**: A specific combination of risk response options that collectively address the current risk posture; evaluated as a unit by the risk analysis.
  - When to use: After options are generated and pruned; the set of alternatives is the input to the CRM deliberation and selection process.
- **Risk Response Matrix**: A tabular tool mapping risk response options (columns) to risk response alternatives (rows), enabling systematic identification and downselection of candidate alternative combinations.
  - When to use: When constructing alternatives from a pool of options to keep the combinatorial explosion manageable.

## Key Concepts
- **Two Planning Pathways**: Tactical (from near-term criticality list — quick-action response required before full analysis is complete, relying on engineering judgment and point estimates) and Strategic (from in-depth graded analysis — full risk driver characterisation, comprehensive alternatives, integrated risk model).
- **Accept**: No action needed because performance risks are all within tolerable levels; must be documented with assumptions. Accept cannot be combined with other options; it applies to the full risk posture.
- **Mitigate**: Positive action addressing risk drivers; two categories — Departure Prevention (reduces likelihood of the departure event) and Consequence Reduction (reduces severity if departure occurs). May require rebaselining of derived requirements.
- **Watch**: Monitoring plan for observables related to a risk driver, with pre-established criteria and optional contingency plans. Does not modify the baseline project plan.
- **Research**: Investigation plan to reduce uncertainty about a risk driver; includes research schedule and contingency plans conditional on findings.
- **Elevate**: Transfer of performance risk management to the next higher organisational level when no available combination of options can return risk to tolerable levels. Typically combined with Watch; should not be proposed as an initial option.
- **Close**: Removes individual risks and risk drivers from active management when their likelihood or consequence has been reduced below a defined level of insignificance, or when the departure has occurred (becoming a problem rather than a risk).
- **Risk Response Plan (RRP)**: The evolving document capturing identified risk drivers, proposed response options, and proposed alternatives; shared across affected organisational units to identify synergies and cross-cutting risks.
- **Downselecting Alternatives**: Alternatives are narrowed by eliminating those that are infeasible (fail to restore performance risk to tolerable levels), dominated (inferior to another in all performance requirements), or markedly inferior on key requirements.

## Mental Models
- Generate response options from risk driver characterisation, not from the risk statement alone — driver-level options address root causes, not just symptoms.
- Combine options into alternatives systematically using the Risk Response Matrix; look for alternatives that address multiple risk drivers and multiple organisational units simultaneously.
- Use tactical planning to stop the bleeding (protect the window of opportunity), then use strategic planning to cure the disease (address the root drivers in the integrated risk model).
- Elevate only after demonstrating that no available combination of Mitigate, Watch, and Research options can return the risk to tolerable (or at least marginal) levels — elevation is a last resort, not a default escalation.
- Close proactively at the start of each strategic Plan step to remove irrelevant risks before generating alternatives; it sharpens focus on the risks that actually matter.

## Anti-patterns
- **Proposing Elevate as an initial response**: Elevation is valid only after exhausting available options at the current level; premature elevation under-uses the planning capability of the unit and creates unnecessary burden upstream.
- **Generating alternatives without risk-analysing them**: The plan step requires probabilistic evaluation of each alternative's effect on performance requirements — qualitative pros/cons alone do not constitute a risk-informed selection.
- **Ignoring new risks introduced by risk response alternatives**: Mitigation options often create new individual risks (mass increase, schedule slip, new technology dependency); these must be identified and communicated to the decision-maker as part of the deliberation package.
- **Treating Accept as a passive default**: Accept is an explicit, documented decision that current performance risks are tolerable under stated assumptions — it must be justified and revisited as conditions change.

## Key Takeaways
1. The six disposition types cover the full response space; every identified risk must receive a documented disposition at every decision point, even if that disposition is Accept.
2. Tactical and strategic planning are both present in every CRM cycle; tactical protects short windows of opportunity while strategic builds a durable risk posture.
3. Mitigation can be departure prevention or consequence reduction — a defence-in-depth strategy combines both layers where risk drivers are complex.
4. Elevate transfers management authority but not shared understanding; the elevating unit must coordinate modelling assumptions and communicate its risk drivers clearly to the receiving unit.
5. The Risk Response Plan shared across organisational units is the mechanism for identifying synergistic responses that address cross-cutting risk drivers more efficiently than unit-isolated responses.

## Connects To
- **CRM Analyze Step (Ch 7 of this pack)**: Provides risk drivers (strategic) and near-term criticality list (tactical) that trigger the two planning pathways.
- **CRM Track Step (Ch 9 of this pack)**: Receives the selected risk response alternative and its tracking requirements.
- **RIDM Part 2 (Ch 4 of this pack)**: Plan deliberation and selection process parallels RIDM Step 6; risk response analysis parallels RIDM Step 4.
- **NPR 8000.4A**: Defines the six risk disposition types that all NASA risk response options must map to.

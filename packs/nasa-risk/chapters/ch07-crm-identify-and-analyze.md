# Chapter 7: CRM — Identify and Analyze Steps

## Core Idea
The Identify step captures concerns as structured individual risk statements before they become problems; the Analyze step assesses their aggregate effect on performance requirements using a two-track approach — a Quick Look for urgency ranking and a Graded Approach for in-depth driver identification.

## Frameworks Introduced
- **Individual Risk Statement (Condition–Departure–Asset–Consequence format)**: "Given that [CONDITION], there is a possibility of [DEPARTURE] adversely impacting [ASSET], thereby leading to [CONSEQUENCE]."
  - When to use: Whenever a new risk is identified by any project personnel; the structure grounds the risk in fact (CONDITION) while separating scenario from consequence.
- **Eight-Question Validity Test**: A checklist for validating an individual risk statement before entry into the risk database, covering adequacy of communication, evidence basis, baseline deviation, factual condition, credible departure, measurable consequence, independence from mitigation, and actionability.
  - When to use: Applied by the risk identifier and reviewed by risk management personnel upon every new risk entry.
- **Risk Scenario Diagram (RSD)**: A flowchart from a unique initial condition through pivotal events to end states, each end state referenced to performance requirements. A specific instantiation of an Event Sequence Diagram (ESD).
  - When to use: Graded Approach Analyze step; detail level calibrated to the strategic criticality of the individual risk.
- **Quick Look Analyze Step**: Rapid criticality ranking of individual risks into near-term (tactical) and long-term (strategic) criticality lists, without waiting for full quantitative analysis.
  - When to use: Immediately after a new individual risk is identified; provides the basis for deciding whether a near-term response is needed before detailed analysis is complete.
- **Graded Approach Analyze Step**: In-depth probabilistic analysis using RSDs to identify risk drivers — the specific uncertain elements that drive performance risk to marginal or intolerable levels.
  - When to use: For all individual risks with non-trivial strategic criticality; depth of analysis proportional to strategic criticality ranking.

## Key Concepts
- **CONDITION**: A current, fact-based situation causing concern — objectively verifiable and forming the evidential basis of the risk.
- **DEPARTURE**: A possible future change from the baseline plan, made credible or more likely by the CONDITION; the source of uncertainty in the risk.
- **ASSET**: The primary element of the organisational unit portfolio affected by the risk; enables assignment of ownership.
- **CONSEQUENCE**: The foreseeable negative impact on the ability to meet performance requirements — written without regard to potential mitigations.
- **Near-Term Criticality**: Ranking of individual risks by urgency — risks for which only a limited window exists for effective response.
- **Strategic Criticality**: Ranking by importance to the aggregate performance risk model — risks where uncertainty in likelihood or severity warrants detailed analysis.
- **Risk Drivers**: Specific uncertain elements (parameters, pivotal events, or departures) that, when set to an optimistic value, cause performance risk to cross a tolerability threshold. Identified through sensitivity analysis of the aggregate risk model.
- **Graded Formulation of Scenarios**: RSDs range from a simple two-pathway diagram (consistent with only the risk statement) to a moderately detailed multi-branch diagram (incorporating additional scenarios); the level is calibrated to the strategic criticality ranking.
- **Defense-in-Depth**: When characterising risk drivers, identify them at all three levels — parameter, pivotal event, and departure — to ensure that the full spectrum of mitigation options is visible.

## Mental Models
- Write the CONSEQUENCE before thinking about mitigations; if mitigation is already baked into the consequence, the risk database understates the actual exposure.
- Apply the eight-question validity test rigorously: a risk that fails "Is the CONDITION factually true?" is speculation, not a risk; a risk that fails "Is it actionable?" belongs in a watch list, not a management action queue.
- Use RSDs to discover scenarios that weren't evident when the risk was first identified — the moderately detailed RSD often reveals additional pathways to unacceptable end states.
- The near-term and strategic criticality lists are independent rankings: a risk can be low strategic criticality but high near-term criticality (window is closing) or vice versa.

## Anti-patterns
- **Combining DEPARTURE and CONSEQUENCE into a single element**: This prevents treating the risk as a scenario and obscures ownership assignment and mitigation targeting.
- **Including proposed mitigations in the CONSEQUENCE**: This understates the baseline risk and makes it impossible to evaluate whether the mitigation is actually necessary.
- **Applying full quantitative analysis uniformly**: Wasting analytical resources on low-strategic-criticality risks starves the analysis of high-criticality risks; the graded approach is essential to resource management.
- **Identifying risk drivers at only the departure level**: Risk drivers can be parameters, pivotal events, or departures; identifying only the departure misses mitigation options that operate earlier in the causal chain.

## Key Takeaways
1. The Condition–Departure–Asset–Consequence structure separates observable fact from uncertain future events from operational impact, making the risk actionable and assignable.
2. The eight-question validity test is the gate between concern and managed risk; all eight questions must be answerable with "yes" for an individual risk to enter the database.
3. RSDs can be developed at multiple levels of detail; the appropriate level is determined by the strategic criticality ranking, not by analytical convenience.
4. Risk drivers are identified through sensitivity analysis: if moving a parameter to its optimistic value causes performance risk to cross a tolerability threshold, that parameter is a driver.
5. Defense-in-depth in characterising risk drivers — parameter, pivotal event, and departure — ensures the planning step has maximum latitude in generating mitigation options.

## Connects To
- **CRM Plan Step (Ch 8 of this pack)**: Receives tactical criticality list for near-term response and risk drivers for strategic response generation.
- **CRM Initialisation (Ch 6 of this pack)**: Provides the risk taxonomies and initial risk list that seed the Identify step.
- **Appendix G (Hypothetical Individual Risks)**: NASA's complete worked example risk statements and RSDs for the planetary science mission.
- **NASA PRA Procedures Guide**: Domain-specific guidance on event sequence diagrams and probabilistic analysis methods used in RSDs.

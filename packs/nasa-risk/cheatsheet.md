# NASA Risk Mgmt Handbook Cheatsheet (Version 2.0)

## When to Use RIDM vs. CRM

- Choice among alternatives with consequence (mission or system design, acquisition strategy, risk-response selection, rebaselining): RIDM.
- Implementation underway and risks must be found, understood, and controlled continuously: CRM.
- CRM Plan step finds no acceptable response, or a mitigation would change derived requirements: hand the decision back to RIDM (Activity-Execution or Activity-Rebaseline mode).

## RIDM: three parts, six steps

Part 1, Identification of Alternatives. Step 1: capture external and upper-level management expectations, decompose fundamental objectives into a hierarchy, and attach performance measures; imposed constraints mark the feasibility floor. Step 2: compile a conservatively broad initial alternative set, then prune with a trade tree or matrix, keeping only alternatives that respect constraints and are not dominated.

Part 2, Analysis of Alternatives. Step 3: set one integrated analytical framework across domains (shared parameters, consistent uncertainty treatment, preserved correlations, configuration control) and choose methods by graded approach, with rigor rising as design definition matures. Step 4: conduct the analysis and develop the Technical Basis for Deliberation: alternatives, methods, distributions, sensitivity studies, credibility assessment per NASA-STD-7009.

Part 3, Risk-Informed Alternative Selection. Step 5: deliberate. Declare risk tolerances, form risk-normalized performance targets at a common percentile, condition them sequentially in a declared measure order, and pare the field to contenders; resolve tolerance-versus-constraint conflicts by culling, relaxing, or renegotiating. Step 6: select, accept the selected alternative's risks explicitly, and document the rationale in a Risk-Informed Selection Report or decision memo.

Three modes: Activity-Planning (full breadth, pre-execution), Activity-Rebaseline (exception condition; re-trades risk against targets inside the selected alternative only), Activity-Execution (runs inside CRM Plan to select risk-response alternatives).

## CRM: five steps plus communicate-and-document

Identify: gather scenarios, opportunities, and leading indicators from the RIDM risk list, taxonomy-facilitated brainstorming, implementation conditions, elevations, and external change; write each as a validated statement (given a fact-based Condition, a possible Departure affecting an Asset, producing a Consequence for stated Objectives) plus a narrative; categorize in the taxonomy to expose cross-cutting entries.

Analyze: build the RSD, then quantify (probabilistic path: event likelihoods, end-state performance for every measure, epistemic uncertainty in a Monte Carlo shell, classification against IRTLs, integration into the risk model, aggregate classification against RTLs, risk drivers by sensitivity) or estimate (heuristic path: history and judgment mapped onto conservative matrices anchored to tolerances); display with spider charts.

Plan: assign one of six dispositions (Accept, Mitigate, Watch, Research, Elevate, Close) per scenario, combine options into response alternatives, analyze residual risk against tolerances, and invoke Activity-Execution RIDM only when the choice is genuinely consequential; rebaseline only on decision-authority approval.

Track: monitor implementation and effectiveness observables for Mitigate, Watch, and Research responses; actual-versus-forecast risk reduction and risk cost for mitigations.

Control: evaluate tracking data, correct within the selected alternative, execute pre-established contingencies, and reinitiate Plan when a response cannot reach its objective.

Communicate and Document: run across all five steps; negotiated protocols in the RMP, standard aids (statements, burn-down profiles, taxonomies, RSDs, tracking charts), a relational risk database holding dispositions, rationales, and evidence.

## Risk Statement Formats

Defined scenario: "Given that [Condition], there is a possibility of [Departure] affecting [Asset], which can result in [Consequence], adversely affecting [Affected Objective(s)]." Note whether the risk is actionable.

Implied scenario: "Given that [Leading Indicator] correlates significantly with U/U risks in this context and that [Condition] has pushed it past its watch value, there is a potential for [Departure] to push it past its respond value, affecting [Affected Objective]."

Validation gate, seven questions: measurable objective impact; coherent condition-to-consequence chain; documented basis; baseline change without adequate contingency; factual condition; credible departure; consequence written without regard to mitigations. Any "no" or "unknown" invalidates the statement.

## The Six Dispositions

- Accept: no action needed now; aggregate risk within tolerances; document assumptions; never combines into alternatives.
- Mitigate: positive action on risk drivers, by departure prevention or consequence reduction; may require rebaselining of derived requirements.
- Watch: monitoring plan over driver observables, with thresholds and contingent deferred decisions.
- Research: plan to reduce epistemic uncertainty blocking robust decisions, on a schedule that feeds the risk model.
- Elevate: transfer the decision upward when no combination of the others works; never an opening move; pair with Watch; propose the alternatives you cannot implement yourself.
- Close: remove from active management when drivers are gone, insignificant, or the event has occurred and become a tracked problem.

## Classification and Tolerance Rules

- Two markers per measure by default: requirement (PMK-R) and goal (PMK-G), each with its tolerance (RTL-R, RTL-G). Green: both satisfied. Yellow: requirement satisfied, goal not. Red: requirement violated.
- Individual tolerances: IRTL equals the aggregate RTL divided by the estimated number of significant contributors (experience: about ten or fewer); re-derive as N evolves.
- Aggregate coloring uses the aggregate tolerances and includes the U/U margin; a scenario can be Red while the aggregate stays Yellow when N is much larger than the scenarios found so far.
- Heuristic matrices are deliberately conservative: one Red path makes the scenario Red; multiple Yellows default to Red absent a defensible cumulative argument; multiple Greens default to Yellow.

## Warning Signs

- Risk statements that embed their own mitigations, or conditions without factual evidence.
- Minimize Risk listed as a standalone objective instead of an attribute of every objective.
- Selection on distribution means while hard constraints exist; constraint-violation probability is the number that matters.
- Execution-stage requirements that quietly diverge from the planning-stage markers the selection compared.
- Cost and schedule reserves consumed by mitigation impacts without rebaselining the reserves: underappreciated risk surfacing.
- Elevate proposed before Mitigate, Watch, and Research combinations were analyzed and shown inadequate.
- Interfacing RMPs written independently, with contradictory elevation or communication criteria.

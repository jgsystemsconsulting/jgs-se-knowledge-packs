# Chapter 34: 6.8 Decision Analysis

## Core Idea
Decision analysis is a structured systems engineering process for identifying, evaluating, and recommending alternatives against defined criteria and selection rules, with rigorous treatment of uncertainty, to support informed decision-making throughout the project lifecycle.

## Frameworks Introduced
- **Decision Analysis Process**: A six-step workflow (6.8.1.2) that structures problem formulation, criteria definition, alternative generation, evaluation, recommendation, and documentation. 
  - When to use: Any major decision affecting system design, architecture, cost, schedule, or technical feasibility
  - **Inputs**: Mission/system context; decision statement; stakeholder perspectives
  - **Activities**: Define decision criteria (primary and secondary factors); identify and screen alternatives; select evaluation methods; evaluate alternatives with uncertainty treatment; assess robustness of rankings; formulate recommendations
  - **Outputs**: Decision matrix; alternative rankings; recommendation with rationale; documented assumptions, uncertainties, sensitivities; lessons learned

- **Trade Studies** (6.8.2.1.2): A formal approach to compare viable options within goals, objectives, and constraints at each system resolution level.
  - When to use: Design alternatives at any lifecycle phase; functional allocation; system architecture definition
  - **Inputs**: Project goals/objectives/constraints; functional requirements; operational concept; available technologies
  - **Activities**: Identify selection rule; define plausible alternatives via trade tree; collect data (analyses, tests, models, simulations, lessons learned); quantify measures of effectiveness, performance, and cost; perform sensitivity and uncertainty analysis; conduct reality check (robustness assessment); iterate if needed
  - **Outputs**: Trade study report; ranked alternatives; recommended option with cost, schedule, technical, and risk impacts; formal team endorsement

- **Cost-Benefit and Cost-Effectiveness Analysis** (6.8.2.1.3): Quantitative comparison of alternatives using net benefits (benefits minus costs) or cost per unit benefit.
  - When to use: When cost is a primary constraint or when efficiency relative to a fixed budget is critical
  - **Methods**: Least-cost analysis (lowest cost for technical feasibility); cost-effectiveness (science data per dollar); weighted cost-effectiveness (multiple outcomes with subjective weights)

- **Analytic Hierarchy Process (AHP)** (6.8.2.2.3): A multi-criteria decision method using pair-wise comparisons and weighted hierarchies to handle subjective and objective evaluation measures.
  - When to use: Complex decisions with conflicting criteria, multiple stakeholders, subjective factors (e.g., software tool selection across NASA centers)
  - **Steps**: Describe alternatives; develop high-level objectives; decompose into hierarchy; assign weights via expert interviews/questionnaires; conduct pair-wise comparisons of alternatives against each criterion; combine results mathematically; iterate until consensus achieved
  - **Caution**: Pair-wise comparison assumes factor independence (often false); best applied to criteria weighting rather than alternative selection

- **Borda Counting** (6.8.2.2.4): A voting-based ranking method where each assessor scores all options with weighted ranks (e.g., 4=first, 3=second, etc.), then sums totals.
  - When to use: When no single criterion should dominate; when close trade-offs favor options that rank consistently across multiple criteria
  - **Advantage**: Captures subject matter expert intuition without requiring pair-wise independence assumptions

- **Decision Trees** (6.8.2.2.2): A graphical representation of decision alternatives, probabilistic branches, and end states with associated outcomes, solved left-to-right.
  - When to use: Moderately complex problems with discrete chance outcomes and multiple decision nodes; often derived from an influence diagram
  - **Outputs**: End-state vectors showing consequences of all decision/chance combinations; alternative ranking via selection rule applied to terminal branch values

- **Influence Diagrams** (6.8.2.2.1): A compact graphical model showing decision nodes, chance nodes, value nodes, and their relationships; does not imply strict sequentiality.
  - When to use: Problem formulation and communication; alternative to decision trees when branch exponential growth is problematic; team analysis where information sharing is incomplete
  - **Converts to**: Decision trees for quantification

- **Multi-Attribute Utility Theory (MAUT)** (6.8.2.2.5): A probabilistic approach to rank alternatives by expected utility, capturing decision-maker risk attitude (risk-averse, risk-neutral, risk-prone).
  - When to use: Significant uncertainties; decision-maker is not risk-neutral; top-level architecture decisions
  - **Foundation**: Utility functions (nonlinear preference mappings) combined across multiple attributes

## Key Concepts
- **Decision Criteria**: Measurable performance, technical, cost, or schedule factors used to evaluate alternatives. Distinguish primary factors (define distinct alternatives) from secondary/tertiary factors (refinements within an alternative). Document rejected options.

- **Operational Definition**: A repeatable, measurable specification of a scale value. Example: "high" = probability ≥67%, "low" ≤33%. Essential for consistent normalization and tool configuration.

- **Normalization**: Converting heterogeneous measurement bases (numbers, dollars, weight, dates) into a common scale (e.g., 1–3–9, qualitative low/medium/high) for comparison and aggregation. Must include explicit operational definitions for all scale values.

- **Uncertainty Treatment**: Evaluation of whether uncertainty in input values or assumptions could alter the ranking of alternatives. If yes, quantify ranges, sensitivities (via Monte Carlo or point-estimate ranges), and assess whether uncertainty reduction is justified.

- **Robustness**: Tentative selection's stability under varying reasonable input values and assumptions. Robust selection holds rank across input ranges; non-robust selections may warrant additional analysis or uncertainty reduction.

- **Selection Rule**: An explicit decision-making formula (e.g., "highest system effectiveness under cost cap X, meeting safety requirements"). Chosen after higher-level guidance; must be consistent with goals/objectives/constraints.

- **Decision Matrix**: A two-dimensional table with alternatives as columns, criteria as rows, completed with evaluation scores. Iteratively populated by team using selected evaluation methods. Also serves as default evaluation method itself.

- **Value Function**: Maps TPM (Technical Performance Measure) range [worst, best] → [0, 1], capturing preference structure without explicit risk attitude modeling. Simpler than utility functions when risk treatment is unnecessary.

- **Technical Performance Measure (TPM)**: A quantified outcome variable (system effectiveness, performance, cost, schedule, reliability, maintainability). Also called "outcome variable" or "decision criteria" in NASA SE context.

## Mental Models
- **Use trade trees (WBS-based, functional trees, or fault trees) when defining plausible alternatives.** Prune unattractive branches as design matures; add detail to merit-worthy branches. In early phases (Pre-Phase A), keep multiple high-level architectures to avoid premature lock-in.

- **Think of decision analysis as concurrent engineering across the full lifecycle.** Perform systems analysis from Pre-Phase A through Phase E (Operations & Sustainment), not serially; early analysis of deployment/operations/disposal prevents costly late-phase redesigns.

- **Use normalization to make heterogeneous criteria comparable.** Without it, adding dollars + pounds + schedule days + probabilities is meaningless. Define operational definitions upfront so the team and tools interpret the scale consistently.

- **Check robustness before accepting the tentative selection.** If the highest-ranked alternative is sensitive to one input or assumption, either improve that input's certainty or present multiple closely-ranked alternatives to the decision-maker with uncertainty assessments.

## Anti-patterns
- **Allowing secondary factors to define distinct alternatives**: Conflates design refinement with architectural choice, bloating the option set and obscuring the primary decision logic.

- **Mismatch between decision complexity and analysis depth**: Applying highly formal methods (MAUT, AHP) to simple binary decisions, or conversely, using simple discussion-based evaluation for high-stakes architecture decisions. Scale the method to the decision's risk and impact.

- **Assuming all factors are independent (AHP pair-wise comparison trap)**: Pair-wise AHP comparisons assume other factors remain fixed; in practice, factors interact. Use pair-wise primarily for criteria weighting; conduct separate holistic evaluation when factor interactions are material.

- **Non-representative testing conditions across alternatives**: Testing alternatives under different environments, durations, or resource conditions introduces bias. Standardize test parameters; if deviation is necessary, document rationale and obtain team endorsement.

- **Selecting the highest-scoring alternative without explanation when lower-ranked options are preferred**: If a lower-ranked option is recommended, either the criteria/weights were incorrectly defined (revisit them) or the scoring method did not properly capture the decision-maker's actual preferences. Recommending outside the matrix without justification signals broken evaluation logic.

- **Ignoring human system integration in evaluation**: Cost and schedule impacts of human roles, training, situational awareness, and workload are often underestimated or omitted. Explicitly include human factors in trade studies and cost-effectiveness analysis.

## Key Takeaways
1. **Document the decision context first**: Mission/system context, problem statement, decision-maker identity, and decision team composition. This framing ensures the chosen criteria and selection rule align with actual strategic priorities, not proxy proxies.

2. **Primary criteria drive alternative definition; secondary criteria refine within alternatives**: Define alternatives by distinct approaches to the primary (architecturally significant) criteria. Secondary and tertiary factors tune within those alternatives. This discipline keeps the option set manageable and the decision logic clear.

3. **Normalization and operational definitions are non-negotiable for consistent evaluation**: When combining different measurement types (cost, reliability, schedule), establish an explicit scale (e.g., numeric, qualitative with quantified thresholds) and define what each value means (e.g., "high reliability" = MTBF >10,000 hrs). Both the team and any decision tool must use the same definitions.

4. **Treat uncertainty as decision-relevant only if it could alter the ranking**: If no plausible input range would change which alternative ranks first, uncertainty reduction may not justify additional analysis. If uncertainty does threaten ranking stability, quantify ranges, compute sensitivities, and assess whether reducing that uncertainty is economically justified.

5. **Robustness check precedes recommendation**: Apply a reality check to the tentative selection: Do goals/objectives/constraints hold? Does the ranking hold across reasonable input ranges (robust)? Are measurement methods discriminating enough? Is dissent documented? Only when robustness is confirmed should the selection advance to the decision-maker.

6. **Trade studies are iterative; reality checks may loop back to goal/option/method redefinition**: If the tentative selection fails robustness checks, do not force-fit it. Instead, consider redefining the selection rule (based on new technical data), adjusting options (changing designs or introducing new alternatives), or improving measures/models (to better predict actual performance). Iteration is normal and reduces downstream redesign cost.

7. **Capture and maintain decision artifacts for lifecycle traceability**: Decision reports (problem statement, criteria, alternatives, evaluation methods, assumptions, uncertainties, recommendation, lessons learned) are part of the project archive and inform later change control. Consistent report formats across projects improve institutional learning and auditability.

## Connects To
- **ISO/IEC/IEEE 15288 (Systems Lifecycle Processes)**: Decision analysis is integral to requirements analysis, design definition, and verification processes throughout the lifecycle. NASA's structured decision process implements and operationalizes 15288's iterative technical management.

- **NASA 17 Common Technical Processes (SE Handbook §4–6)**: Decision analysis appears in Requirements Analysis (6.1), Architectural Design (6.2), Design Definition (6.3), Risk Management (6.4), and other processes. Trade studies in particular are the mechanism by which design at each system resolution level is optimized.

- **NPR 7123.1 (NASA Systems Engineering Processes and Requirements)**: Mandates documented decision analysis for major project milestones and trade studies at each design phase. The decision matrix and trade study report are formal deliverables.

- **Cost-Effectiveness and Life-Cycle Cost Analysis (NASA/SP-2007-3707, related SE guidance)**: Decision analysis incorporates cost as a TPM; cost-benefit and cost-effectiveness methods are extensions of the base decision process.

- **Human Systems Integration (HSI, NASA SE Handbook §2.6 & §7.9)**: Often overlooked in trade studies; decision analysis must explicitly include human workload, training, situational awareness, reliability, and maintainability factors to avoid post-decision surprises.

- **Risk Management (NASA SE Handbook §6.4)**: Risk analysis (probability × consequence) for each alternative feeds into trade study evaluation and supports recommendation robustness assessment.

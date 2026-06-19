# NASA Risk Mgmt Handbook Patterns & Techniques

## Pattern 1: Objectives Hierarchy Construction
**When to use**: At the start of any RIDM process before alternatives can be evaluated; whenever stakeholder expectations are multifaceted, qualitative, or potentially conflicting.
**How**: Decompose the top-level objective through the four mission execution domains (Safety, Technical, Cost, Schedule) into progressively more specific performance objectives. Apply the test of importance at each node. Stop when all leaf-level objectives are quantifiable, operational, non-redundant, and solution-independent.
**Trade-offs**: Deeper hierarchies capture more nuance but increase analytical cost and the risk of redundant objectives. Shallow hierarchies are faster but may miss important stakeholder concerns. Apply the test of importance to prune; check excluded objectives collectively before discarding.

## Pattern 2: Fundamental vs. Means Objectives Check
**When to use**: During objectives hierarchy construction, whenever an objective implies a particular design approach or technology.
**How**: Ask whether the objective states *what* to achieve or *how* to achieve it. If it presupposes a solution (e.g., "Maximise use of solid propellant"), rewrite it as a fundamental objective ("Minimise specific impulse uncertainty") or elevate it to the parent objective it partially captures.
**Trade-offs**: Fundamental objectives produce solution-neutral analyses that permit creative alternatives; but they can be harder to quantify and may require proxy or constructed scales.

## Pattern 3: Risk-Normalised Performance Commitment Development
**When to use**: RIDM Part 3, Step 5 — before deliberation begins; whenever alternatives must be compared on capability at equal probability of success.
**How**: Set risk tolerances for each performance measure (independent of alternatives). Order performance measures from lowest to highest risk tolerance. Sequentially determine the performance commitment value for each alternative at its risk tolerance, conditioning on prior commitments being met. Document the ordering rationale.
**Trade-offs**: Sequential conditioning means the order matters when performance measures are correlated. Ordering heuristic (lowest risk tolerance first) minimises unwanted conditioning effects. Sensitivity excursions over a range of risk tolerances reveal whether the preferred alternative is robust to tolerance choices.

## Pattern 4: Graded Analysis Calibration
**When to use**: Whenever deciding how much analytical effort to invest in a given risk issue, either in RIDM or CRM Analyze.
**How**: Classify the issue by stakes and complexity. Apply bounding analysis first; if it shows performance is clearly within or outside acceptable bounds regardless of uncertainties, stop. If the decision is sensitive to uncertain parameters, increase model rigor iteratively until the decision is robust.
**Trade-offs**: Under-grading wastes analytical resources; over-grading produces false precision and misses issues. The grading decision itself requires judgment about which issues are discriminators.

## Pattern 5: Risk Scenario Diagram (RSD) Development
**When to use**: CRM Graded Approach Analyze step, for individual risks with non-trivial strategic criticality; the level of RSD detail is calibrated to the strategic criticality ranking.
**How**: Start from the individual risk's departure event as the initiating condition. Identify pivotal events along each pathway. For each end state, record the associated performance requirements that are affected. Begin with a simple two-pathway diagram consistent with the risk statement; expand to include additional scenarios (e.g., atmospheric density lower, not just higher) if strategic criticality warrants.
**Trade-offs**: Simple RSDs are fast but may miss critical pathways; moderately detailed RSDs reveal additional end states (e.g., loss of mission pathways that do not involve contamination) that change the risk driver characterisation. Full expansion is expensive and should be reserved for high-criticality risks.

## Pattern 6: Risk Driver Identification via Sensitivity Analysis
**When to use**: After the performance risk models are built in CRM Analyze; to prioritise which uncertainties to address in the Plan step.
**How**: For each performance parameter, pivotal event probability, or departure probability, replace its value with an optimistic estimate while holding all others constant. If the performance risk crosses a tolerability threshold, designate that element as a risk driver. If no individual element is a driver, try combinations of the top-two most influential elements.
**Trade-offs**: Single-element sensitivity is fast but may miss interaction effects. Combination analysis is more thorough but combinatorially expensive. NASA recommends iterating from individual to pairwise to higher-order combinations only as needed.

## Pattern 7: Tactical vs. Strategic Planning Pathway Selection
**When to use**: Every time an individual risk reaches the Plan step with a non-Accept disposition.
**How**: Check the near-term criticality ranking from the Quick Look Analyze step. If the window for effective response is short, initiate tactical planning using point estimates and engineering judgment while detailed analysis proceeds in parallel. If no urgency, proceed to strategic planning using the full risk driver characterisation from graded analysis.
**Trade-offs**: Tactical planning sacrifices analytical rigour for timeliness; the risk analysis of the selected tactical alternative must subsequently be revised in the next detailed Analyze cycle to bring the risk model back to standard. Never skip strategic planning — even tactically resolved risks must eventually be integrated into the aggregate model.

## Pattern 8: Risk Response Option Generation from Risk Drivers
**When to use**: CRM Plan step, after risk drivers have been identified from the Graded Approach Analyze step.
**How**: For each risk driver, brainstorm candidate options for each applicable disposition type (Mitigate, Watch, Research). Characterise potential new risks introduced by each option. Share options via the Risk Response Plan across affected organisational units. Prune options that are infeasible or categorically inferior. Then combine surviving options into risk response alternatives using the Risk Response Matrix.
**Trade-offs**: Broad brainstorming catches options that narrow analysis would miss; but generating too many options before pruning wastes effort. Simple engineering analysis at the option-generation stage (not full risk analysis) is appropriate for initial pruning.

## Pattern 9: Six-Disposition Coverage at Every Decision Point
**When to use**: Every strategic Plan cycle for every performance risk and every identified individual risk.
**How**: Explicitly assign one or more dispositions from {Accept, Mitigate, Watch, Research, Elevate, Close} to every active individual risk. Accept must be documented with assumptions. Close should be applied at the start of each strategic cycle to prune irrelevant risks. Elevate should only be proposed after demonstrating no feasible combination of the other options exists.
**Trade-offs**: Covering all six dispositions comprehensively takes time; but implicit dispositions (tacit acceptance, forgotten risks) create unacknowledged exposure that accumulates invisibly in the aggregate performance risk.

## Pattern 10: Burn-Down Schedule as Risk Budget
**When to use**: CRM initialisation and throughout the project life cycle; whenever risk tolerance targets must be set across multiple milestones.
**How**: Establish initial performance risk levels corresponding to RIDM performance commitments (adjusted for any difference between commitments and baselined requirements). Define Tolerable, Marginal, and Intolerable zones for each performance requirement at each milestone. Update the schedule as mitigations change the expected trajectory.
**Trade-offs**: Burn-down profiles that are too aggressive create false alarms; profiles that are too lenient mask emerging problems. The profile should reflect the actual project plan's success path, not a theoretical optimum.

## Pattern 11: Rebaselining Trigger Evaluation
**When to use**: Whenever CRM produces a risk that cannot be managed to tolerable levels within current requirements, or when a selected mitigation modifies derived requirements at lower levels.
**How**: Confirm that no feasible combination of Mitigate, Watch, Research, and Elevate options can return performance risk to tolerable (or at least marginal) levels within current requirements. Then determine the minimum scope of RIDM re-invocation needed — typically Part 1 and Part 2, focused narrowly on the affected requirements. Exclude sunk-cost bias: previously discounted alternatives that are now attractive must be considered.
**Trade-offs**: Re-invoking RIDM adds cost and schedule; but continuing with unmanageable requirements under the fiction of CRM produces worse outcomes. Narrow scope limits cost; avoiding sunk-cost bias preserves analytical integrity.

## Pattern 12: Cross-Cutting Risk Driver Response Planning
**When to use**: When a risk driver appears in multiple individual risks or affects multiple organisational units.
**How**: Share the Risk Driver List and Risk Response Plan across all affected units. Look for options that simultaneously address the driver across multiple units — a single mitigation (e.g., incorporating an atmospheric probe) may resolve risk drivers for spacecraft, RCS, and contamination individual risks simultaneously. Coordinate analysis of such options using a unified risk model update.
**Trade-offs**: Cross-cutting responses are more efficient than isolated unit responses but require coordination overhead. The Risk Response Plan sharing mechanism and unified risk model are prerequisites; without them, cross-cutting opportunities are invisible.

## Pattern 13: TBfD and RISR Structural Completeness Check
**When to use**: Before finalising either document for deliberation or requirements baselining.
**How**: Use Appendix C (TBfD) and Appendix D (RISR) content guides as checklists. Confirm all mandatory sections are present: for TBfD — Technical Summary, Top-Level Requirements, Performance Measures derivation, Decision Alternatives, Risk Analysis Framework, Risk Analysis Results, Credibility Assessment. For RISR — Executive Summary, TBfD content, Performance Commitments, Deliberation record, Alternative Selection with robustness assessment.
**Trade-offs**: Checking against the template is fast and catches structural gaps before review; but it does not guarantee content quality within sections. Structural completeness is necessary but not sufficient.

## Pattern 14: Defence-in-Depth Risk Driver Characterisation
**When to use**: When a risk driver has been identified and planning for mitigation options is beginning.
**How**: Characterise the driver at all three levels simultaneously — the parameter that drives the pivotal event probability; the pivotal event whose probability drives the departure probability; and the departure that drives performance risk. This multi-level characterisation ensures that mitigation options are considered at every layer of the causal chain, not only at the departure level.
**Trade-offs**: Full three-level characterisation takes more time upfront but produces a richer set of mitigation options; departure-only characterisation is faster but typically yields only consequence-reduction options, missing departure-prevention opportunities.

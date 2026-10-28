# NASA Risk Mgmt Handbook Patterns & Techniques (Version 2.0)

Risk-leadership and graded-approach moves the handbook states, as reusable patterns. Each names where the pack develops it.

## Pattern 1: Risk Leadership Cycle
**When to use**: Setting up any activity or auditing whether declared posture matches actual decisions (ch02).
**How**: Five moves in order: state objectives, values, and priorities; declare the risk posture; translate posture directives into per-objective tolerance criteria with iteration between levels; empower decision makers inside assigned limits while monitoring for consistency; keep vertical and horizontal risk communication flowing with prioritization protocols.
**Trade-offs**: Monitoring is for consistency, not second-guessing; over-monitoring recreates the process burden leadership is supposed to remove.

## Pattern 2: Posture-as-Tolerances Translation
**When to use**: Whenever leadership states tolerance qualitatively ("very low" public safety risk) and analysis needs numbers (ch03, ch07).
**How**: Convert each qualitative posture statement into a Risk Tolerance Level per performance marker by iteration with the decision maker; there is no prescriptive mapping, so converge by trial and feedback. Example calibration from the worked example: medium 10 percent, low 6 percent, very low 3 percent, though any defensible pairing works if agreed.
**Trade-offs**: Numbers anchor decisions and displays; but premature quantification of soft postures invites false precision. Iterate before freezing.

## Pattern 3: Qualitative versus Quantitative Decision Rule
**When to use**: Choosing an analysis style under time, resource, or data limits (ch02, ch05).
**How**: The real qualitative-versus-quantitative distinction is objectivity, not precision: unanchored qualitative scales inherit assessor bias, while quantitative scales with stated uncertainty ranges stay context-independent. Pick the least rigorous style whose output resolution can discriminate the alternatives actually being decided; raise rigor only where the decision is sensitive.
**Trade-offs**: Heuristic results carry deliberate conservatism and may disagree with probabilistic results on the same risk; treat the disagreement as data about data quality.

## Pattern 4: Aggregate-First Risk Accounting
**When to use**: Replacing item-by-item risk lists with objective-anchored assessment (ch01, ch02, ch03).
**How**: Model risk per objective as a shortfall distribution; decompose into individual risk scenarios as triplets; re-aggregate with the correct combination logic (uncorrelated, mutually exclusive, or cumulative); classify the aggregate against its RTL before judging any single scenario.
**Trade-offs**: Scenario sets are analyst-constructed envelopes, not ground truth; two defensible decompositions of the same aggregate can differ.

## Pattern 5: U/U Margin from Leading Indicators
**When to use**: Every tolerance comparison, because identified scenarios are systematically non-conservative (ch03, ch04, ch07).
**How**: Estimate the historical ratio of observed to predicted performance for similar activities, adjust for current leading-indicator readings (complexity, novelty, schedule pressure, quality-practice adherence, AI-specific signals such as training-data quality), and apply the resulting margin to the known-risk distribution before classification. Use implied risk scenarios where event chains are unknown but the correlation is established.
**Trade-offs**: Indicator correlations carry scatter; apply them honestly and without optimism bias, which the handbook flags as a chronic program failure mode.

## Pattern 6: Risk Normalization for Alternative Comparison
**When to use**: RIDM deliberation whenever alternatives must be compared on capability at equal risk (ch04).
**How**: Set one tolerance percentile per measure, identical across alternatives; read each alternative's target at that percentile; condition targets sequentially in a declared measure order (low-tolerance measures first) to respect correlations; compare targets, not means.
**Trade-offs**: Sequential conditioning makes order matter when measures correlate; the low-to-high ordering heuristic minimizes distortion. Sensitivity excursions across a tolerance range test whether the ranking survives posture changes.

## Pattern 7: Graded Rigor by Activity Class
**When to use**: Tailoring any RIDM or CRM execution to criticality and resources (ch04, ch05).
**How**: Assign an activity class (A+ with crewed, down to D), then grade each step: A+ fully quantitative, several SMEs per dimension, iterative deliberation, report-format documentation; D mission-essential objectives only, semi-qualitative expert judgment, minimal alternatives and targets, memo-format records. Class tailoring superimposes on mode-based scoping (planning, rebaseline, execution).
**Trade-offs**: Under-grading gambles mission success; over-grading reads as process burden and gets bypassed. The class assignment is the audit trail for the grading decision.

## Pattern 8: One Integrated Risk Model, Continuously Refined
**When to use**: CRM initialization and every Analyze cycle thereafter (ch05).
**How**: Inherit the RIDM risk model, complete it for non-discriminator measures, absorb each new scenario into the same linked model, preserve parameter correlations, recharacterize the U/U margin per the current knowledge state, and re-derive risk drivers by sensitivity analysis as the model changes.
**Trade-offs**: Batch-updating watched parameters keeps the model tractable; per-scenario isolation analysis is faster but hides cumulative and competing effects.

## Pattern 9: Conservative Heuristic Matrices
**When to use**: When probabilistic analysis is impractical but classification is still needed (ch05, ch07).
**How**: Map RSD pathways onto matrices whose bins are anchored to the tolerance levels and whose coloring is deliberately conservative: any red path makes the scenario red; multiple yellow paths default to red absent a defensible cumulative argument; multiple green paths default to yellow. Use one matrix per threatened objective.
**Trade-offs**: Conservatism counters underestimation but can produce red classifications where a probabilistic analysis would say yellow; document the technical basis and preserve it.

## Pattern 10: Gate-Crossing Information Discipline
**When to use**: Life-cycle transitions, staff handovers, and reviews (ch02, ch06).
**How**: Approve LCR success criteria and their evidence specifications before the phase runs; at the gate, check evidence against specification, claims against independent reading, and deficiencies against posture adherence. Transmit the pre-execution RIDM risk profile formally to the execution organization across the gate.
**Trade-offs**: Pre-specified evidence prevents backfitting but constrains flexibility; evaluators should still expect deficiencies and judge their materiality rather than demand perfection.

## Pattern 11: Cross-Cutting Routing Rule
**When to use**: Any risk originating outside the unit or threatening objectives outside it (ch06).
**How**: Apply the two recognition tests; route officially through the higher-level determination; then classify handling as Type A (coordinated multi-unit handling under a named coordinator with elevation criteria) or Type B (single capable owner with notification-and-update duty to affected units). Write the routing into CORCPs and CORHPs in mutually compatible RMPs.
**Trade-offs**: Type A coordination costs overhead; mislabeling a Type A risk as Type B leaves it unmanaged while every unit assumes another owns it.

## Pattern 12: Response Selection with Visibility to the Top
**When to use**: CRM Plan step whenever no all-green response alternative exists (ch05, ch07).
**How**: Compare alternatives on a spider chart across affected measures; treat a dominated alternative as droppable but keep non-dominated contenders even when all are flawed; if none is acceptable within existing markers, the honest moves are elevation (with the alternatives you cannot implement proposed upward) or rebaselining on decision-authority approval.
**Trade-offs**: Narrow fixes preserve budget today but strand long-term objectives, forcing later spawned risks; elevation and rebaseline cost authority capital now and close the gap properly.

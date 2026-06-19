# NASA Risk Mgmt Handbook Cheatsheet

## When to Use RIDM vs. CRM

| Situation | Process |
|---|---|
| Trade study, architecture decision, make-buy, source selection, budget reallocation | RIDM |
| Requirements-setting or rebaselining | RIDM |
| Decision involves high stakes, complexity, uncertainty, multiple attributes, or diverse stakeholders | RIDM |
| Implementation underway; managing to baselined performance requirements | CRM |
| Technology development with defined cost/schedule constraints | CRM |
| CRM identifies unmanageable risk or mitigation modifies derived requirements | Re-invoke RIDM |

## RIDM Six-Step Quick Reference

| Step | Key Output | Pitfall |
|---|---|---|
| 1. Understand stakeholder expectations | Objectives hierarchy + performance measures + imposed constraints | Using means objectives instead of fundamental objectives |
| 2. Compile feasible alternatives | Trade tree, pruned to feasible set | Pruning by intuition before analysis |
| 3. Set framework and analysis methodologies | Risk analysis framework, configuration-controlled per alternative | Siloed domain analyses without cross-domain coordination |
| 4. Conduct risk analysis | TBfD (performance measure pdfs, sensitivity studies) | Uniform model rigor regardless of stakes |
| 5. Develop risk-normalised performance commitments | Performance commitment chart with risk tolerances | Setting risk tolerances after seeing results |
| 6. Deliberate, select, document | RISR | Basing selection solely on risk analysis results |

## CRM Six-Step Quick Reference

| Step | Key Output | Trigger for Next Action |
|---|---|---|
| Identify | Individual risk statements (Condition–Departure–Asset–Consequence), validated by 8 questions | Near-term or strategic criticality flagged |
| Analyze (Quick Look) | Near-term and strategic criticality rankings | Near-term: initiate tactical Plan; Strategic: proceed to Graded |
| Analyze (Graded) | Risk drivers (parameter + pivotal event + departure level) | Intolerable or marginal performance risk |
| Plan | Selected risk response alternative, documented in RRP | Implementation begins; tracking requirements defined |
| Track | Tracking data (implementation status + effectiveness observables) | Deviation from forecasted risk reduction |
| Control | Updated risk model; corrective actions within alternative scope | Gap unresolvable → re-invoke Plan |

## Individual Risk Statement Template

```
Given that [CONDITION: current, fact-based situation],
there is a possibility of [DEPARTURE: future change from baseline]
adversely impacting [ASSET: affected portfolio element],
thereby leading to [CONSEQUENCE: inability to meet performance requirement].
```

**Eight Validity Questions (all must be YES):**
1. Adequately communicates Condition → Departure → Asset → Consequence?
2. Based on documentation or knowledge?
3. Involves change from baseline without adequate contingency?
4. Condition factually true and supported by evidence?
5. Departure credible (possible)?
6. Impacts a measurable performance requirement?
7. Consequence written without regard to mitigations?
8. Actionable (can something be done)?

## Six Risk Disposition Types

| Disposition | Applies To | Key Rule |
|---|---|---|
| Accept | Entire performance risk posture | Document assumptions; not passive — revisit as conditions change |
| Mitigate | Risk drivers | Departure prevention OR consequence reduction; may trigger rebaselining |
| Watch | Risk drivers | Monitoring plan with pre-established criteria; no baseline change |
| Research | Risk drivers | Reduces epistemic uncertainty; includes research schedule |
| Elevate | Risk management decision | Last resort after exhausting other options; combine with Watch |
| Close | Individual risks | Drivers no longer exist or insignificant; bookkeeping, not risk reduction |

## Performance Commitment Ordering Heuristics
- Order performance measures from **lowest to highest risk tolerance** to minimise conditioning effects.
- **Positively correlated** measures (directions of goodness aligned): lagging commitments will be set at higher performance than marginal pdfs suggest.
- **Negatively correlated** measures: lagging commitments will be set at lower performance.
- Run sensitivity excursions across reasonable risk tolerance ranges to test decision robustness.

## Graded Analysis Decision Rules

| Condition | Action |
|---|---|
| Bounding analysis clearly resolves the decision | Stop; no detailed analysis needed |
| Initiating event probability is vanishingly small | Do not model all downstream scenarios |
| Strategic criticality is low | Use point estimates; simple/two-pathway RSD |
| Strategic criticality is high | Full probabilistic analysis; moderately detailed RSD; derive parameter uncertainty distributions |
| No individual risk driver found | Try pairwise combinations; then higher-order if needed |

## Tells & Smells (Warning Signs)

- **Using imposed constraints as performance measures**: Constraints set feasibility bounds; they are not the same as optimisation objectives — mixing them produces incoherent commitment values.
- **Risk statements that include mitigations in the consequence**: Understates exposure; the whole point of the Plan step is to decide whether mitigation is needed.
- **Elevating before trying other options**: Elevation transfers the problem without solving it; it should come after a documented demonstration that no feasible combination of other dispositions works.
- **Burn-down schedule that never triggers yellow or red**: If performance risk never exceeds Tolerable, the tolerability thresholds may be set too conservatively, providing false assurance.
- **TBfD produced after deliberation begins**: The TBfD is the input to deliberation, not a record of it; producing it after the fact turns risk-informed decision making into risk-rationalised decision making.
- **RISR missing robustness assessment**: Without a documented assessment of decision robustness, there is no basis for confidence that the selected alternative will remain the right choice as conditions evolve.
- **Risk taxonomies never updated**: Accumulation of risks in "Other" nodes signals that the taxonomy no longer covers the actual risk landscape; update the structure, not just the items.
- **Assuming parameter-based RIDM models are sufficient for CRM**: Parameter-based models (mass rollup, cost analogy) do not capture project-specific scenarios; CRM requires scenario-based modelling to identify targeted mitigations.

# Chapter 4: RIDM Part 2 — Risk Analysis of Alternatives

## Core Idea
Part 2 constructs a multidisciplinary, probabilistic risk analysis framework for each alternative and produces the Technical Basis for Deliberation (TBfD) — the primary document for risk-informing the subsequent selection process.

## Frameworks Introduced
- **Risk Analysis Framework**: An alternative-specific network tracing performance parameters through domain-specific models to quantify probability distributions (pdfs) for all performance measures.
  - When to use: Step 3 — before conducting analysis; establishes data pathways, responsible organisations, and configuration control.
- **Technical Basis for Deliberation (TBfD)**: The document that consolidates scenario descriptions, performance measure pdfs, imposed-constraint risks, and sensitivity studies for all alternatives.
  - When to use: Produced at the end of Step 4; input to deliberation and selection in Part 3.
- **Graded Approach to Analysis**: Calibrating model rigor to the decision stakes and life-cycle phase — rough-order-of-magnitude (ROM) early, detailed simulation later.
  - When to use: Throughout Part 2; analysis rigor increases as alternatives are downselected and the decision narrows.

## Key Concepts
- **Performance Parameter**: Any value needed to execute models that quantify performance measures. Unlike performance measures (common to all alternatives), performance parameters are alternative-specific. Uncertainties in parameters propagate to create performance measure uncertainty.
- **Model Rigor vs. Graded Analysis**: Model rigor is the level of detail in a model (proportional to design maturity). Graded analysis is completeness — the effort devoted to a given risk issue is proportional to its importance to the decision. These are orthogonal calibrations.
- **Aleatory vs. Epistemic Uncertainty**: Aleatory uncertainty is irreducible stochastic variability. Epistemic uncertainty arises from lack of knowledge and can in principle be reduced by research.
- **Sensitivity Study**: Analysis of how variation in model outputs can be apportioned to variation in model inputs — used to identify which uncertainties most affect the ability to discriminate between alternatives.
- **Configuration Control**: All involved organisations must work from a common, version-controlled definition of each alternative and risk analysis framework; especially critical during rapid design evolution and rebaselining.
- **Correlation Preservation**: The risk analysis framework must preserve correlations between performance measures (e.g., mass affects both cost and technical performance) so that alternatives are evaluated in an integrated, not siloed, fashion.
- **Estimating Methodologies**: Analogy (comparison to similar past programmes), Parametric (regression-based cost drivers), Engineering Build Up (bottom-up WBS rollup) for cost; First-Order, Detailed Simulation, Testing, and Operating Experience for technical measures; Similarity, First-Order Parametric, Detailed Logic Modelling, and Statistical Methods for safety.

## Mental Models
- Match estimating methodology to life-cycle phase: analogy and parametric in Pre-Phase A/A; engineering build-up and detailed simulation in Phase B/C/D.
- Use graded analysis to decide which scenarios to model in detail: if a scenario's initiating event has vanishingly small probability, full modelling is unnecessary.
- Conduct sensitivity studies early — they guide where additional rigor is worth the cost by identifying which parameters most drive discriminating power between alternatives.
- All analysis inputs must trace back through the framework to the performance parameters of the analysed alternative — traceability is a design requirement, not a documentation afterthought.

## Anti-patterns
- **Siloed domain analyses without cross-domain coordination**: If the cost model uses a different mass assumption than the lift-capacity model, performance commitments are internally inconsistent.
- **Applying uniform model rigor regardless of stakes**: Spending detailed-simulation effort on a risk issue that does not affect the decision wastes resources; conversely, using ROM estimates where alternatives are indistinguishable wastes decision-maker confidence.
- **Analysing only discriminator performance measures**: Non-discriminator measures still need at least a conservative bounding analysis; CRM will need to manage them during implementation.

## Key Takeaways
1. The TBfD is the central deliverable of Part 2; it documents all analysis results and provides the technical foundation for deliberation.
2. Graded analysis and model rigor are separate calibrations — apply them independently to manage analysis cost while preserving decision quality.
3. Configuration control over alternative definitions and risk analysis frameworks is non-negotiable; inconsistent data invalidates comparisons.
4. Correlations between performance measures must be preserved — treating them as independent produces systematically wrong joint probability estimates.
5. Sensitivity studies are the primary tool for deciding where to invest additional analytical effort; focus rigor where it changes the discriminating power of the comparison.

## Connects To
- **RIDM Part 3 (Ch 5 of this pack)**: Receives TBfD as primary input for deliberation and selection.
- **CRM Analyse Step (Ch 7 of this pack)**: Inherits the risk analysis framework and models from RIDM, extending them to scenario-based modelling during implementation.
- **NPR 8715.3C, NASA Cost Estimating Handbook, NASA PRA Procedures Guide, NASA-STD-7009**: Domain-specific guidance for safety, cost, and M&S analyses referenced in Part 2.

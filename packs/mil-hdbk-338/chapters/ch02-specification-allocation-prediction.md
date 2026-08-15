# Chapter 2: Reliability Specification, Allocation, Modeling, and Prediction

## Core Idea
Section 6 turns theory into program practice: write quantitative reliability requirements, allocate them across the product breakdown, build reliability models, and predict performance with documented methods. A step-by-step loop ties specification, allocation, and prediction together.

## Frameworks Introduced
- **Reliability specification**: Quantitative requirements with environment, mission time, and success criteria.
- **Apportionment/allocation**: Breaking system goals into subsystem targets.
- **Reliability modeling**: Block diagrams and models that mirror architecture.
- **Prediction methods**: Part-count/part-stress style predictions with explicit assumptions.

## Key Concepts
- Quantitative reliability requirements need mission time, environment, and success definition.
- Allocation trees turn system goals into design-owner budgets.
- Reliability block models should match real dependency and redundancy.
- Prediction methods require documented parts data and stress assumptions.
- Predictions are decision aids early; tests later confirm or refute them.
- Refresh models when architecture or parts lists change.

## Mental Models
- A requirement without environment and duty cycle is incomplete.
- Allocation is a design contract; fantasy leaf targets poison the system number.
- Prediction is an early decision aid, not a substitute for later test evidence.

## Anti-patterns
- **Orphan system MTBF**: Top-level number with no allocation tree or model.
- **Method shopping**: Picking the prediction path that yields the nicest number.
- **Static predictions**: Never refreshing the model when architecture changes.

## Key Takeaways
1. Specify reliability quantitatively with mission/environment context.
2. Allocate so every design owner has a measurable budget.
3. Model real redundancy and dependency structure.
4. Document prediction method, parts data, stresses, and uncertainty.
5. Keep spec, allocation, and prediction consistent as design evolves.

## Connects To
- **ch01** for distributions and metrics behind predictions.
- **ch03** for parts/derating inputs.
- **ch08** when predictions must be confirmed by test.

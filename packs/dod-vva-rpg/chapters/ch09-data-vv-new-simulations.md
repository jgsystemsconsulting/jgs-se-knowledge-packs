# Chapter 9: Data V&V for New Simulations

## Core Idea
Simulation credibility collapses when input, intermediate, or reference data are wrong, incomplete, or misapplied; data verification and validation are integral to VV&A for new simulations—not a side database chore.

## Frameworks Introduced
- **Data V&V pairing**: verify data meet specifications/pedigree rules; validate data represent the intended real-world quantities for the use.
- **Data lifecycle in M&S**: collection → transformation → storage → use in calibration/validation/operation → update.
- **Uncertainty and pedigree**: track source, age, assumptions, and processing so Users and Agents can judge fitness.

## Key Concepts
- **Data requirements**: driven by intended use and model formulation (units, resolution, ranges, sampling).
- **Verification checks**: completeness, format, range, consistency, version identity, transformation correctness.
- **Validation of data**: comparison to independent sources or physical expectation for the quantities that matter.
- **Configuration of data**: accredited runs must pin dataset versions alongside software versions.
- **Sensitivity**: identify which data uncertainties dominate output uncertainty for the decision.

## Mental Models
- **Garbage in, accredited garbage out**: accreditation of code cannot launder bad data.
- **Transformations are models**: cleansing and aggregation steps need V&V attention too.
- **Pedigree beats folklore**: “SME said so once” is weaker than documented measurement chains.

## Anti-patterns
- Using calibration data as the sole validation referent without independence.
- Undocumented unit conversions or coordinate transforms.
- Mixing classified/controlled and open data assumptions without labeling impacts.
- Updating production data stores without re-checking validation envelopes.

## Key Takeaways
1. Data V&V is mandatory scaffolding for M&S validation and accreditation.
2. Specify, verify, validate, and configuration-manage data as deliberately as software.
3. Pedigree and uncertainty enable honest residual-risk statements.
4. Sensitivity analysis focuses scarce validation effort on decision-driving data.

## Connects To
- **ch03**: developer data pipelines and CM.
- **ch08**: data as referent and as part of “M&S and associated data.”
- **ch05–ch06**: evidence and package contents.
- **ch10**: data error as operational risk driver.

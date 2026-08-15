# Chapter 3: Verification and Validation of M&S

## Core Idea
The standard requires that M&S be verified and validated, and that the domains of verification and validation be recorded. Verification asks whether the implemented model correctly embodies the conceptual/mathematical intent; validation asks whether the M&S adequately represents the real-world system for intended uses. Domains bound where those claims hold.

## Frameworks Introduced
- **Mandatory verification**: The M&S shall be verified (process plus evidence).
- **Domain of verification**: Recorded envelope (inputs, configurations, phenomena) over which verification claims apply.
- **Mandatory validation**: The M&S shall be validated against referent information appropriate to the claim.
- **Domain of validation**: Recorded envelope of favorable comparison / applicability.
- **Acceptance criteria linkage**: V&V criteria and thresholds defined in programmatics drive pass/fail judgment.
- **Handbook implementation**: Phase activities (concept, design, construction) that generate V&V evidence and products.

## Key Concepts
- **Verification is not validation**: Right model built versus right real-world behavior captured.
- **Domain discipline**: Extrapolation beyond recorded domains is a reporting warning trigger.
- **Referent**: Data or knowledge about the RWS used as the validation comparison basis.
- **Favorable comparison**: Explicit criteria (not vibes) for what counts as validated.
- **Release gate**: Successful testing supports permissible-use statements and guidance.
- **Tailored rigor**: Criticality drives depth; the shalls remain, evidence scales.

## Mental Models
- Domains are fences around credibility claims.
- V&V evidence is cumulative across the model life cycle, not a single test event.
- Validation without a defined referent and criteria is storytelling.
- Verification without configuration control is unreproducible.

## Anti-patterns
- **One happy plot as "validated"**: No domain, no criteria, no referent pedigree.
- **Verifying only nominal path**: Ignores limits and off-nominal behaviors that drive risk.
- **Reusing another project's V&V domains without re-baselining**: Pedigree and assumptions differ.
- **Treating AI/ML components as exempt**: Still M&S under the standard's umbrella when used as such.

## Key Takeaways
1. Verify the implementation against the conceptual/mathematical intent.
2. Validate against referent data with explicit favorable-comparison criteria.
3. Record domains of verification and validation as first-class products.
4. Tie V&V outcomes to pre-declared acceptance criteria.
5. Use handbook phase guidance to plan evidence-producing activities.
6. Let domains constrain later proposed uses.

## Connects To
- **ch02**: Assumptions, math, limits, and capability factors that V&V feed.
- **ch04**: Uncertainty characterization that accompanies V&V.
- **ch05**: Use assessment against permissible uses and domains.
- **ch06**: Warnings when use violates domains or assumptions.
- **nasa-se-handbook**: Broader product verification/validation process context.

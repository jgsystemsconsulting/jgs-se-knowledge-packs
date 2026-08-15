# Chapter 6: FMEA/FMECA, Fault Tree Analysis, and Sneak Circuit Analysis

## Core Idea
Sections 7.8–7.10 present complementary tools: inductive bottom-up FMEA/FMECA, deductive top-down fault trees for critical undesired events, and sneak circuit analysis for latent paths that appear without component failure.

## Frameworks Introduced
- **FMEA / FMECA**: Systematic identification of failure modes, effects, and criticality — inductive, bottoms-up.
- **Fault tree analysis (FTA)**: Logic model of how combinations of events produce a top-level fault.
- **Sneak circuit analysis (SCA)**: Search for unintended circuit paths not caused by part failure.

## Key Concepts
- FMEA/FMECA walks failure modes bottom-up and ranks criticality.
- FTA models how combinations of events create a defined top event.
- Sneak circuit analysis finds latent paths without part failure.
- Analyses should stay living as the design changes.
- Outputs feed testability, FRACAS, and safety coordination.

## Mental Models
- FMEA asks what if this fails; FTA asks how can this bad event happen.
- Criticality scoring focuses scarce mitigation on high-severity modes.
- Sneak paths are latent design defects; redundancy does not automatically remove them.

## Anti-patterns
- **Paper FMEA**: Generic modes copied from templates with no design-specific effects.
- **FTA without action**: Pretty trees that never drive design changes.
- **Skipping SCA on complex switching**: Only analyzing failed parts, not healthy-but-wrong paths.

## Key Takeaways
1. Run FMEA/FMECA on critical functions and feed results to design/test.
2. Use FTA for high-severity top events and common-cause insight.
3. Consider SCA where complex modes/power/switching can create latent paths.
4. Keep analyses living as the design changes.
5. Link outputs to FRACAS/growth (ch08) and testability (ch07).

## Connects To
- **ch04** for fault-tolerant features these analyses must validate.
- **ch07** for design reviews and testability using FMEA outputs.
- **ch08** for FRACAS closing predicted vs actual modes.

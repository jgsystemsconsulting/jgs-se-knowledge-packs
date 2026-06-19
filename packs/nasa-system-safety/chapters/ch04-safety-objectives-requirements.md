# Chapter 4: Setting Safety Objectives and Associated Requirements — The Acquirer's Role

## Core Idea
The Acquirer sets two kinds of requirements: probabilistic performance requirements (derived from safety thresholds, goals, and UU risk margins) and deterministic engineering and process requirements (derived from best practices and lessons learned); both are paired with explicit verification procedures negotiated with the Provider.

## Frameworks Introduced
- **Safety Performance Margin Estimation**: A method for deriving the margin to apply to safety thresholds/goals by studying historical ratios of actual (total) loss probability to modelled (known) loss probability from programs with comparable design maturity and complexity.
  - When to use: When developing new probabilistic safety requirements for a system where full-up operational experience does not yet exist.
- **Key Mission Objectives (KMOs) Sub-case Structure**: Division of multi-objective missions into separate safety sub-cases, each with its own requirements and evidence, while sharing common arguments where differences are captured.
  - When to use: When a mission has distinct phases with meaningfully different safety profiles (e.g., planetary rendezvous events, different flight destinations).
- **Safety Risk Burndown Profile**: A time-varying requirement profile that decreases from initial known-risk requirement (derived from threshold divided by safety performance factor) to mature-system requirement (derived from goal) over the operational life, following an exponential burndown curve.
  - When to use: When setting requirements for a system expected to fly many times, with safety performance expected to improve as UU risks are identified and corrected.

## Key Concepts
- **Safety Performance Factor**: The ratio of total loss probability (known + UU risks) to loss probability from known risks alone; used to derive the probabilistic requirement for known risks from the safety threshold.
- **Safety Threshold**: Maximum tolerable total loss probability at first operation; derived from applicable baselines (e.g., Space Shuttle) adjusted for system differences and feasibility.
- **Safety Goal**: Maximum tolerable total loss probability after system maturity (typically ~100–150 flights for launch vehicles); approximately half the initial known-risk loss probability based on historical experience.
- **Probabilistic Safety Requirement for Known Risks**: Initial requirement = Safety Threshold ÷ Safety Performance Factor; the number against which PRA results are compared.
- **Deterministic Engineering Requirements**: Functional, constraint, verification, and interface requirements that protect assumptions underlying the safety analysis and reflect best practices; sources include GSFC-STD-1000F (GOLD Rules), NASA preferred practices, and the NASA Lessons Learned System.
- **Tailoring of Deterministic Requirements**: Process for excluding requirements not relevant to or not practicable for the specific system; justified when a requirement provides no discernible net safety benefit or imposes disproportionate cost/schedule/performance penalty.
- **System Safety Requirements Analysis (SSRA)**: Acquirer-Provider collaborative analysis identifying, reviewing, and baselineing all applicable safety requirements; analogous to MIL-STD-882E Task 203 (SRHA).
- **Verification Procedures**: Methods (analysis, demonstration, inspection, test) specified for each safety requirement; established initially with expectation of evolution as system knowledge matures.
- **Request for Additional Information (RAI)**: Formal mechanism through which the Acquirer seeks clarification or additional evidence from the Provider during RISC evaluation.

## Mental Models
- Use the ratio method to estimate UU risk contribution: examine historical programs of similar complexity and derive the ratio of total-to-known loss probability; this ratio is the safety performance factor and sets the gap between the threshold and the analytic requirement.
- Use the KMO structure when a single safety case would obscure important differences: create separate claims and evidence for each KMO, allow shared arguments where valid, highlight differences explicitly.
- Use mass margin analogies when explaining safety performance margins to non-safety stakeholders: just as mass margins protect against design growth, safety performance margins protect against UU risk growth.

## Anti-patterns
- **Setting thresholds that cannot be verified**: Probabilistic requirements are only meaningful if paired with explicit, agreed verification procedures; a requirement without a verification method is not verifiable.
- **Blanket levying without tailoring**: Imposing every historical best practice without ASARP tailoring can over-constrain novel systems; the Acquirer must assess relevance and practicability, not just levy by default.
- **Ignoring UU risks in threshold development**: Setting thresholds based only on modelled known risks without safety performance margins fails to account for the historically dominant contribution of UU scenarios to actual loss probability.

## Key Takeaways
1. The safety threshold must reflect total actual loss probability including UU contributions, not just modelled known risks; the safety performance margin bridges the gap.
2. Safety performance factors derived from historical programs (Shuttle, early launch vehicles) provide the empirical basis for margins; factor-of-5 ratios have been observed, implying UU risks can be four times known risks.
3. The initial known-risk requirement and the mature-system requirement define the endpoints of a burndown profile; intermediate requirements follow an exponential decay over approximately 100–150 flights.
4. Deterministic requirements must be tailored, not imposed wholesale; irrelevant or counterproductive requirements erode credibility of the requirement set and can sub-optimise safety.
5. Verification procedures are living documents that must evolve with the system; setting them once and freezing them is inadequate for emergent safety properties.
6. For crewed systems, NASA has established minimum tolerable levels for P(LOC) consistent with ISS transportation requirements; these serve as reference points for new crewed mission requirements.

## Connects To
- **NPR 8705.5A (PRA Procedures)**: Governs the technical conduct of probabilistic risk assessment used to demonstrate compliance with probabilistic safety requirements.
- **NPR 7120.5E (Space Flight Program and Project Management)**: Contains project priority rankings that determine the required level of quantitative analysis.
- **GSFC-STD-1000F (GOLD Rules)**: Primary source for design best practices referenced when levying deterministic engineering requirements.
- **NPR 7120.5E**: Governs the process for reporting requirement tailoring (deviations and waivers).

# Chapter 6: CRM Initialisation and Planning

## Core Idea
CRM is initialised by absorbing the RIDM outputs for the selected alternative, establishing a Risk Management Plan (RMP), setting risk tolerance targets and burn-down schedules for each performance requirement, and developing initial risk taxonomies — creating the operational infrastructure for ongoing risk management.

## Frameworks Introduced
- **Risk Management Plan (RMP)**: The formal document specifying how each CRM step will be executed, risk tolerance criteria, elevation protocols, reporting schedules, and inter-unit coordination provisions.
  - When to use: Prepared in preliminary form before RIDM; finalised at CRM initialisation after performance requirements are established.
- **Risk Burn-Down Schedule**: A project-specific profile defining the tolerable level of performance risk for each performance requirement at each programme milestone, from CRM initialisation through mission operations.
  - When to use: Established in the RMP at CRM initialisation; updated as project conditions evolve.
- **Risk Taxonomy**: Tree-structured classification systems — condition/departure taxonomy, asset taxonomy, and consequence taxonomy — used to categorise individual risks, identify cross-cutting risk patterns, and facilitate coordinated responses.
  - When to use: Developed at CRM initialisation; maintained and updated as new risks are identified throughout the project.

## Key Concepts
- **Initial Risk Tolerance Levels**: The performance risks corresponding to the RIDM performance commitments establish the starting risk tolerance for each performance requirement. These are the levels of risk the decision-maker implicitly accepted during RIDM.
- **Performance Requirement vs. Performance Commitment**: Performance requirements are set by systems engineering after RIDM and may differ from RIDM performance commitments. The initial CRM risk tolerance level is derived by comparing the requirement value against the RIDM performance measure pdf.
- **Risk Burn-Down**: As the project matures and mitigations are implemented, residual performance risk should decrease. The burn-down schedule defines the expected trajectory; deviations trigger plan updates or escalation.
- **Performance Margin**: The distance from the current achieved value of a performance measure to its decision boundary (requirement or a derived contingency threshold). Margin statements and risk statements are mathematically equivalent when y = 0.
- **Tolerability Zones**: Performance risks are characterised as Tolerable, Marginal, or Intolerable relative to the burn-down schedule at each milestone.
- **Risk Tolerance Schedule**: For each performance requirement, the RMP specifies whether risks are assessed quantitatively or qualitatively, and provides the time-varying tolerability thresholds.
- **Model Sharing Protocols**: CRM risk models must integrate upward through the organisational hierarchy (lower levels feed results to higher levels), requiring data-reporting and model-sharing protocols to be established at initialisation.
- **Asset Taxonomy**: Derived from the organisational unit portfolio (analogous to a WBS); links individual risks to the resource or element primarily affected, facilitating ownership assignment.

## Mental Models
- Think of the burn-down schedule as the project's "risk budget" over time: the project starts with an initial allocation of tolerable risk and must continuously reduce that balance as milestones pass.
- Margin targets and risk targets are two views of the same reality; use whichever is more natural to the design teams but document the equivalence explicitly.
- Taxonomies are not static catalogues — they are living tools; if many risks accumulate in "Other" nodes, the taxonomy needs restructuring.
- The RMP is not a checkbox document — it is the agreed contract between all organisational units about how risk information will flow, who has authority to accept or escalate, and what the communication protocols are.

## Anti-patterns
- **Treating RIDM risk tolerances as permanent CRM risk tolerances**: RIDM tolerances defined relative to performance commitments; CRM operates relative to performance requirements, which may be more or less stringent.
- **Deferring taxonomy development until risks accumulate**: Retrospective categorisation is inconsistent and misses cross-cutting patterns that a proactive taxonomy would reveal early.
- **RMP as a one-time document**: The RMP must be updated as conditions change; a stale RMP undermines the elevation and communication protocols the whole organisation relies on.

## Key Takeaways
1. CRM initialisation is not a fresh start — it inherits risk analyses, risk tolerances, and a risk list from RIDM and must explicitly acknowledge any gaps relative to the performance requirements now in force.
2. The burn-down schedule is the primary mechanism for making risk tolerance visible and time-bound; it converts abstract tolerability into a project milestone-specific commitment.
3. Three taxonomies — condition/departure, asset, and consequence — together provide a complete risk classification framework that supports cross-cutting response planning.
4. Performance margin and performance risk are equivalent representations; the RMP may use either, but must document the correspondence to avoid confusion across teams.
5. The RMP is the operational contract for RM within the project; its completeness and currency directly determine whether CRM can function as intended.

## Connects To
- **RIDM Part 3 (Ch 5 of this pack)**: Provides RISR, performance commitments, and initial risk list that initialise CRM.
- **CRM Identify Step (Ch 7 of this pack)**: First operational step after initialisation; inherits the taxonomy framework.
- **Systems Engineering**: Provides performance requirements that CRM manages against; SE process is the source of requirements flowdown.
- **NPR 8000.4A Appendix F (Practical Aspects of RMP)**: Additional guidance on staffing, training, plan updates, and contractor process interaction.

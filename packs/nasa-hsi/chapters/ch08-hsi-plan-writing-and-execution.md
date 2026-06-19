# Chapter 8: HSI Plan Writing and Execution

## Core Idea
Effective HSI execution requires mastery of four interconnected practitioner skills — writing the HSI Plan, developing the ConOps, integrating SME expertise, and generating verifiable requirements — each of which produces tangible products that embed human-centered thinking in the SE baseline.

## Frameworks Introduced
- **HSI Plan (HSIP)**: The systematic management document for applying HSI concepts to optimise total system performance across the life cycle; may be standalone, a SEMP section, or part of project documentation depending on P/P scale. Structure: Introduction / Applicable Documents / HSI Objectives (System Description + HSI Relevance) / HSI Strategy (Summary + Domains) / Requirements, Organisation, Risk / Implementation (Activities, Products, Plan Update).
  - When to use: Initiated in Pre-Phase A; updated at each major life-cycle phase and review.
- **Function Allocation Process (Table 4.4-2)**: A structured method for translating high-level human performance requirements into design constraints, interface definitions, and function assignments. Iteratively applied from Pre-Phase A through Phase B.
  - When to use: Whenever system architecture decisions involve trade-offs between human, hardware, and software assignment of functions; particularly at architecture-level trade studies.
- **HSI Metrics Cascade (MOE → MOP → TPM → KPP)**: A four-level hierarchy for quantifying human-system performance from stakeholder goals down to trackable engineering parameters.
  - When to use: From Pre-Phase A (MOEs), through Phase A (MOPs/TPMs), continuing through Phase E (final TPM values) and reported at Phase F.

## Key Concepts
- **ConOps Development**: The ConOps must include all human interaction types across the mission: nominal operations, emergency, and off-nominal contingency scenarios. Function allocation is typically performed in conjunction with ConOps development. The ConOps is the left side of the SE "V" — every validation activity must trace back to it.
- **Function Allocation (HSI Mapping for Resilience)**: HSI-specific considerations overlay the standard function allocation process: ensure lower-level definitions include human functions; add human performance requirements to performance constraints; define adaptive UI and feedback requirements to optimise workload; evaluate existing components under a range of operating conditions.
- **SME Integration**: The HSI practitioner integrates inputs from multiple domain SMEs, balancing depth of specialised knowledge against programmatic utility. "The HSI practitioner holds the key to leveraging the depth of their knowledge and skills, by methodical integration across multiple HSI domains."
- **HSI Requirements Sources**: Requirements derive from Agency standards (NASA-STD-3001 Vol. 1 and 2 for HSF; MIL-STD-1472D for non-HSF; NASA-STD-5005D for GSE) and from ConOps functional analysis. Each standard statement defines an acceptable risk level; requirements translate these to program-specific verifiable "shall" statements.
- **Key Performance Parameters (KPPs)**: High-visibility metrics derived from overarching program goals; must have defined threshold and objective values. Example: crew time KPP for human space flight with threshold at ≤40% crew work day on maintenance/preparation and objective at ≤35%.
- **Technical Leading Indicators (TLIs)**: Program-level indicators tracked to ensure proper progress; defined and documented per NASA/SP-2014-3705.
- **HSI V&V Approach**: Combines human-centred testing, modelling, and analysis to verify that system meets HSI requirements (SEE 7) and validate that it meets ConOps operational intent (SEE 8). Verification requirements must include HSI-related evaluations; validation focuses on operational optimisation and risk mitigation.
- **Crew Time as KPP**: The most important HSI metric for space systems; represents the scarce resource of human attention and effort. Used both as a trade-study cost-equivalent metric and as a formal KPP with threshold/objective values.
- **Training Domain Integration**: Training plans must be considered during early concept phases, not after design is complete. Usability evaluations generate insights that directly improve training effectiveness and can influence design choices that reduce training burden.

## Mental Models
- Write HSI requirements at the design trade space boundary: "requirements that are very specific and quantitative [because of human constraints] but allow as much design/operations trade space as practical while protecting the human."
- Cascade metrics from customer goals downward: MOE (does the system satisfy stakeholders?) → MOP (how is that measured in engineering terms?) → TPM (what is the tracked margin?) → KPP (what is the program-level threshold/objective?). Do not define TPMs without connecting them to MOEs.
- Integrate SMEs before you need their products: arrange SME participation in ConOps development and requirements definition so their knowledge shapes decisions, not just validates conclusions.

## Anti-patterns
- **Requirements without V&V planning**: Every HSI "shall" statement must have a corresponding verification approach (test, analysis, inspection, or demonstration) planned from the start; V&V planning is part of requirements development, not an activity performed after requirements are baselined.
- **Training plans developed after design is fixed**: The guide explicitly warns against this: "Often training plans are only considered after designs have been completed and are fixed." Early training consideration identifies design decisions that reduce training burden and cost.
- **KPPs without defined threshold and objective values**: A KPP without both values cannot be used to make accept/reject decisions at reviews; ISS crew-time experience shows that conservative threshold values must account for unplanned activities.

## Key Takeaways
1. The HSI Plan structure (six sections) provides the management scaffold for all HSI activities; its lifecycle updates (Pre-Phase A through Phase F) ensure that HSI remains current as the design evolves.
2. ConOps is the anchor for validation — every Phase D validation event must trace to a ConOps scenario; gaps in ConOps coverage become gaps in the V&V closure record.
3. Function allocation is a continuous, iterative process from Pre-Phase A through Phase B; the HSI practitioner's role is to ensure human functions are explicitly defined and that interface requirements for adaptive human-system interaction are captured.
4. The metrics cascade (MOE → MOP → TPM → KPP) provides the quantitative spine for HSI influence in SE; without trackable metrics, HSI reduces to qualitative advocacy.
5. Crew time is the premier HSI KPP for space systems; it translates human integration quality into a program-visible, budget-linked metric.
6. SME integration is the practitioner's most challenging skill: balancing deep specialised inputs (e.g., sensorimotor deconditioning) against design team bandwidth and programmatic trade-off timelines.

## Connects To
- **NASA-STD-3001** (Vol. 1 and 2): Primary basis for HSI requirements in human space flight programs.
- **MIL-STD-1472D**: Human engineering design criteria applied for non-HSF programs and human rating.
- **NASA-STD-5005D**: Human integration standards for Ground Support Equipment.
- **NASA/SP-2007-6105 (SEHB), section 7.8**: MOE/MOP use for technical margin management and risk reduction.
- **NASA/TP-2014-218556 (HIDP)**: Key resource for human-centred design activities and spacecraft human certification.

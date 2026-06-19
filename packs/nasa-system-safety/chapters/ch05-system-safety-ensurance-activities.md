# Chapter 5: Performing System Safety Ensurance Activities — The Provider's Role

## Core Idea
The Provider conducts six categories of system safety ensurance activities — SSMP management, integrated safety analysis, requirements support, design support, program control/SCI management, and opportunity exploitation — all anchored by the ISA and documented in the System Safety Management Plan.

## Frameworks Introduced
- **System Safety Management Plan (SSMP)**: The comprehensive planning document that ties baselined safety requirements to specific safety activities, organisational roles, analysis schedules, and RISC development plans.
  - When to use: At the outset of any program/project with non-trivial safety risk; updated whenever requirements are rebaselined or new safety information emerges.
- **Graded ISA Approach (Project Priority Rankings)**: Three-tier analysis depth framework keyed to mission criticality and life-cycle cost: Priority 1 (human spaceflight / >$1B / strategic) requires full PRA + qualitative analysis; Priority 2 ($250M–$1B) requires qualitative analysis supplemented by PRA where appropriate; Priority 3 (<$250M) requires qualitative analysis only.
  - When to use: When scoping the depth of safety analysis resources at program inception or when assessing the adequacy of a Provider's analysis plan.
- **Modeling and Simulation Credibility Assessment Scale (CAS)**: Eight-factor evaluation framework (model verification, model validation, input pedigree, results uncertainty, results robustness, use history, M&S management, people qualifications) rated 0–4 per NASA-STD-7009.
  - When to use: When assessing the validity of ISA models or evaluating the evidentiary strength of modelling-based claims in a RISC.
- **ASARP Trade Analysis**: Structured comparison of safety performance versus cost/schedule/technical performance for alternative design options, framing ASARP determination as a risk-informed decision.
  - When to use: When evaluating whether to incorporate a safety improvement (e.g., crew escape pod) given its impact across all mission execution domains.

## Key Concepts
- **System Safety Management Plan (SSMP)**: 42-element planning document covering mission scope, safety philosophy, organisational structure, analysis techniques, ISA update procedures, SCI management, RISC development approach, and ASARP implementation; must be coordinated with the Systems Engineering Management Plan and Risk Management Plan.
- **Assurance Deficit**: Any knowledge gap that prohibits perfect confidence in a safety claim; caused by variability or lack of knowledge in data, models, parameter inputs, or interpretation of outputs; scored 1–5 (very low to very high deficit, corresponding to ~95–100% down to 0–35% confidence).
- **Safety Control Structure**: The organisational hierarchy of roles and responsibilities for tracking, evaluating, and managing assurance deficit sources; must be documented in the SSMP.
- **Configuration Control Board (CCB)**: Required mechanism for evaluating changes with adequate time, allowing dissent, and maintaining traceability of changes to hardware/software specifications.
- **ISA Scenario-Based Analysis**: The ISA must comprehensively identify credible accident scenarios including causes, contributing factors, control effectiveness, subsystem interactions, physical responses, and probabilities of adverse consequences.
- **Design Order of Precedence**: The MIL-STD-882E hierarchy (eliminate → reduce → engineer → warn → train/PPE) is presented as a menu of potentially fruitful approaches whose relative impacts must be analysed via ISA, not assumed to hold in fixed priority order.
- **Safety Growth**: Operational analogue of reliability growth — the reduction of system-level loss probability as UU risks are discovered, uncovered, and corrected during the operational phase; historically, ~50% reduction in known-risk loss probability over 100–150 flights.
- **Precursor Analysis**: Process for identifying and evaluating near-miss events and anomalies for their potential risk significance; required as part of the SSMP and ISA update cycle.

## Mental Models
- Use the SSMP as the contractual process handshake with the Acquirer: once the SSRA has baselined requirements, the SSMP specifies how each requirement will be met; together they close the loop between "what" and "how."
- Use assurance deficits as the linking mechanism between the ISA and RISC: ISA results generate base claims; knowledge gaps in those results generate assurance deficits; deficits become risk statements managed under CRM.
- Use the M&S CAS before crediting model-based evidence in a RISC: high-criticality risk scenarios require high scores on all eight CAS factors for both individual models and the integrated model.
- Use the priority ranking to justify analytic scope: Priority 1 missions require PRA; lower-priority missions can use qualitative analysis unless PRA is specifically warranted by high-uncertainty scenarios.

## Anti-patterns
- **Treating configuration control as administrative overhead**: Configuration control failures (Mars Climate Orbiter) have been root causes of mission failures; it must be a substantive part of the SSMP and RISC evidence, not just a process checkbox.
- **Bottom-up SCI identification only**: FMEA-based SCI lists miss management practices, interface assumptions, and organisational factors that the ISA top-down approach surfaces as safety-critical.
- **Applying MIL-STD-882 design order of precedence as absolute priority**: The handbook requires each strategy to be ISA-analysed for its actual impact on the specific system's safety performance, not applied in fixed order.

## Key Takeaways
1. The SSMP is the safety backbone of program/project management; it must be integrated with the SE Management Plan and Risk Management Plan, not stand alone.
2. Assurance deficit management is identical in structure to risk management: deficits are the risks, owners are assigned, tracking occurs under CRM; the RISC and CRM process are explicitly linked.
3. The graded approach is mandatory: Priority 1 missions require PRA; forcing full PRA on all missions is wasteful and is explicitly identified as a misapplication.
4. Emerging safety opportunities (new technology, new designs) must be evaluated within the ASARP framework — both risk and opportunity management should be integrated since new risks and new opportunities co-evolve.
5. The ISA must be kept current throughout the life cycle: updated for design changes, test results, anomalies, and operational experience — a stale ISA cannot support valid claims or risk-informed decisions.
6. Personnel qualifications are supporting evidence in the RISC; the SSMP must identify key personnel qualifications and demonstrate that the safety control structure is adequately staffed.

## Connects To
- **NPR 8705.5A**: Technical PRA procedures governing the quantitative dimension of ISA for Priority 1 missions.
- **NASA-STD-7009 (M&S Standard and Handbook)**: CAS factors govern ISA model credibility assessment.
- **NPR 8000.4A**: Assurance deficit management integrates with Continuous Risk Management; risk statements and risk owners map directly.
- **NPR 8715.3C**: Project priority rankings that determine required analysis depth are defined here.

# Chapter 39: Systems Engineering and Quality Attributes

## Core Idea
Quality attributes—including reliability, availability, maintainability, security, and hardware assurance—are non-functional system characteristics essential to lifecycle cost and operational utility that must be designed, verified, and managed throughout system development and operation.

## Frameworks Introduced

- **RAM (Reliability, Availability, Maintainability) Engineering Lifecycle**: Four-stage process—understanding user requirements and constraints, design for reliability, production for reliability, and monitoring during operation and use—that ensures quality attributes are intrinsic product characteristics from inception.
  - When to use: Essential for any system where operational continuity, cost-of-ownership, or uptime are critical (aerospace, defense, medical devices, power systems).

- **Hardware Assurance Dynamic Risk Profile**: A lifecycle framework that models hardware risks through phases (architecture, design, code, implementation) and manages mitigations across supply chains, vulnerability types, and threat evolution.
  - When to use: Critical systems using COTS microelectronics or complex supply chains where early identification and mitigation-in-depth across hardware, firmware, and software is mandatory.

- **Failure Mode Effects and Criticality Analysis (FMECA)**: A table-driven qualitative method that systematically identifies failure modes, their consequences, and criticality (product of likelihood and consequence severity) to prioritize mitigation efforts.
  - When to use: Design phase trade-off analysis and post-production root-cause investigation of unexpected failure modes.

- **Fault Tree Analysis (FTA)**: A graphical top-down method using AND/OR/NOT/K-of-N gates to decompose system failure modes into combinations of component failures and human errors, enabling "drill-down" to nested dependencies.
  - When to use: Safety-critical systems and systems where single-point-of-failure analysis and failure propagation must be exhaustively documented.

- **Reliability Block Diagram (RBD)**: A directed acyclic graph where paths represent operational component subsets; success-oriented complement to fault trees that models redundancy topologies (series, parallel, k-of-n) hierarchically.
  - When to use: Quantitative availability and redundancy trade-studies; particularly suited to software-intensive systems using architectural diversity.

- **Game Theoretic Analysis**: Mathematical models of conflict and cooperation between adversaries, designers, and manufacturing processes that quantify hardware assurance risks through dynamic attacker-defender interactions and cost-benefit constraints.
  - When to use: Supply-chain security and adversarial hardware validation where human malice or financial motivation must be considered alongside unintentional defects.

## Key Concepts

- **Reliability**: Probability that a product performs its intended function under stated conditions without failure for a given time period; requires precise specification of function, environment, timescale, and failure definition.

- **Maintainability**: Probability that a maintenance action restores service within a stated time under stated conditions; comprises serviceability (preventive inspection/servicing) and repairability (restoration after failure).

- **Availability**: Probability that a repairable system is operational at a point in time under given environmental conditions; depends jointly on reliability (frequency of failures) and maintainability (restoration time).

- **Hardware Assurance**: The discipline of quantifying and improving confidence that hardware weaknesses—both inadvertent and intentional—do not become exploitable vulnerabilities across the component lifecycle, supply chain, and operational phases.

- **Function as Intended and Only as Intended**: A principle that systems must perform specified functions reliably AND lack unspecified/hidden functions that could be exploited by adversaries; validated through specification-driven design, exhaustive testing, and multi-source field data.

- **Failure Mechanism**: The physical, chemical, electrical, or thermal process by which an item fails; failure mode is the observable consequence (e.g., "catastrophic," "intermittent," "silent").

- **Dynamic Risk Profile**: A lifecycle-spanning characterization of evolving hardware risks that accounts for supply chain participants, operational conditions, obsolescence, counterfeit threats, and newly discovered attack surfaces; enables risk-based prioritization of mitigations across hardware, firmware, and software.

- **Mitigation-in-Depth**: The practice of layering multiple independent mitigations across hardware, firmware, and software design and operational controls to reduce risk below acceptable thresholds, acknowledging that no single mitigation fully eliminates attack surfaces.

## Mental Models

- **Think of RAM as an intrinsic lifecycle attribute**, not a test-phase checklist. Reliability must be designed in (redundancy, diversity, quality components), built in (process control, configuration management), and verified operationally (FRACAS data, field analytics). Late-stage testing cannot retrofit poor design.

- **Use fault trees and RBDs as dual perspectives**: Fault trees show "what combinations fail the system" (reactive, safety-focused), while RBDs show "what paths keep the system alive" (proactive, availability-focused). Both are necessary for complete risk visibility.

- **View hardware assurance as a supply-chain governance problem**, not just a component-level test problem. Adversaries exploit design intent (espionage), manufacturing quality (counterfeit parts), and information exposure (supply-chain data breaches). Mitigations must span provenance, multi-source validation, and dynamic risk re-assessment.

## Anti-patterns

- **Treating reliability as a testing problem**: Exhaustive testing detects known modes but cannot prove absence of unintended functionality. Assurance requires specification-driven design, traceability, and multi-stakeholder verification before testing begins.

- **Ignoring censored data in RAM analysis**: Omitting units that have not failed biases reliability estimates upward. Rigorous analysis must account for "survival" data, test duration, and operational context.

- **Single-layer security/hardware mitigations**: A firewall or programmable logic update addresses one attack surface but may expose new ones. Mitigation-in-depth (multiple layers) is essential; each mitigation should be independently evaluated for side effects.

- **Decoupling hardware assurance from software/firmware**: Hardware weaknesses are routinely exploited through software vectors (firmware patches, malware). Assurance programs that treat hardware, firmware, and software as separate risks fail to model realistic threat chains.

## Key Takeaways

1. **Quality attributes are design-time properties**, not retrofit fixes. Define RAM requirements early, allocate them to subsystems, and evaluate trade-offs (cost, performance, power vs. reliability, availability, maintainability) during architecture and design phases.

2. **Probability distributions and models are estimates, not truth.** MTTF/MTBF, exponential and Weibull models, and RBDs are tools for decision-making under uncertainty; they are most precise when grounded in operational data (FRACAS systems, field failure rates) and least reliable when based on "similar systems" assumptions.

3. **Qualitative and quantitative analyses are complementary.** FMECA identifies and ranks failure modes qualitatively; fault trees and RBDs quantify system-level effects probabilistically. Both are necessary: qualitative for breadth and new-mode discovery, quantitative for trade-offs and optimization.

4. **Hardware assurance requires dynamic risk profiling across the component lifecycle.** Identify risks at each phase (architecture, design, manufacturing, field operation, sustainment), apply mitigations in depth, and re-assess continuously as threats and operational conditions evolve.

5. **Multi-source data and expert consensus reduce assurance blind spots.** Combine designer specifications, manufacturing process data, field observations, third-party testing, and expert elicitation. Single-source assurance assessments are inherently incomplete.

6. **Game theory and quantitative methods reduce subjective expert variance** in hardware risk scoring. Dynamic interactions between attackers and defenders, cost-benefit trade-off models, and confidence intervals from SAE AS6171 and MITRE CVE provide more defensible risk rankings than expert opinion alone.

7. **Post-fielding FRACAS and continuous monitoring are not optional.** Systems rarely meet RAM objectives exactly; field operation reveals unexpected failure modes, obsolescence risks, and supply-chain issues that must be tracked, root-caused (FRACAS), and fed back into product refreshes.

## Connects To

- **ISO 15288 (Systems Lifecycle Processes)**: RAM engineering processes (understanding requirements, design for reliability, production, monitoring) align with lifecycle phases and review gates.

- **System Safety and Cybersecurity**: RAM shares common concerns with safety (single points of failure, failure propagation) and cybersecurity (availability of defenses, control-device failures creating bottlenecks). Tradeoffs between access control and system availability must be explicit.

- **Supply Chain Risk Management**: Hardware assurance directly drives supply chain governance—component sourcing, counterfeit detection, manufacturing process audits, and provenance tracking are integral to dynamic risk profiling.

- **Configuration Management and Integration Testing**: Production and deployment quality depend on reproducible processes, configuration traceability, and end-to-end testing; these are prerequisites for meeting RAM objectives.

- **Human Factors Engineering**: Operator and maintainer interactions affect both failure rates (human-induced errors) and restoration times (maintainability). Human-factors analyses are necessary design-time disciplines to minimize these contributions.


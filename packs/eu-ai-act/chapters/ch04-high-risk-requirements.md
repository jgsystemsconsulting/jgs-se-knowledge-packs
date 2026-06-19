# Chapter 4: Requirements for High-Risk AI Systems (Chapter III Section 2, Articles 8-15)

## Core Idea
Section 2 imposes seven substantive requirements on every high-risk AI system: a continuous risk management system, data governance, technical documentation, automatic logging, transparency to deployers, human oversight, and accuracy/robustness/cybersecurity. These must be satisfied before placement on the market or putting into service, and maintained throughout the lifecycle.

## Frameworks Introduced
- **Article 9 — Risk Management System (RMS)**: A continuous, iterative, lifecycle-spanning process comprising four steps: (a) identification and analysis of known and foreseeable risks; (b) estimation and evaluation under intended purpose and foreseeable misuse; (c) evaluation of post-market monitoring data (Art 72); (d) adoption of targeted mitigation measures. Residual risk must be acceptable.
  - When to use: As the spine of all compliance activities for high-risk AI; all other requirements feed into or out of the RMS.
- **Article 10 — Data Governance Framework**: Training, validation, and testing data must meet quality criteria covering design choices, data origin, preparation, bias examination, and gap identification. Special categories of personal data may be used for bias correction only under strict conditions.
  - When to use: When specifying training pipelines, bias audits, and data management procedures for high-risk AI.
- **Article 11 — Technical Documentation**: Documentation must be drawn up before placement and kept up to date; it must enable assessment of compliance by competent authorities and notified bodies. Content is specified in Annex IV. SMEs may use a simplified form.
  - When to use: When building the compliance evidence package for market placement or conformity assessment.
- **Article 12 — Record-keeping/Logging**: High-risk AI systems must technically allow automatic logging of events relevant to risk identification, post-market monitoring, and Art 26(5) monitoring. Biometric identification systems (Annex III point 1(a)) must log start/end times, reference database, matched inputs, and identity of verifiers.
  - When to use: When designing AI system architecture; logging must be built in, not retrofitted.
- **Article 13 — Transparency to Deployers**: Systems must be sufficiently transparent for deployers to interpret outputs appropriately. Must include instructions for use (digital or otherwise) covering: provider identity; capabilities, limitations, accuracy metrics; known foreseeable misuse risks; human oversight measures; computational and hardware requirements; log interpretation guidance.
  - When to use: When preparing documentation packages and deployer-facing materials.
- **Article 14 — Human Oversight**: Systems must be designed to allow effective oversight by natural persons during use. Oversight measures must enable deployers to: understand capabilities and limitations; avoid automation bias; correctly interpret outputs; override or disregard outputs; interrupt the system (stop button). For biometric identification (Annex III 1(a)), a minimum of two persons must separately verify each identification before action is taken.
  - When to use: When designing human-machine interfaces and deployer protocols for high-risk AI systems.
- **Article 15 — Accuracy, Robustness, and Cybersecurity**: Systems must achieve appropriate accuracy, robustness, and cybersecurity throughout their lifecycle. Resilience against errors, faults, and inconsistencies (technical redundancy, fail-safe plans). Systems that continue learning post-deployment must mitigate feedback-loop bias. Cybersecurity measures must address data poisoning, model poisoning, adversarial examples/model evasion, confidentiality attacks, and model flaws.
  - When to use: When specifying technical acceptance criteria and security testing requirements.

## Key Concepts
- **Residual risk** (Art 9(5)) — the risk remaining after all feasible design-level risk reduction has been applied; must be judged acceptable.
- **Feedback loop** (Art 15(4)) — the risk that a continuing-learning system produces biased outputs that then feed back as inputs, amplifying bias over time; must be addressed with mitigation measures.
- **Automation bias** (Art 14(4)(b)) — the tendency to over-rely on AI outputs; human oversight provisions are specifically designed to counteract this.
- **Data governance and management practices** (Art 10(2)) — the systematic processes covering design choices, data collection origin, preparation operations (annotation, cleaning, enrichment), assumptions, availability assessment, bias examination, bias mitigation, and gap identification.
- **Instructions for use** (Art 13(3)) — the structured document deployers receive; it must be in digital format or otherwise and cover at minimum seven categories of information specified in Art 13(3)(a)-(f).
- **Stop button** (Art 14(4)(e)) — the requirement to provide a mechanism allowing system interruption and return to a safe state; a key human oversight design element.

## Mental Models
- **"RMS is the spine, other six requirements are vertebrae"**: Every other Section 2 requirement either feeds into the RMS (data quality informs risk estimation) or is implemented via it (logging enables post-market monitoring feeding back into RMS step (c)).
- **"Build-in not bolt-on"**: Logging (Art 12) and human oversight interfaces (Art 14) must be technically integrated into the AI system; they cannot be added by the deployer after the fact.
- **"Accuracy declared, not implied"**: Art 15(3) requires accuracy levels and metrics to be declared in instructions for use; vague claims of high performance do not satisfy this.

## Anti-patterns
- Treating risk management as a one-time pre-deployment exercise: Art 9(1) explicitly requires a continuous iterative process run throughout the entire lifecycle, with regular systematic review and updating.
- Ignoring the bias correction carve-out conditions: Art 10(5) permits processing special categories of personal data for bias detection only if all six listed conditions are met; satisfying GDPR alone is insufficient.
- Conflating transparency for deployers (Art 13) with transparency for end users/affected persons: Art 13 governs what information providers must give to deployers; Art 14 of this section and Art 26(11) + Art 50 govern disclosure to affected individuals.

## Key Takeaways
1. Seven requirements apply cumulatively; satisfying six of seven does not constitute compliance.
2. Risk management is a lifecycle process with four mandatory steps; post-market data must feed back into the RMS.
3. Data governance covers the entire data pipeline from collection to deletion; bias examination and mitigation are mandatory, not optional.
4. Automatic logging must be technically built into the system; minimum logging requirements differ for Annex III point 1(a) biometric systems.
5. Human oversight requires both provider-embedded and deployer-implementable measures; the "stop button" is a legal requirement.
6. Cybersecurity requirements address AI-specific attack vectors (data/model poisoning, adversarial examples) not just general IT security.
7. SMEs may use simplified technical documentation (Art 11(1)) and simplified conformity forms.

## Connects To
- **Chapter III Section 3 (Art 16-27)**: Providers, deployers, and other parties must implement and maintain these requirements.
- **Chapter III Section 4-5 (Art 28-49)**: Conformity assessment verifies that these requirements have been met.
- **Chapter IX (Art 72)**: Post-market monitoring system collects data that feeds back into the Art 9 RMS.
- **Annex IV**: Specifies the minimum content of technical documentation required by Art 11.

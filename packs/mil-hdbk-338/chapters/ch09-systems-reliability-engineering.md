# Chapter 9: Systems Reliability Engineering

## Core Idea
Section 10 lifts reliability engineering from boxes to systems: effectiveness concepts, system R&M parameters, modeling techniques, and COTS/NDI integration issues. It bridges electronic design guidance and mission-level outcomes.

## Frameworks Introduced
- **System effectiveness**: Broader mission success framing in which R/M/A are major contributors.
- **System R&M parameters**: Mission reliability, operational readiness, availability variants.
- **System modeling techniques**: Methods to combine subsystem behaviors into system predictions.
- **COTS/NDI reality**: Integrating items not designed under the program full reliability regime.

## Key Concepts
- System effectiveness frames mission success beyond box-level MTBF.
- Operational readiness and availability include logistics realities.
- System models must capture interfaces and common-cause structure.
- COTS/NDI items transfer assurance burden to selection and integration.
- System metrics should match the mission measure of success.

## Mental Models
- System reliability is an architecture property, not the average of brochure MTBFs.
- Operational measures include logistics delays inherent availability ignores.
- COTS can help cost/schedule but transfers assurance burden to integration.

## Anti-patterns
- **Subsystem sum fallacy**: Adding MTBFs or ignoring dependency/common cause.
- **Paper readiness**: Claiming readiness without maintenance system performance.
- **COTS without delta assurance**: Assuming commercial use equals military environment.

## Key Takeaways
1. Define system R&M metrics that match mission success measures.
2. Model interfaces, dependency, and maintenance concept explicitly.
3. Treat COTS/NDI as risk items in allocation and assurance.
4. Connect system models to lower-level predictions and FMEA results.
5. Use system measures when framing demonstration/growth success (ch08).

## Connects To
- **ch01–ch02** for metrics and allocation inputs.
- **ch04–ch06** for architectural fault tolerance and analysis.
- Related packs: mil-std-882 (safety), mil-hdbk-61 (configuration baselines).

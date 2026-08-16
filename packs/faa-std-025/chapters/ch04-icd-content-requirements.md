# Chapter 4: ICD Content Requirements

## Core Idea
The ICD is the developer-side deliverable that records design characteristics satisfying the parent IRD, serves as the interface specification during implementation, and freezes the as-built interface. Its outline mirrors the IRD so compliance is reviewable section-by-section.

## Frameworks Introduced
- **IRD-driven ICD**: Design characteristics must show compliance with parent IRD requirement layers; IRD is revised if development surfaces new or changed requirements.
- **Common ICD characteristics**: General, security, functional, physical, and electrical/electronic design characteristic groups.
- **Typed ICD slices**: Analog, discrete, general-service, and web-service characteristic sections parallel the IRD structure.

## Key Concepts
- **Role of the ICD**: Describes design characteristics meeting IRD requirements; acts during implementation; documents as-built form, fit, and function.
- **Control difference**: IRD is an FAA-controlled requirements baseline; ICD is typically a developer deliverable under the acquisition.
- **Orphan ICD rule**: If no parent IRD exists, the ICD must document both requirements (shall) and characteristics (is/are)—discouraged.
- **Interface design characteristics**: General functions, services, options, physical design; protocol-layer features consistent with functional specifications; include design tolerances needed to prove IRD compliance.
- **General characteristics**: Identify subsystems, interface points/cable terminations, and connectivity functions/services (same interconnectivity model as the IRD).
- **Security characteristics**: Document how parent IRD security requirements are realized.
- **Functional design characteristics**: Required in every ICD; vary by interface purpose (analog/discrete/service/web).
- **Physical design characteristics**: For analog/discrete/general-service ICDs, document installed (mated) condition, separated half-views, and only interface-applicable hardware; identify the supplier of each component/part. Tolerances as appropriate.
- **Electrical/electronic characteristics**: When power is shared across the interface, document the same factor list as the IRD (voltage, frequency, current, transients, harmonics, polarity/phases, protection, power factor, and related items) under a single selected FAA-G-2100 revision.

## Mental Models
- **Evidence of compliance**: Each ICD slot is an answer to an IRD shall (or an explicit N/A).
- **Two halves of one connector**: Physical ICDs separate mated and unmated views so each party knows its supplied pieces.
- **Feedback loop**: Implementation discoveries update the IRD first; the ICD should not silently redefine requirements.

## Anti-patterns
- ICD that invents new requirements without revising the IRD.
- Documenting whole-subsystem hardware instead of interface-applicable portions.
- Omitting supplier responsibility on physical parts.
- Encouraging orphan ICDs as the normal path.

## Key Takeaways
1. ICD = implemented design characteristics plus as-built record tied to the IRD.
2. Outline parallelism enables requirements-to-design tracing.
3. Physical ICDs stress mated/half views and part ownership.
4. Power/security/functional slots exist to prove—not replace—IRD shalls.

## Connects To
- **ch03**: Parent IRD content the ICD must satisfy.
- **ch02**: Shared format and N/A/reference patterns.
- **ch05**: Verification of design characteristics.
- **ch06**: ICD approval as a subset of the IRD/revision process.

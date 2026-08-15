# Chapter 2: M&S Development Evidence and Capability

## Core Idea
During development, NASA-STD-7009B requires a controlled body of evidence about the real-world system, data/software used, units and frames, assumptions, mathematics, limits, and permissible uses. That evidence feeds an M&S capability assessment across pedigree, verification, validation, uncertainty, and related factors, plus user guidance for setup and execution.

## Frameworks Introduced
- **RWS characterization and data pedigree**: Relevant real-world characteristics and provenance of data used to represent them.
- **Development configuration baseline**: Data sets and supporting software retained under configuration management.
- **Units and coordinate frames register**: Every quantity and I/O variable has explicit units/frames.
- **Assumptions and abstractions log**: Conceptual and implemented-model assumptions, rationales, and consequences.
- **Structure/math description**: Techniques, equations, behaviors/states, control/data flow.
- **Limits and permissible uses**: Boundary conditions and the uses the finished M&S is allowed to support.
- **M&S capability assessment**: Multi-factor rating retained as a development product.
- **Use guidance package**: Setup, execution, interfaces, and appropriate practices.

## Key Concepts
- **Pedigree**: Trust story for data and inputs — origin, quality, applicability.
- **Permissible use**: End-of-development contract derived from intended use, assumptions, limits, and V&V domains.
- **Capability vs results**: Capability is largely a development-phase property; results credibility is assessed in use.
- **CM of development artifacts**: Not only source code — data and supporting tools matter.
- **Guidance is required product**: Operators should not reverse-engineer safe use.
- **Handbook model concepts**: Pedigree/provenance, models-of-models, and AI-model considerations as modern modeling context.

## Mental Models
- Development produces *evidence packages*, not just executables.
- Permissible use is the bridge from development to operations.
- Capability assessment is a structured self-portrait of how strong the M&S is, factor by factor.
- If it is not recorded, it will not be reportable later.

## Anti-patterns
- **Undocumented unit systems / mixed frames**: Silent corruption of results.
- **Assumptions only in someone's head**: Breaks waiver and warning logic at reporting time.
- **Permissible uses = "whatever the customer wants"**: Must be constrained by V&V domains and limits.
- **Capability score without factor evidence**: Assessment theater.

## Key Takeaways
1. Capture RWS characteristics and data pedigree during development.
2. Retain development data/software and unit/frame definitions under control.
3. Document assumptions, structure/math, and limits with rationales.
4. Freeze permissible uses as a development exit product.
5. Perform and record the multi-factor capability assessment.
6. Ship operator guidance with the M&S release.

## Connects To
- **ch01**: Intended use and acceptance criteria that shape development records.
- **ch03**: Verification requirements and domain of verification.
- **ch04**: Validation and development-phase uncertainty characterization.
- **ch05**: Proposed use checked against permissible use.
- **ch07**: Life-cycle construction phase products in the handbook.

# Chapter 7: Design Reviews, Design for Testability, and System Safety Interface

## Core Idea
Sections 7.11–7.13 close the core design-guidelines cluster: structured design reviews, designing for testability/diagnostics, and linking reliability work to the system safety program. Detectability and review discipline determine whether reliability built earlier is verifiable.

## Frameworks Introduced
- **Design reviews**: Formal technical reviews as reliability control gates.
- **Design for testability (DFT)**: Provisions that make faults detectable, isolable, and verifiable.
- **System safety program interface**: Coordination so reliability analyses and safety hazards stay consistent.

## Key Concepts
- Design reviews are reliability gates when analysis artifacts are entry criteria.
- Testability enables detection and isolation of faults across the life cycle.
- BIT and probe access need isolation goals tied to critical modes.
- Reliability and system safety share failure identification but different accept criteria.
- Late packaging freezes often destroy test access if DFT is deferred.

## Mental Models
- If you cannot test it, you cannot claim it — testability is a reliability property.
- Reviews work when entry criteria include analysis artifacts.
- Safety and reliability share failure identification but optimize different accept criteria.

## Anti-patterns
- **Review theater**: Slides without open action closure.
- **Testability after layout freeze**: No probe/BIT access once packaging is done.
- **Separate safety/reliability silos**: Divergent hazard and FMEA stories.

## Key Takeaways
1. Put reliability evidence on design-review checklists.
2. Design BIT/diagnostic provisions with isolation goals tied to FMEA.
3. Distinguish testability from mere presence of a connector.
4. Coordinate reliability outputs with system safety deliverables.
5. Carry testability needs into demonstration planning (ch08).

## Connects To
- **ch06** for analytical inputs to reviews and DFT.
- **ch08** for tests that rely on observability.
- **ch09** for system-level diagnostic/maintainability parameters.

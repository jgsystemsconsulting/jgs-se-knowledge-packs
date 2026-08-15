# Chapter 6: Diagnostics, Avionics, Electrical, and E3 Criteria

## Core Idea
Sections 10–13 cluster electronics-heavy airworthiness areas: diagnostics systems, avionics (manned and UAS/ground segment), electrical power systems, and electromagnetic environmental effects (E3). Criteria emphasize design integrity, qualification evidence, hazard analysis, and integration test.

## Frameworks Introduced
- **Diagnostics criteria**: Health/diagnostic capability supporting safe operation and maintenance decisions.
- **Avionics criteria**: Airborne (and UAS ground segment) avionics functions essential to airworthiness.
- **Electrical system criteria**: Generation, distribution, and protection supporting continued safe flight and operation.
- **E3 criteria**: Electromagnetic environmental effects compatibility as an airworthiness concern.

## Key Concepts
- Diagnostics support safe operation and maintenance decisions.
- Avionics criteria cover manned aircraft and applicable UAS ground segments.
- Electrical generation and distribution support continued safe operation.
- E3 compatibility is an airworthiness concern, not only a lab checkbox.
- Box-level qualification without integration or aircraft-level E3 is incomplete.

## Mental Models
- Avionics airworthiness includes integration and E3, not only functional lab demos.
- UAS control segments can be inside the airworthiness story when applicability pulls them in.
- Diagnostics quality affects both safety and maintainability outcomes.

## Anti-patterns
- **Box-level qual only**: No system integration or aircraft-level E3 evidence.
- **Ground segment ignored for UAS**: Aircraft cert without control-segment criteria when applicable.
- **Electrical load growth**: Adding loads without revisiting electrical criteria evidence.

## Key Takeaways
1. Plan avionics/electrical/E3 evidence as an integrated set.
2. Include UAS ground segment when applicability pulls it in.
3. Tie diagnostic coverage to safety-critical failure modes.
4. Coordinate with software criteria (ch07) for airborne software.
5. Refresh compliance when antennas, wiring, or power architecture change.

## Connects To
- **ch07** for computer systems/software overlapping avionics.
- **ch04** for guidance/flight-path functions.
- **ch02** for CM of avionics configs.

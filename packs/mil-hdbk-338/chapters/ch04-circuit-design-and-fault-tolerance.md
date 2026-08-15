# Chapter 4: Reliable Circuit Design and Fault-Tolerant Design

## Core Idea
Sections 7.4–7.5 cover robust circuit design and fault tolerance (including redundancy) when single-string design cannot meet the reliability budget. Emphasis is margins, worst-case behavior, and structured redundancy with detection — not bolt-on spares without analysis.

## Frameworks Introduced
- **Reliable circuit design**: Practices that reduce sensitivity to variation, noise, and stress excursions.
- **Fault-tolerant design**: Architectures that continue correct operation or safe degradation after faults.
- **Redundancy patterns**: Active/standby and related structures with detection/switchover considerations.

## Key Concepts
- Robust circuit design manages margins, noise, and worst-case corners.
- Fault tolerance needs detection and isolation paths, not only spare hardware.
- Redundancy multiplies logistics and coverage failure modes.
- Common-cause faults can defeat naive parallel designs.
- Coverage analysis is required before claiming fault-tolerant benefit.

## Mental Models
- Circuit reliability is stress management plus deterministic design discipline.
- Redundancy multiplies logistics and coverage failure modes as well as success paths.
- Fault tolerance needs detection and isolation, not only duplicate hardware.

## Anti-patterns
- **Redundancy as perfume**: Parallel strings without coverage or common-cause control.
- **Worst-case ignored**: Nominal sims treated as proof of reliability.
- **Silent spare path**: No BIT/monitoring on the redundant path.

## Key Takeaways
1. Stabilize circuit stress and margins before adding redundancy.
2. Model coverage and switching when claiming fault tolerance.
3. Watch common-cause faults (power, clock, thermal, software).
4. Tie circuit choices to the allocation budget from ch02.
5. Verify fault-tolerant behavior with analysis and targeted test.

## Connects To
- **ch03** for parts/derating prerequisites.
- **ch06** for FMEA/FTA validating fault-tolerant claims.
- **ch07** for testability enabling detection/switchover.

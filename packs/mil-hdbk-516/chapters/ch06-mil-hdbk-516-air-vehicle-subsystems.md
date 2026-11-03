# Chapter: Air vehicle subsystems criteria

## Core Idea

Section 8 covers primary subsystems common on air vehicles: hydraulic and pneumatic; environmental control; fuel; fire and hazard protection; landing gear and deceleration; auxiliary and emergency power; mechanisms; rotary-wing drive. Rotary-wing additions include external cargo hook, external rescue hoist, and fast-rope insertion and extraction systems (FRIES).

D stands this cluster up as its own section. Criteria still use standard-plus-MoC form. Example pattern: loss of one hydraulic system must not drive flying qualities worse than a stated level or loss of a safety-critical function, verified by examination, analysis, and test as specified.

## Frameworks Introduced

### Subsystem catalogue by function

Treat each subsystem family as a design-attribute set with its own failure modes and MoCs, then integrate at the air-vehicle level for cascading effects.

### Redundancy and safety-critical functions (SCFs)

Many standards bind subsystem failures to flying qualities or SCF retention. Cross-check with flight technology when power or actuation is lost.

### Rotary-wing special subsystems

Cargo hook, rescue hoist, and FRIES have dedicated criteria because external load and personnel operations create unique AW hazards.

## Key Concepts

- **Hydraulic and pneumatic power.** Redundant sources for flight control, gear, and deceleration.
- **Environmental control.** Thermal and environmental conditions for occupants and equipment as they affect AW.
- **Fuel system.** Storage, feed, venting, and hazard control tied to propulsion and fire protection.
- **Fire and hazard protection.** Detection and suppression design attributes.
- **Landing gear and deceleration.** Extension, steering, braking, and energy absorption.
- **APU and emergency power.** Independent or backup power for critical functions.
- **Mechanisms.** Doors, ramps, and related mechanical systems with AW impact.
- **Rotary-wing drive.** Power path unique to rotary-wing air vehicles.

## Mental Models

- **Subsystem loss is a flight-technology problem.** MoCs that stop at the subsystem boundary miss the flying-qualities claim.
- **External load gear is not optional kit.** Hooks, hoists, and FRIES are AW-relevant structure and mechanism.
- **Fuel ties three chapters.** Propulsion, fire protection, and electrical bonding/E3 all touch fuel system design.

## Key Takeaways

- Section 8 is the air vehicle subsystems domain, including rotary-wing special systems.
- Argue redundancy against SCF and flying-qualities outcomes.
- Integrate failures upward to the vehicle, not only inside the subsystem.
- Keep mechanisms and external-load systems in the basis when the design includes them.

## Connects To

- ch04 for flying qualities after subsystem loss
- ch05 for fuel and power interfaces
- ch07 for crew station environmental and egress interfaces
- ch08 for electrical power that drives or is backed up by these systems

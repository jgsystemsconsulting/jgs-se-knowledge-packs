# Chapter — Designing Equipment for Maintenance

## Core Idea

Maintainability is not a property you bolt on after the design is frozen; it is a set of choices about how a piece of equipment is divided, packaged, mounted, fastened, opened, and labeled. HF-STD-001B Section 5.2 treats the maintainer as a user whose performance — speed, accuracy, and safety — is governed by the same human-factors logic that governs an operator at a console. The chapter's argument is that maintenance happens in a context: the surrounding system may need to run continuously, the maintenance concept may call for on-site repair versus remove-and-replace versus discard, the physical environment may impose weather or protective clothing, and the maintainers themselves vary in size, strength, skill, and training. Good equipment design anticipates all four and removes friction before the wrench ever touches a fastener.

The through-line across every subsection is **decomposition into independent, interchangeable, easily replaced modules** with **ready access** to anything that has to be inspected, tested, removed, or replaced — backed by quantified limits (weights, forces, clearances, opening dimensions) so that "easy" and "safe" become verifiable requirements rather than aspirations.

This pack is human-systems-integration material that reaches well beyond the NASA-centric HSI body of knowledge; it complements `nasa-hsi` rather than duplicating it. Where `nasa-hsi` frames maintainability inside the spaceflight HSI domains, HF-STD-001B supplies the ground-systems, FAA-facility, and military-derived design rules — drawn from MIL-STD-1472G, MIL-HDBK-759C, MIL-STD-1800A, AFSC DH 1-3, UCRL-15673, NASA-STD-3000A, and OSHA 29 CFR 1910 — and quantifies them.

## Frameworks Introduced (exact source names, when/how)

The standard does not invent a single named framework; it aggregates and harmonizes design criteria from a defined set of source documents, citing each rule to its origin. The recurring sources in this slice are:

- **MIL-STD-1472G (2012)** — the dominant source for weight/force limits, interchangeability, mounting, access opening dimensions, cover behavior, fasteners, and connectors. Cited whenever a hard numeric or "shall" criterion appears (e.g., the one-person lift table, the 635 mm reach limit, the high-torque fastener-head rule).
- **MIL-HDBK-759C (1995)** — the source for the general design-guidance feature list, fastener type preferences, cover/case handling, and screw guidance.
- **MIL-STD-1800A (1990)** — used for damage prevention, remote handling, lifting eyes/jacking points, and labeling of heavy units.
- **AFSC DH 1-3 (1980)** — Air Force Design Handbook material on use-of-existing-items, modularization benefits, handle needs, and serviceability in installed position.
- **UCRL-15673 (1985)** — a Lawrence Livermore human-engineering source heavily relied on for unitization, labeling/typography, latches, washers, retainer chains, and connectors.
- **NASA-STD-3000A (1989)** — the source for the continuous-operation, redundancy, degraded-mode, and fault-detection rules, and for skill/training balance.
- **OSHA 29 CFR 1910 (.147, .303, .333, .301–308, .331–335, .399)** — invoked for hazardous-energy control: lockout/tagout, interlocks, and electrical-equipment marking.

The chapter introduces an explicit **fastener preference order** (MIL-HDBK-759C): for ease of maintenance, prefer quick fastening/releasing devices, then latches and catches, then captive fasteners, then screws, then nuts and bolts last. It also introduces a **definitional hierarchy** the rest of Section 5.2 depends on.

## Key Concepts

**The equipment decomposition hierarchy.** The standard fixes four terms so requirements can be written against them precisely:
- A **unit of equipment** is an assemblage of items packaged into a single hardware package (a computer, a keyboard, a display, a radio transmitter each count).
- A **module** is two or more interconnected parts or components forming one physical and functional entity — it is the *single functionality* that makes something a module.
- A **component** is a subdivision of a unit that a user can treat as one object but that can be broken down further (a populated mounting board).
- A **part** cannot normally be broken down further without destroying its use (fuses, resistors, capacitors).

**General design guidance (5.2.1.1.1).** A consolidated feature list to fold into all equipment, modules, and components as appropriate: simplify maintenance functions and overall design; modularize; minimize the number and complexity of tasks; use built-in test, diagnostic, and fault-localization capability; use disposable items where cost-effective; give quick easy access to anything needing maintenance; comply with lifting/carrying/force criteria; minimize tool and test-equipment variety; match design to maintainer skill and training; maximize user and equipment safety; ease assembly and removal; eliminate precise torque requirements; allow maintenance from above and outside rather than underneath and inside; and use self-lubrication and sealed-lubricated modules.

**Reuse before redesign (5.2.1.1.2).** If an existing item meets the relevant performance, maintainability, and reliability requirements plus the human-engineering criteria, designers must use it rather than design a new one. "Item" is the umbrella term covering parts, components, modules, and units.

**Designing maintenance into continuous-operation systems (5.2.1.2).** For systems that must run without interruption: equipment must be maintainable without stopping operation; provide redundancy if maintenance would otherwise interrupt it; allow degraded-mode operation while awaiting maintenance when the function's importance warrants it; ensure degraded operation does not damage other equipment or worsen the fault; sense and report degraded states and faults to users (and operators when appropriate); add automatic fault detection and isolation when warranted; keep units as independent as practical functionally, mechanically, electrically, and electronically; and make frequently-failing items (lamps, fuses) easy to replace.

**Safety and hazardous-energy control (5.2.1.2.8–9, 5.2.5.6).** Equipment must not expose maintainers to hazards during procedures, and a *positive means* (disconnects, lockouts) must be designed in per OSHA 29 CFR 1910.147. The standard defines a **hazardous condition** as energy or a substance likely to cause death or injury (force, shock, radiation, explosion, flame, poison, corrosion, oxidation, irritation, biological/chemical effects) and a **hazardous location** as a space where such a condition exists or is exposed. Interlocks disable an internal hazard when a cover/case/shield is opened, but — per OSHA 29 CFR 1910.333 — interlocks are explicitly *not* a substitute for lockout/tagout and must not be the sole means of de-energizing a circuit.

**Quantified handling limits (5.2.2.2).** One of the most reference-heavy parts of the chapter. Single-person two-handed lift limits depend on lift height and the body-to-grip distance (e.g., roughly 20 kg at a 0.9 m lift for the closest grip, dropping as the unit gets larger or the lift goes higher). Obstacle reductions are tiered (about a third, a half, two-thirds for obstacles protruding 300/460/610 mm), reach is capped at 635 mm, and the size-versus-obstacle reductions are not stacked — only the more restrictive applies. Multi-person lifting scales by the formula **X + 0.75(N−1)X**, where X is the single-person limit and N is the number of lifters, assuming people do not interfere with each other. Carrying limits are stricter than lifting: 16 kg for one person, 19 kg per person for two, all over distances up to 10 m. Units over 68 kg need lifting eyes or jacking points; units over 13.6 kg or requiring multiple lifters need weight/crew labels.

**Handles, grasp areas, stands, and alignment aids (5.2.2.5–8).** Carry-intended units need handles or grasp areas; handle need is keyed to weight bands (under 4.5 kg if otherwise hard to grasp; 4.5–18 kg one-person handles; 18–68 kg two-or-more-person handles; lifting eyes above that for very large units). Handles must be comfortable, non-cutting, hard-surfaced against grit, non-conductive, permanently attached, and (if folding) lockable upright with one-handed operation. Handle diameter scales with unit weight, and fingers must be able to curl around the handle. Single handles go above the center of gravity; pairs go on opposite sides on/above a horizontal line through the CG to keep the unit from tipping. Alignment aids (guides, pins, tracks) should make incorrect installation impossible — bottom-mounted pins under 9 kg, side-aligning guides above.

**Packaging, arrangement, and mounting (5.2.3).** **Unitization** — packaging into physically and functionally distinct, easily replaceable units — yields access, standardization, design reuse, and lower skill demands. Interchangeability follows a clean rule: functionally interchangeable units should also be physically interchangeable, and units that are *not* functionally interchangeable must *not* be physically interchangeable, with both clearly identifiable. Frequently-moved or heavy inaccessible units mount in drawers, on sliding racks, or on hinges, with limit stops, automatic locks in operating and maintenance positions, easy one-hand lock release, and support that holds the unit open without the maintainer holding it. Positioning rules give the most accessible spots to the most critical and most-frequently-serviced equipment, keep working level between hip and shoulder (about 1–1.5 m), forbid stacking or blocking, and require that no operable unit be removed to reach a unit needing maintenance.

**Labeling and marking (5.2.3.5).** Distinguishes **labels** (alphanumeric identifying/describing text) from **markings** (nonverbal colors/symbols). Specifies label types (identification, hazard, weight, crew-size, instruction, data), location/orientation (readable in installed position, horizontal text, protected from dirt/moisture), typography (character heights by viewing distance, stroke-width ratios, black-on-light for normal illumination and white-on-dark for dim, case rules), and marking limits (no more than nine color codes, distinguishable by color-deficient viewers).

**Access openings, cases, covers, guards, shields (5.2.4–5.2.5).** Provide an access opening wherever a task would otherwise require removing a case, opening a fitting, or dismantling a unit; prefer one large opening to several small ones; round or coat edges; avoid riveted access panels; use quick-action fasteners except under stress. Opening sizes are tabulated for finger, one-hand/arm, and two-hand access. The standard defines **case**, **cover**, **guard**, and **shield**, and lays out the trade-offs of hinged, sliding, removable doors/caps, and removable panels. A notable rule: the **case is lifted off the equipment, not the equipment lifted out of the case**, and covers must indicate fastened/unfastened state.

**Fasteners and connectors (5.2.6–5.2.7).** Fasteners should be few, simple, hand-operable when possible, self-aligning, distinguishable when different types are mixed, and free of precise-torque demands. Type-specific rules cover nuts/bolts, screws ("straight-in" screwdriver only, deep slots, fewer than ten turns), combination heads, latches/catches, captive fasteners, and quick-action devices. Connectors must be safe to release under pressure/voltage, hand- or common-tool operable, protected from damage, distinctively different across functions, and physically incompatible where mismatching could cause harm.

## Mental Models

- **Maintenance is a use case, the maintainer is a user.** Every operator-facing human-factors principle (reach, force, legibility, error-proofing) applies to maintenance, just with tools and access constraints added.

- **Design for the worst combination of context.** Continuous-operation requirement + protective clothing + outdoor environment + lowest-skill maintainer is the design point, not the nominal case.

- **Module-first thinking.** Break a unit into independent, interchangeable, replaceable modules first; access, fault isolation, handling, and skill reduction all fall out of that single decision.

- **Poka-yoke for installation.** Ideally it is *impossible* to install or connect something wrong; alignment pins, asymmetric covers, physically incompatible connectors, and distinct fasteners make the correct action the only possible action.

- **Quantify "easy" and "safe."** Convert qualitative goals into numbers — weight bands, force tables, reach caps, clearance minimums (e.g., 50 mm handle clearance), opening dimensions, character heights — so requirements are testable.

- **Fasteners ranked by maintenance cost.** Quick-release > latches/catches > captive > screws > nuts-and-bolts; reach for the least time-consuming option that still meets closure and structural needs.

- **Layered safety, never single-point.** Interlocks reduce risk but lockout/tagout is the controlling barrier; hazards get both an engineering control and a label that stays visible whether the cover is open or closed.

## Anti-patterns

The source explicitly names design choices to avoid:

- **Maintenance from underneath and inside.** Equipment should be maintainable from above and outside; access from below/inside is the disfavored arrangement.
- **Precise torque requirements.** Designs should eliminate them; where unavoidable, the torquing tool must apply directly without irregular extensions, and the value/sequence must be labeled.
- **Riveted access panels and doors.** Rivets are permanent, slow to remove, and must not cover access openings or attach hinges, latches, catches, or other quick-release devices; rivets are inappropriate on anything that may need removal.
- **Stacking or blocking units.** Units must not be stacked or placed in front of or behind one another, and no unit should require removing another to reach it.
- **Physical access without visual access.** Working blind inside an opening is disallowed without acquisition-program-office approval.
- **Offset screwdrivers / non-straight-in screws.** Screws are only acceptable where a straight-in screwdriver orientation works; offset screwdrivers must not be required.
- **Non-combination straight-slot or cross-recess internal fasteners.** Disallowed except for fastening wood.
- **Interlocks as the sole de-energizing means.** Per OSHA, interlocks are not a substitute for lockout/tagout.
- **Bead-link retainer chains.** More breakable than link, sash, or woven-mesh; not to be used.
- **Integral fasteners (e.g., studs).** Fasteners must not be an integral part of the housing.

## Key Takeaways

- Maintainability is designed in at the architecture stage through modular decomposition, accessibility, and reuse — not patched in later.
- The chapter converts "easy, fast, safe maintenance" into quantified, verifiable limits: lift/carry weights, push/pull forces, reach distances, clearances, opening sizes, character heights, and turn counts.
- Continuous-operation systems demand explicit maintainability strategies — non-interrupting maintenance, redundancy, degraded modes, and automatic fault detection/isolation.
- Safety is layered and standards-anchored: positive disconnects, interlocks, and OSHA-compliant lockout/tagout, with persistent hazard labeling.
- Interchangeability is governed by a strict functional-versus-physical correspondence rule, and error-proofing (alignment aids, incompatible connectors, distinct fasteners) prevents incorrect assembly.
- Fastener and connector selection follows explicit preference orders favoring tool-free, one-handed, few-turn, captive solutions.
- Source traceability is a feature: every rule cites MIL-STD-1472G, MIL-HDBK-759C, MIL-STD-1800A, AFSC DH 1-3, UCRL-15673, NASA-STD-3000A, or OSHA 29 CFR 1910, making the criteria auditable.

## Connects To

- **`nasa-hsi`** — Complements it. HF-STD-001B is HSI material reaching beyond the NASA spaceflight context into FAA ground facilities and military-derived ground systems; many rules here cite NASA-STD-3000A, so the two packs share lineage on continuous-operation, redundancy, and fault-detection criteria while HF-STD-001B adds quantified handling, fastener, and access detail.
- **Reliability, Availability, and Maintainability (RAM) engineering** — Modularization, access, fault isolation, and frequently-failing-item replacement are the human-factors face of mean-time-to-repair and availability goals.
- **Safety engineering and hazardous-energy control** — The interlock, lockout/tagout, and hazard-labeling rules tie directly to OSHA 29 CFR 1910 and to system-safety practice.
- **Logistics and supportability (ILS)** — Reuse-of-existing-items, fastener-variety minimization, tool minimization, and standardized units feed sparing, provisioning, and training analyses.
- **Ergonomics and biomechanics** — The lift, carry, push/pull, reach, and working-level limits are anthropometric and strength criteria projected to a mixed-gender population.
- **Earlier chapters of this pack** — Builds on the standard's general human-factors and anthropometric foundations and feeds forward into the connector, line, and test-point sections that follow Section 5.2.7.

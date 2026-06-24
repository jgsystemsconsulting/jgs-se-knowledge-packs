# Chapter — Foundations: A Good Requirements Specification and the Recommended-Practices Approach

## Core Idea

This Handbook exists because requirements practice is fragmented: the literature is enormous and conventions differ even between teams in the same industry. Rather than invent a new method, the Handbook gathers strong ideas from several established approaches, reconciles them into one coherent set, and grounds each one in worked examples so the payoff is visible. Its scope is deliberately narrow — real-time, embedded systems, with the avionics industry as the target domain — because narrowing the domain is what lets the guidance be concrete instead of generic. A recurring emphasis throughout is the handoff from system-level requirements to software requirements, reflecting how much avionics behavior now lives in software.

The organizing question the Handbook poses is simple to state and hard to satisfy: what separates a good requirements specification from a bad one? The answer it adopts, attributed to David Parnas, is that a good specification captures everything needed to build the correct system and nothing beyond that. That single criterion sets up a tension the rest of the work tries to manage — say enough to fully constrain *what* the system must do, without crossing into *how* it should be built and thereby over-constraining the people who design it.

Crucially, the Handbook does not prescribe a rigid process. It concentrates on *what information* a requirements specification must contain and *how that information can be collected and organized*, leaving organizations free to fit the practices to their own tools and workflows. Almost every team adopting this material is expected to modify it, possibly heavily.

## Frameworks Introduced (exact source names, when/how)

The chapter is unusually explicit about its intellectual lineage. It names the prior bodies of work it draws on and explains the role each one plays.

- **Software Cost Reduction (SCR) methodology** and the **four-variable model** of Parnas and Madey — cited as the origin material, originally created to capture the requirements for a U.S. Navy A-7E Corsair II combat aircraft. The Handbook draws strongly on both. SCR is noted to have kept evolving for two decades, with the Naval Research Laboratory building tools to specify and analyze SCR models.
- **Consortium Requirements Engineering (CoRE) methodology** — an extension of the SCR/four-variable ideas by the Software Productivity Consortium, used to specify requirements for the C-130J aircraft. Many of the Handbook's recommendations on *organizing* requirements trace back to CoRE.
- **Requirements State Machine Language (RSML)** — from Leveson and colleagues, used to specify the Traffic Alert and Collision Avoidance System II. The chapter follows its evolution into **RSML without events (RSML-e)**, used as a basis for formal analysis of requirements specifications.
- **Specification Toolkit and Requirements Methodology (SpecTRM)** — from the Safeware Engineering Corporation, an extension of the RSML notation. SpecTRM models sit inside a larger *intent specification* that the source describes as carrying rationale continuously from a system's highest-level goals down through the model to implementation and even operator-training material.
- **Use cases** (textual) — adopted as the technique for moving from an early, informal overview into a detailed, formal requirements specification. The Handbook's treatment of operational concepts rests on textual use cases.
- **Standards landscape** — the chapter points the reader to REM-relevant standards rather than restating them: IEEE Std 1233 (system requirements specifications), IEEE Std 830-1998 (software requirements specifications), DO-178B and its clarification DO-248B (airborne software certification), DO-278 (CNS/ATM systems software integrity), ARP 4754 (highly-integrated/complex aircraft systems certification), and ARP 4761 (safety assessment process).

### The 11 main-level recommended practices

The backbone framework of the Handbook is its set of eleven main-level recommended practices, presented roughly in execution order (with the last two excepted), and detailed in later sections. Restated compactly, they are:

1. Build a system overview (practice 2.1)
2. Fix the system boundary (2.2)
3. Work out the operational concepts (2.3)
4. Surface the environmental assumptions (2.4)
5. Lay down a functional architecture (2.5)
6. Adjust that architecture for implementation constraints (2.6)
7. Name the system's modes (2.7)
8. Write the detailed behavior and performance requirements (2.8)
9. Derive the software requirements (2.9)
10. Allocate the system requirements down to subsystems (2.10)
11. Record the rationale (2.11)

Each main-level practice in turn contains finer **sublevel recommended practices**. The source flags these sublevels as more sensitive to implementation choices and therefore the most likely to need adjustment when a team tailors a main-level practice to its existing methods and tools.

## Key Concepts

- **"What, not how."** The dividing line between requirements and design: a specification should pin down what the system must do without dictating the implementation. Straying into design over-constrains the developers.
- **Far more than shall-statements.** A good specification is not merely a list of "shall" lines. Because the necessary information is usually large and read by audiences with different concerns and expertise, much of the work is structural — making the requirements readable, maintainable under change, and ensuring they are complete, consistent, clear, and well organized.
- **Informal-to-rigorous progression.** A development typically starts knowing little about the system and ends knowing a great deal. The requirements process should mirror that arc — relatively informal practices early on, more rigorous practices as the requirements firm up.
- **Architecture and requirements are interleaved.** For large systems it is generally impractical to state detailed requirements independent of the architecture. Instead, high-level requirements drive the next level of design, which enables more detailed component requirements, repeating until enough detail is reached. Requirements specification and architecture development advance together.
- **Practices reinforce each other.** The recommended practices can each be applied in isolation, but the source stresses they strengthen one another when used as a set.
- **Tailoring is assumed, not exceptional.** Order is not fixed, iteration between activities is expected, and organizations are explicitly encouraged to modify the practices — sometimes significantly — to fit their processes and tools.
- **Two running examples.** The *Isolette thermostat* (a neonatal-care incubator controller) is the small, single-system example; the simple *Flight Control System / Flight Guidance System / Autopilot* trio is the larger example showing how requirements get allocated from a system to subsystems built by different subcontractors. Neither is meant to be a complete real system — both exist only to make the practices concrete.

## Mental Models

- **The Parnas balance beam.** Picture a beam with "under-specified" on one side and "over-constrained (design leakage)" on the other. A good specification balances it: everything needed for the correct system, and nothing more. Most chapters of the Handbook are, in effect, ways to keep the beam level.
- **Funnel of formality.** Requirements engineering as a funnel that narrows from an informal, high-level system overview at the wide end to a detailed, formal behavioral/performance specification at the narrow end. Use cases are the bridge that carries you down the funnel.
- **Staircase of detail interleaved with architecture.** Each step down is: state high-level requirements, do the next slice of design, then derive more detailed requirements for each component — descend until the needed detail is reached. You never lay the whole specification before touching the architecture.
- **Lineage as a toolbox, not a doctrine.** SCR, the four-variable model, CoRE, RSML/RSML-e/SpecTRM, and textual use cases are sources to draw the best ideas from and recombine — the Handbook positions itself as a curator that organizes borrowed ideas into a coherent whole.
- **Intent specification as a spine.** Borrowed from SpecTRM: imagine a continuous thread of rationale and reasoning running from top-level system goals down to implementation and operator training, so that *why* is never lost as you descend toward *what* and eventually *how*.

## Key Takeaways

- The Handbook is a set of *recommended practices* for collecting, writing, validating, and organizing requirements — explicitly a synthesis of existing approaches, not a brand-new methodology.
- Scope is intentionally narrow: real-time, embedded systems in avionics, with strong emphasis on easing the system-to-software requirements transition.
- The quality bar is the Parnas criterion — everything needed for the correct system and nothing more — which reduces operationally to "specify what, not how."
- A good specification is mostly structure: complete, consistent, clear, well organized, readable by diverse audiences, and maintainable under change — not just a pile of shall-statements.
- The process should move from informal to rigorous as knowledge grows, and requirements work is interleaved with architecture for any large system.
- Eleven main-level recommended practices (each with sublevels) form the spine, presented in rough execution order with heavy iteration and tailoring expected.
- The work rests on a named lineage — SCR, the four-variable model, CoRE, RSML/RSML-e/SpecTRM, textual use cases — and points to a standards set (IEEE 1233, IEEE 830-1998, DO-178B, DO-248B, DO-278, ARP 4754, ARP 4761).
- Two examples — the Isolette thermostat and the FCS/FGS/Autopilot — recur throughout to make the practices concrete and to demonstrate allocation across subsystems and subcontractors.

## Connects To

- **Requirements-writing guidance generally:** This chapter is the embedded/real-time, avionics-slanted complement to general requirements-writing material. Its "what not how" rule, its insistence that good requirements are complete/consistent/clear/well-organized, and its informal-to-rigorous progression all translate directly to non-avionics requirements work, even though the worked examples and standards are domain-specific.
- **The rest of the Handbook:** Sections 2.1 through 2.11 expand the eleven main-level practices; sublevels run from 2.1.1 through 2.11.7 with corresponding tables. This chapter is the map for all of them.
- **Operational concepts and use cases:** The use-case foundation introduced here feeds directly into the operational-concepts practice (#3) and the broader transition from informal overview to formal specification.
- **Architecture practices:** The interleaving-with-architecture idea sets up Develop the Functional Architecture (#5), Revise the Architecture to Meet Implementation Constraints (#6), and Allocate System Requirements to Subsystems (#10).
- **Certification and safety standards:** The named standards (DO-178B/DO-248B, DO-278, ARP 4754, ARP 4761, IEEE 1233/830) anchor this material in the avionics certification and safety-assessment context, distinguishing it from domain-neutral requirements advice.

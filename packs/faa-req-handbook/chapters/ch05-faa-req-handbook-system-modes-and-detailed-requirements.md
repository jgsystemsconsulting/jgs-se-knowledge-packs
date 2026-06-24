# Chapter — Identify System Modes and Develop Detailed Behavior and Performance Requirements

## Core Idea

Once the monitored and controlled variables, the system boundary, the operational concepts, the environmental assumptions, and the functional architecture are in place, two final activities turn that scaffolding into testable requirements. First, identify the system's **modes** — the small set of distinct, externally visible behaviors the system can exhibit. Second, write the **detailed behavior and performance requirements** that say, for every mode and every relevant condition, exactly what value each controlled variable must take, within what tolerance, and within what time bound.

The handbook frames the detailed requirements as a precise mathematical relationship: how the controlled variables change in response to changes in the monitored variables. Modes exist to make that relationship tractable. By carving the input-to-output mapping into a handful of mode-specific pieces, you can specify and check each piece independently. The chapter's embedded/real-time slant is explicit — latency and tolerance are first-class requirement attributes, not afterthoughts — and it complements the requirements-writing discipline by showing the structural pattern every "shall" statement should follow.

## Frameworks Introduced (exact source names, when/how)

- **Leveson's definition of modes** (reference 35) — invoked to anchor the concept. A mode is a distinct behavior of the system: the same stimulus (e.g., a button press) produces different responses during power-up, during self-test, and during normal operation, so those three behaviors are three modes. Used at the start of section 2.7 to define what a mode is and is not.

- **CoRE methodology** (references 4 and 5) — supplies the structural model for detailed requirements. It names the **ideal value function** for each variable: the value a perfect system would assign to that controlled or internal variable in every state. CoRE also frames the requirement as the combination of ideal value, **tolerance**, and **latency**. Referenced throughout section 2.8 as the source of the ideal-value/tolerance/latency decomposition.

- **SCR (Software Cost Reduction)** (references 2 and 3) and **CoRE** (references 4 and 5) — both name the input-to-output mapping the **requirement (REQ) relationship**. Cited where the detailed requirements are introduced as a mathematical relationship between monitored and controlled variables (footnote in section 2.8).

- **State transition diagrams** (reference 42) — presented in section 2.7 as a common notation for specifying modes, illustrated by the Isolette Regulate Temperature mode diagram (INIT → NORMAL → FAILED). The handbook flags them with a caution rather than an unqualified endorsement.

- **Tabular specification formats** — section 2.8.10 surveys several. SCR and CoRE rely heavily on **condition tables, event tables, and mode tables**. **RSML** (reference 8) and **SpecTRM** (reference 15) use a format called **and/or tables**. Additional tabular formats are catalogued in reference 43. These appear as alternatives to "shall" statements for capturing the ideal value function.

## Key Concepts

- **Mode (externally visible discontinuity).** A mode captures a discontinuity in system behavior that an operator or another system can observe. A mode may or may not be displayed to a user, but it is visible by definition, because the system answers the same input differently depending on which mode it is in. Modes can be simple or complex and can apply to the whole system or only a part.

- **Mode transitions.** Identifying the modes is incomplete without defining how the system moves between them. The Isolette example walks through this: the function begins in INIT at power-on, advances to NORMAL once the Regulator Status becomes valid (initialization complete, self-tests passed, monitored variables sensed), and drops to FAILED if initialization times out or if Regulator Status goes false during NORMAL — and stays FAILED until a power cycle.

- **Modes simplify, not complicate.** Breaking the monitored-to-controlled relationship into per-mode pieces is the whole point. Introduce a mode only to mark a discontinuity that can be inferred from observable behavior; never introduce one that cannot. Overly complex transition diagrams are a warning sign that design decisions are leaking into the requirements.

- **The requirement pattern: condition then assignment.** Every detailed requirement splits into a *condition* under which it holds and an *assignment* of a value to a variable. The condition itself decomposes into the relevant system mode plus further constraints on monitored and internal variables. The requirements reuse the established names — monitored variables, controlled variables, modes, internal variables — as their vocabulary, tying each statement back to the framework built in earlier steps.

- **Ideal value function.** At the lowest level of the functional architecture, define what value each controlled and internal variable would take in a perfect system, for every possible state. Chained together, these assignments fully describe how the controlled variables react to the monitored variables in the ideal case.

- **Completeness.** Every controlled and internal variable needs an assigned ideal value for every system state. The handbook makes this concrete: two Heat Control requirements that cover only the "too cold" and "too hot" cases in NORMAL are incomplete, because they say nothing about INIT, FAILED, or the in-band temperature range. Three more requirements close the gap. Where no meaningful assignment exists, the variable is explicitly marked **UNSPECIFIED** — and that fact is documented, so downstream consumers know the value is not to be trusted (e.g., the Display Temperature outside NORMAL mode).

- **Consistency.** No system state may be assigned two different ideal values. The chapter shows how a boundary slip creates a conflict: rewriting the "less than" condition as "less than or equal to" makes one requirement command Heat Control ON at the lower bound while another requires it to hold its previous value at that same point — two values for one state.

- **Non-duplication.** No two requirements should prescribe the same outcome for overlapping modes and conditions, whether by literal repetition or by overlapping ranges.

- **Latency.** The performance dimension. Latency is the maximum lag allowed between a monitored variable changing and the affected controlled variable taking its new value. The Heat Control latency is 6 seconds, with a rationale that traces back to the environmental assumptions: because a closed Isolette warms or cools at no more than 1°F per minute, acting within 6 seconds keeps the Current Temperature from drifting more than 0.1°F — the sensor's required resolution. Latency can be a constant or a function of state, and several controlled variables can share one latency definition; a rationale is always required.

- **Tolerance.** The acceptable deviation from the ideal value for a *numerical* controlled variable (the chapter's example: the delta above and below true altitude that a displayed altitude may carry). For Boolean and enumerated variables, tolerance is not meaningful — Heat Control, being on/off, gets N/A.

- **Internal variables are bookkeeping.** Internal variables exist only to break the ideal value function into manageable pieces. The system makes no timing or accuracy promise about them, so latency and tolerance are never specified for internal variables — only for controlled variables, which are what the system actually owes its environment.

- **Traceability via organization.** Present each variable's requirements inside the function that produces that variable. The dependency diagrams then act as a visual table of contents, and every variable definition traces directly to its parent function (e.g., Heat Control requirements live in the Manage Heat Source Function).

## Mental Models

- **Modes as a switch upstream of the logic.** Think of the mode as selecting which sub-rulebook is active. INIT, NORMAL, and FAILED each carry their own assignment rules; the mode picks the rulebook, the conditions pick the row within it.

- **The completeness grid.** Imagine a grid with modes down one axis and condition ranges across the other. The requirement set is complete only when every cell holds exactly one ideal value, and consistent only when no cell holds two. The handbook's tabular format (table 15) literally renders this grid — Regulator Mode as rows, temperature conditions as columns, the Heat Control value in the bottom row — which is precisely why a table makes completeness and consistency easy to confirm by inspection.

- **Ideal value, then loosen, then time-bound.** Specify the perfect answer first (ideal value function), then admit a band around it (tolerance), then bound how long the system may take to get there (latency). The requirement is the trio, layered in that order.

- **Rationale as a tether to physics.** A latency number floating free is a guess. The 6-second figure is trustworthy because its rationale chains back through the Isolette's thermal rate and the sensor's resolution to the environmental assumptions. Every timing and tolerance value should be similarly tethered.

- **Notation is a vehicle, not the destination.** Whether you write shall statements, a graphical ideal-value model, or condition/event/mode tables, the obligation is identical: state the monitored-to-controlled relationship completely, consistently, unambiguously, and testably. A graphical model can blur where one requirement ends and the next begins — a cost to weigh against its compactness.

## Anti-patterns

The source names these explicitly:

- **Mode confusion.** Poor mode design can leave operators unsure which mode the system is in. The handbook calls this a serious safety concern implicated in several aviation accidents (references 32 and 34). Named contributors include: missing or inadequate feedback to operators, errors entering or interpreting information across modes, system behavior that is inconsistent between modes, differing operator authority limits between modes, silent (unannounced) mode transitions, and unintended side effects of transitions. Designing systems whose modes are clearly indicated and whose behavior is consistent and anticipatable is called out as hard and beyond the handbook's scope (see references 33, 35, 36, 37).

- **Inventing modes with no observable basis.** Defining modes that cannot be inferred from externally visible behavior. Modes are reserved strictly for observable discontinuities.

- **Smuggling design into requirements via over-complex transition diagrams.** When a state transition diagram becomes overly complex, treat it as a signal that design decisions are being baked into the requirements that should have been left out.

- **Incomplete coverage.** Leaving controlled or internal variables unassigned for some modes or conditions (the original two-requirement Heat Control set).

- **Hidden inconsistency at boundaries.** Overlapping conditions — often introduced by a `<` versus `<=` slip at a range boundary — that assign two values to one state.

- **Duplicate requirements.** The same outcome stated twice, directly or through overlapping modes and conditions.

- **Specifying timing/accuracy for internal variables.** Attaching latency or tolerance to internal variables, which carry no such obligation.

## Key Takeaways

- Identify the major modes *before* writing detailed requirements; modes are a starting point that gets validated and refined during detailed specification, where missing or unneeded modes surface.
- A mode is an externally visible discontinuity in behavior — nothing more, nothing less. Do not introduce modes you cannot infer from observable behavior.
- Always define the allowed transitions between modes, including the triggering conditions and any latching behavior (e.g., FAILED persists until power cycle).
- Write each requirement as *condition (mode + variable constraints) → assignment*, using the established variable, mode, and internal-variable names as vocabulary.
- Build the ideal value function variable by variable, ensuring every controlled and internal variable has exactly one value for every system state; use UNSPECIFIED — and document it — where no meaningful value exists.
- Enforce completeness, consistency, and non-duplication; tabular formats make the first two checkable by inspection.
- Specify latency for every controlled variable (with a rationale traceable to environmental assumptions) and tolerance for every numerical controlled variable; never specify either for internal variables.
- Organize requirements under the function that produces each variable so the dependency structure doubles as a navigable table of contents and guarantees traceability.
- The notation (shall statements, graphical models, condition/event/mode tables, and/or tables) is secondary; the requirement set must be complete, consistent, unambiguous, and testable regardless of form.

## Connects To

- **Monitored and controlled variables / system boundary.** Modes and detailed requirements are written entirely in the vocabulary of the variables and boundary established earlier; this chapter is where that vocabulary pays off.
- **Functional analysis and the dependency diagrams.** Requirements are filed under the function that produces each variable, so the functional architecture becomes the organizing index for the requirements.
- **Environmental assumptions.** Latency and tolerance values draw their justification from the environmental assumptions (the Isolette thermal rate and sensor resolution behind the 6-second Heat Control latency).
- **Requirements-writing discipline.** This chapter supplies the structural pattern — condition-plus-assignment, completeness, consistency, testability — that complements the prose-level craft of writing individual requirement statements.
- **Verification and validation.** Completeness, consistency, non-duplication, and testability are exactly the properties that make a detailed requirement set checkable, setting up downstream V&V.
- **Safety analysis.** Mode confusion is framed as a safety issue tied to real aviation accidents, linking mode design to system safety rather than mere usability.

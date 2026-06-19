# Chapter 7: 13 State Machines

## Core Idea

State machines in SysML model discrete, event-driven behavior as a sequence of states, transitions, and guarded actions. They express how a system or component responds to events and conditions over time, with states representing stable conditions and transitions representing reactions to stimuli.

## Frameworks Introduced

- **State Machine (behavior state machine)**: A behavioral classifier modeling object state history through finite state transitions. Instances execute against triggering events and guard conditions.
  - When to use: When behavior is fundamentally discrete, event-responsive, or mode-based (e.g., operational modes, control flow, protocol logic).

- **State**: A stable condition in which an object can exist; may have entry/exit/do activities (continuous or discrete execution while in the state).
  - When to use: Any stable behavioral condition with associated reactions.

- **Composite State**: A hierarchical state containing nested regions; regions may be sequential or concurrent.
  - When to use: To decompose complex behavioral hierarchies into sub-states and manage concurrent substates.

- **Transition**: A directed edge representing a change from one state to another, optionally triggered by an event, guarded by a condition, and executing actions (entry, exit, do, send signal).
  - When to use: To define what causes state changes and what happens during the change.

- **PseudoState** (and subtypes: **Initial**, **Choice**, **Junction**, **Entry Point**, **Exit Point**, **History** [shallow/deep], **Final**): Transient nodes that model control flow without stable residence. Not actual states.
  - Initial: Entry point to a state machine or composite state.
  - Choice/Junction: Conditional branching; choice evaluates guards, junction awaits a trigger.
  - Entry/Exit Points: Alternative ports for entering/exiting a composite state.
  - History (shallow/deep): Resume prior state (shallow) or deepest prior state (deep) upon re-entry.
  - Final: Marks completion of a state machine or region.

- **Submachine State**: A state whose behavior is specified by reference to another state machine (composition by delegation).
  - When to use: To reuse or factor out complex behavioral specifications as separate state machines.

- **Region**: An orthogonal decomposition of a composite state; models concurrent substates within a single state.
  - When to use: To express concurrent behavioral substates that evolve independently.

- **Activity** (entry, exit, do; send signal action, receive signal action): Behaviors executed on state entry/exit, continuously/discretely while in the state, or as transition effects.
  - When to use: To specify side effects or computations triggered by state events.

- **State Machine Diagram**: Graphical representation of state machine structure and transitions; frame notation with state/transition elements.

## Key Concepts

- **Finite state transition system**: State machines model behavior as a discrete sequence of states and transitions; time and events are the drivers.

- **Event-triggered transition**: A transition occurs when an event is received and any associated guard condition evaluates to true; effects execute atomically during the transition.

- **Guard condition**: A Boolean expression evaluated when a transition trigger is received; transition is enabled only if the guard is true.

- **Do activity**: An action that executes continuously or discretely while the state is active; distinct from transition-triggered entry/exit actions.

- **Behavioral equivalence to activities**: State machines as blocks in SysML are analogous to activity definitions as blocks (see clause 11); submachine states parallel call actions, and state machine associations to classifiers parallel activity associations.

- **Orthogonal regions**: Multiple regions within a composite state can execute concurrently, each with its own state history and transitions.

- **Protocol state machines excluded**: SysML uses UML behavior state machines (not protocol state machines) to reduce language complexity; behavior state machines are sufficient for expressing protocols.

## Mental Models

- **Use state machines to partition discrete control logic by mode or operational state.** If behavior radically changes based on a system mode (e.g., powered vs. standby, initializing vs. running), a state machine captures that structure more naturally than conditional branching in an activity.

- **Model hierarchical/nested behavior via composite states, not deeply nested if/else.** Composite states and regions allow you to abstract away sub-behaviors while keeping the top-level state diagram legible.

- **Reserve do activities for continuous or background behavior within a state; use transition actions for discrete event effects.** Entry/exit actions are appropriate for setup/cleanup; do activities run throughout the state residence.

- **Submachine states enable reuse: factor recurring behavioral patterns into separate state machines and instantiate them via submachine references.** This keeps large diagrams manageable and promotes consistency.

## Anti-patterns

- **Conflating guard conditions with state identity**: A guard is a runtime condition checked when a transition fires; it is not part of the state definition. Overloading guards to simulate substates obscures the actual state structure.

- **Ignoring orthogonal regions and using sequential states instead**: If behavior contains truly independent concurrent substates, orthogonal regions are clearer and enforce correct concurrency semantics. A sequence of sequential states can deadlock or miss concurrent events.

- **Using protocol state machines (excluded from SysML)**: SysML intentionally excludes UML protocol state machines to reduce complexity. Behavior state machines are sufficient for all protocol modeling use cases.

## Key Takeaways

1. **State machines model discrete, event-driven behavior.** Use them when system behavior is fundamentally mode-based or reactive to stimuli, not for continuous data flow (use activities instead).

2. **Every state can have entry, exit, and do activities.** Entry/exit run on state transitions; do activities run while resident in the state (useful for continuous monitoring or background tasks).

3. **Guard conditions gate transitions; they are checked when a trigger arrives.** Separate the condition logic from the state definition to avoid spaghetti guards.

4. **Composite states and regions enable hierarchical, concurrent behavior.** Use composite states to abstract sub-behaviors and regions to model independent parallel behaviors within a single state.

5. **Submachine states promote reuse and maintainability.** Factor complex behavioral patterns into separate state machines and reference them via submachine states rather than inlining complex diagrams.

6. **Choice and junction pseudo-states enable conditional branching; history pseudo-states resume prior state.** Choice evaluates guards immediately; junction waits for a trigger. Shallow history resumes the immediate prior state; deep history resumes the deepest prior state in the hierarchy.

7. **State machines as blocks have the same association semantics as activities.** A state machine block can be associated with submachine states or parameter types, analogous to how activity blocks associate with call actions or parameter types.

## Connects To

- **Clause 11 (Activities)**: State machines and activities are both behaviors; submachine states parallel call actions; association semantics between state machine blocks and types mirror activity block associations. Use activities for data-driven transformations; state machines for event-driven mode logic.

- **UML (Behavior State Machines)**: SysML adopts UML's behavior state machine semantics without the excluded protocol state machine variant. The UML normative semantics govern guard evaluation, transition atomicity, and region concurrency.

- **Blocks (Clause 8)**: State machines appear as blocks (tagged with `«stateMachine»`) in block definition diagrams; associations between state machines and classifiers use AdjunctProperty stereotypes to reference submachine states and parameters.

- **State Machine Diagrams (Clause 3, diagram taxonomy)**: State machine diagrams are one of the nine SysML diagram types; they are frame-based and contain state and transition notation.

- **Finite State Automata (Theory)**: The semantic foundation is classical finite state automaton theory, extended with guarded transitions, hierarchical states, and concurrent regions.

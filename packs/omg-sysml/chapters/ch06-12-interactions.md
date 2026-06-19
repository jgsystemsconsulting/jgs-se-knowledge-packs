# Chapter 6: 12 Interactions

## Core Idea

Interactions describe the flow of messages and control between system entities (blocks, actors, or parts) over time. SysML adopts UML's Sequence diagram as the primary interaction notation, enabling engineers to model temporal communication patterns, decompose system behavior hierarchically, and express control logic (sequencing, parallelism, alternatives, loops) within a single visual frame.

## Frameworks Introduced

- **«interaction»**: A SysML block stereotype labeling an Interaction UML construct. Interactions model the executable behavior of multi-participant message exchanges and can be associated with other interactions (via InteractionUse) or blocks (via Association) analogously to how Activity diagrams associate ActivityNodes with blocks.
  - When to use: Define time-ordered message flows between system parts or external actors; decompose complex behaviors into reusable sub-interactions.

- **Sequence Diagram (seq)**: The diagram type selected by SysML for interaction modeling. Represents lifelines (entities), messages (control flow), execution specifications (activity on a lifeline), combined fragments (control operators), and temporal constraints.
  - When to use: Capture message sequences during a scenario, critical path, or failure mode; show which parts communicate and in what order.

- **Lifeline**: A named entity (block, actor, or decomposed part) participating in the interaction, represented vertically. Time flows downward along each lifeline's timeline.
  - When to use: Represent each communicating entity; decompose a lifeline into its constituent parts via InteractionUse reference.

- **Message**: A directed communication between two lifelines, labeled with a signal name, arguments, and optional return value. Messages may be lost (ending at a boundary) or found (originating from a boundary).
  - When to use: Express data or control flow; specify parameters and return types aligned to block operations or ports.

- **ExecutionSpecification**: A rectangle on a lifeline indicating active execution (the participant is processing). Execution start/end may be marked by message arrival or explicit events.
  - When to use: Show which lifeline is "busy" during a segment; highlight computation or processing.

- **CombinedFragment**: A frame enclosing a region of the interaction and labeled with an interaction operator (seq, alt, opt, break, par, strict, loop, critical, neg, assert, ignore, consider) and corresponding operands.
  - When to use: Model control flow: weak sequencing (seq), alternatives (alt), optional paths (opt), parallel execution (par), loops (loop), critical sections (critical), break/escape (break), negative traces (neg), assertions (assert), or filter/ignore constraints (ignore/consider).

- **InteractionUse**: A reference to another interaction (by name), optionally with arguments and return value assignments. Graphically a ref frame; semantically equivalent to "call" in activities.
  - When to use: Decompose complex scenarios; reuse standard interaction sequences; manage diagram scale.

- **StateInvariant**: A constraint or condition that must hold true at a point on a lifeline; labels the expected state of a block.
  - When to use: Assert pre-/post-conditions on a lifeline during the sequence.

- **Continuation**: An explicit label marking a reconnection point when an InteractionUse or CombinedFragment operand is resumed on another diagram.
  - When to use: Split long sequences across multiple diagrams; label resume points.

- **Coregion** (parallelization): A CombinedFragment with the par operator; allows messages within the region to execute in any order (unordered parallel execution).
  - When to use: Model truly concurrent, non-ordered message exchange within a parallel fragment.

- **CreationEvent / DestructionEvent**: Events representing the birth or death of a lifeline participant during the interaction.
  - When to use: Model dynamic creation/destruction of parts or transient actors.

- **DurationConstraint** and **TimeConstraint**: UML constraints labeling message segments (DurationConstraint) or points (TimeConstraint) to specify timing requirements (e.g., "must occur within 100 ms").
  - When to use: Capture non-functional requirements on interaction timing; feed into analysis models.

- **GeneralOrdering**: An explicit arrow linking two events, enforcing a partial order when implicit sequencing is ambiguous.
  - When to use: Clarify ordering when operands or parallel regions need a causality constraint.

- **AdjunctProperty**: A SysML stereotype on a property whose principal is an InteractionUse (referring to a used interaction) or a parameter of an interaction. Enables associations from block diagrams to interaction references and parameter types.
  - When to use: Link block definition diagrams to sequence diagrams; trace which blocks invoke which interactions.

## Key Concepts

- **Interaction as Behavior Block**: An Interaction is a UML Behavior (hence a Class) and a SysML block. It defines a behavioral contract: which entities participate (lifelines), what messages they exchange, and in what temporal order. Interactions can own parameters (inputs/outputs) and can be invoked via InteractionUse, much like Activities invoke sub-Activities.

- **Lifeline Decomposition**: A lifeline can be decomposed via an InteractionUse that references a more detailed interaction, allowing hierarchical refinement of complex behaviors without flattening the diagram.

- **Interaction Operators**: Twelve operators (seq, alt, opt, break, par, strict, loop, critical, neg, assert, ignore, consider) encode control semantics. Each operator defines how its operands relate: `seq` = weak sequencing (default, deterministic order); `par` = parallel (any order); `alt` = exclusive choice; `opt` = conditional execution; `loop` = repetition; `critical` = atomic region; `strict` = strict ordering (unrelated messages must not interleave); `break` = escape (exception-like); `neg` = trace must NOT occur; `assert` = trace MUST occur; `ignore` = messages in the list are irrelevant (filtered); `consider` = restrict to listed messages.

- **Temporal Semantics**: Time flows downward. Messages are ordered top-to-bottom unless explicitly re-ordered by GeneralOrdering. DurationConstraint and TimeConstraint attach timing metadata for analysis.

- **Message Formality**: Messages are typed (signal, operation, or implicit). Arguments and return values are bound to parameters and attributes at design time, enabling integration with block definitions and operation contracts.

- **SysML Restriction**: SysML excludes Communication, Interaction Overview, and Timing diagrams from UML 2 to reduce notation redundancy and focus on the Sequence diagram as the primary interaction vehicle.

## Mental Models

- **Use Sequence diagrams for scenario walkthrough**: When you need to show "what happens when the system receives input X"; trace the message flow top-to-bottom to see causal chains and actor responsibilities.

- **Model parallelism with `par` fragments**: When multiple blocks act concurrently (e.g., steering and speed control happen at the same time), wrap them in a `par` CombinedFragment to capture the unordered semantics.

- **Decompose large interactions via InteractionUse `ref`**: If a sequence grows beyond one page, extract a sub-sequence into a separate interaction and reference it with a `ref` frame; label the frame with the sub-interaction name and actual arguments.

- **Bind interaction parameters to port types**: When an InteractionUse has arguments/return values, map them to the types of the invoking block's ports or properties; this ensures the message interface is formalized in the block definition.

## Anti-patterns

- **Mixing Timing and Logical Sequencing**: SysML sequence diagrams represent logical message order, not wall-clock timing. Do not use y-axis position to imply precise timing delays; use DurationConstraint/TimeConstraint stereotypes instead.

- **Overloading Lifelines with Logic**: Sequence diagrams show message flow, not internal computation. If the diagram needs complex control logic within a lifeline (e.g., conditionals on local state), decompose via InteractionUse or move to a state machine diagram.

- **Undefined Message Types**: Every message should correspond to a named signal, operation, or event defined in the block's interface. Unlabeled or vague messages ("data") weaken traceability and verification.

- **Ignoring Operator Semantics**: Misusing `par` when `seq` is intended (or vice versa) can lead to ambiguous or over-constrained models. Choose the operator that exactly matches the intended behavior.

## Key Takeaways

1. **Sequence diagrams are SysML's primary interaction notation**: Use them to model message flows between blocks and actors; exclude Communication and Interaction Overview diagrams per SysML's design.

2. **Interactions are reusable blocks**: Define interactions as «interaction» blocks; associate them with other blocks via Association or AdjunctProperty; invoke them via InteractionUse (ref frame) to enable hierarchical decomposition.

3. **Operators encode control semantics precisely**: Choose seq (default ordering), par (parallel, unordered), alt (exclusive choice), opt (conditional), loop (repetition), or specialized operators (critical, strict, break, neg, assert, ignore, consider) to match your behavioral intent.

4. **Lifelines decompose hierarchically**: A lifeline can be decomposed via a ref InteractionUse to a more detailed interaction, allowing large scenarios to be split across diagrams without loss of structure.

5. **Timing is explicit via constraints**: Use DurationConstraint and TimeConstraint to attach non-functional timing requirements to message segments or points; the y-axis is logical, not chrono-metric.

6. **Messages are formally typed**: Every message should align to an operation, signal, or property of the sending/receiving block; bind InteractionUse parameters to block port types for end-to-end traceability.

7. **StateInvariant and Continuation support long sequences**: Use StateInvariant to assert block state at interaction points; use Continuation to label where a sequence continues on another diagram.

## Connects To

- **UML 2.x Interactions**: SysML inherits the UML Interaction metamodel (Lifeline, Message, ExecutionSpecification, CombinedFragment, InteractionUse, etc.) and the Sequence diagram notation; SysML's contribution is the «interaction» block stereotype and exclusion of Communication/Interaction Overview/Timing diagrams.

- **SysML Blocks (Clause 9)**: Interactions are stereotyped as blocks («interaction»); they own parameters (in/out), can be associated with classifiers (blocks or value types), and can appear in block definition diagrams alongside other block elements.

- **SysML Activities (Clause 11)**: Interactions and Activities are both Behaviors. Activities model action flow; Interactions model message/event flow. Both can invoke sub-behaviors (CallActivityAction vs. InteractionUse) and both can be represented as blocks.

- **SysML Ports and Interfaces (Clauses 8–9)**: Messages in interactions correspond to signals/operations owned by block ports or the block itself. The message interface must formalize to the port's provided/required interfaces.

- **SysML State Machines (Clause 13)**: State machines define the internal state of a block; interactions show multi-block message exchange. Together, they model behavior at different levels: state machines for intra-block state, interactions for inter-block communication.

- **SysML Requirements (Clause 6)**: Interactions can be annotated with requirement references to trace which behaviors satisfy which requirements. A scenario (interaction) is one way to demonstrate requirement satisfaction.

- **ISO/IEC/IEEE 42010 (Architecture Framing)**: Sequence diagrams are often used in architecture documentation as behavior-viewpoint artefacts to show system-of-systems interactions, lifecycle processes, or scenario enactment.

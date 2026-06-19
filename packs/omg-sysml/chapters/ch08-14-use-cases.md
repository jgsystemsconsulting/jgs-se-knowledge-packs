# Chapter 8: 14 Use Cases

## Core Idea
Use case diagrams capture the system boundary, the actors (external entities) that interact with it, and the use cases (functionality/capabilities) that deliver value through their interaction. Use cases model the "what" the system is supposed to do from the perspective of external stakeholders without prescribing "how."

## Frameworks Introduced
- **`UML4SysML::UseCase`**: A specification of a service or capability realized by the system; appears as a named oval inside the system boundary.
  - When to use: Any time you want to capture a goal, capability, or bundle of functionality that the system delivers to external actors.
- **`UML4SysML::Actor`**: A classifier role external to the system; represents users, other systems, or environmental entities.
  - When to use: Identify every external entity that interacts with the system—users, external systems, hardware, physical environments.
- **`UML4SysML::Association` (Communication path)**: The connection between an actor and a use case, representing the communications and interactions that enable the use case.
  - When to use: Every use case that an actor participates in or triggers.
- **`UML4SysML::include`**: A directed relationship between use cases indicating that the behavior of the included use case is always inserted into (and required for) the including use case.
  - When to use: Factor out common functionality shared among multiple use cases; included behavior is mandatory.
- **`UML4SysML::Extend`**: A directed relationship allowing an extending use case to insert optional, modular behavior increments into a base use case at defined extension points under specified conditions.
  - When to use: Capture optional or variant behavior that augments a base use case without making the base depend on the extension.
- **`UML4SysML::Generalization` (kernel)**: A specialization relationship between use cases; enables a taxonomy of use case variants.
  - When to use: Model alternative behaviors or specialized versions of a base use case.

## Key Concepts
- **System boundary**: The frame (usually a rectangle) that encloses all use cases realized by the subject system; separates internal functionality from external actors.
- **Extension point**: A named location or condition in a base use case where optional behavior from an extending use case may be inserted.
- **Include semantics**: The included use case's behavior is mandatory, required to complete the including use case, and cannot stand alone in that context.
- **Extend semantics**: The extending use case defines optional, supplementary behavior that augments the base use case under specified conditions; the base use case is meaningful independently.
- **Actor specialization**: Actors may be specialized (via generalization) to represent a taxonomy of user types or external system classes.
- **Package organization**: Use cases are organized into packages with explicit dependencies between use cases in different packages, providing implicit traceability mechanisms.

## Mental Models
- **Use Include for mandatory choreography.** If use case B's behavior *must* execute as part of use case A's success criteria, model it as an include relationship. Accelerate, Steer, Brake *include* in Drive the Vehicle because driving is impossible without them.
- **Use Extend for optional enhancements.** If use case B adds optional behavior that triggers only under certain conditions (e.g., "Start the Vehicle" before "Drive the Vehicle" in cold weather), extend is the right choice. The base use case remains meaningful without the extension.
- **Use Generalization for variant families.** If you want to represent different types of the same capability (e.g., "Operate SUV" generalizes to "Operate in Offroad Mode" and "Operate in Street Mode"), generalization captures the family hierarchy.
- **System boundary names define scope.** Name the subject (e.g., "Hybrid SUV System") explicitly in the diagram. Everything inside the boundary is the system; everything outside is actor/environment.

## Anti-patterns
- **Confusing Include and Extend.** Include means mandatory; Extend means optional and conditional. Flipping them obscures whether behavior is required or variant. In many situations they can be *modeled either way* based on perspective—make the semantic choice explicit and document it.
- **Use cases with internal detail.** Use cases describe what the system does from an actor's perspective; they should not prescribe internal implementation (activity diagrams, sequence diagrams, and state machines *realize* use case behavior, not the reverse).
- **Missing extension points.** If you use Extend, always define the extension point(s) in the base use case. Without them, the extension location is ambiguous.
- **Overloading use cases.** Very large, monolithic use cases hide relationships and make dependencies opaque. Break them into smaller, cohesive units and use Include or Generalization to organize them.

## Key Takeaways
1. **Use case diagrams are not workflows.** They capture what the system delivers to actors; sequence diagrams, activity diagrams, and state machines describe how use case behavior is realized internally.
2. **Include is mandatory, Extend is optional.** The distinction directly impacts system behavior and test coverage. Use Include for behaviors required to meet the use case goal; use Extend for optional enhancements that trigger under specific conditions.
3. **Generalization enables capability variants.** When the same use case concept appears in multiple specialized forms (e.g., different user types, different operational modes), generalization organizes them into a family without duplication.
4. **System boundary is part of the specification.** Naming and positioning the subject (system boundary) in the diagram makes scope explicit and prevents ambiguity about what is internal vs. external.
5. **Actors are role-based, not implementation-specific.** An actor represents a role (e.g., "Driver," "Fleet Manager") that may be played by different entity types (human, device, system). Specialize actors to capture taxonomy.
6. **Package hierarchy mirrors use case decomposition.** Organizing use cases into packages with implicit traceability (naming packages after parent use cases) provides a natural organizing principle that complements explicit trace relationships.

## Connects To
- **UML (Use Case model)**: SysML's use case diagram is directly inherited from UML; stereotypes and extensions are minimal. Core semantics (actors, include, extend, generalization) follow UML Superstructure.
- **Activity Diagrams (Chapter 15 in SysML spec)**: Realize use case behavior; activities invoked by use cases show the procedural flow and decision points.
- **Sequence Diagrams (Interactions)**: Complement use cases by showing the temporal and message exchange details between actors and system components.
- **State Machine Diagrams (Chapter 18)**: Capture the event-driven behavior and state transitions that realize use case state-dependent logic.
- **Requirements Diagrams (Chapter 9)**: Use cases often trace to requirements; a requirement may specify that a particular use case must be supported.
- **Allocation and Traceability**: Use cases are allocated to system blocks and behaviors; packages and implicit naming conventions provide traceability hooks.

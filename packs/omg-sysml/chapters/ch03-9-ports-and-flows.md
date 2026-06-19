# Chapter 3: 9 Ports and Flows

## Core Idea
Ports and flows enable modular block design by defining clear, typed boundary interfaces for how blocks connect and exchange materials, energy, data, and services. SysML extends UML ports to support nested ports, interface-typed blocks, and directional flow semantics — allowing a single block to be reused in different contexts with different actual item flows.

## Frameworks Introduced
- **«Port»**: A property with a type that exposes features (operations, receptions, properties, flow properties, and association ends) to external entities via connectors.
  - When to use: When a block needs external interaction points that are more restricted than direct access to the block itself.

- **«ProxyPort»**: A port that exposes features of its owning block or internal parts without specifying a separate system element. Must be typed by an InterfaceBlock.
  - When to use: When port features are actually hosted by the owning block or its nested parts, and you want to surface only a subset of them.

- **«FullPort»**: A port that specifies its own independent system element with its own features, internal parts, and behaviors. Cannot be behavioral or binding-connected to other full ports.
  - When to use: When a port is a separate, standalone component (e.g., a USB port as a separate device).

- **«InterfaceBlock»**: A specialized block type (stereotype of Block) with no behaviors, no internal parts, and no methods. Can own ports that are typed only by other InterfaceBlocks.
  - When to use: As the type for proxy ports, to define a pure feature interface without implementation detail.

- **«FlowProperty»**: A property that specifies a kind of item (data, material, energy) that can flow into, out of, or both ways through a block. Typed by ValueType, Block, or Signal.
  - When to use: To classify the substance/content of flows crossing a port or connector, independent of the usage context.

- **«DirectedFeature»**: A non-flow property or behavioral feature (operation, reception) marked as provided (implemented by owner), required (to be supplied by partner), or both.
  - When to use: To specify contract terms for feature availability across port boundaries.

- **«ItemFlow»**: An information flow (on a connector or association) that specifies what actual items "do" flow in a usage context. Constrains and refines flow properties.
  - When to use: In internal block diagrams (ibd) to label connectors with the concrete items flowing (e.g., "gasoline," "water") versus abstract flow property types.

- **«ChangeStructuralFeatureEvent»**: An event model for changes in structural feature values.
  - When to use: In state machines or activity behaviors to trigger on property mutations.

- **«AcceptChangeStructuralFeatureEventAction»**: An activity action that accepts change structural feature events and outputs the new and old values.
  - When to use: To model behavior reactions to property changes.

- **«AddFlowPropertyValueOnNestedPortAction»**: An activity action that adds values to flow properties and propagates them through specified nested ports.
  - When to use: To model data/energy/material flow initiation in behaviors acting on nested port paths.

- **«InvocationOnNestedPortAction»**: An activity action that sends operation calls or signals out through nested ports.
  - When to use: To model behavior invoking external services through multi-level port hierarchies.

- **«TriggerOnNestedPort»**: A trigger (in state machines) that detects events on nested ports.
  - When to use: To react to external stimuli arriving through proxy ports (nested port paths only).

- **~InterfaceBlock (Conjugated InterfaceBlock)**: A derived InterfaceBlock with inverted DirectedFeature and FlowProperty directions. Tool-generated; semantically used to express role reversal across a connector.
  - When to use: When typing the port on one side of a connector that is typed by an InterfaceBlock on the other side — conjugation swaps provide↔require and in↔out.

## Key Concepts

- **Port**: A boundary point where external entities interact with a block through typed features. Properties can be ports. Ports can be nested (a port on a port). All ports inherit UML port semantics (structural or behavioral identity link to owner) but add flow direction arrows and nested-port paths.

- **Proxy vs. Full**: Proxy ports surface existing features of the owning block or parts (no separate system element); full ports are standalone system elements. Unstereotyped ports do not commit to either—they gain both proxy and full capabilities unless constraints are violated.

- **Nested Ports**: A port typed by a Block (or specialization) that itself owns ports. Represents hierarchical boundary refinement. Proxy ports on proxy ports are constrained to also be proxy. The nesting path is called the "onNestedPort" sequence in activity and state machine contexts.

- **InterfaceBlock**: A Block variant with only features (no behaviors, no internal parts, no methods). Used exclusively as the type for proxy ports. Can own ports (which must also be proxy and typed by InterfaceBlocks).

- **Flow Property**: A property (in or out or inout direction) that characterizes what items can flow through a block. Type-matched with connectors' ItemFlows. "In" flow properties cannot be modified by the owning block; "out" can be modified only by the owner; "inout" both.

- **Directed Feature**: A feature (operation, reception, or non-flow property) marked provided, required, or providedrequired. Feature matching rules enforce type variance for operations (contravariant in, covariant out), type equality for properties, and parameter multiplicity/uniqueness/ordering compatibility.

- **Item Flow**: A label on a connector (or association realization) specifying concrete items flowing (e.g., "fuel: Gasoline") versus abstract flow-property types. Provides looser type matching: target type must be same or more general than source type or ItemFlow classifier.

- **Conjugation (~)**: Swaps provide↔require and in↔out directions in InterfaceBlocks. Automatically applied on the receiving end of a typed port so both ends' ports match. Not manually editable; tools generate it.

- **Interface Compatibility**: Ports match when their features (flow properties by direction & type, directed features by signature and direction variance) align. Matching rules enable automatic connector feasibility checks.

- **Encapsulated Block**: A Block with composite properties that hide internal structure; flow properties on proxy ports behave as if on the owning block (recursively checking internal parts for deeper nested ports).

- **Binding Connector**: A connector that establishes identity between a proxy port and an internal part (or aggregate of parts), or between a full port and another non-full port. Semantically makes the proxy/port values equivalent to the internal part values.

## Mental Models

- **Model a port when you need to hide internal complexity**: Instead of exposing all 30 properties of a block, create a port with 5 flow properties and 3 operations. Typing the port with an InterfaceBlock enforces that encapsulation.

- **Use proxy ports to expose subsets of block or part features**: If you have a transmission block with many internal gears but only want external access to torque flows and RPM, add a proxy port typed by an InterfaceBlock that owns just those properties.

- **Use full ports for standalone, reusable interface hardware**: If modeling a USB port as a separate replaceable component, apply FullPort so it can have its own behavior and internal structure (e.g., a protocol handler).

- **Distinguish flow properties from directed features**: Flow properties describe flowing substance (energy, matter, data streams); directed features (operations, properties) describe services and state. Use both on the same port to model complete I/O contracts.

- **Use conjugation to auto-match port pairs**: When you type one port with `ICE` (interface block) and the other with `~ICE`, SysML inverts directions automatically. No need to manually create "mirror" ports—conjugation handles the matching.

- **Constrain ItemFlows for narrower type compatibility**: A FlowProperty permits "Liquid" to flow; ItemFlow narrows it to "Gasoline" in a particular connector usage. Allows the same block to flow different concrete items in different contexts.

## Anti-patterns

- **Proxy port with internal behaviors or internal parts**: Violates the proxy semantics (proxy ports expose owner features, not their own). Apply FullPort or remove the behaviors/parts.

- **Full port with binding connectors to internal parts**: Full ports are standalone; binding connectors imply identity with owner or parts, breaking full-port independence. Only bind proxy ports to internal parts.

- **Ports typed by Blocks with behaviors**: Proxy ports must be typed by InterfaceBlocks (no behaviors). If you need behavior-rich port types, use full ports instead.

- **Flow properties that are not ValueType, Block, or Signal**: Type checking constrains flow properties to these three kinds. Using any other type violates SysML rules.

- **Ignoring feature direction variance in required/provided matching**: When a required operation's parameter is typed by a subclass, the provided operation's parameter must accept the superclass or supertype (contravariance). Getting this backwards causes interface mismatches.

- **Connecting connectors directly without specifying ItemFlows when types are ambiguous**: If a port can flow multiple specializations of a type, ItemFlow labels clarify which items actually flow. Omitting them leaves the connection semantically underspecified.

## Key Takeaways

1. **Ports are boundaries, not just containers**: A port is a typed property that mediates how external entities interact with a block. It is the only way external blocks see into a block's interface; direct access is architecturally prohibited.

2. **Proxy and full ports are optional but powerful stereotypes**: Unstereotyped ports work fine and carry all proxy/full functionality. Stereotyping them enforces constraints that catch design errors (e.g., behavioral proxy ports, full ports with binding connectors).

3. **InterfaceBlocks are the gold standard for port types**: Use them exclusively as proxy port types. They have no implementations or internal structure—pure feature contracts. This is the only way to separate interface from implementation.

4. **Nested ports represent hierarchical refinement of boundaries**: Port nesting mirrors block nesting. A transmission system's torque port can have nested ports for individual gearboxes. Activity behaviors use onNestedPort sequences to route invocations and data through these hierarchies.

5. **Flow properties enable context-sensitive item typing**: A tank's "fluid in" flow property can be instantiated as gasoline in one context, water in another. ItemFlows narrow the type in specific connectors. This separation of capability from usage is powerful for reuse.

6. **Feature direction matching is not symmetric**: Required and provided features must match according to variance rules (in parameters contravariant, out covariant). Ignoring this causes runtime contract violations. Tools should validate it.

7. **Conjugation (~ operator) is automatic and invisible**: When you type a port with an InterfaceBlock on one end and its conjugate (~) on the other, SysML inverts all directions. You don't create ~InterfaceBlocks manually; tools generate them. It's the standard way to pair complementary interface ports.

## Connects To

- **UML Ports (base definition)**: SysML extends UML ports to support nesting, flow properties, and more general type matching. SysML's proxy/full distinction and interface-block typing are new.

- **Blocks (Clause 8)**: Ports are properties of blocks. Blocks can be typed by ports (nested ports) and blocks can be InterfaceBlocks (feature-only blocks). Binding connectors and association blocks further specialize port composition.

- **Internal Block Diagrams (bdd/ibd)**: Ports appear as rectangles on block or part boundaries (bdd) and are drawn with arrows or labels indicating flow direction. ItemFlows label connectors in ibd to show what actually flows in a specific assembly.

- **Activities (Clause 15 — Allocations, Actions)**: AddFlowPropertyValueOnNestedPortAction, InvocationOnNestedPortAction, and TriggerOnNestedPort extend UML activity semantics to support port paths. Flow allocation ties object nodes to port properties across the model hierarchy.

- **State Machines**: TriggerOnNestedPort enables triggers (event detectors) to receive stimuli from external block interactions via nested ports.

- **Directed Features & Feature Direction Variance**: The matching rules for provided/required features (contravariance in, covariance out) ensure that Liskov Substitution Principle is respected across component boundaries.

- **Conjugated InterfaceBlocks (~InterfaceBlock)**: Essential to the "complementary port" pattern—when two blocks need to interact, one port is typed by an InterfaceBlock, the other by its conjugate. Automatic direction inversion ensures both sides match.

- **ISO/IEC/IEEE 42010 (Architecture Description)**: Ports and flows implement the "interface" and "interaction" aspects of viewpoint definition. An architecture description language (ADL) can use ports to express component interfaces and flows to specify allowed interactions.

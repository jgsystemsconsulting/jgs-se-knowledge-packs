# OMG SysML v1.6 Glossary

**«adjunctProperty»** — Property constrained to hold values of connectors, call actions, object nodes, variables, parameters, or interaction uses; captures execution and token results (Ch 2).
**«allocate»** — Directional dependency (stereotype of UML::Abstraction) associating any two NamedElements across different hierarchies or abstraction levels (Ch 9).
**«allocateActivityPartition»** — Activity-diagram partition representing the supplier (to) end of an allocate relationship, with contained actions as the client (from) end (Ch 9).
**Activity** — Behavior block decomposing system functionality; shown on BDDs and activity diagrams, with instance creation starting it and termination stopping sub-activities (Ch 5).
**Activity diagram (act)** — Diagram type for activities, showing action nodes, object/control flows, and tokens (Ch 5).
**Actor** — Classifier role external to the system, representing users, other systems, or environmental entities (Ch 8).
**Allocation** — Organized cross-association of elements within different structures, supporting behavior, flow, and structure mappings early in design (Ch 9).
**«associationBlock»** — Block stereotype on an Association Class, letting association instances carry their own internal structure and properties (Ch 2).
**Binding connector («bindingConnector»)** — Connector asserting that properties at both ends hold equal values (or same identity), used to bind constraint parameters and proxy ports (Ch 2, Ch 4).
**Block («block»)** — Modular unit describing system structure and behavior via structural and behavioral features; shown on BDDs (Ch 2).
**Block Definition Diagram (bdd)** — Diagram defining blocks, value types, their features, and associations (Ch 2).
**BoundReference** — Reference property using binding connectors to highlight constraint roles of constrained properties (Ch 2).
**CallBehaviorAction** — Action that invokes a behavior (activity, interaction, or state machine) (Ch 5).
**CombinedFragment** — Sequence-diagram frame enclosing a region, labeled with an interaction operator (alt, opt, par, loop, etc.) (Ch 6).
**Composite State** — Hierarchical state containing nested regions that may be sequential or concurrent (Ch 7).
**«Conform»** — Generalization from a View to a Viewpoint, asserting the view adheres to the viewpoint's rules and conventions (Ch 1).
**Conjugated InterfaceBlock (~)** — Derived InterfaceBlock with inverted DirectedFeature and FlowProperty directions, expressing role reversal across a connector (Ch 3).
**Connector** — Relationship between two properties of a block specifying how parts or properties link; binary-only in SysML (Ch 2).
**«connectorProperty»** — Property whose value is the instances of a connector's association-block type (Ch 2).
**Constraint block («constraint»)** — Block packaging constraint parameters and mathematical expressions that constrain properties of other blocks (Ch 4).
**ConstraintProperty** — Property typed by a ConstraintBlock that binds its parameters to properties in the surrounding block (Ch 4).
**ControlFlow** — Activity edge carrying control tokens (Ch 5).
**ControlOperator** — Behavior treating control as data, taking enable/disable ControlValue parameters as regular inputs/outputs (Ch 5).
**Continuous** — Rate subtype for flows where the time increment approaches zero (water, time-continuous signals) (Ch 5).
**«Copy»** — Trace specialization making a slave requirement's text a read-only copy of a master's, enabling reuse across families and projects (Ch 10).
**«DeriveReqt»** — Trace specialization relating a derived (client) requirement to a source (supplier) requirement via analysis decomposition (Ch 10).
**«DirectedFeature»** — Non-flow or behavioral feature marked provided, required, or both (Ch 3).
**Discrete** — Rate subtype for periodic or stepped flows with a non-zero time increment (Ch 5).
**DurationConstraint** — Constraint labeling a message segment with a timing requirement (Ch 6).
**«ElementGroup»** — Lightweight comment stereotype clustering heterogeneous model elements by a modeler-defined criterion, without ownership (Ch 1).
**ExecutionSpecification** — Rectangle on a lifeline indicating active execution by the participant (Ch 6).
**«Expose»** — Dependency from a View to model elements designating entry points for the view's constructor method (Ch 1).
**Extend («Extend»)** — Directed relationship inserting optional, conditional behavior into a base use case at defined extension points (Ch 8).
**Extension point** — Named location in a base use case where extending behavior may be inserted (Ch 8).
**Flow property («FlowProperty»)** — Property specifying an item (data, material, energy) that flows in, out, or both through a block; typed by ValueType, Block, or Signal (Ch 3).
**Full port («FullPort»)** — Port specifying its own independent system element with its own features, parts, and behaviors (Ch 3).
**Generalization** — Specialization relationship enabling a taxonomy of use case (or actor) variants (Ch 8).
**include («include»)** — Directed relationship where the included use case's behavior is always inserted into and required by the including use case (Ch 8).
**InterfaceBlock («InterfaceBlock»)** — Block variant with no behaviors, parts, or methods, used exclusively to type proxy ports (Ch 3).
**Interaction («interaction»)** — Block stereotype modeling executable multi-participant message exchanges, invocable via InteractionUse (Ch 6).
**InteractionUse** — Reference to another interaction by name, semantically equivalent to a call in activities (Ch 6).
**Item flow («ItemFlow»)** — Information flow on a connector specifying what items actually flow in a usage context, refining flow properties (Ch 3).
**Lifeline** — Named entity (block, actor, or part) participating vertically in a sequence diagram, with time flowing downward (Ch 6).
**Message** — Directed communication between two lifelines, labeled with signal name, arguments, and optional return value (Ch 6).
**Metaclass** — UML metamodel class (e.g., Requirement, Block) serving as the extension point for a stereotype (Ch 11).
**Model Library** — Reusable collection of pre-defined blocks, types, requirements, and operations for a domain or system family (Ch 11).
**Namespace** — Scope established by a Package ensuring unique naming and preventing element-name overloading (Ch 1).
**Nested port** — Port typed by a Block that itself owns ports, representing hierarchical boundary refinement (Ch 3).
**NoBuffer** — Object-node stereotype discarding tokens that cannot flow downstream immediately (Ch 5).
**ObjectFlow** — Activity edge carrying object/data tokens of typed classifiers (Ch 5).
**Objective function** — Constraint-block function comparing alternative solutions for trade-off analysis (Ch 4).
**Overwrite** — Object-node stereotype where a new token removes the oldest to ensure fresh data (Ch 5).
**Package** — UML namespace construct partitioning model elements and establishing import/access dependencies (Ch 1).
**Parametric diagram (par)** — Restricted internal block diagram showing constraint properties, the values they constrain, and binding connectors (Ch 4).
**Part property** — Property with composite aggregation, owning one or more instances of its typing block (black diamond) (Ch 2).
**«participantProperty»** — Property of an association block identifying the linked instances at each association end (Ch 2).
**Port («Port»)** — Special property defining allowable interactions at a block boundary by exposing typed features via connectors (Ch 3).
**Probability** — Stereotype specifying the likelihood (0–1) that an outgoing edge or output parameter set is used (Ch 5).
**«Problem»** — Comment stereotype documenting deficiencies, limitations, failures, or undesired outcomes (Ch 1).
**Profile** — UML package grouping stereotypes and metamodel extensions as the container for domain customizations (Ch 11).
**Proxy port («ProxyPort»)** — Port exposing features of its owning block or parts, typed by an InterfaceBlock, with no separate system element (Ch 3).
**PseudoState** — Transient control-flow node (initial, choice, junction, history, fork, final) with no stable residence (Ch 7).
**«Rationale»** — Comment stereotype documenting the justification or decision basis for requirements, designs, or relationships (Ch 1).
**Rate** — Stereotype on activity edges or streaming parameters specifying expected flow rate (items per time) (Ch 5).
**Reference property** — Property without composite aggregation, referring to shared instances (Ch 2).
**«Refine»** — Refinement (with property-path capability) relating a model element to a requirement it refines, or vice versa (Ch 10).
**Region** — Orthogonal decomposition of a composite state modeling concurrent substates (Ch 7).
**Requirement («requirement»)** — Class stereotype specifying a capability, condition, function, or performance criterion, with unique id and text (Ch 10).
**Requirement diagram (req)** — Diagram displaying requirements, test cases, rationale, and relationships (derive, satisfy, verify, refine, copy, trace) (Ch 10).
**«Satisfy»** — Trace specialization linking a design/implementation element to the requirement it fulfills (Ch 10).
**Sequence diagram (seq)** — SysML's primary interaction diagram showing lifelines, messages, executions, and combined fragments (Ch 6).
**Stakeholder («Stakeholder»)** — Classifier representing a role, group, or individual whose concerns are addressed by a View (Ch 1).
**State** — Stable condition in which an object can exist; may have entry, exit, and do activities (Ch 7).
**State machine** — Behavioral classifier modeling object state history through finite, event-triggered, guarded transitions (Ch 7).
**State machine diagram (stm)** — Graphical representation of state machine structure and transitions (Ch 7).
**StateInvariant** — Constraint that must hold at a point on a lifeline, labeling a block's expected state (Ch 6).
**Stereotype** — Metaclass extension specializing a UML construct via «name» notation without structural subclassing (Ch 11).
**Submachine State** — State whose behavior is specified by reference to another state machine (Ch 7).
**System boundary** — Frame enclosing all use cases realized by the subject system, separating internal function from external actors (Ch 8).
**«TestCase»** — Stereotype of Behavior or Operation that verifies a requirement, returning a VerdictKind value (Ch 10).
**TimeConstraint** — Constraint labeling a point on a lifeline with a timing requirement (Ch 6).
**«Trace»** — General-purpose, weak-semantics relationship between a requirement and any model element, used only when no specific relationship applies (Ch 10).
**Transition** — Directed edge changing state, optionally triggered by an event, guarded by a condition, and executing actions (Ch 7).
**Use case (UseCase)** — Specification of a service or capability realized by the system, shown as a named oval inside the boundary (Ch 8).
**Value property** — Property typed by a ValueType, always with composite aggregation (Ch 2).
**Value type («valueType»)** — Classifier for value entities not identified by reference (typed by DataType); may carry units and quantity kinds (Ch 2).
**«Verify»** — Trace specialization linking a test case or element to a requirement whose satisfaction it verifies (Ch 10).
**View («View»)** — Model element representing an artifact (document, table, diagram) generated by querying models per a viewpoint's method (Ch 1).
**Viewpoint («Viewpoint»)** — ISO 42010 specification of conventions, rules, and methods for constructing views to address stakeholder concerns (Ch 1).

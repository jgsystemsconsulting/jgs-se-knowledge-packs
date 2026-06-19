# OMG SysML v1.6 Patterns & Techniques

## Define system structure with Blocks on a BDD
**When to use**: Establishing the system breakdown — what things exist and how they decompose.
**How**: Model each element as a «block» on a Block Definition Diagram. Use *part properties* (composite, black diamond) for owned subparts, *reference properties* for shared elements, *value properties* (typed by ValueType) for quantities. Nest across multiple levels.
**Trade-offs**: Keep composition acyclic (no part-of cycles). Avoid flat one-level decompositions; leverage nesting and property paths for reuse. Show non-default multiplicities explicitly.

## Show internal structure with parts + connectors on an IBD
**When to use**: Specifying how a block's parts are arranged and wired internally.
**How**: On an Internal Block Diagram, place part properties as nested boxes and link them with connectors (default multiplicity 1 each end). Use `initialValues` (context-specific values) to override type defaults for a usage context.
**Trade-offs**: Prefer intermediate properties at each containment level over deep nested connector ends — encapsulation reflects design intent, not just black-box syntax.

## Proxy vs. full ports
**When to use**: Defining interaction points on a block boundary.
**How**: Use a «ProxyPort» (typed by an InterfaceBlock) to expose existing features of the owner or internal parts; bind it to internal parts. Use a «FullPort» when the boundary is its own system element with own parts/behaviors.
**Trade-offs**: Proxy ports must not have internal behaviors/parts; full ports must not bind to internal parts. Unstereotyped ports get both capabilities — commit explicitly when semantics matter.

## Model item flows with flow properties + ItemFlows
**When to use**: Representing matter/energy/data crossing interfaces.
**How**: Declare «FlowProperty» (in/out/inout, typed by ValueType, Block, or Signal) on port types. On the connector, label an «ItemFlow» (e.g. `fuel: Gasoline`) to state what actually flows.
**Trade-offs**: Flow properties must be ValueType/Block/Signal only. Add ItemFlow labels whenever a port can carry multiple specializations, else the connection is underspecified.

## Define interfaces with InterfaceBlocks + conjugation
**When to use**: Specifying a reusable, behavior-free interface contract for proxy ports.
**How**: Define an «InterfaceBlock» (no behaviors, parts, or methods) holding flow properties and «DirectedFeature»s (provided/required). Use the conjugate (~InterfaceBlock) on the matching end so directions invert automatically.
**Trade-offs**: Conjugation is tool-generated, not hand-edited. Respect feature variance (operations contravariant-in/covariant-out) or interfaces won't match.

## Parametric constraints with ConstraintBlocks on a par diagram
**When to use**: Capturing equations/analysis relationships (performance, mass, cost) over system values.
**How**: Define a «constraint» block with constraint parameters and expressions. Hold it as a ConstraintProperty (composite) in the owning block; on a Parametric Diagram, bind parameters to value properties via binding connectors. Nest constraint blocks for complex relations; add objective functions for trade studies.
**Trade-offs**: Constraints are non-causal — don't assume fixed input/output roles. Constraint blocks hold only parameters/expressions/bindings, no behavior. Every constraint-typed property must be composite.

## Value types with units and quantity kinds
**When to use**: Typing physical/measured quantities consistently.
**How**: Define «valueType»s on a BDD, associating a Unit and QuantityKind (VIM concepts) from a model library. Reuse across value and constraint properties.
**Trade-offs**: Equivalence is determined by `definitionURI`, not name — align libraries to avoid silent mismatches.

## Requirements modelling with satisfy/verify/derive traceability
**When to use**: Linking text requirements to design and tests.
**How**: Create «requirement»s (unique `id` + `text`) on a Requirement Diagram. Trace with «Satisfy» (design element → requirement), «Verify» (test case → requirement), «DeriveReqt» (analysis-decomposed child → source), «Refine» (model refines text), «Copy» (reuse master/slave). Nest sub-requirements for hierarchy.
**Trade-offs**: Satisfy ≠ Verify — a complete chain needs both. Avoid weak «Trace» when a specific relationship applies. Requirements can't be types, generalize, or hold associations.

## Verify requirements with TestCases and VerdictKind
**When to use**: Recording how each requirement is checked.
**How**: Stereotype a Behavior/Operation as «TestCase» with a VerdictKind return; link via «Verify». Capture method (inspection/analysis/demonstration/test) and track the verdict.
**Trade-offs**: A Verify link without an actual test case/method is hollow traceability.

## Allocate function to structure (and flows) with «allocate»
**When to use**: Mapping behavior onto components, or activity flows onto connectors.
**How**: Draw an «allocate» dependency (client→supplier) between any NamedElements across hierarchies. For functional-to-structural, use «allocateActivityPartition» swimlanes; show allocated-from/to compartments with type keywords and qualified names.
**Trade-offs**: AllocateActivityPartition keeps partition structure but NOT responsibility semantics — the classifier doesn't invoke the partition's actions. v1.6 has no Pin-to-Port allocation; allocate ObjectNode/ObjectFlow instead.

## Model functional behavior with Activities
**When to use**: Specifying flow-based functions, transformations, and pipelines.
**How**: Use an Activity on an act diagram; ObjectFlows carry data tokens, ControlFlows carry control. Type object nodes/pins by blocks/value types. Apply «rate» (Continuous/Discrete) for throughput; treat control as data via «ControlOperator» + ControlValue.
**Trade-offs**: Pair «rate» with «nobuffer» or «overwrite» on fast inputs to avoid stale-data accumulation. If «probability» is on one outgoing edge, all sibling edges need it. Streaming parameters require a rate.

## Model state-dependent behavior with State Machines
**When to use**: An element's response depends on its current mode/condition.
**How**: Build a behavior State Machine: states (with entry/do/exit activities), event-triggered guarded transitions, composite states, and orthogonal regions for concurrency. Use submachine states for reuse; pseudostates (initial/choice/junction/history/final) for control flow.
**Trade-offs**: Don't encode substates via guards — model them as real states/regions. Use orthogonal regions for genuinely concurrent behavior. Protocol state machines are excluded in SysML.

## Model interaction scenarios with Sequence Diagrams
**When to use**: Showing message exchange order between participants for a scenario.
**How**: Use a seq diagram with lifelines, messages (named signals/operations), execution specs, and CombinedFragments (alt/opt/par/loop/strict/critical/neg/assert…). Decompose lifelines via InteractionUse; attach Duration/TimeConstraints for timing.
**Trade-offs**: Y-position is logical order, not wall-clock timing — use Duration/TimeConstraint for that. Move heavy in-lifeline logic to a state machine. Choose `par` vs `seq` deliberately.

## Capture system services with Use Cases
**When to use**: Framing what the system does for external actors at a high level.
**How**: Draw use cases (ovals) inside the system boundary, actors outside, communication associations between them. Use «include» for mandatory shared behavior, «extend» (with extension points) for optional/conditional behavior, generalization for variants.
**Trade-offs**: Include = mandatory, Extend = optional — keep the choice explicit. Always define extension points when extending. Don't embed internal implementation; activities/state machines realize use cases.

## Make value invariants explicit with binding connectors
**When to use**: Asserting two properties (or a proxy port and a part) must hold equal values/identity.
**How**: Add a «bindingConnector» between the two ends; use BoundReference to surface constrained roles. Follow property paths for nested ends.
**Trade-offs**: Powerful but reduce readability — reserve for critical invariants and annotate purpose in notes.

## Extend SysML for a domain with Profiles and stereotypes
**When to use**: Adding domain-specific element kinds (e.g. functionalRequirement, safetyBlock).
**How**: In a Profile package, define «Stereotype»s extending the relevant Metaclass (Requirement, Block, Operation…) via Extension; give them properties and constraints. Apply with `«stereotypeName»`.
**Trade-offs**: Prefer orthogonal stereotypes over deep subclass hierarchies — they compose flexibly. Encode and enforce stereotype constraints, or they're cosmetic.

## Package reusable assets as Model Libraries
**When to use**: Sharing standard blocks, value types, units, or requirement sets across projects.
**How**: Collect curated, documented, version-controlled definitions in a Model Library package; projects import and specialize/instantiate them.
**Trade-offs**: Curate and document — uncurated libraries bloat into hundreds of purposeless templates. SysML omits UML package «merge»; use «Refine» to extend definitions.

## Organize models with Packages, Views, and Viewpoints
**When to use**: Partitioning a large model and generating stakeholder-facing artifacts.
**How**: Use Packages (with public/private imports) for namespaces. Define a «Viewpoint» (ISO 42010: concerns, stakeholders, language, method); build a «View» that «Conform»s to it and «Expose»s root elements to query. Annotate decisions with «Rationale», issues with «Problem», ad-hoc clusters with «ElementGroup».
**Trade-offs**: Never create a View without a conforming Viewpoint — it's an orphan artifact. Give ElementGroups a clear membership criterion. Use the «Rationale» stereotype (queryable), not a plain comment.

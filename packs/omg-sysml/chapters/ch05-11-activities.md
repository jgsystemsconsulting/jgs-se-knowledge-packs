# Chapter 5: 11 Activities

## Core Idea
Activities model the sequences, inputs, outputs, and control conditions that coordinate system behaviors. SysML extends UML activity diagrams to support continuous flows (e.g. energy, material, information), control as data, probability, and hierarchical decomposition of system behaviors as blocks.

## Frameworks Introduced
- **Activity**: Behavior block that decomposes system functionality; appears on block definition diagrams (BDD) and activity diagrams (act). Instance creation starts the activity; termination stops all invoked sub-activities.
  - When to use: To decompose a system function into controlled sequences of sub-actions with explicit inputs, outputs, and timing.
- **CallBehaviorAction**: Action that invokes a behavior (activity, interaction, or state machine). May appear with stereotypes of the invoked behavior and optional name colon notation.
  - When to use: To compose behaviors or invoke sub-activities from a parent activity diagram.
- **ControlOperator**: Behavior stereotype for complex logical operators that treat control as data, taking `ControlValue` parameters (enable/disable) as regular data inputs/outputs rather than UML control pins.
  - When to use: To model enable/disable logic that depends on data values, not just control flow topology.
- **Rate**: Stereotype applied to activity edges or streaming parameters; specifies expected flow rate (items per time interval). Specialized as **Continuous** (time increment → 0) and **Discrete** (non-zero time increment).
  - When to use: To quantify throughput in material/energy/information flows; e.g. water flow, signal rates, assembly production rates.
- **Continuous** / **Discrete**: Rate subtypes. Continuous models flows where time steps approach zero (water, time-continuous signals). Discrete models periodic or stepped flows (factory production, periodic signals).
  - When to use: To distinguish between perpetual/analog flows and step-wise/periodic flows in the same model.
- **Overwrite**: Object node stereotype; new arriving token removes the oldest one (FIFO on upper bound > 1) to ensure fresh data, preventing stale values in input pins.
  - When to use: To force input pins to hold only the most recent value (e.g. sensor readings overriding old data).
- **NoBuffer**: Object node stereotype; tokens are discarded if they cannot flow downstream immediately (refused by outgoing edges). Prevents buffer accumulation in fast/continuous flows.
  - When to use: To model transient values (electrical signals) or prevent overflow in fast data streams.
- **Optional**: Parameter stereotype; marks a parameter with multiplicity lower bound = 0, meaning it is not required for behavior start/stop.
  - When to use: To declare that a behavior can begin/end without this parameter being populated.
- **Probability**: Stereotype on activity edges (from decision/object nodes) or output parameter sets; specifies likelihood (0 to 1) that the edge or parameter set is traversed/used. All outgoing edges from the same source must have probability applied.
  - When to use: To model stochastic branching or multi-output parameter set likelihood in reliability or failure analysis.
- **ControlValueKind**: Enumeration type for control values. Literals: `enable` (start new execution), `disable` (terminate and require restart). User-extensible.
  - When to use: As the type of parameters, pins, or attributes that carry control signals as regular data.
- **ControlFlow**: Activity edge for control tokens; may be notated with dashed line and stick arrowhead (alternative to solid line).
  - When to use: Standard control-sequence notation; optional dashing clarifies control vs. object flow.
- **ObjectFlow**: Activity edge for object/data tokens; carries values of typed classifiers.
  - When to use: Default for data and material flows.
- **Portability**: Stereotype on activity edges; indicates the edge can carry different token types at runtime.
  - When to use: Rarely used; for highly polymorphic flows.
- **ParameterSet**: Grouping of behavior parameters with associated probabilities for output combinations.
  - When to use: To model multiple valid output combinations with independent probabilities.

## Key Concepts
- **Control as Data**: SysML treats control values (enable, disable) as regular data flowing through pins, not as UML control tokens. A `ControlOperator` behavior transforms inputs to produce enable/disable outputs that act on downstream actions.
- **Streaming Parameter**: UML characteristic allowing behavior parameters to receive/emit data while executing, not just at start/stop. Required for rate stereotypes.
- **Composition Between Activities**: When activity A invokes activity B with composition, termination of A's execution terminates B's execution. Upper multiplicity on the part end restricts concurrent synchronous invocations.
- **Object Node with Type**: Object nodes and pins can be typed by blocks or value types; associations in BDD link activities to these types, supporting traceability of flowing items.
- **Rate of Flow**: Unified treatment of discrete (non-zero time step) and continuous (infinitesimal time step) flows; includes material, energy, and information with quantified throughput per time unit.
- **Token Offering Semantics**: When `nobuffer` or `overwrite` is applied, behavior changes what happens to tokens after refusal (discard vs. keep); does not override UML token selection order.
- **Time Constraints on Actions**: Duration constraints from UML simple time model can constrain action execution (e.g. "Turn Key On ≤ 0.1 sec").

## Mental Models
- **Hierarchical Decomposition**: Model system behavior as a tree: top-level Activity (e.g. Operate Car) contains CallBehaviorActions invoking sub-activities (Driving, Braking). Block definition diagrams show this hierarchy with composition and AdjunctProperty; activity diagrams show the detailed flow.
- **Continuous vs. Discrete Flows**: Use `«continuous»` for analog phenomena (pressure, current, temperature) and `«discrete»` for counted items (assembly count) or periodic signals. Rate expressions must use time denominators (e.g. "5 items/sec").
- **Control Logic as Behavior**: Rather than hardcoding control paths, model control decision logic as a dedicated `«controlOperator»` behavior that takes data inputs (brake pressure) and outputs enable/disable tokens as regular data.
- **Pin Overwrite for Sensor Fusion**: Apply `«overwrite»` to input pins holding the latest sensor reading, ensuring stale values do not block downstream computation. Pair with rate constraints to enforce sampling rates.

## Anti-patterns
- **Mixing Control Pin and ControlValue Parameter**: Do not apply `«controlOperator»` to a behavior and also use UML control pins (isControl=true). If control is data (treated as a value), use `ControlValue` parameters; if control is topology-driven, use UML control pins—not both.
- **Unbounded Buffer on Fast Flows**: Applying `«rate»` without `«nobuffer»` or `«overwrite»` to a fast/continuous input pin risks token accumulation and stale-data bugs. Pair rate with one of the buffer stereotypes.
- **Probability Without Complete Coverage**: If `«probability»` is applied to any edge leaving a decision node, ALL outgoing edges from that node must have probability; missing probabilities are a consistency violation.
- **Streaming Parameter Without Rate**: A streaming parameter without `«rate»` is undefined in throughput. If streaming, add rate stereotype with quantified flow (e.g. "25 messages/sec").

## Key Takeaways
1. **Activities are blocks**: They can own properties, participate in composition, and be associated with the types they process. Use block definition diagrams to show structural relationships and activity diagrams for flow detail.
2. **Control as data unlocks logic modeling**: Dedicate a `«controlOperator»` behavior to complex enable/disable decisions instead of embedding them in control flow topology. This separates decision logic from sequencing.
3. **Rate constraints are quantitative requirements**: Apply `«rate»` (and specialize as `«continuous»` or `«discrete»`) to edges and streaming parameters to express throughput. Time denominators are mandatory.
4. **Buffer stereotypes prevent data pathologies**: `«overwrite»` keeps pins fresh; `«nobuffer»` discards stale tokens. Choose based on whether you need the latest value (overwrite) or real-time streaming (nobuffer).
5. **Probability enables stochastic analysis**: Use `«probability»` on decision branches or output parameter sets to quantify branching likelihood. Requires complete coverage of all outgoing paths.
6. **Composition + Activity = Lifecycle Coupling**: When activity A owns activity B via composition, destroying A kills B. Model this intentionally: synchronous invocation (child behavior lifetime ⊆ parent) uses composition; asynchronous uses association.
7. **Parameters and multiplicity drive execution semantics**: Lower bound > 0 = required (blocks start until present); lower bound = 0 (with `«optional»`) = optional (behavior starts without waiting). Use to model early-exit flows.

## Connects To
- **UML 2.5 Activity Metamodel** (UML4SysML::Action, UML4SysML::Activity, etc.): SysML stereotypes extend UML Activity metaclasses; these are the base metamodel for all activity constructs.
- **Clause 8: Blocks** (AdjunctProperty, Block stereotype): Activities appear as blocks on BDD and may own AdjunctProperty instances for composition and association typing.
- **Clause 10: Constraint Blocks**: Constraint blocks can specify resource constraints and timing bounds on activity parameters, inputs, and outputs (e.g. duration constraints on actions).
- **ISO/IEC 42010 (IEEE 1471)**: Activity decomposition and control/data flow views align with the viewpoint vocabulary for architecture documentation (functional, temporal, information flow viewpoints).
- **UML Simple Time Model**: Basis for duration constraints on actions (e.g. DurationConstraint, Duration, DurationInterval).
- **SysML Libraries (Clause 11.3.3)**: ControlValueKind enumeration and other predefined types (e.g. Continuous, Discrete rate specializations) reside in the SysML model libraries.

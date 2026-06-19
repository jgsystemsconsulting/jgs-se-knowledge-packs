# OMG SysML v1.6 Cheatsheet

## Construct-selection decision rules
- **Need to model structure / a system element?** → `«block»` on a **bdd**. Its parts/values/refs become the type's features.
- **Need to show how parts connect internally?** → drop the block's parts on an **ibd** and wire them with **connectors** (typed by associations or binding).
- **Need an equation / constraint / analysis (mass = …, MoE, trade study)?** → `«constraint»` block, instantiate as a **ConstraintProperty**, bind parameters on a **par** diagram. Never put behavior in it.
- **Need a measurable value with units?** → `«valueType»` (carries QuantityKind + Unit), used as a **value property**.
- **Need a stated capability/condition the system must meet?** → `«requirement»` on a **req** diagram; nest sub-requirements, don't flatten.
- **Need step-by-step function / flow of tokens?** → **Activity** on an **act** diagram. **Need message exchange between participants over time?** → **Interaction** on a **seq**. **Need state-driven, event-triggered behavior?** → **State Machine** on an **stm**.
- **Need actor-facing system capability (scope, not internals)?** → `UseCase` on a **uc**; realize it later with act/seq/stm.
- **Need to map function→form or logical→physical across hierarchies?** → `«allocate»` (directional: client = from, supplier = to).
- **Need a stakeholder-facing artifact (doc/table/slides)?** → `«View»` that **«Conform»**s to a `«Viewpoint»` and **«Expose»**s root elements. No view without a viewpoint.
- **Need to capture a design justification?** → `«Rationale»` stereotype (queryable), not a plain comment. **A defect/limitation?** → `«Problem»`.
- **Need a domain dialect (e.g. functionalRequirement)?** → a `Stereotype` in a `Profile`, *not* a subclass. Stereotypes compose; subclasses lock a rigid hierarchy.

## Diagram taxonomy (9 types)
| Dgm | Shows | Reach for it when… |
|----|----|----|
| **bdd** | Blocks, value/constraint types, associations, generalization | Defining the *catalog* of types and decomposition |
| **ibd** | Parts, ports, connectors, item flows | Showing *one block's* internal wiring/usage |
| **par** | Constraint props + bound value props (binding only) | Hooking equations to properties for analysis |
| **req** | Requirements, test cases, derive/satisfy/verify paths | Capturing + tracing requirements |
| **pkg** | Packages, import/access dependencies | Organizing namespaces, model partitioning |
| **act** | Actions, object/control flows, rates, buffers | Functional flow, transformation, throughput |
| **seq** | Lifelines, messages, fragments, time constraints | Multi-party message ordering / scenarios |
| **stm** | States, transitions, pseudostates, regions | Event-driven lifecycle / mode logic |
| **uc** | Actors, use cases, include/extend, boundary | Black-box scope from the actor's view |

## Port decision guide
- **Proxy port** → exposes the owner's (or its parts') existing features; **must be typed by an `InterfaceBlock`** (no behavior, no parts, no methods). Default choice for interface contracts. Can be bound to an internal part.
- **Full port** → a *standalone* element with its own features/parts/behavior. Use when the boundary itself is a real component. **Cannot** be binding-connected to internal parts (that would break its independence).
- **Unstereotyped port** → gains both capabilities until a constraint is violated; leave undecided only deliberately.
- **Flow property** (on a port/block) → typed only by **ValueType, Block, or Signal**; pick direction `in`/`out`/`inout`. Pair with **ItemFlow** on the connector when multiple item subtypes could flow.
- **Directed feature** → an operation/property marked provided / required / both; matching uses contravariant inputs, covariant outputs. Conjugation (`~`) auto-flips directions on the receiving end.

## Property type guide
| Type | Aggregation | Use when… | BDD/IBD tell |
|----|----|----|----|
| **Part** | composite (owns) | the instance *is part of* the whole, one owner at a time | black diamond |
| **Reference** | none (shares) | you point at an instance owned elsewhere | dashed outline (IBD) |
| **Value** | composite (always) | a quantifiable attribute typed by a ValueType | value compartment |
| **Constraint** | composite (must) | the property holds a ConstraintBlock usage | par diagram only |

## Requirements traceability — pick the relationship
| Relationship | From → To | Use when… |
|----|----|----|
| **Satisfy** | design element → requirement | a block/behavior *implements* it |
| **Verify** | test case → requirement | a TestCase (VerdictKind) *proves* it |
| **DeriveReqt** | derived req → source req | analysis decomposes a higher-level req |
| **Refine** | model element ↔ requirement | text req is elaborated into a model (or vice versa) |
| **Copy** | slave → master | read-only reuse across families/projects |
| **Trace** | requirement ↔ anything | *last resort* — weak semantics, no constraints |

Rule: a complete chain needs **both** Satisfy *and* Verify. Don't use Trace where a specific one fits.

## Tells & smells
- View with no Viewpoint → orphan artifact. ElementGroup with "TBD/misc" criterion → useless for traceability.
- Plain comment saying "rationale" instead of `«Rationale»` → not queryable.
- Non-default multiplicities left implicit → reader ambiguity; always show them.
- Proxy port carrying its own parts/behavior, or full port bound to internal parts → wrong port kind.
- Flow property typed by something other than ValueType/Block/Signal → rule violation.
- `«rate»` on a fast pin without `«nobuffer»`/`«overwrite»` → stale-data bug. `«probability»` on one decision edge but not all → consistency violation.
- y-position on a seq read as wall-clock time → use DurationConstraint/TimeConstraint instead.
- Constraint block holding states/operations → illegal; constraints hold only parameters + expressions, and every constraint property must be composite.
- Requirement used as a type / in an association / generalized → forbidden; separate the block and link via Satisfy.
- Confusing Include (mandatory) with Extend (optional+conditional); Extend without an extension point.
- Using `«merge»` to combine packages → SysML drops it; use `«Refine»`.
- Deep requirement-type subclass tree where orthogonal stereotypes would do.

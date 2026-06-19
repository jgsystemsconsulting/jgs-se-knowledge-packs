---
name: omg-sysml
description: "Knowledge base from the OMG Systems Modeling Language (SysML) v1.6 specification. Use for SysML modelling constructs and notation — blocks, parts, ports and item flows, constraint blocks and parametrics, activities, interactions, state machines, use cases, allocations, requirements and their traceability (satisfy/verify/derive), and profiles/model libraries — across the nine SysML diagram types (bdd, ibd, par, req, pkg, act, seq, stm, uc). Strong for how to model a system in SysML; it is the v1.x notation, not SysML v2, and not a methodology."
---

<!-- argument-hint: [construct, stereotype, diagram type, or chapter number] -->

# OMG Systems Modeling Language (SysML) v1.6
**Source**: Object Management Group (OMG) | **Specification**: SysML v1.6 (formal/2019-11-01) | **Pages**: ~398 | **Chapters**: 11 normative clauses | **Licence**: OMG Specification License

## When to use

Use this pack when you need to know **how to model something in SysML**: which construct, stereotype, and diagram to use for blocks and structure, internal connections via ports and item flows, parametric constraints, behaviour (activities, interactions, state machines, use cases), allocations, requirements and their traceability, and domain extension via profiles. Strong as a SysML **notation reference**. It is **SysML v1.6**, not SysML v2, and it is a language spec — not a modelling *methodology* (pair with SEBoK/NASA for process).

**Prerequisites:** none — this pack is plain Markdown; no MCP server, API key, or licence tier is needed at runtime. Familiarity with basic UML helps (SysML extends UML).

## How to Use This Skill

- **Without arguments** — load the construct/diagram overview below.
- **With a topic** — ask about `proxy vs full port`, `parametrics`, `requirement traceability`, `allocation`, or another construct; I read the relevant clause.
- **With a chapter** — ask for `ch02` to load Blocks.
- **Browse** — ask "what chapters do you have?" for the clause index.

Supporting files: `glossary.md` (82 terms), `patterns.md` (19 modelling patterns), `cheatsheet.md` (construct-selection rules, 9-diagram taxonomy, port/property/traceability guides).

## Core Frameworks & Mental Models

**Blocks are the unit of structure (Ch 2).** A **«block»** defines structural features (part, reference, value, constraint properties) and behavioural features (operations). **Part** properties model composition (owns instances), **reference** properties model shared associations, **value** properties are typed by **«valueType»** (with units and quantity kinds). Blocks appear on **Block Definition Diagrams (bdd)**; their internal structure on **Internal Block Diagrams (ibd)**.

**Ports and flows connect parts (Ch 3).** Ports are interaction points on blocks/parts. **Proxy ports** («proxy») expose features of their owner without behaviour; **full ports** («full») have their own behaviour/state. **Item flows** and **flow properties** model what flows across connectors (matter, energy, data).

**Parametrics capture constraints (Ch 4).** A **ConstraintBlock** packages equations/inequalities as a reusable «constraint»; constraint properties bind to value properties on a **Parametric Diagram (par)** to model analysis (e.g. mass rollup, performance).

**Behaviour: four complementary views (Ch 5–8).** **Activities (act)** for flow-based behaviour and token flow; **Interactions/Sequence (seq)** for message exchange over time; **State Machines (stm)** for state-dependent behaviour; **Use Cases (uc)** for required capabilities and actors.

**Allocations cross the structure/behaviour divide (Ch 9).** **«allocate»** maps elements across domains — function-to-component, logical-to-physical, behaviour-to-structure — recording intent before detailed design binds it.

**Requirements are first-class and traceable (Ch 10).** A **«requirement»** is a text-based model element related to the design by **«satisfy»** (a structural element meets it), **«verify»** (a test case confirms it), **«deriveReqt»** (a requirement is derived from another), plus **«refine»**, **«trace»**, **«copy»**. Shown on **Requirement Diagrams (req)**; this is the backbone of model-based traceability.

**Profiles extend the language (Ch 11).** **Profiles**, **stereotypes**, and **model libraries** let you tailor SysML to a domain without changing the metamodel.

## Chapter Index

| # | SysML clause | Key constructs |
|---|--------------|----------------|
| [ch01](chapters/ch01-7-model-elements.md) | 7 Model Elements | «Conform», «ElementGroup», «View»/«Viewpoint», comments |
| [ch02](chapters/ch02-8-blocks.md) | 8 Blocks | «block», «valueType», part/reference/value properties |
| [ch03](chapters/ch03-9-ports-and-flows.md) | 9 Ports and Flows | «ProxyPort», «FullPort», item flows, flow properties |
| [ch04](chapters/ch04-10-constraint-blocks.md) | 10 Constraint Blocks | ConstraintBlock, parametric diagram (par) |
| [ch05](chapters/ch05-11-activities.md) | 11 Activities | Activity, actions, control/object flow |
| [ch06](chapters/ch06-12-interactions.md) | 12 Interactions | Sequence diagram, lifelines, messages |
| [ch07](chapters/ch07-13-state-machines.md) | 13 State Machines | states, transitions, composite states |
| [ch08](chapters/ch08-14-use-cases.md) | 14 Use Cases | use case, actor, associations |
| [ch09](chapters/ch09-15-allocations.md) | 15 Allocations | «allocate», allocate activity partition |
| [ch10](chapters/ch10-16-requirements.md) | 16 Requirements | «requirement», satisfy/verify/derive/refine/trace/copy |
| [ch11](chapters/ch11-17-profiles-and-model-libraries.md) | 17 Profiles & Model Libraries | stereotype, profile, model library |

## Topic Index

- **Blocks / structure / properties** → ch02
- **Internal structure / ibd** → ch02, ch03
- **Ports (proxy vs full) / flows / interfaces** → ch03
- **Value types / units / quantity kinds** → ch02
- **Parametrics / constraint blocks / analysis** → ch04
- **Activities / behaviour flow** → ch05
- **Sequence diagrams / interactions** → ch06
- **State machines** → ch07
- **Use cases / actors** → ch08
- **Allocation (functional↔physical)** → ch09
- **Requirements / traceability (satisfy/verify/derive)** → ch10
- **Profiles / stereotypes / model libraries / domain extension** → ch11
- **Views & viewpoints (42010)** → ch01
- **Diagram types (bdd/ibd/par/req/act/seq/stm/uc)** → cheatsheet, ch02–ch11

## Supporting Files

- [glossary.md](glossary.md) — 82 SysML terms and stereotypes with chapter refs
- [patterns.md](patterns.md) — 19 modelling patterns (structure, ports/flows, parametrics, requirements traceability, allocation, behaviour)
- [cheatsheet.md](cheatsheet.md) — construct-selection rules, 9-diagram taxonomy, port/property/traceability decision guides

---

## Scope & Limits

This pack covers the **OMG SysML v1.6 specification** only. It is the **modelling language** (notation, constructs, semantics) — **not** SysML v2 (a separate, newer language with different syntax and an API), and **not** a modelling methodology or tool guide (use SEBoK/NASA for SE process). Diagrams in the source are described in prose; the pack captures construct names, semantics, and usage rather than reproducing figures. Source under the OMG Specification License (Tier 2): redistribution and derivative works are permitted with attribution; this pack is a transformed reference, not the normative specification.

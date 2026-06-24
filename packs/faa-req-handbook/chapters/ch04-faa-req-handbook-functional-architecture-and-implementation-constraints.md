# Chapter — Develop the Functional Architecture and Revise it for Implementation Constraints

> Scope note: This chapter synthesizes recommended practices 2.5 (Develop the Functional Architecture) and 2.6 (Revise the Architecture to Meet Implementation Constraints) from the FAA requirements handbook. The handbook carries an embedded and real-time systems slant — its worked examples are an Isolette infant-incubator thermostat and a flight-control system, and its safety reasoning is tied to commercial avionics practice — so the architecture moves described here are explicitly in service of writing readable, change-tolerant, safety-driven requirements, not in service of a software build. Read it as a complement to the requirements-writing material rather than as a standalone design method.

## Core Idea

A requirements specification of any real size cannot be a flat list. The handbook's central move in this stage is to organize the requirements around a **functional architecture**: a recursive grouping of system functions, with the data each function depends on flowing between them. The grouping principle is deliberately chosen to make the document survive change — functions that are closely related and likely to change together are placed together, so that when something changes, the disruption is contained rather than rippling across the whole specification.

The handbook is careful to separate two things. First, in 2.5, you build an **ideal functional architecture** purely from analysis of the problem domain, ignoring how the system will actually be built. This logical structure is the cleanest possible organization of the requirements. Second, in 2.6, you accept that reality intrudes — components fail with safety consequences, legacy systems must be integrated, and platform constraints bite — and you **revise** that ideal structure into a final architecture that absorbs those constraints. The revised architecture, not the ideal one, becomes the framework for the detailed requirements. The discipline of the second step is to bend the ideal architecture as little as possible, because the problem domain is more stable than any particular implementation.

## Frameworks Introduced (exact source names, when/how)

- **Dependency diagram** — introduced in 2.5.2 as the recommended graphical depiction of system functions and their dependencies. It "opens up the black box" of the context diagram to show the major functions and how they relate. Monitored variables appear as arrows that originate outside any function; controlled variables as arrows that terminate outside any function; and data dependencies between functions as arrows that both originate and terminate at functions. The handbook notes a deliberate convention compromise: the true dependency runs opposite to the drawn arrow (a function that consumes a value depends on the function that defines it), but the arrows are drawn in the direction of data flow because that matches accepted data-flow-diagram practice and is far more readily accepted in practice.

- **CoRE methodology** (Consortium Requirements Engineering) — cited as the prior art whose organizing principles this stage closely follows. The handbook notes that CoRE, like classic structured analysis with data flow diagrams, placed the detailed system requirements in the lowest-level functions — a pattern this handbook carries forward.

- **Monitored / controlled / internal variables** — the variable vocabulary the diagrams are built on. Monitored and controlled variables cross the system boundary; internal variables are introduced to name the data dependencies between functions. Internal variables can be defined either centrally with the diagram or within the function where the variable originates (mirroring how monitored and controlled variables are defined at external entities).

- **Commonality and variability analysis** — named in 2.5.4 as an optional, more systematic input to the functional analysis. It identifies which parts of the requirements are stable and which are likely to vary between products, supporting planned reuse across a product family.

- **Functional Hazard Assessment (FHA)** and **Preliminary System Safety Assessment (PSSA)** — introduced in 2.6.3 as the safety-engineering machinery that drives architecture revision for safety-critical systems. The FHA identifies high-level system hazards; the PSSA determines whether the system could contribute to realizing them and, if so, levies derived design safety requirements. The handbook ties this process to the commercial-avionics safety standard ARP 4761.

- **Fault tree** — the PSSA output (figures 5 and 6 in the source) used to apportion probability-of-failure budgets across the functions that could cause a hazard.

- **Exception cases** — introduced in 2.6.5 as extensions of the use cases that capture how departures from the nominal "sunny day" behavior are handled.

## Key Concepts

**Group by what changes together (2.5.1).** The architecture is developed by recursively identifying functions and grouping those that are logically related and likely to change together. The worked example: the Isolette functions for turning the thermostat on/off, indicating status, setting the desired temperature range, displaying current temperature, and indicating failure all touch the operator interface and would all be affected if that interface changed — so they collapse into a single **Manage Operator Interface** function, while the independent on/off control of the heat source becomes **Manage Heat Source**.

**The structure is also the traceability (2.5.1).** Because requirements are grouped recursively by function, the document structure itself traces lower-level requirements up to higher-level ones — the hierarchy is doing double duty as both organization and traceability.

**Stable interfaces, hidden volatility (2.5.3).** The label on each arrow between functions should denote a durable, high-altitude idea rooted in the problem domain — something the source expects to stay put over time. Volatile dependencies are deliberately hidden inside functions and pushed as far down the hierarchy as possible. This creates what the handbook calls firewalls — boundaries that stop a change from propagating across the specification.

**Define internal variables fully (2.5.4).** Any internal variable introduced to express a data dependency must have its type, range, precision, and units defined, just like external variables.

**Nesting for scale (2.5.5).** A single level of functions is not enough for large systems. Functions nest within functions to allow arbitrarily large specifications, and the arrows can represent aggregates of variables so that large collections of monitored, controlled, and intermediate variables can be carried compactly. The detailed behavior and performance requirements live at the lowest level of this hierarchy.

**Keep high-level requirements genuinely high-level (2.5.6).** For non-terminal (non-lowest-level) functions, the dependency diagrams and internal-variable definitions already imply the high-level requirements. Explicit textual high-level requirements are optional and, where present, should state only what is true at that level. The Isolette example: at the top the Thermostat function is only known to set the Heat Control and Operator Feedback controlled variables and the range of their values — not how. Pulling up detail from lower levels either introduces ambiguity or duplicates what is already specified below, and it defeats the whole point of the architecture.

**Why "more precise" can be wrong (2.5.6).** The handbook shows a tempting "improved" version of REQ-1 that says the thermostat sets the heat control to maintain temperature within the desired range. It rejects this on two grounds. First, that statement is only true in NORMAL mode — in INIT or FAILED mode the heat control is off — and modes are not even defined until the next level down, so the precise statement requires vocabulary that does not yet exist at this level.

**Rationale is not requirement (2.5.7).** The second reason the "improved" REQ-1 is wrong: it mixes in *why* the requirement exists with *what* the system does. "Maintain current temperature within the desired range" is rationale — an explanation — not a requirement. In figure 4 that same information appears, but explicitly labeled as rationale to help the reader, never as a requirement.

**The ideal architecture is a starting point, not the answer (2.6).** The logical architecture from 2.5 ignores implementation. Reality forces revision: safety, legacy integration, and platform constraints. Rather than maintaining a continuous mapping between an ideal architecture and a different real one, the handbook revises the functional architecture itself to absorb the most important constraints, then uses that revised structure as the framework for the detailed requirements.

**Stay close to the ideal (2.6.2).** Because the problem domain changes less than implementation constraints do, the closer the final architecture stays to the original functional architecture, the more stable it will be — so differences between the two should be minimized.

**Safety drives the revision (2.6.3).** The worked Isolette case shows the mechanism. The FHA names hazard H1 (prolonged exposure of the infant to unsafe heat or cold), classified catastrophic with a target probability below 1e-9 per hour. The PSSA enumerates the ways each function could realize H1 and, via a fault tree, hands each function a failure-probability budget (initially below 2e-10 per hour). Achieving that per-component reliability would be prohibitively expensive and would conflict with the cost goal, so a cheaper architecture is chosen: add an independent **Monitor** that raises an alarm when temperature leaves a safe range. With the nurse's normal monitoring, a follow-on PSSA shows this combination relaxes the budget to below 1e-5 per hour for the thermostat, heat source, and monitor.

**Architecture change cascades through the specification (2.6.3–2.6.10).** Introducing the monitor renames the Thermostat function to **Regulate Temperature** and splits the thermostat into independent **Regulate** and **Monitor** functions. That single change forces a cascade of revisions, each its own recommended practice: revise the system overview and goals (2.6.3); revise operational concepts (2.6.4); develop exception cases off the use cases (2.6.5); link exception cases to use-case steps, or use the exception precondition when the exception can occur almost anywhere (2.6.6); revise the system boundary for new monitored/controlled variables such as Alarm Temperature Range and the new status variables (2.6.7); document new environmental assumptions, which the handbook warns can be subtle (2.6.8); revise the dependency diagrams (2.6.9); and revise any affected high-level requirements (2.6.10).

**A diagram is a table of contents (2.6.1).** The handbook frames the revised dependency diagrams as a graphical table of contents for the detailed requirements specification that follows — the structure tells the reader where each detailed requirement will live.

## Mental Models

**Firewalls against change.** Picture each function as a compartment with a fireproof boundary. Stable, high-level concepts pass through the boundary as labeled arrows; anything volatile is sealed inside and pushed deeper. A change that would otherwise spread through the whole document is contained to one compartment.

**Black box opening, level by level.** The context diagram is a sealed box. Each dependency diagram opens one box to reveal the functions and arrows inside; each of those functions is itself a box that can be opened again. The hierarchy is a nested sequence of black boxes, and detail only ever appears when you open the lowest one.

**Arrows lie politely.** The drawn arrow points the way data flows, which is intuitive and matches data-flow-diagram convention — even though the true dependency points the other way (the consumer depends on the definer). The handbook accepts this small lie because nothing actually "moves" in a requirements specification and the practical cost is minor.

**Ideal versus final, kept on a short leash.** Hold two pictures: the clean problem-domain architecture, and the real one that safety and platform constraints forced. The job in 2.6 is to deform the first into the second using the smallest possible deformation, because the clean picture is the more durable of the two.

**Budget apportioned down a fault tree.** A top-level reliability target is not met by one heroic component. It flows down a fault tree, splitting into per-function budgets — and when a budget is infeasible or too costly, you change the architecture (add a monitor) rather than the component, which redistributes the budget.

## Anti-patterns

The handbook does not present these under an explicit "anti-pattern" heading, but it does name specific practices to avoid; they are included here because the source frames them as things not to do.

- **Pulling lower-level detail up into high-level requirements (2.5.6).** Doing this in an effort to be thorough and precise negates the entire purpose of the functional architecture, which is to provide a framework for organizing a complex specification. It also forces the use of terms not yet defined at that level.
- **Using lower-level terms in a high-level requirement (2.5.6).** Recommended Practice 2.5.6 directs that a high-level requirement express only what is knowable at its own altitude, without leaning on vocabulary introduced further down the hierarchy.
- **Mixing rationale into the requirement (2.5.7).** Recommended Practice 2.5.7 directs that, when writing high-level requirements, you avoid folding rationale into the requirement as a way of smuggling in detail that belongs to a lower-level function. State what the system does separately from why.

## Key Takeaways

- Build the functional architecture by recursively grouping functions that are closely related and likely to change together; the resulting hierarchy organizes the requirements and supplies their traceability.
- Depict functions and dependencies with dependency diagrams, distinguishing monitored, controlled, and internal variables by where their arrows begin and end.
- Make interfaces between functions stable and high-level; hide volatile dependencies inside functions and push them down the hierarchy to create firewalls against change.
- Fully define internal variables (type, range, precision, units) and nest functions and variable aggregates to scale to large systems.
- Keep high-level requirements honestly high-level: state only what holds at that level, do not borrow lower-level vocabulary, and never embed rationale in the requirement.
- Treat the 2.5 architecture as an ideal starting point; in 2.6 revise it to absorb safety, legacy, and platform constraints, while keeping the final architecture as close to the ideal as possible.
- Let safety analysis (FHA, PSSA, fault tree) drive revision for safety-critical systems, and follow each architecture change through the full cascade — overview, operational concepts, exception cases, boundary, environmental assumptions, diagrams, and high-level requirements.

## Connects To

- **Requirements writing (the complementary thread).** This chapter is the structural counterpart to the requirements-writing guidance: the functional architecture decides where each requirement lives and at what altitude it is stated, while requirements-writing decides how each individual requirement is phrased. The 2.5.7 separation of requirement from rationale is shared ground between the two.
- **Preliminary system functions (section 2.3 in the source).** The functional architecture starts from the preliminary list of system functions developed earlier; this stage groups and decomposes them.
- **System modes (section 2.7).** The handbook repeatedly defers precision to where modes are defined — the high-level Heat Control behavior cannot be stated until NORMAL, INIT, and FAILED modes exist one level down.
- **Detailed behavior and performance requirements (section 2.8).** These live at the lowest level of the functional architecture; the dependency diagrams act as their graphical table of contents.
- **System safety process and ARP 4761.** For safety-critical, real-time and embedded systems, the FHA/PSSA/fault-tree chain is the external driver that forces architecture revision; this is where the handbook's avionics slant is most visible.
- **CoRE methodology and structured analysis.** The organizing principles here are a continuation of CoRE and classic data-flow-diagram structured analysis, both of which placed detailed requirements in the lowest-level functions.
- **Product-line / reuse engineering.** Commonality and variability analysis connects this stage to planned reuse across a product family by localizing the parts of the requirements most likely to vary.

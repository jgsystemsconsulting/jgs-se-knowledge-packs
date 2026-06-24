# Chapter — Develop the System Overview and Identify the System Boundary

## Core Idea

Before a single shall-statement is written, the requirements author owes the reader two things: a quick orientation to *what the system is and why it exists*, and a sharp line dividing *what we are building* from *the world it sits in*. This chapter pairs those two activities. The system overview is the introductory artifact that lets a new reader grasp purpose, environment, and intent at a high level without drowning in detail. The system boundary is the formal answer to "where does our responsibility stop?", expressed not as a box on an org chart but as a concrete set of environmental quantities the system senses and affects. The handbook treats both as early, evolving artifacts — created among the first deliverables, revised continuously as understanding matures. The payoff is concrete: a clear boundary stops you from writing requirements that duplicate or collide with work happening at a higher level, and from silently assuming the surrounding environment will provide something it never will. That risk sharpens when several organizations build pieces of the same system, which is the normal condition for the embedded, real-time avionics and medical-device work this handbook is oriented toward.

## Frameworks Introduced (exact source names, when/how)

- **System Overview (practice 2.1)** — Introduced as the front matter of the requirements specification: a synopsis, one or more context descriptions, short descriptions of each external entity, and a set of high-level goals, objectives, and constraints. Created early, kept high-level, used to orient new readers rather than to fully describe the system.

- **Context Diagram (practice 2.1.4)** — Introduced as a graphical, high-level depiction for each identified context. The system appears as a black box with no internal structure; external entities and their interactions are drawn around it. The handbook notes it can also help to show the higher-level system in which the target system is embedded (e.g., the Isolette surrounding the Thermostat). Worked examples are cited for the Isolette Thermostat (figure A-1) and three avionics cases — the FCS, FGS, and AP (figures B-1, C-1, D-1).

- **Monitored and Controlled Variables (practice 2.2)** — Introduced as the mechanism for defining the boundary. The system is viewed as a component interacting with its environment through a set of *monitored* variables (environmental quantities the system responds to) and *controlled* variables (environmental quantities the system affects), as drawn in figure 1. The system's job is to maintain a relationship between the two that satisfies the system goals; the definition of these variables and their attributes *is* the boundary.

- **SCR, CoRE, and RSML (cited heritage, footnote 1)** — The monitored/controlled framing is attributed to the SCR and CoRE methodologies. The handbook notes RSML uses a similar idea under the labels *manipulated* and *controlled* variables. These are named as the lineage of the approach, not re-taught here.

- **System Goals (practices 2.1.6 / 2.1.7)** — Introduced as informal statements of stakeholder needs. Explicitly *not* requirements: they are unverifiable and underspecified for building, but they explain *why* the system is being built and what stakeholders care about. The Isolette Thermostat is given two goals, G1 (keep the infant at a safe, comfortable temperature) and G2 (minimize manufacturing cost), and these are used to show how goals routinely conflict.

- **Physical Interfaces (practice 2.2.7)** — Introduced as the eventual full extension of the boundary: every discrete input and output, every message, every field within a message, and every protocol used to send and receive. Where a standard interface or protocol applies, the standard is to be cited. Hooks and Farry (reference [22]) are cited as recommending this be done as early as possible.

## Key Concepts

**The overview is an orientation device, not a specification.** At a glance it should convey the system's job, the way it engages the surrounding environment, and the reason it is needed. It deliberately stops short of describing the system completely. Optional material like historical background is allowed, but only when it does not slow down a new reader's orientation.

**The synopsis comes first and stays design-neutral.** The overview opens with a short narrative that names the system, states its purpose, and summarizes its main capabilities — ideally without implying any particular design. The Isolette example illustrates this: it explains what an Isolette is (an infant incubator providing controlled temperature, humidity, and oxygen, widely used in neonatal intensive care) and what the thermostat does (hold air temperature in a desired range by sensing temperature and switching a heat source), while letting a nurse set a safe desired range — all without committing to internals.

**A system has more than one context across its life cycle.** The handbook stresses considering the *entire* life cycle. Beyond the obvious operational context, there is often a testing context (the system wired to test equipment through different interfaces during development) and a maintenance context (used to diagnose and repair the fielded system). Because different stakeholders care about different contexts, the guidance is to describe each one separately rather than fuse them into a single overloaded diagram.

**Monitored vs. controlled, anchored by the elimination test.** Monitored variables are quantities the system reads from the world; controlled variables are quantities it changes in the world. The handbook's avionics illustration: actual aircraft altitude and airspeed as monitored values; control-surface position (an aileron) or a displayed altitude on the primary flight display as controlled values. The defining heuristic: both kinds of variable exist in the environment independently of the system and would persist even if the system were deleted.

**Direct control and direct sensing.** Controlled variables are restricted to what the system controls *directly*. In the Isolette case, air temperature is *not* a controlled variable, because the thermostat only influences it indirectly through the heat source; the directly controlled quantity is the Heat Control signal. Symmetrically, monitored variables should match the physical quantity the system actually senses, chosen at the right level of abstraction — for an avionics suite, true aircraft altitude may be the right monitored variable, but for a subsystem consuming an altitude estimate from another subsystem, the estimate is the right one. The handbook warns against picking "true altitude" as the monitored variable for a system whose whole job is to *estimate* altitude from several sources; each source's altitude should be its own monitored variable.

**Abstraction over wire format.** Monitored and controlled variables should be as abstract as the function allows and must not carry implementation detail. The handbook's sharp example: a variable may legitimately be a real number with one digit of precision over a stated range, but it should *not* be specified as an ARINC 429 word. The variables should hold no more detail than the system needs, assuming an idealized interface to the outside world.

**Presentation is design, not boundary.** Display formatting must be kept out of the environmental variables. The worked example: a display showing altitude in yellow for a warning and blinking red for a hazard actually involves *two* controlled variables — the altitude (a number) and the status (normal / warning / hazard). How those are rendered to the pilot belongs to detailed HMI design, not to the boundary definition.

**Variables and physical interfaces are both required, at different altitudes.** Monitored and controlled variables sit at a stable abstraction level that changes only if the problem domain changes. Physical interfaces — the concrete means of sensing and actuating — sit much lower and are more volatile. Both must be defined. If physical interfaces are known up front they can *help* identify the variables, provided care is taken to extract the true environmental quantities at the proper abstraction. If they are not known up front, they become far easier to define once the variables and full system behavior are nailed down.

**Goals are guidance, not contracts.** Goals come from customers, users, regulatory bodies, and prior developments, gathered directly or via interviews and document review. They guide requirements and frequently surface in a requirement's rationale (section 2.11); operational concepts (section 2.3) also trace back to them. On a small project two goals on one page may suffice with occasional review. On a large or new system, goals evolve as needs, priorities, and personnel change, and managing them becomes work in its own right — warranting tracked attributes such as origin, origin date, author, priority, stakeholders, stability, and schedule date, and configuration control when they churn.

## Mental Models

**The black box with two pipes.** Picture the environment with the system drawn inside it as an opaque box. One pipe flows in (monitored variables), one flows out (controlled variables). You never open the box to define the boundary — the boundary *is* the set of pipes and what flows through them. This is figure 1 distilled, and it is why the context diagram shows the system with no internal structure.

**The elimination test.** For any candidate boundary variable, ask: would this quantity still exist in the world if the system vanished? Altitude exists whether or not your avionics box does. A heat source's on/off command... still describes an environmental effect the system produces. If the answer is no, you have probably grabbed an internal artifact (an input/output to software, a wire format) rather than a true environmental variable.

**Two altitudes for two jobs.** Hold the boundary at the stable, problem-domain altitude (monitored/controlled variables) and the interface definition at the low, volatile altitude (physical interfaces) — and keep them separate. Collapsing the boundary down onto the wire format drags the whole specification to implementation level and forfeits robustness and reuse.

**The orientation budget.** Treat the overview as having a fixed "attention budget" for a brand-new reader. Every paragraph of history or detail you add spends some of it. Spend only what buys orientation.

**Better wrong-and-written than right-and-absent.** A documented boundary you can correct over time beats no boundary at all. The handbook is explicit that the boundary will shift as functionality migrates between systems during development, and that this is expected rather than a failure.

## Anti-patterns

The source frames these as cautions tied to specific practices:

- **Specifying the wire format as the variable.** Using a physical-interface artifact (the ARINC 429 word) where an abstract environmental quantity belongs drags the spec down to implementation level and makes it brittle and non-reusable.
- **Baking presentation into controlled variables.** Folding display formatting (color, blinking) into a controlled variable instead of separating the underlying value (altitude) from its status, leaving rendering to HMI design.
- **Defining physical interfaces without the variables.** Hooks and Farry recommend defining interfaces early, but the handbook warns that doing so *in isolation* — without also identifying the monitored and controlled variables — pulls the requirements down to the interface's low abstraction level and loses robustness.
- **Choosing a monitored variable above the system's real knowledge.** Naming "true altitude" as the monitored variable for a system that can only obtain estimates from sources — when each source estimate should be its own monitored variable.
- **No documented boundary at all.** Without a clear boundary you risk duplicating or conflicting with higher-level requirements, or omitting requirements you wrongly assume the environment supplies — most dangerous on multi-organization builds.

## Key Takeaways

- Build the system overview as one of the first artifacts and treat it as the spec's introduction; keep it high-level so it orients new readers fast.
- Open with a short, design-neutral synopsis that names the system, states its purpose, and summarizes capabilities.
- Enumerate every distinct life-cycle context (operational, testing, maintenance), describe each separately, and give each its own context diagram showing the system as a black box.
- Define the boundary early via a preliminary set of monitored and controlled variables — accept that it is imperfect and will shift.
- Restrict controlled variables to what the system directly controls and monitored variables to what it directly senses, both at the right abstraction.
- Keep variables abstract: no wire formats, no presentation/HMI detail; split a formatted display into its underlying value and status.
- Define both the abstract variables and the full physical interfaces (discrete I/O, messages, fields, protocols; cite standards) — but never let the interfaces stand in for the variables.
- Capture goals early as informal stakeholder guidance, expect them to conflict and evolve, and scale their management (attributes, configuration control) to project size and volatility.

## Connects To

- **Requirements-writing core (this pack's complement).** The overview and boundary are upstream of the shall-statements; the boundary's monitored/controlled variables become the vocabulary that downstream functional requirements operate over. This chapter sets the stage that the requirements-authoring chapters then fill in.
- **Environmental assumptions (section 2.4).** Variable attributes — type, range, precision, status — are explicitly deferred from the boundary definition to the environmental-assumptions treatment, where they live as conditions the system depends on.
- **Operational concepts (section 2.3) and rationale (section 2.11).** Both trace back to system goals: rationale cites goals to explain why a requirement exists, and operational concepts derive from them.
- **SCR / CoRE / RSML methodologies.** The four-variable, monitored/controlled framing is inherited from this embedded/real-time requirements lineage; readers wanting the formal underpinning are pointed to that body of work.
- **Worked examples across the pack.** The Isolette Thermostat (appendix A) and the three avionics systems — FCS (B), FGS (C), AP (D) — recur as the canonical illustrations; their overviews, context diagrams, and variable tables are the concrete instantiations of every practice in this chapter.
- **Embedded/real-time slant.** The boundary-as-variables discipline is most natural for control-oriented, safety-relevant systems (medical incubators, flight control and guidance, autopilot); applying it to information-system or service contexts requires reinterpreting "monitored" and "controlled" beyond physical sensing and actuation.

# Chapter — Systems Thinking

> Synthesized reference notes from SEBoK v2.14, Part 2 Knowledge Area **Systems Thinking** (BKCASE authorship). Content is CC BY-NC-SA 3.0, attributed to the BKCASE Project, transformed for reference use — no long verbatim passages reproduced.

## Core Idea

Systems thinking is the integrating paradigm that links systems science to the systems approaches used in practice. In the SEBoK's framing it is concerned with understanding, or intervening in, problem situations by applying the principles and concepts of the systems paradigm. It looks across systems from different domains for the **similarities** that recur, and captures those similarities as three interlocking kinds of knowledge: **concepts**, **principles**, and **patterns**. The SEBoK is specifically interested in how this body of thinking can support a systems approach to *engineered* systems.

The KA distinguishes three terms carefully. A **concept** is an abstraction — a general idea derived from specific instances. A **principle** is a rule of conduct or behavior, "a basic generalization taken to be true and usable as the basis on which one reasons or acts." A **pattern** is an expression of an observable regularity found in systems of different domains. The three are mutually dependent: principles cannot exist without concepts, and concepts are of little use without principles to guide how to act (Lawson and Martin 2008). The KA's four articles map onto these terms — *What is Systems Thinking?*, *Concepts of Systems Thinking*, then *Principles of Systems Thinking*, and finally *Patterns of Systems Thinking*.

A second core idea is the deliberate balancing of two opposed stances. **Holism** — treating a system as a whole rather than a collection of parts — has dominated systems thinking for nearly a century because of phenomena such as emergence. But pure holism cannot be acted upon, so it is balanced against **reductionism**, the focused study of parts. The SEBoK locates this balance at the heart of any systems approach, and therefore at the heart of systems engineering.

## Frameworks Introduced (exact SEBoK terms, when/how)

- **The systems thinking paradox** — introduced in *What is Systems Thinking?* to name the central tension: to fully understand a system you would have to consider all its possible relationships, internally and externally, across all future situations — which makes complete understanding impossible. The systems approach is what lets useful work proceed despite this, by making pragmatic use of concepts, principles, and patterns. The principles of **encapsulation** and **separation of concerns** are the mechanisms that resolve it in practice: hide enough detail to focus on a change, while bounding the impact within acceptable commercial and social risk.
- **Systemic resolution** — named in *What is Systems Thinking?* for the way of observing a system in which the complex web of relationships is focused around a chosen system boundary. Used when identifying **systems of interest (SoIs)** (Flood and Carson 1993) that are both relevant and represent a whole.
- **System context** — used to define a SoI and to agree on the systems it works with directly and the systems that influence it. Applying a system context is how the holism/reductionism balance is operationalized; it is described as essential to any systems approach (and so to SE). The SEBoK cross-references the **Engineered System Context** topic in the *Systems Approach Applied to Engineered Systems* KA.
- **Churchman's "enemies" of the systems approach** — politics, morality, religion, and aesthetics (Churchman 1979). These "enemies" are framed not as obstacles to be removed but as a learning device: they let the rational thinker step outside a system's boundary and view it through other people's values. Churchman's defining move is that a systems approach requires seeing a system from the viewpoint of those outside its boundary.
- **A Set of Systems Principles** (Table 1, *Principles of Systems Thinking*, SEBoK Original) — a tabulated framework of named principles, each tied back to underlying concepts: Abstraction, Boundary, Change, Dualism, Encapsulation, Equifinality, Holism, Interaction, Layer Hierarchy, Leverage, Modularity, Network, Parsimony, Regularity, Relations, Separation of Concerns, Similarity/Difference, Stability/Change, Synthesis, and View. The KA stresses these are *not independent* — they have synergies and trade-offs, and judgment, experience, and heuristics determine which apply.
- **The conceptagon** (Edson 2008, modified from Boardman and Sauser 2008) — a structure relating many of the named principles, with guidance on applying them.
- **Prerequisite Laws of Design Science** (Warfield 1994) — three are stated: the **Law of Requisite Variety**, the **Law of Requisite Parsimony**, and the **Law of Gradation** (with its corollary, the Law of Diminishing Returns).
- **Hitchins' systems life cycle theory** (Hitchins 2003) — a set of seven integrated principles describing the creation, manipulation, and demise of engineered systems, centered on the **connected variety** principle and a cyclic progression of variety generation, dominance, decay, and renewal.
- **Heuristics and pragmatic principles** — the SEBoK draws on Maier and Rechtin's (2000) heuristics (each mapped to a principle, e.g. "efficiency is inversely proportional to universality" → Leverage) and INCOSE's (1993) **pragmatic principles** (best-practice heuristics such as "know the problem, the customer, and the consumer").
- **Pattern taxonomy** (*Patterns of Systems Thinking*) — **hierarchy patterns** and **network patterns** (basic foundational), **metapatterns**, **systems engineering (SE) patterns**, and **antipatterns / patterns of failure**. The KA also names **pattern-based systems engineering (PBSE)** (Schindel and Smith 2002; Schindel 2005) as the combination of patterns with MBSE.
- **System archetypes** (Table 3, SEBoK Original) — a collection from the system dynamics community (originated by Forrester 1969; the term introduced by Senge 1990), grouped by the SEBoK under antipatterns.

## Key Concepts

The *Concepts of Systems Thinking* article synthesizes a system of system concepts from Ackoff (1971), Skyttner (2001), Flood and Carson (1993), Hitchins (2007), and Lawson (2010). The principal concepts:

- **Wholeness and Interaction** — a system is a set of elements with enough cohesion ("togetherness") to form a bounded whole. Per Hitchins, **interaction** between elements is *the* key system concept; in complex systems the interactions matter at least as much as the parts. An **open system** is defined by interactions among its elements and between its elements and other systems in an environment; the remaining concepts apply to open systems.
- **Regularity** — a uniformity or similarity across multiple entities or times (Bertalanffy 1968). Regularities make science possible and engineering efficient; without them every problem and solution would be unique. Contrasted: the **nomothetic** approach (assumes regularities) versus the **idiographic** approach (assumes each entity is unique).
- **State and Behavior** — an **attribute** is any property of an element; the **state** is the set of attributes at a given time; an **event** is any change to the environment and hence the state. Systems are characterized as **static**, **dynamic**, or **homeostatic** (static system, dynamic elements). **State variables** trace state through a **state space**, modelable as a finite state model. Behavior is distinguished as **react / respond / act** (Ackoff 1971). Systems are **deterministic** (one-to-one state mapping, predictable) or **non-deterministic** (many-to-many, unpredictable).
- **Survival Behavior** — **entropy** is the tendency toward disorder (used metaphorically for aging, obsolescence, skill fade); **negentropy** is what holds entropy off, with **homeostasis** as the biological equivalent maintaining a steady state or dynamic equilibrium. Hitchins' **connected variety** holds that a system's stability increases with its connectivity, internal and environmental.
- **Goal Seeking Behavior** — a defining trait of engineered systems. A **goal** is a specific outcome achievable in a set time; an **objective** is a longer-term outcome reached through a series of goals; an **ideal** is an objective that cannot be achieved with certainty but progress toward which has value. Systems may be single-goal seeking, multi-goal seeking, or reflective. **Purposive** systems pursue predetermined outcomes (most machines/software); **purposeful** systems freely determine their own goals (humans, sufficiently complex machines).
- **Control Behavior** — from cybernetics: **negative feedback** (maintains state against objectives) and **positive feedback** (forced growth or contraction). A **black-box** view controls via inputs/outputs (slower); a **white-box** view embeds control in the element structure (more responsive, more risk to stability). A **meta-system** sits over the system to control it. Control trades **specialization** against **flexibility** — an instance of **dualism**. **Variety** and the **Law of Requisite Variety** (Ashby 1956): a controller must have at least as much variety as the system it controls.
- **Function** — outcomes that contribute to goals or objectives (Ackoff). To have a function a system must deliver an outcome in two or more ways (**equifinality**). In hard systems approaches, functions are drawn from the problem statement and bound to element structures until a **system component** (an implementable function-plus-structure) is defined. Transformations are **synchronous** or **asynchronous**.
- **Hierarchy, Emergence and Complexity** — **synergy** (weak emergence) is the whole being greater than the sum of its parts; the reverse (reducing variety) is also possible. Complexity often takes the form of **hierarchies**, which evolve faster and are easier to understand than non-hierarchic systems of comparable size (Simon 1962, 1996). **Encapsulation** hides internal elements behind a boundary. **Emergence** names behaviors arising across a complex hierarchy.
- **Effectiveness, Adaptation and Learning** — **effectiveness** measures the ability to perform the functions needed to meet goals; Hitchins decomposes it into performance, availability, and survivability. An **adaptive system** can change itself or its environment when effectiveness is insufficient. A system may also **learn**, improving effectiveness over time with no change in state or goal.

Additional concepts introduced with the principles: **separation of concerns** (balancing focus on parts against sight of the whole, Greer 2008), **abstraction**, **view** and **viewpoint** (a view is a subset of observed information; the viewpoint is the point from which it is observed; views must be both separate and integrated), **modularity** (Griswold 1995), and **dualism / leverage** — where **leverage** is the duality of **power** (how well a system solves one specific problem) versus **generality** (how well it solves a whole class), drawing on the **yin yang** concept of harmonized opposites (Hybertson 2009).

## Mental Models

- **The "systems thinking paradox" as a working constraint, not a wall.** Full understanding is impossible, so the move is to gather *enough* knowledge to proceed at an acceptable risk level — a blend of codifiable rules and the irreducible skill and judgment of the people doing the work.
- **Step outside the boundary.** Churchman's discipline of viewing a system "through the eyes of another" (and confronting its "enemies") is a deliberate practice for surfacing values and assumptions a boundary hides.
- **We reason over models, not reality.** Per Ossimitz, systems thinking presupposes awareness that we deal with models of reality, not reality itself — pairing with Gharajedaghi's framing of systems thinking as the art of simplifying complexity (seeing through chaos, managing interdependency, understanding choice).
- **Holism and separation of concerns are dual, not contradictory.** They look opposed but are two ways of dealing with complexity; both are required, and choosing only one yields insufficient understanding or a poor solution. This dualism is the principle-level expression of the systems thinking paradox.
- **Boundaries are chosen, and the choice has consequences.** Too narrow a boundary in scope or timeline solves the problem of the moment by creating a similar or larger one elsewhere in space, community, or time — the dynamic captured by the "shifting the burden" archetype.
- **Patterns as a maturity signal.** A domain's stock of well-defined patterns indicates its maturity. Physical and technical systems are relatively mature; social and complex systems are less so — the system dynamics community has good *antipatterns* (problem descriptions) but the matching solution patterns remain elusive. Rittel and Webber's **wicked problems** mark the pessimistic boundary of this gap.
- **Holistic thinking is bigger than systems thinking.** Per Kasser, systems thinking is one element within holistic thinking — the combination of analysis (elaboration), systems thinking, and critical thinking.

## Anti-patterns

The KA names **antipatterns** (coined by Koenig 1995) as patterns of failure — things that superficially resemble a solution but are not one; knowing the likely blind alleys is itself useful. It groups three families:

**System Archetypes** (Table 3, SEBoK Original) — common recurring patterns of behavior in organizations and complex social systems, repeatedly but unsuccessfully used to solve recurring problems. The SEBoK groups them under antipatterns (noting the system dynamics community does not). Named archetypes include:
- **Counterintuitive Behavior** (Forrester's three "especially dangerous" social-system behaviors).
- **Low-Leverage Policies: Ineffective Actions** (a.k.a. Policy Resistance).
- **High Leverage Policies: Often Wrongly Applied** (High Leverage, Wrong Direction).
- **Long-Term vs. Short-Term Trade-offs** (Fixes that Fail, Shifting the Burden, Addiction).
- **Drift to Low Performance** (Eroding Goals, Collapse of Goals).
- **Official Addiction — Shifting the Burden to the Intervener.**
- **Limits to Growth** (a.k.a. Limits to Success).
- **Balancing Process with Delay.**
- **Escalation.**
- **Success to the Successful.**
- **Tragedy of the Commons** (Hardin 1968).
- **Growth and Underinvestment.**
- **Accidental Adversaries.**
- **Attractiveness Principle.**

**Software and other antipatterns** — named examples: **Escalation of commitment** (failing to revoke a wrong decision), **Moral hazard** (insulating a decision-maker from the consequences), and **Big ball of mud** (a system with no recognizable structure). The SEI's "patterns of failure" work links the system archetypes to recurring software **acquisition archetypes**.

**Systems pathologies** (Troncale 2010, 2011) — a general-systems set of antipatterns: **cyberpathologies** (malfunctions in feedback architectures), **nexopathologies** (malfunctions in network architectures/dynamics), and **heteropathologies** (malfunctions in hierarchical, modular structure and dynamics).

## Key Takeaways

- Systems thinking is the integrating paradigm between systems science and systems practice; the SEBoK organizes its knowledge as **concepts**, **principles**, and **patterns**, with concepts and principles mutually dependent.
- The discipline lives in a **balance of holism and reductionism**, applied through a **system context** around a chosen **system of interest** — the heart of any systems approach and of SE.
- The **systems thinking paradox** explains why complete understanding is impossible and why **encapsulation** and **separation of concerns** are the practical mechanisms for proceeding under acceptable risk.
- A named **set of systems principles** (Abstraction, Boundary, Dualism, Holism, Interaction, Leverage, Modularity, Network, Parsimony, Regularity, Separation of Concerns, Synthesis, View, and others) is interdependent — application depends on judgment, heuristics, and Warfield's prerequisite **laws of design science**.
- The system **concepts** give a vocabulary for state and behavior, control (feedback, requisite variety), goal-seeking (purposive vs. purposeful), function (equifinality), hierarchy, emergence, and adaptation/learning.
- **Patterns** (hierarchy, network, metapatterns, SE patterns, PBSE) capture positive regularities; **antipatterns** — system archetypes, software antipatterns, systems pathologies — capture regularities of failure. Boundary choices that are too narrow recur as the "shifting the burden" archetype.
- Pattern maturity tracks domain maturity: technical systems are well-patterned; social and complex systems remain partly characterized by antipatterns without matching solution patterns (the **wicked problems** frontier).

## Connects To

- **Systems Approach Applied to Engineered Systems KA** — the *Engineered System Context* topic operationalizes the system context and the holism/reductionism balance for engineered systems; Hitchins' SE principles point here for resolving systems problems.
- **Representing Systems with Models** — abstract system representations and models, only touched on in this KA, are detailed there; PBSE links patterns to MBSE.
- **Emergence and Complexity** topic — extends the determinism/complexity relationship, chaotic systems, and the use of patterns and antipatterns to understand and exploit emergence.
- **System Definition** and **Synthesizing Possible Solutions** (Part 3) — where the named principles and patterns are applied to defining solution options for a system of interest.
- **History of Systems Science** — the deeper account of the systems-theory movements (holism, GST, cybernetics) summarized here.
- **Introduction to Part 2** — situates systems thinking within the wider systems knowledge that provides SE its common language and intellectual foundation.
- **External standards and bodies referenced** — **ISO/IEC/IEEE** glossary terminology for encapsulation/modularity (IEEE Std 610.12-1990); **INCOSE** (Systems Engineering Handbook; the 1993 pragmatic principles; the Insight articles by Hitchins); **cybernetics** (Ashby's Law of Requisite Variety) underpinning control behavior.

# Chapter 11 — Agile Approaches

> Synthesized reference notes from the *Guide to the Systems Engineering Body of Knowledge* (SEBoK) v2.14, Knowledge Area **Agile Approaches**. Source content © BKCASE Project, licensed CC BY-NC-SA 3.0. This chapter is a transformed synthesis, not a reproduction.

## Core Idea

The **Agile Approaches** Knowledge Area treats agility not as a single prescribed method but as a set of strategic capabilities that systems engineering can deploy when the operating world is uncertain and changing. SEBoK frames the whole area through **ISO/IEC/IEEE 24748-10**, which positions agility as strategic capability rather than a fixed recipe. The motivation is that modern systems live in conditions of uncertainty, fast-moving technology, and shifting stakeholder expectations, so SE has to move past linear, plan-driven life cycle models toward continuous adaptation across the life cycle.

At its most abstract, agility in SE is the ability to **sense** change, **respond** to it well, and **evolve** the system solution over time. Achieving that calls for three things working together: architectural foresight (modularity, scalability), organizational alignment, and feedback-rich processes that feed iterative learning and decision-making. SEBoK is explicit that agility is *not* confined to development — it reaches across the full life cycle, including production, utilization, and support.

The KA contains two complementary articles. **Agile Systems Engineering** supplies the conceptual and strategic foundation for being agile (the *what*). **Industrial DevOps** is the practical realization of those principles through integrated practices, toolchains, and value-stream-oriented workflows (the *how*). Read together, they show how SE can hold rigor and adaptability at the same time — delivering dependable outcomes while staying responsive in complex socio-technical settings.

## Frameworks Introduced (exact SEBoK terms)

- **ISO/IEC/IEEE 24748-10** — *Guidelines for systems engineering agility*. Used as the framing standard for the entire KA. It treats agility as strategic capabilities, and it is the source standard behind the eight core aspects of SE agility (cited via Dove et al, 2023). When/how: invoked at the KA level to set the conceptual lens, and again as the primary reference for the Agile Systems Engineering article.

- **Agile Systems Engineering** (Dove, Lunney, Orosz, Yokell) — a principle-based way to design, build, sustain, and evolve systems under uncertain knowledge and/or dynamic environments. SEBoK's signature framing here: it is **being agile, not doing agile** — a *what*, not a *how*. When/how: introduced as the strategic foundation, then elaborated through the eight strategic aspects.

- **The eight strategic aspects of SE agility** (Dove et al, 2023; ISO/IEC/IEEE 24748-10) — the core framework of the Agile Systems Engineering article. Each aspect is presented as a **Why (need)**, a **What (behavior)**, and some **How (method)**. The eight, in SEBoK's exact naming:
  1. **adaptable modular architecture**
  2. **iterative incremental development**
  3. **attentive situational awareness**
  4. **attentive decision making**
  5. **common-mission teaming**
  6. **shared-knowledge management**
  7. **continual integration and test**
  8. **being agile: operations concept**
  When/how: SEBoK stresses these are strategic concepts that manifest tactically over a range of intensity; multiple aspects must operate in concert to constitute an agile engineering process, and a "big bang" all-at-once rollout is not required to gain benefit.

- **The SE life cycle spectrum** (Dove, 2022) — a spectrum of life cycle approaches with two ends; every life cycle approach sits somewhere between them. When/how: used to position Agile SE relative to plan-driven SE rather than as an either/or.

- **DevOps** (development and operations), per **ISO/IEC/IEEE 32675** — a set of principles and practices enabling better communication and collaboration among relevant stakeholders to specify, develop, and operate software, systems, products, and services with continuous improvement across the life cycle. When/how: the conceptual parent of Industrial DevOps.

- **Industrial DevOps (IDO)** (Johnson, Yeman) — carries **Lean, Agile, and DevOps** principles into the design, development, deployment, and sustainment of **cyber-physical systems (CPS)**. When/how: presented as a practical approach to address the strategic aspects of SE agility, organized around nine principles and a set of enabling practices.

- **The nine Industrial DevOps Principles** (SEBoK Original table) — each principle paired with a description and a benefit:
  1. **Organize Around the Flow of Value**
  2. **Apply Multiple Horizons of Planning**
  3. **Implement Data-Driven Decisions**
  4. **Architect for Change and Speed**
  5. **Manage Queues and Create Flow**
  6. **Establish Cadence / Synchronization**
  7. **Integrate Early and Often**
  8. **Shift Left**
  9. **Adopt a Growth Mindset**

- **The Industrial DevOps enabling practices** — eight named practices that operationalize the principles: **Value Stream Management**; **Integrated Digital Engineering (IDE)**; **Agile Program Execution**; **Test Automation and Virtualization**; **Continuous Integration and Deployment (CI/CD)**; **Infrastructure as Code (IaC)**; **AI and Digital Twins**; **Lean Governance and Compliance Automation**.

## Key Concepts

**Agile vs. agility (the grammar matters).** SEBoK draws a deliberate distinction. *Agile* is an adjective meaning able to move quickly and easily (an agile development approach, an agile person). *Agility* is a noun (systems engineering agility). Within software/systems engineering, *agile* names a development approach built on iterative development, frequent inspection and adaptation, and incremental delivery, where requirements and solutions evolve through cross-functional collaboration and continual stakeholder feedback (ISO/IEC/IEEE 24748-1:2024). **SE agility** is the broader strategy-based way to design, build, sustain, and evolve purpose-fulfilling creations under uncertain knowledge and dynamic environments.

**Aspects are strategic, intensity is tactical.** Each of the eight aspects can independently improve a process's ability to handle uncertainty, but a genuinely agile process — at the domain or system level — needs several aspects working together. The achieved degree of agility is a product of *how many* aspects are operating *and* how effectively each contributes to the agility the environment actually demands. Incremental adoption is endorsed; concurrent all-at-once implementation is not required.

**Increments vs. iterations.** SEBoK gives these distinct meanings: increments generally create capabilities; iterations add and augment features that improve those capabilities. Increment cycles are timed to coordinate events such as integrated test and evaluation, capability deployment, experimental deployment, or release; they may run at constant or variable cadence. Iteration cycles are timed so that rework cost stays low as the project learns experimentally and empirically.

**Internal vs. external awareness.** Attentive situational awareness asks two questions in parallel: whether things are being done right (internal awareness) versus whether the right things are being done (external awareness)? The capability to change cheaply and quickly is worth little unless you know *when* to exercise it.

**Closing the awareness-to-action loop.** Attentive decision making is the systemic link from situational awareness to decisive action, with authority empowered at the point of most knowledge. SEBoK names **technical debt** as the counter-example: knowing something needs correction but postponing the action — i.e., situational awareness with no causal link to a prompt response.

**Three teaming behaviors are not synonyms.** Common-mission teaming separates **collaboration** (relevant information exchange among individuals), **cooperation** (optimal give-and-take among individuals), and **teaming** (collective endeavor toward a common purpose). Each needs individual attention.

**Two horizons of knowledge.** Shared-knowledge management distinguishes near-term operational knowledge (what has happened, what is happening, what is planned) from long-time-frame curated knowledge (reusable, relevant material — digital artifacts, lessons learned, proven practices), serving a single source of truth for internal and external stakeholders.

**Industrial DevOps targets cyber-physical systems.** Where DevOps grew up in software, IDO deliberately extends Lean/Agile/DevOps to CPS — integrating hardware and software development, bridging engineering silos, and applying flow, cadence, and shift-left thinking to high-stakes, safety-critical, complex systems.

## Mental Models

- **Sense → Respond → Evolve.** The behavioral kernel of "being agile." Whenever you decide how to implement *any* of the core aspects — including this one — do it with sense-respond-evolve in mind as the objective.

- **Being agile, not doing Agile.** Agile SE is a behavior sensitive to threats and opportunities, decisive when one appears, and driven to keep improving that capability — not a procedure you follow. This is the single most load-bearing distinction in the Agile Systems Engineering article.

- **Process agility rides on product agility.** A hallmark of agile SE is iterative incremental development that reworks work-in-process as suitability is repeatedly evaluated; the agility of the *process* depends on the agility of the *product*, so both must be easy to change. Composable, reconfigurable designs built from variations of reusable assets make that possible.

- **The life cycle spectrum, not a binary.** Don't ask "agile or plan-driven?" Ask where on the spectrum this work belongs, given how uncertain the knowledge is and how dynamic the environment is.

- **What vs. how.** Agile Systems Engineering = the strategic *what* (foundations, aspects, principles). Industrial DevOps = a practical *how* (practices, toolchains, value-stream workflows). The KA is built so the two interlock.

- **Flow over local efficiency.** The IDO principles read as a flow model: organize around the value stream, minimize work-in-progress, shrink batch sizes, synchronize cadence, integrate early and often, and shift testing left — all to reduce bottlenecks, shorten feedback, and cut risk.

## Anti-patterns

- **Technical debt** — explicitly named in SEBoK as the counter-example to attentive decision making: situational awareness that knows correction or improvement is needed, but with no causal link that prompts action. (This is the only named anti-pattern in the slice.)

## Key Takeaways

- Agility in SE is a set of **strategic capabilities** to sense, respond, and evolve — framed by **ISO/IEC/IEEE 24748-10** — not a fixed method, and it spans the *entire* life cycle including production, utilization, and support.
- **Agile Systems Engineering** is principle-based and is a **what, not a how**: being agile, not doing Agile.
- The framework is **eight strategic aspects** of SE agility, each expressed as Why/What/How; they must operate **in concert**, can be adopted incrementally, and scale in intensity to match the environment.
- SEBoK insists on precise vocabulary: *agile* (adjective) vs. *agility* (noun); increments create capabilities vs. iterations augment features; collaboration vs. cooperation vs. teaming; internal vs. external awareness.
- **Industrial DevOps** operationalizes Lean/Agile/DevOps for **cyber-physical systems** through **nine principles** and **eight enabling practices**, and is positioned as a way to deliver on the strategic aspects of SE agility.
- The two articles are complementary by design: strategic foundation (Agile SE) plus practical realization (Industrial DevOps), letting SE balance rigor with adaptability.

## Connects To

- **ISO/IEC/IEEE 24748-10** (*Guidelines for systems engineering agility*) and **ISO/IEC/IEEE 24748-1:2024** — the standards SEBoK uses to define agile development and SE agility; ties this KA into the **Systems Engineering Standards** landscape and the broader 15288 life-cycle family.
- **ISO/IEC/IEEE 32675** (DevOps) — the standard underwriting the DevOps definition feeding Industrial DevOps.
- **INCOSE Systems Engineering Handbook, 5th Edition** (Ch. 4.2.2) — cited companion treatment of agile life-cycle process content.
- **Life Cycle Models** KA — Agile SE is positioned along the **SE life cycle spectrum**, directly connecting to plan-driven vs. evolutionary/iterative life cycle model discussions.
- **System Verification and Validation / Integration** — continual integration and test, shift-left, and CI/CD draw this KA toward V&V and integration practice.
- **Digital Engineering / MBSE** — Industrial DevOps's Integrated Digital Engineering (IDE), **AI and Digital Twins**, and Infrastructure as Code link to the digital engineering and model-based KAs.
- **Systems of Systems (SoS) and Enterprise SE** — data-driven decisions and value-stream organization explicitly address managing the flow of work across systems of systems.
- **Lean roots** — IDO's lineage runs back through Lean manufacturing and the Toyota Production System, the historical seed (1991 DoD study, the DARPA-funded Agility Forum at Lehigh) from which agile manufacturing, agile systems, and agile enterprises grew.

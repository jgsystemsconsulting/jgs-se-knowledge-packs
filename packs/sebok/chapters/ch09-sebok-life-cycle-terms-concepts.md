# Chapter 9 — Life Cycle Terms and Concepts

*Synthesized reference notes from SEBoK v2.14, Knowledge Area "Life Cycle Terms and Concepts" (BKCASE authorship). Content is transformed for reference use under CC BY-NC-SA 3.0; attribution to the BKCASE Project required.*

## Core Idea

Every engineered thing — a system, product, service, project, or any other human-made entity — moves through an arc from conception to retirement. SEBoK calls that arc a **life cycle**, citing the ISO/IEC/IEEE 24748-1:2024 definition of it as the evolution of such an entity from conception through retirement. Because that arc is long and consequential, it helps to build representations of it that you can plan against and steer by; SEBoK names those representations **life cycle models**.

This Knowledge Area assembles the shared vocabulary that the rest of SEBoK's life-cycle material depends on. It is deliberately definitional rather than prescriptive: it fixes the meaning of four linked terms — life cycle, life cycle model, **stage**, and **technical reviews and audits** — so that later KAs (model selection, process descriptions, maintenance) can use them without re-defining them. A stage is a bounded period within the life cycle tied to the state of the entity's description or realization, anchored to major progress, milestones, or decision points. Technical reviews and audits are the mechanism by which independent, knowledgeable stakeholders examine the current state of a system or work products against pre-established criteria, feeding both programmatic and technical decisions.

## Frameworks Introduced (exact SEBoK terms, when/how)

- **Life cycle** — introduced as the foundational term and reused verbatim at the head of every article in the KA. SEBoK grounds it in ISO/IEC/IEEE 24748-1:2024.
- **Life cycle model** — defined as a framework of processes and activities concerned with the life cycle, organizable into stages, serving as a shared reference that supports communication and understanding (ISO/IEC/IEEE 24748-1:2024). SEBoK points readers to the separate "Life Cycle Model Selection and Adaptation" KA for deeper treatment.
- **Stage** — a period within the life cycle relating to the state of the entity's description or realization, tied to progress, milestones, or decision points; SEBoK notes that stages often overlap. The "Life Cycle Stages" article carries entry/exit detail.
- **Life cycle processes** — the processes and activities integrated into a life cycle model's framework; positioned as one enabler for managing a solution across stages, applicable concurrently, iteratively, and recursively in some models. SEBoK names ISO/IEC/IEEE 15288, SAE 1001, and the INCOSE SE Handbook as sources that define them, and maps them into the System Concept Definition; System Architecture Design Definition; System Maintenance; and the Technical Management Processes KAs.
- **SE life cycle spectrum** — a depiction (attributed to Dove, 2022) placing life cycle approaches along a continuum keyed to the level of uncertainty, with both extreme ends described as uncommon in practice.
- **Typical Life Cycle Stages** — the conception → development → production → utilization → support → retirement naming, attributed jointly to ISO/IEC/IEEE 24748-1 and 15288, plus the INCOSE SE Handbook (2023).
- **Decision gates (criteria-based)** — the review/gate construct governing stage transitions, each with entry/exit criteria, applied to reduce risk and confirm satisfactory progress.
- **Technical review** vs. **audit** — SEBoK distinguishes the two: a technical review is a series of SE activities at logical transition points assessing project progress against technical requirements using mutually agreed criteria (per ISO/IEC/IEEE 24748-8:2019); an audit, by contrast, is an independent examination of work products for compliance with specifications, standards, agreements, or other criteria (ISO/IEC/IEEE 15288:2023). It notes organizations may use either term, or others, for these related concepts.
- **Boehm and Lane review typology** — three review types keyed to what triggers them: schedule-based, event-based, and evidence-based, each with characteristic opportunities and risks.

## Key Concepts

**Models versus reality.** The life cycle is the real evolution of the entity; the life cycle model is a chosen depiction of it. SEBoK is explicit that a single system of interest can be viewed through more than one life cycle model, that models differ in whether they permit iteration and concurrency of stages, and that which stage(s) a system occupies depends on the model in use. A system of interest can occupy multiple stages simultaneously.

**Project models are not life cycle models.** SEBoK flags a common conflation: some diagrams that look like life cycle models actually model the phases of a *project* rather than the stages of a *system's* life cycle. Generic stage names map onto other viewpoints only loosely (a comparison derived from Forsberg et al., 2005), so the reader must check what a given figure is actually segmenting.

**Four principles of a life cycle model.** SEBoK lists four recurring properties: (1) a system advances through specific stages over its life; (2) enabling systems should be available at each stage so the stage's outcomes can be achieved; (3) at given stages, quality characteristics — producibility, usability, supportability, disposability — should be specified and designed or implemented in; (4) stages start and end on criteria or external events.

**Stages can run in parallel and recur.** The worked example shows a short concept stage, longer development and production, and lengthy utilization, support, and retirement. With multiple units produced, utilization and support began with the first unit; for the software element, support began early in development, before delivery. A planned mid-life upgrade restarted concept, development, and production, so support ran parallel to utilization, support ended while units were still in use, and retirement continued until the last unit retired. SEBoK adds the practical caveat that the original developer cannot always know whether units are still being used.

**The DevOps/DevSecOps infinity loop.** Where most models read left-to-right, DevOps and DevSecOps depict the life cycle as an infinity loop (Figure 3, attributed to D'Souza derived from Banach 2019 and Anx 2021). In this model there is no development/support distinction — the work is never "done" — and retirement risk and effort are assumed negligible, so retirement is not a focus.

**Typical stages and their primary goals.** SEBoK pins a goal to each stage: Concept — identify stakeholder needs, explore concepts, propose viable solutions; Development — refine requirements, create the solution description, build the system, perform system verification and validation; Production — produce, inspect, and test; Utilization — operate to satisfy users' needs; Support — provide sustained capability; Retirement — store, archive, or dispose.

**Entry and exit criteria are not always clean.** Criteria can be satisfied before, concurrent with, or after the decision — or not at all (SEBoK ties this to diamonds versus triangles in its decision-gate figure). Decision criteria can include an assessment of **technical debt**: its presence harms design suitability, and it can accumulate in any stage. SEBoK stresses that not all parts of a system of interest reach the same maturity, hence the same gate, at the same time — making interim maturity reviews essential — and that entry/exit criteria must be tailored, because one size does not fit all.

**Looking back and looking forward.** At a decision gate, actual progress is assessed against the criteria expected for a stage or an independent increment, with two facets: a backward look at progress to date and a forward look at readiness to continue. SEBoK enumerates the decision options available at a gate: begin another stage(s), continue the current stage, go to or restart another stage, pause activity, or terminate. In two-party acquisition, joint stakeholder reviews can support these gates, and ISO/IEC/IEEE 24748-8 supplies more rigorous review/audit requirements (framed for defense projects but applicable more broadly).

**Technical reviews and audits support several processes.** SEBoK ties them to project assessment and control (visibility into technical progress and risk; readiness for the next milestone or stage), configuration management (establishing, revising, and verifying baselines), and validation (early validation of requirements, design, and other work products through stakeholder and end-user involvement). They apply to a system, a system element, or any established technical boundary, and can also authorize risky activities such as testing with safety or security concerns.

**The review/audit approach: prepare, conduct, complete.** *Prepare* — balance business case/mission, budget, and technical maturity (with risks) so baselines lead to satisfactory V&V; document assumptions and risks given the uncertainty; plan name, purpose and outcomes, scope, properties assessed, timing/frequency, and activities; define and coordinate entry/exit criteria, confirm entry criteria first, and select SMEs including specialty engineering. *Conduct* — participants analyze relevant information (documents, models, simulations, prototypes) from their own perspectives (safety, security, reliability), independently or as a group, then meet to discuss results and identify actions. *Complete* — once exit criteria are met, communicate results to participants and absent stakeholders and implement identified actions.

**Independence is a balancing act.** SEBoK frames reviewer selection as a tension: people "too close" to a project may be biased (it cites the loss of a bonus as an example), while people "too far" may miss critical issues. The recommended remedy is a mixed team — some close enough for insight, some removed enough for independence.

**Timing and frequency.** Reviews and audits apply to a system of interest and recursively to its elements, occurring sequentially, iteratively, incrementally, or concurrently — but never before pre-defined entry criteria are met.

## Mental Models

- **Territory vs. map.** The life cycle is the territory (the entity's actual evolution); the life cycle model is a map. Multiple maps of one territory are legitimate, and the right one depends on uncertainty (the SE life cycle spectrum) and intent.
- **The uncertainty dial.** Picture every life cycle approach as a point on a slider between two extremes neither of which you'd actually run. Where you land sets how much iteration and concurrency your stages need.
- **Stages as overlapping bands, not a relay race.** Default intuition draws stages as a clean left-to-right baton pass. The KA's worked example and the DevSecOps infinity loop break that: bands overlap, recur on a mid-life upgrade, and in DevOps fold development and support into one continuous loop.
- **Gates as a two-way mirror.** At each decision gate you look backward (what's been achieved) and forward (readiness to go on) at once. The valid moves are not just go/no-go but a fuller menu: begin, continue, restart, pause, terminate.
- **Criteria that may or may not land.** Treat entry/exit criteria as targets that can be hit early, on time, late, or never — diamonds and triangles — rather than as crisp gates, and let technical debt count against suitability when you assess them.
- **The Goldilocks reviewer.** For an honest review, staff the team in the "just right" zone — insiders close enough to see the real state, outsiders far enough to say so.

## Anti-patterns

SEBoK does not label named anti-patterns in this slice, but it does flag recurring failure modes worth treating as cautions:

- **Mislabeling a project model as a life cycle model** — confusing the phases of a project with the stages of a system's life cycle.
- **Reviewing on the wrong trigger** — each Boehm-and-Lane review type carries its own risk: schedule-based reviews risk insufficient information and stalled progress; event-based reviews risk shallow analysis and unresolved issues; evidence-based reviews risk late feedback on latent defects with cost, schedule, and technical impact. Across all three, schedule or cost pressure can force a review with inadequate preparation or information.
- **Reviewer too close or too far** — bias on one side, missed critical issues on the other.
- **Holding a review before entry criteria are met** — explicitly cautioned against.

## Key Takeaways

- A **life cycle** runs from conception through retirement; a **life cycle model** is a chosen framework of processes and activities, organizable into **stages**, used as a common reference (all grounded in ISO/IEC/IEEE 24748-1:2024).
- One system of interest can be seen through several models, can sit in several stages at once, and can have stages that overlap, run in parallel, or restart (e.g., for a mid-life upgrade).
- The typical stage set — conception, development, production, utilization, support, retirement — comes jointly from ISO/IEC/IEEE 15288 and 24748-1, together with the INCOSE SE Handbook (2023), each stage carrying a primary goal.
- **Decision gates** govern transitions with tailored entry/exit criteria, weigh **technical debt** against design suitability, look both backward and forward, and offer five decision options (begin, continue, restart, pause, terminate).
- **Technical reviews** (progress against technical requirements) and **audits** (compliance of work products) are distinct but related; they run prepare → conduct → complete, demand a balanced-independence review team, and must wait for entry criteria.
- DevOps/DevSecOps reframes the whole life cycle as an infinity loop with no dev/support split and negligible retirement focus.

## Connects To

- **Life Cycle Model Selection and Adaptation** (SEBoK KA) — explicitly cross-referenced for deeper treatment of choosing and tailoring models.
- **Technical Management Processes, System Concept Definition, System Architecture Design Definition, System Maintenance** (SEBoK KAs) — where SEBoK locates the life cycle processes themselves.
- **ISO/IEC/IEEE 24748-1:2024** (Life cycle management, Part 1) — source of the core definitions of life cycle, life cycle model, and stage.
- **ISO/IEC/IEEE 15288:2023** (System life cycle processes) — defines system life cycle processes and the audit concept.
- **ISO/IEC/IEEE 24748-8:2019** (Technical reviews and audits on defense programs) — source of the technical-review definition and more rigorous gate requirements, defense-oriented but broadly applicable.
- **SAE 1001** and the **INCOSE Systems Engineering Handbook (2023)** — additional sources defining system life cycle processes and stage naming.
- **Boehm & Lane (Incremental Commitment Spiral Model)** — origin of the schedule/event/evidence-based review typology; ICSM also cited as an example application of reviews and audits.
- External standards cited as example applications of technical reviews and audits: **US DoD Systems Engineering Guidebook (Feb 2022)**, **NATO AAP-48 (May 2022)**, and **NASA NPR 7123.1D (Jul 2023)** — each represented in the broader knowledge-pack family.

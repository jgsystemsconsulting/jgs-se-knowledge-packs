# Chapter — System Design Processes: Stakeholder Expectations, Requirements, Logical Decomposition, Design Solution

> Depth supplement to the NASA SE Handbook pack (chapters 17–20, sections 4.1–4.4). This chapter does **not** re-teach what NGOs, ConOps, MOEs, MOPs/TPMs, the five-step requirements validation, or the PBS/WBS *are* — the handbook pack already does that. It carries the **expanded guidance** layer: the recursive-loop mechanics, the terminology and ownership traps, the survivability lineage behind space asset protection, the doctrine of successive refinement and its objective-function math, and the specialty-engineering integration detail that the base handbook compresses to a sentence.

## Core Idea

The four system design processes are not a pipeline — they are a single recursive engine run repeatedly at every level of the product hierarchy. The expanded guidance frames them as one closed loop in which three artifacts are forced into mutual consistency: a strawman architecture/design, a concept of operations, and a set of derived requirements. None of the three is "done" until all three agree with each other *and* survive a validation test against stakeholder expectations. The loop asks three blunt questions — will it work as expected, is it achievable within budget and schedule, and does it deliver the functionality that justified the funding — and any "no" throws the team back to either the design or the expectations themselves. The same loop fires at progressively finer resolution as the project moves Pre-Phase A → A → B → C, and the depth of effort at each turn is calibrated to one standard: it must be deep enough that an independent review team would judge the design feasible and credible, and deep enough to support cost and operations modeling. That feasibility-to-a-skeptical-reviewer bar, not "all requirements written," is the real exit criterion.

## Frameworks Introduced

Names and usage are taken verbatim-as-concepts from the source slice (NASA/SP-2016-6105-SUPPL, §4.0–4.4); descriptions are paraphrased.

- **The recursive system-design loop (Figure 4.0-1, "Interrelationships among the System Design Processes")** — the governing diagram of the whole chapter. Used continuously from Pre-Phase A through Phase C. It couples the four processes so that ConOps, requirements, and design solution iterate against one another, with explicit "Inconsistencies — Iterate" and "No — Iterate" feedback arcs, until the system meets stakeholder expectations. The handbook treats the four processes as separate chapters; this loop is what binds them.

- **"Concept of Operations" vs. "Operations Concept" (boxed distinction in §4.1.2.1)** — a deliberate terminology split. The *Concept of Operations* is authored early by the technical team to describe, usually time-sequenced, how the system will be used to satisfy stakeholders; the *Operations Concept* is a later, narrower description (typically by the operational team) of how flight and ground segments work together so the ConOps is reasonable — e.g., how data are captured, returned, processed, distributed, and archived (referencing NPR 7120.5). Used to avoid the two documents being conflated.

- **Typical Operational Phases table (Table 4.1-2)** — a reference set of Phase D/E/F operational phases (integration-and-test ops, launch ops, deployment, on-orbit checkout, science operations, safe-hold, anomaly resolution/maintenance, disposal). Used when building the time-sequenced ConOps structure that drives configuration changes and critical-event definition.

- **Threat × Susceptibility = Vulnerability survivability model (§4.1.2.2, Figures 4.1-7/4.1-8)** — the analytical backbone of space asset protection. The source attributes it to aircraft-survivability work (Robert Ball, *The Fundamentals of Aircraft Combat Survivability Analysis and Design*) and applies it to spacecraft and ground infrastructure. Used to derive a Program/Project Protection Plan (PPP) under NPR 7120.5, iterated between PPP baseline and each succeeding KDP.

- **Flow / Type / Ownership of Requirements model (Figure 4.2-2)** — classifies requirements by where they originate (mission-directorate-imposed, program-imposed, self-imposed/derived), what they are called (programmatic vs. technical), and **who owns the waiver authority**: programmatic requirements are owned by the program/project; technical requirements are owned by the Technical Authority. Used to route any requirement-change or waiver to the correct authority.

- **Requirements Metadata schema (Table 4.2-2)** — the per-requirement attribute set (ID, rationale, traced-from, owner, verification method, verification lead, verification level) plus a structured Rationale block (reason, assumptions, relationships, design constraints). Used at requirement-write time to populate the requirements database.

- **Technical-standards order of authority (§4.2.2.6.2, per NPR 7120.10)** — the precedence rule: (1) standards mandated by law, (2) national/international voluntary consensus standards, (3) other government standards, (4) NASA technical standards; with a "core standards" concept whose waivers escalate to Agency level. Used when selecting and tailoring standards.

- **Functional analysis technique trio (§4.3.2.2)** — Functional Flow Block Diagrams (FFBDs) for task sequence, N² diagrams (N×N interaction matrices) for interface identification, and TimeLine Analyses (TLAs) for time-critical sequencing. Used as the concrete methods behind "functional analysis" during logical decomposition.

- **DOD Architecture Framework (DODAF) (boxed in §4.3)** — operational, systems, and technical-standards views with associated products (operational nodes/connectivity, systems interconnectivity, dictionaries). Offered not as a NASA mandate but as a borrowable formalism for structuring complex system-of-systems problems.

- **Doctrine of Successive Refinement (Figure 4.4-2)** — the model of design as a spiral of "create concepts" steps, each a turn of the recursive loop, moving from general strategies/architecture to functional design to detailed design at ever-finer resolution. Used to explain *why the design effort proceeds in turns* rather than top-down once.

- **Quantitative Objective Function / cost-effectiveness search space (Figure 4.4-3)** — a single scalar ("objective" or "cost" function) over candidate solutions in a "search space," where an optimal solution maximizes/minimizes it; risk is shown as probability clouds (concepts A, B, C with different risk patterns). Used in Design Solution Definition together with the Decision Analysis Process (§6.8) to recommend the "best" alternative — while explicitly cautioning that trade studies yield *bounds*, not final values.

## Key Concepts

These extend, rather than repeat, the handbook's concept lists.

- **The mutually-consistent triad.** At every "create concepts" turn, three products must be made consistent with one another: a strawman design/architecture, its matching ConOps, and the requirements derived from them (with programmatic constraints folded in). Consistency among the three is the precondition for validation; achieving it requires iterations and explicit design decisions, not just authoring.

- **Per-phase calibration of design depth.** The *same* processes are run at different intent each phase: Pre-Phase A aims at a feasible design that earns Formulation approval; Phase A pursues alternatives and analytical maturity to optimize the architecture; Phase B yields a preliminary design meeting approval criteria; Phase C completes detailed build-to designs. Architecture design completes in Formulation; for most projects a single architecture is baselined in Phase A.

- **Initial vs. validated stakeholder expectations.** Expectations are explicitly captured as *initial* and remain so until the ConOps is developed and stakeholders give final agreement — at which point they are baselined. Developing the ConOps is what surfaces gaps and ambiguities that refine the initial set.

- **Constraint as immovable boundary.** A constraint is a condition to be met that typically *cannot* be changed by tradeoff analysis — orbital mechanics, a mandated external interface, a regulatory restriction, technology state, or the budget environment. It establishes the design boundary, distinct from the trade space.

- **Key Driving Requirements (KDRs).** A KDR is a requirement that can swing cost or schedule heavily when implemented; it may carry any priority or criticality. Identifying KDRs early lets the team manage where the cost/schedule leverage actually sits.

- **Threshold vs. baseline performance as trade space.** Performance is stated as a threshold (minimum acceptable; going below forces a project descope) and a baseline (desired). The gap is deliberate trade space. The expanded guidance adds the *inverse* caution: over-tight performance requirements destroy solutions and inflate cost — a 3-hour recharge spec where 12 hours suffices, or ±0.5 kg where ±2.5 kg suffices, raises metrology cost with no added value.

- **Deterministic vs. risk-informed safety requirements.** A deterministic safety requirement is a hard threshold of action or performance (physical hardware stops, command-range limits, fault-tolerant processors, automatic shutdown on out-of-limit values, approved-language-subset rules). A risk-informed safety requirement is set partly from safety-related TPMs and their uncertainty — e.g., a P(LOC) (Probability of Loss of Crew) ceiling of value *p* held at a stated confidence level — or established human-tolerance limits.

- **Derived requirements as architecture byproduct.** Logical decomposition *generates* requirements that were not in the baselined input — they arise from the chosen architecture's definition. Both baselined and derived requirements are then allocated to the architecture and functions. Verification methods can themselves spawn derived requirements (e.g., adding a test port for internal-signal visibility during integration).

- **Verify-the-design vs. validate-the-design (and why both differ from the *product* V&V).** Design-solution **verification** confirms the chosen design is realizable within constraints, has acceptable-statement requirements with bidirectional traceability, and that its decisions/assumptions are consistent with the technical requirements — done largely by **peer review**. Design-solution **validation** is the recursive check of each alternative against stakeholder expectations. Both are distinct from Product Verification (§5.3) and Product Validation (§5.4), which happen later against the realized end product.

- **Enabling products are part of the system.** Production, test, deployment, training, maintenance, and disposal products/services are interdependent with the end product and are treated as one system. The design process must identify them, set realistic need-dates with schedule slack, and secure firm commitments early — because facilities are oversubscribed and lead times are long.

## Mental Models

- **The loop is a consistency clamp, not a checklist.** Picture three jaws — architecture, ConOps, requirements — being tightened until they meet. You are not finished when each is individually written; you are finished when moving any one of them no longer forces a change in the other two, *and* the clamped assembly passes the three validation questions (works as expected? achievable in budget/schedule? delivers the funded functionality?). Inconsistency is the normal state; iteration is the work.

- **Run the same engine at higher magnification each pass.** Successive refinement means the design isn't drawn once top-down; it's resolved in turns, each turn baselining derived/allocated requirements that *become* the high-level requirements for the next level down. Ask "when do we stop?" and the answer is resolution-based: stop refining a branch when its depth is enough to analytically validate against requirements/ConOps and to convince a review team of feasible performance, cost, and risk margins — not before, not arbitrarily after.

- **Stay the outsider during bottom-up integration.** Designers grow fond of their own designs and lose objectivity; the systems engineer deliberately remains external to preserve it. This bites hardest on *heritage* equipment, where technology developers and managers systematically overestimate maturity and applicability — heritage reused in a different architecture or environment outside its experience base is, in fact, technology development and must be assessed as such.

- **Watch the top-down/bottom-up race.** Concepts are built bottom-up by integrating lower-level elements while requirements flow top-down. There's a standing danger the top-down process can't keep up with the bottom-up one — so resolve system-architecture issues *early* enough to model the system realistically and run reliable trade studies, before the bottom-up momentum outruns the governing structure.

- **Trade studies buy bounds, then confidence.** An objective function lets you rank concepts as single cost-effectiveness numbers, but risk turns those numbers into probability clouds (one concept may have a high-cost/near-zero-effectiveness failure cloud hugging the axis). Increasing resolution narrows the spread between upper and lower bounds; you never get final values from a trade study because the final design detail is intentionally deferred. The discipline is that trades happen *before* irreversible decisions, so the baseline can be set with confidence.

- **Human elements have a maturity level too.** Treat operators and maintainers like a subsystem whose capability must be assessed, not assumed. Over-expecting them fails the total system exactly as immature hardware does — the Space Shuttle was projected at up to 40 flights/year but never exceeded 9, because quick-turnaround, ground-crew, and maintenance realities were not designed in. Early HSI is the hedge against this class of life-cycle-cost surprise.

- **Baseline late, but baseline.** Baselining a single design is the stake in the ground that lets a team stop chasing a moving target — but doing it too early kills the inventive, wide-open exploration of alternatives. So baselining is deliberately one of the *last* steps of Design Solution Definition, after the free exploration has run its course.

## Anti-patterns

Only patterns the source itself names as failure modes are listed.

- **Over-specified performance requirements (§4.2.2.2.2).** Writing tighter tolerances than the mission needs (recharge < 3 hr when 12 hr works; weight ±0.5 kg when ±2.5 kg works) eliminates viable designs and raises metrology cost without adding value. The source frames this as a direct caution.

- **Vague, unverifiable requirements (§4.2.2.5).** "Minimize noise" cannot be verified and therefore should either not be a requirement or be rewritten quantitatively ("the noise level of component X shall remain under Y decibels"). If a requirement can't be verified, it isn't a requirement yet.

- **Bolting safety/reliability on after the design is formed (§4.4.2.3.1).** The source states that in too many cases risk/reliability/fault-management analysts are engaged only *after* the design is formulated, so those features get added on or outsourced rather than designed in — yielding analysis that misses the real risk drivers and adds no design value. The fix is integrating those analysts inside the design teams from the start.

- **Premature focus on a single design (§4.4.1.2.2).** Locking onto one concept too early prevents discovery of the truly best design; the explicit countermeasure is to keep as wide a range of plausible, parameter-described alternatives as the charter allows.

- **Premature baselining (§4.4.1.2.10).** Baselining before alternatives are understood removes the inventive nature from concept exploration; the source flags this as a danger and prescribes late baselining.

- **Overestimating heritage-technology maturity (§4.4.1.2.2, §4.4.2.1).** Treating reused "heritage" equipment as mature when it is operating in a new architecture/environment causes critical systems-engineering aspects to be overlooked; such modifications should be recognized as technology development.

## Key Takeaways

1. **Consistency is the gate, feasibility-to-a-reviewer is the exit.** The four processes converge only when architecture, ConOps, and derived requirements agree and the design would convince an independent review team it is feasible and credible — deep enough to support cost and operations modeling. "All requirements written" is not the bar.

2. **Distinguish Concept of Operations from Operations Concept.** They are different documents with different authors and scope; conflating them loses the early technical-team vision (ConOps) or the later flight/ground reasonableness check (Operations Concept). The ConOps also matures from a simple event ordering into detailed subsystem behavior across all modes.

3. **Route every requirement by flow, type, and ownership.** Programmatic requirements are owned (and their waivers approved) by the program/project; technical requirements by the Technical Authority. Knowing the owner before you change or waive a requirement is what keeps change control coherent.

4. **Space asset protection is survivability engineering, not security paperwork.** It applies the aircraft-survivability identity threat × susceptibility = vulnerability to spacecraft and ground infrastructure, feeds a PPP under NPR 7120.5, and iterates from PPP baseline through each KDP — with Space Situational Awareness (including collision avoidance and space weather) as an essential input.

5. **Apply standards by their order of authority.** Law first, then voluntary consensus standards, then other government standards, then NASA standards; core-standard waivers escalate to the Agency. Standards are not self-invoking — they must be explicitly called out as requirements.

6. **Successive refinement: baseline derived requirements become the next level's high-level requirements.** The engine reruns at finer resolution; each turn's allocated/derived requirements seed the next decomposition. Stop a branch when its resolution is sufficient to validate analytically and convince reviewers of feasible margins — a resolution criterion, not a phase boundary.

7. **Decision Analysis picks the design, but trades yield bounds.** Use an objective function and the Decision Analysis Process to recommend the best alternative; respect that the output bounds cost-effectiveness rather than fixing it, and that unquantifiable factors (robustness, etc.) must be weighed alongside the numbers.

8. **Verify the *design* by peer review; validate the *design* against expectations — both separate from product V&V.** Design-solution verification (realizable, traceable, internally consistent) and validation (meets stakeholder expectations) happen in this phase and precede the later Product Verification/Validation against the built article.

9. **Integrate specialty engineering early or pay later.** Safety/reliability, fault management (with a dedicated Fault Management Systems Engineer), QA (with Government Mandatory Inspection Points for loss-of-life/mission attributes), Integrated Logistics Support (its ten technical disciplines), maintainability, producibility, and human factors must be designed in from concept development — their cost-benefit is greatest the earlier they contribute, and prototypes exist to "wring out" producibility and maintainability before commitment.

## Connects To

- **NASA SE Handbook pack, chapters 17–20 (§4.1–4.4):** This chapter is the depth layer over those four. The handbook defines NGOs, ConOps, MOEs, the five-step requirements validation, MOPs/TPMs, crosscutting requirements, PBS/WBS, FFBD/N²/TLA, DODAF, and the objective-function idea; this chapter supplies the recursive-loop mechanics, the ConOps/Operations-Concept split, ownership/waiver routing, the survivability lineage, successive-refinement stop criteria, and specialty-engineering integration.

- **NPR 7120.5 (NASA Program and Project Management Requirements):** Mandates the Program/Project Protection Plan and frames the Operations Concept; the design-process baselines feed its phase gates.

- **NPR 7120.10 (Technical Standards for NASA Programs and Projects):** Source of the standards order-of-authority and core-standard waiver escalation invoked in requirements definition.

- **Decision Analysis Process (§6.8) and Technical Assessment (§6.7):** Design Solution Definition's trade studies, objective function, and the SRR/concept-review gates that baseline expectations and requirements depend on these crosscutting management processes.

- **Fault Management (§7.7) and Human Systems Integration (§7.9):** The FMSE role, fault-management-as-ILS-element, and human-capability assessment / human-centered design (NASA-STD-3001) tie the design processes to these specialty domains; HSI function allocation is an input as early as Stakeholder Expectations Definition.

- **Product Verification (§5.3) and Product Validation (§5.4):** The downstream counterparts to design-solution verify/validate; the design phase produces the verification and validation *plans* that these later processes execute against the realized end product.

- **MBSE / SysML and architecture frameworks:** Logical decomposition models, derived-requirement traceability, and the functional-analysis trio map directly onto model-based representations; DODAF is offered as a borrowable formalism for complex system-of-systems structuring.

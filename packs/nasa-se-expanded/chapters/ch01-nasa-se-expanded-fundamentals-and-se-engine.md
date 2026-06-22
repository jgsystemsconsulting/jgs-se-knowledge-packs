# Chapter — Fundamentals of Systems Engineering, the SE Engine, and a Worked Example

> **Depth note.** This chapter is the *Expanded Guidance* companion to the base `nasa-se-handbook` treatment of the same sections (2.0–2.3 of NASA/SP-2016-6105). The handbook pack already states the definitions, the three process sets, recursion/iteration, the Product Breakdown Structure, phase-vs-end products, NGOs, requirement flowdown, and the verify-right/validate-the-right distinction. This chapter deliberately does **not** restate those. It adds the load-bearing detail the base chapters compress or omit: the intellectual lineage behind the NASA definition, the mechanics of the SE↔Project-Control overlap, the precise normative meaning of *iterative* vs *recursive*, the by-phase cadence of engine cycles (with the Phase C/D split), the AS9100 crosswalk, and the Space Transportation System (STS) example read as a chain of *engineering-judgment* decisions rather than a list of passes.

## Core Idea

Systems engineering at NASA is positioned as a *way of thinking* before it is a set of processes — a deliberately holistic, integrative discipline whose job is to keep any one specialty from dominating the whole, and whose value comes from the relationships among parts rather than the parts themselves. The Expanded Guidance frames this through two ideas the base handbook leaves implicit: first, that emergent system value lives in the *interconnections* (the Rechtin lineage), and second, that the systems engineer operates inside a deliberate tension with the project-control function — providing the technical truth about what is achievable while the project manager owns delivery within cost and schedule. The SE Engine is then the operational expression of that thinking: not a workflow diagram to follow once, but a template re-instantiated against every product in the hierarchy and re-run with a different cadence in each life-cycle phase. The STS worked example exists to make one non-obvious point concrete — that *where you stop decomposing* and *which side of the engine you run when* are judgment calls that distinguish competent systems engineering from mechanical process-following.

## Frameworks Introduced

These are the named constructs from this slice of the source. Where the base handbook already introduces a construct, the entry here records only the *added* mechanics.

- **The Systems Engineering Engine (NPR 7123.1)** — the canonical 17-process model arranged as three sets (system design, product realization, technical management). *Added mechanics this chapter carries:* processes 1–9 are the *execution* tasks of a project, while processes 10–17 are explicitly described as **crosscutting tools** for carrying out the first nine — a tool/task split the base treatment blurs. Use it as the organizing spine of any NASA project, but read 10–17 as instruments rather than sequential steps.

- **SE-in-Context-of-Project-Management model (Figure 2.0-1)** — a notional three-function view of managing a project: managing the technical aspects, managing the team, and managing cost and schedule. The Expanded Guidance names the two *cornerstones* explicitly: Systems Engineering (SE) and Project Planning & Control (PP&C). Use this framing whenever you need to explain *where SE's authority ends* — in the overlap region, SE supplies technical inputs and PP&C supplies programmatic, cost, and schedule inputs.

- **The Overview of the SE Engine by Project Phase (Section 2.2 / Figure 2.2-1)** — the "poster" model showing how the engine is re-run across Pre-Phase A through Phase F. This is the framework most thinly covered in the base pack. Its load-bearing facts: the development processes (1–9) run **five engine cycles** spanning Pre-Phase A to Phase D; the technical-management processes (10–17) run **seven cycles** spanning Pre-Phase A to Phase F; and Phases C and D are deliberately *split* so the engine runs the left side (design) in C and the right side (realization) in D, bounded by a dashed line, to give management tighter control. Each engine entry carries a "6105 paragraph label" keying it to the detailed chapters (e.g., "Get Stakeholder Expectations" → §4.1). Use this as the map for *when in the life cycle* a given process actually fires.

- **AS9100 Alignment Crosswalk (Table 2.1-1)** — a mapping of the 17 SE processes onto the AS9100 aerospace quality-management standard. This crosswalk is **absent from the base handbook chapters** and is the single most reusable artifact in this slice for anyone bridging NASA SE to a commercial quality system. Use it when a Center or contractor is AS9100-certified and must show that NPR 7123.1 conformance also satisfies the quality system.

- **The Product Breakdown Structure (PBS) and SE Engine Tracking Icon (Figures 2.3-1, 2.3-4 ff.)** — the tiered product hierarchy plus the small numbered icon used in the worked example to mark *which* of the 17 processes is active at any point in a pass. The base pack introduces the PBS; the *tracking-icon device* — reading a worked example by watching which numbered cells are lit — is the added pedagogical mechanic here.

## Key Concepts

The base handbook covers stakeholder expectations, technical requirements, ConOps, SEMP, NGOs, flowdown, and the verify/validate split. The concepts below are the ones this slice develops *beyond* that baseline.

- **Emergent value lives in the interconnections.** The source roots its definition of "system" in the claim that what the whole adds *beyond* the independent contribution of the parts comes primarily from how the parts are interconnected (attributed to Rechtin, *Systems Architecting of Organizations*). This is the conceptual justification for why interface management and architecture — not component excellence — are where systems engineering earns its keep.

- **The "two cultures of engineering."** Chapter 2.0 of the source draws its framing from a Michael Griffin address contrasting the conventional-engineer's drive to optimize a subsystem against the systems-engineer's mandate to balance across subsystems. The practical takeaway: the systems engineer's deliverable is a *coherent whole not dominated by a single discipline*, which is frequently in direct tension with each specialist's local optimum.

- **The SE/PP&C overlap is structural, not accidental.** The Expanded Guidance is explicit that the overlap between the systems engineer's remit and the project manager's remit is *natural*: SE focuses on the success of the engineering (technical, cost, schedule *realism*), while PP&C imposes constraints on engineering options to protect delivery. Three different NPRs route the management relationship depending on project type — NPR 7120.5 (space flight), NPR 7120.8 (research & technology), and NPR 7120.7 (IT and institutional infrastructure, which points project managers back to NPR 7123.1 for SE requirements). Knowing *which* NPR governs tells you whose vocabulary and constraints apply.

- **"Iterative" and "recursive" are distinct defined terms.** This is a precise distinction the base pack uses loosely. Per the NPR 7123.1 definitions paraphrased in the source: *iterative* means re-running a process on the **same** product to fix a found discrepancy or any other departure from the requirements; *recursive* means adding value by re-applying the processes either to design the **next lower** layer or to realize the **next upper** layer — and likewise re-running them against the structure in a **later life-cycle phase** to mature the definition and clear that phase's success criteria. In short: iterate to *fix*, recurse to *descend, ascend, or advance a phase*.

- **Get it right vs. get the right thing.** The source compresses the whole purpose of SE into a doublet: not only *getting the design right* (meeting requirements) but *getting the right design* (enabling operational goals and meeting stakeholder expectations). The first is verification's domain; the second is validation's — and the second is the one that is cheap to fix early and ruinous to fix late.

- **The lowest feasible level is not a fixed tier.** A point the worked example makes that the base pack only gestures at: the level at which decomposition can stop differs by product. A simple product may bottom out at Tier 2; a complex one may require Tier 8. Consequently, at any moment a project's products sit at *different* stages of maturity, and branch length in the PBS does **not** correspond to elapsed time.

- **Implementation happens only at the bottom; everything above is integration.** In the realization passes, the *Product Implementation* process fires **only** at the bottom-most product (where something is bought, built, coded, or reused). Every higher pass uses *Product Integration* of already-realized products. Verifying the component parts is explicitly *not sufficient* to conclude the integrated product works — interface gaps and bad design assumptions surface only at integration-level V&V.

## Mental Models

- **Read the engine as a stamp, not a pipeline.** The most useful reframing in the worked example: the SE Engine is a template you *stamp* onto every product in the hierarchy. The orbiter, the external tank, the avionics box each "reset to process 1" and run their own full pass. When you find yourself thinking "we already did stakeholder expectations," check whether you did them *for this product at this tier* — recursion means you do them again, with new stakeholders inheriting from the tier above.

- **Watch which side of the engine is legal to run.** A discipline the example enforces: you may not run the right side (realization) until the left side (design) has produced something buildable. In Pre-Phase A through Phase B you are running the left side against *phase products* (models, mockups, simulations); only in Phases C–D do you run both sides against the *actual end product*. If you catch yourself trying to verify a design that isn't yet detailed enough to build, you've jumped sides too early.

- **Treat phase products as dress rehearsals that also write the plan.** The models and prototypes built in early phases do double duty: they prove feasibility *and* they generate the draft verification/validation/integration/transition procedures for the eventual end product. The transition of a model "to the next lab" is rehearsing the transition of the real article.

- **Stop decomposing at first-order trade-space convergence.** The judgment heuristic the example names: in Phase A you descend only far enough to pin down the first-order trade space across technical, cost, and schedule dimensions and to retire the high-risk requirements — not down to circuit boards for everything. Going deeper than risk reduction warrants burns schedule for no return. Knowing when to stop is described as a matter of *experience*, not rule.

- **Long-lead and storage decouple branch order from time.** The example's Aa/Ab integration shows that a bottom-tier item (Aa) may be procured and then sit in secure storage waiting for a sibling (Ab), or vice versa for a long-lead purchase. Read PBS branches as a *dependency* structure, not a schedule — which is precisely why front-loaded planning is load-bearing.

## Anti-patterns

The source frames the following as pitfalls to avoid (it is explicitly a "best practices and pitfalls" document):

- **Letting a single discipline dominate the design.** The named failure mode behind the entire "two cultures" framing: favoring one system or subsystem at the expense of another instead of balancing across them. The systems engineer's job is described as *constantly validating* that the operational goals will still be met while no specialty runs away with the design.

- **Overlooking the technical-management processes "because the example skips them."** The source warns directly: although processes 10–17 are omitted from the narration of the worked example for simplicity, they are *always in effect*, can *generate additional requirements*, and can *significantly impact the design* (it singles out risk management, interface control, and HSI). Treating them as optional or deferrable is the pitfall.

- **Concluding an integrated product is good because its parts passed.** Explicitly called out: verifying the component models is *not* sufficient grounds to assume the integrated product will work — incomplete interface requirements and wrong design assumptions are named as the sources of the surprise. The only sound conclusion comes from V&V *at each integration stage*.

- **Decomposing to academic completeness during a feasibility phase.** The source flags driving every system down to circuit-board level in Pre-Phase A / Phase A as a waste of time and money — feasibility, not completeness, is the phase's purpose.

## Key Takeaways

1. **SE is sold as a *way of thinking* first.** Before it is 17 processes, the discipline is the holistic balancing of conflicting constraints so that the whole is coherent — value created chiefly by how the parts interconnect.
2. **The engine's processes 10–17 are crosscutting *tools*, not the next steps after 1–9.** This tool/task split is the cleanest way to read the engine diagram correctly.
3. **The phase cadence is specific and worth memorizing:** development processes run five engine cycles (Pre-A → D), management processes run seven (Pre-A → F), and Phases C/D are split so design runs in C and realization in D.
4. **Iterative ≠ recursive.** Iterate to correct a discrepancy on the *same* product; recurse to move down a tier, up a tier, or forward a life-cycle phase.
5. **The AS9100 crosswalk is the bridge artifact** for any AS9100-certified Center or contractor — it shows NPR 7123.1 conformance maps cleanly onto the quality system, process by process.
6. **Implementation is a bottom-only event; everything above is integration**, and integration-level V&V is non-negotiable because parts passing does not imply the whole passes.
7. **Know when to stop decomposing.** Converge the first-order trade space and retire high-risk requirements; deeper is waste. PBS branch length is a dependency map, not a timeline.

## Connects To

- **`nasa-se-handbook` (base pack), Chapters 1 and 3** — the companion treatment of sections 2.0–2.3. Read that pack for the canonical definitions and the straight description of the passes; read this chapter for the overlap mechanics, the phase cadence, the AS9100 crosswalk, and the judgment-level reading of the STS example.
- **NPR 7123.1 (NASA Systems Engineering Processes and Requirements)** — the normative source of the 17 processes, the engine, and the exact `iterative`/`recursive` definitions quoted here.
- **NPR 7120.5 / 7120.7 / 7120.8** — the three program/project-management requirement documents that determine which management relationship and vocabulary govern a given project type (space flight / IT & infrastructure / research & technology).
- **AS9100** — the commercial aerospace quality-management standard that Table 2.1-1 crosswalks against, relevant wherever a Center or contractor is AS9100-certified.
- **Expanded Guidance §§4.0, 5.0, 6.0** — the detailed chapters for the system-design, product-realization, and technical-management process sets respectively; the "6105 paragraph labels" on the engine diagram point directly into them.
- **Expanded Guidance §2.5 (Cost-Effectiveness), §2.6 (HSI), §2.7 (Competency Model)** — downstream sections of this same source chapter, carried in their own pack chapters; the cost-effectiveness "locked-in early" curve and the HSI-in-the-critical-path argument extend the fundamentals established here.
- **INCOSE / ISO/IEC/IEEE 15288** — the broader systems-engineering canon NASA's 17-process model is an interpretation of (see the `sebok` skill for the wider body of knowledge).

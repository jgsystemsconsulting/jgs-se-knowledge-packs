# Chapter — Project Definition Tasks (Tasks 1-3: Customer Request, WBS, Technical Description)

## Core Idea

A cost estimate is only as trustworthy as the understanding it rests on. The NASA Cost Estimating Handbook (CEH) v4.0 opens its estimating process with a deliberately front-loaded "Project Definition" stage built from three sequential tasks: receive and understand the customer's request, build or obtain a Work Breakdown Structure (WBS), and define or obtain the project technical description. The governing logic is that estimators cannot price what they have not first scoped, bounded, and described in a shared vocabulary. These three tasks convert a vague request into a structured, commonly-understood definition of *what is being estimated* — the prerequisite for choosing any methodology. Skipping or short-changing definition does not save time; it relocates the error into the estimate itself, where it is harder to detect and more expensive to correct.

## Frameworks Introduced (exact source names, when/how)

- **CADRe (Cost Analysis Data Requirement)** — introduced in Task 1 as a three-part document capturing programmatic, technical, and cost data for NASA-funded space missions in a single artifact. The CEH notes it is produced six times across a project's life cycle, aligned to major milestones (the source lists SRR, CSR or Project PMSR, PDR, CDR, SIR, Launch, and EOM). Begun in 2005, the CADRe initiative exists to systematically collect and archive historical data so future estimates have a defensible empirical basis. It recurs in Task 3 as a ready-made technical baseline an estimator can reuse.
- **ONCE (One NASA Cost Engineering database)** — named as the repository where completed CADRes live, enabling fast search and retrieval; in Task 3 it is where end-of-contract actual costs and technical parameters get ported back to update NASA cost models.
- **WBS (Work Breakdown Structure)** — the central framework of Task 2. The CEH grounds its authority in **NPR 7120.5E** (NASA Space Flight Program and Project Management Requirements), which confirms the WBS as a key project-management element and mandates a standard WBS for all NASA space flight projects.
- **NASA Level 2 Standard Space Flight WBS** — shown in the source as Figure 4; required for all NASA space flight projects and standardized only down to Level 2.
- **CADRe Standard WBS** — a more detailed recommended structure (presented in the source's end-of-section box) used for breakouts below Level 2.
- **Supporting reference documents named for WBS preparation:** the NASA Systems Engineering Handbook (cited for WBS policy/process, Section 6.1.2.1), the NASA Work Breakdown Structure Handbook (SP-2010-3404), MIL-HDBK-881C (DoD work breakdown structures for defense materiel items), and NPR 7120.5E.
- **NSM numbering scheme** — named as the numbering convention an Agency project's WBS must use, and which must correlate exactly through Level 7 to the NASA Core Financial System accounting structure.
- **Four Critical Elements** — shown in the source as Figure 3: resources, data, schedule, and expectations. These must be understood and agreed between estimator and decision maker before a methodology is selected.

## Key Concepts

- **The four critical elements as an agreement, not a checklist.** The CEH frames *resources, data, schedule,* and *expectations* as items to be negotiated and jointly agreed before any estimating method is chosen. Each carries its own diagnostic questions: data asks what is needed, whether it is available, what the fallbacks are, and whether non-disclosure agreements apply; resources ask how many people and how much budget are required versus available; schedule asks whether the allotted time is sufficient given resources and data; expectations probe the intended outcome and usage of the estimate across the customer, team, and Agency.

- **Acceptance gating in Task 1.** Before work begins, the supervisor of the cost group judges whether adequate resources exist to take the assignment. The estimator then sizes the workload (estimate type, due dates, relative priority). If accepted, the requester is notified and an estimator is assigned; if the request is problematic, it is negotiated with the requester rather than silently absorbed.

- **The WBS as a coverage guarantee.** The handbook defines the WBS's purpose as dividing the project into manageable pieces to enable planning and control of cost, schedule, and technical content. Crucially, it provides *full coverage without double counting* — each element represents the cost to do that work. The WBS underpins planning and scheduling, cost estimation and budget formulation, scope and statement-of-work definition, status reporting (including EVM and Estimate at Completion), and the creation of products like the Systems Engineering Management Plan (SEMP).

- **Product-oriented structure enables apples-to-apples comparison.** The source stresses that costs collected in a product-oriented WBS can be compared against historical data for the same products. Standardizing at higher levels (Levels 1 and 2) enables comparison to heritage programs — a recurring theme tying definition back to empirical grounding.

- **Build-out by maturity.** Activities for the WBS task: start from the NASA standard flight project WBS (only to Level 2), then define elements to the lowest level appropriate to the estimate's maturity. Below Level 2, use the CADRe standard as a reference for lower breakouts. Build a WBS dictionary to define elements, and ensure consistency with other project functions such as scheduling. The cost estimator owns the cost WBS and is responsible for mapping it back to the standard WBS. Level 3 typically goes to individual instruments and spacecraft subsystems — the level used for hardware and software estimating.

- **The technical baseline as a common definition.** Task 3 establishes a baseline document giving quantitative and qualitative descriptions of project characteristics from which costs are derived. Its strategic value: it ensures estimates produced *separately* by the Project Offices and by independent review organizations rest on the *same* definition of the system. It must also flag any area with major cost impact — explicitly including risks — so the estimator addresses it.

- **Document type scales with context.** The technical description's form depends on time available, project size, technical information on hand (including requirement thresholds and goals), and life-cycle phase. Small or early-phase projects may need only a simple data sheet of technical requirements to support a Rough Order Magnitude (ROM) estimate.

## Mental Models

- **Define-before-price.** Definition is not preamble; it is the load-bearing first stage. The three tasks exist so that resources, data, schedule, and expectations are settled and the system is described in shared terms *before* methodology selection.

- **One definition, two independent estimators.** The technical baseline exists precisely so the Project Office estimate and the independent-review estimate can diverge in *method* while sharing the same *object*. Without a common baseline, any disagreement between the two becomes uninterpretable — you cannot tell whether they priced differently or simply priced different things.

- **The estimator as insightful questioner.** Early in the life cycle, unknowns dominate. The CEH casts the estimator not as a passive recipient but as someone who asks questions that surface decisions project staff might not yet have considered — maintenance concept, testing strategy — and who raises personnel, schedule, technology, and cost-driver issues that materially affect risk. (This is the natural seam where this pack pairs with **nasa-risk**: the definition tasks deliberately surface the risk areas that the risk-management discipline then carries forward.)

- **Standardization is a future-self investment.** Building a WBS that mirrors or easily maps to the CADRe structure is described as a recognized best practice because it saves level-of-effort later. Likewise, feeding data into CADRe and ONCE is an investment that pays off in better future estimates. Consistency now buys defensibility and comparability later.

- **Coverage without double counting.** A useful test for any decomposition: every piece of work appears once and only once. The WBS is the instrument that makes this property checkable.

## Anti-patterns

The source does not frame its guidance as named anti-patterns, so none are asserted here. The closest cautions the CEH states explicitly are advisory rather than labeled failures: a WBS derived from the NASA Level 2 standard may not map cleanly to the estimating structures inside commercial tools, so an estimator should know the intended tool in advance and be prepared to provide a mapping back to the project WBS where structures differ; and data gathering must not be treated as less important in later phases, where overlooking any element can still distort the outcome.

## Key Takeaways

- The CEH's estimating process begins with a three-task Project Definition stage: understand the request, build/obtain a WBS, and define/obtain the technical description — done in that order and for a reason.
- Four critical elements — resources, data, schedule, expectations — must be jointly agreed between estimator and decision maker before any methodology is chosen.
- Task 1 includes an explicit acceptance/negotiation gate: the cost group decides whether it has the resources, sizes the workload, and renegotiates problematic requests rather than absorbing them.
- The WBS provides full coverage without double counting, is mandated by NPR 7120.5E, standardized to Level 2 (Figure 4), and extended below Level 2 via the CADRe standard; the estimator owns the cost WBS and maps it back to the standard.
- A WBS dictionary, NSM numbering, and exact correlation through Level 7 to the NASA Core Financial System are part of doing the WBS properly for an Agency project.
- The technical baseline gives one common definition of the system so Project Office and independent-review estimates are comparable, and it must surface any major cost-impact area, risks included.
- CADRe and ONCE form the empirical backbone: CADRe captures programmatic/technical/cost data at six milestones; ONCE stores it and receives end-of-contract actuals to update cost models.
- Documentation depth scales with time, size, available information, and life-cycle phase — a ROM may need only a simple technical-requirements data sheet.

## Connects To

- **nasa-risk (pairs with):** Task 3 mandates that the technical baseline identify any area of major cost impact, explicitly naming risks; Task 1 charges the estimator with raising cost-driver and risk issues during early-phase questioning. Project definition is where the risks that nasa-risk manages are first identified and recorded — read the two together.
- **WBS Handbook / SEBoK / 15288 systems-thinking content:** The WBS as a hierarchical, coverage-complete decomposition aligns with broader systems-engineering decomposition practice; the CEH cites the NASA Systems Engineering Handbook (Section 6.1.2.1) and the NASA WBS Handbook (SP-2010-3404) as authorities.
- **DoD cost / acquisition packs:** The CEH names MIL-HDBK-881C (DoD work breakdown structures) as a peer reference, a natural bridge to defense-side WBS and cost-estimating material.
- **Earned Value Management:** The WBS is positioned as the structure under EVM and Estimate at Completion reporting, linking project definition to in-execution performance measurement.
- **Downstream estimating chapters:** This definition stage is the gate to methodology selection — the four critical elements must be settled here before the estimating-method chapters of the CEH apply.

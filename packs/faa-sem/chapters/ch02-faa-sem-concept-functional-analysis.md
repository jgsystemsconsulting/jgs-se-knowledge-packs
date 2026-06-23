# Chapter — Operational Concept Development and Functional Analysis

> Civil-agency SE process companion to NASA and DAU. This chapter renders the FAA Systems Engineering Manual's front-end processes — how a perceived service gap becomes a vetted concept, and how that concept is then dissected into solution-agnostic functions. The mechanics rhyme with NASA and DAU front-end practice, but the artifacts, gating bodies, and life-cycle phases are FAA-specific.

## Core Idea

The FAA SEM treats the path from "we think there's a problem" to "we have an analyzable solution" as two coupled but distinct disciplines: **Operational Concept Development** and **Functional Analysis**. The first answers *what the solution is for and how it will be used*; the second answers *what the solution must do*, deliberately deferring *how*.

Operational Concept Development is framed as proposing how FAA resources — people, technology, and procedures — combine to satisfy well-defined needs. It is grounded in agency policy and planning artifacts (the NAS Enterprise Architecture, the Acquisition Management System, the NextGen Implementation Plan, Infrastructure Roadmaps) plus outside research. It runs as two interleaved activities — Concept Development and Concept Validation — performed iteratively until candidate solutions are mature enough to enter investment analysis. The end product is a fully vetted Concept of Operations (ConOps) plus preliminary analyses of shortfalls, cost, benefit, and risk, all expressed from the user's point of view.

Functional Analysis then transforms the capabilities described in that ConOps into a functional view of a system that could deliver them. Its discipline is to stay *implementation-free*: because any given function can be performed by more than one system element, the SEM stresses that functions themselves are not allocated. Instead, functions drive requirements, and *requirements* get allocated to a physical architecture. This separation is what lets the FAA avoid locking onto a single-point solution before the problem is fully understood.

## Frameworks Introduced

**Operational Concept Development (SEM Section 3.1).** The umbrella process. Inputs are a perceived need or gap and NextGen Operational Improvements; outputs are a preliminary shortfall analysis, a vetted ConOps, a benefits analysis, a preliminary safety assessment, and a list of research issues. It runs mostly within the AMS Service Analysis and Strategic Planning phase, with the supporting activity Research for Service Analysis (RSA) carrying the concept-development load.

**Concept Development and Concept Validation.** Presented as two separate, often parallel processes. Development progresses through defining and analyzing candidate solutions, testing feasibility, and building an integrated concept evaluation environment. Validation runs underneath to confirm the *right* operational solutions are being pursued, quantifying and qualifying expected benefits and feeding results back to the user community to decide whether the concept or the validation plan needs to change. Models and prototypes are cited as typical validation products.

**Concept of Operations (ConOps).** The primary repository for a concept's assumptions, constraints, and operational environment, describing operational and functional characteristics within the intended environment. The SEM notes concepts can exist at multiple levels — from a Service-level concept that touches the overall NAS ConOps down to a Solution-level concept describing a single technical improvement — and insists lower-level concepts stay consistent with the higher-level ones they sit under. First-draft ConOps content includes traceability to relevant Operational Improvements, a clear problem statement, assumptions and constraints, the operational environment, and a benefits summary. The term ConOps is used at every level, enterprise/NAS down to solution (often called "system-level," though the SEM cautions the solution is not always a system).

**Operational Improvements (OI) and Operational Sustainments (OS).** The forms in which shortfalls are documented inside the ConOps — initiatives to improve or to sustain existing operations, respectively.

**Concept Maturity Levels (CML 1–4).** A maturity scale used to give everyone a shared read on a concept's developmental status, and concretely to drive funding allocation, align NextGen research priorities, and track progress. CML 1 explores multiple candidate solutions and ends with one selected concept; CML 2 produces a draft ConOps and initial concept-level requirements; CML 3 builds detailed operational scenarios and an integrated concept prototype (e.g., a human-in-the-loop simulation or field demonstration) for advanced validation; CML 4, reached only if research did not transition straight to program initiation after CML 3, is the final refinement and validation phase. The SEM defers detail to the FAA Concept Development and Validation Guidelines.

**Functional Analysis (SEM Section 3.2).** Examines the functions, sub-functions, and interfaces that accomplish a solution's mission. Inputs are the ConOps, the operational context diagram, NAS-level operational requirements, policy and standards, interface control documents, and (if relevant) legacy system documentation. The activity defines functional boundaries, top-level functions, constraints, and interfaces, then decomposes functions. The output is a Functional Analysis Document (FAD) containing the Functional Architecture.

**Primitive Requirement Statement (PRS).** The FAA's stated preference for the function-to-requirement path: translate a function into a PRS, mature the PRS into a requirement, then allocate the mature requirement to a physical-architecture entity.

**Functional Flow Block Diagram (FFBD) and N-squared (N2) diagram.** The FAA's complementary preferred diagramming pair. A complete functional model has to capture both the "control" aspect (sequencing — the FFBD) and the "data" aspect (interfaces — the N2). The SEM notes the enterprise-architecture SV-4 carries similar information, but FFBD is preferred for engineering work.

## Key Concepts

**Shortfall analysis.** A shortfall is the gap between future service needs and current capability. The analysis gathers service-environment information, examines business/technology/organizational/process/personnel issues with their assumptions and risks, checks the gap against FAA strategic and performance goals, and produces a Preliminary Shortfall Analysis. At this early stage a shortfall is stated as a *level of service improvement*, not as specific performance numbers. Whether a shortfall already lives in the ConOps determines its routing: in-scope shortfalls decompose into operational requirements and investment initiatives; out-of-scope ones require deciding what development or validation work is needed.

**Concept-level requirements as proto-requirements.** The ConOps carries very preliminary operational requirements that get progressively refined later during Requirements Analysis. The front end is not where requirements are finalized — it is where they are seeded.

**Function defined.** A function is a characteristic action needed to achieve a system objective or stakeholder need, named as an action verb plus a noun or noun phrase (the SEM uses everyday examples like "read book" or "go to store"). Each function sits inside the system's environment and is delivered by one or more system elements built from equipment (hardware, software, firmware), people, and procedures.

**Implementation-free decomposition.** Functional Analysis starts from a high-level need and recurses through successively finer layers until the system's desired behavior is understood well enough to define functional requirements completely and correctly. The three stated reasons to do it: decompose functions toward design elements, expose relationships among functions and between functions and external users, and arrive at a complete functional requirement set.

**The seven-step perform-functional-analysis sequence.** Define the functional boundary (stimuli and responses, in quantitative terms); identify and document each top-level function (best read off the context diagram's inputs and outputs); define implementation constraints from stakeholders or unavoidable limits (e.g., FAA standards); define external and functional interfaces; verify results against the ConOps; validate results against stakeholder expectations; and document everything in a Functional Architecture Document. Organizing aids called out include the functional hierarchy, FFBDs, N2 diagrams, and a lexicon of functions and data elements.

**FFBD mechanics.** A multi-tier, time-sequenced diagram where each verb-noun function is a node, directed lines run left to right, and logic symbols express sequencing. The "control" rule: a function cannot begin until its predecessor(s) finish — a "display targets" function waits on "detect targets." Beyond being *enabled* by completion, a function may also need to be *triggered* by an input arriving (the data side, captured by the N2). The three logic symbols are AND (all paths required), Exclusive OR (one path but not all), and Inclusive OR (one, some, or all paths — drawn as a composite of AND and Exclusive OR). Each FFBD must carry administrative data: creation date, author/organization, and the diagrammed function's unique decimal-delimited number and name.

**N2 mechanics.** An N×N matrix with entities (functional or physical) on the diagonal and interface inputs/outputs in the off-diagonal cells; a blank cell means no interface. Data flows clockwise — a value to the right of F1 is data F1 sends downstream, a value to the left of a function is feedback. The diagram is finished when every entity has been compared against every other, and it is reapplied at each lower decomposition level. Its payoff is twofold: cataloguing interfaces and pinpointing where interface conflicts might arise so integration goes smoothly. Same administrative-data requirements as the FFBD.

**The Functional Architecture Document (FAD).** The seven-part output: context diagrams (lower-level boundaries with more functional detail than the operational context diagram), functional hierarchy, functional flow, N2 diagrams, list of functional interfaces, lexicon, and acronyms/abbreviations. The SEM also gives a recommended FAD outline running from introduction and operational context through the functional architecture to references, definitions, and acronyms.

**Alternative diagram notations.** While FFBD is preferred, functional flow can also be documented with IDEF0 diagrams (which model input-to-output transformation; the A-0 page is the context diagram, and the OV-5 operational activity model is an IDEF0 diagram useful for finding system functions) or with the SV-4 enterprise-architecture artifact, which the functional analysis directly feeds.

## Mental Models

**What it is for vs. what it does vs. how it does it.** A three-way split runs through the whole chapter. The ConOps fixes *what the solution is for and how it will be used*; Functional Analysis fixes *what it does*; only later does physical architecture address *how*. Keeping these lanes separate is the load-bearing idea.

**Functions describe; requirements get allocated.** Because one function can be served by several elements, you never hang a function on a box. You convert functions to requirements (via PRS), and requirements are what map onto the physical architecture. This is the SEM's stated guard against premature commitment.

**Control plus data equals a complete model.** Neither the FFBD nor the N2 is sufficient alone. Sequencing (control) without interface definition (data) — or vice versa — leaves the functional model incomplete. The two diagrams are designed as complements, not alternatives.

**Maturity as a shared currency.** CMLs exist so that funding bodies, researchers, and engineers all read the same number and mean the same thing by it. Maturity is treated as something to be communicated and budgeted against, not just an internal engineering judgment.

**The FAD is a living document, not a one-time deliverable.** The SEM is explicit that once the FAD is JRC-approved it must not be left in isolation while requirements and architecture evolve around it. As requirements update (in the iPR/fPR) and as architecture views add functions or interfaces, the FAD is re-evaluated and updated — and this continues through Investment Analysis, Solution Implementation, and In-Service Management (where Tech Refresh and System Life Extension Programs can force functional changes that trace high enough to matter).

## Key Concepts in Life-Cycle Context

Both processes are anchored to specific AMS phases rather than treated as abstract. Operational Concept Development runs in Service Analysis and Strategic Planning (via RSA). Functional Analysis begins preliminarily in Service Analysis — supporting the Recommended Changes to Enterprise Architecture and the Preliminary Shortfall Analysis, including checking whether needed top-level functions already appear in the SV-4 — and is mostly executed during Concept and Requirements Definition, where the final FAD is produced and reviewed by the Joint Resources Council (JRC). The approved FAD then anchors alignment of preliminary requirements and the SV-4 view, and is maintained through later phases. Contractors are expected to take a significant role in functional analysis once Solution Implementation begins.

## Key Takeaways

- The front end is two coupled disciplines: concept (what it's for / how used) and functional analysis (what it does), with physical "how" deliberately deferred.
- Operational Concept Development pairs Concept Development with continuous Concept Validation; its capstone is a vetted ConOps plus preliminary shortfall, benefit, safety, and risk analyses.
- Shortfalls are gaps between future need and current capability, expressed early as service-improvement levels and documented in the ConOps as Operational Improvements and Operational Sustainments.
- CML 1–4 give a shared maturity vocabulary that drives funding, research prioritization, and progress tracking.
- Functional Analysis is implementation-free; functions are not allocated — requirements derived from functions (via PRS) are.
- The FAA prefers complementary FFBD (control/sequencing) and N2 (data/interfaces) diagrams; a complete functional model needs both.
- The seven-part Functional Architecture Document is the durable output, and it must be kept aligned with requirements and architecture across the rest of the life cycle.

## Connects To

- **Requirements Analysis / Requirements Management (later SEM sections):** concept-level requirements seeded in the ConOps and the functions produced here feed forward into the preliminary Program Requirements Document (pPRD) and the maturing requirement set.
- **NASA Systems Engineering Handbook & DAU SE Guidebook:** ConOps development, functional decomposition, FFBDs, and N2 diagrams are shared front-end practice; this pack supplies the civil-agency (AMS/NAS/JRC) framing and artifact names that differ from the defense and space lineages.
- **NAS Enterprise Architecture / SV-4 / OV-5:** functional analysis both consumes EA context and directly contributes to the SV-4 artifact, with OV-5 (an IDEF0 model) usable to help identify system functions.
- **NextGen Implementation Plan:** the source of Operational Improvements that act as inputs and benefit references for concept development.
- **Safety processes (SIA, OSA, OSED, OHA):** preliminary safety assessment begins inside concept development and matures toward the operational safety assessment package.
- **Cross-cutting Technical Methods (SEM Section 3.5):** models, simulations, and prototypes used for concept validation are detailed there.

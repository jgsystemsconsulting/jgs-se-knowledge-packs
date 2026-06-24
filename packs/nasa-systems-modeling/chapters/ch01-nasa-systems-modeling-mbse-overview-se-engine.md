# Chapter 1 — MBSE Overview and the NASA SE Engine

## Core Idea

This handbook (NASA-HDBK-1009A) exists to answer one question: how do you take system modeling done in SysML and wire it directly into the systems engineering processes NASA already mandates under NPR 7123.1? Rather than treating modeling as a parallel activity that produces pretty diagrams off to the side, the handbook positions the model as the source from which standard SE work products are generated. The model captures the definitions and relationships of the system of interest; the diagrams, tables, and matrices drawn from that model are how the SE processes get implemented and how the artifacts feeding program and project technical reviews get produced.

The scope is deliberately bounded. The handbook covers modeling support for just four of NASA's common technical processes: defining stakeholder expectations, defining technical requirements, and then verifying and validating the product. That selection was not arbitrary: it came out of a survey run through NASA's Agency MBSE Community of Practice, so it reflects where practitioners across the agency saw the most value in formalizing modeling guidance first.

A foundational caveat runs through the whole document and should anchor how you read everything that follows: the modeling **method** is tool-agnostic. The text leans on SysML v1.7 to illustrate, but the handbook is explicit that the underlying metamodel (defined later, in section 7) can be expressed in any modeling language. The companion model that ships with the handbook happened to be built in MagicDraw, but that is an implementation choice, not an endorsement or a requirement. The version under discussion is Revision A; treat it as the current baseline.

## Frameworks Introduced (exact source names, when/how)

The chapter introduces several named frameworks and standards, each playing a distinct role:

- **NPR 7123.1, NASA Systems Engineering Processes and Requirements.** The governing document. It gives a generic description of how SE is applied across NASA and sorts the common technical processes into three sets — those for system design, those for product realization, and those for technical management. Everything in the handbook traces back to it. The handbook does not replace or override NPR 7123.1 — it shows how to model in support of it.
- **The NASA Systems Engineering Engine (the "SE Engine").** Drawn from NPR 7123.1D, Figure 3-1, and reproduced in the handbook as Figure 4.1-1. The Engine illustrates the three process sets, their interactions, and their flows. It is described as the *means* by which NASA does systems engineering, comprising 17 common technical processes.
- **NASA/SP-2016-6105, NASA Systems Engineering Handbook.** The deeper reference for the SE Engine and the 17 processes; the handbook points readers to its Section 2.1 for the full treatment and reuses its System Design Process figure (from Revision 2, Figure 4.0-1).
- **SysML (Systems Modeling Language), OMG, version 1.7.** The illustrative modeling language. INCOSE recognizes SysML for specifying, analyzing, designing, and verifying complex systems, and the handbook adopts it for its examples. SysML is noted as a subset of UML 2 with some extensions, UML 2 being the graphical language built for software.
- **OOSEM — Object-Oriented Systems Engineering Method (an INCOSE standard).** Used to source the two model-specific steps the NASA SE Engine itself does not contain: "Model Planning" and "Setting Up the Model." OOSEM details an SE process similar in shape to NASA's, plus these model-specific additions. More detail lives in Appendix B.
- **MBSE Grid.** The framework chosen for organizing the model's elements and relationships. The handbook tailors the MBSE Grid to the NASA SE Engine, putting NASA technical processes on the rows and the SysML pillars on the columns. The Grid originates in INCOSE work (Morkevicius et al., 2017) and is expanded on in Appendix B.
- **The INCOSE definition of MBSE.** The handbook adopts INCOSE's formulation: MBSE is the formalized application of modeling to support requirements, design, analysis, and V&V activities, starting in conceptual design and carrying through development and the later life-cycle phases.

## Key Concepts

**Processes versus products.** The handbook is careful to separate the two. The SE Engine and its 17 common technical processes are *how* the work gets done; the products — things like a ConOps Report, Requirements Specifications, V&V Plans — are *what* results. NPR 7123.1, Table 5-1 holds the full list of primary work products. For the four in-scope processes, the handbook (in Table 4.1-1) commits to covering a specific product set: stakeholder identification and expectations, Concept of Operations, Measures of Effectiveness, Technical Requirements, Measures of Performance, Technical Performance Measures, plus the verification and validation requirements, planning, and results/reports.

**The three aspects of MBSE.** This is the organizing spine of the overview. MBSE is decomposed into three things, and the handbook treats each separately:

1. *Modeling language* — the means of describing the system with graphical constructs, analogous to how programming needs a programming language and human communication needs a natural language. The handbook uses SysML.
2. *Modeling methodology* — the step-by-step approach for actually building and using the model. A language gives you structure and rigor but not a procedure; the methodology supplies the procedure.
3. *Modeling framework* — the approach to organizing the system's elements and relationships within the model.

**SysML's nine diagram types and four pillars.** SysML offers nine diagram types: four behavior diagrams (activity, sequence, state machine, use case), one requirement diagram, and four structure diagrams (block definition, internal block, package, parametric). These are conventionally grouped into four *modeling pillars* — structure, behavior, requirements, and parametrics. Structure handles logical and physical layers (systems, subsystems, components, interfaces); behavior covers functionality, interactions, response, and information/data flow; requirements covers specifications and V&V; parametrics covers constraints and mathematical statements. The pillars are not silos — together they build a shared context across the whole model, integrating elements and diagrams so SE products can be generated.

**The methodology = NASA SE Engine plus two steps.** The handbook's methodology follows the NASA SE Engine but inserts two model-specific steps the Engine itself omits. "Model Planning" lands inside Technical Process 10 (Technical Planning). "Setting Up the Model" lands at the very start of the System Design Process as "Step 0." Both are borrowed from OOSEM and detailed in sections 5 and 6.

**The framework = MBSE Grid tailored to NASA.** The Grid is a matrix: NASA technical processes down the rows, SysML pillars across the columns. Critically, the Grid only shows technical processes 1 through 9 — it deliberately excludes the Technical Management Processes (10 through 17). A metamodel (section 7) relates the modeling elements and relationships across all four pillars, producing the content for the model's diagrams and tables, and the Grid's cross-sections become the slots where those diagrams and tables get organized (Appendix C shows a populated example).

## Mental Models

**Language, methodology, framework are three independent dials.** The cleanest way to hold the chapter is to keep the three aspects of MBSE distinct. The language tells you *what symbols mean*. The methodology tells you *what order to do things in*. The framework tells you *where things go*. Confusing them is the usual trap — a language does not give you a procedure, and a procedure does not tell you how to organize the result. The handbook's tool-agnostic stance is exactly an assertion that the language dial can be swapped (SysML out, something else in) without disturbing the methodology and framework dials, because the metamodel sits underneath all three.

**The model is the well; work products are buckets drawn from it.** Don't picture diagrams as the deliverable. The system model is the single reservoir of definitions and relationships; diagrams, tables, and matrices are views *pulled from* that reservoir to satisfy a specific SE process and feed a specific review. This is the conceptual difference between document-centric SE and model-based SE that the rest of the handbook operationalizes.

**The Grid is a map with the rows you'd expect and one you wouldn't.** When you internalize the MBSE Grid, remember it intentionally stops at process 9. The technical *management* processes (10–17) are not laid out on the Grid even though one of them, Technical Planning (10), is where Model Planning happens. So the Grid is a design-and-realization map, not a whole-lifecycle map; management activities sit alongside it rather than inside its cross-sections.

**"Means" versus "what results" as a discipline.** Carry the process-versus-product split as a habit of mind. Whenever you reference a SE activity, ask whether you're naming the engine that turns or the artifact it stamps out. NPR 7123.1 keeps these in separate places (the Engine for the means, Table 5-1 for the products), and the handbook mirrors that separation deliberately.

## Key Takeaways

- The handbook's mission is integration: SysML system modeling plugged into the NPR 7123.1 SE processes, with the model serving as the source for standard SE work products.
- Scope is four processes — defining stakeholder expectations, defining technical requirements, plus product verification and product validation — chosen via a NASA Agency MBSE Community of Practice survey.
- The method is tool-agnostic; SysML v1.7 and the MagicDraw companion model are illustrations, and the metamodel in section 7 can be rendered in any modeling language. This is Revision A.
- MBSE has three aspects: language (SysML here), methodology (NASA SE Engine plus the OOSEM-derived Model Planning and Setting-Up steps), and framework (the MBSE Grid tailored to NASA).
- SysML supplies nine diagram types grouped under four pillars — structure, behavior, requirements, parametrics — that jointly build one integrated model context.
- The MBSE Grid maps NASA technical processes 1–9 against the four SysML pillars; processes 10–17 (technical management) are excluded from the Grid.
- Keep processes (the means, the SE Engine's 17 processes) distinct from products (the artifacts, listed in NPR 7123.1 Table 5-1).

## Connects To

- **NPR 7123.1 and NASA/SP-2016-6105** — the governing requirements and the deeper SE Engine reference; the handbook supports them rather than supersedes them, and existing Agency guidance always takes precedence (conflicts resolved by the delegated Technical Authority).
- **OOSEM (INCOSE)** — origin of the Model Planning and Setting-Up-the-Model steps; expanded in Appendix B and detailed in handbook sections 5 and 6.
- **MBSE Grid (Morkevicius et al., INCOSE)** — the framework tailored here; Appendix B for background, Appendix C for a populated grid.
- **The section 7 metamodel** — the tool-agnostic core that lets the framework relate elements across all four SysML pillars and makes the language swappable.
- **SEBoK and the INCOSE MBSE definition** — the broader systems-engineering canon the handbook situates itself within for terminology and the MBSE concept itself.
- **Downstream chapters** — model planning, model setup, the metamodel, model building with SysML examples, and diagram/table generation, each of which builds on the language/methodology/framework decomposition established here.

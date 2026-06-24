# Chapter 1: Introduction and Background — Agile vs. Waterfall and Core Frameworks

## Core Idea
Agile is iterative, incremental software development that prizes the early and continuous delivery of working software, evaluated each cycle for functionality, quality, and customer satisfaction. The GAO Agile Assessment Guide (GAO-24-105506) treats "Agile" as an umbrella for a family of methods — Scrum, Kanban, XP, Lean, DevOps, and others — rather than a single prescriptive process. Its contrast case is Waterfall, where requirements, design, development, and testing run in sequence; Agile runs those same activities concurrently in small iterations, using frequent reviews and customer feedback to keep the highest-value requirements in focus. The guide frames Agile primarily as a way to reduce technical, programmatic, schedule, and budget risk, and it sets out generally accepted best practices for Agile adoption, execution, and control rather than step-by-step "how-to" instructions.

## Frameworks Introduced
The chapter establishes the conceptual scaffolding the rest of the guide rests on and names several specific Agile frameworks via Table 1 (Description of Commonly Used Agile Frameworks).

- **The Agile Manifesto (Feb 2001)** — articulated by a group of 17 developers calling themselves the Agile Alliance; it states four value pairs that favor the first item over the second while still valuing both.
  - When/how introduced: presented as the historical and philosophical origin of Agile. The guide stresses that whatever frameworks an organization picks, its application should align with the Manifesto and the 12 principles.
- **The 12 Agile Principles** — the Alliance's elaboration of the Manifesto into twelve principles (e.g., satisfy the customer through early and continuous delivery; welcome changing requirements; working software as the primary measure of progress; self-organizing teams; regular reflection and tuning).
  - When/how introduced: listed in full as the operational expression of Agile values.
- **Waterfall** — the sequential model whose phases flow continuously from one to the next.
  - When/how introduced: used as the comparison baseline (Figure 1). A footnote traces it to Winston W. Royce's 1970 paper "Managing the Development of Large Software Systems," noting the paper never used the word "Waterfall," warned the sequential model was risky, and actually recommended iterative interaction between steps.
- **eXtreme Programming (XP)** — a process that pushes software best practices to the extreme, built on five values (communication, feedback, simplicity, courage, respect); pair programming and full unit testing are example practices.
- **Feature Driven Development (FDD)** — drives development from the functionality perspective through a defined sequence: build the overall model, build a feature list, then plan, design, and build by feature; uses practices such as Domain Object Modeling and individual code ownership.
- **Kanban** — encourages flow of work from commitment to delivery, limits work in progress to relieve bottlenecks, and uses a visual board whose columns represent activities (analysis, development, testing, deployment) with tasks pulled rather than pushed.
- **Scrum** — defines three core roles (product owner, development team, scrum master) and breaks work into time-boxed sprints with daily standups, an end-of-sprint demonstration to the product owner, and a retrospective.
- **Disciplined Agile (DA)** — a scalable decision framework spanning the whole product life cycle. Its stated characteristics put people first and learning at the center; it is hybrid in nature, covers delivery end-to-end, is driven by process goals and focused on the solution, runs on a risk-and-value life cycle, and stays aware of the wider enterprise.
- **Dynamic Systems Development Method (DSDM)** — formerly DSDM Atern, a rapid-development framework with eight principles and the MoSCoW prioritization technique (Must / Should / Could / Won't-have-but-would-like).
- **Large Scale Scrum (LeSS)** — a scaled version of single-team Scrum with one prioritized backlog, one definition of done, one product owner, and many cross-functional teams in a common iteration.
- **Scaled Agile Framework (SAFe)** — a framework for Agile at scale (described as of SAFe V6.0) offering guidance for roles and inputs across organizational levels, organized around ten principles such as taking an economic view, applying systems thinking, and decentralizing decision making.
- **Scrum@Scale** — coordinates multiple Scrum teams by grouping four to five into a "Scrum of Scrums" (with its own Scrum Master and Product Owner), repeating the pattern as the organization grows.
- **Scrumban** — a hybrid that keeps Scrum roles while using Kanban to visualize workload and improve flow; work is bounded by a work-in-progress limit rather than by the sprint.
- **Crystal** — a family of methodologies selected by team size and software criticality (the variant closest to Agile is Crystal Clear); it relies on trust and communication and allows individual freedom rather than dictating specific practices.
- **DevOps** — emphasizes collaboration among development, IT operations, and quality assurance for more frequent releases; considered an expansion of Agile across the whole product life cycle. "Infrastructure as code" is a common principle, and under DevSecOps security becomes the whole team's responsibility across every stage.
- **Lean Software Development** — applies lean-manufacturing principles to software through seven principles: eliminate waste, amplify learning, deliver fast, decide late, empower the team, build integrity in, and optimize the whole.

(The guide groups these into Agile-at-scale frameworks, hybrid frameworks, and related frameworks. Note: Figure 1 — the Agile-vs-Waterfall comparison diagram — is an embedded copyrighted image and is excluded here; the prose describes its meaning.)

## Key Concepts
- **Iteration and release**: an iteration is a predefined, time-boxed, recurring period in which working software is produced; a release is a planning segment of usable requirements.
- **Concurrent vs. sequential**: the defining structural difference is that Agile performs requirements, design, development, and testing concurrently in small iterations, whereas Waterfall performs them in sequence.
- **A framework is a structure, not a recipe**: the guide defines a framework as a basic structure to guide customers rather than a prescriptive process. Frameworks each carry their own terminology, are not mutually exclusive, and can be combined.
- **Agile is not inherently prescriptive — until you apply it**: as a concept Agile is non-prescriptive, but a specific organization's implementation may become prescriptive once defined.
- **Alignment over orthodoxy**: regardless of the specific frameworks and practices chosen, what matters is that the organization's application aligns with the Manifesto and the 12 principles.
- **"Customer" is context-dependent**: the customer may be the end user, or the customer and sponsor may be one and the same — the definition is organizationally and contextually determined.
- **Scope of applicability**: although the guide focuses on software, it states the best practices apply to any incremental development program — including hardware programs and managed services — regardless of the product or service delivered.
- **Why GAO wrote it**: federal IT investments (at least $100 billion annually) have a long record of cost overruns and schedule slippage; IT acquisition and operations management remains on GAO's High-Risk List. FITARA and OMB guidance push agencies toward incremental development that delivers new or enhanced functionality at least every six months, and this guide gives auditors and agencies criteria to assess Agile readiness and use.
- **Best-practice posture**: the guide presents high-level concepts of software development, contracting, and program management across the life cycle and addresses key risks without prescriptive steps; it is an update to the GAO-20-590G exposure draft and is meant to be periodically refreshed.

## Mental Models
- **Agile as a risk-mitigation instrument, not a productivity gimmick**: its central justification in this chapter is shrinking technical, programmatic, schedule, and budget risk by surfacing problems early. Collaborating with customers up front and adapting continuously limits the chance of pouring money into a failing program or outdated technology.
- **Working software is the yardstick**: progress is measured by working software each iteration, not by documents produced or phases "completed."
- **Discover, don't just plan**: Agile fits programs whose final product includes distinct features, some of which are discovered during the work rather than fully specified at the outset.
- **Frameworks are a toolkit, mixable to fit context**: because frameworks are non-exclusive and combinable (e.g., Scrumban = Scrum + Kanban), selection is a deliberate choice driven by the program's needs and the organization's culture and structure — and adoption may demand real cultural, structural, even physical-space change.
- **The Manifesto is the invariant**: frameworks come and go and may even diverge from the Manifesto in places (the guide notes Kanban applies "customer collaboration over contract negotiation" differently than time-boxed Scrum), but alignment to Agile values and principles is the constant test.

## Anti-patterns
- **Misapplication of Agile processes and methods**: the guide states that problems can arise from misapplying Agile, and points to GAO case findings — one program that never set outcomes for its Agile development, and the TIM modernization program, which left its Agile roles undefined, did not rank its system requirements, and never put automated capabilities in place. The named anti-pattern is adopting Agile in name while omitting its defining disciplines (clear roles, prioritized requirements, automation, outcome definition).

## Key Takeaways
1. Agile = iterative, incremental delivery of working software, continuously evaluated for functionality, quality, and customer satisfaction.
2. The structural contrast with Waterfall is concurrency: Agile interleaves requirements, design, development, and testing in small iterations instead of running them in sequence.
3. The Agile Manifesto (2001, 17 authors) and its 12 principles are the philosophical anchor; alignment to them matters more than allegiance to any single framework.
4. "Framework" means a guiding structure, not a prescriptive process — frameworks are non-exclusive and combinable, and selection should be deliberate and context-driven.
5. Table 1 catalogs many frameworks (Scrum, Kanban, XP, FDD, DA, DSDM, LeSS, SAFe, Scrum@Scale, Scrumban, Crystal, DevOps, Lean), grouped as at-scale, hybrid, or related.
6. The best practices target any incremental development program — software, hardware, or services — even though the guide focuses on software.
7. The guide's purpose is risk reduction and giving federal auditors and agencies criteria to assess Agile adoption, execution, and control; it is a non-prescriptive best-practices guide, updated from GAO-20-590G.

## Connects To
- **Later chapters of this pack**: adoption best practices (team dynamics, program operations, organization environment) are developed in chapter 3; execution and control concepts (requirements, acquisition strategy, monitoring) in chapter 4, expanded for requirements and contracting in chapters 5–6; cost/schedule/EVM in chapter 7; and metrics in chapter 8.
- **`gao-tra` pack**: shares GAO's "best practices guide" lineage and risk-identification framing (the Agile Guide explicitly cites the Cost Estimating, Schedule Assessment, and Technology Readiness Assessment guides as companions).
- **`sebok` / `dau-se-guidebook` packs**: position Agile/iterative development within the broader systems-engineering life-cycle and review canon.

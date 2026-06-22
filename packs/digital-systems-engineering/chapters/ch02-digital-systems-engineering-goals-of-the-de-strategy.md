# Chapter — Goals of the Digital Engineering Strategy

> Source: Huang et al., *Towards Digital Engineering: The Advent of Digital Systems Engineering* (arXiv:2002.11672, 2020), Section 2. CC BY 4.0. This chapter is grounded in the openly licensed arXiv preprint, not the paywalled journal version.

## Core Idea

The U.S. Department of Defense Digital Engineering Strategy (cited here as US DoD, 2018) has one organizing ambition: to render the systems an enterprise cares about as digital models, and then to let those models be authored, joined together, and consumed at every stage of the lifecycle. The connective tissue that makes this possible is an **Authoritative Source of Truth** — a shared, governed repository that all the models hang off. The authors decompose this ambition into five interlocking goals, and crucially they do not treat the goals as a flat checklist. They arrange them as a dependency stack, where the lower goals create the conditions that let the upper goals exist. Understanding the *relations* among the goals is the chapter's real payload: the workforce and IT foundations sit at the bottom, the trusted repository and formalized modeling sit in the middle, and the drive to absorb new digital technologies sits at the top as the force that keeps generating fresh demands on everything beneath it.

## Frameworks Introduced (exact source names, when/how)

- **DoD Digital Engineering Strategy (US DoD, 2018)** — introduced at the opening of Section 2 as the document whose central theme drives the entire discussion. The authors lean on it to enumerate the five goals and to quote its language about consolidated, trusted environments and right-data-to-right-person delivery. The source treats this strategy as the authoritative statement of intent for digital engineering.
- **Authoritative Source of Truth (AST)** — named throughout the section as the trustworthy knowledge infrastructure that hosts and shares standardized models, data, and other digital artifacts across the lifecycle. It is introduced first informally (Goal 2's subject) and then formalized with the AST acronym, appearing again in the closing list of core transformations.
- **The Goal Stack (Figure 2)** — the source presents a diagram, referred to as the relations among the five goals, that orders the goals from foundation to driving force. The chapter introduces it as the mental scaffold for reading the goals as layered dependencies rather than parallel tasks.

## Key Concepts

**The five goals.** The source lays them out in order, and each carries a distinct character:

- **Goal 1 — Formalized model lifecycle.** Described as the *fundamental* goal. It targets planned model creation, curation, integration, and use to support decision making. Concretely it calls for digitally representing the system of interest; establishing policy, guidance, rules, and standardized syntax, semantics, and lexicons so models can be developed and reused; capturing model provenance so that traceability can underwrite a judgment of trustworthiness for reuse; and curating a standardized model set inside the AST so different disciplines and organizations can collaborate and decide together across the lifecycle.

- **Goal 2 — The Authoritative Source of Truth.** Aims to stand up the trustworthy knowledge infrastructure that hosts and shares the standardized models, data, and artifacts that are traditionally walled off inside individual organizations or disciplines. The AST captures the history of how models evolve, maintains traceability, and propagates updated models and data outward to every affected system and entity so dependent activities stay coordinated. The source frames its purpose as getting the correct data to whoever needs it, for the intended use, at the moment it is needed. Stakeholder organizations are expected to wrap it in governance: access control limiting use to authorized users, use of the AST as the technical baseline for cost/schedule/performance decisions, support for technical review, and support for cross-team communication and collaboration.

- **Goal 3 — End-to-end digital enterprise.** Aims to establish a digital enterprise operating in a digitalized, connected environment that can rapidly innovate with and absorb advanced technologies — the source lists big data analytics, cloud computing, AI and machine learning, virtual and augmented reality, digital twins, digital manufacturing, 3D printing, and others — while also advancing human-machine interaction.

- **Goal 4 — Transformed IT infrastructure.** Aims to convert today's IT environment — characterized in the source as stove-piped, complex, and hard to manage, control, secure, and support — into a more consolidated, collaborative, trusted digital engineering environment. The target infrastructure must supply: secure connected information networks carrying computing and information flows across all security levels; the evolving DE methods, processes, and tools for visualization, analysis, model management, interoperability, workflow, collaboration, and extensibility; and cybersecurity that protects both the IT itself and intellectual property such as patents, copyrights, and trademarks, achieved through government-industry collaboration.

- **Goal 5 — Transformed culture and workforce.** Targets the human and organizational shift: advancing DE policies, standards, and guides; accommodating DE development and management; and building and preparing the workforce through training and education.

**The dependency ordering.** Read the stack upward from its base. At the very bottom sits Goal 5 — the organizational and human foundation on which every other goal rests. Goal 4 provides the IT basis. Goal 2 builds the AST repository, drawing support from Goal 4 and feeding Goal 1. Goal 1 formalizes modeling across lifecycle, disciplinary, and organizational boundaries, drawing support from Goal 2. Goal 3 sits on top, supported by Goal 1, and acts as the driving force whose pursuit of new technology continually generates fresh requirements for every goal below it.

**The three core digital transformations.** The section closes by distilling what sits at the heart of the strategy into three required shifts: digital representation of the system of interest (broadly construed to include not just the focal system and its components but also relevant processes, equipment, products, parts, functions, services, and neighboring systems in the operating environment); use of the AST as the repository and access portal for standardized models, data, and artifacts; and formalized model creation, curation, sharing, integration, and use across disciplinary, organizational, and lifecycle boundaries with AST support.

## Mental Models

- **Goals as a load-bearing stack, not a to-do list.** The most useful reframing in this section is that the five goals form a structural hierarchy. You cannot meaningfully pursue formalized modeling (Goal 1) without a repository to put the models in (Goal 2), which in turn needs the IT foundation (Goal 4), which only succeeds inside a workforce and culture prepared for it (Goal 5). Skipping a lower layer leaves the upper ones without support.

- **Goal 3 as the pump, not the base.** While Goals 5, 4, 2, and 1 build upward as foundations, Goal 3 is positioned as a driving force at the top. It is the goal that creates pressure — every new technology the enterprise wants to absorb generates new requirements that ripple back down to the modeling, repository, IT, and workforce layers. Think of it as the demand source that keeps the whole structure evolving.

- **Provenance as the currency of reuse.** The source ties model reuse to a chain of reasoning: provenance enables traceability, and traceability is what lets an engineer judge whether a model is trustworthy enough to reuse. Without recorded provenance, a model in the AST is just data; with it, the model becomes a reusable, accountable asset.

- **Right data, right person, right use, right time.** The AST's value is framed not as storage but as targeted delivery. The mental model is a propagation network: when a model changes, the consequences flow automatically to every dependent entity so that coordinated work stays in sync, rather than each team discovering the change later on its own.

## Key Takeaways

- The DoD Digital Engineering Strategy's central theme is digitally representing systems and connecting their models through an Authoritative Source of Truth across the whole lifecycle.
- The strategy comprises five tightly related goals: formalized model lifecycle (G1, the fundamental one), the AST repository (G2), an end-to-end digital enterprise (G3), transformed DE IT infrastructure (G4), and transformed culture and workforce (G5).
- The goals form a dependency stack: G5 and G4 are the human and IT foundations; G2 builds on G4 and feeds G1; G1 builds on G2; G3 sits on top of G1 as the driving force that issues new requirements downward.
- The AST is governed infrastructure — access-controlled, used as the technical baseline for cost/schedule/performance and technical review, and engineered to propagate updates to all affected entities.
- At its core the strategy demands three transformations: digital representation of the system of interest, use of the AST as the standardized-model repository and access portal, and formalized model work across disciplinary, organizational, and lifecycle boundaries.

## Connects To

- **Authoritative Source of Truth as a recurring backbone** — the AST introduced here is the shared concept that the rest of the digital-systems-engineering pack builds methods and tooling around; this chapter establishes why it sits at the center of every other goal.
- **MBSE and model-based practice** — the formalized model creation, curation, and reuse of Goal 1 is the strategic justification for the model-based systems engineering machinery treated elsewhere in the SE-standards landscape (e.g., the SEBoK MBSE material).
- **Digital twins and advanced technology absorption** — Goal 3's named technologies (digital twins, AI/ML, digital manufacturing) connect forward to later chapters and packs that treat these as the demand drivers reshaping the DE foundations beneath them.
- **Workforce and governance foundations** — Goals 4 and 5 connect to the policy, standards, and infrastructure themes that recur across the DoD-aligned packs in this collection, framing digital engineering as an organizational transformation, not only a tooling one.

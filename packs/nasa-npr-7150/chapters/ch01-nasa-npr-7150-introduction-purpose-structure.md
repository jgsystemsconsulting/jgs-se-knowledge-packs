# Chapter — Introduction, Purpose, and Document Structure

> Source caveat: This chapter synthesizes the Preface and Chapter 1 of NPR 7150.2D, a NASA Procedural Requirement published through the NASA Online Directives Information System (NODIS) and rendered here from the NODIS HTML. NPR 7150.2D carries the Agency's software-engineering requirements; it complements — and explicitly is influenced by — the broader software-for-systems and program/project area, rather than standing alone.

## Core Idea

NPR 7150.2D treats software engineering as a core Agency capability and an enabling technology for NASA's missions and supporting infrastructure, and on that premise it sets out the engineering requirements that govern software across its whole life: acquisition, development, maintenance, retirement, operations, and management. The directive positions itself inside NASA's existing governance hierarchy — it operates consistent with the governance model of NPD 1000.0 (the Governance and Strategic Management Handbook) and supports the implementation of NPD 7120.4 (the Engineering and Program/Project Management Policy). In other words, it is not a free-standing rulebook; it is the software-engineering layer of a larger directive stack.

The requirements themselves are presented as drawn from two wells: published industry standards and accumulated, proven NASA experience. The directive frames its central purpose as building a common framework of generic requirements so that NASA's engineering and software communities can communicate and work seamlessly across Center boundaries, optimizing resources and talent rather than re-inventing software practice Center by Center. A second, equally explicit purpose is stewardship — protecting the Agency's investment in software-engineering products and discharging NASA's responsibility to U.S. citizens.

## Frameworks Introduced (exact source names, when/how)

- **Software classes (Classes A through F)** — Introduced in the Preface (Applicability) as the NASA-wide mechanism for deciding how the requirements apply to a given system or subsystem. The full definition lives in Appendix D, and the classification structure is shown in the document's Figure 1. Applicability is keyed to class: existing Class A–E efforts sit with the cognizant Mission Directorate under Chief-Engineer-level approval (or a delegate), whereas existing Class F efforts sit with the Center CIO and are signed off by the NASA CIO (or a delegate). A single project may carry multiple software systems and subsystems of differing classes.

- **Requirements Mapping Matrix (RMM)** — Named in the Preface (Measurement/Verification) and located in Appendix C. Compliance with the NPR is verified by submitting the completed Requirements Mapping Matrix (including any approved tailoring) to responsible NASA officials, reinforced by internal and external controls.

- **The "shall / should / will / may-can / is-are" requirement vocabulary** — Defined in the Preface (item g). Mandatory requirements use *shall* and are tagged with a numbered software-engineering (SWE) requirement identifier; *should* marks recommended good practice; *will* denotes an expected outcome; *may* or *can* denote discretionary permission; *is/are* signals descriptive material. This vocabulary is the grammar the rest of the document is written in.

- **The document-hierarchy model** — Laid out in Section 1.2 as three tiers: (1) Agency-level software policies and requirements, anchored by NPD 7120.4 and this NPR; (2) Agency-level multi-Center and product-line requirements that are not software-specific (the Preface and 1.2.2 cite examples such as NPR 8705.2 human-rating, NPR 8715.3 general safety, NPR 8735.2 hardware quality assurance, NPR 7120.5, NPR 7123.1, NPD 2800.1, NPR 2800.2, and NPR 2810.1); and (3) Center-level directives that localize the higher-level rules. The model also fixes precedence: where an NPD and an NPR conflict, the NPD wins; where this NPR conflicts with a Center-level directive, this NPR wins.

- **NASA standard life-cycle models (referenced, not imposed)** — Section 1.1.4 and 1.3.3 are explicit that the directive mandates no particular software life-cycle model. When it does refer to phases and milestone reviews, it borrows the standard NASA life-cycle models described in NPR 7120.5, NPR 7120.7, and NPR 7120.8, with milestone reviews drawn from NPR 7123.1 (the Systems Engineering Processes and Requirements directive).

## Key Concepts

- **Whole-life scope.** Applicability (Preface b) covers the complete software development life cycle — planning, development, testing, maintenance, retirement, operations, management, acquisition, and assurance — and reaches software that NASA creates, acquires, or maintains, including software running on processors embedded in programmable logic devices. The software definition itself sits in Appendix A.

- **Applicability is mediated, not automatic, for non-NASA parties.** The NPR binds NASA Headquarters and Centers (including Component Facilities and Technical and Service Support Centers). For JPL (an FFRDC), other contractors, grant recipients, and parties to cooperative or other agreements, it applies only to the extent specified in the relevant contract, grant, or agreement. The directive's own note stresses that the applicability statement alone does not levy requirements on a contractor — those become mandatory only through contract clauses, specifications, or statements of work consistent with the NASA FAR Supplement.

- **Not retroactive; not a ceiling.** The requirements do not reach back to software work begun before the NPR's effective date (the source names ISS, Hubble, and Chandra as examples of pre-existing systems), and the NPR does not override more stringent requirements imposed by individual NASA organizations, other Federal agencies, or Federal law.

- **Verification through evidence and controls.** "Implementation" means executing all identified processes, activities, and requirements per the software classification and approved tailoring; verification is the completed RMM plus internal controls (per NPD 1200.1) and external controls — surveys, audits, and reviews conducted under NPD 1210.2.

- **Authority chain.** The directive derives its authority from the National Aeronautics and Space Act (51 U.S.C. § 20113(a)) and the NPD 1000-series and NPD 7120.4 directives — establishing that its requirements rest on statute and Agency policy, not on local preference.

- **The five investment areas.** Section 1.1.3 frames the directive's reach across NASA's investment areas: Space Flight, Aeronautics, Research and Technology, Information Technology, and Institutional Infrastructure — the breadth that motivates a single shared requirement set.

- **What each chapter does (Section 1.3).** Chapter 2 covers roles, responsibilities, and institutional requirements (notably outside the Appendix C mapping matrix); Chapter 3 sets software management requirements (interfaces, deliverables, cost estimates, schedule tracking, risk management, reviews, verification and validation), captured in software or system plans; Chapter 4 holds the life-cycle engineering requirements; Chapter 5 holds the supporting life-cycle requirements that run with steady intensity across the whole life — the cross-cutting disciplines of configuration management for software, management of software risk, peer review and inspection practice, the software measurement program, and the handling of non-conformances and defects; Chapter 6 lists recommended software records. Appendices A–E supply definitions, acronyms, the Requirements Mapping Matrix, software classifications, and references.

## Mental Models

- **The directive as a layer, not a monolith.** Picture a stack: statute and the NPD 1000-series at the top, NPD 7120.4 as the overarching engineering/PM policy, NPR 7150.2D as the software-engineering slice beneath it, multi-Center and product-line NPRs sitting alongside, and Center-level directives at the base. Conflicts resolve upward — NPD over NPR, this NPR over Center directives.

- **Class drives applicability.** Rather than one-size-fits-all, the right mental picture is a dial: a system's software class (A–F, from Appendix D) selects which requirements bite and which approval authority owns the tailoring decision (Chief Engineer track for A–E, CIO track for F).

- **Generic framework over prescribed process.** The directive deliberately specifies *what* must be satisfied while staying agnostic about *how* — it imposes no life-cycle model (agile, spiral, iterative, waterfall, or otherwise), instead supporting a standard set of life-cycle phases so products can mature from concept through fielding to retirement.

- **Compliance is a paper-backed claim.** A project does not "comply" by asserting it; compliance is demonstrated by a completed Requirements Mapping Matrix plus the internal/external control regime — evidence, with approved tailoring made visible.

- **A living directive.** Section 1.1.5 frames the NPR as iterative: successful experience, lessons learned, and Engineering Technical Authority (ETA) implementation records get codified into later versions, so the requirement set is expected to evolve with the Agency's challenges.

## Key Takeaways

- NPR 7150.2D is NASA's Agency-wide software-engineering requirements directive, spanning the full software life cycle and grounded in both industry standards and proven NASA experience.
- It is explicitly subordinate to and supportive of NPD 7120.4, and it lives inside a three-tier document hierarchy with defined precedence rules (NPD over NPR; this NPR over Center directives).
- Applicability is driven by software classification (Classes A–F, Appendix D); approval authority for tailoring splits along the Chief Engineer (A–E) and CIO (F) tracks.
- The NPR does not bind contractors by itself — only contract/grant/agreement mechanisms make its requirements mandatory for non-NASA parties — and it is neither retroactive nor a cap on stricter requirements.
- Requirement intent is carried by precise verb usage (*shall* + an SWE number for mandatory items; *should*, *will*, *may/can*, *is/are* for the rest).
- Compliance is verified through the completed Requirements Mapping Matrix (Appendix C) plus internal (NPD 1200.1) and external (NPD 1210.2) controls.
- No specific life-cycle model is imposed; the directive supports standard NASA life-cycle phases and borrows phase/milestone definitions from NPR 7120.5/7/8 and NPR 7123.1.
- The six chapters move from institutional roles (Ch. 2) through management (Ch. 3), life-cycle engineering (Ch. 4), supporting processes (Ch. 5), to recommended records (Ch. 6), with reference material in Appendices A–E.

## Connects To

- **NPD 7120.4 (NASA Engineering and Program/Project Management Policy)** — the overarching directive this NPR implements and supports.
- **NPR 7123.1 (NASA Systems Engineering Processes and Requirements)** — supplies the milestone reviews the software life cycle hangs on, anchoring software work in the wider systems-engineering process.
- **NPR 7120.5 / 7120.7 / 7120.8** — the program/project management directives whose standard life-cycle models this NPR reuses for phases and milestones.
- **NASA-STD-8739.8 (Software Assurance and Software Safety Standard)** and **NASA-HDBK-2203 (NASA Software Engineering Handbook)** — the assurance/safety standard and the companion handbook listed among applicable documents, extending the requirements with guidance and assurance practice.
- **Appendix D software classifications** and **Appendix C Requirements Mapping Matrix** — the two internal mechanisms (class-based applicability and matrix-based verification) that every downstream chapter depends on.
- **NPR 8705.2 (Human-Rating), NPR 8715.3 (Safety), NPR 8735.2 (Hardware QA), NPR 2810.1 (IT Security)** — the multi-Center and product-line requirements that layer atop this NPR for safety-, security-, and mission-critical software.

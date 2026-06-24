# Chapter — Definitions: The Controlled Vocabulary of NASA Software Engineering

> Source caveat: This chapter synthesizes Appendix A (Definitions) of NPR 7150.2D, a NASA Procedural Requirement issued through NODIS and rendered here from the NODIS HTML. These are software-engineering requirements that complement the broader software-for-systems area; the definitions below carry their meaning only "for this document" unless the source cites an external standard.

## Core Idea

A procedural requirement is only enforceable if everyone reads its key terms the same way. Appendix A exists to remove that ambiguity. It is the controlled vocabulary that fixes the meaning of every load-bearing word used across NPR 7150.2D — so that when a requirement says "verify," "assure," "ensure," or "off-the-shelf," there is exactly one sanctioned interpretation rather than the looser everyday senses those words carry in conversation.

Three things make this glossary distinctive. First, many entries are scoped explicitly to this directive ("Only for this document," "In this directive"), meaning the NPR deliberately narrows or specializes a term rather than inheriting its general usage. Second, a large share of definitions are imported wholesale from external standards — ISO/IEC/IEEE 24765, IEEE 1012, IEEE 1028, several NASA Standards (the 8739 and 8715 families), and sibling NPRs (7120.x, 7123.1, 8000.4) — which anchors NASA's software vocabulary in the wider systems-and-software engineering canon. Third, the definitions encode policy thresholds, not just meanings: the boundary between "modified" and "new" software, the dollar and dependency cutoffs that make a facility "major," and the disciplines that constitute "software assurance" are all decided here, in the glossary, where they govern how requirements apply.

In short, Appendix A is where the directive draws its lines. Reading it is reading the rulebook for how every other requirement is to be interpreted.

## Frameworks Introduced (exact source names, when/how)

The appendix does not define new frameworks; instead it ties NASA's vocabulary to an explicit web of named external authorities, citing each as the source for specific terms. The recurring sources, named exactly as they appear:

- **ISO/IEC/IEEE 24765** ("Systems and software engineering — Vocabulary") — cited as the source for *Bidirectional Traceability*, *Computer System*, *Embedded Computer System*, *Embedded Software*, *Independent Verification and Validation*, *Software Engineering*, *Static Analysis*, *Subsystem*, and one branch of *Unit Test*. This is the most heavily leaned-on external authority in the glossary.
- **IEEE 1012** ("IEEE Standard for Software Verification and Validation") — source for *Software Validation*, *Software Verification*, and parts of the general *Validation* entry.
- **IEEE 1028** — source for *Software Peer Review and Inspection*.
- **IEEE 828-2012** and several **ISO/IEC** documents (19770 series, 26514:2008, 26513:2017) — invoked collectively in the multi-part definition of *Software*.
- **ISO/IEC/IEEE 15026-1:2019, ISO 5806:1984, ISO/IEC/IEEE 29119-4:2015** — the three sources stacked into the multi-sense definition of *Condition*.
- **NASA Standards** — *NASA-STD-8739.9* (source for *Defect*, *Failure*), *NASA-STD-8719.24 Annex* (*Fault*), *NASA-STD-8739.8* (where IV&V requirements live), *NASA-STD-7009* (*Model*, *Simulation*).
- **Sibling NPRs** — *NPR 7123.1* (*Insight*, *System*), *NPR 8715.3* (*Mission Critical*, *Risk Management*, *Safety Critical*), *NPR 7120.7* (*Information Technology*), *NPR 7120.5* (referenced for *Project Manager* roles), *NPR 8000.4* (*Uncertainty*).
- **CMMI** for Systems Engineering / Software Engineering / IPPD — source for *Process Asset Library*.
- **PMBOK Guide (Fifth Edition)** — cited for one sense of *Validation*.

The pattern, when read across all of these: NASA does not reinvent definitions it can inherit. It reserves bespoke definitions for terms where it needs its own policy meaning (the off-the-shelf taxonomy, the auxiliary verbs, the facility and mission thresholds) and otherwise points outward to the established standards.

## Key Concepts

**The verb distinctions.** The glossary separates three auxiliary verbs that ordinary English treats as near-synonyms. *Assure* is making certain that others have actually performed the specified software engineering, management, and assurance activities. *Ensure* is to secure or guarantee — to make something sure or certain. *Accredit* is the official acceptance of a tool, model, or simulation (and its data) for a specific stated purpose. Treating these as distinct is deliberate: each maps to a different actor and obligation.

**The off-the-shelf taxonomy.** A substantial block of the appendix carves up software the project did not build for itself. *Off-the-Shelf Software* is the umbrella term, covering COTS, GOTS, MOTS, OSS, freeware, shareware, trial/demo software, and legacy/heritage/reuse software. Underneath it:
- *COTS* — purchasable and usable without development work, ready off the commercial market.
- *GOTS* — government-created software, typically from a prior project, usually delivered with source and documentation.
- *MOTS* — COTS or heritage software that has been changed; the glossary attaches percentage thresholds to this label (see Mental Models).
- *Open-Source Software* — source made broadly available at no cost under an OSS license granting use, modification, and redistribution rights, often developed in the open.
- *Freeware* — proprietary but free to use, typically not modifiable, redistributable, or reverse-engineerable without permission.
- *Shareware* — free to obtain and evaluate, with a fee expected for continued use.
- *Glueware* — software written to connect off-the-shelf or reused components to the rest of the system, including interface adapters, isolating "firewalls," and input/output checkers.
- *Legacy and Heritage Software* — products written for one project that, without prior planning, turn out useful elsewhere.

**Verification versus validation.** The glossary fixes the classic V&V pair with memorable framing. *Software Verification* confirms that products correctly reflect their specified requirements — building the thing right. *Software Validation* confirms that the delivered product fulfills its intended use — building the right thing. The longer general *Validation* entry layers on multiple standards' phrasings but holds the same distinction.

**The assurance discipline set.** *Software Assurance* is defined as the planned, systematic activities that make life-cycle processes and products conform to requirements, standards, and procedures — and for NASA it bundles a named set of sub-disciplines: Software Quality (Engineering, Assurance, and Control), Software Safety, Software Reliability, Mission Software Cybersecurity Assurance, Software V&V, and IV&V. *IV&V* itself is V&V performed by an organization technically, managerially, and financially independent of the developer.

**Coverage and complexity metrics.** Several entries fix the meaning of test-related measures: *Code Coverage* (percentage of software executed by the test suite), *MC/DC* (modified condition/decision coverage, requiring each condition in a decision to be shown to independently affect the outcome by varying one condition at a time), and *Cyclomatic Complexity* (a count of linearly independent paths through a function's code).

**Defect, fault, failure.** The glossary distinguishes the failure chain: a *Defect* is anything incomplete or incorrect relative to requirements or expectations; a *Fault* is the manifestation of an error that may cause a failure; a *Failure* is the actual incorrect or undesired behavior of a specified severity when a fault is encountered.

**Criticality terms.** *Mission Critical Software* can cause, contribute to, or mitigate loss of capabilities essential to primary mission objectives; *Safety Critical* describes anything that could lead to severe injury, major damage, or mission failure if done wrong or left uncorrected.

**The breadth of "Software."** The directive's own scope-setting definition matters: *Software* spans NASA-developed, NASA-contracted, and NASA-maintained code, plus COTS/GOTS/MOTS/OSS, reused components, auto-generated code, embedded software including code running on processors inside programmable logic devices, legacy and heritage code, applications, freeware, shareware, trial/demo software, and open-source components. The point of listing all of these is to leave little room to argue a given artifact is out of scope.

## Mental Models

**The glossary as a set of policy switches, not a dictionary.** Some definitions silently encode decisions that change what the rest of the NPR requires:
- *MOTS thresholds* — the appendix offers a graduated rule of thumb: changing less than roughly five percent of code may not even count as "modified," up to about 30 percent of changed code the product can still be treated as "modified," but beyond 30 percent changed (or if new code is added) it should be handled as a new development. Where a project lands on this scale determines which requirements bite.
- *Major Engineering/Research Facility* — qualifies only when it represents a significant investment (Current Replacement Value at or above 50 million dollars) and carries a Mission Dependency Index at or above 70, while hosting software supporting 7120.x-managed programs. Two numeric gates decide the label.
These entries show that in this directive, defining a term is often the same act as setting a threshold.

**Scoped-to-document narrowing.** When an entry says "Only for this document" (as with *Model* and *Simulation*, both restricted to software-implemented forms) or "In this directive" (as with *Software*), read it as a deliberate fence. NASA-STD-7009 defines model and simulation broadly across systems work; the NPR narrows them to software so the requirement set applies cleanly. Always check whether a term has been scope-limited before importing its general meaning.

**Inherit by default, define by exception.** The dominant pattern across the appendix is citation, not invention. The mental shortcut: if a term is generic systems-and-software vocabulary, expect a cited external source (24765, IEEE, ISO); if a term carries NASA-specific policy weight (the off-the-shelf family, the auxiliary verbs, the criticality and facility thresholds, the assurance discipline list), expect a bespoke in-house definition. Knowing which kind you are reading tells you whether to consult the parent standard for nuance.

**Off-the-shelf as a tree, not a flat list.** Picture *Off-the-Shelf Software* as the root, with COTS/GOTS/OSS/freeware/shareware/legacy as leaves and MOTS as the "modified" branch that can grow back into "new development" once enough changes accumulate. *Glueware* is the connective tissue you add around any leaf to make it fit. This tree structure is what lets the directive apply different obligations to different origins of code.

## Key Takeaways

- Appendix A is the directive's controlled vocabulary; it exists to give every load-bearing term one sanctioned meaning so requirements elsewhere cannot be read loosely.
- NASA inherits most definitions from named external standards — ISO/IEC/IEEE 24765 most of all, plus IEEE 1012/1028/828, the ISO 19770/26513/26514 family, several NASA Standards, and sibling NPRs — and reserves bespoke definitions for policy-bearing terms.
- The off-the-shelf taxonomy (the umbrella term over COTS, GOTS, MOTS, OSS, freeware, shareware, legacy/heritage, with glueware as connective code) is the most developed concept block in the appendix.
- Several definitions are really policy switches: MOTS percentage thresholds (≈5% / 30%) and the Major Facility gates ($50M replacement value, Mission Dependency Index ≥ 70) decide which requirements apply.
- The verbs *assure*, *ensure*, and *accredit* are deliberately distinguished, as are the *defect / fault / failure* chain and *verification* ("built it right") versus *validation* ("built the right thing").
- *Software Assurance* is defined as a bundle of named NASA sub-disciplines (Software Quality, Safety, Reliability, Mission Software Cybersecurity Assurance, V&V, and IV&V), making the definition itself the scope statement for the assurance program.
- Watch for "Only for this document" and "In this directive" qualifiers — they signal a term whose general meaning has been intentionally narrowed for software-engineering use.

## Connects To

- **NPR 7150.2D requirement chapters** — every requirement that uses "shall verify," "shall assure," "off-the-shelf," "safety critical," or "software assurance" resolves its meaning here; the glossary is the interpretation layer beneath the requirement set.
- **ISO/IEC/IEEE 24765 (Vocabulary)** — the primary external anchor; many NASA terms are this standard's definitions, so the appendix functions partly as a NASA-curated subset of the broader SE vocabulary.
- **IEEE 1012 (Software V&V)** and **IEEE 1028 (reviews/inspections)** — the verification, validation, and peer-review definitions are imported from these, tying NASA practice to industry V&V standards.
- **NASA Standards (8739.9, 8739.8, 8719.24, 7009, 8715.3)** — the defect/failure, IV&V, model/simulation, and criticality terms point to these, linking the NPR to the wider NASA software and safety standard set.
- **Sibling NPRs (7120.5/7120.7/7120.8, 7123.1, 8000.4)** — program, project, insight, system, IT, and uncertainty definitions come from the systems-engineering and program-management NPRs, situating software engineering inside NASA's overall governance hierarchy.
- **The software-for-systems area generally** — by scoping *model*, *simulation*, and *software* tightly, the appendix marks the boundary between software-engineering requirements and the broader systems context they complement.

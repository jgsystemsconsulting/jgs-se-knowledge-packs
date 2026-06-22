# Chapter — Concluding Remarks and Research Agenda

> Source: Huang et al., *Towards Digital Engineering: The Advent of Digital Systems Engineering* (arXiv preprint version only — not the paywalled journal edition). This chapter synthesizes the paper's closing section (Section 6, "Concluding Remarks").
> Funding context: the work was partially supported by the U.S. National Science Foundation (grant CNS-1828593), and revises an earlier 2019 white paper by the same authors.

## Core Idea

The paper closes by positioning **digital systems engineering as an emerging academic field** — a deliberate scholarly response to the U.S. Department of Defense's call (in its 2018 digital engineering strategy) for new methods, processes, and tools. The authors frame their contribution not as a finished theory but as a *vision* that names what must be built: theory, methods, models, and tools that let digital engineering practice work in a connected, digitalized environment. The central recurring claim is that the pivotal task ahead is **digitalizing engineering artifacts** — models, datasets, products, functions, services, and the SE processes themselves — so that they become machine-processable. Once artifacts are machine-understandable, organizations can rapidly absorb and exploit new digital technologies. The chapter is explicitly forward-looking: it summarizes what the paper accomplished, then enumerates the open problems the authors intend to pursue.

## Frameworks Introduced (exact source names, when/how)

The concluding section does not introduce new frameworks; instead it recapitulates the structuring devices the paper built earlier, naming them as the scaffolding for the field:

- **The four-level "big picture" of digital systems engineering — vision, strategy, action, and foundation** (referenced as figure 5 in the source). The authors cite this as their organizing model for laying out where research issues sit. Each level frames a different class of problem, from aspirational direction down to enabling groundwork.
- **The transformation analysis from traditional engineering to digital engineering** (referenced as figure 3). The conclusion recalls this as the paper's diagnostic of *what is changing* and why a new field is warranted.
- **A defined core-concept set**: the authors state they clarified and defined a small, deliberate vocabulary — **digitalization, digitalized artifacts, digital augmentation, and digitalized models**. These four are presented as the minimal conceptual base the field needs to reason precisely.

These are invoked by name as the paper's deliverables, used here to summarize scope rather than to introduce anything new.

## Key Concepts

- **Digitalization of engineering artifacts** — the foundational move. Artifacts spanning models, datasets, products, functions, services, and SE processes are converted into forms that are universally machine-processable. This is named as the critical enabler for rapidly infusing and leveraging innovative digital technologies.
- **Unique identification** — treated as a sub-element of digitalization. Assigning unique identity to artifacts is what makes information **traceability and accountability** possible across the system lifecycle.
- **Provenance** — within the digital engineering information flow, provenance lets engineers trace the dependency relationships among artifacts. The authors tie it directly to improving **model reproducibility and replicability** — a notably scientific framing of engineering rigor.
- **Distributed digital trust** — an open research direction for managing digital identity and attribute information, and for sharing digital engineering artifacts in real-world, multi-party engineering collaboration.
- **Data-intensive systems engineering** — a proposed approach centered on trustworthy AI systems, machine-learning models, and algorithms for knowledge discovery from large data. The stated quality goals are reliable performance, explainability, safety, security, resilience, and scientific-computing integrity.
- **Workforce dimension** — the field is meant to supply not only knowledge, methods, and technologies but also training and education for the engineering workforce, supporting DoD's digital engineering strategy and digital engineering broadly.

## Mental Models

- **Field, not just a method.** The authors deliberately cast digital systems engineering as an *academic discipline* with its own theory-building agenda, rather than a toolkit. This reframing means the conclusion reads as a research charter: name the concepts, lay out the levels, then list what is still unknown.
- **Vision → strategy → action → foundation as a ladder.** The four levels function as altitude bands. Reading top-down explains intent; reading bottom-up explains feasibility — the foundation level is where the hard enabling research lives.
- **Machine-understandability as the unlock.** The mental shortcut throughout: if an artifact cannot be processed by a machine, it cannot participate in rapid technology infusion. Digitalization is therefore the gate every downstream capability passes through.
- **Provenance as scientific reproducibility for engineering.** The authors borrow the reproducibility/replicability standard from science and apply it to engineering models, framing dependency-tracing as the mechanism that makes engineering work auditable and re-runnable.

## Key Takeaways

- The paper's stated accomplishments are threefold: (1) it analyzed the shift from traditional to digital engineering; (2) it defined a compact core vocabulary (digitalization, digitalized artifacts, digital augmentation, digitalized models); and (3) it presented the four-level big picture and discussed the research issues in each identified area.
- Digitalizing engineering artifacts is named the *critical task* on the road to digital engineering — everything else depends on it.
- Unique identification and provenance are the two named enablers that turn raw digitalization into something trustworthy: identification gives traceability and accountability; provenance gives dependency-tracing, reproducibility, and replicability.
- The authors are explicit that this is a vision with much work ahead. Their own near-term agenda prioritizes: an **ontological approach** to digitalizing artifacts; a **model of models** for digitalizing models; and **provenance representation and reasoning** models.
- Further out, they intend to research **distributed digital trust** mechanisms and a **data-intensive systems engineering** approach grounded in trustworthy AI and ML.
- The ultimate purpose is practical: to equip the implementation of DoD's digital engineering strategy — and digital engineering generally — with the knowledge, methods, technologies, training, and education it needs.

## Connects To

- **The DoD Digital Engineering Strategy (2018)** — the conclusion is anchored to this policy driver; the field exists to operationalize that strategy's demand for new methods, processes, and tools.
- **Earlier chapters of this pack** — the closing section references figures 3 and 5 and the core-concept definitions established earlier, so it functions as the synthesis of the pack's preceding material rather than standalone content.
- **MBSE and model-centric engineering** — the emphasis on digitalized models, a "model of models," and model reproducibility connects to the broader model-based systems engineering canon (see the `sebok` knowledge base for the established lifecycle and MBSE background this paper extends toward AI/data integration).
- **Trustworthy AI and data-intensive engineering** — the data-intensive systems engineering direction links forward to ML reliability, explainability, and assurance work, positioning AI integration as a first-class SE research concern.
- **The prior 2019 white paper by Huang et al.** — this paper is named as a revision and further development of that earlier work, marking it as one step in an ongoing research program rather than a terminal statement.

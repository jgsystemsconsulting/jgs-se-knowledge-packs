# Chapter 6: The Four-Level Framework — Vision, Strategy, Action, and Foundation

## Core Idea
Having argued that digital systems engineering (DSE) is the discipline that *digitalizes* systems engineering, the paper proposes a way to organize the field's knowledge and research areas so the broad digital-engineering vision can actually be realized. That organizing scheme is a **four-level framework** — **Vision, Strategy, Action, and Foundation** — illustrated in the paper's Figure 5. The levels read top-down as a chain of realization: a clear *vision* of digital engineering motivates a set of *strategic* moves, those strategies are carried out through concrete *actions*, and the actions stand on a *foundation* of enabling digital technologies and foundational research. The whole framework is the authors' attempt to draft a general DSE agenda situated in the wider context of digital transformation, Industry 4.0, and Data Science — not merely a restatement of the US DoD Digital Engineering Strategy, which they treat as insightful but specific to the DoD enterprise.

## Frameworks Introduced
- **The four-level DSE framework (Figure 5: "Knowledge and Research Areas of Digital Systems Engineering")** — Level 1 *Vision*, Level 2 *Strategy*, Level 3 *Action*, Level 4 *Foundation*.
  - When/how to use: as the master map for the entire DSE research field — to locate any given problem (e.g., "how do I share a digitalized model across organizations?") at the right altitude and to see what it depends on below it. Introduced and unpacked across Section 5.2 and its four subsections (5.2.1–5.2.4).
- **The relations diagram (Figure 4)** — positions DSE alongside Model-Based Systems Engineering (MBSE) and classical SE, all serving "Digital Engineering" above and resting on "Systems Thinking & (Classical) Systems Approach / Systems Engineering" below.
  - When/how to use: to explain that DSE and MBSE are *complementary*, not competing — MBSE drives the document-centric-to-model-centric transformation; DSE adds digitalization, unique identification, big data, and digital trust. Both are subfields of SE guided by systems thinking.
- **MBSE (INCOSE definition, cited via INCOSE 2007)** — the formalized application of modeling to support requirements, design, analysis, verification, and validation from conceptual design onward through the life cycle; its central goal is to move SE from document-centric to model-centric approaches.
  - When/how to use: as the adjacent discipline DSE "works together with" to support digital engineering.
- **The artifact-operation × life-cycle matrix (Figure 6: model operations vs. SE life-cycle stages)** — crosses model operations (creation/learning, integration, curation, sharing & use, trustworthiness) against the five life-cycle stages (Concept, Development, Production, Utilization/Support, Retirement).
  - When/how to use: at the Action level, to systematically enumerate research issues — one appears in *every* cell of the grid (each operation type × each life-cycle activity).

## Key Concepts
- **Digitalization is the core.** The overarching goal of DSE is to develop the principles, theories, methods, models, and technologies for digitalizing engineering and for doing SE in digitalized, connected environments. Everything in the four levels ultimately serves this.
- **Immediate targets.** DSE's near-term focus is digitalizing engineering artifacts, sharing information and models, and the consequent problems of digital trust, big data, automatic machine processing, and machine learning that arise once the environment is digitalized and connected.
- **Digital augmentation.** A central task is to attach, to each engineering artifact, a digital augmentation with well-defined semantics — a machine-processable wrapper that lets digital technologies manipulate, operate on, or interact with the artifact. Artifacts span models, data, materials, products, services, processes, parts, software, services, roles, and even enterprise organizations.
- **Unique identification.** Treated as part of digitalization, unique identification is what enables *accountability* and *traceability* — tracing information flow, material flow, fault chains, and supply chains across the life cycle.
- **The four levels (top-down):**
  - *Vision (Level 1)* — establish a clear, general vision of engineering in the digital age, via needs analysis (features of a fast-changing environment, deficiencies of current practice, conceptualization of the future, gap analysis, enabling technologies, feasibility) and the goals/targeted advantages to pursue.
  - *Strategy (Level 2)* — four strategic moves (see Mental Models).
  - *Action (Level 3)* — four groups of work: digitalization of artifacts; operations on digitalized artifacts; SE life-cycle activities performed *with* digitalized artifacts; and innovative applications enabled by digital technologies.
  - *Foundation (Level 4)* — the enabling technologies and foundational research that make the upper levels possible (see Mental Models).
- **The six operations on digitalized artifacts.** At the Action level, once artifacts can be digitalized, practice must handle: **Creation, Curation, Qualification, Governance, Sharing, Utilization**. Each artifact type needs its own study; digitalized *models* warrant immediate attention given their central role.
- **Levels of automation in systems design.** The paper sketches a ladder for digitalized models: a basic level (a human-readable diagram wrapped in metadata), a middle level (an executable formal model run in a container, with traceable origin and dependencies), an advanced level (machine V&V via model checkers/theorem provers, automatic fault finding, human-integrated multi-model construction), and a highest level (a machine autonomously building and improving a system model on top of available digitalized artifacts).
- **The "five Vs" of big data.** In the digitalized, connected environment, big data is characterized by volume, velocity, variety, veracity, and *views* (Huang, 2018) — framing the Foundation-level challenge of trustworthy AI/ML for knowledge discovery.

## Mental Models
- **Read the framework as a dependency stack, not a list.** Vision answers *why*, Strategy answers *what moves*, Action answers *what work*, Foundation answers *what makes it possible*. A research problem placed too high without its foundation has nothing to stand on; a foundation built without a vision solves nothing in particular.
- **The four strategic moves (Level 2) as the bridge from why to how:**
  1. **Transform engineering practice** — the central task here is digitalizing engineering artifacts.
  2. **Transform education and workforce development** — humans advance engineering, so reskill the workforce and build AI-powered learning/training systems for the digital-engineering environment.
  3. **Transform engineering infrastructure** — stand up cloud-based platforms and digital trust/security mechanisms to meet the demands of big data, security, and a distributed environment.
  4. **Embrace innovative digital technologies in operations** — once digital engineering is realized, rapidly adopt, interact with, and integrate emerging technologies to achieve fast design, delivery, and sustainment of agile, intelligent, complex systems.
- **The four Foundation clusters (Level 4) as the bedrock:**
  1. **Foundation for digitalization** — drawn mainly from AI, specifically knowledge representation & reasoning (KR&R) and semantics from ontology engineering and the Semantic Web: *model of models*, *provenance modeling*, *ontologies* for well-defined semantics, and *standardization* (centralized; decentralized with mappings; distributed fine-grained evolutionary convergence with ontologies).
  2. **Digital mechanisms of trust** — for the distributed environment: centralized (e.g., the DoD's *Authoritative Source of Trust*, AST), decentralized (multiple ASTs structured as hierarchies or meshes, as with PKIs), distributed (digital signatures, distributed key/attribute certification, evidence-based trust, blockchain), and hybrid mechanisms.
  3. **Cybersecurity technologies** — access control of digitalized artifacts, engineering-computing integrity in a distributed environment, identity/attribute management, blockchain-based trust and security, intrusion detection. (The paper defers a full treatment to a separate paper.)
  4. **Big Data & Machine Learning** — cloud platforms for big data in DE, big-data manipulation, big-data analytics and ML for knowledge discovery, and *Data-intensive Systems Engineering* (SE combined with data-derived insight).
- **DSE and MBSE are partners, not rivals.** Use Figure 4 as the mental anchor: MBSE pushes SE from document-centric to model-centric; DSE adds the digitalization, identification, big-data, and trust layer. They jointly support digital engineering, and both are governed by classical systems thinking. DSE also extends support to System-of-Systems Engineering and Mission Engineering by enriching information for complex-system governance, coordination, and planning.
- **DSE seen two ways.** From the digital-transformation lens, DSE is the digitalization of systems engineering; from the data-science lens, it is data science extended to systems engineering.

## Key Takeaways
1. DSE's knowledge and research areas are organized into **four levels — Vision, Strategy, Action, Foundation** (Figure 5), read top-down as a realization chain.
2. The **core of DSE is digitalization**; its immediate targets are digitalizing artifacts, sharing models/information, and the resulting digital-trust, big-data, and machine-processing problems.
3. **Strategy** comprises four moves: transform practice, transform workforce/education, transform infrastructure, and embrace innovative technologies in operations.
4. **Action** comprises four work groups — digitalize artifacts; operate on them (Creation, Curation, Qualification, Governance, Sharing, Utilization); run life-cycle activities with them (research issues appear in *every* operation × life-cycle cell, per Figure 6); and build innovative applications (AI-aided design, autonomous factories/transport).
5. **Foundation** rests on four clusters: foundations for digitalization (KR&R, ontologies, provenance, standardization), digital mechanisms of trust (centralized/decentralized/distributed/hybrid, with AST as the centralized exemplar), cybersecurity, and big data & ML.
6. **DSE complements MBSE** (Figure 4); both serve digital engineering and rest on classical systems thinking — and DSE also supports SoS Engineering and Mission Engineering.
7. The framework is explicitly **non-exhaustive** — the authors note that human-machine interaction, team collaboration, parts recycle/reuse evaluation, and environmental-impact analysis in digitalized connected environments were left out for space.

## Connects To
- **The artifact / digital-augmentation chapters of this pack** (Section 5.1 material): the four-level framework operationalizes digital augmentation and unique identification as the Action-level "digitalization of artifacts" group.
- **MBSE** (INCOSE 2007; Estefan 2007; Madni & Sievers 2018) and the **`sebok` skill**: the model-centric transformation that DSE partners with, and the classical-SE base both rest on.
- **System-of-Systems Engineering** (cited to C. Keating et al., 2003) and **Mission Engineering** (cited to Sousa-Poza, 2015, and Gold, 2016): both are downstream beneficiaries of the enriched information DSE supplies for complex-system governance (per C. B. Keating & Katina, 2019).
- **US DoD Digital Engineering Strategy and the Authoritative Source of Trust (AST)**: the centralized digital-trust mechanism named at the Foundation level; treated as an insightful but DoD-specific vision the general framework generalizes.
- **Data Science / Big Data and ML**: the Foundation-level cluster underpinning the field; DSE is framed as data science extended to SE.

---
*Source: J. Huang et al., "Towards Digital Engineering: The Advent of Digital Systems Engineering," Section 5.2 and Figures 4–6. Synthesized from the open-access **arXiv:2002.11672** preprint only (not the paywalled journal version). Licensed CC BY 4.0; attribution to the original authors required.*

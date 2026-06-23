# Chapter — Goal 1: Formalize the Development, Integration & Use of Models

## Core Idea
Goal 1 of the 2018 Strategy makes modeling a deliberate, planned engineering practice rather than an ad-hoc activity. The aim is to apply formal modeling across every lifecycle phase — from concept through disposal — so that models inform both program-level and enterprise-level decisions. A model is treated as a precise, flexible representation of a system, phenomenon, entity, or process. Early in the lifecycle, models let teams explore candidate solutions virtually before anything physical is built; later, mature models become high-fidelity stand-ins for their physical counterparts, supporting virtual testing and sustainment. The key shift is that models are not discarded and rebuilt at each phase boundary — the collection of models evolves continuously and persists for the full life of the system. The goal is decomposed into three focus areas: plan for models (1.1), develop/integrate/curate models (1.2), and use models in decisions (1.3).

## Frameworks Introduced
- **Goal 1 — Formalize the Development, Integration, and Use of Models** (the Strategy's first of five goals). It frames modeling as the foundation for informing both enterprise and program decision making, applied across all lifecycle phases.
  - *When/how:* invoked whenever a DoD program decides how modeling will support engineering work; it sets the expectation that modeling is formalized, persistent, and decision-driving rather than incidental.
- **Authoritative Source of Truth (ASoT)** — introduced here (via Figure 4) as the integrated foundation that different types of models connect through. It lets multiple disciplines and domains operate concurrently on different facets of the same system inside a shared virtual environment.
  - *When/how:* established as the collection of integrated models is built up; it should carry traceability of models from concept through disposal and serve as the single reference that decision makers draw on.
- **Model formalisms** (1.2) — the foundational quality standards and rules models must conform to: syntax, semantics, lexicons, and applicable standards. They keep models consistent both internally and against external program dependencies.
  - *When/how:* set in place during planning (1.1) and applied during model development (1.2), so every model is built to a known, shared rule set.
- **Model provenance and pedigree** (1.2) — the recorded origin and lineage of a model, captured and maintained to establish trust, credibility, accuracy, and a defensible basis for deciding whether a model can be reused.
  - *When/how:* captured as models are developed under policy, guidance, standards, and formalisms; it underpins model-based reviews, audits, and verification/validation.

## Key Concepts
- **Formalized modeling across the full lifecycle** — modeling is applied deliberately at every phase from concept to disposal, not just in design.
- **Models that live and evolve** — rather than being thrown away between phases, models mature and carry forward, so the model set spans the system's entire lifespan (the source cites a 50-year horizon for the carrier example).
- **Three focus areas of Goal 1:**
  - **1.1 Formalize the planning for models** — organizations write formal plans covering model creation, curation, integration, and the related program/enterprise engineering activities; the plans describe how models will be realized coherently as work proceeds and as analyses and decisions are supported.
  - **1.2 Formally develop, integrate, and curate models** — organizations use model formalisms to develop and curate models, integrate models from all stakeholders into one digital representation of the system of interest, and ensure models are accurate, complete, trusted, and reusable through provenance/pedigree and V&V-based reviews and audits.
  - **1.3 Use models to support engineering activities and decision making** — models become the basis for defining, evaluating, comparing, and optimizing alternatives and for making decisions, spanning all disciplines to enable concurrent engineering.
- **Digital representation of the system of interest** — planning establishes an approach that uses models to orchestrate activities, manage work efficiently, and integrate work products across enterprises and multidisciplinary teams into one digital representation.
- **Model-based reviews and audits** — reviews, audits, and trust judgments grounded in verification and validation attributes are treated as essential to effective collaboration and to the system's evolution.
- **Model exchange and automated transformation** — information should move between disciplines and organizations through model exchanges and automated transformations wherever possible, with instructions prepared to ensure accurate use.
- **Communicating with models** — a model becomes the medium for answering questions, reasoning about the candidate solution, backing decisions, and communicating clearly at every level of fidelity and throughout the lifecycle's activities.

## Mental Models
- **Plan it, build it, use it.** Goal 1 reads as a pipeline: 1.1 plans how models will exist, 1.2 develops/integrates/curates them to quality, and 1.3 puts them to work in decisions. Skipping 1.1 leaves later models inconsistent because no shared formalisms were set.
- **Formalisms are the grammar of the model set.** Syntax, semantics, lexicons, and standards are to models what spelling and grammar are to a shared document — they are what makes independently authored models combine into one coherent digital representation.
- **Trust is engineered, not assumed.** A model is only as reusable as its provenance and pedigree are documented; trust comes from recorded lineage plus verification and validation, not from the model merely existing.
- **One source of truth, many concurrent users.** The ASoT lets multiple disciplines work different aspects of the same system at the same time in the virtual environment, instead of holding disconnected copies — and it preserves traceability from concept through disposal.
- **Exchange models, not documents.** Where possible, hand off a model (with automated transformation) rather than a static document, so information moves between teams without manual re-interpretation.

## Anti-patterns
The source frames Goal 1 in positive, prescriptive terms and does not enumerate named anti-patterns, so none are asserted here. (The implied failure modes — discarding and rebuilding models each phase, and modeling without formalisms or recorded provenance — are described in the Key Concepts above as the practices Goal 1 is intended to replace.)

## Key Takeaways
1. **Goal 1 formalizes modeling across the whole lifecycle** (concept through disposal) so models inform both program and enterprise decisions.
2. **Models persist and evolve** — the model set is carried forward, not rebuilt at each phase, and lives for the full system lifespan.
3. **Plan first (1.1):** write formal plans for model creation, curation, and integration, establishing the formalisms (syntax, semantics, lexicons, standards) up front.
4. **Develop to quality (1.2):** integrate every stakeholder's models into one digital representation, and make them accurate, complete, trusted, and reusable via provenance/pedigree and V&V-based reviews and audits.
5. **Use models to decide (1.3):** make models the basis for defining, comparing, and optimizing alternatives, exchanging models and automating transformations between disciplines wherever possible.
6. **The Authoritative Source of Truth ties it together** — an integrated, traceable model collection that concurrent disciplines operate on and that decision makers rely on.
7. **Worked example:** the source cites USS Ford (CVN-78) as the first ship fully designed using a full-scale 3-D product model, where integrated 3-D models surfaced hidden value and yielded a projected multi-billion-dollar reduction in ownership costs over a 50-year lifespan — concrete evidence of formalized modeling paying off.

## Connects To
- **ch01 (Strategy overview / the five goals)**: Goal 1 is the first of the Strategy's goals; the remaining goals build the infrastructure, environment, and workforce that make formalized modeling feasible.
- **Goals 2–5 of this pack**: the ASoT and formalisms introduced here are operationalized by the later goals (technological innovation, infrastructure/environments, and the cultural/workforce transformation needed to sustain model-based practice).
- **`dau-se-guidebook` pack (ch02, Digital Engineering)**: the Guidebook's DE goal set restates this same formalize-models-across-the-lifecycle objective and the authoritative-source-of-truth concept.
- **`sebok` skill (MBSE, V&V, traceability)**: model formalisms, provenance/pedigree, model-based reviews, and ASoT traceability map onto SEBoK's MBSE and verification/validation canon.
- **MBSE tooling (SysML v2 / Cameo)**: the syntax/semantics/lexicon formalisms and model-exchange/transformation ideas are realized concretely in standards-based modeling environments.

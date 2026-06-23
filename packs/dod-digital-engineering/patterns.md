# DoD Digital Engineering Strategy — Patterns & Techniques

Reusable patterns distilled from the *DoD Digital Engineering Strategy* (2018). Each has
**When / How / Trade-offs**. The Strategy is intentionally non-prescriptive, so these are
practitioner patterns synthesized from its goals and focus areas — not a mandated method.

## Pattern 1: Plan models before you build them (Goal 1.1 first)

**When to use**: at the outset of any program deciding how modeling will support engineering work.

**How**: write a formal plan covering model creation, curation, integration, and the related engineering activities *before* developing models — establishing the formalisms (syntax, semantics, lexicons, applicable standards) up front so independently authored models combine into one coherent digital representation. Then develop and curate to quality (1.2) and use the models to decide (1.3).

**Trade-offs**: front-loading planning feels slow when teams want to start modeling immediately — but skipping 1.1 leaves later models inconsistent because no shared formalisms were set, and the model set never integrates cleanly.

---

## Pattern 2: Engineer trust into models with provenance and pedigree

**When to use**: whenever a model may be reused, exchanged, or relied on for a decision.

**How**: capture each model's recorded origin and lineage (provenance and pedigree) as it is developed under policy, guidance, standards, and formalisms; base reuse decisions and model-based reviews/audits on verification and validation attributes, not on the model merely existing.

**Trade-offs**: recording lineage and running V&V-based reviews is overhead — but a model with no documented pedigree is untrustworthy and unreusable, forcing expensive re-creation or, worse, decisions made on unverified data.

---

## Pattern 3: Define → Govern → Use the authoritative source of truth (Goal 2 arc)

**When to use**: when standing up the shared model-and-data reference for an enterprise or program.

**How**: follow the 2.1→2.2→2.3 progression. **Define** (2.1) what the AST is and what it captures (current state + technical-baseline history), planning the data needs for acquisition and engineering decisions. **Govern** (2.2) with policies, procedures, standards, and access controls so data stays trusted and compliant. **Use** (2.3) it across the lifecycle as the technical baseline, the source of digital artifacts, and the basis for reviews, decisions, and collaboration.

**Trade-offs**: governance adds process, but the chain is explicit — governance raises data quality, data quality raises confidence, and confidence is what lets people make data-driven decisions. Without it the AST becomes just another silo nobody can rely on.

---

## Pattern 4: Hold the open-but-guarded tension on access

**When to use**: when defining who may reach the authoritative source of truth and how.

**How**: define access and controls so data flows uninterrupted to all intended recipients across organizational boundaries *and* stays protected from unauthorized users — treat both halves as failure modes, not a one-sided lockdown. Combine with cybersecurity integrated into every phase (Goal 4.3) to protect classification, availability, and integrity.

**Trade-offs**: maximizing flow and maximizing protection pull against each other; the Strategy frames this as a deliberate balance to hold, not a problem to solve once. Drop either half and you either leak data or starve the people who need it.

---

## Pattern 5: Bet on standards and interfaces, not specific tools (Goal 4.2)

**When to use**: when selecting and provisioning the digital engineering tool environment.

**How**: concentrate on standards, data, formats, and the interfaces *between* tools rather than locking into specific products; evaluate tools against current and future stakeholder needs for visualization, analysis, model management, model interoperability, workflow, collaboration, and extensibility; weigh license agreements and data-exchange requirements; favor modular approaches and commercial cloud for scalable, cost-effective, faster deployment.

**Trade-offs**: standards-first integration is more work up front than adopting one vendor stack — but it keeps the enterprise from being constrained by or captive to particular tools as technology turns over.

---

## Pattern 6: Infuse technology as a managed practice, not an occasional upgrade (Goal 3)

**When to use**: when improving the engineering practice with advancing technology.

**How**: build on the model-based foundation of Goals 1–2 and work three lines of effort — make better use of data for awareness and decisions, advance human-machine interaction, and improve the technology insertion process (marketplace-leveraged, high-payoff, cost-effective selection). Keep the digital representation evolving alongside the physical end item so the operational environment continuously feeds insight back in.

**Trade-offs**: continuous infusion demands rigorous, ongoing selection discipline and weighs both current and future needs — slower than grabbing whatever is newest, but it avoids costly, poorly integrated bolt-ons.

---

## Pattern 7: Transform the people, not just the machine (Goal 5)

**When to use**: alongside every technical digital engineering effort — adoption is the gating risk.

**How**: treat transformation as change management led from the top. Improve and organize the knowledge base and close the standards gap (5.1); communicate the vision, build cross-sector alliances, and establish metric-backed accountability with champions and short- and long-term wins (5.2); and prepare a dispersed, multidisciplinary, multigenerational workforce, converting training into new habits through active participation and "doing" (5.3). Reach contracting, legal, and business practices (RFP/SOW/CDRL/DID), not only engineers.

**Trade-offs**: cultural change is slow, sustained, and hard to measure — the harder side of a socio-technical change — but the four technical goals are inert without a workforce and culture able to adopt them.

---

## Pattern 8: Pilot before you scale (Next Steps)

**When to use**: when moving from strategy and implementation plans toward major-program adoption.

**How**: sequence the transition as coordinate → develop implementation plans → pilot → sustain. Stand up bounded pilot programs to surface barriers and evaluate tools, processes, and cost; learn, measure, and optimize for efficiency and effectiveness; only then scale into major programs and institutionalize through policy, guidance, training, and continuous improvement.

**Trade-offs**: piloting delays full rollout, but it deliberately keeps failure cheap — discovering barriers in a bounded pilot is far less costly than discovering them across a major program.

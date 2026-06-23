# DoD Digital Engineering Strategy — Cheatsheet

## Quick Decision Rules

**"What is digital engineering, in one line?"**
An integrated digital approach using **authoritative sources of system data and models** as a **continuum across disciplines** to support lifecycle activities **from concept through disposal**.

**"Is the Strategy telling me exactly how to do this?"**
No. It is a **non-prescriptive, living document** — a compass, not a checklist. The concrete "how" lives in **DoD Component / Service implementation plans**.

**"Where does the modeling effort start?"**
With **planning (Goal 1.1)** — establish formalisms (syntax, semantics, lexicons, standards) before developing models, or they won't integrate.

**"How do I know a model can be trusted or reused?"**
By its **provenance and pedigree** plus **V&V-based reviews/audits** — trust is engineered and recorded, never assumed.

**"What makes the AST authoritative rather than just another silo?"**
**Governance.** Governance → data quality → stakeholder confidence → data-driven decisions. Skip governance and the chain breaks.

**"Tool decision — what do I optimize for?"**
**Standards, data, formats, and interfaces between tools** — not a specific vendor product. Weigh license and data-exchange terms; lean modular and cloud.

**"Why isn't the technology enough?"**
Because **culture is the operating system** (Goal 5). The four technical goals are inert without a workforce and culture able to adopt them.

**"How do we move from strategy to practice?"**
**Coordinate → plan → pilot → sustain.** Pilot before scaling so failure stays cheap.

---

## The Five Goals (at a glance)

| # | Goal | One-line intent | Chapter |
|---|------|-----------------|---------|
| **1** | Formalize models | Formalize the development, integration, and use of models to inform enterprise & program decisions | ch02 |
| **2** | Authoritative source of truth | Provide an enduring, authoritative source of truth — move communication from documents to models/data | ch03 |
| **3** | Technological innovation | Incorporate technological innovation to improve the engineering practice | ch04 |
| **4** | Infrastructure & environments | Establish supporting infrastructure and environments to perform, collaborate, and communicate | ch05 |
| **5** | Culture & workforce | Transform the culture and the workforce so digital engineering is adopted and sustained across the lifecycle | ch06 |

---

## Goal → Focus Areas (Appendix 1 map)

- **Goal 1** — 1.1 plan for models · 1.2 develop/integrate/curate models · 1.3 use models in decisions.
- **Goal 2** — 2.1 define the AST · 2.2 govern the AST (access, controls, governance) · 2.3 use the AST across the lifecycle.
- **Goal 3** — 3.1 establish an end-to-end digital engineering enterprise · 3.2 use technological innovations to improve the practice (better use of data · human-machine interaction · technology insertion).
- **Goal 4** — 4.1 develop/mature/use IT infrastructures (networks, hardware, software) · 4.2 develop/mature/use methodologies (methods, processes, tools) · 4.3 secure the infrastructure & protect IP.
- **Goal 5** — 5.1 improve the knowledge base (policy/standards, contracting, best practices) · 5.2 lead & support transformation (vision, alliances, accountability) · 5.3 build & prepare the workforce.

---

## Mental-Model Shifts the Strategy Demands

| From | To |
|------|-----|
| Document-centric, sequential | Model-based, connected continuum |
| Design-build-test | **Model-analyze-build** (virtual-first) |
| Disposable, phase-local artifacts | Models that **live and evolve** concept→disposal |
| Accept the **document** as deliverable | Accept the **model** as deliverable |
| Many copies, "which is current?" | One **authoritative source of truth**, traced |
| Stove-piped, program-by-program IT | Consolidated, collaborative, trusted environment |
| Lock into specific tools | Bet on **standards & interfaces** |
| One-off gate-date reviews | **Continuous** reviews from a living baseline |
| Technology rollout | Socio-technical **culture & workforce** change |

---

## Goal 4 — Environment success criteria (Figure 7)

The supporting environment must: **keep pace with technology** · **strengthen cybersecurity and IP protection** · **improve information sharing**. Provide solutions at both **enterprise** and **program** level.

## Goal 5 — Culture/workforce enablers (Figure 8)

**Training · Education · Strategic communication · Leadership · Continuous improvement** — ongoing, mutually reinforcing levers, not a one-time launch. Arc of the focus areas: **knowledge (5.1) → leadership (5.2) → people (5.3)**.

---

## The Four Next Steps

1. **Coordinate** — ODASD(SE) convenes a summit and runs the standing **DEWG**.
2. **Develop implementation plans** — owned by the **DoD Components**, supported by ODASD(SE).
3. **Implement pilot programs** — learn, measure, optimize before scaling into major programs.
4. **Sustain** — policy, guidance, training, and continuous improvement institutionalize the practice.

*Ownership: Components own the plans; ODASD(SE) coordinates (gap-closer, not gatekeeper).*

---

## Worked Examples Cited in the Strategy

| Example | Goal | What it shows |
|---------|------|---------------|
| **USS Ford (CVN-78)** | 1 | First ship fully designed on a full-scale 3-D product model; projected multi-billion-dollar lifecycle savings over 50 years |
| **U.S. Army LPDM/ePDM** | 2 | Lifecycle/enterprise product data management as an authoritative source of truth |
| **A-10 Wing Replacement** | 3 | 3-D MBD + PLM built a sustainment-phase digital thread and identified the AST |
| **Engineered Resilient Systems (ERS)** | 4 | Integrated computational/simulation/trade-space tools; 19M+ Navy ship designs |
| **NAVAIR SE Transformation** | 5 | Modeling environments + policy + workforce/culture + pilots to cut cycle time |

---

## Tells & Smells

- **Modeling with no plan or formalisms** → models won't integrate (skipped Goal 1.1).
- **A model with no provenance/pedigree** → untrustworthy, unreusable; decisions on unverified data.
- **An "AST" with no governance** → just another silo nobody can rely on.
- **Access locked down OR wide open** → both halves of open-but-guarded are failure modes.
- **Tool-first selection** → vendor lock-in; bet on standards and interfaces instead.
- **Bolt-on technology** → innovation must build on the model-based foundation, not run parallel.
- **Stove-piped, program-by-program IT** → the exact state Goal 4 exists to replace.
- **Treating the Strategy as a procedure** → it is intent-setting; the "how" is in implementation plans.
- **Technology rollout with no culture plan** → Goal 5 is co-equal; adoption is the gating risk.
- **Scaling to a major program without piloting** → failure gets expensive; pilot first.
- **Accepting documents as the deliverable** → defeats the document-to-model shift; documents are generated views.

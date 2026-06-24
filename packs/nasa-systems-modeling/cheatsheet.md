# NASA Systems Modeling Handbook — Cheatsheet

Fast-reference decision rules and tables for NASA-HDBK-1009A Rev A (2025). Synthesized;
NPR 7123.1 and the NASA SE Handbook govern.

---

## The one-line thesis

> The **model** is the source; **diagrams, tables, and matrices** are views extracted from it to implement the SE processes and feed reviews. SysML/tools are illustrations — the **metamodel** (traceable to NPR 7123.1) is what carries meaning.

---

## The three aspects of MBSE (keep them distinct)

| Aspect | Question it answers | Handbook's choice |
|---|---|---|
| **Language** | What do the symbols mean? | SysML (OMG v1.7) |
| **Methodology** | What order do I do things in? | NASA SE Engine + 2 OOSEM steps |
| **Framework** | Where does everything go? | MBSE Grid tailored to NASA |

The metamodel sits *underneath* all three — that's why the language dial is swappable.

---

## Methodology = SE Engine + two added steps

| Added step | Lands in | Produces / does |
|---|---|---|
| **Model Planning** | Technical Process 10 (Technical Planning) | the **Modeling Plan** (a SEMP subset) |
| **Setting Up the Model** ("Step 0") | start of System Design Processes | conventions, standards, organization |

**Setup mnemonic:** *name it (conventions) · govern it (standards) · file it (organization).*
**Plan mnemonic:** *the Modeling Plan is the SEMP, zoomed in — and it's living, not one-and-done.*

---

## The four SysML pillars

| Pillar | Covers | Diagrams |
|---|---|---|
| **Structure** | systems, subsystems, components, interfaces | bdd, ibd, package |
| **Behavior** | functionality, interaction, response, flow | uc, act, sd, stm |
| **Requirements** | specifications, V&V | req, requirements table |
| **Parametrics** | constraints, math statements | parametric |

Nine SysML diagram types total = 4 behavior + 1 requirement + 4 structure.

---

## The relationship verbs (the value lives here)

| Verb | Connects | Use it for |
|---|---|---|
| **derive** | requirement → requirement | flow-down (Needs→Goals→Objectives→reqs) |
| **trace** | stakeholder→need; measure→req/structure | linking the web |
| **satisfies** | requirement ← block/behavior/value | "met"; validation requirements |
| **verifies** | verification req → system req (1-to-many) | verification |
| **refines** | MOE→objective; MOP→requirement | refinement |
| **allocate** | behavior → structure (swim lanes) | activity allocation |

---

## The measure chain

```
MOE  (qualitative — does it satisfy the stakeholder?)
  └─ refined by →  MOP  (quantitative target; satisfying it props up the MOE)
                     └─ time-tracked subset →  TPM  (current vs. anticipated over time)
```

- **MOP encoding:** a requirement element holding the quantitative target + a `satisfies` relationship ("met") + a `trace` up to its MOE.
- **TPM:** one or more value properties; may be defined on a block or computed (computed = marked derived with a slash `/`).
- MOE↔MOP is **not** one-to-one; measures can sit at multiple design levels.

---

## V&V pattern (learn once, swap the verb)

| | Verification | Validation |
|---|---|---|
| Question | built to its requirements? | meets stakeholder intent in use? |
| Relationship | `verifies` | `satisfies` |
| Success criteria | constraint `{ }` on the requirement | constraint `{ }` on the requirement |
| Owns | V&V case → V&V activity | (same) |
| References | shared V&V configuration | (same, reusable) |

- `verifyMethod` attribute: put on the **requirement** early, migrate to the **verification requirement** later.
- Diagram ↔ matrix/VCS = two windows on one model.
- Matrix columns are a tailoring choice (facility column omitted because that data lives in the V&V configuration parts).

---

## MBSE Grid layout (tailored to NASA)

| Grid section | Row | Maps to NASA System Design Process |
|---|---|---|
| **Problem** | Black box (conceptual) | Stakeholder Expectation Definition |
| **Problem** | White box (technical) | Technical Requirements Definition + Logical Decomposition |
| **Solution** | design alternatives | Design Solution Definition |

- Rows = technical processes **1–9** (management processes **10–17 excluded** from the Grid).
- Columns = the four pillars. Cross-sections file the diagrams/tables (Appendix C = populated example).
- A diagram may legitimately appear in more than one row, tuned per process.

---

## Alternative approaches (Appendix D — a menu, by pillar)

| Approach | Extends pillar | What it adds | Source |
|---|---|---|---|
| **PBR** (Property-Based Requirements) | Requirements | numerical attributes + constraints on a requirement | App. D.2 |
| **Scenario Modeling** | Behavior | context block bridging activities ↔ state machines | OpenSE Cookbook |
| **System Specification** | Structure→Requirements | Logical/Node/Physical Design + Spec Block bridge | OpenSE Cookbook |
| **Verification Modeling** | V&V / Parametrics | Verification Context Block + parametric diagram | OpenSE Cookbook |

Each must still trace back to the section 7 metamodel; record the choice in the Modeling Plan.

---

## ConOps section → model view (Appendix F)

| ConOps section | Primary model view(s) |
|---|---|
| Overview (1.2 / 3.2) | context bdd (+ ibd); bdd with values tied to MOE/MOP |
| Needs/Goals/Objectives (3.1) | requirements table + requirements diagram |
| Interfaces (3.3) | context ibd; interface tables; structural ibd |
| Modes of operation (3.4) | state machines; modes table; modes↔phases/scenarios matrices |
| Proposed capabilities (3.5) | use cases; activity/functional decomposition |
| Environment (4.0 / 5.0) | environment bdds (subset of structural bdd) |
| Scenarios / use cases / DRMs (6.0) | uc, act, stm, sd for each thread (nominal + off-nominal) |
| Risks (8.0) | block with impact/likelihood value properties |

**Draw once, reference many.** Keep the SE Handbook (App. S) outline text intact; label threads `[DRM-0100]`.

---

## Tells & smells (when something is off)

- **Diagrams treated as the deliverable** → you've reverted to document-centric SE; the model should be the source.
- **A diagram using elements/relationships the metamodel doesn't sanction** → you skipped pairing it with its metamodel fragment.
- **A Modeling Plan written at concept and never updated** → stale; the plan is supposed to breathe with the life cycle.
- **A modeling decision with no trace up to a SEMP/NPR 7123.1 obligation** → it probably doesn't belong in the plan.
- **Forcing a stakeholders→context→behavior→structure→reqs waterfall** → order doesn't matter; SE work enters the Engine at many points.
- **Keeping a requirements diagram and its matrix "in sync" as two documents** → they're two views of one model; treat them as interchangeable.
- **Maximizing structural decomposition depth** → decompose to need, not to exhaustion.
- **An alternative approach that can't trace back to the section 7 metamodel** → it's no longer auditable against NASA SE process.
- **Trying to model technical-management processes (10–17) on the MBSE Grid** → the Grid only covers processes 1–9.

---

## Scope reminders

- In scope: **4 processes** — Stakeholder Expectation Definition, Technical Requirements Definition, Product Verification, Product Validation.
- Tool-agnostic: MagicDraw / CATIA No Magic / SysML 1.7 are illustrations; no NASA endorsement.
- Current binding is **SysML 1.7**; handbook commits to updating for **SysML v2.0**.
- This is **Revision A (2025-03-12)**, Approved for Public Release, Distribution Unlimited.

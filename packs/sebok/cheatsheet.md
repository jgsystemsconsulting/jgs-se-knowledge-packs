# SEBoK Cheatsheet

Quick decision rules, selection tables, and tells & smells from the SEBoK v2.14. Synthesized for reference use under CC BY-NC-SA 3.0; attribution to the BKCASE Project required.

## Quick Decision Rules

**"Where do I start?"**
The **problem space** — Business/Mission Analysis then Stakeholder Needs Definition. Fix why and what before how. Never architecture-first. (Ch 16)

**"What is the system, exactly?"**
Scope the **engineered-system context**, not the bare system: the related engineered, social, and natural systems and environments. Use the Seven Samurai as a forget-nothing checklist. (Ch 7, Ch 2)

**"How much SE is enough?"**
A risk-balance dial, not a switch: too little → rework explodes on large projects; too much → analysis paralysis. Scale with size and interdependence. (Ch 1)

**"Which development approach?"**
By three questions — requirements known up front? work split into increments? what are the increments for? → sequential / incremental / evolutionary (agile overlaps). All real efforts are concurrent and iterative to some degree. (Ch 10, Ch 12)

**"Serial process sequence?"**
No. Expect **concurrency, iteration, recursion**. Describe processes uniformly (24774); select from 15288; tailor with 24748-2 and document the rationale. (Ch 13, Ch 14)

**"When do I do V&V?"**
Concurrently and recursively, level by level up the right of the **Vee** — never one big bang at the end. (Ch 17, Ch 10)

**"Is this a true System of Systems?"**
Check Maier: **operational + managerial independence** of constituents (plus evolution, emergence, distribution). If yes, **compose** via interfaces; you don't command it. (Ch 24)

**"Product, service, enterprise, or SoS context?"**
They overlap — most real systems need a combination. Pick the dominant context to drive tailoring, then borrow from the others. (Ch 20)

**"Competency vs. performance?"**
Different things. A competent individual can still perform poorly if team capability, capacity, or culture block them. Enable all three levels. (Ch 28, Ch 26)

**"Who owns what — SE or PM?"**
No standard split. PM owns programmatic, SE owns technical; decide per project, write it in the PMP and SEMP. (Ch 31)

---

## The Eight Parts of the SEBoK

| Part | Title | Pack chapters |
|---|---|---|
| 1 | SEBoK Introduction | ch01 |
| 2 | Foundations of SE | ch02–ch07 |
| 3 | SE and Management | ch08–ch19 |
| 4 | Applications of SE | ch20–ch25 |
| 5 | Enabling SE | ch26–ch28 |
| 6 | Related Disciplines | ch29–ch34 |
| 7 | SE Implementation Examples | ch35 |
| 8 | Emerging Knowledge | ch36 |

## Three Grades of SE Knowledge

**Concept** (mental building block) → **Principle** (generalization usable for reasoning/action) → **Heuristic** (works in practice; the "why" not yet scientifically explained). Observed heuristics drive research toward principles and a systems-science basis. (Ch 2, Ch 5)

## Holism ↔ Reductionism

The balance at the heart of any systems approach: treat the whole (because of emergence) **and** study the parts (because pure holism can't be acted on). (Ch 5)

## Development Approaches — Selection

| Family | Use when | Representative models |
|---|---|---|
| **Sequential** | requirements well-known, low change | Waterfall, Vee, Dual Vee |
| **Incremental** | requirements known, deliver in defined increments | Incremental Commitment Spiral Model |
| **Evolutionary** | requirements emerge through use | evolutionary delivery, DevOps/DevSecOps |
| **Agile (overlaps)** | high uncertainty, fast change | Scrum, SAFe, LeSS; Industrial DevOps |

## Architecture Views (Architecture Definition)

**Functional** (what it does) · **Logical** (behavioural/temporal, implementation-independent) · **Physical** (system elements and groups). Carry PIM→PSM and govern via an Authoritative Source of Truth in MBSE. (Ch 17)

## SE Standards Landscape (trunk + branches)

**ISO/IEC/IEEE 15288** = trunk (system life-cycle processes). Branches/companions: **24748-1** (terms/concepts), **24748-2** (applying 15288), **24748-10** (agile), **24774** (process-description form), **12207** (software life cycle). Take a full-life-cycle approach to any standard: evaluate → select → adapt/tailor → assess → improve. (Ch 19, Ch 14, Ch 13)

## Applications — Five Contexts (Part 4)

**Product SE** (end product + enabling products; NPDP) · **Service SE** (value co-creation; can't inventory) · **Enterprise SE** (enterprise as a system; people are components) · **Systems of Systems** (compose independent constituents) · **Healthcare SE** (domain extension over the others). (Ch 20–25)

## Quality Attributes / Specialty Engineering

Same things, four names: **quality attributes = non-functional requirements = -ilities = specialties**. They're interdependent, not orthogonal. Engineer them as specialty engineering; where they share a concern with **loss**, use a Loss-Driven view (assets, loss, adversity, coping strategies) instead of per-"-ility" silos. (Ch 34)

## Enabling SE — Three Levels (Part 5)

**Business/Enterprise** (PDCA: strategy → capabilities → org → assessment → development → barriers → culture) → **Team** (capability + dynamics; Tuckman; IPTs) → **Individual** (roles + KSAA competency; assess → develop; ethics). (Ch 26–28)

---

## Tells & Smells

- **"We'll define the problem as we build."** — skipped Concept Definition; you're optimizing an unstated or wrong problem. (Ch 16)
- **Architecture set before stakeholder needs are integrated.** — solution-first; needs should drive architecture. (Ch 16, Ch 17)
- **A single "best" life cycle model imposed org-wide.** — life cycle models are situation-specific and adapted per project, not inherited. (Ch 12)
- **Processes run as a fixed serial sequence.** — ignores mandated concurrency, iteration, recursion. (Ch 13)
- **All V&V deferred to a final test phase.** — big-bang V&V concentrates risk; the Vee runs it level by level. (Ch 17)
- **Treating an SoS as if one authority owns it.** — managerial/operational independence means compose, don't command. (Ch 24)
- **Digital Engineering bought as a tool.** — "new paint on crumbling walls"; DE is a Why/What/Who/How transformation, MBSE is one part. (Ch 1, Ch 36)
- **Each "-ility" engineered in its own silo.** — produces conflicting requirements; use a unified loss-driven view. (Ch 34)
- **Assuming competency guarantees performance.** — team capability, capacity, and culture can block a competent engineer. (Ch 28)
- **Leaving the SE/PM boundary implicit.** — no standard split exists; un-negotiated boundaries leave gaps and double-ownership. (Ch 31)
- **Reading SwE as a subset of SE (or vice versa).** — bounded overlap, neither contains the other. (Ch 1, Ch 32)
- **Blaming the domain for a systems-engineering shortfall.** — large-system failures most often trace to inadequate SE, not the domain disciplines. (Ch 1)

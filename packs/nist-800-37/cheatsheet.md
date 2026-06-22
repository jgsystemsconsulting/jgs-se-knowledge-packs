# NIST SP 800-37 Rev. 2 (RMF) Cheatsheet

Fast-reference decision aids for running the Risk Management Framework. Paraphrased from
SP 800-37 Rev. 2; for the controlling text consult the source and its companions
(SP 800-53/53B, SP 800-39, FIPS 199/200, SP 800-137, SP 800-161).

---

## The seven RMF steps and their tasks

| Step | Tasks | One-line purpose | Chapter |
|---|---|---|---|
| **Prepare** | P-1…P-7 (org), P-8…P-18 (system) | Establish roles, risk strategy, common controls, baselines, boundaries, requirements | ch03 |
| **Categorize** | C-1, C-2, C-3 | Fix the system's impact level from loss-of-CIA consequences | ch04 |
| **Select** | S-1…S-6 | Choose, tailor, allocate, document controls; set monitoring | ch04 |
| **Implement** | I-1, I-2 | Build the controls, then record the as-built configuration | ch05 |
| **Assess** | A-1…A-6 | Prove controls are correct, working, and effective; route findings | ch05 |
| **Authorize** | R-1…R-5 | Accept (or refuse) residual risk by a named senior official | ch06 |
| **Monitor** | M-1…M-7 | Sustain situational awareness; ongoing authorization; disposal | ch07 |

Prepare runs first; after that, steps may run **non-sequentially** (driven by system
type, leadership risk decisions, agile cycles, or monitoring findings). The only fixed
point: the authorizing official explicitly accepts risk *before* the system operates.

---

## The assessment criterion (the three-part test)

A control passes assessment only when **all three** hold:
1. it was **implemented correctly**,
2. it is **operating as intended**, and
3. it **produces the outcome** needed to satisfy the security/privacy requirements.

This same triple defines initial assessment (A-3), reassessment after remediation (A-5),
and ongoing assessment (M-2).

---

## Categorize: which roll-up?

| System type | Roll-up rule | Standard |
|---|---|---|
| Non-national-security | Single impact level = **high-water mark** across information types | FIPS 199 / FIPS 200 |
| National security system | **Three separate values** (C, I, A may differ) — no high-water mark | CNSSI 1253 |

Impact levels: **low / moderate / high**. The privacy official approves the
categorization of PII systems *before* the authorizing official does.

---

## Select: baseline vs. organization-generated

| Use the **baseline** (top-down) approach when… | Use the **organization-generated** (bottom-up) approach when… |
|---|---|
| The system is mainstream / typical | The system is highly specialized (weapons system, medical device) |
| A predefined SP 800-53B baseline fits | The system is limited in scope (smart meter) |
| Consistency across many systems matters | Importing a broad baseline only to delete most of it is wasteful |

Approaches can be mixed across a portfolio. Both require requirements produced by a
life-cycle SE process (SP 800-160 v1 / ISO/IEC/IEEE 15288) — **requirements first,
controls second.**

---

## Control allocation: three designations

| Designation | Who implements / assesses | Inheriting systems |
|---|---|---|
| **System-specific** | Implemented and assessed for the one system | n/a |
| **Common** | Provided by the organization; assessed once by the provider | Inherit it; do not re-assess |
| **Hybrid** | Partly central, partly system-level | Inherit the common part; implement and document the rest |

Allocate a control only to the elements (machine, physical, human) that need the
capability — not every control to every element.

---

## Routing a deficiency (three destinies)

```
finding ──► exploitable?  ── no ─► still a finding (not a vulnerability)
                │ yes
                ▼
          deficiency ──► fix now?     ─► remediate + reassess (A-5); add, never overwrite
                     ──► schedule it?  ─► POA&M entry (A-6): tasks, resources, milestones, dates
                     ──► accept it?    ─► AO-only; logged in assessment reports; no milestone
```
Prioritize by **risk assessment + security categorization + mission criticality**, not
arrival order.

---

## Authorization: types and the one non-delegable rule

| Output | Cascades to… |
|---|---|
| Authorization to **operate** | the system | 
| Authorization to **use** | a system the org didn't build but relies on |
| **Common control authorization** | every system inheriting those controls, at the stated impact level |

…each with a matching **denial**. **Risk acceptance cannot be delegated** — it is the
authorizing official's personal accountability. Every RMF step can be performed by an
external provider **except Authorize**.

---

## Dated vs. ongoing authorization

| Classic (dated) | Ongoing |
|---|---|
| Fixed termination date | Time-driven re-judgment **frequency** |
| Periodic re-authorization event | Reauthorization is a by-product of a live package |
| Snapshot of risk | Continuous stream from monitoring evidence |

Ongoing authorization requires a **robust, mature continuous monitoring program** and
timely artifact updates.

---

## Tells & smells (failure modes the source warns about)

- **Skipping organizational Prepare** → costly, redundant, vulnerable systems and scarce
  skills burned per-system.
- **Mis-sized authorization boundary** → too wide = needless complexity; too narrow =
  many separately managed systems and inflated cost.
- **Treating privacy as "secured PII"** → misses harms from *authorized* processing;
  privacy needs its own program and expertise.
- **Assessing only at the end** → forfeits cheap early fixes and evidence reuse.
- **Treating product validation as system validation** → a lab evaluation covers a COTS
  product in isolation/one configuration; integration can break its assurance.
- **Letting the authorization package go stale** → ongoing authorization and
  reauthorization silently break.
- **Overwriting original assessment results** on reassessment → assessors *add* findings,
  never erase the originals.
- **Destroying audit-relevant information** during artifact updates → breaks
  traceability and accountability.
- **Disposing of a system without reviewing inheritance** → can leave dependent systems
  exposed.

---

## Where RMF meets systems engineering

| RMF construct | SE seam |
|---|---|
| Controls | Decompose into specification + statement-of-work requirements engineers build and test |
| Assess (A-1…A-6) | The RMF's verification & validation lane (SP 800-160 v1 V&V) |
| Implement (I-1/I-2) | SP 800-160 v1 Implementation, Integration, Configuration Management |
| Monitor | The RMF expression of in-service surveillance / operations & maintenance |
| Authorization boundary | Defines the "system of interest" for risk purposes (ISO/IEC/IEEE 15288 system definition) |

RMF governs **how much** protection and **whether to accept residual risk**; the
engineering disciplines (see `nist-sse`, `dau-se-guidebook`, `nasa-npr-7123`) decide
**how** protection is built.

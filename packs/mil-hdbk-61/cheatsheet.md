# Cheatsheet — MIL-HDBK-61B Configuration Management

Fast-reference decision rules, selection tables, and tells & smells. For the
authoritative requirements behind any item here, go to the EIA-649 suite; this is
the quick lookup, not the source of obligation.

---

## The five CM functions (one process, five activities)

| # | Function | One-line job | Chapter |
|---|---|---|---|
| 1 | **Management & Planning** | Plan, establish, manage, improve the CM program; coordinate the other four | ch02 |
| 2 | **Configuration Identification** | Select CIs, document attributes, assign identifiers, release docs, set baselines — *the foundation* | ch03 |
| 3 | **Configuration Control / Change Management** | Prepare, evaluate, disposition, and implement changes and variances | ch04 |
| 4 | **Configuration Status Accounting (CSA)** | Record and report configuration, change, and audit status — *the knowledge base* | ch05 |
| 5 | **Configuration Verification & Audit** | Prove the built item matches its documentation and performs (FCA + PCA) | ch06 |

> Identification is foundational — control, CSA, and audit all consume its
> products. If identification is wrong, everything downstream inherits the error.

---

## The three baselines (the spine of CM)

| Baseline | Captures | Doc set | Established |
|---|---|---|---|
| **FBL** (Functional) | System-level performance, interoperability, interface + verification | FCD | When FCD is Government-approved; always Government-controlled |
| **ABL** (Allocated) | CI-level performance/functional/interface allocated from above + verification | ACD | Per CI; Government *or* contractor control |
| **PBL** (Product) | Complete functional + physical definition for production/re-procurement | PCD | Initial per CI at CDR; finalized & validated at PCA |

- **Order of precedence on conflict:** FCD → ACD → PCD (always).
- **Developmental configuration** = contractor's internal, evolving design before PBL.
- **Same baseline, two viewpoints:** an ABL to the prime is an FBL to the subcontractor.

---

## Change instruments — pick the right one

| Instrument | What it is | Goes to |
|---|---|---|
| **ECP** (DD 1692) | The change itself | CCB (Class I) / local rep concurrence (Class II) |
| **NOR** | The precise documentary edits tied to an ECP | With the ECP; optional if originator controls the doc |
| **RFV** (DD 1694) | Bounded permission to deliver/install off-baseline | Government — approval is inherently Governmental, non-delegable |

**Class I vs Class II:** Class I (Major) touches approved functional/allocated/
product requirements (or cost, warranties, contract milestones) → CCB + contract
mod. Class II (Minor) = any approved-doc change that is not Class I → local rep
concurrence.

**Who approves?** Government baseline touched, or contractually specified impact on
a Government CI → Government. Contractor's own docs, no Government baseline touched
→ contractor. One **CDCA** per document, always; **AAs** may comment but never
authorize.

---

## Audits — FCA vs PCA

| | **FCA** (Functional Configuration Audit) | **PCA** (Physical Configuration Audit) |
|---|---|---|
| Question | "Does it perform?" | "Does the documentation match what we deliver?" |
| Verifies | Actual performance vs. performance spec | Design documentation vs. delivered design; validates production processes |
| Establishes | — | Locks down the PBL |
| When | EMD (normal focus) | Slips toward early production (EMD articles may be unrepresentative) |

- Run audits in **three phases**: pre-audit → audit → post-audit. Not done until
  every action item is closed.
- **Not in MSA/TMRR** (no production-ready design that early); central in
  EMD/Production; generally absent in O&S.
- A strong, evidenced verification process makes the audit light; a weak one forces
  a heavyweight audit.

---

## CM intensity by phase (the curve)

| Phase | Identification | Control | CSA | Audit | Appendix C template? |
|---|---|---|---|---|---|
| **MSA** (pre-Milestone A) | n/a | n/a | n/a | n/a | **No template** — CM not applicable |
| **TMRR** | active (process stand-up) | informal | active | **not applicable** | C-1 |
| **EMD** | establish FBL/ABL/PBL | formal; CCB online | active | **central (FCA/PCA)** | C-2 (most elaborate) |
| **Production & Deployment** | maintain baselines | formal | active | central | C-3 |
| **Operations & Support** | re-identify after change | joint Gov/contractor | active | **generally not applicable** | C-4 (leanest) + demil/disposal |

---

## Tailoring flow (Appendix B)

1. **Determine** recommended CM requirements from the Figure B-1 matrix (R / T / NR per phase).
2. **Tailor** — select the corresponding EIA-649-1 "shall" statements via Annex A worksheet.
3. **Incorporate** the selected statements into the tasking document.
4. **Execute** day-to-day CM (GEIA-HB-649 is the working reference).

- **R / T / NR** = Recommended / Tailorable / Not Recommended; read **per phase**.
- EIA-649 principles are copyright-protected (reference only); **Annex A may be quoted directly in contracts**.
- Tailoring factors: phase, contract type, acquisition method, complexity, size, intended use, mission criticality, logistics support.

---

## Data-rights ladder (ch07)

| Data / funding | Rights |
|---|---|
| Form-Fit-Function (FFF) and Operation/Maintenance/Installation/Training (OMIT) | **Unlimited** (automatic) |
| 100% Government-funded | **Unlimited** |
| Mixed funding | **Government purpose rights** |
| Solely private funding | **Limited / restricted rights** |

> Above-default rights are negotiable with the OEM. **Order ≠ own ≠ hold:** order
> via CDRL/DID, secure rights, and hold the master in a Government PDM system.
> **Never substitute access for delivery.**

---

## Tells & smells (anti-patterns)

| Smell | What it signals | Fix |
|---|---|---|
| Ad-hoc / erratic change management | No defined control process → "technical anarchy" | Stand up the formal control process for the phase |
| Recurring RFVs against the same characteristic | The requirement is too stringent or manufacturing is broken | Raise a Class I ECP to revise the requirement |
| CM measured for its own efficiency | Divorced from program objectives | Measure CM contribution against overall program objectives |
| Score-keeping / history-only metrics | Wrong metric design | Use a few critical, forward-focused metrics |
| Substituting access for delivery | No enforceable rights, no guaranteed availability | Order via CDRL/DID; take delivery; hold the master copy |
| Over-ordering / mis-ordering data | True need/use never understood → cost driver | Run a data requirements review to de-duplicate and validate |
| OEM is sole data store | Markings alterable; recovery hard at contract end | Hold the official copy in a Government PDM system |
| Hoarding technical data | Blocks reuse and downstream support | Treat data as a shared DoD corporate asset |
| Redundant configuration documentation | Conflicts between levels | Keep one consistent set; honor FCD→ACD→PCD precedence |
| Extravagant interface management | Over-engineering a simple boundary | Use the simplest method that works; escalate to ICWG only when needed |
| Uncontrolled MOSA interface | Recreates the lock-in MOSA was meant to break | Put interface specs/standards/control drawings under strict CM |
| Importing EIA-649-1 wholesale | Unnecessary requirements drive cost | Tailor — subtract from the vetted maximum per phase |

---

## Quick mental models

- **CM = the product's single source of truth** — one-to-one correspondence among
  the physical/digital thing, its defining documents, and its requirements.
- **Responsibility can't be delegated; authority can** — the Government PM owns the
  configuration no matter who does the work.
- **Identification is the floor; everything builds on it.**
- **CSA is exhaust, not extra work** — query it, don't re-instrument.
- **FCA = promise kept; PCA = map matches territory.**
- **DM is the supply chain; CM is the warehouse** — skip DM and CM has nothing
  legitimate to control.
- **The CM principle is constant; only the artifacts change** — paper, models,
  twins, algorithms all need identify-a-master / control-change / trace.
- **Tailoring is subtraction from a vetted maximum, not addition from zero.**

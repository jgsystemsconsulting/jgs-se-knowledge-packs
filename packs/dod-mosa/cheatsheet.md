# DoD MOSA Cheatsheet

## Quick Decision Rules

**"Is MOSA optional?"**
No. It is statutory (10 U.S.C. 4401–4403) and applies *to the maximum extent practicable* across every AAF pathway. The pathways change how *formally* it is enforced, never *whether* it applies.

**"Where do I start?"**
A cost-benefit analysis at the front, then the interface-lifecycle framework: *plan → modularize → identify → define → standardize*. Decide the *desired* level of modularity — a point on a spectrum, not the maximum.

**"When is MOSA real?"**
Only when it is contractual. Until MOSA is written into the RFP and Acquisition Strategy and backed by CDRLs/DIDs and data rights, it is intent, not commitment.

**"How do I know it worked?"**
Demand conformance certification (pillar 5) and metrics tied to the five benefit classes. Without V&V against the chosen open standards, the other four pillars are claims, not facts.

**"Which assessment tool?"**
By stakeholder and level: **PART** (Army, 24 questions) · **OAAT/OAAM** (Navy, business + technical axes 0–4) · **KOSS** (NAVAIR, lock-prone subsystems) · **SEAM** (Air Force, ten SE process areas). MAUT scores trade-offs and pairs against life-cycle cost.

---

## The Five OUSD(R&E) Pillars (current authority)

| # | Pillar | Core move |
|---|--------|-----------|
| 1 | **Establish an Enabling Environment** | Set requirements, business practices, strategy, and T&E before design hardens |
| 2 | **Employ a Modular Design** | Partition functionality before the RFP, driven by business + technical objectives |
| 3 | **Designate Modular Interfaces** | Decouple interface from implementation so each follows its own life cycle |
| 4 | **Leverage Consensus-Based Open Standards** | Standardize interfaces openly; manage Government interface repositories |
| 5 | **Certify Conformance** | Verify and validate that the build conforms to the selected open standards |

Read the pillars as a progression: each later pillar depends on the earlier ones. *(Note: PART scores against an older, legacy five-pillar set — Modular Design, Key Interfaces, Open Standards, Conformance, Enabling Environment — that overlaps but differs.)*

## The Five Benefit Classes (align metrics here)

Interoperability · Technology Refresh · Enhanced Competition · Innovation · Cost Avoidance / Cost Savings.

Secondary benefits: plug-and-play interchangeability · reuse · scalability · vendor independence · commonality · cyber resilience (patch one module, not the whole system).

## Statute → Regulation → Contract Chain

| Layer | Carries MOSA as… |
|---|---|
| **Statute** — 10 U.S.C. 4401–4403; FY2017 & FY2021 NDAA (Sec. 804) | the mandate + definitions (major system component/interface, modular system interface) |
| **Regulation** — DFARS 207.106, 227.7203-2; case 2021-D005; 252.227 | acquisition policy + data-rights clauses |
| **Contract** — RFP, Acquisition Strategy, SEP, CDD, CDRLs/DIDs | the binding obligation on industry |

A break anywhere — especially insufficient data rights — undermines the whole.

## MOSA Across the Six AAF Pathways

| Pathway (DoDI) | MOSA enforcement |
|---|---|
| **Major Capability** (5000.85) | Most prescriptive; located in Acquisition Strategy; carried into EMD + P&D RFPs with minimum major system components |
| **Software** (5000.87) | Stressed strongly; architecture must enable an interoperable MOSA; open interfaces on commercial/proprietary software |
| **Middle Tier** (5000.80) | Not required; rapid prototyping *should* where practical; rapid fielding must actively manage added integration risk |
| **Urgent Capability** (5000.81) | Not required, but modular open interfaces speed fielding and cut interface-failure risk |
| **Defense Business Systems** (5000.75) | Not specifically required; push COTS/GOTS toward maximum openness |
| **Acquisition of Services** (5000.74) | A pathway under the same maximum-extent-practicable obligation |

## Mandatory vs. Supporting Documents

- **Mandatory MOSA content** (10 U.S.C. 4401–4403; DoDI 5000.85; DoDI 5000.88): AoA/Economic Analysis · RFP · SEP · Acquisition Strategy · CDD.
- **Supporting ("address as appropriate")**: Product Support Strategy · LCSP · performance specs · architecture products · CWBS/CDRLs · **ICD + IRS** (the high-value interface artifacts).

---

## Tells & Smells

- **MOSA stated as intent** but absent from the RFP/Acquisition Strategy → not contractual, won't be delivered.
- **"Key interface"** used as if it were statutory → it isn't defined in current law; anchor legacy terms to statute.
- **Clean interface, no data rights** → modularity the Government can't legally exercise; not a MOSA success.
- **Modularity bolted on** to a mature design → fights fixed constraints; build it in via Figure 3-2.
- **Two standard implementations that don't interoperate** → missing a profile to pin the variability.
- **COTS-heavy MOSA with no business case** → a design change can force regression testing or recertification, erasing the benefit.
- **Buying IP rights everywhere (or nowhere)** → ignore the KOSS targeting of volatile, lock-prone interfaces.
- **OTA assuming DFARS data rights come along** → they don't; build equivalent terms by hand.
- **Document set treated as proof** → SEAM checks work-product existence, not delivered customer outcome.
- **Org chart misaligned with the architecture** → Conway's Law: the system inherits the organization's seams.
- **Refresh deferred with no roadmap** → DMSMS and obsolescence go unmanaged; pair product + technology roadmaps.

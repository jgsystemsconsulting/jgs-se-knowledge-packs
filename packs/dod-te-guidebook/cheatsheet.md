# DoD T&E Enterprise Guidebook Cheatsheet

Quick decision rules, selection tables, and tells & smells for DoD test and evaluation (OUSD R&E Enterprise T&E Guidebook, August 2022). This is **guidance**; binding requirements live in DoDI 5000.89 and the related DoDI 5000-series.

## Quick Decision Rules

**"Which test type is this?"**
- Contractor-run, to confirm the contractor's own work → **Contractor Testing (CT)**
- Generates substantiated knowledge of capabilities/limitations, verifies technical requirements, manages development risk → **Developmental Test & Evaluation (DT&E)**
- Judges operational effectiveness, suitability, survivability under realistic conditions and threats → **Operational Test & Evaluation (OT&E)**
- Characterizes survivability and lethality against likely combat threats → **Live Fire Test & Evaluation (LFT&E)**

**"Characterize or demonstrate?"** Align the test's purpose to the decision: is the event meant to *characterize* how the system behaves, or to *demonstrate* that a requirement is met? Knowing which keeps the test honest and rightsized.

**"Can I skip a dedicated DT&E / OT&E / LFT&E event by reusing data?"** No. Collaboration and the shared body of evidence *rescope* events; they never *replace* a dedicated test type. Reuse where data pedigree supports it; run the dedicated event regardless.

**"Can LFT&E be waived?"** No. Only **FUSL** (full-up/end-to-end) testing can be waived, via a two-part congressional package (certification of need + alternative LFT&E plan grounded in actual testing). There is no waiver from LFT&E itself.

**"Who approves my T&E Strategy / test plans?"** Read **oversight status first**. On the T&E Oversight List → **DOT&E** (final approver; TEMP ~45 days before the decision, operational test plans ~60 days before test start, deviations need DOT&E concurrence). Off the list → **Component/Service** level.

**"Is the system ready for an operational event?"** Only after the **OTRR** verifies reliability, maintainability, supportability, and hazard/ESOH/software-safety manageability.

**"Policy or guidance?"** This Guidebook = **guidance** (how). Binding requirements = **DoDI 5000.89** (T&E policy) and the related 5000-series and Title 10 statutes (what). Defer to policy in any conflict.

---

## The Four Test Communities

| Type | Owner / lead | Question it answers |
|---|---|---|
| **CT** — Contractor Testing | Contractor | Does the contractor's build meet its spec? |
| **DT&E** — Developmental T&E | Gov't (CDT / Lead DT Org), USD(R&E) oversight | Did we build it right (technical requirements)? Is it ready for OT? |
| **OT&E** — Operational T&E | OTA (independent), DOT&E oversight | Effective, suitable, survivable in realistic use? |
| **LFT&E** — Live Fire T&E | DOT&E oversight | Survivability (endure the threat) and lethality (defeat the target)? |

Integrate, streamline, automate, and reuse across all four — but each dedicated type still gets its event.

---

## Five Operational Events (the maturity ladder)

| Event | What it does |
|---|---|
| **Operational Demonstration** | Characterizes technical maturity, interoperability, risk in a threat-realistic setting |
| **Early Operational Assessment (EOA)** | Early, largely analytical read on operational risk (plans, early DT, M&S, reviews) |
| **Operational Assessment (OA)** | More realism; often a risk-reduction event ahead of IOT&E |
| **Initial OT&E (IOT&E)** | Statutory (10 U.S.C. §4171); production-representative articles, end-to-end, realistic combat conditions; gates full-rate production |
| **Follow-on OT&E (FOT&E)** | Confirms fixes, evaluates untested aspects, assesses modifications and new increments |

---

## The Six Acquisition Pathways and Their T&E Anchors

| Pathway (chapter) | Governing DoDI | T&E anchors |
|---|---|---|
| **Urgent Capability (UCA)** — ch04 | 5000.81 | 2-year fielding clock; tailored Strategy inside the Acquisition Strategy; first unit equipped is the test unit; FUSL waiver may precede LFT&E completion |
| **Middle Tier (MTA)** — ch05 | 5000.80 | 5-year cap; Rapid Prototyping (ops demo) vs. Rapid Fielding (IOT&E/OA/ops demo + PQT/FAT/AT); Strategy to DOT&E ≤45 days before program start |
| **Major Capability (MCA)** — ch06 | 5000.85 | Deliberate 5 phases (MSA→TMRR→EMD→P&D→O&S); milestone TEMP at A/B/C/FRP; ITRA/TRA/DTSA/DTA stack; IOT&E + FUSL |
| **Software Acquisition** — ch07 | 5000.87 | MVP (not operational) → MVCR (triggers IOT&E); continuous automated test; BDD/ATDD (Given-When-Then); risk-informed OT&E after MVCR |
| **Defense Business Systems (DBS)** — ch08 | 5000.75 | Five-phase BCAC; each phase boundary is an ATP; COTS/GOTS still needs independent gov't T&E; level-of-test determination; IOT&E = Level 3 |
| **Acquisition of Services** | (under review) | Noted in the source as under review; not a chapter in this pack |

---

## T&E Organizations — Who's Who

**OSD (by test type, not hierarchy):**
- **USD(R&E)** — DT&E and test infrastructure; approves the DT&E plan in the TEMP; MS B/C DT&E sufficiency assessments for MDAPs. Advisor: D(DTE&A). Infrastructure arm: **TRMC** (MRTFB, CTEIP, JMETC, NCRC, TENA, T&E/S&T).
- **DOT&E** — OT&E and LFT&E policy; approves strategies/plans on the oversight list; statutory reports to the Secretary of Defense and Congress; beyond-LRIP report gate.

**Each Service: an Executive (policy) + an OTA (independent judgment):**
- Army — Army T&E Executive + **ATEC**
- Navy/USMC — DON T&E Executive (OPNAV N94) + **OPTEVFOR** / **MCOTEA**
- Air Force/Space Force — AF/TE + **AFOTEC** / **STARCOM**
- IT & National Security Systems — **JITC** (the only non-Service OTA)

**Program level:** PM resources the program and charters the **T&E WIPT**; names a **CDT**, a Lead DT&E Organization, and a Lead OTA.

---

## T&E Strategy / TEMP — Minimum Content

- **IDSK** linking decisions to data requirements and sources (CT/DT/LFT/OT/M&S), correlated to critical operational issues and technical requirements
- Resources for all phases, including **M&S VV&A** where required
- DT&E, OT&E, LFT&E scope, objectives, and data
- Schedule carrying T&E events and reporting timelines
- Phase **entrance/exit criteria**, cybersecurity test objectives, M&S events
- Data-collection requirements (live events + M&S)
- Projected and actual **funding** with sources (DT&E/OT&E/LFT&E resource table per PL 115-91 §839(b))

It is a **stakeholder agreement** and a **living document** — write it early enough to inform the contract; keep it current.

---

## The Risk-Assessment Stack (MCA)

| Assessment | Who / when | What it judges |
|---|---|---|
| **ITRA** | USD(R&E) or component; MS A/B, LRIP, FRP entry | Independent technical risk + mitigations (report subsumes the TRA) |
| **TRA** | Critical-technology maturity on objective evidence | Technology readiness/risk |
| **DTSA** | USD(R&E); MS B (§4252), MS C (§4253) | Sufficiency of DT&E plans, schedule, resources, production entry |
| **DTA** | USD(R&E); MS B/C for DT-oversight programs | Technical performance, integration maturity, sustainment, survivability |

---

## Tells & Smells (warning signs)

- **T&E expectations not in the RFP/contract** → the data will not be delivered. Self-inflicted wound.
- **Treating "rapid" or "COTS/GOTS" as exempt from LFT&E** → no such exemption; only FUSL can be waived.
- **Reused data presented as a substitute for a dedicated DT&E/OT&E event** → reuse rescopes, never replaces.
- **IOT&E resting on modeling/simulation or document analysis alone** → fails the statute; IOT&E needs end-to-end realistic testing.
- **Compressing the integrated test schedule without characterizing the loss** → compression is allowed only with the residual-evidence risk made explicit.
- **Early OT involvement reduced to "observation" or "a seat at the table"** → that is symbolism, not the genuine team membership the OT principles require.
- **Milestone-only reporting in a fast program** → reports can be stale before publication; feedback must be continuous and cumulative.
- **A T&E Strategy frozen at one milestone** → it has already begun to drift; it is a living document.
- **Interoperability testing on production environments (DBS)** → risks real transactions / corrupting operational data; use interfacing systems' test environments.
- **A test event that maps to no decision in the IDSK** → candidate for cutting under the tailoring logic.

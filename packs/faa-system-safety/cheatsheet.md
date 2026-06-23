# FAA System Safety Handbook — Cheatsheet

## Quick Decision Rules

**"Where does a safety effort start?"**
With the plan — fix the risk-acceptability criteria up front, then identify hazards. Order 8040.4's
five steps: plan, identify, analyze, assess, decide.

**"Hazard or risk?"**
A *hazard* is a condition that could lead to an undesired event. *Risk* couples two things that
must both be characterized: severity of consequence and likelihood of occurrence.

**"How safe is safe enough?"**
There is no zero-risk goal — safety is balanced against cost, schedule, and performance. Some risk
must be accepted; the appropriate management authority decides how much and documents why.

**"Which control do I reach for first?"**
Descend the Safety Order of Precedence: design out → safety devices → warning devices →
procedures/training. Procedures for severe hazards normally need concurrence of authority.

**"Development or operations?"**
Engineered-in safety (PHA/SSHA/SHA/O&SHA) for the system being built; **ORM** for the system being
operated, run before the task (e.g., before each flight).

**"Which analysis technique?"**
By framing: *what could cause this accident?* → top-down (**FTA**, Fault Hazard Analysis); *if this
fails, what happens?* → bottom-up (**FMEA/FMECA**); *is the redundancy real?* → **CCFA**; *latent
wiring fault with nothing broken?* → **Sneak Circuit Analysis**; *where is the energy?* →
**Energy Trace**.

---

## The Five-Step Risk Management Process (Order 8040.4)

| Step | What it does |
|---|---|
| **Plan** | set the process and the risk-acceptability criteria in advance |
| **Identify** | surface the hazards |
| **Analyze** | characterize each by severity and likelihood |
| **Assess** | compare against the plan's criteria (the Comparative Safety Assessment) |
| **Decide** | management owns the residual-risk decision |

## Risk = Severity × Likelihood → Acceptance Band

- **Severity** (FAA AMS): Catastrophic → Hazardous → Major → Minor → No Safety Effect.
- **Likelihood** (FAA AMS): Probable → Remote → Extremely Remote → Extremely Improbable.
- Combine in the matrix → **High** (track until reduced) · **Medium** (acceptable with MA review) ·
  **Low** (acceptable, no further tracking). MIL-STD-882C renames the bands R1–R4.
- The more catastrophic the outcome, the lower its allowable probability. Fix severity first.

## System-Description Models

- **5M**: Mission · Man · Machine · Management · Media.
- **SHEL(L)**: Software · Hardware · Environment · Liveware. Interfaces matter as much as elements.

---

## The Hazard Analysis Activities (lifecycle order)

**PHL → PHA → RHA → SSHA → SHA → O&SHA → HHA**

| Activity | Purpose / timing |
|---|---|
| **PHL** | early hazard seed list, carried into the RFP/contract |
| **PHA** | foundational analysis; frames the rest; before preliminary design review |
| **RHA** | turns hazards + generic standards into design requirements; by allocated baseline |
| **SSHA** | how a component's operation/failure affects the whole |
| **SHA** | how the whole system + interfaces affect subsystem safety; integrates the SSHAs |
| **O&SHA** | procedurally controlled operation/support; usually completed last |
| **HHA** | hazardous materials and physical agents, with life-cycle-cost-aware controls |

SSHA/SHA typically submitted before Critical Design Review. A **proactive** program shapes the
design via the PHL before it starts; a **reactive** one justifies redesign after milestones.

## Analysis Techniques (Chapter 9)

| Technique | Direction | Use it for |
|---|---|---|
| **Fault Hazard Analysis** | deductive | safety-relevant subset of an FMEA |
| **Fault Tree Analysis (FTA)** | top-down | failure paths from one defined undesired event |
| **CCFA** | extends FTA | coupling factors in minimal cut sets — is redundancy real? |
| **Sneak Circuit Analysis** | topological | latent conditions with no component failure |
| **Energy Trace** | completeness | inventory controlled/uncontrolled energy; seed FTA top events |
| **FMECA** | bottom-up | FMEA + criticality figure of merit; hardware/software failures only |

Qualitative first; quantify only when value justifies cost and the limits of the numbers are stated.

---

## Acquisition Lifecycle Hooks (AMS / IPDS)

- **Pre-investment**: OSA (sets requirements — *not* a risk assessment) + CSA (ranks alternatives).
  ASOR allocates objective/requirement against a Target Level of Safety.
- **Post-investment**: the **SSPP** becomes the binding baseline (MIL-STD-882 Section 4 core is
  mandatory, non-tailorable); complex multi-contractor efforts escalate to an **ISSPP**.
- **Contract is the only enforceable interface**: define safety in the specification, SOW, CDRL, and
  bidders' instructions early, or it is not delivered. Tie deliverables to milestones, not dates.

## Specialty Domains

- **Software**: five-step process (JSSSC handbook + DO-178B); rank by *control capability* (882C
  categories / DO-178B levels) × severity in the SHCM; verify by test; 100% coverage rarely possible.
- **Test & Evaluation**: testing is both safety *evidence* and a *hazard* — analyze the test itself.
- **Facilities**: a facility is a subsystem; managed across the Facility Acquisition Life Cycle under
  FAA Order 3900.19 + MIL-STD-882; scaled to low/medium/high risk.
- **Commercial launch (AST)**: applicant proves acceptable public risk to earn a license; risk =
  **expected casualty**; MPL + DAMP set financial responsibility (probable, not possible, loss).
- **Operations (ORM)**: six steps (identify, assess, analyze, decide, implement, supervise/review);
  four principles; time-critical / deliberate / strategic; user ownership beats compliance.

---

## Tells & Smells

- **No stated acceptance criteria** → can't distinguish acceptable from unacceptable risk.
- **"Combine many techniques in one report"** → stapling, not integration; reason about interactions.
- **"Eliminate failures and it's safe"** → reliable ≠ safe; a working part can still injure.
- **"It conforms to the standard, so risk is acceptable"** → standards can be outdated or generic.
- **"It's redundant and monitored, so it's safe"** → independence may be unproven; common cause defeats all legs.
- **Probability alone controls risk** → a number says nothing about when or to whom a mishap occurs.
- **FMEA treated as a finished hazard analysis** → it misses human, procedural, and sequential hazards.
- **Hazards fixed by procedure, not design** → a sign they were caught too late.
- **Safety engineer working "in a vacuum"** → feed recommendations to designers as they surface.
- **NRTL listing or COTS provenance taken as proof of safety** → risk lives in the application; analyze it.
- **Control imposed without involving the people exposed** → the root cause of most control failures.
- **Judging a control by accident statistics** → too slow; measure behavior, conditions, attitudes, knowledge.
- **Vague learning objectives ("know", "understand")** → not observable or measurable; not objectives.

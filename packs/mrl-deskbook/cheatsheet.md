# MRL Deskbook Cheatsheet

## Quick Decision Rules

**"What MRL should this element be at right now?"**
Read the target off the milestone, not off a feeling:
- MSA / Milestone A → **MRL 4** (on each competing materiel solution)
- Milestone B / end of TMRR → **MRL 6**
- CDR (in EMD) → **MRL 7**
- LRIP / Milestone C → **MRL 8**
- Full-Rate Production → **MRL 9**
- Production & deployment, continuous improvement → **MRL 10**

**"Is the element mature enough to assign a number?"**
Don't assign a number — work the MRL Criteria Matrix. The output is the answer to two questions: (1) has the element met the appropriate maturity, and (2) if not, what remains. The number is a risk-focusing target, not a grade.

**"The element is below its target at a milestone — now what?"**
The PM has the same three courses of action every time: (1) delay the milestone decision for risk reduction; (2) switch to a lower-risk approach or alternative design; or (3) carry the risk forward with a funded Manufacturing Maturation Plan. The assessment informs the decision; it does not make it.

**"How do I report a whole system's maturity?"**
Report level-by-level, each MRL identified to its specific risks. Avoid collapsing to one number and avoid the weakest-link rollup — both mislead, worst for complex subsystems.

**"How do I make MRL maturity binding on a contractor?"**
Section L (what to submit) + Section M (how it's scored) at award; SOW "shall" statements after award. Task the work through AS6500A — the Criteria Matrix grades maturity but does not direct work.

**"Which OT cybersecurity standards apply?"**
Resolve two axes first: information sensitivity (classified → FAR 52.204-2; CTI → DFARS 252.204-7012) and operator status (Federal System → NIST SP 800-53; Non-Federal System → NIST SP 800-171).

---

## Manufacturing Readiness Levels (MRL 1–10)

| MRL | Maturity state | Typical life-cycle anchor |
|---|---|---|
| 1 | Basic manufacturing implications identified | Pre-systems acquisition / basic research |
| 2 | Manufacturing concepts identified | Applied / early research |
| 3 | Manufacturing proof of concept developed | Lab experiments, limited-function hardware |
| 4 | Capability to produce in a lab environment | MSA exit toward Milestone A |
| 5 | Capability to produce prototype components in a **production-relevant** environment | TMRR midpoint |
| 6 | Capability to produce a prototype system/subsystem in a production-relevant environment | Milestone B (enter EMD) |
| 7 | Capability to produce systems/subsystems in a **production-representative** environment | CDR (in EMD) |
| 8 | Pilot-line capability demonstrated; ready for LRIP | Milestone C / LRIP |
| 9 | LRIP demonstrated; ready for FRP | FRP decision |
| 10 | FRP demonstrated; lean practices, continuous improvement | Production & Deployment / O&S |

**Non-linear**: the effort to climb one level is not equal between levels. The number is shorthand for the worst-supported corner of the levels-by-threads grid.

---

## The Five Environments (escalating realism)

| Environment | What it proves |
|---|---|
| Laboratory | The process/idea works under controlled lab conditions (pre-Milestone A) |
| Production-relevant | Prototypes can be made outside the lab with some shop-floor realism (EMD targets) |
| Production-representative | Made with the personnel/equipment/processes/materials that will be on the pilot line |
| Pilot line | Production-configuration items built in LRIP using FRP processes where practical |
| Production line | Items made at required rate/quantity with processes under control |

"Production-relevant" is a stakeholder agreement for the application, not a fixed place — agree it before an MRL 6 assessment.

---

## The Nine MRL Threads

Technology & Industrial Base · Design · Cost & Funding · Materials · Process Capability & Control · Quality · Manufacturing Workforce · Facilities · Manufacturing Management. Each decomposes into sub-threads so maturity traces independently MRL 1→10.

---

## MRL vs TRL

| | MRL | TRL |
|---|---|---|
| Measures | Manufacturing maturity / production risk | Technology/performance maturity |
| Levels | 10 | 9 |
| Relationship | General, **not** one-to-one | — |

Best practice: **pace manufacturing maturity by technology maturity** ("move manufacturing left"). High TRL with ignored manufacturability, or high MRL on an unstable design, both raise programmatic risk.

---

## Pathway Targets at a Glance

| Pathway | Entry / key targets |
|---|---|
| MCA | MRL 4 (MSA) → 6 (MS B) → 7 (CDR) → 8 (LRIP/MS C) → 9 (FRP) |
| MTA Rapid Prototyping | Enter MRL 4 → 6 (MS B insert) → 8 (MS C / field) |
| MTA Rapid Fielding | Enter MRL 8; production within 6 months |
| UCA | MRL 7 (CoA) → 8 (Development Milestone) → 9 (production), under 2 years |
| Single/limited system | System-level MRL 8 at CDR (subsystems MRL 8–9) — First Build is effectively production |
| Ship (Navy 2-pass, 6-gate) | MRL 6 at SD1/PDR → 7 by MS B/CDR → 8 for PRR before keel-laying |

MRL Assessments are best practice for MCA, MTA, and UCA; generally **not required** for Business Systems or Defense Acquisition of Services.

---

## Tells & Smells (when something is wrong)

- **A single MRL quoted for a whole system** → maturity varies element-to-element; ask for the level-by-level picture.
- **An MRL used as a go/no-go gate** → it's a risk-identification tool, not a pass/fail verdict; the number doesn't decide.
- **A number assigned without the criteria behind it** → maturity comes from working the Criteria Matrix, not labeling the element.
- **MRL forced into a one-to-one map with TRL** → there is a general relationship but no fixed mapping.
- **A criterion tailored out without documentation** → that's a buried known-unknown; assess to the phase and write down anything you can't assess.
- **An assessment with no MMP for its gaps** → an unfinished thought; every shortfall needs a costed, scheduled, owned plan.
- **Maturity claims with no objective evidence** → conformance is demonstrated through artifacts and a cross-reference matrix, not assertions.
- **Reliance solely on the contractor's self-assessment** → use independent sources (e.g., DCMA) to read manufacturing strengths and weaknesses honestly.
- **OT cybersecurity treated as a deep audit** → the MRL criteria are a top-level screen for major gaps, not a compliance certification.
- **CMMC treated as the source of CUI requirements** → CMMC is the certification process; NIST SP 800-171 is the source.

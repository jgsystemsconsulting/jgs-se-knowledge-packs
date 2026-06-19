# NIST CSF 2.0 Cheatsheet

## Decision Rules

**Which component do I need?**
- Describing *what* outcomes to pursue → **CSF Core** (Functions/Categories/Subcategories)
- Documenting *where we are* vs *where we want to be* → **Organizational Profile** (Current + Target)
- Characterizing *how rigorously* we manage risk → **CSF Tiers** (1 Partial → 4 Adaptive)
- Finding *how to achieve* an outcome → **Informative References** + **Implementation Examples** (online)

**Which Function first?**
- Always start with **GOVERN** — it sets the strategy that makes all other Functions coherent.
- Run **IDENTIFY** before spending on **PROTECT** — you cannot safeguard what you have not inventoried and risk-classified.
- **DETECT** depends on **PROTECT** for its monitoring substrate (logs, baselines); deploy monitoring infrastructure first.
- **RESPOND** activates on incident declaration (DE.AE-08); the plan (ID.IM-04) must exist before the incident.
- **RECOVER** gates on **RESPOND** completion (RS.MA-05 criteria); verify backup integrity (RC.RP-03) before restoring.

**What Tier should we target?**
- Progress to a higher Tier only when: (a) risks or mandates are greater, OR (b) cost-benefit analysis justifies it.
- Tier 4 (Adaptive) is not a universal target — it requires real-time supply chain risk monitoring and cultural embedding.

**Current Profile vs Target Profile?**
- Current Profile = honest baseline; inflating it defeats gap analysis.
- Target Profile = outcomes prioritized by mission, risk appetite, and threat landscape — not "achieve everything."

---

## Function / Category Quick-Reference Table

| Function | Category | ID | What it covers |
|----------|----------|----|---------------|
| **GOVERN** | Organizational Context | GV.OC | Mission, stakeholders, legal/regulatory requirements |
| | Risk Management Strategy | GV.RM | Risk appetite, tolerance, ERM integration, standardized risk method |
| | Roles, Responsibilities, Authorities | GV.RR | Accountability, resources, HR integration |
| | Policy | GV.PO | Cybersecurity policy establishment, enforcement, review |
| | Oversight | GV.OV | Feedback loop: results → strategy adjustment |
| | Supply Chain Risk Mgmt | GV.SC | C-SCRM program, supplier prioritization, contracts, monitoring |
| **IDENTIFY** | Asset Management | ID.AM | Hardware, software, data, network flows, supplier services, life cycle |
| | Risk Assessment | ID.RA | Vulnerabilities, threats, likelihood/impact, risk response prioritization |
| | Improvement | ID.IM | Lessons from evals, exercises, operations, incident plan maintenance |
| **PROTECT** | Identity Mgmt, Auth, Access Control | PR.AA | Credential mgmt, identity proofing, auth, least privilege, physical access |
| | Awareness and Training | PR.AT | General and specialized-role cybersecurity training |
| | Data Security | PR.DS | Data at rest, in transit, in use; tested backups |
| | Platform Security | PR.PS | Config mgmt, software/hardware maintenance, logging, unauthorized software prevention, SSDLC |
| | Technology Infrastructure Resilience | PR.IR | Network protection, environmental threats, resilience mechanisms, capacity |
| **DETECT** | Continuous Monitoring | DE.CM | Networks, physical, personnel, external providers, computing environments |
| | Adverse Event Analysis | DE.AE | Correlation, impact/scope estimation, threat intel integration, incident declaration |
| **RESPOND** | Incident Management | RS.MA | Plan execution, triage, categorization, prioritization, escalation, recovery criteria |
| | Incident Analysis | RS.AN | Root cause, record integrity/provenance, magnitude validation |
| | Incident Reporting & Communication | RS.CO | Stakeholder notification, information sharing |
| | Incident Mitigation | RS.MI | Containment, eradication |
| **RECOVER** | Incident Recovery Plan Execution | RC.RP | Recovery actions, backup integrity verification, post-incident norms, restoration verification, recovery declaration |
| | Incident Recovery Communication | RC.CO | Stakeholder coordination, approved public messaging |

---

## Tells and Smells

**Smell: "We don't know what we have."**
→ Missing ID.AM asset inventories; start with hardware (ID.AM-01), software (ID.AM-02), and data (ID.AM-07) before any other investment.

**Smell: "Cybersecurity is the CISO's problem, not the board's."**
→ Missing GV.RR-01 leadership accountability and GV.OV oversight; the board owns risk posture, the CISO manages it.

**Smell: "We have controls but we don't know if they work."**
→ Missing ID.IM (improvement from evaluations/exercises) and GV.OV (oversight of performance); add regular testing and governance feedback loops.

**Smell: "Our incident response was chaos."**
→ Missing RS.MA structure (triage, categorization) and/or the incident response plan was not maintained (ID.IM-04); root cause was not established (RS.AN-03).

**Smell: "We restored from backup and the attackers were still in the system."**
→ Skipped RS.MI-02 (eradication) before RC.RP recovery, and/or skipped RC.RP-03 backup integrity verification; the gateway between RESPOND and RECOVER was not enforced.

**Smell: "We don't know what our suppliers are doing."**
→ Missing GV.SC supply chain risk management; supplier monitoring (GV.SC-07) and incident planning inclusion (GV.SC-08) are explicit outcomes, not optional.

**Smell: "Security alerts are ignored because there are too many."**
→ Missing DE.AE incident declaration criteria (DE.AE-08) and multi-source correlation (DE.AE-03); undefined thresholds create undifferentiated noise.

**Smell: "We comply with regulations but had a breach anyway."**
→ CSF outcomes are not compliance checkboxes; compliance demonstrates minimum posture, not risk management rigor; advance toward Repeatable (Tier 3) or Adaptive (Tier 4) governance.

# NIST AI RMF 1.0 Cheatsheet

## Decision Rules

**Starting a new AI system programme?**
→ GOVERN first. Establish policies, accountability, risk tolerance, and AI inventory before any system-specific work.

**Should we build or deploy this AI system?**
→ Complete MAP → MEASURE → record a formal go/no-go (MANAGE 1.1). If unacceptable risk is present, halt until manageable.

**Which risk to tackle first?**
→ Highest impact × highest likelihood = highest priority (MANAGE 1.2). Always start MEASURE with the most significant MAP-identified risks (MEASURE 1.1).

**We cannot measure a risk. What now?**
→ Document it explicitly (MEASURE 1.1). Silence is not acceptable. Use alternative tracking approaches (MEASURE 3.2).

**A deployed system is behaving inconsistently with intended use.**
→ Activate the pre-tested deactivation mechanism (MANAGE 2.4). Communicate the incident to affected communities (MANAGE 4.3).

**We found an unknown risk in production.**
→ Follow MANAGE 2.3: respond and recover from previously unknown risks. Feed findings back into MAP for re-contextualisation.

**We need to retire an AI system.**
→ Follow GOVERN 1.7: decommission safely; ensure the process does not increase risk or decrease organisational trustworthiness.

**We inherited a third-party AI model or dataset.**
→ Apply MAP 4, GOVERN 6.2, and MANAGE 3.1–3.2. You own the risk even if you did not build the component.

---

## Function Quick-Reference Table

| Function | Core question | When it runs | Key output |
|---|---|---|---|
| **GOVERN** | Do we have the right policies, culture, and accountability? | Continuously; before and throughout all other functions | Policies, roles, risk tolerance, training programmes, AI inventory |
| **MAP** | What is this system, for whom, in what context, with what risks? | At system initiation; re-applied when context changes | Context documentation, system categorisation, impact characterisation, go/no-go basis |
| **MEASURE** | How do we know the system is trustworthy and within risk tolerance? | Pre-deployment and continuously in operation | TEVV results, trustworthiness metrics, risk tracking, measurement documentation |
| **MANAGE** | What do we do about the risks we have found? | After MAP/MEASURE outputs; continuously in operation | Risk response plans, residual risk disclosures, monitoring plans, incident communications |

---

## GOVERN Categories at a Glance

| Category | Focus |
|---|---|
| GOVERN 1 | Policies, procedures, risk tolerance, AI system inventory, decommissioning |
| GOVERN 2 | Accountability structures, training, executive responsibility |
| GOVERN 3 | Workforce diversity, equity, inclusion, human-AI configuration roles |
| GOVERN 4 | Risk culture: critical thinking, safety-first, incident information sharing |
| GOVERN 5 | External stakeholder feedback collection and integration |
| GOVERN 6 | Third-party and supply chain risk policies |

---

## Seven Trustworthiness Characteristics (Fig. 4 Order)

| Characteristic | Foundation role | Primary MEASURE subcategory |
|---|---|---|
| Valid & Reliable | BASE — necessary condition for all others | MEASURE 2.5 |
| Safe | Physical / environmental protection | MEASURE 2.6 |
| Secure & Resilient | Confidentiality, integrity, availability; graceful degradation | MEASURE 2.7 |
| Accountable & Transparent | Cross-cutting vertical — spans all characteristics | MEASURE 2.8 |
| Explainable & Interpretable | How decisions are made and what they mean | MEASURE 2.9 |
| Privacy-Enhanced | Human autonomy, identity, dignity | MEASURE 2.10 |
| Fair / Bias Managed | Equality, equity, three bias categories | MEASURE 2.11 |

---

## Tells and Smells

**Smell: No AI system inventory** → GOVERN 1.6 gap; cannot manage what you have not catalogued.

**Smell: Risk measurement done only by the builders** → MEASURE 1.3 gap; conflicts of interest undermine validity; bring in independent or internal non-developer assessors.

**Smell: MAP skipped, jumped straight to model building** → Context-free risk management; trustworthiness characteristics cannot be evaluated without knowing the deployment setting and stakeholder population.

**Smell: Risk response not documented** → MANAGE 1.3 gap; implicit acceptance is not acceptance; creates no accountability and cannot be re-evaluated.

**Smell: "We'll add oversight later"** → MAP 3.5 and MANAGE 2.4 require human oversight processes and a deactivation mechanism to be designed before deployment, not retrofitted.

**Smell: Third-party model treated as zero-risk** → GOVERN 6, MAP 4, MANAGE 3 all require explicit management of third-party AI risks; provider assurances do not substitute for your organisation's own controls.

**Smell: Post-deployment monitoring described as a dashboard** → MANAGE 4.1 requires appeal, override, decommissioning, incident response, and change management — not just metric display.

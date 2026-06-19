# EU AI Act Cheatsheet

**Source**: Regulation (EU) 2024/1689 | Quick-reference for classification, obligations, timelines, and penalties.

---

## Application Timeline

| Date | What applies |
|------|-------------|
| 2 February 2025 | Ch I (definitions/scope) + Ch II (prohibited practices, Art 5) |
| 2 August 2025 | Ch III Sec 4 (notified bodies), Ch V (GPAI), Ch VII (governance), Ch XII (penalties except Art 101) |
| 2 August 2026 | Full Act applies (main application date) |
| 2 August 2027 | Art 6(1) Route A (product safety AI components) + large-scale IT system AI brought into compliance |
| 31 December 2030 | Large-scale IT system AI components fully compliant |

---

## AI System Classification Decision Tree

```
Is the AI system a prohibited practice (Art 5)?
  YES → STOP. Prohibited. No compliance pathway.
  NO  ↓

Route A: Is it a safety component of an Annex I product, and that product requires third-party
         conformity assessment under sector law?
  YES → HIGH-RISK (Art 6(1))
  NO  ↓

Route B: Does the system fall under one of the 8 Annex III use-case areas?
  NO  → Not high-risk under Ch III
  YES ↓

Does the de minimis carve-out apply (Art 6(3))?
  (a) narrow procedural task, OR
  (b) improves prior human activity result, OR
  (c) detects patterns without replacing human assessment, OR
  (d) preparatory task for an Annex III assessment
  AND the system does NOT perform profiling of natural persons
  YES → NOT HIGH-RISK (but document and register, Art 6(4))
  NO  → HIGH-RISK (Art 6(2))

Also check Art 50 transparency obligations for ANY AI system (regardless of high-risk status).
Also check Chapter V for GPAI models (regardless of high-risk status).
```

---

## Annex III High-Risk Areas — Quick Reference

| Area | Key examples |
|------|-------------|
| 1. Biometrics | Remote biometric ID, biometric categorisation (sensitive attributes), emotion recognition |
| 2. Critical infrastructure | Safety components in digital infra, road traffic, utilities |
| 3. Education | Admissions, learning evaluation, level assessment, exam proctoring |
| 4. Employment | Recruitment/selection, performance monitoring, promotion, termination, task allocation |
| 5. Essential services | Creditworthiness, insurance pricing, public benefits eligibility, emergency dispatch |
| 6. Law enforcement | Victim/crime risk assessment, evidence reliability, recidivism prediction, profiling |
| 7. Migration/asylum/border | Risk assessment, asylum examination, border detection/identification |
| 8. Justice/democracy | Judicial decision support, election/referendum influence |

---

## Penalty Tiers

| Tier | Violation | Fine maximum |
|------|-----------|-------------|
| 1 | Art 5 (prohibited practices) | EUR 35M or 7% of global annual turnover (higher) |
| 2 | Art 16, 22-24, 26 (operator obligations); Art 50 (transparency) | EUR 15M or 3% of global annual turnover (higher) |
| 3 | Misleading information to authorities or notified bodies | EUR 7.5M or 1% of global annual turnover (higher) |
| GPAI | Ch V violations (Commission-imposed, Art 101) | EUR 15M or 3% of global annual turnover (higher) |
| SME cap | All tiers — SMEs pay lower of % or absolute | Applies automatically |
| Union institutions | Prohibited practices (EDPS-imposed) | EUR 1.5M |
| Union institutions | Other violations | EUR 750,000 |

---

## High-Risk AI System Requirement Checklist (Art 8-15)

| Requirement | Article | Key obligation |
|-------------|---------|----------------|
| Risk Management System | 9 | Continuous iterative lifecycle process; 4 steps; acceptable residual risk |
| Data Governance | 10 | Quality criteria; bias examination and mitigation; special-category conditions |
| Technical Documentation | 11 | Draw up before placement; Annex IV content; keep up to date |
| Record-keeping / Logging | 12 | Automatic event logging built in; min. content for biometric ID systems |
| Transparency to deployers | 13 | Instructions for use covering 7 content categories |
| Human oversight | 14 | Oversight measures; automation bias awareness; stop button; 2-person verification for biometric ID |
| Accuracy/robustness/cybersecurity | 15 | Declared metrics; resilience; feedback-loop mitigation; AI-specific attack defence |

---

## Operator Obligations at a Glance

| Party | Core obligations |
|-------|-----------------|
| Provider | QMS, technical docs, conformity assessment, DoC, CE marking, EU database registration, log retention (10 yr), corrective actions, authority cooperation |
| Deployer | Follow instructions, assign human oversight, log retention (≥6 months), worker notification, FRIA (public bodies), EU database check (public bodies), inform affected persons |
| Importer | Verify conformity before placement, retain docs 10 yr, cooperate with authorities |
| Distributor | Verify CE marking and DoC before making available, cooperate with authorities |
| Authorised representative | Verify docs, retain copies 10 yr, cooperate with authorities, can terminate mandate if provider violates Act |
| Becomes provider if... | Affixes own name/trademark; makes substantial modification; changes purpose to create high-risk |

---

## GPAI Obligations Summary

| Obligation | All GPAI providers | Systemic-risk GPAI only |
|-----------|-------------------|------------------------|
| Technical documentation (Annex XI) | Yes (open-source exempt*) | Yes |
| Downstream provider information (Annex XII) | Yes (open-source exempt*) | Yes |
| Copyright compliance policy | Yes | Yes |
| Training data summary (public) | Yes | Yes |
| Adversarial testing (red-teaming) | No | Yes |
| Systemic risk assessment and mitigation | No | Yes |
| Serious incident reporting to AI Office | No | Yes |
| Cybersecurity of model and infrastructure | No | Yes |

*Open-source exception lost if model has systemic risk.
Systemic risk presumed if training compute > 10^25 FLOPs (Art 51(2)).

---

## Art 50 Transparency Obligation Quick Matrix

| Situation | Who acts | Obligation |
|-----------|---------|------------|
| AI system interacts with natural persons | Provider (design); Deployer (deploy) | Disclose AI interaction (unless obvious) |
| AI generates synthetic audio/image/video/text | Provider | Machine-readable labelling as AI-generated |
| Emotion recognition or biometric categorisation system | Deployer | Inform persons exposed |
| Deep fake deployment | Deployer | Disclose artificial generation |
| AI text on public-interest matters | Deployer | Disclose AI generation (unless editorial control + responsibility) |

---

## Serious Incident Reporting Timelines (Art 73)

| Severity | Reporter | Timeframe |
|----------|---------|-----------|
| Death / serious health harm (causal link) | Provider | Immediately |
| Immediate risk of death or serious health harm | Provider | Within 2 working days |
| All other serious incidents | Provider | Within 15 days |
| Deployer to provider notification | Deployer | Without undue delay |
| Deployer direct to authority (if provider unreachable) | Deployer | Without undue delay |

---

## Governance Architecture

| Body | Level | Role |
|------|-------|------|
| AI Office | Union (within Commission) | GPAI enforcement; Union-level expertise; guideline and code facilitation |
| European AI Board | Union (Member State representatives) | Coordination, advice, harmonisation, Board opinions |
| Advisory Forum | Union (stakeholders) | Technical expertise, stakeholder input to Board and Commission |
| Scientific Panel | Union (independent experts) | GPAI risk assessment, qualified alerts, benchmark development |
| National notifying authority | Member State | Notified body assessment and designation |
| National market surveillance authority | Member State | Post-market AI system enforcement (all chapters except GPAI) |

---

## Key Definition Tells

- **AI system vs GPAI model**: AI system = specific deployment; GPAI model = underlying foundation model usable across many deployments. A GPAI model integrated into a product = GPAI model obligations (Ch V) + downstream AI system obligations (Ch III if high-risk).
- **Provider vs deployer**: Provider = brings to market under own name. Deployer = uses under their authority. A party can be both for different systems.
- **Real-time vs post-remote RBIS**: Real-time = capture, compare, identify simultaneously (banned in public spaces except 3 objectives). Post-remote = significant delay (regulated, not banned, but requires judicial authorisation for criminal investigations).
- **Substantial modification**: Changes the conformity assessment scope OR changes the intended purpose → restarts the provider liability chain.

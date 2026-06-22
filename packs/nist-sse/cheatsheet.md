# NIST SP 800-160 (SSE) Cheatsheet

## Quick Decision Rules

**"Where do I start a security effort?"**
The **problem context** — assets, losses, adversity, protection needs, requirements. Never controls-first.

**"Is this claim of 'secure' real?"**
Demand the **assurance case**: claim → argument → evidence. No case = assertion, not assurance.

**"How secure is secure enough?"**
**Adequately secure** — evidence-justified, stakeholder-relative, with accepted residual risk. Absolute security can't be proven (security is asymmetric).

**"Prevention or resiliency?"**
Both. Prevention keeps the adversary out; **cyber resiliency assumes breach** and keeps the mission going. Use Vol 2 when the mission must survive a capable APT.

**"Which resiliency technique?"**
By effect needed: **detect** → Analytic Monitoring / Contextual Awareness / Substantiated Integrity · **contain** → Segmentation / Privilege Restriction / Non-Persistence / Realignment · **survive/recover** → Redundancy / Diversity / Dynamic Positioning / Adaptive Response / Coordinated Protection · **confuse** → Deception / Unpredictability.

---

## Vol 1 — The SSE Framework (3 contexts)

| Context | Question | Produces |
|---|---|---|
| **Problem** | What to protect, from what, why? | protection needs, adversity, security requirements |
| **Solution** | How is protection achieved? | security architecture, design, element security, trade-offs |
| **Trustworthiness** | Why believe it? | assurance, the assurance case |

Interacting + iterative, over a common base of security analyses. Apply recursively at every level.

## Vol 1 — Design Principles for Trustworthy Secure Design (selection)

Clear Abstractions · **Reduced Complexity** · Least Privilege · Least Functionality · Least Persistence · Least Sharing · **Minimal Trusted Elements** · Defense in Depth · Domain Separation · Hierarchical Protection · Mediated Access · Protective Defaults · Protective Failure · Protective Recovery · Distributed Privilege · Diversity · Redundancy · Anomaly Detection · Minimize Detectability · Loss Margins · Substantiated Trust.

**Two groups:** security architecture/design (structure) + security capability/trust (protection & basis for trust).

## Vol 1 — Trustworthiness vs. Assurance

- **Trustworthiness** = worthy of trust (the goal) · **Assurance** = justified confidence (the evidence) · **Assurance case** = claim→argument→evidence (the artifact).
- Plan assurance from the claims; scale rigor to consequence (up to formal verification).

## Vol 1 — Security across the 15288 process groups

Technical · Technical Management · Organizational Project-Enabling · Agreement (supply chain).
*(Named + security-augmented here; the 15288 process text is third-party copyrighted, not reproduced — see `se-standards-signpost`.)*

---

## Vol 2 — Cyber-Resiliency Framework hierarchy

**Goals → Objectives → Techniques → Implementation Approaches → Design Principles**

| 4 Goals | Meaning |
|---|---|
| **Anticipate** | informed preparedness for adversity |
| **Withstand** | continue essential functions despite adversity |
| **Recover** | restore functions during/after adversity |
| **Adapt** | change in response to predicted/actual change |

Objectives (assessable): Prevent/Avoid · Prepare · Continue · Constrain · Reconstitute · Understand · Transform · Re-Architect.

## Vol 2 — The 14 Techniques (by defensive role)

- **Detect**: Analytic Monitoring · Contextual Awareness · Substantiated Integrity
- **Contain/limit**: Segmentation · Privilege Restriction · Non-Persistence · Realignment
- **Survive/recover**: Redundancy · Diversity · Dynamic Positioning · Adaptive Response · Coordinated Protection
- **Confuse the adversary**: Deception · Unpredictability

Coordinated Protection binds the rest into defense in depth. Deception + Unpredictability target the adversary's decisions.

## Vol 2 — Design principles & application

- **Strategic** principles = posture/trade-offs (assume breach, expect adaptation, raise adversary cost, reduce attack surface).
- **Structural** principles = architecture placement (constrain/verify trust, contain spread, enable detection, support graceful degradation/recovery, add diversity/unpredictability).
- **Apply** by tailoring to critical functions + the **APT** + architecture + constraints; integrate with **RMF (SP 800-37)** and **SP 800-53**.

---

## Tells & Smells

- **Controls-first** with no problem context → solving an unstated problem.
- **"It's secure"** with no assurance case → assertion, not assurance.
- **Absolute-security goal** → security is asymmetric; aim for *adequately* secure.
- **Sprawling trusted computing base** → violates minimal trusted elements; everything must be verified.
- **Fail-open defaults** → violates protective defaults/failure.
- **Prevention-only** for an APT-facing mission → no operate-through-compromise plan.
- **Backups/replicas an APT can corrupt** → pair Redundancy with Substantiated Integrity.
- **All 14 techniques regardless of adversary** → cost without focus; tailor to mission risk.
- **Static resiliency posture** → the APT adapts; use Adapt goal + Realignment/Unpredictability.
- **Resiliency outside the RMF** → can't be prioritized, assessed, or sustained.

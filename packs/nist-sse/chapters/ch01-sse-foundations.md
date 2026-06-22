# Chapter 1: Systems Security Engineering Foundations (Vol 1)

## Core Idea
Systems security engineering (SSE) is a specialty engineering discipline that applies scientific, engineering, and assurance principles to deliver systems that are **trustworthy** and **adequately secure** for their stakeholders — engineering security *into* the whole system across its life cycle, within cost, schedule, and risk constraints, rather than bolting it on.

## Frameworks Introduced
- **SSE as a specialty within systems engineering** — security is engineered through the same life-cycle processes used for the rest of the system, not as a separate late-phase activity.
  - When to use: from the earliest concept work; SSE activities apply at every layer (mechanism, component, element, system, system of systems, enterprise).
- **Adequately secure** — the engineering goal is *adequate* security, justified by evidence and traceable to stakeholder protection needs, because absolute security cannot be proven.
  - When to use: when scoping security objectives and accepting residual risk.

## Key Concepts
- **System**: an arrangement of parts/elements that exhibits behavior or meaning the individual constituents do not — security is a property of the *whole*, including its interactions and environment.
- **Security (in SSE terms)**: freedom from conditions that can cause unacceptable asset loss and the associated consequences; deliberately broad, because "now that everything's acquiring connectivity," security touches every property of the system.
- **Adversity**: conditions that can cause asset loss — threats, attacks, vulnerabilities, hazards, disruptions, exposures. SSE engineers against adversity, not just against "attackers."
- **Asymmetry of security**: you can *observe* a system to be insecure, but no finite observation lets you declare it arbitrarily secure. This is why SSE produces *assurance* (justified confidence) rather than proofs of absolute security, and why "adequately secure" is the honest goal.
- **Trustworthiness as the aim**: the system must be *worthy of trust* to meet its security (and other) expectations — a claim that must be substantiated with evidence (Ch 4).
- **Audience**: systems engineers, security engineers, architects, and the program/risk roles who must make risk-informed decisions about protection.
- **Relationship to risk management**: SSE supplies the engineering substance that risk frameworks (RMF / SP 800-37, controls / SP 800-53) govern and assess; SSE decides *how* protection is built, risk management decides *how much* and *whether to accept*.

## Mental Models
- Engineer security in, don't bolt it on: the cheapest, most effective security decisions are made in concept and architecture, where the trusted computing base and trust relationships are still malleable.
- "Adequately secure" is a stakeholder-relative, evidence-backed judgment — not a checklist score and not "100% secure."
- Because security is asymmetric, every security claim needs a *reason to believe it* (assurance), or it is just an assertion.
- Security is a whole-system property: a perfectly secure component in an insecure composition is not secure.

## Anti-patterns
- **Bolt-on security**: adding controls after the architecture is fixed, when the expensive trust decisions are already made.
- **Absolute-security thinking**: chasing "fully secure" instead of *adequately* secure with evidence and accepted residual risk.
- **Component-only focus**: securing parts while ignoring interactions, interfaces, enabling systems, and the operational environment.
- **Assertion without assurance**: claiming the system is secure with no substantiating evidence.

## Key Takeaways
1. SSE engineers **trustworthy, adequately secure** systems through the system life cycle — security as a whole-system property.
2. The goal is **adequately secure** (evidence-justified, stakeholder-relative), because absolute security can't be proven — security is **asymmetric**.
3. SSE engineers against **adversity** broadly (threats, hazards, disruptions, exposures), not just attackers.
4. SSE supplies the engineering; **risk management** (RMF/SP 800-53) governs how much and whether to accept.
5. **Trustworthiness** must be *claimed and substantiated*, never assumed (Ch 4).

## Connects To
- **ch02 (SSE Framework)**: the three contexts that structure all SSE activity.
- **ch04 (Trustworthiness & Assurance)**: how "adequately secure" is evidenced.
- **`nist-csf` / RMF (SP 800-37) / SP 800-53**: the risk and control frameworks SSE feeds.
- **`nasa-npr-7123` / `dau-se-guidebook`**: the open SE process models SSE augments with security.
- **Vol 2 (ch05–ch08)**: cyber resiliency, the specialty SSE approach for surviving the APT.

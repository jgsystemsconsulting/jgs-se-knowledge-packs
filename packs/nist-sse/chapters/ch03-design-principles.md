# Chapter 3: Design Principles for Trustworthy Secure Design (Vol 1)

## Core Idea
Vol 1 provides a catalog of **30+ design principles for trustworthy secure design** — time-tested rules for structuring a system so it is more secure and more *analyzable*. They are applied in the solution context (Ch 2) and split broadly into principles for **security architecture & design** (how to structure the system) and principles for **security capability & trust** (what protection and assurance to provide).

## Frameworks Introduced
- **The design-principle catalog** — a named set of principles to apply and to check designs against.
  - When to use: throughout architecture and design; as a review checklist for any security-relevant decision.
- **Architecture/design vs. capability/trust split** — the principles fall into two broad groups: those that shape system structure, and those that determine protection capability and the basis for trust.
  - When to use: to ensure both structural soundness *and* sufficient, evidenced protection.

## Key Concepts — representative principles
- **Clear Abstractions**: clean, well-defined interfaces and behaviors; no needless complexity or hidden function.
- **Reduced Complexity**: the simpler the system, the smaller the attack surface and the more analyzable it is — complexity is the enemy of assurance.
- **Least Privilege / Least Functionality / Least Persistence / Least Sharing**: grant only the privileges, functions, lifetime, and shared resources actually required — each "least" shrinks what can go wrong.
- **Minimal Trusted Elements**: minimize the trusted computing base; the less the system must trust, the less must be verified and the smaller the consequence of misplaced trust.
- **Defense in Depth**: layered, diverse protections so no single failure or bypass is catastrophic.
- **Domain Separation / Hierarchical Protection**: isolate protection domains and order them so more-trusted elements are protected from less-trusted ones.
- **Mediated Access**: every access to a protected resource is checked — no bypass paths.
- **Protective Defaults / Protective Failure / Protective Recovery**: default to the secure state, fail securely (deny rather than expose), and recover to a secure state after disruption.
- **Distributed Privilege**: require cooperation of multiple elements/actors for sensitive actions, so no single compromise suffices.
- **Diversity / Redundancy**: vary and duplicate so a single flaw or failure does not bring down protection.
- **Anomaly Detection / Minimize Detectability**: be able to see adversary activity, while denying the adversary visibility into the system's protections.
- **Loss Margins / Substantiated Trust**: engineer margin against loss, and trust elements only to the degree their trustworthiness is *evidenced*.

## Mental Models
- Principles are *design constraints with a why*: each one reduces a class of risk. Applying a principle is cheap in design and expensive to retrofit.
- The "least" family is one idea repeated across dimensions — privilege, functionality, persistence, sharing, trusted elements: minimize each, and the blast radius of any compromise shrinks.
- Reduced complexity and minimal trusted elements are force multipliers for assurance (Ch 4): you can only substantiate trust in what you can analyze.
- Principles can tension each other (e.g. redundancy vs. reduced complexity); resolving the tension is the engineering judgment, made and recorded in the solution context.

## Anti-patterns
- **Principle-free design**: making security architecture decisions with no reference to the catalog, then discovering structural weaknesses late.
- **Maximal trust / sprawling TCB**: trusting many elements broadly, so everything must be verified and any compromise is severe.
- **Complexity creep**: accreting functions and privileges "just in case", enlarging the attack surface and defeating analyzability.
- **Fail-open defaults**: systems that on error or default expose resources rather than deny them.

## Key Takeaways
1. Vol 1 catalogs **30+ design principles** for trustworthy secure design, applied in the solution context.
2. They split into **architecture/design** principles (structure) and **capability/trust** principles (protection + basis for trust).
3. The **"least" family** (privilege/functionality/persistence/sharing) and **minimal trusted elements** shrink the blast radius and the verification burden.
4. **Reduced complexity** is foundational — you can only assure what you can analyze.
5. **Protective defaults/failure/recovery** keep the system safe at its defaults, on error, and after disruption.
6. Principles can **tension** each other; resolving the trade-off is recorded engineering judgment.

## Connects To
- **ch02 (SSE Framework)**: principles are applied within the solution context.
- **ch04 (Trustworthiness & Assurance)**: reduced complexity / minimal trusted elements make assurance feasible.
- **ch07 (Cyber-Resiliency Design Principles)**: Vol 2's strategic/structural principles complement these for the APT case.
- **`mil-std-882` / `nasa-system-safety`**: analogous "design it in" discipline for safety.

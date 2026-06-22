# Chapter 6: Cyber-Resiliency Techniques & Approaches (Vol 2)

## Core Idea
Vol 2 defines **14 cyber-resiliency techniques** — categories of capability that achieve the resiliency objectives — each realized through specific **implementation approaches**. Techniques are selected and combined against the adversary; some defend by detecting adversity, some by limiting its spread, some by confusing or denying the adversary, and some by keeping essential function alive through it.

## Frameworks Introduced
- **The 14 techniques** — the menu of resiliency capability categories.
  - When to use: when translating objectives (Ch 5) into concrete capability; pick the techniques whose effect matches the threat and mission.
- **Implementation approaches** — specific methods within each technique.
  - When to use: when designing the actual mechanism; one technique offers several approaches with different cost/effect.

## Key Concepts — the 14 techniques
- **Adaptive Response** — implement agile, timely courses of action to respond to adversity (contain, eject, restore).
- **Analytic Monitoring** — monitor and analyze a wide range of properties and behaviors continuously to detect adversity and its effects.
- **Contextual Awareness** — construct and maintain an understanding of mission dependencies and the status of resources relative to threat activity.
- **Coordinated Protection** — ensure protection mechanisms operate in a coordinated, defense-in-depth manner so the adversary must overcome multiple, diverse safeguards.
- **Deception** — mislead, confuse, or hide critical assets from the adversary (e.g. disinformation, decoys, obfuscation).
- **Diversity** — use heterogeneity to minimize common-mode failures and force the adversary to attack many different things.
- **Dynamic Positioning** — distribute and relocate functionality or assets to complicate targeting and to recover quickly (e.g. functional relocation, asset mobility).
- **Non-Persistence** — generate and retain resources only as needed and for limited time, reducing the adversary's foothold and exposure window.
- **Privilege Restriction** — restrict privileges based on attributes of users and elements and on environmental factors (dynamic privileges, attribute-based usage restriction).
- **Realignment** — align cyber resources with mission/business needs and reduce the attack surface by removing non-essential function (and reducing dependence on unreliable elements).
- **Redundancy** — provide multiple protected instances of critical resources (protected backup/restore, surplus capacity, replication).
- **Segmentation** — define and separate elements based on criticality and trust (predefined and dynamic segmentation/isolation) to contain adversity.
- **Substantiated Integrity** — ascertain whether critical elements have been corrupted (integrity checks, provenance, behavior validation).
- **Unpredictability** — make changes randomly or unpredictably so the adversary cannot anticipate or plan around defenses.
- **Defensive roles**: techniques cluster by purpose — *detect* (Analytic Monitoring, Contextual Awareness, Substantiated Integrity), *contain/limit* (Segmentation, Privilege Restriction, Non-Persistence, Realignment), *survive/recover* (Redundancy, Diversity, Dynamic Positioning, Adaptive Response, Coordinated Protection), and *confuse the adversary* (Deception, Unpredictability).
- **Selection against the adversary**: most techniques focus on cyber resources; Deception and Unpredictability are notable in that they specifically target the *adversary's* decision-making.

## Mental Models
- Pick techniques by the effect you need against this adversary: to *see* them → monitoring/awareness/integrity; to *limit* them → segmentation/privilege/non-persistence; to *keep going* → redundancy/diversity/positioning; to *waste their effort* → deception/unpredictability.
- Techniques compose and reinforce: Coordinated Protection is the meta-technique that makes the others work together as defense in depth.
- Each technique has a cost and a potential adversary counter; the implementation *approach* is where you tune cost vs. effect.
- Resilience must survive the adversary: a Redundancy approach an APT can corrupt (e.g. unprotected backups) is not resilient — pair with Substantiated Integrity.

## Anti-patterns
- **Single-technique reliance**: betting on one technique (e.g. redundancy alone) with no detection or containment.
- **Corruptible resilience**: backups/replicas/monitoring the adversary can tamper with — no Substantiated Integrity.
- **Technique without approach discipline**: naming "we use diversity" with no concrete, costed implementation approach.
- **Ignoring the adversary-facing techniques**: never using Deception/Unpredictability, ceding all initiative to the attacker.

## Key Takeaways
1. Vol 2 defines **14 techniques**, each realized via specific **implementation approaches**.
2. They cluster by role: **detect, contain/limit, survive/recover, confuse the adversary**.
3. **Coordinated Protection** binds the others into defense in depth.
4. **Deception and Unpredictability** uniquely target the adversary's decision-making.
5. Resilience must **survive tampering** — pair recovery techniques with **Substantiated Integrity**.
6. Choose techniques and approaches by **effect needed vs. cost vs. adversary counter**, not by completeness.

## Connects To
- **ch05 (Framework)**: techniques achieve the objectives that serve the four goals.
- **ch07 (Design Principles)**: principles guide which techniques to select and where to place them.
- **ch08 (Applying & Risk)**: techniques are selected against the APT and tailored to mission risk.
- **`nist-csf` (Detect/Respond/Recover)** and **SP 800-53**: control families that implement many of these techniques.

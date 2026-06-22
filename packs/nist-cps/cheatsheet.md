# NIST CPS Framework Cheatsheet

## Quick Decision Rules

**"Where do I start analyzing a CPS?"**
On the **aspect × facet grid**: nine aspects examined through three facets. Tailor it down first (process, depth, scope, domains, which activities/aspects to keep) — tailoring is an explicit, recorded decision.

**"Device or system?"**
Wrong question. Ask *from whose perspective?* The same artifact is a device, a system, or a system-of-systems depending on where you stand. The irreducible core is a **decision flow + at least one physical flow** (information or action).

**"How do I handle security in a CPS?"**
**Cross-property risk management** — reason about safety, security, privacy, reliability, and resilience *together*, never as five silos. Push each protection onto the element type (physical/analog/cyber) best able to enforce it.

**"Reliability or resilience?"**
Reliability handles **risk** (known outcome distribution, fault tolerance). Resilience handles **uncertainty** (unknown distribution, threat tolerance). Most security/privacy challenges live in resilience.

**"Which timing class?"**
Use the **weakest TI** that meets the need: **Bounded** (deadline only) → **Deterministic** (precise on local clock) → **Accurate** (internationally traceable). Over-specifying wastes hardware.

**"Is the time trustworthy?"**
Treat time as a measured, attackable supply chain. Distinguish **denial** (degrade safely) from **spoofing** (confident wrong time — the dangerous case). Detect → alarm → fail over to a trusted backup.

---

## The Framework — Aspects × Facets

**Three facets (engineering views, run as modes not phases):**

| Facet | Question | Produces |
|---|---|---|
| **Conceptualization** | What should it be/do? | the CPS model (a tree of traceable *properties*) |
| **Realization** | How is it made and run? | the built/deployed instance, designs, tests, trade-offs |
| **Assurance** | How confident, and why? | the assurance case (claims, evidence, argumentation, confidence) |

**Nine aspects (groupings of concerns):** functional · business · human · trustworthiness · timing · data · boundaries · composition · lifecycle.

Concerns are **not orthogonal** — applying several together forces trade-offs, formalized as **composition of concerns** = set union of required properties.

---

## Trustworthiness — Five Top-Level Properties

| Property | Roughly measures |
|---|---|
| **Cybersecurity** | operational & reputational risk |
| **Safety** | error rates |
| **Reliability** | failure rates |
| **Privacy** | unwanted-disclosure rates |
| **Resilience** | recovery rates |

One holistic process, one shared **risk budget** (a common resource, allocated by consequence — not split equally). Expect the **cyber** components to consume the largest share. *Stuxnet*: a cyber payload defeated all five engineered-in-isolation provisions; a physical over-speed interlock would have stopped it.

---

## Data Interoperability — The Three-Rung Ladder

**syntactical** (move bytes intact) → **semantic** (agree on meaning) → **contextual** (agree on rules of use). Physical connectivity sits below the bottom rung.

- **Canonical model + adaptors** cut transformations from ~n(n−1) toward n.
- **Archival vs. real-time** data — real-time data can expire in transit.
- **Identifiers** must be unique, persistent, resolvable; keep changeable attributes out of the name.
- Security = **confidentiality / integrity / availability**, with **availability** prioritized in control systems. Trust chains all the way down to actuation.

---

## Timing — TI Classes & Architecture

| TI class | Holds | Use when |
|---|---|---|
| **Bounded** | under a stated max | only a deadline matters |
| **Deterministic** | within error of a target, local timescale | a precise *relationship* must repeat |
| **Accurate** | deterministic + traceable to UTC/TAI | spatial scale or regulation forces it |

- **Frequency · phase · time** are distinct; phase and time need signal transport + delay compensation, so position and time are coupled.
- **Time domain** runs a continuous primary timescale; prefer **holdover** over discontinuity through a brief source loss.
- The **CNM** computes schedules + reserves bandwidth so time-sensitive and best-effort traffic converge on one network.
- Modern CPUs/OSes are **not time-aware**; explicit time lives in FPGAs/ASICs, time-aware PHYs, and time-triggered architectures. Aim for **time-correctness by design**.

---

## Securing Time — Threats & Defenses

- **Source attacks**: GNSS jamming (denial) and spoofing (counterfeit signal). NMA (signed nav data) is the affordable baseline.
- **Network attacks** (PTP/NTP): packet-delay manipulation, rogue master, replay/spoofing, DoS, crypto-performance exhaustion.
- **Defenses**: strong symmetric keys + AES-based MACs, authenticate the *whole packet*, NTP (symmetric-key, not Autokey), IEEE 1588 Annex K, MACsec (hop-by-hop) / IPsec (end-to-end), NIDS/HIDS, trusted-platform attestation, delay-threshold detectors, clock-drift correction.
- **Resilience**: holdover oscillators, integrity monitoring (time-to-alarm · integrity risk · alarm limit), the **detect/alarm/fail-over** triad, source diversity (other GNSS, dedicated WANs, SyncE+PTP/White Rabbit, WWVB/WWV, eLORAN), redundant ring topologies.

---

## Use-Case Analysis (requirements)

Two stages: broad **CPS Examples** (many systems/actors) → single-actor/single-system **specific use cases** with step-level **primitive requirements**. Score consistently on the requirement-category form (a *living* artifact). Cluster on architectural characteristics to find and **fill coverage gaps**. Gathers *functional* requirements only.

---

## Tells & Smells

- **Facets as a strict waterfall** → forfeits the Framework's iteration; run them as modes.
- **Concerns analyzed in isolation** → they are not orthogonal; misses security-vs-safety trade-offs.
- **Siloed, per-discipline risk management** → the named thing to break; use cross-property risk management.
- **Risk budget split into fixed per-property shares** → treat it as a common resource instead.
- **Orphaned devices / orphaned code / lingering throwaway systems** → standing risks that can be co-opted.
- **Clean-slate interoperability that ignores legacy** → called unacceptable; legacy must be accommodated.
- **Changeable attributes baked into an identifier** → brittle; put them in the resolved record.
- **Non-cryptographic integrity checks (CRC/checksum/hash) against an attacker** → recomputable after tampering; use signatures.
- **Over-specifying the TI class** → SI-traceable accuracy where a quartz oscillator would do wastes hardware.
- **Ordering timestamps too close to distinguish** → within resolution / sync error, order is undefined.
- **Single timing source, no holdover/backup** → makes pervasive time loss possible.
- **NTP Autokey for authentication** → short effective key, flawed cert scheme; use symmetric-key.
- **GPS synchrophasors in automated control without secure timing** → a 10° walk-off can trip generators offline.
- **Naively "restoring" time after compromise** → risks new discontinuities; recovery must be bounded.

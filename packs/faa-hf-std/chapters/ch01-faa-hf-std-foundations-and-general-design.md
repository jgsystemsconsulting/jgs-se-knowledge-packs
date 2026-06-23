# Chapter 1 — Foundations: Scope, Definitions, and General Design Requirements

> Source basis: HF-STD-001B, Sections 1 (Scope), 2 (Applicable Documents), 3 (Definitions), and 4 (General Design Requirements). All claims in this chapter are grounded in those sections. Where a requirement names its provenance, that provenance is reproduced.

## Core Idea

HF-STD-001B is the FAA's human factors standard for acquiring and building the systems the agency manages, operates, or maintains. Its opening sections do three jobs in sequence: they fix the *scope* (what the standard governs and when it applies), they fix the *vocabulary* (a long controlled glossary so that "alert," "module," or "luminance" mean exactly one thing throughout), and they lay down the *general design requirements* that every later, more specialized requirement inherits. The general design section is the philosophical spine — durability, simplicity, consistency, standardization, safety, a user-centered perspective, support, and maintainability — stated as broad principles before the document descends into specifics like display contrast ratios or control spacing.

A defining feature is that the standard does not invent most of its general requirements from scratch. It aggregates and harmonizes prior human-engineering work — military standards, other-agency handbooks, and human factors literature — and re-states each requirement in FAA-applicable language with an explicit source attribution attached in brackets. So the foundational chapter is best read as a *curated synthesis* of the human-engineering canon, tuned to the FAA acquisition lifecycle.

A note on positioning relative to the rest of this knowledge-pack collection: HF-STD-001B is human factors / human-systems integration guidance from a *civil aviation regulator's* engineering standard. It is one instance of HSI thinking that lives outside the NASA tradition. It complements the `nasa-hsi` pack — indeed it cites NASA man-systems integration standards among its applicable documents (NASA-STD-3000A/B) — rather than duplicating it. Read the two as parallel HSI sources from different mission domains: spaceflight habitability and crew systems on the NASA side, FAA-operated air traffic and airway facility systems here.

## Frameworks Introduced (exact source names, when/how)

The foundational sections introduce or invoke the following named frameworks and source documents. Names are reproduced exactly as the standard cites them.

**The standard itself — HF-STD-001B.** Establishes human factors requirements for FAA system acquisition and development. Stated to apply at every stage of FAA system development — from the earliest mission-need determination, on through production and into deployment — and to be weighed for any engineering change or modification that touches how a human interacts with the fielded system.

**MIL-STD-1472G — *Design criteria standard, human engineering* (Department of Defense, 2012).** This is the single most-cited source in the general design section. It backs the durability requirement (4.1.1), function allocation (4.1.2), simplicity and minimal-training requirements (4.2.1–4.2.2), hardware/software standardization and identical-interface rules (4.4.1–4.4.2, 4.4.3, 4.4.6, 4.4.7), most of the safety requirements (4.5.1, 4.5.2, 4.5.10, 4.5.11), and several user-centered requirements including the design-within-user-abilities and percentile-accommodation rules (4.6.4, 4.6.5, 4.6.6, 4.6.10, 4.6.11), plus the common-tools maintenance rule (4.8.1). When the standard needs an authoritative human-engineering basis, it reaches for this document first.

**MIL-HDBK-759C — *Human engineering design guidelines* (Department of Defense, 1995).** Cited jointly with MIL-STD-1472G as support for standardization (4.4.1).

**DOD-HFDG-ATCCS (1992).** The DoD human factors design guide for the Army Tactical Command-and-Control System's soldier-machine interface. Backs the standardized-terminology/look-and-feel requirement (4.4.5), the design-to-meet-user-requirements rule (4.6.7), and the maintainability requirement (4.8.2). Notable because it is command-and-control human factors guidance, a domain close to air traffic control.

**DSTL-95-033 — *User-interface guidelines* (NASA Goddard Space Flight Center, 1996).** Supplies the consistency definition and several consistency requirements (4.3.1 by attribution, 4.3.2, 4.3.3) and the provide-help requirement (4.7.1). This is another point of contact with the NASA tradition: a NASA Goddard interface guideline cited directly as the basis for FAA consistency principles.

**NISTIR 4909 — *Software quality assurance: Documentation and reviews* (NIST, 1992).** Backs a cluster of safety requirements: identifying safe/unsafe states (4.5.6), emergency procedures for critical systems (4.5.7), redundancy for critical functions (4.5.8), and modular design (4.5.9).

**Galitz (1993).** A human factors literature source cited for the reliability requirement and its discussion (4.1.4), simplicity-related judgment, consistency (4.3.1), the standardized look-and-feel discussion (4.4.5), error tolerance (4.5.4), and the minimize-user-actions and transfer-of-skills requirements (4.6.8, 4.6.9).

**Martin & Dong (1999).** Cited for make-functions-obvious (4.2.3), error resistance (4.5.3), predictable results (4.6.2), and use-familiar-terms-and-images (4.6.3).

**Apple Computer Incorporated (1995).** Cited for warning before potentially serious actions (4.5.5) and timely-and-informative feedback (4.6.1) — a commercial UI guideline pulled into a federal standard.

**Ameritech (1998).** Cited for test-with-users (4.1.3, jointly with Galitz) and flexibility for different skill levels (4.6.13).

**Billings (1991).** Cited in the discussions of error resistance and error tolerance (under 4.5.3 and 4.5.4) — the source for the resistance-versus-tolerance distinction.

**Title 29 (1973) — accommodation for users with disabilities.** Cited as the basis for 4.6.12, designing to accommodate people with disabilities.

**NASA-STD-3000A / NASA-STD-3000B — *Man-systems integration standards* (1989 / 1995); DOE-HDBK-1140 (2001); NUREG-0700 and NUREG/CR-6015 (Nuclear Regulatory Commission); ISO 9241 series.** These appear in the Applicable Documents section as part of the reference base. DOE-HDBK-1140 backs the make-unique-functions-distinctive rule (4.4.4). Their presence signals that the standard's lineage spans space, energy, nuclear, and international ergonomics standards — not a single source domain.

**Order of precedence.** The standard sets an explicit precedence rule: where its text conflicts with a cited reference, the standard's own text governs — but nothing in it overrides applicable law or regulation absent a specific exemption. This is the conflict-resolution framework that makes the aggregation of so many external sources tractable.

## Key Concepts

**Scope as lifecycle-wide.** The standard is not a late-stage checklist. It applies to new, modified, or updated facilities, systems, and equipment, and is meant to inform decisions from mission-need determination onward. It is also offered as an evaluation aid for Commercial-Off-The-Shelf (COTS) and non-developmental item (NDI) selection and for research programs transitioning into fielded FAA systems.

**Requirement strength encoded in verbs.** The general design requirements are split between "shall" (mandatory) and "should" (recommended). Durability, function allocation, simplicity, minimize-training, hardware/software standardization, identical interfaces for identical functions, uniform controls/displays, interchangeability of identical equipment, non-interchangeability of different equipment, the full safety cluster's mandatory items, design-within-user-abilities, the 5th-to-95th-percentile floor, and accommodation of people with disabilities are all "shall." Reliability, make-functions-obvious, consistency, error tolerance, and most user-centered niceties are "should." Reading the verb is essential to knowing what is binding.

**The controlled glossary as an engineering instrument.** Section 3 is not a courtesy appendix; it is operative. It pins precise meanings to terms an engineer might otherwise treat loosely — for example, the difference between an *alert* (requires immediate action or signals a significant update), a *caution* (condition needs attention but not immediate action, or warns of possible equipment damage), an *advisory* (safe/normal condition or routine-action information), and a *warning* (notice that a situation might cause injury or loss of life). It also disambiguates *alarm filtering* (eliminating unnecessary alarms) from *alarm suppression* (alarms hidden but available on request). When later requirements use these words, the glossary is what gives them teeth.

**Levels of automation are defined, not assumed.** The glossary distinguishes *adaptive automation* (real-time, flexible reallocation of tasks between user and system to match situational demand, keeping the user in active control rather than a passive observer), *control automation* (the automated system executes control tasks with some autonomy), *information automation* (acquisition and integration — filtering, distributing, transforming data, confidence/integrity checks), and *decision aids* / decision support systems (automated support that can narrow alternatives or suggest a preferred decision). This taxonomy lets the standard talk about automation without ambiguity.

**Effectiveness versus efficiency.** The glossary separates the two precisely: doing a task *effectively* means producing the desired result; doing it *efficiently* means producing that result with minimum waste, typically of time. Several "should" requirements (e.g., minimize user actions) are efficiency claims, not effectiveness claims.

**Anthropometric accommodation as a design boundary.** The percentile concept is defined (*design limits approach*: applying population statistics about human physical characteristics so a chosen portion of users is accommodated) and then operationalized: design for at least the 5th-to-95th-percentile range of the relevant physical characteristics, and *should* accommodate the full range up to 100%. The standard is candid that a single-dimension 5th-to-95th cut does not equal 90% of the population across all dimensions, because body proportions are not linearly correlated.

**User-centered perspective, defined.** Focusing on the needs and requirements of the end user throughout design, acquisition, or development. This single definition anchors the entire 4.6 cluster — feedback, predictability, familiar terms, design within abilities, performance maximization, training minimization, skill transfer, anthropometric accommodation, disability accommodation, and skill-level flexibility.

## Mental Models

**Resistance versus tolerance (the two-layer error model).** The standard treats human error as something to handle in two distinct layers, citing Billings for the distinction. *Error resistance* (4.5.3) makes it hard for a user to commit an error in the first place — through simplicity, clear information, and aids like electronic checklists. *Error tolerance* (4.5.4) accepts that errors will still happen and mitigates their effects — for example by adding monitoring capability. A robust design needs both layers; they are not substitutes.

**Reliability is perceived, not just measured.** The reliability discussion (4.1.4) reframes reliability as a user judgment, not a binary uptime metric. A system that never fully shuts down can still be "unreliable" in the user's eyes if it misses alert conditions, gives incomplete situational information, or degrades under certain conditions. The mental model: design for *perceived* reliability across degraded states, not merely for absence of total failure.

**Consistency exploits existing mental models.** The consistency principles rest on the idea that users carry transferable knowledge. Consistent and standardized design lets a user apply skills learned on one system to a similar one without extensive retraining (4.3.1, 4.6.9). The standard names the levers for aligning a design with users' existing mental models: analogy with real-life objects, experience with similar systems, and previous operational experience (4.3.2).

**Simplicity as an error-reduction strategy.** Simplicity is framed not as aesthetic minimalism but as reliability and error engineering: the simplest design consistent with functional requirements tends to be more reliable, easier to maintain and operate, and carries less potential for human error (4.2.1 discussion). When comparing candidate designs from a human factors view, the simpler one is the lower-error-risk one.

**Standardization as a cost-and-error multiplier.** Standardization is modeled as paying off across many dimensions simultaneously: it simplifies maintenance, reduces the tools required, reduces potential for human error, and cuts training time, skill requirements, spares inventory, and documentation (4.4.1 discussion). The three sub-dimensions — standardized terminology, standardized look, standardized feel — each suppress a different class of variation (naming differences, appearance differences, action differences) (4.4.5).

**Modularity as fault-recovery.** The standard's mental model for modular design is replaceability: a module is a single physical-and-functional entity, and the advantage of designing in modules is that when one component fails it is easier to replace (4.5.9 definition). Modularity is thus tied to safety and maintainability, not just architectural tidiness.

**Anthropometric percentiles are a multidimensional trap.** The 5th-to-95th-percentile rule looks like it accommodates 90% of users, but the standard's model warns that this intuition fails across multiple body dimensions: someone at the 5th percentile in height may not be at the 5th percentile in reach or leg length, so applying the cut to every dimension excludes far more than 10%. Extending the range incurs cost/benefit tradeoffs. The model says: analyze the actual user population, design for adjustability, and provide accessories or custom modifications rather than trusting a single percentile band.

## Anti-patterns

The standard frames most guidance positively, but a few discussions name patterns to avoid:

- **Treating a single-dimension percentile band as full population coverage.** The 4.6.11 discussion explicitly warns that applying a 5th-to-95th cut to every body measurement at once tends to leave out a far larger share of users than the per-dimension 90% figure would suggest, because body proportions are not linearly correlated.
- **Equating "still running" with "reliable."** The 4.1.4 discussion identifies the failure of judging reliability only by complete-shutdown criteria; a degraded, partially-functioning system that misses alerts or gives incomplete information is perceived as unreliable.
- **Making functionally different equipment physically interchangeable.** Requirement 4.4.7 explicitly forbids this: if equipment is not functionally interchangeable, it shall not be physically interchangeable — the implied anti-pattern being parts that fit where they must not.

## Key Takeaways

- HF-STD-001B governs FAA-managed, -operated, or -maintained systems across the full development lifecycle and is also a tool for COTS/NDI evaluation and research-to-fielded transitions.
- Almost every general design requirement carries an explicit bracketed source; the standard is a harmonized synthesis of MIL-STD-1472G (its anchor), other military and agency handbooks (MIL-HDBK-759C, DOD-HFDG-ATCCS, NISTIR 4909, DOE-HDBK-1140, DSTL-95-033), and human factors literature (Galitz, Martin & Dong, Billings, Apple, Ameritech).
- The "shall" / "should" distinction is load-bearing: durability, function allocation, safety-critical items, the 5th-to-95th-percentile floor, and disability accommodation are mandatory; reliability, consistency, and error tolerance are recommended.
- The controlled glossary is operative engineering vocabulary — it pins down alert/caution/advisory/warning, alarm filtering/suppression, the automation taxonomy (adaptive, control, information, decision aids), and effectiveness versus efficiency.
- Error handling is two-layered: resistance (prevent errors) plus tolerance (mitigate the ones that occur).
- The eight general-design themes — durability/allocation/testing/reliability, simplicity, consistency, standardization, safety, user-centered perspective, support, and maintenance — are the inherited backbone for all later, more specific requirements.
- Order of precedence: the standard's text beats cited references on conflict, but never overrides law or regulation without a specific exemption.

## Connects To

- **`nasa-hsi`** — This is the primary complement. HF-STD-001B is HSI guidance from outside the NASA lineage, yet it cites NASA man-systems integration standards (NASA-STD-3000A/B) and a NASA Goddard interface guideline (DSTL-95-033) as source material. Read the two packs as parallel HSI traditions: NASA's crew/habitability focus and the FAA's air-traffic/airway-facility focus, sharing common human-engineering roots.
- **Later chapters of this pack** — The general design requirements here (Section 4) are the abstract layer; subsequent sections operationalize them into specific topics that the Section 3 glossary terms (displays, controls, alerts, automation, workstations, maintenance access) make precise.
- **Military human-engineering standards** — Through its heavy citation of MIL-STD-1472G and MIL-HDBK-759C, this pack connects directly to the DoD human-engineering corpus; an FAA requirement and its DoD parent can usually be traced one-to-one via the bracketed sources.
- **Systems engineering lifecycle packs** — The scope statement ties human factors to the FAA acquisition lifecycle from mission-need determination through deployment, aligning with SE lifecycle and acquisition framing found elsewhere in the collection.

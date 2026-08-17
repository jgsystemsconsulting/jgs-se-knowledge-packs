# Chapter 2: Interface Definition vs Identification

## Core Idea
Section 3.1 defines the interface in one sentence: two RF links (L1, L2) on which space vehicles continuously provide Earth-coverage ranging codes and system data so a suitably equipped user with RF visibility can navigate. Section 3.2 *identifies* the code and data families that realize that definition. Definition is the contract object; identification is the parts list. Chip-by-chip P/Y/C/A/CM/CL tables are identification *payload*, not the lesson.

## Frameworks Introduced
- **Definition (3.1)**: SS → US interface = L1 + L2; continuous Earth coverage; ranging + NAV data; available to a user with RF visibility. That is the shall-level “what exists.”
- **Identification (3.2)**: carriers are typically modulated by bit trains that are PRN ranging codes modulo-2 mixed with NAV data. CDMA lets many SVs share the same frequencies.
- **Code family, not a codebook**: P (principal precision ranging), Y (replaces P when anti-spoof is on), C/A (acquisition and civil ranging), plus — from IIR-M onward — L2 CM (moderate civil) and L2 CL (long civil). Non-standard (NSC, NSY, NSCM, NSCL) codes exist to keep users off anomalous signals and are *intentionally undefined* for user utilization.
- **Inseparable pairs**: a C/A phase assignment travels with a specific P phase. Identification tables are pairing contracts, not mix-and-match menus.
- **Block-conditional identification**: later blocks add codes and expand PRN space; GPS III/IIIF add “expanded” sequences (time-shifted or differently initialized). A manufacturer who chooses upper PRNs (38–63) inherits those table rows.

## Key Concepts
- **Dummy vs usable SVs**: users shall only use non-dummy satellites as defined by the current broadcast almanac (pointers into Apps II/IV). Identification includes a *validity rule*, not just a code list.
- **Upper-PRN bootstrap**: an initial almanac collected from P(Y) or C/A on upper PRNs must come from a stated subset (35, 36, or 38–63). PRN 33 is reserved (e.g. ground transmitters). CS prevents simultaneous C/A transmission of PRNs 34 and 37 (those C/A sequences are identical).
- **Signal structure (3.2.3) as identification of combinations**: L1 is two quadrature BPSK components (P(Y)+LNAV and C/A+LNAV). L2 combinations are ground-command selectable and block-dependent (P(Y) with or without data; C/A with or without data; L2 CM+CNAV time-muxed with L2 CL). All elements on one SV are coherently derived from one onboard frequency source.
- **Requirements traceability habit**: every identified component should be testable against a later 3.3 criterion or an appendix message spec. If it cannot be tested, it is color commentary.

## Mental Models
- **Contract object first, SKU list second** — same move as IRD “what” before ICD “how,” except here both live inside one IS.
- **Undefined on purpose** is an interface technique: non-standard codes are named so operators can switch them on, and left unspecified so users do not track them.
- **Block letters are applicability tags**, not a history essay.

## Anti-patterns
- **Transcribing Gold-code tap tables into a skill chapter** — that is App/table payload; open the official IS when implementing.
- **Treating Y-code as a documented civil ranging code** — it replaces P under A-S; this IS does not teach how to generate it.
- **Mixing codes across an inseparable pair.**
- **Ignoring dummy-SV / reserved-PRN rules** because “we have a lock.”

## Key Takeaways
1. 3.1 is the one-sentence interface; 3.2 names the codes and data that implement it.
2. CDMA + coherent onboard source is the identification architecture.
3. Know the family names (P/Y, C/A, L2 CM/CL, non-standard) without memorizing chips.
4. Pairing, dummy-SV, and reserved-PRN rules are part of identification.
5. L1/L2 combinations are block- and command-selectable; Table 3-III is the map, not a dump.
6. Trace each identified item to a criterion or an appendix — or cut it.

## Connects To
- **ch01**: Why this document is the contract and how it changes.
- **ch03**: Measurable criteria on the composite signal.
- **ch04**: NAV data as the other half of the bit train.
- **ch06**: Where the actual PRN assignment tables live if you must implement them.

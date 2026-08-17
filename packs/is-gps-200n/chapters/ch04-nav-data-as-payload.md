# Chapter 4: NAV Data as Interface Payload

## Core Idea
Navigation data is an interface *payload family*, not a pile of bits in the body of the IS. Section 3.2.2 names two families — legacy LNAV D(t) and civil CNAV DC(t) — says what each is for, how it is attached to which code, and *which appendix* holds the structure. Section 3.3.3 points at modulation (including L2 CM FEC) without reproducing polynomials here.

## Frameworks Introduced
- **LNAV D(t)**: 50 bps stream with ephemerides, system time, clock behavior, status, and C/A-to-P(Y) handover, etc. Modulo-2 added to P(Y) and C/A; when present, the same D(t) is common to those codes on L1 and L2 for a given SV.
- **Split annex by PRN band**: App II = LNAV for PRN 1–32; App IV = LNAV for PRN 33–63. Same family, two normative homes so upper-PRN differences do not rewrite the lower-PRN decoder.
- **CNAV DC(t)** (IIR-M, IIF, and later): also ephemerides, time, clock, status. 25 bps encoded with a rate-1/2 convolutional encoder to 50 sps, modulo-2 onto L2 CM, then chip-by-chip TDM with dataless L2 CL onto the L2 carrier when so commanded. Structure lives in App III.
- **Message-type thinking (CNAV)**: App III organizes payload as typed messages (ephemeris, clock, iono/group delay, almanacs, EOP, UTC, differentials, GNSS time offset, text, integrity support). The body only needs you to know that *types exist* and are selected/paged — not each field.

## Key Concepts
- **Body vs annex contract**: 3.2.2 is the allocation clause (“this family exists, rides these codes, details in App X”). Implementing a subframe parser without opening the annex is a defect, not a synthesis win.
- **Common-on-SV LNAV**: one D(t) shared across P(Y)/C/A and L1/L2 simplifies user correlation of data with ranging, and is itself an interface shall-level fact.
- **Commanded presence**: CNAV-on-L2 is ground-command selectable among several L2 configurations (ch02). Payload availability is a configuration of the interface, not a permanent bit on every SV.
- **FEC is a modulation criterion, not a chapter**: 3.3.3.1.1 exists so a civil L2C receiver can decode DC(t). This pack does not reproduce the encoder taps.
- **Integrity and health travel with the payload** (alarm/marginal protocols in §6; ISM message type in App III). Treat health bits as interface semantics, not as optional telemetry.

## Mental Models
- Think **envelope + attachments**: the IS body is the envelope; Apps II–IV are the attachments that carry normative bits.
- LNAV is a *single stream, two PRN neighborhoods*; CNAV is a *typed mailbox* on L2 CM.
- If you cannot name the appendix that owns a field, you are not ready to implement it.

## Anti-patterns
- **Transcribing TLM/HOW/subframe bit maps or CNAV type figures into this pack.**
- **Assuming CNAV is always on L2** — it is a selectable configuration.
- **Merging App II and App IV mentally** — upper PRNs were given their own annex for a reason.
- **Treating FEC polynomials as core-framework content.**

## Key Takeaways
1. Name the payload family (LNAV vs CNAV), its rate, and its host code(s).
2. Point implementers at App II / III / IV; do not paste those annexes.
3. LNAV D(t) is common across codes/carriers on one SV when present.
4. CNAV is typed, FEC’d, and command-selected onto L2 CM.
5. Health/integrity bits are interface semantics.
6. Preparation-side traceability (shall → VRTM) still belongs in `faa-std-025`.

## Connects To
- **ch02**: Codes the payload is mixed with.
- **ch03**: Physical criteria the symbols ride on.
- **ch05**: Time tags, URA, CEI that make payload *usable*.
- **ch06**: Appendix map for when you actually need the bits.

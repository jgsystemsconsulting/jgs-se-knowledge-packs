# Chapter 5: Time, Z-Count, and Definition Hygiene

## Core Idea
An ICD that cannot define time, accuracy, and “what counts as valid” will be mis-implemented even if every RF shall is perfect. Section 3.3.4 (GPS time and SV Z-count) plus §6 notes (URA, CEI, reserved, invalid, operational intervals) are the hygiene layer. Skip SV-block trivia; keep the definitions that change user algorithms.

## Frameworks Introduced
- **GPS time / Z-count**: the Space/User timebase and the SV’s integer time count that ties ranging epochs to NAV data (HOW and related fields live in the annexes). Users convert SV time to GPS time with the broadcast clock model — the *existence* of that conversion is a body-level interface fact.
- **User Range Accuracy (URA)** and **User Differential Range Accuracy (UDRA)**: broadcast indicators of ranging integrity/accuracy, not a promise of a particular RMS in every geometry. Defined in §6 so App II/III fields have a home meaning.
- **Clock, Ephemeris, Integrity (CEI) data set**: the bundled parameters a user needs to treat a solution as one consistent set. Core CEI vs sequence-propagation rules tell you when a new issue-of-data starts and how long a set may be used. Mixing parameters from two CEI sets is an interface defect.
- **Reserved / valid range / invalid**: reserved bits are not user-writable semantics; valid range is the legal broadcast interval; invalid means do not use. These three words prevent “decoder archaeology.”
- **Operational intervals**: normal, short-term extended, long-term extended — they change how long data remains applicable. Extended and autonomous navigation modes exist as supporting notes, not as a license to ignore CEI cutovers.

## Key Concepts
- **Week number** is an interface type with rollover implications; §6.2.4 exists so implementers do not invent a private epoch.
- **Health and alarm protocol** (§6.4.6): common vs specific alarm indications, plus “marginal” indications. Users have a stated protocol for combining signal-availability and health information — another ICD hygiene pattern (do not leave health as folklore).
- **PRN-number protocols** (§6.4): lower vs upper PRNs, consistency, special handling of 33 and 37, 33–63. These are operational interface rules sitting next to the definitions.
- **L5 / L1C civil signals** are pointed out as *other* IS documents (705/800 family). This pack does not follow that pointer.
- **Pre-operational use** and letters of exception (App I) can qualify a definition for a specific SV — check exceptions before declaring a shall absolute.

## Mental Models
- Time + issue-of-data + health is the *usability triple*. RF lock without that triple is not a compliant use of the interface.
- CEI is a *transaction*: take the whole set or take none.
- “Reserved” means *off limits*, not *available for vendor extensions*.

## Anti-patterns
- **Blending clock from one IODC/IODE with ephemeris from another.**
- **Treating URA as a guaranteed user RMS.**
- **Ignoring extended-operation intervals** after an upload gap.
- **Narrating Block II vs IIR vs III history** instead of the definition that still binds.
- **Following L5/L1C pointers into 705J/800J in this phase.**

## Key Takeaways
1. Define the timebase (GPS time, Z-count, week) in the IS body or notes, not only in a figure.
2. URA/UDRA are broadcast accuracy *indicators* with §6 definitions.
3. Consume CEI as a set; honor sequence-propagation and issue-of-data.
4. Reserved / valid / invalid are first-class interface words.
5. Health/alarm protocol is normative user behavior.
6. Check App I exceptions before hard-coding a shall.

## Connects To
- **ch01**: IRNs often exist to clarify exactly these definitions (URA, health bits, leap second).
- **ch04**: Payload fields that carry URA, clock, and CEI.
- **ch06**: App I letters; Apps II–IV field homes.

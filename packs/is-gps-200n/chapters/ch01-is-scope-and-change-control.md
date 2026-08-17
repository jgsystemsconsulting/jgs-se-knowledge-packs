# Chapter 1: What an IS/ICD Is — Scope, DIST-A, and Change Control

## Core Idea
IS-GPS-200 is an Interface Specification between the GPS Space Segment and the navigation User Segment for L1 and L2. It is the worked example of a public ICD/IS: a numbered technical contract, under configuration control, marked Distribution Statement A. It specifies technical requirements and, by its own cover notice, does not alter any contract or purchase order.

## Frameworks Introduced
- **IS vs ICD naming**: this document is titled Interface Specification (historically ICD-GPS-200; a later revision renamed it IS-GPS-200). Functionally it is the Space/User interface control document for L1/L2.
- **DIST-A marking**: “DISTRIBUTION STATEMENT A. Approved for public release. Distribution is unlimited.” A revision-record line records that distribution status was changed to Public Release.
- **Change-control chain**: government-designated Interface Control Contractor (ICC) prepares, coordinates, distributes, and retains the IS per GP-03-001. GPS Directorate (historically SMC/GP; cover authority is SSC / MilComm & PNT) makes the IS effective via a Configuration Control Board. Civil/public interest is represented at the CCB by the Department of Transportation member.
- **PIRN / IRN loop**: any ICWG participant may propose a change. ICC writes a Proposed Interface Revision Notice, coordinates it with the Interface Control Working Group (45-day review, extendable in writing), then the CCB approves. Approved changes become Interface Revision Notices folded into the next revision letter. Rev N is “Incorporation of IRN-IS-200M-001; RFC-467.”

## Key Concepts
- **Cover identity to record, not to romanticize**: IS-GPS-200, REV N, 01-AUG-2022; PNT Technical Director, MilComm & PNT Directorate, Space Systems Command. SAIC is named Interface Control Contractor — a watch-item for licence hygiene, not pack content and not a street-address chapter.
- **Authority vs contractor**: ICC does the paper; the Directorate CCB is the necessary authority. Segment members represent military/contractor organizations; DOT speaks for civil users.
- **Empty §4 / §5**: “NOT APPLICABLE” is an explicit ICD pattern — reserved section numbers stay in the outline so later revs do not renumber the world.
- **Applicable documents are thin on purpose**: the interface is largely self-contained. Government citations include the AWG/ROM-IA charter (GP-03-001) and IERS Technical Note 36. No pile of “see also” specs substitutes for the shalls in §3.
- **Revision record as CM evidence**: lettered revs plus IRN/RFC identifiers are how a receiver vendor proves which interface they built to.

## Mental Models
- An IS is a *bilateral technical contract* under CM, not a tutorial and not a statement of work.
- Public release (DIST-A) is a *distribution* fact; it is why this pack can exist. It is not a promise that every GPS ICD is public (ICD-GPS-153 is request-only and is not here).
- Change is a *paper trail* (PIRN → ICWG → CCB → IRN → next letter), not a Slack agreement.

## Anti-patterns
- **Treating the ICC street address as interface content.**
- **Implementing “what the last IRN meant” without the approved IRN/revision letter.**
- **Assuming every GPS interface document is DIST-A** — confirm on the copy you extracted (P11-PRE-2).
- **Using this pack as a substitute for `faa-std-025`** — that pack is how to *write* an IRD/ICD; this one is a live IS.

## Key Takeaways
1. IS-GPS-200N is the L1/L2 Space/User interface specification, Rev N, public release.
2. DIST-A is on this extracted copy; quote it when citing licence posture.
3. ICC prepares; Directorate CCB approves; ICWG gets 45 days on PIRNs.
4. Empty numbered sections are reserved, not forgotten.
5. Do not ingest 705J, 800J, ICD-GPS-153, or a fictional IS-300.
6. Pair with `faa-std-025` when the question is preparation format rather than this interface.

## Connects To
- **ch02**: What the interface *is* versus how its parts are *named*.
- **ch06**: Where exceptions and normative annexes live.
- **faa-std-025**: IRD/ICD preparation, VRTM, and CM process (different slug, complementary role).

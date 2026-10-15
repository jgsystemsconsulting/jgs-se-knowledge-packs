# Chapter 5 - DO-178C Recognition and Transition

Sources: AC 20-115D, Airborne Software Development Assurance Using EUROCAE ED-12( ) and RTCA DO-178( ) (2017-07-21), sections 1-6 and 10 (printed pages 1-4 and 10-12 body; section 7 Reserved and sections 11-12 out of scope for this chapter).

## Core Idea

AC 20-115D is the FAA recognition instrument for airborne software development assurance. It describes an acceptable means (not the only means, and not a regulation) for showing software compliance in type certification or TSO authorization. The AC recognizes ED-12C/DO-178C and the related tool and technique supplements, keeps a path for mature ED-12B/DO-178B process users to continue those processes on new development under stated criteria, and moves tool qualification onto ED-215/DO-330 with explicit transition rules for legacy-qualified tools.

## Frameworks Introduced

- **Recognition set (section 1.b).** ED-12C / DO-178C (software considerations); ED-215 / DO-330 (tool qualification); ED-218 / DO-331 (model-based development and verification); ED-217 / DO-332 (object-oriented technology and related techniques); ED-216 / DO-333 (formal methods). EUROCAE ED and RTCA DO pairs listed together are treated as equivalent. Supporting information documents ED-94C / DO-248C (FAQs and discussion papers) are identified but are not themselves the means of compliance.

- **References include supplements.** Mentions of ED-12C/DO-178C in the AC include ED-215/DO-330 and the three technique supplements as applicable.

- **Objective / activity / evidence model (section 4).** The recognized documents give objectives for life cycle processes, activities that satisfy them, and descriptions of evidence that objectives are satisfied.

- **DO-178B process reuse for new development (section 5).** Six criteria; fail any and upgrade to DO-178C (and section 12.2 / paragraph 10.c tool rules). New process establishments use DO-178C.

- **Using DO-178C (section 6).** Satisfy all objectives for the assigned software level; produce associated life cycle data per Annex A tables in DO-178C and applicable tool/supplement tables; submit section 9.3 (and tool 9.0.a) data; keep section 11 data available on request.

- **Tool qualification transition (section 10).** DO-330 is the complete tool qualification method aligned with DO-178C section 12.2. Legacy DO-178 / DO-178A / DO-178B tool situations follow separate branches, including Table 2 correlation of DO-178B tool types to DO-178C tool criteria and TQLs.

## Key Concepts

### Purpose, applicability, cancellation

- Acceptable means for software aspects of airborne systems and equipment in type certification or TSO authorization; not mandatory; not a regulation. If you use the means, follow it in all applicable respects.

- Audience: applicants, design approval holders, and developers of airborne systems and equipment containing software for type-certificated aircraft, engines, and propellers, or for TSO articles.

- Cancels AC 20-115C (2013-07-19).

- Technical content is harmonized as far as practicable with EASA AMC 20-115D (named only; this pack does not restate EASA text).

### Section 5 - keep DO-178B processes for new development only if all apply

1. **No known process deficiencies** (audits, reviews, or open problem reports that leave DO-178B objectives unsatisfied). Evidence of closure of process-related OPRs and findings may be requested.

2. **Prior use at equal or higher software level** on a certified product.

3. **MBD, OOT, or formal methods:** existing processes for those techniques were evaluated and found acceptable by the FAA on a previous certified project, developed under FAA technique-specific guidance (issue paper or published AC).

4. **Parameter Data Item / configuration data:** existing processes acceptable on a previous certified project, or else establish new PDI processes per DO-178C.

5. **No significant changes** to processes in the plans or to the software development environment (show this by analysis of changes to the previously accepted processes and environment).

6. **No intent to declare** the proposed software as having satisfied DO-178C.

If section 5.a fails: upgrade processes and develop new software using DO-178C; address tool qualification per DO-178C section 12.2 and AC paragraph 10.c. Applicants establishing new life cycle processes do so under DO-178C.

### Section 6 - operating under DO-178C

- Satisfy every objective for the assigned software level and build the life cycle data that shows it, including applicable DO-330 and supplement Annex A tables. Plan and execute activities for each objective.

- If the FAA chooses not to engage in certification liaison, liaison objectives and activities may be treated as satisfied after producing the life cycle data in Table(s) A-10 of DO-178C, DO-330, and supplements as applicable.

- Submit life cycle data in DO-178C section 9.3 and, for tools, DO-330 section 9.0.a, to the project certification office. Performing planned activities and producing the data remains the applicant responsibility.

- Type design related data: DO-178C section 9.4. Not all items apply at every level; Design Description and Source Code are not type design data for Level D.

- Make available on request any section 11 data, applicable tool qualification data, supplement outputs, and other data needed to substantiate objectives.

- FAA-published acceptable means for specific regulations that tie system criticality to DO-178C software levels take precedence over applying DO-178C section 2.3 alone.

### Section 10 - tool qualification branches

- **Method.** DO-178C section 12.2 and DO-330 provide an acceptable tool qualification method. DO-330 carries its own objectives, activities, and life cycle data.

- **Legacy DO-178 or DO-178A software, new or modified tool.** Use DO-178C section 12.2 to decide if qualification is needed. If yes, derive TQL from the system-safety-assigned software level and use DO-330. You may declare the qualified tool as satisfying DO-330, but you may not declare the legacy software equivalent to DO-178C on that basis alone.

- **Legacy DO-178B software, no DO-178C equivalence claim.** Either keep DO-178B tool qualification processes for new/modified tools supporting that legacy software, or update tool processes and qualify under DO-330 using Table 2 for TQL; then you may declare the tool as satisfying DO-330.

- **Legacy DO-178B software, intending DO-178C equivalence, with legacy tools to qualify.** DO-178C defines five TQLs from tool use and impact (see DO-178C section 12.2.2 and Table 12-1). Table 2 in the AC correlates prior DO-178B development/verification tool qualification types and software levels to DO-178C tool criteria and TQLs (development tools map across TQL-1 through TQL-4 by level; verification tools map to TQL-4 or TQL-5 by criteria 2 or 3).

  - **Development tools:** if the prior DO-178B software level assigned to the tool meets or exceeds the required TQL, keep DO-178B tool processes (run DO-330 sections 11.2.2/11.2.3 change impact analysis on tool or environment changes, then change under DO-178B processes). If it does not meet the required TQL, update processes and requalify under DO-330. Declare DO-330 equivalence only if tool and process changes satisfy DO-330.

  - **Verification tools:** if required TQL is TQL-5 and the tool was DO-178B-qualified, keep DO-178B processes (on changes, impact-analyze and reverify under DO-178B or requalify under DO-330). If required TQL is TQL-4, requalify under DO-330. DO-330 equivalence declaration follows the same all-changes-satisfy-DO-330 rule.

## Mental Models

- AC 20-115D points at industry standards; it does not reprint them. Objectives and Annex tables live in the paywalled RTCA/EUROCAE documents (see avionics-signpost for designations only).

- May keep DO-178B processes is a gated privilege for proven process owners, not a default for every applicant. New process shops start on DO-178C.

- Tool story and software story can diverge: a tool may be declareable to DO-330 while legacy software is not declareable to DO-178C, and unmodified tools cannot be declared equivalent to DO-330 merely because software was upgraded.

- Parameter data / PDI is a first-class transition trigger. Missing acceptable PDI processes forces DO-178C PDI process creation even when other DO-178B process reuse criteria pass.

- Section 6.e precedence: a regulation-specific FAA acceptable means that sets software level from system criticality outranks rolling your own reading of DO-178C section 2.3.

## Anti-patterns

- **Declaring DO-178C satisfaction while still on unchanged DO-178B processes.** Section 5.a(6) forbids that combination for the reuse path.

- **Reusing DO-178B processes after significant plan or environment change without analysis.** Criterion 5.a(5) requires change analysis against the previously accepted baseline.

- **Assuming liaison absence removes data obligations.** Even if the FAA steps back from liaison, Table A-10 data still has to exist before liaison objectives are considered satisfied.

- **Treating Level D like Level A for type design data.** Under DO-178C section 9.4 as applied by section 6.c, Design Description and Source Code are not type design data at Level D.

- **Mapping legacy verification tools to TQL-4 without requalification.** Section 10.c(3)(b) requires DO-330 requalification when TQL-4 is required.

- **Copying DO-178C objective tables into project paperwork from secondary notes.** This pack intentionally carries none; use the standard itself.

## Key Takeaways

1. AC 20-115D recognizes DO-178C plus DO-330 and the DO-331/332/333 supplements (with EUROCAE equivalents) as the current software assurance means set, and cancels AC 20-115C.

2. Mature DO-178B process users may keep those processes for new development only when all six section 5.a criteria hold; otherwise move to DO-178C.

3. Under DO-178C, meet every applicable objective, submit section 9.3 (and tool) data, and keep section 11 data available; Level D drops Design Description and Source Code from type design data.

4. Tool qualification transitions to DO-330; section 10 and Table 2 govern legacy DO-178B development and verification tools when DO-178C equivalence is in play.

5. The AC is guidance, not regulation; other acceptable means remain possible, and regulation-specific FAA level-mapping ACs can take precedence on criticality-to-level linkage.

## Connects To

- **ch01** - recognition-chain orientation across Order 8110.49A, AC 20-115D, and AC 20-152A.

- **ch02** - FAA software review / certification liaison that consumes the life cycle data section 6 requires.

- **ch06** - supplement use, FLS, UMS, and the legacy software modification flow that builds on these recognition and tool rules.

- **ch04** - conformity type-design data expectations that align with section 9.4 discussions in both the order and this AC.


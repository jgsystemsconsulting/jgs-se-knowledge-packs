# Chapter 6 - Legacy Software, Field-Loadable Software, and User-Modifiable Software

Sources: AC 20-115D, Airborne Software Development Assurance Using EUROCAE ED-12( ) and RTCA DO-178( ) (2017-07-21), sections 8-9 (printed pages 4-10; Figure 1 legacy software process flow chart on printed pages 6-7). Tool details referenced from section 10 remain in ch05.

## Core Idea

AC 20-115D sections 8 and 9 cover three practical problems that sit on top of DO-178B or DO-178C projects: how to apply the technique supplements, what extra controls field-loadable and user-modifiable software need, and how to modify or re-use software previously approved under DO-178, DO-178A, or DO-178B. Section 9 centers on a flow chart (Figure 1) and numbered procedures. Most projects follow that flow; anything outside it is coordinated with the certification office.

## Frameworks Introduced

- **Supplement application rules (section 8.a).** DO-331 (model-based), DO-332 (object-oriented), and DO-333 (formal methods) apply when those techniques are used. Multiple techniques mean multiple supplements. Supplements are not stand-alone documents.

- **FLS add-on controls (section 8.b).** Field-loadable software uses DO-178B/C FLS system-level guidance plus four AC-level protections (corruption/partial-load integrity, verifiable loaded part number, inhibit of field loading in flight or other safety-critical phases, plus developer support data for the standard system-level items).

- **UMS add-on controls (section 8.c).** User-modifiable software uses DO-178B/C UMS system-level guidance plus the rule that the modifiable portion is developed at a software level at least as high as the level assigned to that software.

- **Legacy software flow (section 9 + Figure 1).** Usage-history gate, then software-level acceptability (Table 1), then modify-or-not branch, then change impact analysis and tool triggers, then keep-original-version-versus-upgrade-to-DO-178C decision tree, including optional DO-178C equivalence declaration rules.

- **Table 1 - legacy level relationships.** Maps assigned DO-178B/C software levels A-D against legacy DO-178B levels, DO-178A levels 1-3, and DO-178 Critical / Essential / Non-Essential. A mark at a row/column intersection means the legacy level is acceptable for that assigned level; blank means not acceptable. DO-178B levels align with DO-178C levels. Worked example in the AC: DO-178A Level 2 satisfies B, C, and D but not A.

## Key Concepts

### Section 8.a - supplements with DO-178C

When using one or more supplements, the Plan for Software Aspects of Certification (PSAC) describes:

- How DO-178C and the supplement(s) apply together.

- How applicable DO-178C objectives and objectives added or modified by the supplement(s) are covered: which objectives from which documents apply to which software components, and how planned activities satisfy all applicable objectives.

If supplement techniques are used to develop a qualified tool (TQL 1-4 only), the Tool Qualification Plan describes which tool qualification objectives the technique affects (from supplement analysis) and how planned activities satisfy added or modified objectives.

**Model-based clarification (DO-331 MB.6.8.1).** If models as defined in DO-331 MB.1.0 are the basis for developing software, apply DO-331. For MB.6.8.1: identify which reviews-and-analyses objectives will be satisfied by simulation alone or combined with reviews and analyses; all other objectives stay with reviews and analyses per MB.6.3. For each identified objective, justify in detail how simulation (alone or combined) fully satisfies that specific objective.

### Section 8.b - field-loadable software (FLS)

Use in addition to DO-178B section 2.5 items a-d or DO-178C section 2.5.5 items a-d:

1. Developer provides information supporting those system-level guidance items.

2. Protect FLS against corruption or partial loading to an integrity level appropriate for the FLS software level.

3. FLS part number, when loaded in the airborne equipment, must be verifiable by appropriate means.

4. Protection mechanisms prevent inadvertent enabling of the field-loading function during flight or any other safety-critical phase.

### Section 8.c - user-modifiable software (UMS)

Use in addition to DO-178C section 2.5.2 items a, b, c, and f (or DO-178B section 2.4 items a and b):

1. Developer provides information supporting those system-level items.

2. The modifiable part of the component is developed to a software level at least as high as the software level assigned to that software.

### Section 9 - legacy software definition and flow

**Legacy software** here means previously approved software, or a component of it, used in legacy systems under DO-178, DO-178A, or DO-178B as the means of compliance. Section 9 explains how to show software aspects of certification when modifying legacy software or using it unmodified.

**Figure 1 procedure spine (section 9.b):**

1. **Usage history (9.b(1)).** Assess history from prior installations. If safety-related service difficulties, airworthiness directives, or open problem reports have potential safety impact on the proposed installation, plan resolution of related software deficiencies. Before modify/reuse, correct related development process deficiencies (audit/review findings or OPRs that leave DO-178B objectives unsatisfied). Closure evidence may be requested.

2. **Software level acceptability (9.b(2) + Table 1).** System safety assigns the minimum development assurance level from failure-condition severity. Check Table 1 whether the legacy level satisfies the assigned level for the new installation.

   - DO-178 Essential previously accepted by the authority for Level B remains acceptable; if never assessed or not acceptable, upgrade baseline (processes, procedures, tool qualification) using DO-178C section 12.1.4 and DO-330.

   - DO-178A level not acceptable: upgrade baseline via DO-178C section 12.1.4 and DO-330.

   - DO-178B level not acceptable: upgrade baseline via DO-178B section 12.1.4 or DO-178C and DO-330.

3. **No modification required and criteria 9.b(1)-(2) hold (9.b(3)).** Original approval may serve as the basis for the software in the new installation approval. If you upgraded the baseline fully to DO-178C and DO-330 processes, you may declare software equivalent to satisfying DO-178C, but you cannot declare unmodified tools equivalent to DO-178C/DO-330; all later software and tool changes use the DO-178C/DO-330 processes.

4. **Modifications required (9.b(4)).** Perform software change impact analysis (CIA) for extent, impact, and required verification so modified software still performs its intended function and meets the identified means of compliance. Identify changes; run one or more analyses per DO-178C section 12.1; verify as the CIA indicates; summarize CIA results in the PSAC or SAS. AC 00-69 section 3.1 gives the best-practice contents of that analysis; see ch11. It is best practices, not a means of compliance.

5. **New or modified tools (9.b(5)).** Determine qualification needs per section 10 (see ch05).

6. **After a 9.b(2) upgrade to DO-178C (9.b(6)).** Make all software modifications under DO-178C section 12.1. Equivalence declaration, if sought, covers modified and unmodified software even if unmodified tools were not DO-178C-qualified; unmodified tools still cannot be declared DO-330-equivalent; subsequent changes use DO-178C/DO-330 processes.

7. **Keep original DO-178( ) version processes for modifications (9.b(7)).** Allowed only if all hold: MBD/OOT/FM processes (if used) were FAA-accepted on a prior certified project under technique-specific guidance; software plans, processes, and life cycle environment are maintained and still usable (including captured improvements); no intent to declare DO-178C satisfaction.

8. **When 9.b(7) holds (9.b(8)).** Accomplish modifications under the same DO-178( ) version as the original approval; do not declare DO-178C equivalence. For Parameter Data Item / configuration data, reuse FAA-accepted prior processes or establish new PDI processes under DO-178C.

9. **When any 9.b(7) condition fails (9.b(9)).** Update all processes and procedures (including tool qualification) to DO-178C and DO-330; modify software under DO-178C section 12.1. Equivalence rules match 9.b(6): software may be declared equivalent even with unmodified non-DO-330 tools; tools themselves may not; all subsequent changes use DO-178C/DO-330 processes.

## Mental Models

- Figure 1 is the default decision procedure. Branch off it only with certification-office coordination.

- History and level gates come before style-of-change questions. Do not plan a small DO-178B delta until usage history and Table 1 acceptability are clean.

- Equivalence is declared, not assumed. Upgrading processes enables a DO-178C claim; keeping original-version processes forbids it.

- Tools lag software on equivalence: software can be claimed DO-178C-equivalent while unmodified tools cannot be claimed DO-330-equivalent.

- FLS is about load integrity and inhibit-in-flight; UMS is about the modifiable partition assurance level. Both still rest on the base DO-178B/C system-level FLS/UMS guidance the AC points to by section number.

- Supplements attach to techniques and to components. PSAC must say which document objectives hit which software pieces; a generic we follow DO-331 statement is not enough.

## Anti-patterns

- **Using a supplement as a stand-alone means.** Section 8.a forbids it; supplements modify and add to DO-178C, they do not replace it.

- **Satisfying DO-331 reviews-and-analyses objectives by simulation without per-objective justification.** MB.6.8.1 requires explicit identification and detailed justification.

- **Field load without corruption/partial-load protection or in-flight inhibit.** Sections 8.b(2) and 8.b(4) are AC-level requirements on top of the standard.

- **UMS modifiable partition at a lower software level than the component.** Section 8.c(2) requires at least the assigned level.

- **Reusing legacy software with open safety-related OPRs, SDs, or ADs and no resolution plan.** Section 9.b(1) blocks that path.

- **Claiming DO-178C equivalence while modifying under original DO-178B plans.** Section 9.b(7)(c) and 9.b(8)(a) make those states mutually exclusive.

- **Skipping CIA on small modifications.** Section 9.b(4) requires CIA, verification per CIA, and PSAC/SAS summary whenever modifications are required.

## Key Takeaways

1. Apply DO-331/332/333 with DO-178C when those techniques are used; describe the combined objective coverage in the PSAC (and in the Tool Qualification Plan when tools use the techniques at TQL 1-4).

2. FLS needs developer support data, corruption/partial-load protection scaled to software level, verifiable loaded part number, and inhibit of field loading in flight or other safety-critical phases.

3. UMS needs developer support data and a modifiable partition developed at least at the component assigned software level.

4. Legacy modify/reuse follows Figure 1: clean usage history, Table 1 level fit, then either reuse original approval, run CIA-based modification under original version (if 9.b(7) holds), or upgrade processes to DO-178C/DO-330.

5. DO-178C equivalence is available after full process upgrade paths; it never extends automatically to unmodified tools.

6. New or changed tools during legacy work route to section 10 (ch05).

## Connects To

- **ch01** - which source answers recognition versus legacy-change questions.

- **ch05** - DO-178C recognition, section 5 new-development reuse criteria, life cycle data rules, and section 10 tool qualification transition invoked by 9.b(5).

- **ch02** - certification liaison and reviews that will examine PSAC/SAS CIA summaries and supplement coverage claims.

- **ch04** - conformity still needs controlled part numbers and load procedures when FLS is the delivery path into the target LRU or aircraft system.

- **ch11** - CIA best-practice checklist that deepens section 9.b(4).


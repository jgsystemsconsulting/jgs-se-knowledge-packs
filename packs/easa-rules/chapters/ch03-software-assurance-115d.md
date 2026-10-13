# Chapter 3: Software Assurance as AMC 20-115D Frames It

Sources: S1 AMC 20-115D (ED Decision 2017/020/R; AMC-20 Amendment 14, consolidated in Amendment 23), sections 4 BACKGROUND through 9 MODIFYING AND REUSING SOFTWARE APPROVED USING ED-12/DO-178, ED-12A/DO-178A, OR ED-12B/DO-178B, lines 89-580 of `sources/text/S1.txt` (printed pp. 417-424). Exclusions: EAR footers; section 7 RESERVED; figure ASCII art kept as paraphrase only. Name-only standards cited here by designation: ED-12C/DO-178C, ED-12B/DO-178B, ED-12A/DO-178A, ED-12/DO-178, ED-215/DO-330, ED-216/DO-333, ED-217/DO-332, ED-218/DO-331. Objective tables from those standards are not reproduced (see ED-12C/DO-178C, not reproduced).

## Core Idea

AMC 20-115D treats software development assurance as a set of life cycle processes: planning, development, verification, configuration management, quality assurance, and certification liaison. The recognised EUROCAE/RTCA documents supply that guidance as objectives for the processes, activities that satisfy the objectives, and descriptions of the evidence that the objectives were met. The AMC itself does not restate those objective tables. On top of recognition, the AMC adds process rules: when established ED-12B/DO-178B processes may continue for new development, how ED-12C/DO-178C and its supplements are used, how field-loadable and user-modifiable software are handled, and how legacy software approved under earlier editions is modified or reused.

## Frameworks Introduced

- **Three-part guidance form.** Objectives for life cycle processes; activities that provide a means of satisfying them; evidence descriptions that show satisfaction. Source of the form: the recognised documents listed in section 1.b (see ch02), not a reprint in this AMC.
- **ED-12B/DO-178B process continuation (section 5).** Six criteria gate continued use of established B-era processes (including tool qualification processes) on new development. Fail any criterion and the applicant upgrades to ED-12C/DO-178C.
- **ED-12C/DO-178C usage rules (section 6).** Satisfy all objectives for the assigned software level; produce associated life cycle data; submit the data the standard's certification-liaison sections call for; make further data available on request; respect any CS-specific AMC that sets the criticality-to-software-level relationship (that AMC wins over the standard's generic mapping section).
- **Supplements with the primary pair (section 8.a).** Technique supplements are not stand-alone. The plan for software aspects of certification (PSAC) states how the primary document and each supplement apply together, which objectives come from which document, and how planned activities cover them. Tool qualification plans do the same when a qualified tool uses those techniques, with supplement use in qualification limited to tool qualification levels 1 through 4.
- **Field-loadable software (FLS) and user-modifiable software (UMS) add-ons (sections 8.b, 8.c).** Project-level supplements to both B and C editions: protect load integrity, verify loaded part numbers, prevent inadvertent load enable in critical phases; keep the modifiable part at least at the assigned software level; feed the system-level guidance items the standard already lists.
- **Legacy modify/reuse flow (section 9).** Usage-history and level checks first; change impact analysis (CIA) when modifications are required; tool path when tools change; optional stay-on-original-edition modifications under tight conditions; baseline upgrade to ED-12C/DO-178C when those conditions fail or when equivalence is declared.

## Key Concepts

- **Harmonisation note.** Section 4.b states the technical content is, as far as practicable, harmonised with FAA AC 20-115D, which is also based on ED-12C/DO-178C. This pack stays on the EASA AMC text; the FAA twin lives in faa-8110-49.
- **Section 5 continuation criteria (all must hold).** (1) No known process deficiencies that leave B-era objectives unsatisfied (evidence of closed process OPRs and audit findings may be requested). (2) Prior certified use at a software level at least as high as the new software. (3) If model-based development, object-oriented technology, or formal methods will be used, EASA already accepted those process embeddings on a prior certified project (CRI or CM path). (4) Parameter data item (PDI) / configuration-data processes likewise previously accepted, or new PDI processes established under ED-12C/DO-178C. (5) No significant changes to the plans or the development environment (supported by change analysis). (6) No intent to declare the new software as having satisfied ED-12C/DO-178C. If any criterion fails, upgrade processes and develop under ED-12C/DO-178C; tool qualification follows section 12.2 of that standard and paragraph 10 of this AMC (see ch04).
- **Section 6 data duties.** The applicant plans and executes activities for every applicable objective, including supplement and tool-qualification objectives where they apply. Life cycle data specified for certification liaison is submitted; type-design-related data follows the standard's rules (design description and source code are not type-design data for Level D). Broader life cycle data, tool data, and supplement outputs are made available on request.
- **CS-specific level mapping.** A published AMC to a specific CS that ties system criticality to software level takes precedence over the generic mapping in the recognised standard.
- **Multiple supplements.** Using more than one technique means more than one supplement applies. Simulation used to satisfy model-based review/analysis objectives needs explicit identification of which objectives simulation covers and a detailed justification that simulation (alone or with reviews/analyses) fully satisfies each one.
- **FLS protections.** Corruption and partial-load protection at integrity matching the FLS software level; verifiable loaded part number; protection against inadvertent enable of field loading during cruise or other safety-critical phases; developer-supplied information for the system-level FLS items in the recognised standard.
- **UMS constraints.** Developer-supplied information for the system-level UMS items; the modifiable portion developed at a software level at least as high as the level assigned to that software.
- **Legacy software definition.** Previously approved software or components approved under ED-12/DO-178, ED-12A/DO-178A, or ED-12B/DO-178B.
- **Usage history gate (9.b.1).** Assess service difficulties, airworthiness directives, and OPRs with potential safety impact; plan resolution of related software deficiencies; correct related development-process deficiencies before modify/reuse.
- **Software level relationship (9.b.2).** System safety assigns the minimum development assurance level from failure-condition severity. B-era and C-era software levels align. Earlier editions used different labels; the AMC's Table 1 maps legacy labels to assigned A/B/C/D. Acceptable intersections keep the legacy level; blank intersections require baseline upgrade (processes, procedures, and tool qualification) under the paths in 9.b.2.a-c. Original summary of that relationship (see ED-12C/DO-178C, not reproduced for objective detail):

| Assigned level | ED-12B legacy | ED-12A legacy | ED-12 legacy |
|----------------|---------------|---------------|--------------|
| A | A only | Level 1 only | Critical only (and only if previously accepted as Level A-equivalent where the AMC requires that prior acceptance) |
| B | A, B | Level 1, 2 | Critical, Essential (Essential remains acceptable for Level B if previously accepted as such) |
| C | A, B, C | Level 1, 2, 3 | Critical, Essential, Non-Essential |
| D | A, B, C, D | Level 1, 2, 3 | Critical, Essential, Non-Essential |

Exact checkmarks are in the AMC Table 1; use the official table for a certification decision. Unassessed ED-12 Essential software, or any unacceptable level, forces baseline upgrade via the C-era change path and ED-215/DO-330.

- **Unmodified reuse (9.b.3).** If history and level gates pass and no modifications are required, the original approval may serve as the basis for the proposed installation. If the baseline was upgraded to ED-12C/DO-178C (processes and tool qualification included), the applicant may declare software equivalence to ED-12C/DO-178C, but cannot declare unmodified tools equivalent; all later changes use the C-era processes.
- **CIA when modifying (9.b.4).** Identify changes; run the change analyses the recognised standard associates with software change; perform the verification the CIA indicates; summarise CIA results in the PSAC or the software accomplishment summary (SAS).
- **Tools on legacy paths (9.b.5).** New or changed tools route to paragraph 10 (ch04).
- **Stay on original edition (9.b.7-8).** Allowed for modifications only if: technique processes (MBD/OOT/FM) were previously EASA-accepted when those techniques are used; plans, processes, and life cycle environment remain maintained and usable; and the applicant will not declare ED-12C/DO-178C satisfaction. Configuration data / PDI then uses a previously accepted process or a new ED-12C/DO-178C PDI process. Failing any 9.b.7 condition forces full process upgrade and C-era modification under the standard's change section, with the same equivalence limits on unmodified tools (9.b.9).

## Mental Models

- The AMC is a process gatekeeper around a recognised standard, not a second objective catalogue. When you need the objective list, open ED-12C/DO-178C (see ED-12C/DO-178C, not reproduced).
- Section 5 is a six-lock door. One open lock (deficiency, lower prior level, unaccepted technique, missing PDI process, environment churn, or intent to claim C-era satisfaction) moves the project onto ED-12C/DO-178C.
- Equivalence declarations attach to software baselines and processes, not to untouched legacy tools. Tool claims need their own qualification path (ch04).
- CIA is the hinge between "reuse as approved" and "change under control." No CIA, no controlled modification story in the PSAC/SAS.
- Staying on a pre-C edition is a deliberate non-claim: you keep the old processes only while you refuse the C-era declaration and keep the environment alive.

## Anti-patterns

- **Reproducing Annex A objective tables in plans or in this pack.** The AMC points at them; it does not copy them. Mark any summary column that would need the paywalled text as `see ED-12C/DO-178C, not reproduced`.
- **Continuing B-era processes while planning to declare C-era satisfaction.** Criterion 5.a.6 forbids that combination.
- **Dropping a technique supplement in as a stand-alone MoC.** Supplements ride with ED-12C/DO-178C; the PSAC must show the joint application.
- **Using simulation for model-based review objectives without saying which objectives and why simulation fully covers them.** Section 8.a.3 requires both the list and the justification.
- **Loading FLS without integrity, part-number verification, or critical-phase enable protection.** Section 8.b treats those as required add-ons.
- **Reusing legacy software with open safety-related service history and no resolution plan.** Section 9.b.1 blocks that path.
- **Declaring unmodified legacy tools equivalent to ED-215/DO-330 after a software baseline upgrade.** The AMC repeatedly separates software equivalence from tool equivalence.

## Key Takeaways

1. Software assurance under this AMC is life cycle process assurance: planning, development, verification, configuration management, quality assurance, and certification liaison, expressed as objectives, activities, and evidence in the recognised standards (not reprinted here).
2. Established ED-12B/DO-178B processes may continue for new development only when all six section 5 criteria hold; otherwise develop under ED-12C/DO-178C.
3. Using ED-12C/DO-178C means satisfying every applicable objective for the software level, producing the life cycle data, submitting liaison data, and honouring any CS-specific level-mapping AMC.
4. Technique supplements apply with the primary document through the PSAC (and TQP when tools use those techniques); FLS and UMS carry extra integrity and level constraints.
5. Legacy modify/reuse runs through usage history, level relationship (AMC Table 1), optional unmodified reuse, CIA-driven modification, and a narrow stay-on-original-edition path; tool changes go to paragraph 10.
6. Software equivalence declarations after baseline upgrade do not make unmodified tools equivalent; subsequent software and tool changes use C-era processes.

## Connects To

- **ch02** - purpose, applicability (product and ETSO), and replacement of AMC 20-115C that open this assurance model.
- **ch04** - tool qualification (paragraph 10) and GM1-GM3 practices for CIA, data/control coupling, and design-level error handling.
- **ch07** - PSAC/SAS and joint software-hardware planning interfaces that carry CIA summaries and supplement application descriptions.
- **faa-8110-49** - FAA-side twin material where harmonisation with AC 20-115D matters; not a substitute for this AMC text.

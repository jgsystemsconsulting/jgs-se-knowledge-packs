# Chapter 3 - Level of FAA Involvement

Sources: FAA Order 8110.49A, Software Approval Guidelines (effective 2018-03-29), Chapter 2 paragraph 2.b (LOI criteria; printed page 2-2) and Appendix A, Level of Involvement Worksheets 1-3 (printed pages A-1 to A-4).

## Core Idea

Level of FAA involvement (LOI) is how much certification-authority attention a software project receives. Order 8110.49A requires that involvement be determined and documented as early as practicable in the life cycle. Appendix A supplies three example worksheets the authority or a designee may use to turn software level, project attributes, applicant track record, and designee capacity into a LOW / MEDIUM / HIGH call. The worksheets are examples only: criteria may not fit every project, and use of any worksheet, alone or combined, is not mandatory.

## Frameworks Introduced

- **Eight LOI factors (Chapter 2 paragraph 2.b).** Software level from the system safety assessment; product attributes (size, complexity, system functionality or novelty, software design); new technologies or unusual design features; novel software methods or life cycle models; the applicant's experience satisfying DO-178B/C objectives; availability, experience, and authorization of designees; issues tied to DO-178B/C Section 12; and applicability of software-specific issue papers.
- **Worksheet 1 - software level band.** Maps DO-178B/C software level to a default involvement band: Level D to LOW; Level C to LOW or MEDIUM; Levels B and A to MEDIUM or HIGH.
- **Worksheet 2 - scored project criteria.** Five criterion groups on MIN/mid/MAX scales that produce a Total Score Result (TSR): (1) applicant/developer software certification experience; (2) demonstrated software development capability; (3) software service history; (4) current system and software application attributes; (5) designee capabilities.
- **Worksheet 3 - combine TSR with software level.** Converts the Worksheet 2 TSR and the project's software level into LOW / MEDIUM / HIGH. Higher scores (stronger experience, cleaner history, stronger designees, less novelty) push involvement down within the level's band; lower scores push it up.

## Key Concepts

- **LOI is not a pass/fail gate.** It sizes authority attention. The certification basis and DO-178B/C objectives still apply at every involvement level.
- **Worksheet 1 bands (from the printed table).** Level D: LOW. Level C: LOW or MEDIUM. Level B: MEDIUM or HIGH. Level A: MEDIUM or HIGH.
- **Worksheet 2 group 1 - certification experience (project counts drive the scale).** Civil aircraft or engine certification (0 / 3-5 / 6+ projects map to 0 / 5 / 10); DO-178B/C experience (0 / 2-4 / 5+ map to 0 / 5 / 10); DO-178 or DO-178A experience (0 / 4-6 / 7+ map to 0 / 3 / 5); other software standards (0 / 4-6 / 7+ map to 0 / 2 / 4).
- **Worksheet 2 group 2 - demonstrated capability.** Ability to produce DO-178B/C software products consistently; cooperation, openness, and resource commitments; ability to manage software development and subcontractors; capability assessments (for example SEI CMM or ISO 9001); development-team average relevant experience (including a tenure-style scale at one row).
- **Worksheet 2 group 3 - service history and quality posture.** Software-related problem incident rate as a percentage of affected products (worse rates score lower); management support of designees; software QA organization and configuration management process quality; company stability and commitment to safety; success of past certification efforts.
- **Worksheet 2 group 4 - this application.** Complexity of system architecture, functions, and interfaces (high complexity scores low); complexity and size of the software and safety features; novelty of design and use of new technology (more novelty scores lower); software development and verification environment; use of alternative methods or additional considerations.
- **Worksheet 2 group 5 - designee side.** Designee DO-178B/C experience by project count; authority, autonomy, and independence; cooperation, openness, and issue-resolution effectiveness; relevance of assigned experience; current workload (high workload scores low); experience with other software standards.
- **Worksheet 3 layout (reconstructed from the A-4 table).** Approximate bands: TSR below 80 yields Level A HIGH, Level B HIGH, Level C MEDIUM, Level D LOW; TSR between 80 and 130 yields Level A HIGH, Level B MEDIUM, Level C MEDIUM, Level D LOW; TSR above 130 yields Level A MEDIUM, Level B MEDIUM, Level C LOW, Level D LOW. Use the printed worksheet on a live project; this note is a reading aid, not a substitute table.
- **Optional, not mandatory.** Appendix A states the worksheets may contain inapplicable criteria and that individual or combined use is not required. Staff may document LOI another way as long as it is early, explicit, and reasoned from the eight factors.

## Mental Models

- Start from software level (Worksheet 1), then let evidence about people, history, and novelty move you inside the band (Worksheets 2-3).
- Score direction matters: on novelty and complexity rows, high complexity or much novelty sits at the MIN end of the scale. Experience and clean service history sit at the MAX end. Read each row's MIN/MAX labels before adding points.
- Designee strength can lower needed FAA hands-on time; designee overload or weak autonomy can raise it. LOI is a joint function of product risk and oversight capacity.
- Document the call when the project is still flexible. Late LOI either under-protects novel work or burns review effort after plans are frozen.

## Anti-patterns

- **Treating Worksheet 1 as the whole answer.** Level alone gives a band; Worksheet 2 exists to refine inside that band.
- **Using the worksheets as mandatory checklists.** The order marks them examples; forcing inapplicable criteria invents precision the source does not claim.
- **Scoring novelty as a bonus.** On Worksheet 2 group 4, more novelty and higher complexity reduce the score and raise involvement. Inverting the scale understates risk.
- **Ignoring designee workload and autonomy.** Group 5 is part of the TSR. A strong product team with an overloaded or narrowly authorized designee is not automatically LOW involvement.
- **Leaving LOI oral.** Paragraph 2.b requires determination and documentation; an undocumented plan to figure it out at the first review fails the order's timing rule.

## Key Takeaways

1. Set and document LOI as early as practicable; eight Chapter 2 factors shape both LOI and the resulting review program.
2. Appendix A offers three example worksheets; they are optional aids, not mandatory forms.
3. Worksheet 1 bands LOI by software level (D low; C low/medium; A and B medium/high).
4. Worksheet 2 scores experience, capability, service history, application attributes, and designee capacity into a TSR.
5. Worksheet 3 combines TSR with software level into LOW / MEDIUM / HIGH; higher TSR lowers involvement inside the level's band.
6. LOI sizes authority attention; it does not waive objectives or the certification basis.

## Connects To

- **ch01** - orientation: where LOI sits in the Order 8110.49A versus AC 20-115D division of labor.
- **ch02** - software review process whose scope and count depend on the LOI this chapter sets.
- **ch04** - conformity inspection intensity and ASE/ASI tasking still assume an agreed involvement posture.
- **ch05** - applicant process maturity under AC 20-115D (prior DO-178B use, tool qualification state) feeds the same experience and novelty factors LOI scores.

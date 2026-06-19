# Chapter 2: Implementing Human Systems Integration

## Core Idea
HSI implementation is governed by three interlocking NASA Technical Authorities (TAs), executed through the program/project (P/P) management structure, and depends on sustained collaboration between HSI practitioners, systems engineers, and domain SMEs via Integrated Product Teams (IPTs).

## Frameworks Introduced
- **Three-TA Governance Model**: NASA HSI authority spans three institutional TAs — Engineering (ETA via OCE), Safety and Mission Assurance (SMA TA via OSMA), and Health and Medical (HMTA via OCHMO). Each TA covers overlapping aspects of HSI domains.
  - When to use: When navigating P/P decisions that cross HSI domain boundaries or require institutional sign-off; particularly for human-rated programs where HMTA delegates are assigned as HSI leads.
- **Control Board Participation**: HSI practitioners and institutional TAs reach agreements on P/P issues through formal control boards (element-level, vehicle-level, program-level).
  - When to use: For large, complex programs (e.g., ESD) where multi-level boards coordinate cross-program HSI concerns.

## Key Concepts
- **Programmatic Authority**: NASA mission directorates that fund and create P/Ps; their funded personnel (civil servants and prime contractor staff) are the primary resources for executing HSI work.
- **Institutional Authority (Technical Authority / TA)**: Cross-cutting technical offices (OCE, OSMA, OCHMO) whose personnel provide skills, facilities, and technical oversight separate from programmatic goals. HSI must navigate the healthy tension between programmatic risk appetite and institutional safety standards.
- **Engineering Technical Authority (ETA)**: Delegated from the Agency's Chief Engineer through the OCE; primary TA documents for HSI are NPR 7123.1B and the SEHB.
- **Health and Medical Technical Authority (HMTA)**: Delegated from the CHMO; maintains NASA-STD-3001 and the HIDH. For human space flight, the JSC CMO serves as HMTA for all centers; delegates are typically assigned as the program-funded HSI leads.
- **Safety and Mission Assurance Technical Authority (SMA TA)**: Manages NPR 8705.2B; requires a formal HSI team to be formed before SRR for human-rated programs.
- **Integrated Product Team (IPT)**: The primary collaboration vehicle within a P/P. HSI practitioners must participate in relevant IPTs and Working Groups (WGs) beginning in Phase A to provide timely human-centered input.
- **HSI Tools and Models**: Analytical tools selected by the HSI team to support life-cycle work, including human error analysis (CREAM), workload assessment (NASA TLX), usability (SUS), task analysis, and physiological/medical models. Tools must be validated per NASA-STD-7009.
- **SEMP (Systems Engineering Management Plan)**: The primary top-level technical management document for a P/P; HSI Plan may be a section within the SEMP or a standalone document.

## Mental Models
- Use programmatic channels (IPTs, working groups) for daily HSI influence on design; use TA channels for institutional compliance and risk escalation when programmatic decisions threaten safety margins.
- Use the three-TA model to identify who holds approval authority over each category of HSI issue: engineering design (ETA), safety risk (SMA TA), or health and medical (HMTA).
- Select HSI tools before the HSI Plan is baselined, so budget and schedule are allocated for tool application; tools that produce outputs suitable as inputs to other P/P tools maximise collaboration value.

## Anti-patterns
- **Bypassing TA involvement**: The Constellation Program case study shows that "influence leadership" without top-down authority from TA channels limits HSI's ability to drive integrated design decisions.
- **Treating HSI tools as optional embellishments**: Tools must be planned and budgeted in the HSI Plan from Pre-Phase A; ad hoc tool adoption in later phases cannot produce the analytical depth needed for V&V.

## Key Takeaways
1. NASA HSI authority is distributed across three TAs (ETA, SMA TA, HMTA) whose domains overlap with all HSI domains — the HSI practitioner must navigate all three.
2. Program HSI work is funded and executed by programmatic resources (civil servants, prime contractor), while institutional TAs provide technical oversight and standards enforcement.
3. The HSI practitioner's primary collaboration vehicles are IPTs and WGs; participation must begin in Pre-Phase A for ConOps development and continue throughout the life cycle.
4. HSI teams for human-rated programs are mandated by NPR 8705.2B to form before SRR; for all other programs, formation is recommended from Pre-Phase A.
5. Analytical tools must be validated per NASA-STD-7009 and their selection documented in the HSI Plan, including budget provisions for the necessary SMEs.
6. The healthy tension between programmatic goals (accomplish mission) and institutional standards (protect safety) is inherent to NASA's governance model; the HSI practitioner manages this balance.

## Connects To
- **NPR 7123.1B**: Defines ETA authority and HSI Plan requirement.
- **NPR 8705.2B** (Human-Rating Requirements): Defines SMA TA authority; requires HSI team before SRR for human-rated programs.
- **NPR 7120.11** (HMTA Implementation): Defines HMTA authority and delegation structure.
- **NASA-STD-3001**: Primary HMTA standard maintained with involvement of all three TAs for Volume 2.
- **NASA-STD-7009** (Standard for Models and Simulations): Validation/accreditation requirement for HSI analytical tools.

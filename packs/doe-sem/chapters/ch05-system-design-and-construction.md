# Chapter 5: System Design and Construction Stages

## Core Idea
System Design converts the functional baseline into physical/technical design — architecture, components, data structures, interfaces, and construction-ready specifications. Construction (formerly Programming) builds the system using consistent, maintainable techniques under configuration management and ongoing quality reviews.

## Frameworks Introduced
- **System Design stage**: Physical/technical design work products and interface specifications sized to the project.
- **Construction stage**: Implementation of designed components, unit-level verification, and integration preparation.
- **CM-controlled construction**: Work products and code/config baselines tracked per the CM plan from planning.

## Key Concepts
### System Design
- **Purpose**: Specify how the functional design will be realized — platforms, modules, data design, internal/external interfaces, security and operability considerations appropriate to DOE IT context.
- **Activities**: Elaborate architecture; detailed design of components; update traceability; prepare construction and test scaffolding; review for feasibility, maintainability, and requirement coverage.
- **Exits**: Design baseline approved via Stage Exit before major construction spend.
- **COTS note**: When commercial products are selected, design must account for proprietary interfaces and long-term maintenance cost trade-offs called out in SEM discussions of alternatives.

### Construction
- **Rename significance**: “Construction” signals broader IT build (including configuration of platforms/packages), not only custom coding.
- **Activities**: Implement components to design; conduct unit tests; perform walkthroughs on critical work products; maintain CM baselines; track defects against requirements/design.
- **Quality**: Peer reviews catch construction defects early; In-Stage Assessments verify process adherence and deliverable completeness; Stage Exit authorizes entry to Integration and Testing.
- **Maintainability**: SEM premise that consistent construction techniques reduce lifecycle cost — coding standards, reusable patterns, and documentation are in scope.

## Mental Models
- System Design is the last cheap place to fix architectural mistakes; construction is where cost-of-change climbs.
- Construction without a design baseline is prototyping forever.
- CM is how multiple builders stay coherent; treat branches/baselines as SEM configuration items even in modern VCS.
- COTS construction is mostly integration and configuration — still needs design, CM, and review.

## Anti-patterns
- **Coding against unbaselined design drafts**: Guarantees thrash and failed exits.
- **No unit verification before integration**: Pushes defects into the most expensive test stage.
- **Orphan configuration** (undocumented environment builds): Breaks installation/acceptance later.
- **Ignoring proprietary lock-in accepted in design**: Maintenance stage pays the bill.

## Key Takeaways
1. System Design produces the physical/technical baseline for build.
2. Traceability and interface specs must stay current through design.
3. Construction implements the design with maintainable, consistent techniques.
4. Unit-level verification and peer reviews belong inside Construction, not only later test.
5. CM baselines bind design and construction work products.
6. Stage Exits prevent unauthorized progression into integration/test.

## Connects To
- **ch04**: Functional baseline feeding system design.
- **ch06**: Integration/testing and acceptance consume construction outputs.
- **ch02**: Walkthrough/assessment/exit pattern during build.
- **ch07**: Maintainability debt created or avoided here.

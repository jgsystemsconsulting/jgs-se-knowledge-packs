# Chapter 7: Project Viewpoint (PV)

## Core Idea
The Project Viewpoint is DoDAF's integration point with **portfolio management and acquisition**. PV models describe how programs, projects, portfolios, and initiatives deliver capabilities — linking architecture models to DAS, PPBE, and CPM processes through the Work Breakdown Structure (WBS) and project scheduling constructs. Projects in the DM2 are themselves activities: they produce resources (systems, services, persons in roles, facilities) that are then used to perform types of activities in an operational architecture.

## Frameworks Introduced
- **PV-1: Projects and Organizations**: Identifies individual organizations and individual projects, and the relationships between them. Hierarchical project and organizational structures are modeled using whole-part relationships. One sort of PV-1 model is a WBS.
  - When to use: When mapping who is responsible for what in the delivery of architectural products; for acquisition milestone management; for linking architecture to the WBS.
- **PV-2: Project Schedules**: Shows the temporal structure of projects — before-after relationships, milestone overlaps, schedule dependencies. May incorporate organizations from PV-1. One sort of PV-2 model is a Gantt Chart.
  - When to use: When analyzing project timelines, schedule dependencies, and milestone-resource relationships; to show how budget years (happens-in) relate to project temporal parts.
- **PV-3: Projects and Capabilities**: Maps projects to the capabilities they deliver; shows which program elements contribute to which capabilities.
  - When to use: When performing capability gap analysis in conjunction with portfolio management; to trace PPBE program elements to CV-defined capability requirements.

## Key Concepts
- **Project (DM2)** — A temporary endeavor (a type of individual activity) undertaken to create desired states of resources. Projects have whole-part, temporal whole-part, and super-subtype relationships; major projects contain minor projects, projects have time phases, and projects can be categorized.
- **Work Breakdown Structure (WBS)** — A product-oriented family tree of hardware, software, services, data, and facilities. The primary instrument connecting an architecture description to DAS and PPBE. Required by DoD Instruction 5000.2; governed by MIL-STD-881C.
- **Program Element (PE)** — The basic building block of the Future Years Defense Program (FYDP). Describes program mission and identifies the responsible organization; may consist of forces, manpower, materiel, services, and associated costs.
- **Milestone** — In PV-2, the overlap between a project temporal boundary (end of one part / start of another) and a resource state produced by a project part. Milestones have cardinal and physical measures.
- **Earned Value Management** — WBS-based reporting required by ANSI/EIA 748; PV data supports contractor cost data reports, software resource data reports, and contract performance reports.
- **happensIn Relationship** — A DM2 relationship associating project temporal parts with interesting time periods (e.g., budget years); enables schedule-to-PPBE cycle alignment.
- **Before-After Relationship** — A DM2 temporal ordering relationship used in PV-2 to sequence project temporal parts and model schedule dependencies.
- **PV-1 Existence Predicate** — The mandatory constraint on PV-1: for every organization-project pair modeled, the organization must perform a project that produces guidance or resources identified by other DoDAF viewpoint models. PV-1 may not introduce new guidance or resources.

## Mental Models
- Use PV-3 to close the loop between planning and delivery: CV tells you what capabilities are needed; PV-3 tells you which projects are delivering them; PV-2 tells you when they will be delivered.
- Use PV-1 as the architectural WBS: it is not just a management artifact — it connects architecture activities and performers to contract requirements and cost structures.

## Anti-patterns
- Using PV-2 to introduce new projects: PV-2 only temporally decomposes projects already established in PV-1; it may not add new projects. The existence predicate governs PV-1; PV-2 is strictly derivative.
- Confusing PV-1 organizational structure with operational structure: PV-1 shows organizations responsible for project execution, not the operational hierarchy shown in OV-4.
- Treating PV as a standalone project management tool: PV models are meaningful only in the context of the overall architectural description; PV-3 is only as good as the CV capability map it references.

## Key Takeaways
1. Projects are activities in the DM2 — the same producer-consumer resource-flow mechanics that govern all activities apply to projects, which produce the performers and resources used by other activities.
2. The WBS is the architectural artifact that bridges DAS and PPBE to the architecture — MIL-STD-881C is the authoritative reference.
3. PV-1 carries an existence predicate: every project modeled must produce something traceable to other viewpoint models.
4. PV-3 provides the capability traceability chain: program elements → projects → capabilities. Without it, portfolio investment decisions cannot be linked to operational needs.
5. Measures and rules can be attached at any level of the project decomposition, enabling earned value tracking and compliance tracking throughout the WBS hierarchy.

## Connects To
- **Chapter 4 (Capability Viewpoint)**: PV-3 provides the project-to-capability mapping that closes the loop between CV requirements and delivery.
- **Chapter 6 (Operational Viewpoint)**: Organizations in PV-1 are types also found in OV-4; the same organizational structures appear in both viewpoints.
- **Chapter 9 (Services Viewpoint)**: Services-as-a-service can be portfolio items; SvcV models detail what the service does, PV-1/PV-3 show how projects deliver it.
- **Chapter 11 (Systems Viewpoint)**: SV-8 (Systems Evolution) is the system-level complement to PV-2 — both address temporal transitions, but SV-8 focuses on technology migration while PV-2 focuses on delivery schedules.

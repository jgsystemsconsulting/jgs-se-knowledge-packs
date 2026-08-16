# Chapter 8: T&E Strategy, TEMP, Test Plans, and STE Planning

## Core Idea
Documentation turns enterprise intent into executable, approvable T&E. The guidebook centers a T&E Strategy (often realized via TEMP and related artifacts), supporting test plans, and the resources/environments (including STE—system test & evaluation environments/infrastructure) needed to produce decision-quality evidence.

## Frameworks Introduced
- **T&E Strategy spine**: Describes how T&E will produce knowledge for decisions across CT/DT/OT/LFT; updated as requirements and pathway phase change.
- **TEMP as common vehicle**: Developmental and operational test planning content, schedules, resources, and evaluation frameworks live in the TEMP (or pathway-equivalent strategy docs).
- **Test plans**: Event-level plans decompose the Strategy; oversight programs face DOT&E approval regimes for relevant OT/LFT plans.

## Key Concepts
- **Upstream feeders**: Capabilities docs, CONOPS/OMS/MP, system specs, threat assessments, and engineering plans feed Strategy content.
- **IDSK / data strategy thinking**: Identify data required, sources (CT/DT/OT/LFT/M&S), analytics, and repository access for independent assessment.
- **STE / resources**: Facilities, ranges, threat representations, instrumentation, M&S, personnel, test articles, and automation tools must be explicit—wishful resources fail sufficiency and OTRR.
- **Approval paths**: Decision Authority / Component / DOT&E / USD(R&E) roles depend on pathway and oversight status; software pathway examples include DA approval before execution and DOT&E final approval when on oversight.
- **Integrated schedule**: Show concurrency risks between DT and production and how test tempo supports milestone/fielding decisions.
- **Cyber and reliability content**: Strategy should resource lifecycle cyber T&E and reliability/suitability evidence, not only performance KPP shots.

## Mental Models
- **A TEMP nobody resources is fiction.**
- **Oversight status is a header field that rewires the approval graph.**

## Anti-patterns
- Copy-pasting a prior TEMP without pathway/oversight tailoring.
- Hiding STE shortfalls until after Strategy approval.
- Writing OT plans that assume data rights the contract never bought.

## Key Takeaways
1. Strategy/TEMP is the enterprise planning spine for multi-community T&E.
2. Test plans and STE/resources make the Strategy executable.
3. Data/IDSK thinking enables independent assessment and reuse.
4. Approvals follow pathway + oversight rules; keep docs living.

## Connects To
- **ch01**: Who approves what.
- **ch02–ch04**: Community content inside the Strategy.
- **ch05–ch07**: Cross-cutting cyber/MOSA/suitability resource needs.
- **dod-te-guidebook**: Deeper pathway-specific Strategy patterns.

# Capability to Knowledge-Pack Map

Working artifact mapping systems-engineering **technical capabilities** to the pack chapters that provide
“what good looks like” reference depth for each capability. Intended as input for SE role-agent skill generation.

Rules of construction:
- Every chapter in every pack under `packs/<slug>/chapters/` is assigned to exactly one capability cluster (best fit).
- Cross-cutting chapters carry a remark noting the strong secondary fit.
- `glossary.md` / `patterns.md` / `cheatsheet.md` are included (marked “support file”) only for packs that are
  essentially single-cluster; multi-cluster packs' support files are omitted as ambiguous.
- The two signpost packs (`omg-signpost`, `se-standards-signpost`) contain no chapters and are not mapped.
- A standard's own process definitions go to cluster 30; performing the capability goes to the capability cluster.
- Machine-readable version: `docs/capability-pack-map.json`.
- Changelog (v1.17.0): added `nist-800-171`, `nist-800-61`, `cisa-cpg`, `doe-sem`, `mil-hdbk-338`, `mil-hdbk-516`, `nasa-ms-7009`, and `doe-o-413-3` (this pack was renamed from `doe-413-3b`; same content, new slug).

## Summary

| Cluster | Entries |
|---|---|
| 1. Systems Thinking & Fundamentals | 25 |
| 2. Requirements Engineering | 19 |
| 3. Requirements Traceability & Allocation | 2 |
| 4. Architecture & Design | 20 |
| 5. Interface Management & ICIDs | 2 |
| 6. Integration | 3 |
| 7. Verification | 9 |
| 8. Validation | 3 |
| 9. Test & Evaluation | 11 |
| 10. Modeling, MBSE & SysML | 16 |
| 11. Digital Engineering & Digital Twins | 24 |
| 12. Configuration Management & Baselines | 14 |
| 13. Data & Information Management | 6 |
| 14. Risk Management | 26 |
| 15. Opportunity/Benefit Management | 1 |
| 16. Decision Analysis & Trade Studies | 2 |
| 17. Technical Planning & Work Breakdown | 6 |
| 18. Measurement & Technical Assessment | 36 |
| 19. Quality Assurance & Process Compliance | 3 |
| 20. Safety, Reliability & Survivability | 88 |
| 21. Cybersecurity & Security Engineering | 68 |
| 22. Human Systems Integration / Human Factors | 26 |
| 23. Logistics, Supportability & Sustainment | 11 |
| 24. Operations, Maintenance & Disposal | 6 |
| 25. Training & Documentation Delivery | 0 |
| 26. Project/Program Management | 66 |
| 27. Supplier, Procurement & Acquisition | 7 |
| 28. Stakeholder Engagement & Needs | 3 |
| 29. Governance, Reviews, Gates & Control Points | 17 |
| 30. Standards, Tailoring & Process Models | 35 |
| 31. Specialty Engineering | 7 |
| 32. Assurance & System Assurance | 8 |
| **Total** | **570** |

## 1. Systems Thinking & Fundamentals

| Pack | Chapter | Why it fits / one-line value |
|---|---|---|
| dau-se-guidebook | ch01-introduction.md | SE orientation across the defense acquisition life cycle |
| dau-se-guidebook | ch02-system-level-considerations.md | SoS, digital eng, value/sustainability engineering at system level |
| doe-sem | ch01-sem-purpose-and-context.md | DOE SEM/SDLC purpose, scope, and CMM alignment orientation |
| faa-sem | ch01-faa-sem-introduction-ams-lifecycle.md | FAA SEM and AMS lifecycle orientation |
| nasa-se-expanded | ch01-nasa-se-expanded-fundamentals-and-se-engine.md | SE fundamentals and the SE engine |
| nasa-se-handbook | ch01-2-0-fundamentals-of-systems-engineering.md | SE fundamentals |
| nasa-se-handbook | ch03-2-3-example-of-using-the-se-engine.md | Worked SE engine example |
| nist-cps | ch01-nist-cps-introduction-and-what-makes-cps-different.md | What makes cyber-physical systems different |
| nist-cps | ch02-nist-cps-framework-facets-aspects-concerns.md | CPS framework: facets, aspects, concerns |
| nist-cps | ch07-nist-cps-use-case-analysis-method.md | Use-case analysis method for CPS concerns |
| sebok | ch01-sebok-introduction.md | SEBoK orientation |
| sebok | ch02-sebok-se-fundamentals.md | SE fundamentals |
| sebok | ch03-sebok-nature-of-systems.md | Nature of systems |
| sebok | ch04-sebok-systems-science.md | Systems science |
| sebok | ch05-sebok-systems-thinking.md | Systems thinking |
| sebok | ch07-sebok-systems-approach-engineered.md | Systems approach applied to engineered systems |
| sebok | ch20-sebok-applications-overview.md | SE applications overview |
| sebok | ch21-sebok-product-systems-engineering.md | Product SE context |
| sebok | ch22-sebok-service-systems-engineering.md | Service systems SE context |
| sebok | ch23-sebok-enterprise-systems-engineering.md | Enterprise SE context |
| sebok | ch24-sebok-systems-of-systems.md | Systems of systems SE |
| sebok | ch25-sebok-healthcare-systems-engineering.md | Healthcare SE context |
| sebok | ch32-sebok-se-software-engineering.md | SE and software engineering relationship |
| sebok | ch35-sebok-implementation-examples.md | Implementation examples |
| sebok | ch36-sebok-emerging-knowledge.md | Emerging SE knowledge |

## 2. Requirements Engineering

| Pack | Chapter | Why it fits / one-line value |
|---|---|---|
| doe-sem | ch04-requirements-and-functional-design.md | Requirements definition and functional design stages with RTM (also architecture) |
| faa-req-handbook | ch01-faa-req-handbook-foundations-and-introduction.md | Requirements foundations |
| faa-req-handbook | ch02-faa-req-handbook-system-overview-and-boundary.md | System overview and boundary definition |
| faa-req-handbook | ch03-faa-req-handbook-operational-concepts-and-environmental-assumptions.md | ConOps and environmental assumptions (also stakeholder needs) |
| faa-req-handbook | ch05-faa-req-handbook-system-modes-and-detailed-requirements.md | Modes and detailed requirement statements |
| faa-req-handbook | ch07-faa-req-handbook-rationale-and-summary.md | Requirement rationale capture |
| faa-req-handbook | ch08-faa-req-handbook-worked-avionics-examples.md | Worked requirement-writing examples |
| faa-sem | ch03-faa-sem-requirements-architecture-crosscutting.md | Requirements and architecture crosscutting topics |
| gao-agile | ch05-gao-agile-requirements-development-management.md | Requirements development/management in Agile |
| nasa-se-handbook | ch18-4-2-technical-requirements-definition.md | Technical requirements definition |
| nasa-se-handbook | ch28-6-2-requirements-management.md | Requirements management (also traceability) |
| requirements-writing | ch01-quality-characteristics.md | Requirement quality characteristics |
| requirements-writing | ch02-ears-overview.md | EARS syntax overview |
| requirements-writing | ch03-ears-patterns.md | EARS sentence patterns |
| requirements-writing | ch04-applying-ears.md | Applying EARS to system requirements |
| requirements-writing | ch05-defects-and-anti-patterns.md | Requirement defects and anti-patterns |
| requirements-writing | cheatsheet.md (support file) | Cheatsheet / quick reference |
| requirements-writing | glossary.md (support file) | Glossary for the pack |
| requirements-writing | patterns.md (support file) | Patterns/practice heuristics |

## 3. Requirements Traceability & Allocation

| Pack | Chapter | Why it fits / one-line value |
|---|---|---|
| faa-req-handbook | ch06-faa-req-handbook-software-requirements-and-subsystem-allocation.md | Software requirements and subsystem allocation |
| requirements-writing | ch06-verifiability-and-traceability.md | Verifiability and traceability of requirements (also verification) |

## 4. Architecture & Design

| Pack | Chapter | Why it fits / one-line value |
|---|---|---|
| dau-se-guidebook | ch06-design-considerations.md | Design-solution considerations incl. open systems and resiliency |
| dod-mosa | ch01-dod-mosa-introduction-and-policy.md | MOSA policy context and intent |
| dod-mosa | ch02-dod-mosa-pillars-and-benefits.md | MOSA pillars (modularity, key interfaces, standards) |
| dod-mosa | ch04-dod-mosa-technical-considerations.md | Design rules for modular open architectures |
| dod-mosa | ch07-dod-mosa-implementation-appendices.md | Implementation guidance and appendices |
| dodaf | ch01-introduction-and-dodaf-concepts.md | DoDAF framework concepts and viewpoint structure |
| dodaf | ch03-all-viewpoint-av.md | All-Viewpoint: overarching architecture info |
| dodaf | ch04-capability-viewpoint-cv.md | Capability viewpoint products |
| dodaf | ch06-operational-viewpoint-ov.md | Operational viewpoint: activities and exchanges |
| dodaf | ch08-services-viewpoint-svcv.md | Services viewpoint products |
| dodaf | ch10-systems-viewpoint-sv.md | Systems viewpoint: functions, connectivity, allocation |
| doe-sem | ch05-system-design-and-construction.md | Physical system design and CM-controlled construction stages |
| faa-req-handbook | ch04-faa-req-handbook-functional-architecture-and-implementation-constraints.md | Functional architecture and constraints under requirements |
| faa-sem | ch02-faa-sem-concept-functional-analysis.md | Functional analysis in concept development |
| nasa-se-expanded | ch03-nasa-se-expanded-system-design-processes.md | Design processes: reqs through architecture (also reqs eng) |
| nasa-se-handbook | ch19-4-3-logical-decomposition.md | Logical decomposition (also allocation) |
| nasa-se-handbook | ch20-4-4-design-solution-definition.md | Design solution definition |
| nasa-se-handbook | ch21-5-1-product-implementation.md | Product implementation/fabrication (also make/buy) |
| sebok | ch17-sebok-system-architecture-realization.md | System architecture and realization |
| sebok | ch34-sebok-se-quality-attributes.md | Quality attributes / ilities (also reliability) |

## 5. Interface Management & ICIDs

| Pack | Chapter | Why it fits / one-line value |
|---|---|---|
| faa-sem | ch04-faa-sem-technical-management-interface-risk.md | Interface and risk management (also risk mgmt) |
| nasa-se-handbook | ch29-6-3-interface-management.md | Interface management process |

## 6. Integration

| Pack | Chapter | Why it fits / one-line value |
|---|---|---|
| doe-sem | ch06-integration-test-and-acceptance.md | Integration and testing plus installation and acceptance stages (also T&E) |
| nasa-se-expanded | ch04-nasa-se-expanded-product-realization.md | Product realization: integration, V&V, transition (also verification/validation) |
| nasa-se-handbook | ch22-5-2-product-integration.md | Product integration process |

## 7. Verification

| Pack | Chapter | Why it fits / one-line value |
|---|---|---|
| faa-ams-vv | ch01-faa-ams-vv-introduction-and-vv-philosophy.md | V&V philosophy overview |
| faa-ams-vv | ch02-faa-ams-vv-implementation-guidance.md | V&V implementation guidance |
| faa-ams-vv | ch03-faa-ams-vv-approach-and-early-lifecycle.md | V&V approach through early lifecycle |
| faa-ams-vv | ch05-faa-ams-vv-solution-implementation.md | Verification during solution implementation |
| faa-ams-vv | ch07-faa-ams-vv-acronyms-checklists-definitions.md | V&V checklists and definitions |
| faa-ams-vv | cheatsheet.md (support file) | Cheatsheet / quick reference |
| faa-ams-vv | glossary.md (support file) | Glossary for the pack |
| faa-ams-vv | patterns.md (support file) | Patterns/practice heuristics |
| nasa-se-handbook | ch23-5-3-product-verification.md | Product verification process |

## 8. Validation

| Pack | Chapter | Why it fits / one-line value |
|---|---|---|
| faa-ams-vv | ch04-faa-ams-vv-investment-analysis.md | Validation during investment analysis |
| faa-ams-vv | ch06-faa-ams-vv-in-service-management.md | In-service validation and V&V mgmt (also ops) |
| nasa-se-handbook | ch24-5-4-product-validation.md | Product validation process |

## 9. Test & Evaluation

| Pack | Chapter | Why it fits / one-line value |
|---|---|---|
| dod-te-guidebook | ch01-dod-te-guidebook-te-fundamentals-types-events.md | T&E fundamentals, types, events |
| dod-te-guidebook | ch02-dod-te-guidebook-te-strategy-documentation.md | T&E strategy and TEMP documentation |
| dod-te-guidebook | ch03-dod-te-guidebook-te-organizations-roles.md | T&E organizations and roles |
| dod-te-guidebook | ch04-dod-te-guidebook-urgent-capability-acquisition.md | T&E in urgent capability acquisition |
| dod-te-guidebook | ch05-dod-te-guidebook-middle-tier-acquisition.md | T&E in middle-tier acquisition |
| dod-te-guidebook | ch06-dod-te-guidebook-major-capability-acquisition.md | T&E in major capability acquisition |
| dod-te-guidebook | ch07-dod-te-guidebook-software-acquisition.md | T&E in software acquisition |
| dod-te-guidebook | ch08-dod-te-guidebook-defense-business-systems.md | T&E for defense business systems |
| dod-te-guidebook | cheatsheet.md (support file) | Cheatsheet / quick reference |
| dod-te-guidebook | glossary.md (support file) | Glossary for the pack |
| dod-te-guidebook | patterns.md (support file) | Patterns/practice heuristics |

## 10. Modeling, MBSE & SysML

| Pack | Chapter | Why it fits / one-line value |
|---|---|---|
| dodaf | ch02-dm2-data-groups-overview.md | DM2 conceptual data model overview (also data mgmt) |
| dodaf | ch11-dm2-data-groups-detail.md | DM2 data groups in detail |
| nasa-ms-7009 | ch01-ms-scope-criticality-programmatics.md | M&S intended use, criticality, and programmatics planning (also reviews) |
| nasa-ms-7009 | ch03-ms-verification-validation.md | Verification and validation of M&S with recorded domains (also verification/validation) |
| nasa-systems-modeling | ch01-nasa-systems-modeling-mbse-overview-se-engine.md | MBSE overview in SE engine |
| nasa-systems-modeling | ch02-nasa-systems-modeling-model-planning-and-setup.md | Model planning and setup |
| nasa-systems-modeling | ch03-nasa-systems-modeling-the-metamodel.md | The MBSE metamodel |
| nasa-systems-modeling | ch04-nasa-systems-modeling-building-stakeholders-requirements-structure.md | Modeling stakeholders and requirements |
| nasa-systems-modeling | ch05-nasa-systems-modeling-building-verification-validation.md | Modeling verification and validation |
| nasa-systems-modeling | ch06-nasa-systems-modeling-generating-se-work-products.md | Generating SE work products from models |
| nasa-systems-modeling | ch07-nasa-systems-modeling-methodology-framework-alternative-approaches.md | Methodology and alternative approaches |
| nasa-systems-modeling | ch08-nasa-systems-modeling-conops-template-with-model-content.md | ConOps template with model content |
| nasa-systems-modeling | cheatsheet.md (support file) | Cheatsheet / quick reference |
| nasa-systems-modeling | glossary.md (support file) | Glossary for the pack |
| nasa-systems-modeling | patterns.md (support file) | Patterns/practice heuristics |
| sebok | ch06-sebok-representing-systems-models.md | Representing systems with models |

## 11. Digital Engineering & Digital Twins

| Pack | Chapter | Why it fits / one-line value |
|---|---|---|
| digital-systems-engineering | ch01-digital-systems-engineering-introduction-and-landscape.md | DSE discipline landscape and motivation |
| digital-systems-engineering | ch02-digital-systems-engineering-goals-of-the-de-strategy.md | Goals of digital engineering strategy |
| digital-systems-engineering | ch03-digital-systems-engineering-challenges.md | Barriers to digitalizing SE |
| digital-systems-engineering | ch04-digital-systems-engineering-key-enabling-technologies.md | Enabling technologies for DSE |
| digital-systems-engineering | ch05-digital-systems-engineering-framework-and-core-concepts.md | Core concepts organizing the DSE field |
| digital-systems-engineering | ch06-digital-systems-engineering-four-level-framework.md | Four-level framework organizing DSE knowledge/research |
| digital-systems-engineering | ch07-digital-systems-engineering-concluding-remarks-and-research-agenda.md | Research agenda and conclusions |
| digital-systems-engineering | cheatsheet.md (support file) | Cheatsheet / quick reference |
| digital-systems-engineering | glossary.md (support file) | Glossary for the pack |
| digital-systems-engineering | patterns.md (support file) | Patterns/practice heuristics |
| dod-digital-engineering | ch01-dod-digital-engineering-introduction-purpose-vision.md | DoD DE strategy vision and purpose |
| dod-digital-engineering | ch02-dod-digital-engineering-goal1-formalize-models.md | Goal 1: formalized development of authoritative models |
| dod-digital-engineering | ch03-dod-digital-engineering-goal2-authoritative-source-of-truth.md | Goal 2: authoritative source of truth (also data mgmt) |
| dod-digital-engineering | ch04-dod-digital-engineering-goal3-technological-innovation.md | Goal 3: technological innovation |
| dod-digital-engineering | ch05-dod-digital-engineering-goal4-infrastructure-environments.md | Goal 4: DE infrastructure and environments |
| dod-digital-engineering | ch06-dod-digital-engineering-goal5-culture-workforce.md | Goal 5: culture and workforce transformation |
| dod-digital-engineering | ch07-dod-digital-engineering-next-steps-conclusion-summary.md | Implementation summary and next steps |
| dod-digital-engineering | cheatsheet.md (support file) | Cheatsheet / quick reference |
| dod-digital-engineering | glossary.md (support file) | Glossary for the pack |
| dod-digital-engineering | patterns.md (support file) | Patterns/practice heuristics |
| nasa-de-acquisition | ch01-nasa-de-acquisition-framework-rationale-and-dee.md | DE acquisition rationale and digital engineering ecosystem |
| nasa-de-acquisition | ch06-nasa-de-acquisition-collaboration-architecture-interoperability.md | Collaboration architecture and interoperability |
| nasa-de-acquisition | ch07-nasa-de-acquisition-mbe-use-cases.md | Model-based engineering use cases |
| nasa-de-acquisition | ch08-nasa-de-acquisition-mbe-plan-development.md | MBE plan development |

## 12. Configuration Management & Baselines

| Pack | Chapter | Why it fits / one-line value |
|---|---|---|
| faa-sem | ch05-faa-sem-configuration-decision-vv.md | CM, decision analysis, V&V (crosscutting bundle) |
| mil-hdbk-61 | ch01-mil-hdbk-61-scope-fundamentals-definitions.md | CM scope and definitions |
| mil-hdbk-61 | ch02-mil-hdbk-61-lifecycle-management-planning.md | CM planning across lifecycle |
| mil-hdbk-61 | ch03-mil-hdbk-61-configuration-identification.md | Configuration identification |
| mil-hdbk-61 | ch04-mil-hdbk-61-configuration-control-change-management.md | Configuration control / change mgmt |
| mil-hdbk-61 | ch05-mil-hdbk-61-configuration-status-accounting.md | Configuration status accounting |
| mil-hdbk-61 | ch06-mil-hdbk-61-configuration-verification-audit.md | Configuration verification and audits (FCA/PCA) |
| mil-hdbk-61 | ch08-mil-hdbk-61-tailoring-cm-templates-by-phase.md | Tailoring CM by program phase |
| mil-hdbk-61 | cheatsheet.md (support file) | Cheatsheet / quick reference |
| mil-hdbk-61 | glossary.md (support file) | Glossary for the pack |
| mil-hdbk-61 | patterns.md (support file) | Patterns/practice heuristics |
| nasa-de-acquisition | ch02-nasa-de-acquisition-drds-and-configuration-data-management.md | DRDs, configuration and data mgmt (also data mgmt) |
| nasa-se-expanded | ch06-nasa-se-expanded-crosscutting-cm-data-assessment-decision.md | Crosscutting CM, data, assessment, decision (also measurement) |
| nasa-se-handbook | ch31-6-5-configuration-management.md | Configuration management process |

## 13. Data & Information Management

| Pack | Chapter | Why it fits / one-line value |
|---|---|---|
| dodaf | ch05-data-information-viewpoint-div.md | Data & Information viewpoint: structural data descriptions |
| mil-hdbk-61 | ch07-mil-hdbk-61-data-management-emerging-technologies.md | CM-linked data management and emerging tech |
| nasa-de-acquisition | ch05-nasa-de-acquisition-model-based-data-definition.md | Model-based data definitions |
| nasa-npr-7150 | ch06-nasa-npr-7150-recommended-software-records.md | Recommended software records/records retention |
| nasa-se-handbook | ch32-6-6-technical-data-management.md | Technical data management process |
| nist-cps | ch05-nist-cps-data-interoperability.md | CPS data interoperability |

## 14. Risk Management

| Pack | Chapter | Why it fits / one-line value |
|---|---|---|
| dod-rio | ch01-dod-rio-foundations.md | Risk/issue/opportunity management foundations |
| dod-rio | ch02-dod-rio-risk-identification-analysis.md | Risk identification and analysis practice |
| dod-rio | ch03-dod-rio-mitigation-monitoring-issues.md | Mitigation, monitoring, issue management |
| dod-rio | ch05-dod-rio-aaf-pathways-hardware.md | RIO applied on hardware pathways |
| dod-rio | ch06-dod-rio-aaf-pathways-software-services.md | RIO applied on software/services pathways |
| dod-rio | ch07-dod-rio-additional-methods.md | Additional RIO methods |
| dod-rio | ch08-dod-rio-process-roles-se-tools.md | RIO process, roles, tools |
| doe-o-413-3 | ch05-risk-safety-and-exceptions.md | Risk-informed management, safety/security interfaces, and exception paths |
| nasa-ms-7009 | ch06-ms-risk-and-decision-reporting.md | M&S risk assessment and decision-maker reporting (also measurement) |
| nasa-risk | ch01-introduction-and-rm-overview.md | RIDM/CRM risk framework overview |
| nasa-risk | ch02-ridm-crm-integration.md | RIDM and CRM integration |
| nasa-risk | ch03-ridm-part1-identification-of-alternatives.md | Identifying decision alternatives (also decision analysis) |
| nasa-risk | ch04-ridm-part2-risk-analysis-of-alternatives.md | Risk analysis of alternatives |
| nasa-risk | ch05-ridm-part3-risk-informed-selection.md | Risk-informed selection |
| nasa-risk | ch06-crm-initialisation-and-planning.md | CRM initialization and planning |
| nasa-risk | ch07-crm-identify-and-analyze.md | CRM identify and analyze |
| nasa-risk | ch08-crm-plan-step.md | CRM plan step |
| nasa-risk | ch09-crm-track-control-communicate.md | CRM track/control/communicate |
| nasa-risk | ch10-enterprise-risks-and-appendices.md | Enterprise risks and appendices |
| nasa-risk | cheatsheet.md (support file) | Cheatsheet / quick reference |
| nasa-risk | glossary.md (support file) | Glossary for the pack |
| nasa-risk | patterns.md (support file) | Patterns/practice heuristics |
| nasa-se-handbook | ch30-6-4-technical-risk-management.md | Technical risk management process |
| nist-ai-rmf | ch01-framing-ai-risk.md | Framing AI risk |
| nist-ai-rmf | ch05-map-function.md | Map function: risk context |
| nist-ai-rmf | ch07-manage-function.md | Manage function: risk treatment |

## 15. Opportunity/Benefit Management

| Pack | Chapter | Why it fits / one-line value |
|---|---|---|
| dod-rio | ch04-dod-rio-opportunity-cross-program.md | Opportunity management and cross-program risk/opportunity |

## 16. Decision Analysis & Trade Studies

| Pack | Chapter | Why it fits / one-line value |
|---|---|---|
| nasa-ceh | ch06-nasa-ceh-decision-support-analyses.md | Cost-based decision support and trade analysis |
| nasa-se-handbook | ch34-6-8-decision-analysis.md | Decision analysis process |

## 17. Technical Planning & Work Breakdown

| Pack | Chapter | Why it fits / one-line value |
|---|---|---|
| doe-sem | ch03-planning-stage.md | Planning stage: QA/CM plans, objectives, scope, feasibility |
| nasa-npr-7123 | ch06-systems-engineering-management-plan.md | SEMP content and structure |
| nasa-se-expanded | ch05-nasa-se-expanded-crosscutting-planning-requirements-interface-risk.md | Crosscutting planning, reqs, interface, risk |
| nasa-se-handbook | ch26-6-0-crosscutting-technical-management.md | Crosscutting technical management overview |
| nasa-se-handbook | ch27-6-1-technical-planning.md | Technical planning and SEMP |
| sebok | ch15-sebok-technical-management.md | Technical management processes overview |

## 18. Measurement & Technical Assessment

| Pack | Chapter | Why it fits / one-line value |
|---|---|---|
| dod-mosa | ch05-dod-mosa-assessment-tech-change-roadmaps.md | Assessing MOSA designs and tech-change roadmaps (also planning) |
| gao-agile | ch08-gao-agile-metrics.md | Agile metrics and measurement |
| gao-tra | ch01-tra-fundamentals.md | Technology readiness assessment fundamentals |
| gao-tra | ch02-technology-readiness-levels.md | TRL definitions and use |
| gao-tra | ch03-critical-technology-elements.md | Identifying critical technology elements |
| gao-tra | ch04-five-step-tra-process.md | Five-step TRA process |
| gao-tra | ch05-four-characteristics.md | Four characteristics of a quality TRA |
| gao-tra | ch06-technology-maturation-plans.md | Technology maturation planning |
| gao-tra | ch07-using-tras-in-decisions.md | Using TRAs in decisions (also decision analysis) |
| gao-tra | cheatsheet.md (support file) | Cheatsheet / quick reference |
| gao-tra | glossary.md (support file) | Glossary for the pack |
| gao-tra | patterns.md (support file) | Patterns/practice heuristics |
| mrl-deskbook | ch01-mrl-deskbook-foundations-and-dod-policy.md | Manufacturing readiness fundamentals |
| mrl-deskbook | ch02-mrl-deskbook-scale-threads-and-trl-relationship.md | MRL scale, threads, TRL relationship |
| mrl-deskbook | ch03-mrl-deskbook-adaptive-acquisition-framework.md | MRL within the AAF (also acquisition) |
| mrl-deskbook | ch04-mrl-deskbook-conducting-assessments.md | Conducting MRL assessments |
| mrl-deskbook | ch05-mrl-deskbook-maturation-plans-and-risk.md | Maturation plans and risk (also risk mgmt) |
| mrl-deskbook | ch07-mrl-deskbook-tailoring-and-users-guide.md | MRL tailoring and use |
| mrl-deskbook | cheatsheet.md (support file) | Cheatsheet / quick reference |
| mrl-deskbook | glossary.md (support file) | Glossary for the pack |
| mrl-deskbook | patterns.md (support file) | Patterns/practice heuristics |
| nasa-ms-7009 | ch02-ms-development-evidence-capability.md | M&S development evidence and capability assessment factors |
| nasa-ms-7009 | ch04-ms-uncertainty-sensitivity.md | Uncertainty characterization and sensitivity analysis |
| nasa-ms-7009 | ch05-ms-use-results-assessment.md | M&S use-phase input control and results assessment |
| nasa-npr-7123 | ch08-technology-readiness-levels.md | TRL definitions for assessment |
| nasa-se-handbook | ch33-6-7-technical-assessment.md | Technical assessment, TPMs, measures |
| nist-ai-rmf | ch06-measure-function.md | Measure function: metrics for AI risk |
| nist-stat-handbook | ch01-nist-stat-handbook-exploratory-data-analysis.md | Exploratory data analysis |
| nist-stat-handbook | ch02-nist-stat-handbook-measurement-process-characterization.md | Measurement process characterization |
| nist-stat-handbook | ch03-nist-stat-handbook-production-process-characterization.md | Production process characterization |
| nist-stat-handbook | ch04-nist-stat-handbook-process-modeling.md | Process modeling |
| nist-stat-handbook | ch05-nist-stat-handbook-process-improvement-doe.md | DOE for process improvement |
| nist-stat-handbook | ch07-nist-stat-handbook-product-and-process-comparisons.md | Product/process comparisons |
| nist-stat-handbook | cheatsheet.md (support file) | Cheatsheet / quick reference |
| nist-stat-handbook | glossary.md (support file) | Glossary for the pack |
| nist-stat-handbook | patterns.md (support file) | Patterns/practice heuristics |

## 19. Quality Assurance & Process Compliance

| Pack | Chapter | Why it fits / one-line value |
|---|---|---|
| gao-agile | ch09-gao-agile-assessment-reference-auditor-questions-frameworks.md | Auditor assessment questions (also program mgmt) |
| mil-hdbk-516 | ch02-systems-engineering-criteria.md | SE airworthiness criteria: design criteria control, tech data, CM, mfg quality (also CM) |
| nist-stat-handbook | ch06-nist-stat-handbook-process-monitoring-and-control.md | SPC monitoring and control (quality control) |

## 20. Safety, Reliability & Survivability

| Pack | Chapter | Why it fits / one-line value |
|---|---|---|
| faa-rma | ch01-faa-rma-introduction-and-key-documents.md | RMA intro and key documents |
| faa-rma | ch02-faa-rma-fundamentals.md | Reliability/maintainability/availability fundamentals |
| faa-rma | ch03-faa-rma-lifecycle-stages.md | RMA across lifecycle stages |
| faa-rma | ch04-faa-rma-technical-management-process.md | Managing the RMA process |
| faa-rma | ch05-faa-rma-methods-and-tools.md | RMA analysis methods and tools |
| faa-rma | ch06-faa-rma-glossary-and-definitions.md | RMA definitions |
| faa-rma | ch07-faa-rma-software-reliability.md | Software reliability |
| faa-rma | ch08-faa-rma-requirements-guidelines.md | Writing RMA requirements |
| faa-rma | cheatsheet.md (support file) | Cheatsheet / quick reference |
| faa-rma | glossary.md (support file) | Glossary for the pack |
| faa-rma | patterns.md (support file) | Patterns/practice heuristics |
| faa-system-safety | ch01-faa-system-safety-foundations-policy-process-principles.md | System safety policy, process, principles |
| faa-system-safety | ch02-faa-system-safety-acquisition-lifecycle-assessments-contracting.md | Safety in acquisition and contracting |
| faa-system-safety | ch03-faa-system-safety-integrated-hazard-analysis-tasks.md | Integrated hazard analysis tasks |
| faa-system-safety | ch04-faa-system-safety-analysis-techniques.md | Safety analysis techniques (FHA, FTA...) |
| faa-system-safety | ch05-faa-system-safety-software-test-facilities-safety.md | Software and test facility safety |
| faa-system-safety | ch06-faa-system-safety-launch-safety-and-training.md | Launch safety and safety training |
| faa-system-safety | ch07-faa-system-safety-orm-human-organizational-factors.md | Operational risk mgmt and human/org factors |
| faa-system-safety | cheatsheet.md (support file) | Cheatsheet / quick reference |
| faa-system-safety | glossary.md (support file) | Glossary for the pack |
| faa-system-safety | patterns.md (support file) | Patterns/practice heuristics |
| mil-hdbk-338 | ch01-rma-theory-foundations.md | Reliability, maintainability, availability theory and life distributions |
| mil-hdbk-338 | ch02-specification-allocation-prediction.md | Reliability specification, allocation, modeling, prediction (also requirements) |
| mil-hdbk-338 | ch03-parts-management-and-derating.md | Parts management and derating |
| mil-hdbk-338 | ch04-circuit-design-and-fault-tolerance.md | Reliable circuit design and fault-tolerant/redundant design |
| mil-hdbk-338 | ch05-environmental-and-human-reliability.md | Environmental design and human performance reliability (also human factors) |
| mil-hdbk-338 | ch06-fmea-fta-and-sneak-circuits.md | FMEA/FMECA, fault tree, and sneak circuit analysis |
| mil-hdbk-338 | ch07-design-reviews-testability-safety.md | Design reviews, design for testability, safety interface (also control gates) |
| mil-hdbk-338 | ch08-data-fracas-demonstration-growth.md | Reliability data, FRACAS, demonstration, growth testing |
| mil-hdbk-338 | ch09-systems-reliability-engineering.md | System effectiveness and system-level R&M engineering |
| mil-hdbk-338 | cheatsheet.md (support file) | Cheatsheet / quick reference |
| mil-hdbk-338 | glossary.md (support file) | Glossary for the pack |
| mil-hdbk-338 | patterns.md (support file) | Patterns/practice heuristics |
| mil-hdbk-516 | ch03-structures-criteria.md | Airframe structures airworthiness criteria |
| mil-hdbk-516 | ch04-flight-technology-criteria.md | Flying qualities, performance, stability/control criteria |
| mil-hdbk-516 | ch05-propulsion-criteria.md | Propulsion and installation airworthiness criteria |
| mil-hdbk-516 | ch06-avionics-e3-and-diagnostics.md | Diagnostics, avionics, electrical power, and E3 criteria |
| mil-hdbk-516 | ch07-computer-systems-and-software.md | Computer systems and software airworthiness criteria (also verification) |
| mil-std-882 | ch01-scope-purpose-definitions.md | System safety scope and definitions |
| mil-std-882 | ch02-system-safety-process.md | MIL-STD-882 system safety process |
| mil-std-882 | ch03-risk-assessment.md | Safety risk assessment matrices (also risk mgmt) |
| mil-std-882 | ch04-software-system-safety.md | Software system safety |
| mil-std-882 | ch05-task-100-management.md | Program management safety tasks |
| mil-std-882 | ch06-task-200-analysis.md | Hazard analysis tasks |
| mil-std-882 | ch07-task-300-evaluation.md | Safety evaluation tasks |
| mil-std-882 | ch08-task-400-verification.md | Safety verification tasks |
| mil-std-882 | cheatsheet.md (support file) | Cheatsheet / quick reference |
| mil-std-882 | glossary.md (support file) | Glossary for the pack |
| mil-std-882 | patterns.md (support file) | Patterns/practice heuristics |
| nasa-fault-management | ch01-nasa-fault-management-introduction-and-fm-definitions.md | Fault management definitions and scope |
| nasa-fault-management | ch02-nasa-fault-management-process.md | FM development process |
| nasa-fault-management | ch03-nasa-fault-management-requirements-development.md | FM requirements development (also reqs eng) |
| nasa-fault-management | ch04-nasa-fault-management-design-and-architecture.md | FM design and architecture (also arch/design) |
| nasa-fault-management | ch05-nasa-fault-management-analysis-verification-validation.md | FM analysis, verification, validation |
| nasa-fault-management | ch06-nasa-fault-management-operations-and-lifecycle-reviews.md | FM ops and lifecycle reviews |
| nasa-fault-management | ch07-nasa-fault-management-fundamental-concepts-and-principles.md | FM concepts and principles |
| nasa-fault-management | ch08-nasa-fault-management-organization-and-lessons-learned.md | FM organization and lessons learned |
| nasa-fault-management | cheatsheet.md (support file) | Cheatsheet / quick reference |
| nasa-fault-management | glossary.md (support file) | Glossary for the pack |
| nasa-fault-management | patterns.md (support file) | Patterns/practice heuristics |
| nasa-pra | ch01-nasa-pra-foundations-risk-management-and-pra-framework.md | PRA and risk mgmt framework |
| nasa-pra | ch02-nasa-pra-scenario-development-and-logic-modeling.md | Scenario development, event/fault trees |
| nasa-pra | ch03-nasa-pra-data-collection-and-bayesian-parameter-estimation.md | Data collection and Bayesian estimation |
| nasa-pra | ch04-nasa-pra-uncertainty-modeling-and-common-cause-failures.md | Uncertainty and common-cause failures |
| nasa-pra | ch05-nasa-pra-human-reliability-and-software-risk-assessment.md | Human reliability and software risk |
| nasa-pra | ch06-nasa-pra-physical-structural-and-phenomenological-models.md | Physical/structural/phenomenological models |
| nasa-pra | ch07-nasa-pra-uncertainty-propagation-and-results-presentation.md | Uncertainty propagation and results |
| nasa-pra | ch08-nasa-pra-launch-abort-modeling-and-worked-pra-examples.md | Launch abort modeling and worked examples |
| nasa-pra | cheatsheet.md (support file) | Cheatsheet / quick reference |
| nasa-pra | glossary.md (support file) | Glossary for the pack |
| nasa-pra | patterns.md (support file) | Patterns/practice heuristics |
| nasa-rm-standard | ch01-nasa-rm-standard-scope-and-applicability.md | R&M standard scope |
| nasa-rm-standard | ch02-nasa-rm-standard-terminology-and-definitions.md | R&M terminology |
| nasa-rm-standard | ch03-nasa-rm-standard-objectives-and-strategies.md | R&M objectives and strategies |
| nasa-rm-standard | ch04-nasa-rm-standard-implementation-requirements.md | Implementation, planning and gate review requirements (also governance) |
| nasa-rm-standard | ch05-nasa-rm-standard-objectives-hierarchy-and-scope.md | Objectives hierarchy and scoping |
| nasa-rm-standard | ch06-nasa-rm-standard-evidentiary-analysis-methods.md | Evidentiary analysis methods |
| nasa-rm-standard | cheatsheet.md (support file) | Cheatsheet / quick reference |
| nasa-rm-standard | glossary.md (support file) | Glossary for the pack |
| nasa-rm-standard | patterns.md (support file) | Patterns/practice heuristics |
| nasa-system-safety | ch01-introduction.md | System safety introduction |
| nasa-system-safety | ch02-key-concepts.md | Safety key concepts |
| nasa-system-safety | ch03-system-safety-framework-overview.md | Safety framework overview (also process models) |
| nasa-system-safety | ch04-safety-objectives-requirements.md | Safety objectives and requirements (also reqs eng) |
| nasa-system-safety | cheatsheet.md (support file) | Cheatsheet / quick reference |
| nasa-system-safety | glossary.md (support file) | Glossary for the pack |
| nasa-system-safety | patterns.md (support file) | Patterns/practice heuristics |
| nist-stat-handbook | ch08-nist-stat-handbook-assessing-product-reliability.md | Assessing product reliability |

## 21. Cybersecurity & Security Engineering

| Pack | Chapter | Why it fits / one-line value |
|---|---|---|
| cisa-cpg | ch01-cpg-purpose-and-2-0-changes.md | CPG 2.0 baseline purpose and CSF alignment |
| cisa-cpg | ch02-govern-and-identify-goals.md | Govern and identify performance goals |
| cisa-cpg | ch03-protect-goals.md | Protect goals: identity, segmentation, resilience |
| cisa-cpg | ch04-detect-respond-recover-goals.md | Detect, respond, recover goals |
| cisa-cpg | ch05-it-ot-implementation-and-prioritization.md | IT/OT implementation and goal prioritization |
| cisa-cpg | cheatsheet.md (support file) | Cheatsheet / quick reference |
| cisa-cpg | glossary.md (support file) | Glossary for the pack |
| cisa-cpg | patterns.md (support file) | Patterns/practice heuristics |
| mrl-deskbook | ch08-mrl-deskbook-ot-cybersecurity.md | OT cybersecurity in MRL context |
| nist-800-171 | ch01-cui-scope-fundamentals-and-structure.md | CUI protection model tailored from SP 800-53B moderate baseline (also standards tailoring) |
| nist-800-171 | ch02-access-control-and-identification.md | Access control and identification/authentication for CUI |
| nist-800-171 | ch03-awareness-personnel-physical.md | Awareness/training, personnel security, physical protection |
| nist-800-171 | ch04-audit-and-configuration.md | Audit and accountability plus configuration management (also CM) |
| nist-800-171 | ch05-incident-maintenance-media.md | Incident response, maintenance, and media protection |
| nist-800-171 | ch06-risk-assessment-monitoring-planning.md | Risk assessment, security assessment, monitoring, planning (also risk mgmt) |
| nist-800-171 | ch07-communications-and-integrity.md | System/communications protection and information integrity |
| nist-800-171 | ch08-acquisition-and-supply-chain.md | Acquisition and supply chain risk management for CUI (also supplier/acquisition) |
| nist-800-171 | cheatsheet.md (support file) | Cheatsheet / quick reference |
| nist-800-171 | glossary.md (support file) | Glossary for the pack |
| nist-800-171 | patterns.md (support file) | Patterns/practice heuristics |
| nist-800-37 | ch01-nist-800-37-introduction.md | Risk management framework intro |
| nist-800-37 | ch02-nist-800-37-fundamentals.md | RMF fundamentals |
| nist-800-37 | ch03-nist-800-37-process-and-prepare.md | Prepare step |
| nist-800-37 | ch04-nist-800-37-categorize-and-select.md | Categorize and select controls |
| nist-800-37 | ch05-nist-800-37-implement-and-assess.md | Implement and assess controls |
| nist-800-37 | ch06-nist-800-37-authorize.md | Authorize step (also control gates) |
| nist-800-37 | ch07-nist-800-37-monitor.md | Monitor step |
| nist-800-37 | cheatsheet.md (support file) | Cheatsheet / quick reference |
| nist-800-37 | glossary.md (support file) | Glossary for the pack |
| nist-800-37 | patterns.md (support file) | Patterns/practice heuristics |
| nist-800-61 | ch01-scope-shift-and-csf-integration.md | IR reframed as cybersecurity risk management via CSF 2.0 |
| nist-800-61 | ch02-ir-lifecycle-model.md | CSF 2.0 incident response life cycle model |
| nist-800-61 | ch03-roles-policies-and-playbooks.md | IR roles, policies, procedures, and playbooks |
| nist-800-61 | ch04-preparation-and-lessons-learned-profile.md | Community profile: preparation and lessons learned (GV/ID/PR + ID.IM) |
| nist-800-61 | ch05-detect-respond-recover-profile.md | Community profile: detect, respond, recover execution |
| nist-800-61 | ch06-coordination-training-and-improvement.md | Coordination, training, communications, and improvement |
| nist-800-61 | cheatsheet.md (support file) | Cheatsheet / quick reference |
| nist-800-61 | glossary.md (support file) | Glossary for the pack |
| nist-800-61 | patterns.md (support file) | Patterns/practice heuristics |
| nist-cps | ch04-nist-cps-cybersecurity-and-privacy-risk.md | CPS cybersecurity and privacy risk |
| nist-csf | ch01-csf-overview-and-components.md | CSF overview and functions |
| nist-csf | ch03-identify-id.md | Identify function |
| nist-csf | ch04-protect-pr.md | Protect function |
| nist-csf | ch05-detect-de.md | Detect function |
| nist-csf | ch06-respond-rs.md | Respond function |
| nist-csf | ch07-recover-rc.md | Recover function |
| nist-csf | cheatsheet.md (support file) | Cheatsheet / quick reference |
| nist-csf | glossary.md (support file) | Glossary for the pack |
| nist-csf | patterns.md (support file) | Patterns/practice heuristics |
| nist-ssdf | ch01-introduction-and-how-to-use.md | SSDF purpose and use |
| nist-ssdf | ch02-prepare-the-organization.md | Prepare the organization |
| nist-ssdf | ch03-protect-the-software.md | Protect software and supply chain |
| nist-ssdf | ch04-produce-well-secured-software.md | Produce well-secured software |
| nist-ssdf | ch05-respond-to-vulnerabilities.md | Respond to vulnerabilities |
| nist-ssdf | cheatsheet.md (support file) | Cheatsheet / quick reference |
| nist-ssdf | glossary.md (support file) | Glossary for the pack |
| nist-ssdf | patterns.md (support file) | Patterns/practice heuristics |
| nist-sse | ch01-sse-foundations.md | Systems security engineering foundations |
| nist-sse | ch02-sse-framework.md | SSE framework |
| nist-sse | ch03-design-principles.md | Secure design principles (also arch/design) |
| nist-sse | ch04-trustworthiness-and-lifecycle.md | Trustworthiness across lifecycle |
| nist-sse | ch05-cyber-resiliency-framework.md | Cyber resiliency framework |
| nist-sse | ch06-cyber-resiliency-techniques.md | Resiliency techniques |
| nist-sse | ch07-cyber-resiliency-design-principles.md | Resiliency design principles |
| nist-sse | ch08-applying-and-risk.md | Applying resiliency with risk mgmt |
| nist-sse | cheatsheet.md (support file) | Cheatsheet / quick reference |
| nist-sse | glossary.md (support file) | Glossary for the pack |
| nist-sse | patterns.md (support file) | Patterns/practice heuristics |

## 22. Human Systems Integration / Human Factors

| Pack | Chapter | Why it fits / one-line value |
|---|---|---|
| faa-hf-std | ch01-faa-hf-std-foundations-and-general-design.md | HF foundations and general design |
| faa-hf-std | ch02-faa-hf-std-automation.md | Human-automation interaction |
| faa-hf-std | ch03-faa-hf-std-designing-equipment-for-maintenance.md | Maintainability/human factors of maintenance |
| faa-hf-std | ch04-faa-hf-std-displays-controls-and-visual-indicators.md | Displays, controls, visual indicators |
| faa-hf-std | ch05-faa-hf-std-alarms-audio-and-voice-communications.md | Alarms and audio/voice comms |
| faa-hf-std | ch06-faa-hf-std-chi-information-presentation.md | Computer-human interface: information presentation |
| faa-hf-std | ch07-faa-hf-std-chi-interaction-and-dialogue.md | CHI interaction and dialogue |
| faa-hf-std | ch08-faa-hf-std-input-devices-and-workplace-design.md | Input devices and workplace design |
| faa-hf-std | ch09-faa-hf-std-safety-environment-anthropometry-documentation.md | Safety, environment, anthropometry, documentation |
| faa-hf-std | cheatsheet.md (support file) | Cheatsheet / quick reference |
| faa-hf-std | glossary.md (support file) | Glossary for the pack |
| faa-hf-std | patterns.md (support file) | Patterns/practice heuristics |
| mil-hdbk-516 | ch08-crew-systems-criteria.md | Crew systems: pilot-vehicle interface, life support, escape/survival criteria (also airworthiness) |
| nasa-hsi | ch01-introduction-to-hsi.md | HSI introduction and domains |
| nasa-hsi | ch02-implementing-hsi.md | Implementing HSI |
| nasa-hsi | ch03-hsi-in-the-see-engine.md | HSI inside the SE engine |
| nasa-hsi | ch04-pre-phase-a-and-phase-a.md | HSI in early phases |
| nasa-hsi | ch05-phases-b-and-c.md | HSI in phases B/C |
| nasa-hsi | ch06-phases-d-e-f.md | HSI in phases D/E/F |
| nasa-hsi | ch07-hsi-products-scaling-tailoring.md | HSI products, scaling, tailoring |
| nasa-hsi | ch08-hsi-plan-writing-and-execution.md | HSI plan writing and execution |
| nasa-hsi | ch09-appendices-hsi-plan-checklist-cases.md | HSI plan checklist and cases |
| nasa-hsi | cheatsheet.md (support file) | Cheatsheet / quick reference |
| nasa-hsi | glossary.md (support file) | Glossary for the pack |
| nasa-hsi | patterns.md (support file) | Patterns/practice heuristics |
| nasa-se-handbook | ch05-2-6-human-systems-integration-hsi-in-the-se-pr.md | HSI overview in SE processes |

## 23. Logistics, Supportability & Sustainment

| Pack | Chapter | Why it fits / one-line value |
|---|---|---|
| sd-22-dmsms | ch01-sd-22-dmsms-introduction-fundamentals.md | DMSMS fundamentals |
| sd-22-dmsms | ch02-sd-22-dmsms-policy-lifecycle-guidance.md | DMSMS policy and lifecycle guidance |
| sd-22-dmsms | ch03-sd-22-dmsms-prepare-program-infrastructure.md | Setting up a DMSMS program |
| sd-22-dmsms | ch04-sd-22-dmsms-identify-monitoring-surveillance.md | Identifying: monitoring and surveillance |
| sd-22-dmsms | ch05-sd-22-dmsms-assess-resolution-need-timing-level.md | Assessing resolution need, timing, level |
| sd-22-dmsms | ch06-sd-22-dmsms-analyze-resolution-determination.md | Analyzing resolution options |
| sd-22-dmsms | ch07-sd-22-dmsms-implement-resolutions.md | Implementing DMSMS resolutions |
| sd-22-dmsms | ch08-sd-22-dmsms-obsolescence-relationship.md | Obsolescence vs DMSMS relationship |
| sd-22-dmsms | cheatsheet.md (support file) | Cheatsheet / quick reference |
| sd-22-dmsms | glossary.md (support file) | Glossary for the pack |
| sd-22-dmsms | patterns.md (support file) | Patterns/practice heuristics |

## 24. Operations, Maintenance & Disposal

| Pack | Chapter | Why it fits / one-line value |
|---|---|---|
| doe-sem | ch07-maintenance-stage.md | Post-acceptance maintenance process model under operational CM |
| eu-ai-act | ch10-post-market-surveillance.md | Post-market monitoring of fielded AI (also ops) |
| nasa-se-handbook | ch15-3-8-project-phase-e-operations-and-sustainment.md | Phase E operations and sustainment |
| nasa-se-handbook | ch16-3-9-project-phase-f-closeout.md | Phase F closeout and disposal |
| nasa-se-handbook | ch25-5-5-product-transition.md | Product transition to operations |
| sebok | ch18-sebok-system-maintenance.md | System maintenance (also sustainment) |

## 25. Training & Documentation Delivery

| Pack | Chapter | Why it fits / one-line value |
|---|---|---|

## 26. Project/Program Management

| Pack | Chapter | Why it fits / one-line value |
|---|---|---|
| dod-mosa | ch03-dod-mosa-program-management-considerations.md | PM considerations for MOSA programs |
| dod-mq-bok | ch01-dod-mq-bok-pre-mdd.md | SE/PM work in pre-MDD phase |
| dod-mq-bok | ch02-dod-mq-bok-msa.md | SE/PM work in MSA phase |
| dod-mq-bok | ch03-dod-mq-bok-tmrr.md | SE/PM work in TMRR phase |
| dod-mq-bok | ch04-dod-mq-bok-emd.md | SE/PM work in EMD phase |
| dod-mq-bok | ch05-dod-mq-bok-prod-deploy.md | SE/PM work in production & deployment |
| dod-mq-bok | ch06-dod-mq-bok-ops-support.md | SE/PM work in ops & support |
| dodaf | ch07-project-viewpoint-pv.md | Project viewpoint: program/organization mappings |
| doe-o-413-3 | ch01-purpose-applicability-governance.md | Capital-asset Order purpose, applicability, and governance (also governance) |
| doe-o-413-3 | ch04-performance-baseline-cost-schedule.md | Performance baseline, cost, schedule, contingency, EVMS (also measurement) |
| gao-agile | ch01-gao-agile-introduction-background.md | Agile in federal context |
| gao-agile | ch02-gao-agile-adoption-challenges-federal-response.md | Adoption challenges and federal response |
| gao-agile | ch03-gao-agile-adoption-best-practices.md | Agile adoption best practices |
| gao-agile | ch04-gao-agile-execution-and-controls.md | Agile execution and control mechanisms |
| gao-agile | ch07-gao-agile-program-monitoring-control.md | Agile program monitoring and control |
| gao-cost | ch01-gao-cost-fundamentals-credible-estimates.md | Cost estimating fundamentals |
| gao-cost | ch02-gao-cost-process-planning-program-definition.md | Cost process and program definition |
| gao-cost | ch03-gao-cost-data-ground-rules-point-estimate.md | Cost data, ground rules, point estimates |
| gao-cost | ch04-gao-cost-sensitivity-risk-uncertainty.md | Cost sensitivity, risk, uncertainty (also risk mgmt) |
| gao-cost | ch05-gao-cost-document-present-update.md | Documenting and presenting cost estimates |
| gao-cost | ch06-gao-cost-auditing-validating.md | Auditing and validating cost estimates |
| gao-cost | ch07-gao-cost-earned-value-management.md | Earned value management |
| gao-cost | ch08-gao-cost-specialized-techniques-internal-control.md | Specialized cost techniques and internal control |
| gao-cost | cheatsheet.md (support file) | Cheatsheet / quick reference |
| gao-cost | glossary.md (support file) | Glossary for the pack |
| gao-cost | patterns.md (support file) | Patterns/practice heuristics |
| gao-schedule | ch01-gao-schedule-introduction-reliable-schedule.md | Reliable schedule fundamentals |
| gao-schedule | ch02-gao-schedule-capturing-and-sequencing-activities.md | Capturing and sequencing activities |
| gao-schedule | ch03-gao-schedule-resources-and-durations.md | Resources and durations |
| gao-schedule | ch04-gao-schedule-traceability-and-critical-path.md | Schedule traceability and critical path |
| gao-schedule | ch05-gao-schedule-total-float-and-risk-analysis.md | Float and schedule risk analysis |
| gao-schedule | ch06-gao-schedule-updating-baseline-four-characteristics.md | Baseline updating, four characteristics |
| gao-schedule | ch07-gao-schedule-auditing-key-questions.md | Schedule audit key questions |
| gao-schedule | ch08-gao-schedule-evm-forward-backward-pass-reference-data.md | EVM and forward/backward pass reference |
| gao-schedule | cheatsheet.md (support file) | Cheatsheet / quick reference |
| gao-schedule | glossary.md (support file) | Glossary for the pack |
| gao-schedule | patterns.md (support file) | Patterns/practice heuristics |
| nasa-ceh | ch01-nasa-ceh-introduction-and-process-overview.md | Cost estimating process overview |
| nasa-ceh | ch02-nasa-ceh-project-definition-tasks.md | Project definition for costing |
| nasa-ceh | ch03-nasa-ceh-cost-methodology-tasks.md | Cost methodology selection |
| nasa-ceh | ch04-nasa-ceh-cost-estimate-tasks.md | Building the cost estimate |
| nasa-ceh | ch05-nasa-ceh-jcl-analysis.md | Joint confidence level analysis |
| nasa-ceh | ch07-nasa-ceh-economic-analysis.md | Economic analysis |
| nasa-ceh | cheatsheet.md (support file) | Cheatsheet / quick reference |
| nasa-ceh | glossary.md (support file) | Glossary for the pack |
| nasa-ceh | patterns.md (support file) | Patterns/practice heuristics |
| nasa-schedule | ch01-nasa-schedule-foundations.md | Schedule fundamentals |
| nasa-schedule | ch02-nasa-schedule-management-planning.md | Schedule management planning |
| nasa-schedule | ch03-nasa-schedule-development-scope-and-boe.md | Scope and basis of estimate |
| nasa-schedule | ch04-nasa-schedule-development-build-and-outputs.md | Building the schedule and outputs |
| nasa-schedule | ch05-nasa-schedule-assessment.md | Schedule assessment/health analysis |
| nasa-schedule | ch06-nasa-schedule-risk-analysis.md | Schedule risk analysis |
| nasa-schedule | ch07-nasa-schedule-maintenance-and-control.md | Schedule maintenance and control (also baselines) |
| nasa-schedule | ch08-nasa-schedule-documentation-and-communication.md | Schedule documentation and communication |
| nasa-schedule | cheatsheet.md (support file) | Cheatsheet / quick reference |
| nasa-schedule | glossary.md (support file) | Glossary for the pack |
| nasa-schedule | patterns.md (support file) | Patterns/practice heuristics |
| nasa-se-handbook | ch04-2-5-cost-effectiveness-considerations.md | Cost-effectiveness considerations |
| nasa-se-handbook | ch08-3-1-program-formulation.md | Program formulation |
| nasa-se-handbook | ch09-3-2-program-implementation.md | Program implementation |
| nasa-se-handbook | ch10-3-3-project-pre-phase-a-concept-studies.md | Pre-Phase A concept studies |
| nasa-se-handbook | ch11-3-4-project-phase-a-concept-and-technology-dev.md | Phase A concept and technology development |
| nasa-se-handbook | ch12-3-5-project-phase-b-preliminary-design-and-tec.md | Phase B preliminary design |
| nasa-se-handbook | ch13-3-6-project-phase-c-final-design-and-fabricati.md | Phase C final design and fabrication |
| nasa-se-handbook | ch14-3-7-project-phase-d-system-assembly-integratio.md | Phase D assembly/integration (also integration) |
| sebok | ch31-sebok-se-project-management.md | SE and project management relationship |

## 27. Supplier, Procurement & Acquisition

| Pack | Chapter | Why it fits / one-line value |
|---|---|---|
| dod-mosa | ch06-dod-mosa-acquisition-pathways.md | MOSA across AAF acquisition pathways |
| doe-o-413-3 | ch03-acquisition-planning-and-ipt.md | Acquisition strategy, project execution planning, and IPTs (also planning) |
| gao-agile | ch06-gao-agile-federal-contracting-process.md | Agile federal contracting |
| mrl-deskbook | ch06-mrl-deskbook-contract-language.md | MRL contract language |
| nasa-de-acquisition | ch03-nasa-de-acquisition-requirements-exchange-and-contract-language.md | Requirements exchange and DE contract language |
| nasa-de-acquisition | ch04-nasa-de-acquisition-data-acquisition-contract-language.md | Data acquisition contract language |
| nasa-npr-7123 | ch04-contracted-projects.md | Requirements flow to contracted projects |

## 28. Stakeholder Engagement & Needs

| Pack | Chapter | Why it fits / one-line value |
|---|---|---|
| nasa-se-handbook | ch17-4-1-stakeholder-expectations-definition.md | Stakeholder expectations definition |
| nist-ai-rmf | ch02-audience-and-ai-actors.md | AI actors and stakeholders in the RMF |
| sebok | ch16-sebok-system-concept-definition.md | System concept definition from stakeholder needs |

## 29. Governance, Reviews, Gates & Control Points

| Pack | Chapter | Why it fits / one-line value |
|---|---|---|
| dau-se-guidebook | ch03-technical-reviews-and-audits.md | TRRs, PDR/CDR, FCA/PCA and other formal control gates |
| doe-o-413-3 | ch02-critical-decisions-cd0-cd4.md | CD-0 through CD-4 stage gates and approval authorities |
| doe-o-413-3 | ch06-reviews-responsibilities-crd.md | External/independent reviews, roles, and contractor requirements (also supplier) |
| eu-ai-act | ch01-general-provisions.md | Scope, definitions, regulatory structure |
| eu-ai-act | ch02-prohibited-practices.md | Banned AI practices |
| eu-ai-act | ch05-obligations-operators.md | Operator obligations along the value chain |
| eu-ai-act | ch07-transparency-obligations.md | Transparency obligations |
| eu-ai-act | ch08-general-purpose-ai.md | GPAI model obligations |
| eu-ai-act | ch09-governance.md | AI Office / Board / national authority governance |
| eu-ai-act | ch11-penalties-enforcement.md | Penalties and enforcement |
| eu-ai-act | cheatsheet.md (support file) | Cheatsheet / quick reference |
| eu-ai-act | glossary.md (support file) | Glossary for the pack |
| eu-ai-act | patterns.md (support file) | Patterns/practice heuristics |
| nasa-npr-7123 | ch05-lifecycle-technical-reviews.md | Lifecycle technical reviews (SRR through FRR) |
| nasa-npr-7123 | ch09-review-entrance-success-criteria.md | Review entrance/success criteria |
| nist-ai-rmf | ch04-govern-function.md | Govern function |
| nist-csf | ch02-govern-gv.md | Govern function (cyber governance) |

## 30. Standards, Tailoring & Process Models

| Pack | Chapter | Why it fits / one-line value |
|---|---|---|
| dau-se-guidebook | ch04-technical-management-processes.md | The 8 technical management processes mapped to 15288 |
| dau-se-guidebook | ch05-technical-processes.md | The 8 technical processes (15288-style process definitions) |
| dodaf | ch09-standards-viewpoint-stdv.md | Standards viewpoint: applicable standards profiles |
| doe-sem | ch02-lifecycle-model-and-quality-reviews.md | Eight-stage SEM lifecycle with walkthrough/ISA/stage-exit gates (also governance gates) |
| mil-hdbk-516 | ch01-scope-applicability-and-tailoring.md | Airworthiness certification basis scope, applicability, and tailoring |
| nasa-ms-7009 | ch07-hdbk-lifecycle-implementation.md | Handbook life-cycle implementation of M&S credibility requirements |
| nasa-npr-7123 | ch01-introduction.md | NPR 7123 structure and applicability |
| nasa-npr-7123 | ch02-institutional-programmatic-requirements.md | Programmatic process requirements |
| nasa-npr-7123 | ch03-common-technical-processes.md | Common technical processes (15288-style defs) |
| nasa-npr-7123 | ch07-definitions.md | Process definitions |
| nasa-npr-7150 | ch01-nasa-npr-7150-introduction-purpose-structure.md | Software requirements NPR structure |
| nasa-npr-7150 | ch02-nasa-npr-7150-roles-responsibilities-tailoring.md | Roles and tailoring |
| nasa-npr-7150 | ch03-nasa-npr-7150-software-management-requirements.md | Software management requirements |
| nasa-npr-7150 | ch04-nasa-npr-7150-software-engineering-lifecycle-requirements.md | Software lifecycle requirements |
| nasa-npr-7150 | ch05-nasa-npr-7150-supporting-lifecycle-requirements.md | Supporting lifecycle requirements |
| nasa-npr-7150 | ch07-nasa-npr-7150-definitions.md | Definitions |
| nasa-npr-7150 | ch08-nasa-npr-7150-software-classifications.md | Software classification levels |
| nasa-se-expanded | ch02-nasa-se-expanded-life-cycle-and-tailoring.md | Lifecycle models and tailoring |
| nasa-se-handbook | ch02-2-1-the-common-technical-processes-and-the-se.md | Common technical processes model |
| nasa-se-handbook | ch06-2-7-competency-model-for-systems-engineers.md | SE competency model |
| nasa-se-handbook | ch07-3-0-nasa-program-project-life-cycle.md | NASA program/project life cycle model |
| nist-ai-rmf | ch08-profiles-and-use.md | Profiles and tailoring the RMF |
| nist-cps | ch03-nist-cps-related-standards-and-applying-the-framework.md | Related standards and applying the framework |
| nist-csf | ch08-profiles-tiers-and-using-the-csf.md | Profiles, tiers, and tailoring CSF use |
| sebok | ch08-sebok-se-and-management-overview.md | SE and management overview (process framing) |
| sebok | ch09-sebok-life-cycle-terms-concepts.md | Life-cycle terms and concepts |
| sebok | ch10-sebok-development-approaches.md | Choosing development approaches |
| sebok | ch11-sebok-agile-approaches.md | Agile approaches for systems |
| sebok | ch12-sebok-life-cycle-model-selection.md | Life-cycle model selection |
| sebok | ch13-sebok-process-concepts.md | SE process concepts |
| sebok | ch14-sebok-process-selection-tailoring.md | Process selection and tailoring |
| sebok | ch19-sebok-se-standards.md | SE standards landscape |
| sebok | ch26-sebok-enabling-businesses-enterprises.md | Enabling businesses/enterprises for SE |
| sebok | ch27-sebok-enabling-teams.md | Enabling teams |
| sebok | ch28-sebok-enabling-individuals.md | Enabling individuals (competency) |

## 31. Specialty Engineering

| Pack | Chapter | Why it fits / one-line value |
|---|---|---|
| faa-sem | ch06-faa-sem-specialty-rma-lifecycle-e3-humanfactors.md | Multi-specialty: RMA, E3, human factors |
| faa-sem | ch07-faa-sem-specialty-infosec-safety-environmental.md | Multi-specialty: infosec, safety, environmental |
| nist-cps | ch06-nist-cps-timing-and-time-awareness.md | Timing and time awareness (specialty concern) |
| nist-cps | ch08-nist-cps-managing-and-securing-time.md | Managing and securing time (also cybersecurity) |
| sebok | ch29-sebok-related-disciplines-env-geo.md | Related disciplines: environment, geospatial |
| sebok | ch30-sebok-se-industrial-engineering.md | SE and industrial engineering |
| sebok | ch33-sebok-se-physical-domain-disciplines.md | Physical-domain disciplines (specialties) |

## 32. Assurance & System Assurance

| Pack | Chapter | Why it fits / one-line value |
|---|---|---|
| eu-ai-act | ch03-high-risk-classification.md | Classifying high-risk AI systems |
| eu-ai-act | ch04-high-risk-requirements.md | Requirements placed on high-risk AI systems |
| eu-ai-act | ch06-conformity-assessment.md | Conformity assessment and CE marking regime |
| eu-ai-act | ch12-annex-iii-high-risk-usecases.md | Annex III high-risk use-case list |
| nasa-system-safety | ch05-system-safety-ensurance-activities.md | Safety ensurance/assurance activities |
| nasa-system-safety | ch06-risc-development.md | Risk-informed safety case development |
| nasa-system-safety | ch07-risc-evaluation.md | Safety case evaluation |
| nist-ai-rmf | ch03-trustworthiness-characteristics.md | Trustworthiness characteristics of AI |

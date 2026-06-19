# Chapter 38: Systems Engineering and Enterprise IT

## Core Idea
Human Systems Integration (HSI) applies systems engineering processes to ensure that human, organizational, and technical considerations are jointly optimized throughout the entire system lifecycle — from early stakeholder requirements through production, operation, and disposal.

## Frameworks Introduced
- **Human Systems Integration (HSI)**: A management and technical discipline that coordinates planning, enabling, and optimizing all human-related considerations across seven integration domains to achieve balanced optimization of performance, effectiveness, suitability, survivability, safety, and affordability.
  - When to use: In any system acquisition or development where human operators, maintainers, or support personnel interact with technology; mandatory in DoD and widely adopted across government and commercial sectors
  
- **Seven HSI Domains Framework**: A structured approach identifying manpower, personnel, training, human factors engineering, safety & occupational health, force protection & survivability, and habitability as co-equal engineering considerations requiring dedicated expertise and cross-domain trade-off analysis.
  - When to use: As the template for organizing HSI efforts; organizations may adapt domain names to align with local structures, but the technical work across all domains remains essential

## Key Concepts
- **Human Factors Engineering (HFE)**: One domain of HSI focused specifically on designing human-machine interfaces consistent with users' physical, cognitive, and sensory abilities—*not* synonymous with HSI itself.
- **Manpower**: The most efficient, cost-effective mix of personnel and contract support required to operate, maintain, train, and support a system (quantitative: staffing levels and composition).
- **Personnel**: The cognitive, physical, and social capabilities—aptitudes, knowledge, skills, abilities, experience—required to execute assigned roles; critical to operational success.
- **Training**: The integrated instructional system (courseware, simulators, embedded training, job aids, technical manuals) that enables personnel to acquire or enhance job-relevant knowledge, skills, and team capabilities.
- **Safety & Occupational Health**: System design features and administrative controls minimizing risks of human or machine error, injury, acute/chronic illness, or disability to operators and maintainers.
- **Force Protection & Survivability**: Design features enabling system operation and personnel safety during and after exposure to hostile environments, chemical/biological/nuclear threats, and accidents.
- **Habitability**: Living and working conditions (lighting, space, ventilation, temperature, noise, services) sustaining morale, health, safety, comfort, recruitment, and retention.
- **Measure of Effectiveness (MOE)**: Mission-outcome metric encompassing hardware, software, and human performance; often decomposed into human-specific Measures of Performance (MOP) and Measures of Suitability (MOS).

## Mental Models
- **Think of HSI as integral to systems engineering, not a "specialty":** HSI must be embedded in early requirements generation and maintained throughout the lifecycle; assigning it to a separate human factors team deprives it of scope and authority to optimize trade-offs.
- **Manpower and lifecycle cost are inseparable:** Insufficient human-centered design creates large manpower and training costs, reduced performance, and catastrophic risk; early HSI investment yields substantial lifecycle savings.
- **Human-in-the-loop simulation strengthens design:** Models of human cognition, behavior, performance, and fatigue should be built into system models during design; simulation during development catches integration failures before production.

## Anti-patterns
- **Assigning HSI to a human factors engineer without systems engineering expertise:** Human factors engineers lack the broader SE process knowledge and cross-domain authority to optimize trade-offs; this relegates HSI to a specialty role, depriving it of sufficient scope.
- **Deferring human considerations to training:** Historically, technology-centered projects addressed human challenges through post-design training rather than human-centered design; this yields high manpower costs, poor usability, and safety risks.
- **Treating MOEs as HSI-specific metrics:** MOEs measure overall mission performance (hardware + software + human); the HSI integrator must identify and incorporate relevant human-specific MOPs and MOSs, not create separate HSI effectiveness measures.

## Key Takeaways
1. **Start HSI early:** Initiate HSI activities during stakeholder requirements generation, not after design is locked; sustained involvement across the lifecycle realizes maximum benefit and cost savings.
2. **The integrator must be a systems engineer first:** The human systems integrator should be a knowledgeable SE practitioner with respect among peers and working knowledge of all seven domains—not an expert in any one domain.
3. **Joint working groups enable knowledge sharing:** Customer and contractor HSI teams should collaborate through integrated working groups to share priorities and align objectives across organizational boundaries.
4. **HSI domain experts collaborate but don't lead:** Domain specialists (manpower analysts, HFE designers, safety engineers, etc.) report to or consult with the HSI integrator; the integrator makes cross-domain trade-offs to optimize total system performance.
5. **HSI shares concerns with RAM, logistics, and test & evaluation:** The integrator and domain experts coordinate with Reliability/Availability/Maintainability specialists, logistics teams, and T&E leads to ensure human considerations are represented in modeling, simulation, and validation.
6. **Modularization around sources of change improves affordability:** Designing the architecture so that frequent changes (e.g., operator roles, training requirements) are contained within single elements reduces lifecycle costs and brittleness.
7. **Budget and schedule must account for HSI scope:** Integrators must be involved early in program planning to secure adequate budget and schedule; HSI risk and trade-study activities must be explicitly resourced in the SEMP or standalone HSIP.

## Connects To
- **ISO 15288 (System Lifecycle Processes)**: HSI applies SE lifecycle discipline specifically to human and organizational aspects; both standards share early-and-continuous integration as a core principle.
- **SAE 6906 (Standard Practice for Human Systems Integration)**: The authoritative commercial and aerospace standard codifying HSI practices, definitions, and domain frameworks.
- **DoD Instruction 5000.02T (Defense Acquisition System)**: The regulatory context in which HSI originated; the seven-domain framework is embedded in DoD acquisition requirements.
- **Reliability, Availability, Maintainability (RAM)**: HSI shares concerns with RAM engineering; human factors (operator fatigue, skill degradation, error rates) directly influence system reliability and maintainability metrics.
- **System Security:** Hardware assurance and cyber resilience strategies must account for human vulnerabilities (social engineering, operator error, insider threats) and human-in-the-loop defenses.
- **System Affordability:** Total ownership cost analysis, service-oriented architectures, and autonomous system design all rely on HSI trade-offs to balance acquisition cost, lifecycle cost, and labor requirements.


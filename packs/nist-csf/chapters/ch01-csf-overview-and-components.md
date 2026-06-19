# Chapter 1: CSF Overview and Components

## Core Idea
The NIST Cybersecurity Framework (CSF) 2.0 is a voluntary, sector- and technology-neutral taxonomy of high-level cybersecurity outcomes organized into three interoperable components — Core, Organizational Profiles, and Tiers — that any organization can use to understand, assess, prioritize, and communicate its cybersecurity risks.

## Frameworks Introduced
- **CSF Core**: Hierarchical taxonomy of Functions, Categories, and Subcategories describing desired cybersecurity outcomes without prescribing how to achieve them.
  - When to use: as the universal outcome vocabulary for structuring a cybersecurity program.
- **CSF Organizational Profile**: A mechanism for documenting an organization's current and/or target cybersecurity posture in terms of Core outcomes.
  - When to use: to baseline current state, set a target state, and track gap closure over time.
- **CSF Tiers**: A four-level scale (Partial → Risk Informed → Repeatable → Adaptive) characterizing the rigor of cybersecurity risk governance and management practices.
  - When to use: to communicate maturity ambition internally and set the overall tone for risk management.

## Key Concepts
- **CSF Core**: The nucleus of the CSF — a taxonomy of high-level cybersecurity outcomes arranged in a Function/Category/Subcategory hierarchy applicable to any organization regardless of size, sector, or maturity.
- **CSF Function**: The highest-level organizational unit of the Core; there are six Functions (GOVERN, IDENTIFY, PROTECT, DETECT, RESPOND, RECOVER), each named after a verb summarizing its outcomes.
- **CSF Category**: A group of related cybersecurity outcomes that collectively comprise a Function; each Category has a two-part alphabetic identifier (e.g., GV.OC, ID.AM).
- **CSF Subcategory**: More specific outcomes of technical and management activities that divide a Category; identified by a numeric suffix (e.g., GV.OC-01).
- **CSF Organizational Profile**: Documents current and/or target cybersecurity posture in Core outcome terms; used to prioritize actions and communicate with stakeholders.
- **CSF Tier**: Characterizes rigor of risk governance and management on a four-point scale: Partial (Tier 1), Risk Informed (Tier 2), Repeatable (Tier 3), Adaptive (Tier 4).
- **Informative References**: Mappings between Core outcomes and existing standards, guidelines, regulations, or other content — helping organizations understand how outcomes can be achieved.
- **Implementation Examples**: Concise, action-oriented, notional illustrations of ways to achieve Core Subcategory outcomes; not a required baseline.
- **Quick-Start Guides (QSGs)**: Brief, audience-tailored documents that distill specific CSF portions into actionable first steps for improving cybersecurity posture.
- **Community Profile**: A sector-, subsector-, or use-case-specific baseline of CSF outcomes published to address shared goals; usable as the starting point for an organization's own Target Profile.

## Mental Models
- Use the Core for the *what* (desired outcomes), and Informative References/Implementation Examples for the *how*.
- Use Organizational Profiles to translate strategy into measurable gap analysis; use Tiers to characterize how rigorously risk management is conducted, not whether specific outcomes are met.
- Treat all six Functions as concurrent, not sequential: GOVERN, IDENTIFY, PROTECT, and DETECT run continuously; RESPOND and RECOVER must be ready at all times and activate on incidents.

## Anti-patterns
- **Treating the Core as a checklist**: The order and size of Functions, Categories, and Subcategories do not imply sequence or relative importance; a checkbox approach misses the outcome orientation.
- **One-size-fits-all application**: Each organization has unique risks, appetites, and missions; the CSF explicitly requires tailoring.

## Key Takeaways
1. The CSF provides a common outcome vocabulary usable across sectors, countries, and technologies, enabling consistent communication from board to practitioner.
2. Three components — Core, Profiles, Tiers — serve distinct purposes: Core = outcomes, Profiles = posture documentation, Tiers = governance rigor.
3. The CSF does not prescribe controls; it links to online Informative References and Implementation Examples for implementation guidance.
4. GOVERN sits at the center of the six-Function wheel because it informs how an organization prioritizes and implements all other Functions.
5. Profiles support both internal improvement cycles and external stakeholder communication (e.g., supplier expectations, customer assurance).
6. The framework applies to all ICT types — IT, IoT, OT, cloud, mobile, and AI systems — and is designed to remain relevant as technology evolves.

## Connects To
- **NIST Risk Management Framework (SP 800-37)**: CSF complements RMF by providing outcome-level goals that guide control selection from SP 800-53.
- **NIST Privacy Framework**: Overlapping risk domains (confidentiality, integrity, availability of personal data); used alongside CSF to address privacy risks not fully covered by cybersecurity alone.
- **NIST AI RMF**: Parallel structure (Functions, Categories, Subcategories) for AI risk; CSF and AI RMF together address combined cybersecurity/AI risk portfolios.
- **ISO/IEC 42010 (architecture description)**: Informative References can link CSF outcomes to any standard; the CSF is the interoperability layer across global frameworks.

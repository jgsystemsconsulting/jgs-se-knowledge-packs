# Chapter 6: Representing Systems

## Core Idea
In MBSE, models are the primary artifacts of systems engineering rather than text-based documents. Models provide integrated representations that support analysis, design, verification, and validation across the system lifecycle while enabling effective communication among multidisciplinary teams.

## Frameworks Introduced
- **Model-Based Systems Engineering (MBSE)**: Systematic use of models as the central technical baseline, managed and controlled alongside other system artifacts.
  - When to use: Throughout the full system lifecycle to replace or augment document-centric approaches
- **View and Viewpoint (IEEE 1471)**: View represents a system from the perspective of related concerns; Viewpoint specifies conventions for constructing views.
  - When to use: When addressing multiple stakeholder concerns or discipline-specific requirements
- **Black-Box and White-Box Models**: Black-box exposes only external features and behavior; white-box reveals internal structure.
  - When to use: At any decomposition level to manage complexity and abstraction
- **Model Classification (Formal/Informal, Physical/Abstract)**: Formal models use languages with defined syntax and semantics; physical models are concrete; abstract models are mathematical or logical.
  - When to use: When selecting appropriate representation depth and precision for specific model purposes
- **Conceptual Models and Meta-Models**: Define the set of concepts and relationships in a system (e.g., requirements, behavior, structure, properties).
  - When to use: As foundation for standardized descriptions across projects and organizations
- **Integration of Descriptive and Analytical Models**: Combine logical relationships (descriptive) with mathematical relationships (analytical, static or dynamic).
  - When to use: To fully realize benefits of model-based approaches by connecting architecture to performance and risk
- **Semantic Interoperability**: Ensures constructs in one model have consistent meaning across other models through transformations and standards.
  - When to use: When integrating multi-domain models (electrical, mechanical, software) or exchanging data between tools
- **Work Breakdown Structure (WBS)**: Deliverable-oriented organization of project scope mapped to system components and capabilities.
  - When to use: To align project planning with system architecture and enable traceability of costs and resources
- **Design Structure Matrix (DSM)**: Visualizes dependencies between system components and project activities, derived from unified models.
  - When to use: To identify coupling loops and manage integration complexity in product-process models
- **SysML Requirements Diagram**: Captures requirements and their relationships visually; traceability captured via satisfy/refine links to blocks.
  - When to use: To move beyond textual requirements management and enable automated consistency checking
- **Object-Process Methodology (OPM)**: Bimodal graphical (OPD) and textual (OPL) language for conceptual modeling; enables solution-neutral requirements and automated generation.
  - When to use: For requirements-level modeling and generating system designs from formal specifications
- **Risk-Oriented Systems Engineering (ROSE)**: Integrates risk layers into core system models via Object-Process Methodology.
  - When to use: When designing for robustness and resilience in response to risk scenarios
- **CORAS Framework**: UML-derivative for IT security risk modeling using misuse cases and extended notation.
  - When to use: For security risk assessment in information systems
- **System-Theoretic Accident Model and Processes (STAMP)**: Reformulates safety as a control problem; enables hazard avoidance in socio-technical systems.
  - When to use: For safety-critical and mission-critical system design

## Key Concepts
- **Abstraction**: Hiding unimportant details to focus on essential characteristics; essential for managing behavioral and structural complexity.
- **Model Scope**: Three dimensions define a model's extent: breadth (requirement coverage), depth (decomposition levels), and fidelity (level of detail).
- **Model Quality**: Adherence to modeling guidelines and degree of support for intended purpose (not to be confused with quality of the design modeled).
- **Formal Model**: Representation using a modeling language with defined syntax and semantics; necessary for MBSE rigor.
- **Descriptive Model**: Represents logical relationships (structure, interconnections, functions, test cases); typically includes architecture and geometric models.
- **Analytical Model**: Represents mathematical relationships; subdivided into dynamic (time-varying) and static (non-time-varying) models.
- **Simulation**: Implementation of an analytical model in executable code with input/output infrastructure; can be stochastic/deterministic, steady-state/dynamic, continuous/discrete, local/distributed.
- **Model Integration**: Alignment of descriptive, analytical, and executable models across disciplines to ensure consistency and traceability.
- **Model-Based Metrics**: Progress (completeness vs. scope), cost/effort estimation, technical quality/risk assessment, and model quality measurement.

## Mental Models
- **Use abstraction strategically**: Choose breadth, depth, and fidelity to support the model's specific purpose without drowning in irrelevant detail.
- **Think of models as executable specifications**: Formal models can be analyzed, simulated, and transformed to generate designs or validate requirements; they are not passive documentation.
- **Integrate across domains early**: Multi-disciplinary system design requires that electrical, mechanical, and software models stay semantically interoperable from concept onwards, not retrofitted at integration.
- **Treat the model as the baseline**: In MBSE, models replace documents as the primary controlled artifact; traceability, verification, and management all flow from the model, not parallel to it.

## Anti-patterns
- **Treating models as documentation**: Models are active engineering artifacts for analysis and synthesis, not decorative visualizations of pre-decided designs.
- **Over-modeling**: Choosing a scope that includes details irrelevant to the model's purpose, increasing maintenance burden without adding value.
- **Model-document schism**: Maintaining separate, inconsistent repositories of information (e.g., requirements in a database, architecture in a separate tool) breaks traceability and invites drift.
- **Ignoring model quality for design quality**: A high-quality model accurately represents the design; a flawed design can still be modeled correctly. Confusing the two leads to false confidence.
- **Isolated multi-domain models**: Electrical, mechanical, and software models that do not establish semantic interoperability become islands that fail to reveal integration failures until late in development.

## Key Takeaways
1. Models are the primary artifacts of MBSE, not supporting documentation—they drive analysis, design, and verification across the lifecycle.
2. Every model must have a clearly defined purpose; scope is set by breadth (what requirements?), depth (how many levels?), and fidelity (how detailed?).
3. Abstraction is not a limitation—it is the foundation of tractable engineering; choose what to hide based on the model's purpose.
4. Descriptive and analytical models must be integrated (via transformations, semantic mappings, and shared repositories) to realize the full benefits of model-based approaches.
5. Formal modeling languages with defined syntax and semantics are non-negotiable for MBSE; informal sketches are useful for communication but not for traceability or automated analysis.
6. Multi-view modeling (requirements, functional, structural, parametric, safety/reliability views) is essential—no single view captures all stakeholder concerns.
7. Semantic interoperability between models (electrical, mechanical, software, project, risk) is the key to catching integration failures early.

## Connects To
- **ISO/IEC/IEEE 42010 (Architecture Description)**: Codifies view/viewpoint concepts for architecture modeling; directly referenced by IEEE 1471 and adopted in SysML.
- **Systems Modeling Language (SysML) v1/v2**: Extends UML with domain-specific constructs (requirements diagrams, parametric diagrams, allocations) to formalize descriptive and analytical modeling.
- **Object Management Group (OMG) standards**: MDA (Model-Driven Architecture), UML, SysML, and model transformation standards (QVT, XMI) enable semantic interoperability across tools and domains.
- **ISO/IEC 15288 (Systems Lifecycle Processes)**: Defines the lifecycle stages (conception, development, production, utilization, support, retirement) within which models are created and maintained.
- **Data exchange standards (AP-233, ReqIF, XMI)**: Enable interoperability of models between tools; critical for integrating component design models with system models.
- **IDEF0, DFD, FFBD**: Functional modeling languages that predate SysML; still used alongside SysML for specific domains and backward compatibility.

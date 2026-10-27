# Cheatsheet: jsp-936

Decision rules and role and lifecycle structures the directive contains, described in text. Tables in the source are described, not reproduced.

> Contains public sector information licensed under the Open Government Licence v3.0.
> Source: JSP 936 Dependable Artificial Intelligence (AI) in Defence, Part 1: Directive, V1.1 (November 2024), Ministry of Defence, © Crown copyright.
> Reconstructed reference notes, not reproductions. Licence text and source links: [LICENSE](LICENSE).

Part 2 (Guidance) is not in this pack.

## Directive vocabulary

Where the policy says must, the action is a compulsory requirement completed by the actioner. Where it says should, the action is recommended good practice, considered and applied as far as the context allows.

## Scope decision rule

Tie scope to existing risk management: AI developed or purchased to meet a Defence need is generally in scope (ISR object detection, reinforcement learning in C2 and autonomous systems, LLMs in HR, AI in decision support from course-of-action development to logistics planning); openly available proprietary search engines, predictive text on consumer messaging, and low-risk office productivity tools are named out of scope, with responsible use still the user's duty. Where AI is blended with non-AI techniques, judgement decides component by component.

## Dependability rule

No dependability scale exists. Confidence in a system must be commensurate with the reliance placed on it, risk owners judge evidence adequacy through the lifecycle, and owners of resultant risk must understand and communicate uncertainty. Risk management itself stays with JSP 892.

## Ethical risk referral ladder

Run an AI ethical risk assessment at the outset and at any material change in scope or outputs. Rate each use case overall from impact and likelihood assessed together, and set the approval level from residual risk, not inherent risk. The printed table walks five bands, Critical down to Minor, across escalating referral levels: Critical escalates to the 2PUS or Ministers by exception, Severe to defence-level oversight such as JROC/IAC, and Major to TLB-level oversight with delegation to business level as appropriate. A programme may need JROC/IAC or Ministerial attention even where JSP 892 financial and output thresholds would not trigger it. AI in kinetic effects and AI in novel or contentious applications always merit special attention and are referred to DAU, notifying DAIC, wherever the ethical risk warrants top-level departmental ownership. Unacceptable risk halts deployment or development safely until risks are sufficiently managed.

## Ethics governance roles

Every TLB appoints an RAISO; all AI projects identify their organisation's RAISO, and SROs of medium- and high-risk projects inform the RAISO of the project. The RAISO ensures appropriate assurance is in place across accountable AI projects, sets the culture, and manages trade-offs between ethical risk and operational effectiveness; on transfer of AI, the receiving organisation's RAISO must understand and accept the risk. TLB Executive Boards provide annual Statements of AI Ethical Assurance to the 2PUS underpinned by auditable evidence. Large projects, projects with significant ethics risk, and teams producing AI regularly should have at least an Ethics Manager and an Independent Ethics Assurance mechanism; the Ethics Manager coordinates with quality and safety roles and may be a combined appointment where competence and independence hold. DAU is consulted before external communication on ethically sensitive work.

## AI lifecycle stage objectives

The directive is lifecycle agnostic; per stage it asks for: Planning, version-controlled documents covering tools, standards, controlled transitions, change and waiver routes, in-situ modification control, through-life monitoring, obsolescence, environmental impact, and steps ensuring the ethical principles can be met. Requirements, performance requirements beside functional ones, hazard analysis including data failure modes, new hazards passed up to system safety as derived requirements, honest handling of lost ML traceability, operating-context articulation, and demonstration information with acceptable-performance measures. Architecture, traceable to requirements and protecting against analysed failure modes. Algorithm design and implementation, justified choices, justified optimisation measures, overfitting avoidance, traceability, and justified frameworks and libraries. Data, separate training, test and verification sets, the four correctness properties (relevant, complete, balanced, accurate), provenance recorded from collection or ingestion, configuration management of all data and metadata, and validated synthetic data. Models, risk-informed reuse information, interpretability with stakeholder-appropriate views, classification inherited from training data. Verification and validation, demonstration across the ODD including boundaries and edge cases, demonstrated safe behaviour outside the ODD, regression testing across updates checking for catastrophic forgetting and model drift, and evidence supporting the sufficiency of validity claims. Integration and use, environment-difference analysis, approved ODD clearly defined, SyOPs, environment and performance monitoring at appropriate rates, and expert checks on important or risky decisions.

## Data correctness properties

Data should be demonstrated correct as relevant to the intended behaviour in the ODD, complete across the potential input space against real-world distributions, balanced for the model's purpose, and an accurate reflection of the real-world application. The source credits this framing to Ashmore, Calinescu and Paterson.

## Verification versus validation

Verification demonstrates the AI meets requirements (did we build it right). Validation demonstrates the AI meets the user's needs (did we build the right thing). Both must include demonstration across the ODD, and both apply again across updates.

## Supplier contracting rule

External AI must attract the same confidence as in-house AI. Require demonstrated supplier competence commensurate with the use, compelling arguments that third-party components have not undermined confidence, assured and documented provenance for all training and test data including third-party data, through-life support with access to data, algorithms and models, clear intellectual property ownership for data, algorithms, models and tests, and an export-control assessment covering data as well as algorithms and models so MOD keeps freedom of action.

## Assurance decision rules

Keep traditional software assurance approaches and add the AI overlay. Treat assurance risk, the risk that the assurance process itself cannot resolve imprecise requirements, lost traceability, complexity and unpredictable behaviour, as a decision gate: where it cannot be tolerated, the AI must not be adopted. Exploit system-context tolerance where some incorrect outputs are acceptable within an overall safe, secure and ethical outcome. Where AI replaces extant technology or human judgement, argue the AI's specific risk is no greater than what it replaced. Assure behaviour on expected ODD excursions, especially adversarially caused ones, choosing between fail safe and fail operational postures, with confidence commensurate with the ethical, safety, security and mission risk of the function.

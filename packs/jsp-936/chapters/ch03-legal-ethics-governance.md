Sources: JSP 936 Part 1 V1.1, printed body pp. 8-18 (source Chapters 3 and 4, paragraphs 44 to 114).

# Legal and Ethical Considerations, AI Ethics Governance

## Core Idea

MOD's ambition to adopt AI is bounded by three perspectives: good governance, demonstration of safety, and legal compliance. Five ethical principles from the ASR policy connect to all three. The directive then builds governance machinery on top: an AI ethical risk rating that sets the approvals pathway, a Responsible AI Senior Officer in every TLB, annual assurance statements to the department's second Permanent Under Secretary, and rules for AI shared with or acquired from international partners.

On the legal side, every aspect of MOD's AI development and use is governed by national and international law, including International Humanitarian Law. Appropriate legal advice must be sought through existing channels at the beginning of an AI project and at relevant stages through the programme; industry and developers must obtain their own advice, and wider queries go to MOD Legal Advisers. Systems of control that keep AI use within legal obligations, such as controls on personal data when operating internationally, must be clearly communicated to relevant stakeholders.

## Frameworks Introduced

- Five MOD AI Ethical Principles from the ASR: Human-centricity, Responsibility, Understanding, Bias and Harm Mitigation, and Reliability. The directive states the principles should be read in the context of the whole ASR document and related publications, with JSP 985 named among them.
- An AI ethical risk assessment run at the outset and at any material change in scope or outputs, which determines the approvals pathway; a guiding framework is promised for Part 2 and meanwhile supplied as Minimum Viable Products by DAU.
- A referral ladder that pairs an overall risk rating, calculated from impact and likelihood together and judged on residual risk, with escalation levels: Critical reaches the 2PUS or Ministers by exception, Severe goes to defence-level oversight such as JROC/IAC, and Major sits at TLB-level oversight with delegation to business level as appropriate, down through the lower bands.
- Two categories that always merit special attention under extant policy: AI in kinetic effects, and AI in novel and contentious applications; such cases are referred to DAU, notifying DAIC, wherever the ethical risk warrants top-level departmental ownership.

## Key Concepts

Human-centricity requires that all humans interacting with or affected by the system, from MOD personnel to civilians to targets of military action, are clearly identified, with the AI's impact on each group assessed so positive effects are maximised and any negatives are justified. Impact analysis runs for all modes and autonomy levels and weighs eight human-security factors summarised from JSP 985: personal and physical, political, economic, cultural and community, health, food, environmental and climate, and informational. Harmful effects are treated as distinct from intended military effects, and even military effect must show benefit outweighing wider negative impacts.

Responsibility rests with humans as moral agents: the behaviour of an AI system is not solely the operator's or duty holder's problem, and it is the governance chain's job to identify responsible people for contributing factors, down to the correctness of training data, and to keep accountability continuous across every agreed context of use, re-examined whenever that context changes.

Understanding is transparency plus explainability. Since individual ML decisions may be impossible to explain in human-understandable terms, what matters is enough understanding of overall behaviour and performance to judge effectiveness, safety and risk-benefit; that is why Testing, Evaluation, Verification and Validation carry the weight. Stakeholder groups must be identified and explanations matched to their needs, within security, privacy and intellectual property limits.

Bias and harm mitigation demands an open, inclusive culture where diverse teams feel safe raising issues and taking part in ethical risk assessment; analysis of data, learning algorithms and models must be made for unwanted bias; and monitoring and mitigation strategies must cover the harms that may arise, including physical, psychological and discrimination harms.

Reliability is read in its broadest sense across three focal areas: reliable (correct operation meeting intended outcomes within acceptable performance criteria), robust (handling inputs outside the intended design appropriately), and secure (protection against data loss, adversarial action, and insecure interaction in the wider system of systems, with confidentiality, integrity and availability applying throughout). Resilience, the ability to manage and recover from failure, and maintainability are added alongside. An AI cannot be expected to be reliable outside its ODD and cannot be guaranteed error-free inside it, so the operating context must be clearly defined and communicated, with geospatial, temporal or functional constraints where they help. Performance targets must be defined for the operating context and demonstrated with confidence commensurate with the risk of failure; where AI replaces an existing approach, demonstrating Globally At Least Equivalent (GALE) performance may be appropriate. Security threat analysis must cover the development environment, supply chains, data chains and other threat vectors, with guards in place, the adversarial attack surface minimised so far as reasonably practicable, remaining vulnerabilities and unmitigated failure modes communicated to the risk owner, and emergent inter-system and cascading-failure effects considered as AI becomes ubiquitous.

## Mental Models

- Compliance is determined by how a system does what it does, not by what it does; no list of acceptable or unacceptable concepts can exist, and nearly any concept might be delivered responsibly if the directive's precepts are followed.
- The RAISO is the ethics-governance hinge: every AI project must identify its organisation's RAISO, SROs of medium- and high-risk projects must inform the RAISO, the RAISO ensures assurance is in place across the accountable estate and sets the culture that makes responsible AI possible, and the RAISO manages the trade-offs between ethical risk and operational effectiveness.
- Risk ratings can outgrow ordinary risk management: a programme may need JROC/IAC or Ministerial attention even where financial and output thresholds in JSP 892 would not trigger it, and unacceptable risk halts deployment or development until reviewed.

## Anti-patterns

Approving on inherent rather than residual risk is refused; the referral decision uses the severity left after controls and mitigations. Point-in-time risk assessment is refused too: risks change across the lifecycle as latent risks emerge and systems adapt, so management must continue throughout. Treating ethics as a barrier is also rejected; the directive argues ethical practice is what makes ambitious adoption deliverable, and that Defence must not only be ethical but be seen to be ethical, with evidence communicated as transparently as security constraints allow.

## Key Takeaways

- Ethics governance is layered onto existing software governance, not substituted for it: TLB Executive Boards must provide annual Statements of AI Ethical Assurance to the 2PUS underpinned by auditable evidence, and each TLB must appoint an RAISO.
- Large projects, projects with significant ethics risk, or teams producing AI regularly should have at least an Ethics Manager and an Independent Ethics Assurance mechanism; the Ethics Manager coordinates with quality and safety roles and may be a combined appointment where competence and independence are demonstrable.
- DAU sets AI ethics policy and must be consulted before external communication on ethically sensitive work; DAIC coheres the training obligations.
- For AI shared internationally, a UK RAISO should satisfy themselves that use of UK-developed AI aligns with ASR; for non-UK-developed AI or data used by MOD, the RAISO must satisfy themselves it meets UK ASR policy, including provision of a Statement of AI Ethics Assurance. MOD supports NATO's Data and Artificial Intelligence Review Board and its Responsible AI Certification Standard work, named here as allied context.

## Connects To

The risk-communication duties here feed the assurance arguments in ch08, the human factors behind bias and understanding in ch04, and the data-side controls in ch05. JSP 892 remains the risk-management baseline; the safety-management system obligations named in ch06 belong to the jsp-815 pack, and the acquisition-safety framing to the jsp-376 pack.

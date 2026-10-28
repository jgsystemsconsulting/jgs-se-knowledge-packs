Sources: JSP 936 Part 1 V1.1, printed body pp. 5-8 (source Chapter 2, paragraphs 27 to 43).

# AI in Defence Systems (RAS, digital systems)

## Core Idea

AI is a cross-cutting technology: it spreads from back-office corporate services to frontline military capability because it performs where the input space is too large and complex for traditional software. That strength carries a counterweight. The potential for unpredictable and opaque behaviour means adopting AI instead of an existing technology is a balance-of-risk judgement, and for AI components assessed at major risk and above the rationale must be recorded and agreed at the appropriate level through the AI governance chain.

The directive divides the systems AI lives in into two main classes: Robotic and Autonomous Systems (RAS), physical platforms that typically move to achieve a desired outcome, and Digital Systems, which receive, process and store data and output information to a human or another system. The boundary is acknowledged as blurred, and some concepts apply across both.

## Frameworks Introduced

- The RAS/digital split as the organising frame for where AI sits and which failure shapes matter.
- A working characterisation of an autonomous system (a defined term): it acts on high-level human goal-setting, decides a course of action from alternatives without depending on human oversight and control, may behave in ways that are individually unpredictable even when the overall activity is predictable, and is contrasted with automated systems that only perform pre-programmed actions.
- The autonomy continuum: manually operated, through automatic, to fully autonomous. The JSP concerns dependable AI at every point, but higher autonomy reduces the potential for human decision-making in the control loop, which must be considered when applying the requirements. Context-appropriate human involvement achieving meaningful human control is required throughout the AI lifecycle.
- The Operational Design Domain (ODD) as the declared envelope of context, conditions and systems an AI is designed for.

## Key Concepts

On RAS: the directive treats only advanced robotics, meaning systems that need AI for complex tasks. There is no consensus definition of an autonomous system, so the JSP supplies its own characterisation and notes NATO's published definition of autonomy as external context, named here and not quoted. Robots and autonomous systems overlap without coinciding: advanced robots need not be autonomous and autonomous systems need not be robotic.

Dual-use technology gets specific treatment. Where a civil-sector RAS containing AI is procured for Defence use, the military delta in the ODD must be identified, and the AI tested so that any performance drop-off from the benign designed-for ODD is understood and the additional risks identified, with the adversary's capacity for malign action a particular concern.

On Digital Systems: their more open-loop nature means incorrect behaviour is subtler than a physical failure. Credibly incorrect outputs from generative AI, including LLMs, can mislead operators into poor decisions. The ODD must be identified including the context of use and host digital systems. AI-based digital systems within scope must be clearly identified as AI-based, and products developed with AI assistance must state that AI was used; for high-risk products, the risk owner must have relevant information on how the AI was developed, used and assured, with the risk captured in the relevant register.

## Mental Models

- Ask what class the system is in, then ask what failure looks like there: physical motion for RAS, persuasive wrongness for digital systems.
- AI advice needs provenance: where AI advises an operator, alternate information sources and their provenance should be identified so the level of AI influence on decision-making is understood, and that influence is folded into overall system risk analysis.
- Special channels get named treatment: AI used in producing official statistics must be communicated in the associated Technical Annex detailed in JSP 200.

## Anti-patterns

Reading a credible generative output as evidence of correctness: the directive's open-loop warning exists precisely because fluent wrong answers are the digital-system failure mode. Deploying an AI component without a declared ODD is another refusal shape, since the ODD anchors the testing, monitoring and assurance obligations set out in ch05 and ch08.

## Key Takeaways

- Classify the host system first (RAS or digital), then apply the requirements that the class makes relevant.
- Record and agree the AI-versus-alternatives risk judgement through the governance chain for major-and-above components.
- Autonomy level never removes the human-control requirement; it changes what context-appropriate involvement must look like.
- Identify AI in systems and products explicitly, because downstream users cannot respect limits they cannot see.

## Connects To

The human-control thread continues in ch04; the ODD anchors data, verification and monitoring duties in ch05; assurance of ODD excursions is in ch08. The accountable-owner thread runs through the governance material in ch03.

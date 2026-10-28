Sources: JSP 936 Part 1 V1.1, printed body pp. 1-5 (source Chapter 1, paragraphs 1 to 26).

# Introduction: policy, scope, applicability, tailoring

## Core Idea

JSP 936 Part 1 mandates ambitious, safe and responsible practices for every Defence project that includes AI. It implements the Defence AI Strategy and the Ambitious, Safe, Responsible (ASR) policy statement, is aligned to the Government's Technology Code of Practice, and applies to MOD staff who develop or use AI-containing systems regardless of application domain. The directive is written to be complementary to the wider software and security JSPs rather than to replace them, and it commits to review at least every two years.

On definitions, MOD deliberately avoids pinning AI to one technical boundary. It adopts a general characterisation (a defined term): machines that perform tasks normally requiring human intelligence, especially where the machines learn from data how to do those tasks. The National Security and Investments Act legal definition is named as clearer but less practical for this context. The indicative technology map in the source's Figure 1 is presented as deliberately vague and incomplete; the field moves too fast for completeness, and anything that looks like AI in software behaviour is treated as in scope unless excluded.

Dependability itself is framed relationally: how much the user can rely on safe, secure and correct operation within a given context, including mission, human involvement, environment and system constraints. The level of confidence developed in a system must be commensurate with the reliance placed upon it, and risk owners judge the adequacy of that evidence through the whole AI lifecycle. Where uncertainty is high, as in a fast-evolving operating environment, owners of resultant risk must understand and communicate it to all stakeholders.

## Frameworks Introduced

- The ASR policy chain: Defence AI Strategy, then the ASR statement, then this directive, with the MOD data and digital backbone strategies named as closely linked context.
- Reliance-confidence proportionality: no fixed dependability scale exists; confidence must match how much the system is relied upon, judged by risk owners lifecycle-wide.
- A two-part structure: Part 1 is the directive that must be followed; Part 2 would carry the guidance, and is not part of this publication or this pack.
- A directive vocabulary where must marks a compulsory requirement for the actioner and should marks recommended good practice to be applied as far as the context allows.

## Key Concepts

Scope is drawn around a broad sense of software: program code, operating procedures, relevant data, and associated documentation such as requirements, specifications, test plans and user manuals. It covers software in MOD equipment, Programmable Elements as defined by Def Stan 00-056, and software in other Defence digital information systems. Software acquisition as a whole belongs to JSP 441, JSP 604 and internal policy; where AI takes the form of a model, JSP 939 may apply and must then be used in combination with this JSP.

The applicability rule is outset-first: the requirements must be implemented from the start of all Defence capability development where MOD requirements lead to AI. Legacy AI still running or being repurposed should be aligned so far as possible, and where that is impossible, tailoring is the route. The JSP binds all MOD staff across the full system lifecycle, pre-concept to disposal, and names the stakeholders it especially addresses: S&T providers at every technology readiness level, customers and sponsors, SROs and requirements managers, Delivery Agents, DLOD owners, trials units, Specialist Engineering Functions, policy makers, and end users.

Delegation runs from the top: TLB Holders and Chief Executives issue direction and must ensure that anyone they delegate to, such as an RAISO, is competent and adequately resourced. DAU is the consultation point for policy questions and DAIC for technical guidance.

## Mental Models

- Judgment over checklists: because AI is combined with non-AI techniques until the boundary blurs, deciding which components fall in scope requires judgement, tied to existing risk management.
- In-scope examples named in the directive include object detection in ISR, reinforcement learning in command and control and autonomous systems, LLMs in HR applications, and AI in decision-support toolsets such as course-of-action development, task allocation, mission tactics engines and logistics planning.
- Out-of-scope examples include open proprietary search engines, predictive text on consumer messaging, and common office productivity tools where the risk of the resulting material is low; even there, responsible use remains the user's responsibility.

## Anti-patterns

The directive refuses to provide a dependability scale; confidence claims are always contextual, never a graded badge. Tailoring without a prior risk assessment is refused: where some requirements cannot be met, an assessment of risk must be undertaken and the additional risk managed through the AI ethical risk activities the directive sets out.

## Key Takeaways

- If a Defence project includes AI, this directive applies from the outset; proportionality comes from the maturity and nature of the application, not from opting out.
- Documentation follows the extant policy for software in the application area.
- The primary software standard named is Def Stan 00-055 for safety of Programmable Elements, which currently addresses ML only, so non-ML AI may need additional considerations; Def Stan 00-056 is relevant because AI always sits inside a larger system.
- Organisations must review the latest government and commercial standards for applicability, adopt civil standards where possible, consult military standards for the military delta, and consider even optional standards.

## Connects To

Risk management stays with JSP 892 and is not restated here. The ethics and governance machinery that tailoring escalates into is carried in ch03, and the assurance consequences of uncertain evidence in ch08. For the Defence safety management system itself, use the jsp-815 pack; for acquisition safety policy, use the jsp-376 pack.

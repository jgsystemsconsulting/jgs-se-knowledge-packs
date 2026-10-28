Sources: JSP 936 Part 1 V1.1, printed body pp. 30-31 (source Chapter 9, paragraphs 205 to 209).

# AI Assurance

## Core Idea

Assurance of AI shares many common features with its traditional software counterpart, and those traditional approaches should continue to be applied; the chapter supplies an overlay of requirements for the novel aspects AI introduces. The overlay is honest about difficulty: given the breadth of AI technologies and development approaches, the directive refuses to prescribe how to resolve every difference between traditional and AI assurance, and instead names the difference pattern and the decision rule around it.

## Frameworks Introduced

- Assurance risk: the risk associated with the assurance process itself. AI differences typically show up as imprecise requirements, reduced requirement traceability, excessive complexity, and unpredictable specific or adaptive behaviour, which make the assurance process less certain. In some applications that assurance risk is simply too much, and in those cases AI must not be adopted; where it can be tolerated, assurance activities must still be undertaken commensurate with the risk posed by incorrect AI outputs.
- System-context tolerance: some systems can tolerate a level of incorrect specific outputs provided the overall intended outcome remains acceptable, for example safe, secure and ethical. The directive marks this as possibly the key difference from traditional software assurance, and warns that without accommodating it, the potential gains of AI may be lost unnecessarily.
- The replacement argument: where AI replaces extant technology or human decision-making, AI assurance should be able to argue that the specific risk of the AI is no greater than the system replaced. The worked example is route planning: if AI plans vehicle trajectories that a human previously produced, the risk of failure should be no greater than when the human planned them.

## Key Concepts

Assurance must include behaviour when the AI excursions beyond its ODD can reasonably be expected, and in many Defence applications those excursions will be caused by adversarial action. There, careful consideration is required of failure-mode behaviour, with the directive naming the options of fail safe or fail operational designs. The level of confidence sought in assurance must be commensurate with the acceptable ethical, safety, security and mission risk associated with the function the AI provides.

Assurance sits inside the system context: the same assurance questions are asked of the AI and of the wider system it operates in, because integration effects and the tolerance of the surrounding system determine what the AI's outputs do in practice.

## Mental Models

- Assurance is a two-sided budget: one side is the risk of the AI's incorrect outputs, the other is the risk that the assurance process itself cannot see straight; both must be spent down, and if the second cannot be, the AI does not ship.
- The replaced baseline is the measuring stick: an AI does not have to be perfect, it has to be no worse than what it replaces, and the argument for that has to be made explicitly.
- ODD excursions are assumed, not exceptional: the assurance question is what the system does when it leaves its envelope, especially because an adversary pushed it.

## Anti-patterns

Adopting AI where the assurance risk cannot be tolerated is refused outright; this is the chapter's one hard stop. Demanding zero incorrect outputs in every circumstance is the opposite failure, since a blanket refusal to tolerate any specific incorrect output in a tolerant system forfeits AI's gains unnecessarily.

## Key Takeaways

- Keep traditional software assurance approaches; layer AI-specific coverage on top rather than starting over.
- Size the assurance effort by the risk of incorrect outputs and by the ethical, safety, security and mission risk of the function provided.
- Decide and document, before adoption, whether the assurance risk is tolerable for the application at hand; that decision is what the no-adoption stop hangs on.

## Connects To

The ODD, verification, monitoring and regression duties in ch05 are what assurance examines; the ethical risk rating and referral ladder in ch03 set the approvals context the assurance evidence supports; the safety-case integration named in ch06 belongs to the surrounding SMS carried by the jsp-815 pack.

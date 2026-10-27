Sources: JSP 936 Part 1 V1.1, printed body pp. 29-30 (source Chapter 8, paragraphs 198 to 204).

# Suppliers

## Core Idea

AI acquired externally must attract exactly the same level of confidence that the directive's requirements have been met as AI developed within or for MOD. Getting there is harder for AI than for traditional software, so MOD teams may need to stand up additional assurance capabilities to address evidence shortfalls when they arise. The chapter treats suppliers as part of the dependability argument rather than as a procurement afterthought.

## Frameworks Introduced

- Competence demonstration: contracting teams must require suppliers to demonstrate competence to deliver products at a confidence level commensurate with their use. The worked example is an ML model intended for a safety-related application, where the supplier must show appropriate people, processes and experience, and evidence supporting an appropriate level of confidence in the associated safety argument.
- Third-party component assurance: most AI developers use commercially available or open-source applications, tools, libraries, frameworks and data, and MOD recognises these are harder to assure to the same degree as bespoke software. Suppliers relying on them must be required to develop compelling arguments that confidence in the resulting AI has not been undermined.
- Data provenance: the provenance of all data used to train and test the AI must be assured and documented, including legal and ethical compliance in line with MOD policy, covering data supplied by MOD and third-party data alike, so the data is fit for purpose and free of adversarially introduced vulnerabilities.

## Key Concepts

Many suppliers in the AI space are new to Defence. Where they deliver directly into Defence organisations, they need to understand the Defence context: information and operational security; MOD policies, including the ASR statement and the equality, diversity and inclusion duties set out in JSP 887; MOD standards; and, where appropriate, the operational contexts their products will face.

Contracting shapes through-life dependability. Contract conditions should consider through-life support, including access to the data and algorithms as well as the resulting models, and clear ownership of intellectual property for data, algorithms, models and tests. Contracting should also address the stakeholder-understanding duties from the legal and ethics material, so the people who must understand the AI can.

Foreign export controls enter the risk picture too: assessment of restrictions should cover data as well as algorithms and models, so that MOD retains the freedom of action to maintain, modify, upgrade and operate its AI.

## Mental Models

- Same confidence, new evidence path: the bar for an externally acquired AI equals the in-house bar; what changes is how the evidence is demanded and produced, contractually.
- The supplier is inside the governance chain: context, policy and operational knowledge are transfer duties, not courtesies, because an AI built without them cannot meet the directive's context-appropriate requirements.
- Freedom of action is an assurance property: an AI you cannot legally maintain or retrain abroad is not dependable in the directive's sense, whatever its technical performance.

## Anti-patterns

Accepting a supplier's component stack as assured by its vendor popularity is refused; the burden of a compelling argument sits explicitly on the supplier. Treating data provenance as the supplier's private concern is refused, since provenance must be documented and covers MOD-supplied and third-party data equally.

## Key Takeaways

- Write the confidence requirement, the third-party argument duty, the provenance documentation duty, and the through-life access and IP terms into the contract, because after award the bargaining power mostly disappears.
- Onboard new-to-Defence suppliers into the Defence context deliberately: security, policy, standards and operational reality.
- This pack names JSP 887 and the ASR statement and does not reproduce them; the surrounding acquisition-safety machinery lives in the jsp-376 pack.

## Connects To

The data duties here extend the lifecycle data controls in ch05; supplier evidence feeds the assurance arguments in ch08; the competence and culture expectations mirror the ethics-governance duties in ch03.

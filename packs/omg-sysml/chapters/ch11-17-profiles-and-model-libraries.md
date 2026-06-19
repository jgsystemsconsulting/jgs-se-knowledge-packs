# Chapter 11: 17 Profiles and Model Libraries

## Core Idea

Profiles and model libraries are SysML's mechanisms for extending UML's metamodel to suit domain-specific purposes. Profiles allow you to specialize existing UML/SysML constructs through stereotypes, while model libraries provide reusable collections of domain elements (blocks, types, requirements) that can be tailored for automotive, aerospace, defense, or other specialized systems engineering contexts.

## Frameworks Introduced

- **`Stereotype`**: A metaclass extension that specializes an existing UML construct (e.g., a requirement, block, or operation) without creating a structural subclass. Applied to model elements via the `«stereotypeName»` notation.
  - When to use: When you need to add domain-specific properties, constraints, or semantics to an existing SysML construct without modifying its structural inheritance hierarchy.

- **`Profile`**: A UML package that groups stereotypes and related metamodel extensions. Serves as the container for domain customizations.
  - When to use: When packaging domain specializations (e.g., «functionalRequirement», «functionalBlock») for reuse across a project or organization.

- **`Model Library`** (UML `StandardProfile`): A reusable collection of pre-defined model elements—blocks, types, requirements, operations—tailored for a specific domain or system family.
  - When to use: When you have common element definitions (e.g., standard interface blocks, baseline requirements) that should be instantiated across multiple projects or variants.

- **`Extension` (graphical path)**: The directed relationship from a stereotype to the metaclass it extends, shown as a line with an extension arrow in profile definition diagrams.
  - When to use: Automatically present when you define a stereotype; it documents the semantic binding between the stereotype and its base metaclass.

- **`Metaclass`**: A UML metamodel class (e.g., Requirement, Block, Operation) that serves as the extension point for a stereotype.
  - When to use: When authoring profiles, you extend metaclasses to create domain variants (e.g., extending Requirement to create FunctionalRequirement).

## Key Concepts

- **Stereotype Application**: The act of marking a model element with a stereotype notation (e.g., `«functionalRequirement»`) to signal that it conforms to that domain specialization. The element retains its base type (Requirement) while gaining stereotype-specific properties.

- **Metaclass Extension (vs. Subclassing)**: Creating a stereotype that extends Requirement is different from UML subclassing (e.g., `class FunctionalRequirement extends Requirement`). A stereotype is a notational and property-level overlay; subclassing changes the type hierarchy itself.

- **Stereotype Properties**: Additional attributes and constraints that a stereotype defines. For example, a `«functionalRequirement»` might have a `satisfiedBy: Operation` constraint, meaning any functional requirement must be satisfied by an operation or behavior.

- **Profile Reusability**: Profiles are packaged extensions designed to be applied across projects, teams, or organizational domains. They encode domain conventions without duplicating work.

- **Model Library Content**: Reusable definitions within a model library—blocks (with interfaces and ports), value types, operations, requirement hierarchies—serve as templates or base implementations that projects specialize or instantiate.

- **Domain Customization**: Profiles and libraries together enable SysML customization for sectors such as automotive systems, military platforms, or space systems, each with distinct engineering standards, terminology, and constraints.

## Mental Models

- **Use stereotypes for notational and semantic tagging, not structural inheritance.** If you want to add properties to all requirements in a domain (e.g., "verification method"), define a stereotype with those properties and apply it; do not create a UML subclass.

- **Model libraries as domain-specific "kits."** Populate a library with pre-configured blocks, types, and requirement patterns that your domain expects. Teams instantiate or refine these rather than building from scratch.

- **Profile definition happens in a separate, metadata-level diagram space.** Profile diagrams show stereotypes extending metaclasses (not model elements extending each other). Once a profile is defined, you apply it to regular model elements in your design.

## Anti-patterns

- **Overusing subclassing when a stereotype suffices**: Creating a deep inheritance hierarchy of requirement types (FunctionalRequirement → SafetyRequirement → ...) instead of using orthogonal stereotypes. Stereotypes compose and apply flexibly; subclasses commit to a rigid hierarchy.

- **Ignoring stereotype constraints**: Defining a stereotype that mandates a certain relationship (e.g., "must be satisfied by a block") but not enforcing it in the model or tooling. Stereotype definitions should encode both properties and validation rules.

- **Model library bloat without curation**: Accumulating hundreds of undefined block templates in a library without documented purpose or reuse patterns. Libraries should be curated, documented, and version-controlled.

## Key Takeaways

1. **Stereotypes are the primary extension mechanism for SysML profiles.** Use them to extend UML metaclasses (Requirement, Block, Operation, etc.) for domain-specific variants; they are lightweight, reusable, and do not alter the metamodel itself.

2. **Profiles are metamodel customizations; model libraries are asset collections.** Profiles define extensible stereotypes; libraries populate those definitions with concrete, reusable elements (blocks, types). Both support domain tailoring.

3. **Notation «stereotypeName» signals both intent and constraints.** When you see `«functionalRequirement»`, you know the element is a requirement with domain-specific semantics and validation rules. Use this notation consistently in your models.

4. **Stereotype properties and constraints are the gateway to automation.** Once a stereotype is applied, tools can validate constraints (e.g., "this functional requirement must be satisfied by exactly one operation"), trace compliance, and generate reports.

5. **Model libraries encode organizational patterns.** Invest in curating a domain-specific library (e.g., standard interface blocks for avionics, baseline requirements for automotive safety) to accelerate project onboarding and enforce consistency.

6. **Profiles support iterative domain refinement.** Start with a minimal profile (a few stereotypes for your most-used elements), apply it across a pilot project, and evolve it based on what you learn. Versioning and inheritance of profiles (one profile extending another) are supported.

## Connects To

- **UML 2.5.1 Profiles**: SysML profiles inherit their mechanism from UML. The underlying stereotype and extension semantics are defined by OMG UML; SysML adds notational conveniences (stereotype property compartments, notes) and domain specializations.

- **SysML Diagram Taxonomy**: Profiles are defined using UML class and composite structure diagram notations. Profile diagrams are not a distinct SysML diagram type; they are metaclass-level representations of how stereotypes extend metamodel elements.

- **SysML Model Elements and Metaclasses (Clauses 5–15)**: Every SysML construct (Block, Requirement, Activity, etc.) is a potential extension point for a stereotype. Understanding the semantics of the base metaclass is essential before extending it.

- **ISO/IEC 42010 (Architecture Description)**: Viewpoints and view definitions in 42010 can be realized as SysML profiles, allowing standardized viewpoint libraries to be packaged and reused across organizations.

- **OMG MOF (Meta Object Facility)**: SysML profiles conform to MOF metamodel structuring principles. Profiles are layered above UML's metamodel in the same way UML is layered above MOF.

- **Annex E (Non-normative Extensions)**: Provides extended worked examples of profile creation (e.g., FunctionalRequirement, SafetyRequirement stereotypes and their application).

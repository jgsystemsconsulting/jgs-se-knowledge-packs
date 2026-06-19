# Chapter 5: Data and Information Viewpoint (DIV)

## Core Idea
The Data and Information Viewpoint models the information and data that decision-makers need to perform their activities. Unlike every other viewpoint, DIV models are cross-cutting: their content may draw on **any combination** of DM2 data groups, and the three DIV models look at the same enterprise-wide information from three successively more concrete levels of abstraction — conceptual, logical, and physical. This three-level stack is the DoDAF's formal treatment of the information modeling problem.

## Frameworks Introduced
- **DIV-1: Conceptual Information Model**: Identifies and describes the concepts that decision-makers must understand to make decisions within the scope of the architecture. Uses super-subtype and whole-part relationships rooted in DoDAF genus terms. No physical implementation implied.
  - When to use: Early in an architecture effort when establishing a shared understanding of what the enterprise deals with; for stakeholder communication and COI harmonization.
- **DIV-2: Data Requirements Model**: Reifies DIV-1 concepts into specific information requirements — what exactly decision-makers need to know about each concept (completeness, correctness, consistency). May model mesodata, metadata, and microdata requirements.
  - When to use: During requirements definition when specifying what data must be available, to whom, when, where, and with what accuracy and confidence.
- **DIV-3: Data Implementation Model**: Specifies data structures and data elements that satisfy DIV-2 requirements in a physical medium (database schemas, message formats, class specifications, web pages). Must comply with metadata standards from the Standards Viewpoint.
  - When to use: During design and implementation when specifying database schemas, message exchange formats, or cybernetic (human-machine) interfaces; for configuration management of data assets.

## Key Concepts
- **Information** — A representation of a thing of interest; the state of something materialized and communicated. Can describe other information (metadata). Any textual description is a long name in DM2 terms. Information is a subtype of Resource.
- **Data** — Proceduralized information — encoded for repeatable processing by humans or machines. Not all proceduralized information is computerized (forms are an example).
- **Conceptual Level** — Defines and relates terms as concepts; understandable by enterprise experts. Uses Entity-Relationship or UML Class style. Super-subtype and whole-part relationships provide cognitive economy.
- **Logical Level** — Adds cardinalities, normalization rules, and reification of relationships. More parts than the conceptual model but still readable by enterprise experts.
- **Physical Level** — Specifies exact storage, exchange, and processing mechanisms: relational databases, message exchange formats (XML/XSD), cybernetic interfaces. Efficiency, reliability, and repeatability are primary concerns at this level.
- **Mesodata** — Data about the internal structure of an information resource.
- **Metadata** — Data that guides interpretation of data values (e.g., units, scale, authority).
- **Microdata** — Data characterizing the integrity of specific data values (e.g., pedigree, confidence).
- **COI (Community of Interest)** — A group that shares information needs and vocabulary. DIV models can reveal COI overlaps and enable harmonization.
- **Data Normalization** — Structural modification to ensure freedom from undesirable insertion/update/deletion anomalies; uncovers additional business rules.

## Mental Models
- Use DIV-1 when Y = "what concepts must be understood?"; use DIV-2 when Y = "what data must be provided?"; use DIV-3 when Y = "how must data be stored or exchanged?". The three levels answer progressively more concrete questions about the same subject matter.
- The DIV stack is the architecture's contract for interoperability: DIV-1 says what matters, DIV-2 says what must be captured about it, DIV-3 says how it will travel.

## Anti-patterns
- Mixing abstraction levels: DIV-3 must satisfy every DIV-2 requirement and may not introduce concepts unrelated to specific implementations. Adding new concepts at DIV-3 without a DIV-2 requirement is a scope violation.
- Conflating AV-2 and DIV-1: AV-2 defines the architectural vocabulary; DIV-1 models the information concepts needed for decision-making within the architecture. They may overlap but serve different purposes.
- Using DIV-3 as a database design document without DIV-1/DIV-2 backing: DIV-3 data elements must trace to requirements, not be invented at the physical level.

## Key Takeaways
1. DIV is the only DoDAF viewpoint where all three models look at the same subject at different abstraction levels — it is not three different topics, it is one topic seen three ways.
2. DIV-1 is rooted in DoDAF genus terms; any concept introduced must be a subtype or part of an existing DoDAF concept.
3. DIV-2 addresses the five rights: right data, right decision-maker, right time, right place, right form.
4. DIV-3 must comply with metadata standards established in the Standards Viewpoint — it is not an isolated implementation artifact.
5. DIV models can span enterprise-wide scope — they are not constrained to data groups of a single viewpoint.

## Connects To
- **Chapter 2 (DM2 Data Groups)**: The Information and Data group is the DM2 counterpart; DIV viewpoint models present this group at three abstraction levels.
- **Chapter 10 (Standards Viewpoint)**: StdV-1/StdV-2 standards apply to DIV-3 data element specifications.
- **Chapter 7 (Operational Viewpoint)**: OV-3 identifies information resources exchanged between organizational performers — these feed DIV-1 and DIV-2 content.
- **Chapter 9 (Services Viewpoint)**: Service descriptions (SvcV-1) reference DIV information models to specify what information a service provides access to.

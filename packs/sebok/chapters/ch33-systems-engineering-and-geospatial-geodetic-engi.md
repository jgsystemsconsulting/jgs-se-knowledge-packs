# Chapter 33: Systems Engineering and Geospatial/Geodetic Engineering

## Core Idea
Geospatial and geodetic engineering technologies—including GIS, GNSS/GPS, map projections, and spatial reference systems—are fundamental to systems design wherever location-based data, navigation, positioning, or geographic context matters; systems engineers must integrate GGE subject matter experts early to manage dependencies, ensure resilience, and optimize lifecycle costs.

## Frameworks Introduced
- **Geographic Information Systems (GIS)**: A software and methodological framework for capturing, storing, analyzing, and visualizing spatial data in application domains ranging from agriculture to military C4ISR systems.
  - When to use: Systems involving stationary or dynamic geographic features, environmental impact analysis, decision support requiring spatial context, logistics optimization, or infrastructure management.

- **Positioning, Navigation and Timing (PNT)**: A service triad from GNSS (GPS, GLONASS, Galileo, Beidou) providing positioning accuracy, navigation capability, and extremely precise time synchronization.
  - When to use: Any system requiring accurate location, motion tracking, timestamp integrity, or time-synchronized operations; critical for transport, energy, financial services, and communications.

- **Geodetic Reference Frames (Geodetic Datum/Ellipsoid)**: Mathematical and physical frameworks anchoring all coordinate systems (horizontal and vertical) to the Earth, enabling numeric description of objects in space.
  - When to use: When system design must reference global (WGS84), regional, or local coordinate systems; mandatory for interoperability across spatial data.

- **Feature Catalogues and Vector Models**: Structured definitions of what real-world objects and their attributes should be represented in a geographic database (e.g., street width, building height).
  - When to use: Modeling discrete objects in GIS; domain-specific examples include DGIWG Feature Data Dictionary (DFDD) for military applications.

- **Digital Terrain Models (DTM) and Map Projections**: Mathematical techniques to represent 3D Earth surfaces in 2D (or 3D virtual) form, selecting projection type (Mercator, Stereographic, etc.) based on application needs.
  - When to use: Visualization and spatial analysis; choice of projection affects distortion, navigation properties (e.g., Mercator for maritime, Stereographic for aeronautics).

## Key Concepts
- **Geospatial/Geodetic Engineering (GGE)**: The discipline providing frameworks, data, and techniques for systems whose function or deployment depends on location, spatial relationships, or precise coordinate referencing.
- **Interoperability Standards**: Open Geospatial Consortium (OGC), ISO/TC 211, International Hydrographic Organization (IHO), and NATO standards for GIS and sensor system interoperability; studies show adoption yields 119–163% ROI over 5–10 years.
- **Critical Infrastructure Dependency**: National critical infrastructures (energy, transport, telecommunications, financial services, search-and-rescue) are now dependent on GNSS signal availability, making PNT resilience a systemic concern.
- **Holdover Technology**: Redundancy mechanism allowing systems to operate safely for up to three days without GNSS signals during jamming or outages.
- **Discrete vs. Continuous Spatial Representation**: GIS models either discrete objects (features with boundaries and attributes) or continuous fields (variables defined at every position, like temperature).
- **Spatial Reference System**: Establishes how coordinates relate to Earth; includes horizontal (latitude/longitude on ellipsoid) and vertical (height referenced to geoid or ellipsoid) dimensions.
- **Cartography**: The science and practice of abstracting, simplifying, and visualizing geographic data according to display scale, human perception, and application-specific rules.

## Mental Models
- **Use GGE as a Specialty Engineering discipline**: Whenever a system performs navigation, manages referenceable objects, displays geographic context, or depends on GNSS, integrate GGE expertise into the SE team—do not relegate it to vendor default behavior.
- **Think of GIS as a modeling and decision-support platform**: GIS is not just visualization; it enables scenario analysis, trade-off optimization (cost vs. deployment variants), and formal geometric modeling required in SE lifecycle activities (concept formulation, architecture design, training support).
- **Frame PNT resilience as a system safety concern**: Systems relying on GPS/GNSS require explicit design for fault tolerance and graceful degradation; consider holdover technology, eLoran alternatives, or Satelles as architectural choices when signal loss poses risk.
- **View spatial data quality as a lifecycle cost driver**: Maintaining geospatial databases is costly; leverage centralized data services (single source of truth) to reduce update burden and ensure availability constraints are met.

## Anti-patterns
- **Ignoring GGE dependencies until late in design**: Systems critically dependent on GNSS or geographic context should identify GGE needs during concept formulation and architecture phases, not integration.
- **Treating geospatial data as static or "good enough"**: Geospatial databases require active maintenance and updates; systems must design for data refresh, reliability, and source traceability—outdated maps or coordinate errors propagate system-wide failures.
- **Relying solely on GPS without resilience safeguards**: The 2017 Hamburg G20 intentional GPS jamming warning and documented vulnerabilities show that systems assumed to have signal availability must design alternative time sources and navigation modes.
- **Overlooking interoperability standards in multi-domain systems**: Custom proprietary geospatial formats increase lifecycle costs; standards-based approaches reduce maintenance and interoperability risk.

## Key Takeaways
1. **Geospatial technologies are not optional for location-aware systems**: Whether supporting environmental analysis, logistics, safety monitoring, or navigation, GGE must be integrated early into systems engineering activities; the alternative is costly rework and vulnerability.
2. **PNT is a shared critical resource**: GNSS signals support power grids, transportation networks, financial systems, and emergency services; system design must account for signal loss and include resilience mechanisms (holdover, redundancy).
3. **GIS scales from stand-alone systems to systems-of-systems**: GIS enables mission concept evaluation, architecture optimization, integration support, and virtual training environments; treat it as a formal modeling tool, not an afterthought.
4. **Interoperability standards (OGC, ISO/TC 211) pay for themselves**: Adopting geospatial standards yields measurable ROI (119–163%) over the system lifecycle and reduces maintenance burden in multi-supplier environments.
5. **Spatial reference systems (geodetic data, ellipsoids, projections) are foundational**: All numeric descriptions of objects must anchor to a geodetic datum; misalignment across subsystems or suppliers causes integration failures—establish reference system requirements early.
6. **GIS and Human Factors Integration are inseparable**: Geographic displays often dominate user interfaces; system usability depends on proper application of cartographic principles (generalization, symbolization, scale-dependent presentation) alongside HFE analysis.
7. **Modeling and simulation for deployment/operations benefits from geospatial data**: Realistic 2D/3D/4D environments (Digital Terrain Models + imagery) support concept evaluation and ConOPS analysis; geospatial technologies provide data to create and update those environments cost-effectively.

## Connects To
- **ISO/IEC/IEEE 15288 (System Life Cycle Processes)**: GGE contributions span stakeholder needs definition (spatial requirements), system design (coordinate systems, interoperability), and verification (geodetic survey, positional accuracy).
- **SE and Environmental Engineering**: Pollution dispersal, flooding simulation, run-off analysis, and environmental impact assessment rely on GIS modeling and spatial analysis.
- **SE and Safety Engineering**: Monitoring of critical structures (dams, bridges), volcanoes, fracture zones, and earthquake-prone areas; deformation analysis via geodetic techniques.
- **SE and Logistics Engineering**: Route planning, transportation optimization, facility management (BIM/GIS integration), cargo tracking, and supply chain visualization using GNSS and GIS.
- **SE and Quality Attributes** (Reliability, Availability, Maintainability): Geospatial data reliability, database update costs, IT infrastructure availability for geospatial services, and redundancy in PNT systems.
- **Open Geospatial Consortium (OGC), ISO/TC 211**: Standards bodies for GIS interoperability, geospatial data encoding, and sensor system integration—critical for multi-vendor, multi-domain systems.
- **INCOSE Specialty Engineering Disciplines**: GGE is recognized as a specialty engineering activity across affordability analysis, resilience design, interoperability assessment, and human systems integration.


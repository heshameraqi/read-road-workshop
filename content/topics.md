# Research Topics

We invite submissions spanning the full pipeline from visual observation to structured map knowledge.

## Traffic Sign/Signal ↔ Map Element Association
- icon: fa-traffic-light
- description: Detecting traffic signs and signals in imagery is well-studied, but associating a detected sign with the correct road segment, intersection, or lane in a map graph remains an open challenge involving spatial reasoning, occlusion handling, and many-to-many matching.

## Visual Map Attribute Inference
- icon: fa-road
- description: Street-level imagery contains rich cues about road properties—speed limits, lane counts, surface type, access restrictions—that are expensive to annotate manually. We seek methods that infer these attributes reliably from visual observations alone or in combination with sparse map priors.

## Change Detection for Map Maintenance
- icon: fa-exchange-alt
- description: Maps decay the moment they are published. We invite work on detecting conflicts between new visual observations and existing map data, including construction zones, new signage, altered lane configurations, and removed infrastructure.

## Vision-Language Models for Geospatial Reasoning
- icon: fa-brain
- description: VLMs excel at describing scenes but struggle with the precise spatial and topological reasoning required to place observations within a map coordinate frame. This theme explores prompting strategies, fine-tuning approaches, and hybrid architectures that ground VLM outputs in map structures.

## Graph Neural Networks for Road Network Understanding
- icon: fa-share-alt
- description: Road networks are naturally graphs. GNNs offer principled tools for attribute propagation, link prediction, and conflation, yet their application to map construction and maintenance is nascent. We welcome work on topology-aware encodings and message-passing schemes tailored to road graphs.

## Scene Graph ↔ HD Map Alignment
- icon: fa-layer-group
- description: Autonomous vehicles increasingly rely on scene graphs as an intermediate representation. Aligning detected scene elements (lanes, barriers, crosswalks) to structured HD map layers poses unique challenges in representation, registration, and uncertainty quantification.

## Sensor-to-Map Conflation
- icon: fa-satellite
- description: Matching heterogeneous sensor streams—GPS traces, camera observations, LiDAR scans—to existing map features is a prerequisite for map updating. We seek advances in learned matching, registration under noise, and fusion of multi-modal evidence.

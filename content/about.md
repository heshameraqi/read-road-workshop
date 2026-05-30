# About the Workshop

Maps are the silent backbone of navigation, autonomous driving, urban planning, and logistics. Yet the process of constructing and maintaining accurate, richly-attributed maps remains surprisingly manual and brittle.

Meanwhile, vision-language models (VLMs) can now describe street scenes with remarkable fidelity, graph neural networks (GNNs) can encode complex road topologies, and foundation models for geospatial data are rapidly maturing. What is missing is **the bridge**: the ability to read visual observations into structured map knowledge—detecting what has changed, inferring latent attributes, and associating observations with the correct map elements at scale.

This workshop brings together researchers from **computer vision**, **natural language processing**, **graph machine learning**, **autonomous driving**, and **geospatial science** to tackle the end-to-end pipeline of visual observation → structured map knowledge. We aim to catalyze a new research community at the intersection of these fields, establishing shared problems, benchmarks, and representations.

## Why This Workshop?

- **VLMs can "see" roads but cannot "read" them into maps.** State-of-the-art VLMs produce impressively detailed scene descriptions, yet translating these outputs into structured, actionable map updates requires spatial grounding, topological reasoning, and schema-aware generation that current models lack.

- **Map freshness is an industry-critical bottleneck.** Commercial map providers estimate that 10–15% of road attributes change annually. Fleet operators, autonomous vehicle developers, and routing services depend on up-to-date maps, yet current update pipelines involve weeks-to-months latency.

- **GNNs + vision convergence is underexplored.** The graph ML community and the computer vision community each bring powerful tools to this problem but rarely collaborate. Road networks are a natural meeting point: they are spatial, visual, and graph-structured simultaneously.

- **No unifying venue exists.** Related work is scattered across venues for autonomous driving (CVPR workshops), geospatial AI (AAAI, SIGSPATIAL), and graph learning (GLFrontiers). No single venue addresses the full pipeline from visual observation to map knowledge.

## Why Now?

- **Explosion of VLMs with spatial reasoning.** Models such as GPT-4o, Gemini, and domain-specific geospatial VLMs have demonstrated nascent spatial reasoning capabilities.
- **Autonomous driving matures beyond perception.** The industry is shifting from object detection to full scene understanding and map integration.
- **Foundation models for geospatial data are emerging.** Models pre-trained on satellite imagery, street-level photos, and GPS traces provide powerful feature backbones.
- **Map freshness crisis.** The proliferation of delivery robots, ride-hailing fleets, and micro-mobility services has amplified the cost of stale maps.
- **Graph ML + vision convergence is new and active.** Recent works on scene graphs, topology-aware lane detection, and graph-based HD map prediction signal a growing intersection.

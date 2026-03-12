## Meeting Notes

### Attendees
- Felix George (IBM Research)
- Mudit Verma (IBM Research)
- Gerard Vanloo (IBM Research)
- Rohan Arora (IBM Research)
- Cyrille Le Clerc (Grafana)
- Jonathan Munz (Embrace)
- Donal O’Sullivna (Elastic)
- Felix George (IBM Research)
- Divya Pathak (IBM Research)
- Anoushka Nag (IBM Research)
- Shenoy Pratik (OpenSearch)

### Agenda
- **Agentic Version of Astronomy Shop (Agent Astronomy Shop)**
  - **Context**: The **Astronomy Shop** has long been a widely used microservice-based benchmarking application, serving as a valuable platform for innovation in the IT operations space across both industry and academia. With the rise of **agentic workloads**, it would be beneficial to introduce a reference agentic application that enables the community to experiment with agentic systems. Such a platform could generate rich telemetry, including both agentic and non-agentic trajectories, and provide a foundation for advancing the innovation in GenAI space and enhanced capabilities across multiple dimensions, such as resilience, performance, and overall system reliability.
  - **What We have**:
    - **Agentified Astronomy Shop**: At IBM Research, we have created an agentic version of astronomy shop, where backend microservices becomes the tool, and the frontend becomes the langgraph based agent. We also have the chatBotUI to interact with the application as opposed to a web page that the astronomy shop had.
    - **Agentic Load Genenator:** Prompt based load generation to agent astronomy shop with varied complexity of prompts invoking one or multiple astronomy shop tools in varied planning complexities (microservices).
    - **Agentic Fault Injector**:  Component with UI to inject a variety of agentic and system faults into the agent astronomy shop and its various components, including calls to tools and LLM.
    - **Observability:** Otel Compliant observability including logs, metrics and traces.
  - **Demo**: We would like to demonstrate the implemented system to the community and seek feedback for potential absorption into Otel Demo as a reference agentic system.

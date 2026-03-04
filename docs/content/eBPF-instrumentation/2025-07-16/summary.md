## Key Topics
- Discussion on Java TLS support and its importance for OpenTelemetry.
- Challenges with implementing TLS support in Java due to JVM's native implementation and uprobe limitations.
- Proposal for a small agent to dynamically load alongside the JVM for better instrumentation.
- Concerns about potential conflicts with existing OpenTelemetry Java agents.
- The need for flexibility in instrumentation methods beyond eBPF for certain use cases.

## Action Items
- Evaluate the feasibility of developing a standalone agent for TLS support in Java.
- Investigate the integration of dynamic loading of the OpenTelemetry Java agent with existing instrumentation.
- Consider community feedback on the proposed solutions and potential conflicts with other agents.

## Participants
Tyler Yahn, Mike Dame, Mattia Meleleo, Stephen Lang, Nikola Grcevski, Rafael Roquetto

## Key Topics
- **Demo of OpenTelemetry eBPF Instrumentation**: Nimrod presented a demo showcasing the OpenTelemetry demo with microservices, highlighting modifications made to enhance observability.
- **Context Propagation Issues**: Discussion on challenges with context propagation between services, particularly across different nodes, and potential solutions involving C group versions.
- **Kafka Integration Challenges**: Issues with Kafka message metadata and suggestions for enriching messages to improve traceability.
- **Observability Enhancements**: Insights on achieving complete observability with the current setup and minor bugs encountered during implementation.

## Action Items
- Investigate C group version compatibility issues and their impact on context propagation.
- Explore the possibility of enriching Kafka message metadata to improve traceability.
- Review the architecture diagram and identify potential connection issues with Kafka clients.

## Participants
Rafael Roquetto, Tyler Yahn, Nikola Grcevski, Nimrod Avni, Mattia Meleleo

## Key Topics
- Discussion on the use of finalizers in the OpenTelemetry Kubernetes Operator and their impact on namespace deletion.
- Overview of the cluster observability documentation and the development of a new controller for managing observability.
- Considerations for testing and guarantees regarding telemetry data consistency across versions.
- Exploration of deployment strategies for telemetry collectors, including daemon sets and cluster deployments.

## Action Items
- Evaluate the necessity of finalizers and consider making their use conditional based on the presence of cluster resources.
- Gina to create PRs for the cluster observability design document and POC.
- Discuss testing strategies and establish a framework for ensuring telemetry data consistency.

## Participants
Antoine Toulme, jea, Mikołaj Świątek, Mátyás Végh, Jina, Pavol Loffay

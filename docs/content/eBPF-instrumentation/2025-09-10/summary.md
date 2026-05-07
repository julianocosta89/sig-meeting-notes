## Key Topics
- **GKE Autopilot Support**: Discussion on the challenges of running OpenTelemetry agents with elevated permissions on GKE Autopilot and potential collaboration with Grafana.
- **gRPC Instrumentation Issues**: Addressing the problem of excluding already instrumented gRPC services and exploring heuristics for better detection.
- **Network Observability Tracer Refactor**: Rafael presented a significant refactor aimed at optimizing the Network Observability Tracer by reducing context switches and improving data handling.
- **Internal Metrics and Trace Export**: Discussion on internal metrics for trace exports and ensuring no unnecessary spans are generated, which could confuse users.
- **Tooling Updates**: Introduction of Go 1.24 features for managing internal tools and dependencies more effectively.

## Action Items
- **Follow-up on GKE Autopilot**: Nikola to investigate how Grafana's Bela and Alloy were registered as Autopilot partners and explore similar registration for OpenTelemetry agents.
- **gRPC Detection Improvements**: Team to implement additional heuristics for detecting gRPC traffic based on ports and environment variables.
- **Review Open PRs**: Team members to review and provide feedback on ongoing PRs related to metrics and tracer refactoring.
- **Debugging Failing Tests**: Rafael to investigate failing Kubernetes tests and collaborate with Mario for troubleshooting.

## Participants
Rafael Roquetto, Tyler Yahn, Nimrod Avni, Mattia Meleleo, Mario Macias, Nikola Grcevski

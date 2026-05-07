## Key Topics
- Discussion on the PR regarding the duplication of model code and the need to manage it better between different usages.
- Plans for enhancing the OpenTelemetry operator to improve user experience and reduce complexity for customers.
- Challenges faced with OpenShift integration and the need for a more streamlined installation process without CRDs.
- Exploration of using a managed custom resource (CR) to simplify instrumentation and configuration for users.
- Concerns about the performance impact of the current webhook implementation and potential optimizations.

## Action Items
- Antoine to open a Jira ticket to address customer concerns about OpenTelemetry's integration with OpenShift.
- Follow up on the instrumentation code refactor and explore caching strategies to reduce API server load.
- Investigate the feasibility of embedding instrumentation CR directly into operator configuration to simplify user experience.

## Participants
Antoine Toulme, Jacob Aronoff, ploffay

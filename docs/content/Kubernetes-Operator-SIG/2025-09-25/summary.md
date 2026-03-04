## Key Topics
- Discussion on the use of finalizers in the OpenTelemetry Kubernetes Operator and their impact on resource cleanup.
- Challenges faced with namespace-bound deployments and the race conditions during namespace deletions.
- The role of owner references in managing cluster-scoped resources and the limitations of finalizers.
- Considerations for improving the operator's cleanup mechanisms without relying heavily on finalizers.

## Action Items
- Explore the possibility of conditionally adding finalizers only when necessary.
- Investigate the implementation of owner references for cluster roles to enhance cleanup processes.
- Review the current operator behavior during namespace deletions and assess potential improvements.

## Participants
Antoine Toulme, jea, Mikołaj Świątek, Mátyás Végh, Vincent de Bois

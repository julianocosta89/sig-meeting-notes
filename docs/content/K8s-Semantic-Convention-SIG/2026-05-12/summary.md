## Key Topics
- Discussion on CPU modes and the potential removal of the 'other' category in CPU metrics.
- Controversy surrounding CPU usage metrics in Kubernetes and the proposal to focus on utilization metrics instead.
- The need for alignment between OpenTelemetry and host metrics receiver regarding CPU time and utilization calculations.
- Consideration of a feature gate for implementing changes in CPU metrics.
- The inconsistency in how Kubernetes computes CPU usage and the implications for OpenTelemetry metrics.

## Action Items
- Finalize the decision on whether to remove the 'other' CPU mode from the documentation.
- Document the approach for calculating utilization metrics and how it aligns with host metrics receiver.
- Update the issue regarding the implementation of CPU metrics based on the discussions held.

## Participants
Christos Markou, Stephen Lang, David Ashpole, Dmitrii Anoshin, João Marques Correia, Jina

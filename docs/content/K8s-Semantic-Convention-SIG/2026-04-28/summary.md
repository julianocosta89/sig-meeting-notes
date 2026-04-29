## Key Topics
- Discussion on using container namespace vs. kh.container namespace for metrics.
- Ongoing issues regarding file system container metrics and log usage specific to Kubernetes.
- Proposal to deprecate generic metrics in favor of Kubernetes-specific metrics.
- Need for revisiting container utilization metrics and their definitions.
- Concerns about the fixed sampling window in Kubernetes metrics affecting data accuracy.

## Action Items
- Revisit the existing metrics to determine if the generic metrics should be deprecated.
- Share the non-normative guide on CPU principles related to metrics.
- Consider adding metrics for empty dir volumes at the pod level in the future.

## Participants
Christos Markou, João Marques Correia, Stephen Lang, David Ashpole, Dmitrii Anoshin

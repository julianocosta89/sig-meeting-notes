## Key Topics
- Discussion on the use of container namespace vs. kube.container namespace for metrics.
- Ongoing considerations for Kubernetes-specific metrics, particularly around log usage and file system metrics.
- Debate on whether to deprecate existing metrics or maintain them with clearer documentation.
- The implications of Kubelet's fixed sampling window on metric accuracy and usefulness.
- Future of CAdvisor and its metrics within Kubernetes.

## Action Items
- Revisit the existing metrics to determine if they should be deprecated or maintained.
- Document the specific behaviors and caveats of Kubernetes metrics clearly.
- Consider moving certain metrics to the Kubernetes namespace for clarity.

## Participants
Christos Markou, João Marques Correia, Stephen Lang, David Ashpole, Dmitrii Anoshin

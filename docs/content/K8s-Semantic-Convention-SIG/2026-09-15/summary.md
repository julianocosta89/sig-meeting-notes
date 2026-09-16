## Key Topics
- Discussion on the deprecation of node utilization metrics and transition to stable metrics.
- Proposal for adding object creation time as an attribute for Kubernetes objects, with comparisons to existing metrics.
- Use cases for tracking pod start times and the importance of having both start time and creation time for better UI representation.
- Consideration of whether to implement creation time as an attribute or a metric, with a consensus leaning towards starting with an attribute.

## Action Items
- Review the PR for marking node utilization metrics for deprecation.
- Gather specific use cases from the community regarding the need for creation time as an attribute or metric.
- Approve the PR for adding creation time as an optional attribute if no objections arise.

## Participants
Stephen Lang, Christos Markou, David Ashpole, Jina Jain

## Key Topics
- Discussion on updating memory usage metrics in the host metric receiver to use the more accurate "available" memory metric instead of the current derived usage metric.
- The need for alignment with industry standards and practices regarding memory metrics, particularly in light of changes made in common Linux tools.
- Proposal to create a feature gate for the new memory calculation and to document the changes through a blog post.
- Ongoing discussions about moving components to stable semantic conventions and the approach for adopting Kubernetes-specific metrics.

## Action Items
- Roger Coll to share a gist or small program demonstrating the memory metric discrepancies.
- Consider creating a pull request to the semantic conventions to reflect the proposed changes in memory calculation.
- Plan to document the changes and rationale in a blog post to raise visibility.
- Internal discussions to prioritize addressing unknowns related to the adoption of stable semantic conventions.

## Participants
Dmitrii Anoshin, Roger Coll, Fraggle Rock, Christos Markou

## Key Topics
- **Promoting remaining K8s metrics to release candidate:** Two PRs (volume and utilization metrics) are open for review. Once merged, the metrics go into the Kubeletstats receiver behind feature gates to gather user feedback before stabilizing. Volume metrics are mostly a rename (pod-based naming) plus a persistent volume name attribute. Utilization metrics add request/limit and desired/actual concepts.
- **Migration documentation:** The OTel migration page must be kept current, and it is maintained manually. Tyler will check that the new metrics and attributes are listed when reviewing the PRs.
- **Volume metadata:** Stuart asked about exposing the backing CSI driver. Christos noted that volume type and PV/PVC names already allow linking to more detail.
- **Controller ownership attribute:** Stuart proposed a `controlled-by` attribute (API version, kind, name, UID) for parity with kube-state-metrics, avoiding the ambiguous "workload" definition. David raised questions about single-level versus top-level owner resolution and collector API load. Christos suggested that this may duplicate the entity relationship model, which is still being implemented.

## Action Items
- Review the two RC PRs for volume and utilization metrics (all reviewers).
- Tyler Helmuth: verify the migration page includes the new metrics and attributes when reviewing the PRs.
- Christos Markou: share the link on entity relationship support in the spec and tooling on Slack.
- Stuart Buckingham: wait for triage, then open a PR for the `controlled-by` attribute, and explore whether it can be expressed using the entities model.

## Participants
Christos Markou, Tyler Helmuth, Stuart Buckingham, David Ashpole

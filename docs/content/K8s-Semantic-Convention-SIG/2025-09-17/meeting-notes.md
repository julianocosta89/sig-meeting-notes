## Meeting Notes

### Attendees
- Christos Markou (Elastic)
- Stephen Lang (Grafana Labs)
- David Ashpole (Google)

### Agenda
- [status update] Introducing the Stability board: [https://github.com/orgs/open-telemetry/projects/114/views/7](https://github.com/orgs/open-telemetry/projects/114/views/7)
- [status update] Few leftovers to complete the initial definition of the K8s metrics: [https://github.com/open-telemetry/semantic-conventions/issues/1032](https://github.com/open-telemetry/semantic-conventions/issues/1032)
  - [K8s.pod.phase](https://github.com/open-telemetry/semantic-conventions/pull/2488) PR should be unblocked now
  - [K8s memory metrics PR](https://github.com/open-telemetry/semantic-conventions/pull/2776)
  - [PR](https://github.com/open-telemetry/semantic-conventions/pull/2779) for some openshift metrics
- We will start small during the stability phase, declaring small subsets of metrics as stable in RCs while also working on PoC-ing these in the Collector. More details about the process coming soon.

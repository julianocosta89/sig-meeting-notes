## Meeting Notes

### Attendees
- **[David Ashpole](mailto:dashpole@google.com)**
- Stephen Lang (Grafana)
- Joao Correia (Elastic)
- Dmitry Anoshin (Splunk)
- Christos Markou (Elastic)
- Jina Jain (Splunk)

### Agenda
- [Christos] cpu.mode final review? -> [https://github.com/open-telemetry/semantic-conventions/pull/3700](https://github.com/open-telemetry/semantic-conventions/pull/3700)
  - Christos to remove the extra note to avoid confusion.
- [Christos & Joao] Shall we deprecate the *cpu.usage metrics? Please provide feedback ->[https://github.com/open-telemetry/semantic-conventions/issues/2418](https://github.com/open-telemetry/semantic-conventions/issues/2418)
  - We can start with the implementation of cpu.utilisation metrics based on collector’s interval and see how it looks like.
  - [https://github.com/kubernetes/kubernetes/blob/17274240a1d95ea698a5bb5fc04c65eebb17bf80/pkg/kubelet/stats/cri_stats_provider.go#L55](https://github.com/kubernetes/kubernetes/blob/17274240a1d95ea698a5bb5fc04c65eebb17bf80/pkg/kubelet/stats/cri_stats_provider.go#L55)

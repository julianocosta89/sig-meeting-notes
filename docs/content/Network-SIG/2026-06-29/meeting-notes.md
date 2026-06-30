## Meeting Notes

### Attendees
- Rob Cowart (ElastiFlow)
- Sven Cowart (ElastiFlow)
- Mario Macias (Grafana)
- Stephen Lang (Grafana)
- Giuseppe Ognibene (Coralogix)
- Braydon Kains (Google)
- Antonio Jimenez (Cisco ThousandEyes)

### Agenda
- [Rob Cowart] Things/Questions I have been thinking about, and looking for input
  - Entities (interfaces, VLANs, tunnels, adjacencies/peers) - both to model/discover network environments and identify instances in signals
    - I think this need to be the first step to both inform and prioritize SemConv work
  - Unsigned 64-bit values given the OTel restriction to floats.
    - deltas, rates, ???
    - Current type [https://github.com/open-telemetry/opentelemetry-proto/blob/7c63f7b8b69e83bdda071a70898cd8a9f4ec77a2/opentelemetry/proto/metrics/v1/metrics.proto#L410](https://github.com/open-telemetry/opentelemetry-proto/blob/7c63f7b8b69e83bdda071a70898cd8a9f4ec77a2/opentelemetry/proto/metrics/v1/metrics.proto#L410)
- [Sven Cowart] Community project: [https://github.com/svencowart/community/blob/network/projects/network.md](https://github.com/svencowart/community/blob/network/projects/network.md)
  - Agree on objectives, and leads
  - TC/GC?
- [Mario Macias] Flow metrics: semantic convention WIP [https://github.com/open-telemetry/semantic-conventions/pull/3828](https://github.com/open-telemetry/semantic-conventions/pull/3828)
- [Sven] Submit project template
- [Braydon] Investigate the overflow problem with signed values

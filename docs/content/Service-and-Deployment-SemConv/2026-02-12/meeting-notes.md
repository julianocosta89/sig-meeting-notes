## Meeting Notes

### Attendees
- Ankit Bhadu (Google)
- Josh Suereth (Google)
- Jina Jain (Splunk)
- Neil Yashinsky (Force Multiplier Labs / [ContextCore](http://contextcore.me/) )

### Agenda
- [trask] [`k8s.service.name` proposal](https://github.com/open-telemetry/semantic-conventions/pull/3295#discussion_r2770352218)
- [trask] Stabilize deployment environment
  - [Should `deployment.environment.name` be an enum?](https://github.com/open-telemetry/semantic-conventions/issues/2910)
- [trask] [Stabilize `service.peer.name` and `service.peer.namespace`](https://github.com/open-telemetry/semantic-conventions/pull/3352)
  - [suereth] Concerns - network.peer.* vs. client.* / server.* When do we decide one vs. another.
  - Taxonomy of telemetry type:
    - Common - Single-Source:   Resource {my service} - Signal {jvm.memory usage}
    - Edge - From Source or Dest
      - Resource {my service} - Signal {client span - has the server service name}
      - Resource {my service} - Signal {server span - has the client service name}
    - Edge - From the middle
      - Resource {middle mane} - Signal {log - source service + destination service are listed}
- [Ankit] [Introduce service.cost_center attribute](https://github.com/open-telemetry/semantic-conventions/issues/3397)
  - AI - Move to - service.cost_center.id

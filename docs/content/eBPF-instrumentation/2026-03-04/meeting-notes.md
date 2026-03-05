## Meeting Notes

### Attendees
- ~~Mike Dame (Odigos) (can't make it)~~
- Tyler Yahn (Splunk)
- Mario Macias (Grafana)
- Giuseppe Ognibene (Coralogix)
- Rafael Roquetto (Grafana)
- Stephen Lang (Grafana)
- Nikola Grcevski (Grafana)
- Robert Pająk (Splunk)
- [Florian Lehner](mailto:florian.lehner@elastic.co) (Elastic)
- Mattia Meleleo (Coralogix)
- Nimrod Avni (Coralogix)

### Agenda
- [Nimrod] - Go instrumentation vs General TCP instrumentation - making sure of feature parity
  - Go HTTP requests go through a different processing path, not enjoying post classification for http sub protocols (aws / graphql, …)
  - Also, what are the benefits of the go based instrumentation that make it worth maintaining both?
  - [Nikola] Stalled PR here: [https://github.com/open-telemetry/opentelemetry-ebpf-instrumentation/pull/1244](https://github.com/open-telemetry/opentelemetry-ebpf-instrumentation/pull/1244)
  - [Rafael] Socket programs
    - [https://github.com/rafaelroquetto/opentelemetry-ebpf-instrumentation/tree/sk_verdict/bpf/tpinjector](https://github.com/rafaelroquetto/opentelemetry-ebpf-instrumentation/tree/sk_verdict/bpf/tpinjector)
- [Nikola] Discuss if there’s anything outstanding about [https://github.com/open-telemetry/opentelemetry-ebpf-instrumentation/pull/1374](https://github.com/open-telemetry/opentelemetry-ebpf-instrumentation/pull/1374)
- [Nikola] [Service.instance.id](http://Service.instance.id) is [moving to](https://github.com/open-telemetry/semantic-conventions/pull/312/) UUID
- [Nikola] Sharing service metadata through the protocols (mostly non Kubernetes)
- [Tyler] [Next release](https://github.com/open-telemetry/opentelemetry-ebpf-instrumentation/milestone/7)
- [Rafael] Large buffers

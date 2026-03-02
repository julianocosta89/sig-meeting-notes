## Meeting Notes

### Attendees
- Mattia Meleleo (Coralogix)
- Nimrod Avni (Coralogix)
- Mario Macias (Grafana)
- Rafael Roquetto (Grafana)
- Stephen Lang (Grafana)
- Nikola Grcevski (Grafana)
- Tyler Yahn (Splunk)
- Mike Dame (Odigos)
- Ittai Corem (Coralogix)

### Agenda
- [Nikola] Walkthrough distributed tracing and decisions made
- https://github.com/open-telemetry/opentelemetry-helm-charts/pull/1704#issuecomment-3128878646
- [Tyler] [Open PRs Review](https://github.com/open-telemetry/opentelemetry-ebpf-instrumentation/pulls)
  - Related to changes to the service_graph [https://pkg.go.dev/github.com/open-telemetry/opentelemetry-collector-contrib/connector/servicegraphconnector#section-readme](https://pkg.go.dev/github.com/open-telemetry/opentelemetry-collector-contrib/connector/servicegraphconnector#section-readme)
    - Additional labels can be included using the dimensions configuration option. Those labels will have a prefix to mark where they originate (client or server span kinds). The client_ prefix relates to the dimensions coming from spans with SPAN_KIND_CLIENT, and the server_ prefix relates to the dimensions coming from spans with SPAN_KIND_SERVER.

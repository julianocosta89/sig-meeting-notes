## Meeting Notes

### Attendees
- Nikola Grcevski (Grafana)
- [Florian Lehner](mailto:florian.lehner@elastic.co) (Elastic)
- Stephen Lang (Grafana)
- Tyler Yahn (Splunk)
- Nimrod Avni (Coralogix)
- Giuseppe Ognibene (Coralogix)
- Mattia Meleleo (Coralogix)
- Marc Tudurí (Grafana)
- Mike Dame (Odigos)

### Agenda
- [Nimrod] - Network monitoring ([https://github.com/open-telemetry/opentelemetry-network/blob/main/docs/metrics/metrics.yaml](https://github.com/open-telemetry/opentelemetry-network/blob/main/docs/metrics/metrics.yaml))
  - The plan was we will implement what the networking metrics have
  - Unify on OBI once this is done
  - The network metrics project uses old approach to writing the eBPF code
- [Mattia] - PID - Trace context mapping in eBPF
  - Usecases: Trace <> Log correlation, Trace <> Profiles correlation
  - Exposed as eBPF map (yes!)
  - [Stephen] Similar to the following OTEP which was mentioned recently [https://github.com/open-telemetry/opentelemetry-specification/pull/4719](https://github.com/open-telemetry/opentelemetry-specification/pull/4719)
    - [Nimrod] This might be helpful with correlating OBI traces with already instrumented services so a trace can include both (we only support go)
    - We need to ask for support of a standardized format that will work in eBPF
  - [https://docs.google.com/document/d/1eatbHpEXXhWZEPrXZpfR58-5RIx-81mUgF69Zpn3Rz4/edit?tab=t.0#heading=h.fvztn3xtjxxm](https://docs.google.com/document/d/1eatbHpEXXhWZEPrXZpfR58-5RIx-81mUgF69Zpn3Rz4/edit?tab=t.0#heading=h.fvztn3xtjxxm)
- [Nimrod] [Embedding OBI as a otel receiver](https://github.com/open-telemetry/opentelemetry-ebpf-instrumentation/pull/1053)
- [Stephen] MQTT in progress ([latest PR](https://github.com/open-telemetry/opentelemetry-ebpf-instrumentation/pull/1055)), AMQP next
- [Tyler] Road to stabilization
- [Tyler] [Open PRs Review](https://github.com/open-telemetry/opentelemetry-ebpf-instrumentation/pulls)
- [https://sergiocipriano.com/beyla-envoy.html](https://sergiocipriano.com/beyla-envoy.html)

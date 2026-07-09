## Meeting Notes

### Attendees
- Tyler Yahn (Splunk)
- Evan Bradley (Dynatrace)
- Mario Macias (Grafana)
- Nikola Grcevski (Grafana)
- Stephen Lang (Grafana)
- Alex Boten (Honeycomb)
- [Jade Guiton](mailto:jade.guiton@datadoghq.com) (Datadog)
- Braydon Kains (Google)
- Pablo Baeyens (Datadog)
- Nimrod Avni (Coralogix)
- Israel Blancas (Coralogix)
- Mattia Meleleo (Coralogix)
- Roy Reshef (Kubex)
- Mike Dame (Odigos)
- Giuseppe Ognibene (Coralogix)
- Marc Tudurí (Grafana)
- Josh MacDonald (Microsoft)

### Agenda
- [alex] - Support OBI with OCB builder [timebox: 15min]
  - [https://github.com/open-telemetry/opentelemetry-collector/issues/15430](https://github.com/open-telemetry/opentelemetry-collector/issues/15430)
- [Nimrod] -  [OBI Nightly releases](https://github.com/open-telemetry/opentelemetry-ebpf-instrumentation/issues/2553)
- [Tyler] Declarative configuration placement — [#2211](https://github.com/open-telemetry/opentelemetry-ebpf-instrumentation/issues/2211)
  - Does the SIG agree [https://github.com/open-telemetry/opentelemetry-ebpf-instrumentation/issues/2553](https://github.com/open-telemetry/opentelemetry-ebpf-instrumentation/issues/2553)to keep OBI config in `extension.obi` for v2 and track future work in another issue?
- [Tyler] Supported declarative configuration subset — [#594](https://github.com/open-telemetry/opentelemetry-ebpf-instrumentation/issues/594)
  - Which declarative configuration fields are part of the OBI v1 contract?
  - Should unsupported fields be rejected, ignored, or accepted with a warning?
- [Nimrod] - [Testing conventions](https://github.com/open-telemetry/opentelemetry-ebpf-instrumentation/pull/2545#issuecomment-4881341614)

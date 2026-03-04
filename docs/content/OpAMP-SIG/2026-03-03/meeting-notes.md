## Meeting Notes

### Attendees
- Andy Keller (Bindplane)
- Tigran Najaryan
- Dakota Paasman (Bindplane)
- Juande Manjon
- Evan Bradley (Dynatrace)
- Blake Rouse (Elastic)
- Bejal Lewis (Grafana Labs)
- [Jade Guiton](mailto:jade.guiton@datadoghq.com) (Datadog)
- Aunsh Chaudhari (Splunk)
- Michel Laterman (Elastic)
- Pavan Krishna (Splunk)

### Agenda
- [Jade Guiton] Correlation between reported `identifying_attributes` and OTLP telemetry:
  - PR seems correct
  - Jade to file a separate issue about `service.name` and `service.version`
- [Tigran] Maintainers' high-level roadmap view:
  - Supervisor goal: Release a production-ready MVP Supervisor 1.0
    - Implement the MVP features (to be decided)
    - Harden the implementation
    - Make official deb/rpm/etc release, bundled with Collector
  - OpAMP Go goal: Implement the stable features of the spec completely and release production-ready 1.0
  - OpAMP Spec goal: Mark subset of features stable (to be decided), release 1.0
  - TODO:
    - look at K8s Operator and decide what goes into the Roadmap.
    - Do we want Supervisor-less extension-only goal as well?
- [Blake] Callout [RFC] Partial Reload Support
  - [https://github.com/open-telemetry/opentelemetry-collector/pull/14640](https://github.com/open-telemetry/opentelemetry-collector/pull/14640)
- [Aunsh] Remote config support for opamp extension ([reference](https://cloud-native.slack.com/archives/C02J58HR58R/p1765395440077059))

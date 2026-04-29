## Meeting Notes

### Attendees
- ~~Tigran Najaryan (Splunk)~~ can’t join this time
- Dakota Paasman (Dynatrace)
- Andy Keller (Dynatrace)
- Michel Laterman (Elastic)
- Evan Bradley (Dynatrace)
- Kevin Wagner (AWS)
- Bejal Lewis (Grafana Labs)
- Israel Blancas (Coralogix)
- Douglas Camata (Coralogix)

### Agenda
- [Dakota] Various supervisor PRs in need of reviews
  - Extensions: [https://github.com/open-telemetry/opentelemetry-collector-contrib/pull/47732](https://github.com/open-telemetry/opentelemetry-collector-contrib/pull/47732)
  - Upgrades: [https://github.com/open-telemetry/opentelemetry-collector-contrib/pull/47300](https://github.com/open-telemetry/opentelemetry-collector-contrib/pull/47300)
- [Michel] Change how connection settings status’ are applied to async: [https://github.com/open-telemetry/opamp-go/pull/544](https://github.com/open-telemetry/opamp-go/pull/544)
- [Andy] New opampexporter in bindplane-otel-contrib [https://github.com/observIQ/bindplane-otel-contrib/tree/main/exporter/opampexporter](https://github.com/observIQ/bindplane-otel-contrib/tree/main/exporter/opampexporter)
- [Douglas] Two Supervisor PRs needing reviews
  - Startup fallback config: [https://github.com/open-telemetry/opentelemetry-collector-contrib/pull/45100](https://github.com/open-telemetry/opentelemetry-collector-contrib/pull/45100)
  - Start Collector with previous working config when new remote config fails to apply: [https://github.com/open-telemetry/opentelemetry-collector-contrib/pull/47853](https://github.com/open-telemetry/opentelemetry-collector-contrib/pull/47853)
    - PR updated to answer questions and documents decision made during the call.

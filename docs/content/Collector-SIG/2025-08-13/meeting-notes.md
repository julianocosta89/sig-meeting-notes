## Meeting Notes

### Attendees
- [Andrzej Stencel](mailto:andrzej.stencel@elastic.co) (Elastic)
- Antoine Toulme (Splunk)
- Sean Marciniak (Splunk)
- Alex Boten (Honeycomb)
- Tyler Helmuth (Honeycomb)
- Israel Blancas (Coralogix)
- Matthew Hensley (Grafana Labs)
- [Yang Song](mailto:yang.song@datadoghq.com) (Datadog)
- [Jade Guiton](mailto:jade.guiton@datadoghq.com) (Datadog)
- [Heitor Ganzeli](mailto:heitor.ganzeli@gmail.com)(Huawei)
- [Evan Bradley](mailto:google@evanbradley.org) (Dynatrace)
- Pablo Baeyens (Datadog)
- [Raj Nishtala](mailto:rnishtala@sumologic.com) (SumoLogic)
- Braydon Kains (Google)
- Edmo Vamerlatti (Elastic)
- [Paulo Janotti](mailto:pjanotti@splunk.com) (Splunk)
- João Duarte (Elastic)
- Douglas Camata (Coralogix)
- Dmitry Anoshin (Splunk)
- Arthur Sens (Grafana Labs)

### Agenda
- [Pablo, announcement]
  - [service] Add a debug-level log each time there is an error  [opentelemetry-collector/pull/13474](https://github.com/open-telemetry/opentelemetry-collector/pull/13474)
  - [chore][docs/rfc] Amend universal telemetry RFC with proposed implementation for logs [opentelemetry-collector/pull/13609](https://github.com/open-telemetry/opentelemetry-collector/pull/13609)
- [ArthurSens] Regarding building automation that asserts internal collector telemetry.
  - At Grafana Labs we're using a tool called [OATs](https://github.com/grafana/oats), who spins up storage for all telemetry types and then run queries to assert telemetry is sent.
    - [Used in OpenTelemetry eBPF Instrumentation (OBI)](https://github.com/open-telemetry/opentelemetry-ebpf-instrumentation/tree/main/test/oats)
    - Is this something of interest to the collector?
- [Raj] Split a log record with slice bodies into multiple log records
  - [https://github.com/open-telemetry/opentelemetry-collector-contrib/issues/41791#issuecomment-3177610768](https://github.com/open-telemetry/opentelemetry-collector-contrib/issues/41791#issuecomment-3177610768)
- [Antoine] OpenCensus deprecation
  - [https://github.com/open-telemetry/opentelemetry-collector-contrib/issues/36791](https://github.com/open-telemetry/opentelemetry-collector-contrib/issues/36791)
- [Antoine] small improvement with PRs for first time contributors [https://github.com/open-telemetry/opentelemetry-collector-contrib/issues/41944](https://github.com/open-telemetry/opentelemetry-collector-contrib/issues/41944)
- [Evan] Looking for additional context on [https://github.com/open-telemetry/opentelemetry-collector/pull/11575](https://github.com/open-telemetry/opentelemetry-collector/pull/11575)
- [Antoine] moving components to beta [https://github.com/open-telemetry/opentelemetry-collector-contrib/issues?q=is%3Aissue%20state%3Aopen%20author%3Aatoulme%20beta](https://github.com/open-telemetry/opentelemetry-collector-contrib/issues?q=is%3Aissue%20state%3Aopen%20author%3Aatoulme%20beta)
- [Heitor] sponsor needed for new Huawei LTS logs receiver: [https://github.com/open-telemetry/opentelemetry-collector-contrib/issues/41083](https://github.com/open-telemetry/opentelemetry-collector-contrib/issues/41083)
- [Paulo] working to get a Windows ARM release, current PR on core: [https://github.com/open-telemetry/opentelemetry-collector/pull/13625](https://github.com/open-telemetry/opentelemetry-collector/pull/13625)
  - Next steps: enabling CI tests on Windows ARM
  - Windows + ARM: may expose even more concurrency issues in tests.
- (Not present) [João] looking for sponsor on Lookup / Enrichment processor: [https://github.com/open-telemetry/opentelemetry-collector-contrib/issues/41816](https://github.com/open-telemetry/opentelemetry-collector-contrib/issues/41816)
  - Interfaces and scaffolding suggestion in [issuecomment-3167963229](https://github.com/open-telemetry/opentelemetry-collector-contrib/issues/41816#issuecomment-3167963229)

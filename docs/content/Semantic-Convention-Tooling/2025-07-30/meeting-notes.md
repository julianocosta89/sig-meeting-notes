## Meeting Notes

### Attendees
- Laurent Querel (F5)
- Josh Suereth
- Jay DeLuca (Grafana Labs)
- Jeremy Blythe
- Nathan Smith (Elastic)
- Liudmila Molkova (Microsoft)

### Agenda
- New Topic:
  - [Jay] Instrumentation metadata
    - Opportunities to work together with weaver
    - [https://github.com/open-telemetry/opentelemetry-java-instrumentation/blob/main/docs/instrumentation-list.yaml](https://github.com/open-telemetry/opentelemetry-java-instrumentation/blob/main/docs/instrumentation-list.yaml)
    - [https://jaydeluca.github.io/instrumentation-explorer/](https://jaydeluca.github.io/instrumentation-explorer/)
    - [Luidmila] config-related semconv discussions
      - [https://github.com/open-telemetry/semantic-conventions/pull/2504#issuecomment-3057814935](https://github.com/open-telemetry/semantic-conventions/pull/2504#issuecomment-3057814935)
      - [https://github.com/open-telemetry/semantic-conventions/issues/705](https://github.com/open-telemetry/semantic-conventions/issues/705)
      - general [https://github.com/open-telemetry/semantic-conventions/issues/1450](https://github.com/open-telemetry/semantic-conventions/issues/1450)
- Triage:
  - [https://github.com/orgs/open-telemetry/projects/74](https://github.com/orgs/open-telemetry/projects/74)
- Other topics:
  - [josh] V2 Schema - let's agree on what we cut, I was lazy in my PR
    - metric_name or name?
      - [Name on proto](https://github.com/open-telemetry/opentelemetry-proto/blob/b553517a730dc72097beb60292815ca221766598/opentelemetry/proto/metrics/v1/metrics.proto#L191)

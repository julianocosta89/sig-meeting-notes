## Meeting Notes

### Attendees
- [Juliano Costa](mailto:juliano.costa@datadoghq.com)(Datadog)
- Cyrille Le Clerc (Grafana Labs)
- Donal O'Sullivan (Elastic)
- Shenoy Pratik Gurudatt (OpenSearch)
- Antonin Bruneau (Tsuga)

### Agenda
- [Create OpenTelemetry Demo Light Branch · Issue #2195](https://github.com/open-telemetry/opentelemetry-demo/issues/2195)
  - This is the most required change from discussions on OTel Unplugged and on the GH issue.
  - We should discuss the issue, and possible solutions.
  - Khurso's discussion: [https://github.com/open-telemetry/opentelemetry-demo/discussions/2931](https://github.com/open-telemetry/opentelemetry-demo/discussions/2931)
    - POCs
      - Damien: OpenTelemetry Demo Builder (ODB)
        - [OpenTelemetry Demo Builder](https://docs.google.com/document/d/1ukpwYi-0EsWIoTnH-rfpU-58g2fqEtlJi62IF3jCglo/edit?tab=t.0)
      - Roger: decouple telemetry services from main docker compose file
        - [https://github.com/open-telemetry/opentelemetry-demo/pull/3015/changes](https://github.com/open-telemetry/opentelemetry-demo/pull/3015/changes)
  - Docker Profiles was the idea that called more our attention
    - [Juliano] Will bring that back to the GH issue
  - Cyrille: What do we want to prioritize?
    - Reducing memory consumption?
    - Removing included OSS observability backends?
    - Docker Compose or K8s?
    - Keeping an otel-demo distro with oss batteries included governed by the OTel community?
    - Create another distro of the demo or change the existing default distro of the demo
- [Dónal]
  - [https://github.com/open-telemetry/opentelemetry-demo/pull/3022](https://github.com/open-telemetry/opentelemetry-demo/pull/3022)
  - [https://github.com/open-telemetry/opentelemetry-demo/issues/3034](https://github.com/open-telemetry/opentelemetry-demo/issues/3034)
- [Shenoy Pratik]
  - [https://github.com/open-telemetry/opentelemetry-demo/pull/3005](https://github.com/open-telemetry/opentelemetry-demo/pull/3005)
  - [https://github.com/open-telemetry/opentelemetry-demo/pull/3014](https://github.com/open-telemetry/opentelemetry-demo/pull/3014)
- Weaver
  - Juliano: Do we want to add an extra service as proposed in the PR? Is it conflicting with our goal of reducing the size of the demo
  - Cyrille: excited to showcase “schema driven custom metrics & attributes”. Cyrille was expecting to see code generation

## Meeting Notes

### Attendees
- Pierre Tessier (Resolve AI)
- Cyrille Le Clerc (Grafana Labs)
- Dónal O’Sullivan (Elastic)
- [Juliano Costa](mailto:juliano.costa@datadoghq.com)(Datadog)
- Shenoy Pratik (OpenSearch)
- Jonathan Munz (Embrace)

### Agenda
- Upgrading the Android app / Expo SDK (required with Gradle changes 8 -> 9) is a big effort, ref: [#3195](https://github.com/open-telemetry/opentelemetry-demo/pull/3195), [#3232](https://github.com/open-telemetry/opentelemetry-demo/pull/3232)
- Use Prometheus info PromQL function [#2869](https://github.com/open-telemetry/opentelemetry-demo/pull/2869)
- K8s Grafana Dashboards - based on Otel Collector Daemonset (ie on otel helm chart presets for K8s monitoring). It’s a port of [kubernetes-monitoring/kubernetes-mixin](https://github.com/kubernetes-monitoring/kubernetes-mixin)
- [https://github.com/open-telemetry/opentelemetry-helm-charts/pull/2094](https://github.com/open-telemetry/opentelemetry-helm-charts/pull/2094)
- Pros:
  - helps advance OTel-native infrastructure monitoring
  - Will help improve OTel-native K8s monitoring:
    - Are there metrics missing in the otelcol receivers
    - Shall we
- Cons / challenges
  - PR includes 13 dashboards with a few missing metrics
- Pierre: these dashboards are great but should be owned by something else than the OTel Demo
- Decision: we love this contribution but we want to find a home for these dashboards, outside of the OTel Demo. A home like [kubernetes-monitoring/kubernetes-mixin](https://github.com/kubernetes-monitoring/kubernetes-mixin).
- [https://github.com/open-telemetry/opentelemetry-demo/pull/3229](https://github.com/open-telemetry/opentelemetry-demo/pull/3229)

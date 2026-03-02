## Meeting Notes

### Attendees
- [Juliano Costa](mailto:juliano.costa@datadoghq.com)(Datadog)
- Alessio (Suse)
- Cyrille Le Clerc(Grafana)
- Shenoy Pratik Gurudatt (OpenSearch)
- Roger Coll (Elastic)

### Agenda
- Should we think about adding a swift? (hopefully replacing an existing service)
  - swift-otel/swift-otel vs open-telemetry/opentelemetry-swift
    - [https://github.com/open-telemetry/opentelemetry-demo/pull/2526#issuecomment-3274089510](https://github.com/open-telemetry/opentelemetry-demo/pull/2526#issuecomment-3274089510)
- PostgreSQL init on K8s using the upstream image
  - [https://github.com/cyrille-leclerc/my-shopping-cart/blob/main/kubernetes/postgres.yaml](https://github.com/cyrille-leclerc/my-shopping-cart/blob/main/kubernetes/postgres.yaml)
  - Do we plan to demo infra monitoring?
- Should we use the [opentelemetry-kube-stack](https://github.com/open-telemetry/opentelemetry-helm-charts/tree/main/charts/opentelemetry-kube-stack) helm chart?
  - This would demo:
    - The otel-kube-stack is great, soon to be the obvious default to install otel on K8s
    - Turnkey setup on K8s
    - Auto injection on K8s
    - OTel based infra monitoring
  - Other benefits
    - Simpler config of otel SDKs and collectors
  - Identified challenges:
    - Self signed certs can be fragile
    - Host file access doesn’t work (Host Metrics & pod logs) on Docker Desktop Mac
- TODO:
  - Release a new version of Demo with the env vars update
  - Release Helm chart
  - Roger and Cyrille will work on sending a follow-up PR on Helm to replace otel collector helm with [opentelemetry-kube-stack](https://github.com/open-telemetry/opentelemetry-helm-charts/tree/main/charts/opentelemetry-kube-stack) helm.

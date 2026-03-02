## Meeting Notes

### Attendees
- Krish Aryan
- Cyrille Le Clerc (Grafana Labs)
- Pierre Tessier (Honeycomb)
- Jonathan Munz (Embrace)

### Agenda
- FYI Cyrille pushing PRs to the OTel Collector Helm Chart to prepare the OTel Demo on K8s to add support for infra monitoring (K8s, Linux…)
  - Proposal
    - Add infra monitoring to the OTel demo on K8s
      - Starting with K8s and Linux
      - Expanding to Pod logs, PostgreSql, Http Checks,
      - Don’t increase the size of the OTel Demo implementing infra monitoring through daemon collector rather than a deployment collector
        - Pierre & Cyrille: we want the otel-demo on K8s to support both the daemonset & deployment modes because some practitioners cannot deploy as a daemonset
  - Ongoing PRs
    - [[opentelemetry-collector] Support presets/clustermetrics for daemonset mode #1941](https://github.com/open-telemetry/opentelemetry-helm-charts/pull/1941)
    - [(opentelemetry-collector) Align presets/kubernetesAttributes on the opentelemetry-kube-stack presets #1918](https://github.com/open-telemetry/opentelemetry-helm-charts/pull/1918)
  - Next
    - Validate usage of the receive creator, Cyrille is likely to have found a few glitches in the receiver creator for http checks and Kafka receivers
- Collector self telemetry
  - [[grafana] OpenTelemetry Collector Dashboard needs re-work · Issue #2735](https://github.com/open-telemetry/opentelemetry-demo/issues/2735)
- Cyrille: [[postgres] Showcase Postgresql monitoring with dedicated user and the role pg_monitor #2665](https://github.com/open-telemetry/opentelemetry-demo/pull/2665)
  - PR got closed due to inactivity, can we discuss it
  - Pierre: Postgresql init script changed since the PR
  - Cyrille & Pierre: next step: create a dedicated monitoring user on postgresql that will used by the otelcol postgresql receiver

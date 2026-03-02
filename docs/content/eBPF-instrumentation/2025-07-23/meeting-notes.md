## Meeting Notes

### Attendees
- Mike Dame (Odigos)
- Tyler Yahn (Splunk)
- Mattia Meleleo (Coralogix)
- Nimrod Avni (Coralogix)
- Marc Tuduri (Grafana Labs)
- Nikola Grcevski (Grafana)
- Rafael Roquetto (Grafana)
- Mario Macias (Grafana)
- Stephen Lang (Grafana, late)
- David Ashpole (Google, late)

### Agenda
- [Tyler] [Milestone 0.1.0](https://github.com/open-telemetry/opentelemetry-ebpf-instrumentation/milestone/1) review
  - [https://github.com/open-telemetry/opentelemetry.io/pull/7295](https://github.com/open-telemetry/opentelemetry.io/pull/7295)
- How we are going to do a release
  - We need docker publish scripts
  - We need to upgrade the helm chart
    - [https://github.com/open-telemetry/opentelemetry-helm-charts/pull/1704](https://github.com/open-telemetry/opentelemetry-helm-charts/pull/1704)
      - CNCF slack channel is [#otel-helm](https://cloud-native.slack.com/archives/C03HVLM8LAH)
      - Above PR has outstanding feedback
    - Set the version of the docker image
    - Set the version of the chart
    - This is in a different repository, we’ll need to make a PR there
    - How do we coordinate the rollout?
  - Go tag
- [Tyler] [Open PRs](https://github.com/open-telemetry/opentelemetry-ebpf-instrumentation/pulls)
- [Tyler] AI: open issue to track removing vendor directory

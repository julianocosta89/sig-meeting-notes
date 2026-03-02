## Meeting Notes

### Attendees
- [Juliano Costa](mailto:juliano.costa@datadoghq.com)(Datadog)
- Pierre Tessier (Honeycomb)
- Derek Mitchell (Splunk)
- Cyrille Le Clerc(Grafana)
- Jonathan Munz (Embrace)

### Agenda
- [https://github.com/open-telemetry/opentelemetry-demo/pull/2645](https://github.com/open-telemetry/opentelemetry-demo/pull/2645)
  - Let's Dapr’ize
    - Cyrille: Can we try to get the semconv [db client metrics](https://opentelemetry.io/docs/specs/semconv/database/database-metrics/)? 🙏
    - [https://github.com/open-telemetry/opentelemetry-demo/pull/2143#event-19625629993](https://github.com/open-telemetry/opentelemetry-demo/pull/2143#event-19625629993)
  - Cyrille: Why switching rather than adding at least a document oriented db? Size of the demo?
  - Cyrille: Why maintain both for K8s a Helm Chart and a Manifest?
    - Drop k8s manifest and add a docker container with helm and a shared volume to generate k8s manifests.
- [https://github.com/open-telemetry/opentelemetry-demo/pull/2663](https://github.com/open-telemetry/opentelemetry-demo/pull/2663)
  - Derek:  remove K8s manifest changes (since this is auto-generated from the Helm chart)
  - Derek:  submit separate PR for Helm changes
  - Derek:  follow-up PR to allow a real OpenAI compatible LLM to be swapped in
  - Derek:  switch to use the same Postgres database used by accounting service
- [Cyrille Le Clerc](mailto:cyrille.leclerc@grafana.com) INFORM - Ticket [[chore] Make all OTel Demo components use the http/protobuf OTLP protocol #2676](https://github.com/open-telemetry/opentelemetry-demo/issues/2676) created as discussed during the last SIG call
- [Proposal to add OpenSearch Dashboards · Issue #2172 · open-telemetry/opentelemetry-demo](https://github.com/open-telemetry/opentelemetry-demo/issues/2172)

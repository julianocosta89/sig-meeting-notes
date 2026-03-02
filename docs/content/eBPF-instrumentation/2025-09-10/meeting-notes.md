## Meeting Notes

### Attendees
- Mattia Meleleo (Coralogix)
- Rafael Roquetto (Grafana)
- Nikola Grcevski (Grafana)
- Mario Macias (Grafana)
- Tyler Yahn (Splunk)
- Nimrod Avni (Coralogix)

### Agenda
- [Nimrod] [GKE Autopilot support](https://cloud-native.slack.com/archives/C08P9L4FPKJ/p1756149467940459)
  - hey everyone, one of our customers is interested in deploying obi on GKE autopilot, from what i understood some of the configurations obi requires like privileged: true and hostPid: true are disallowed in GKE autopilot workloads, with exceptions for [autopilot partners](https://cloud.google.com/kubernetes-engine/docs/resources/autopilot-partners), in our case more specifically we want to be on the [privileged open source workloads section](https://cloud.google.com/kubernetes-engine/docs/concepts/run-autopilot-open-source-workloads), right now i saw beyla there so im gussing the grafana folk might know a bit more about the process of being vetted
- [Nimrod] `exclude_otel_instrumented_services` GRPC issues
- [Tyler] [Open PRs Review](https://github.com/open-telemetry/opentelemetry-ebpf-instrumentation/pulls)
- [Nikola] Does anyone know how we can address this [https://github.com/open-telemetry/opentelemetry-ebpf-instrumentation/issues/583](https://github.com/open-telemetry/opentelemetry-ebpf-instrumentation/issues/583)?

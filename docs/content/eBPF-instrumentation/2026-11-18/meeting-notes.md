## Meeting Notes

### Attendees
- Mattia Meleleo (Coralogix)
- [Gregor Zeitlinger](mailto:gregor.zeitlinger@grafana.com)(Grafana)
- Roy Reshef (Kubex)
- Giuseppe Ognibene (Coralogix)
- Tyler Yahn (Splunk)
- Marc Tuduri (Grafana)
- Nimrod Avni (Coralogix)

### Agenda
- [Nimrod] Option to turn off `target.info`
  - Does it fit in `capture.metrics.features`
    - `capture.metrics.features: [applications, application_without_target_info, ….]`
    - We could move to the `metrics` level: `capture.metrics.target_info: false`
  - [https://github.com/open-telemetry/opentelemetry-ebpf-instrumentation/issues/2974#issuecomment-5241564864](https://github.com/open-telemetry/opentelemetry-ebpf-instrumentation/issues/2974#issuecomment-5241564864)
  - [AI: Nimrod] Add issue to look into removing this in v2
- [Nimrod] [v1.1.0](https://github.com/open-telemetry/opentelemetry-ebpf-instrumentation/milestone/22)?
  - [https://github.com/open-telemetry/opentelemetry-ebpf-instrumentation/pull/4277](https://github.com/open-telemetry/opentelemetry-ebpf-instrumentation/pull/4277) ✅
  - [https://github.com/open-telemetry/opentelemetry-ebpf-instrumentation/pull/4028](https://github.com/open-telemetry/opentelemetry-ebpf-instrumentation/pull/4028)
  - [https://github.com/open-telemetry/opentelemetry-ebpf-instrumentation/pull/4027](https://github.com/open-telemetry/opentelemetry-ebpf-instrumentation/pull/4027)
  - [https://github.com/open-telemetry/opentelemetry-ebpf-instrumentation/pull/4257](https://github.com/open-telemetry/opentelemetry-ebpf-instrumentation/pull/4257)
  - [https://github.com/open-telemetry/opentelemetry-ebpf-instrumentation/pull/4149](https://github.com/open-telemetry/opentelemetry-ebpf-instrumentation/pull/4149)
- [Mattia] Request a SIG-specific otelbot in open-telemetry/community?  [https://github.com/open-telemetry/community/blob/main/assets.md#otelbot-sig-specific](https://github.com/open-telemetry/community/blob/main/assets.md#otelbot-sig-specific)
- [Tyler] [Enable approver branches for OBI](https://github.com/open-telemetry/admin/pull/994#top)
- [Tyler] [Roadmap](https://github.com/orgs/open-telemetry/projects/187) status and planning
- [Roy] is rust the future? Raising this in view of the ecosystem trend… [https://www.linkedin.com/posts/bwplotka_opensource-rust-apache-share-7526643584754958337-f8Lv/](https://www.linkedin.com/posts/bwplotka_opensource-rust-apache-share-7526643584754958337-f8Lv/)

## Meeting Notes

### Attendees
- Stephen Lang (Grafana)
- João Duarte (Elastic)
- Kalman Meth (IBM)
- Douglas Camata (Coralogix)
- Tiffany Hrabusa (Grafana)
- Edmo Vamerlatti (Elastic)
- Sam DeHaan (Grafana)
- Alex Boten (Honeycomb)
- Pablo Baeyens (Datadog)
- [Andrzej Stencel](mailto:andrzej.stencel@elastic.co) (Elastic)
- Rob Bavey (Elastic)
- Josh MacDonald (Microsoft)
- Israel Blancas (Coralogix)
- David Ashpole (Google)
- Sindy Li (Snowflake)
- [Yang Song](mailto:yang.song@datadoghq.com) (Datadog)
- Tyler Helmuth (Honeycomb)

### Agenda
- [Stephen] Looking for feedback on this comment please: [https://github.com/open-telemetry/opentelemetry-collector-contrib/issues/31649#issuecomment-2790478007](https://github.com/open-telemetry/opentelemetry-collector-contrib/issues/31649#issuecomment-2790478007)
  - Ping #otel-k8s-semconv-sig channel for more feedback
- [Stephen] Also wondering if this is the right place to ask about helm chart release process/cadence? [https://github.com/open-telemetry/opentelemetry-helm-charts/pull/1704](https://github.com/open-telemetry/opentelemetry-helm-charts/pull/1704)
  - CNCF slack #otel-helm channel
- [João] Discussion about Enrichment and Lookups in the Collector
  - Doc to review: [Enrichment in OTel Collector](https://docs.google.com/document/d/1fCV8R6YE56LQ4uCRwx8_QiCsvJc-lI4mAm3MHnIffzs/edit?usp=sharing)
  - Follow up: create issue with this content and share to relevant slack channel, collect feedback async
    - Issue created: [opentelemetry-collector-contrib#41816](https://github.com/open-telemetry/opentelemetry-collector-contrib/issues/41816)
- [Victoria] I may not be available on the call today, but I wanted to make sure everyone had an opportunity to review the [Collector follow-up survey form](https://docs.google.com/forms/d/1Q8loBYV6Vv3pWVK0HImTNbOQr_i8a1IbaVSP9s1RheY/edit) before we (the End User SIG) publish.
  - Some folks have already shared feedback in [this Slack thread](https://cloud-native.slack.com/archives/C01N6P7KR6W/p1752776501570099?thread_ts=1751976033.525999&cid=C01N6P7KR6W). If you can’t access the form, feel free to DM me your email and I’ll add you as an editor.
  - If everything looks good and no further changes are needed, please leave a comment here or in the Slack thread to give your go-ahead so we can proceed with publishing. Thank you
- [Josh M] Introducing OTel-Arrow’s Go/Rust interop proposal draft
- [Sindy] Context propagation across batching  [issues/13320](https://github.com/open-telemetry/opentelemetry-collector/issues/13320) [pull/13460](https://github.com/open-telemetry/opentelemetry-collector/pull/13460)
- [Josh M] About adding new metrics: [Process for introducing new metrics in the core collector · Issue #13467 · open-telemetry/opentelemetry-collector](https://github.com/open-telemetry/opentelemetry-collector/issues/13467)
- [Pablo] <placeholder for any release discussion and prometheus bugs>
- [Jade] Discussion about recommending exporting Collector metrics directly to a backend vs. to a gateway layer: [Github thread](https://github.com/open-telemetry/opentelemetry.io/pull/7035#discussion_r2174787031)

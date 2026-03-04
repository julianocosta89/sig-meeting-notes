## Meeting Notes

### Attendees
- Christos Markou (Elastic)
- Jina Jain (Splunk)
- Dmitry Anoshin (Splunk)
- Stephen Lang (Grafana)

### Agenda
- [christos] Promoting k8s attributes to release_candidate: [https://github.com/open-telemetry/semantic-conventions/pull/3491](https://github.com/open-telemetry/semantic-conventions/pull/3491) . Please review/approve.
- [dmitry] entities centric metrics builder
  - [https://github.com/open-telemetry/opentelemetry-collector/pull/14660](https://github.com/open-telemetry/opentelemetry-collector/pull/14660)
  - [https://github.com/open-telemetry/opentelemetry-collector-contrib/pull/46542](https://github.com/open-telemetry/opentelemetry-collector-contrib/pull/46542)
- [stephen] [k8s.container.restart.count](https://opentelemetry.io/docs/specs/semconv/system/k8s-metrics/#metric-k8scontainerrestartcount) and [k8s.node.condition.status](https://opentelemetry.io/docs/specs/semconv/system/k8s-metrics/#metric-k8snodeconditionstatus) - semconv vs impl.
  - [https://github.com/open-telemetry/opentelemetry-collector-contrib/blob/18081b2196eb1a3085060f99674d83bf08f1a80d/receiver/k8sclusterreceiver/metadata.yaml#L537](https://github.com/open-telemetry/opentelemetry-collector-contrib/blob/18081b2196eb1a3085060f99674d83bf08f1a80d/receiver/k8sclusterreceiver/metadata.yaml#L537)
  - [https://github.com/open-telemetry/opentelemetry-collector-contrib/blob/18081b2196eb1a3085060f99674d83bf08f1a80d/receiver/k8sclusterreceiver/metadata.yaml#L730](https://github.com/open-telemetry/opentelemetry-collector-contrib/blob/18081b2196eb1a3085060f99674d83bf08f1a80d/receiver/k8sclusterreceiver/metadata.yaml#L730)
  - Focus on conventions first, work toward stability
- [Jina] prometheus info style metrics - [https://github.com/open-telemetry/semantic-conventions/pull/3376#discussion_r2851904585](https://github.com/open-telemetry/semantic-conventions/pull/3376#discussion_r2851904585)

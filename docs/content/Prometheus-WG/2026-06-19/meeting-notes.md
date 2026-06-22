## Meeting Notes

### Attendees
- Krisztian
- Jonathan
- Arve
- Krajo
- Israel
- Arthur

### Agenda
- [krisztian] Measuring appetite for a bridge for Promclient -> OTel, similar to the Go one.
  - Krisztian: Prometheus Rust SDK has a new maintainer and is back to active development.
    - In Istio we developed an L4 proxy layer in rust and we also have metrics from that proxy, instrumented with Prometheus rust SDK. For performance reasons we don't want to migrate to OTel.
    - We also don't want to force our users to use a collector to as a middleware between Prometheus and OTLP.
  - Action Items:
    - Move Prometheus Rust code generated from proto to prometheus/client_model
    - Implement the Gatherer interface in Prometheus Rust SDK
    - Reach out to potential new maintainers from Linkerd
    - All are assigned to Krisztian
- [arthur] Let's discuss David's PR: [https://github.com/open-telemetry/opentelemetry-specification/pull/4956](https://github.com/open-telemetry/opentelemetry-specification/pull/4956)
  - [Arve] The problems I see with the PR, with a Prometheus OTLP maintainer’s perspective:
    - It suggests treating job and instance OTel resource attributes as if they correspond to Prometheus job and instance labels. I think it would be fundamentally wrong to project these semantics from the Prometheus world onto OTel. It’s also a breaking change that would, *rightfully*, surprise any users with job and/or instance OTel resource attributes that do not stem from Prometheus. This would in turn backfire on those of us maintaining Prometheus and providing Prometheus based products to consumers. The previous idea of prefixing the attributes with “prometheus.” made more sense, as it would be a sensible convention within the ecosystem that such attributes are connected to Prometheus.
    - The PR’s stated mandate is preserving the Prometheus job and instance labels when translating from Prometheus to OTLP. However, it goes significantly beyond this mandate and introduces a new stipulation as to what should be considered identifying resource attributes when converting from OTLP to Prometheus. At the very least, sufficient justification should be laid out for why this breaking change should be necessary to fulfil the mandate. I don’t see any such justification in the PR.
    - Following from the previous point, I think that the PR needs to provide concrete use cases to sufficiently define the problems it seeks to solve, and to define how the changes it proposes solve those use cases. As [krajo@prometheus.io](mailto:krajo@prometheus.io)pointed out, if breaking changes are to be made, it should be justified through making things demonstrably better.

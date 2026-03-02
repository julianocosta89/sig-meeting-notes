## Meeting Notes

### Agenda
- [[Jonathan Santos](mailto:perebaj@gmail.com)] Someone knows how to answer the first bullet point of this comment?
  - [https://github.com/open-telemetry/opentelemetry-collector-contrib/issues/37277#issuecomment-2977622926](https://github.com/open-telemetry/opentelemetry-collector-contrib/issues/37277#issuecomment-2977622926)
  - 1. Protocol Support
- Remote write v2 is required due to transactionality additions in PRW 2.0
- [Juraj] Do we want to couple migration from RW1 to RW2 in the exporter with converting OTel explicit histograms into Custom Buckets Native Histograms. [PR](https://github.com/open-telemetry/opentelemetry-collector-contrib/pull/40494) options (can we do it in a follow up PR?):
  - Only support this
  - Add config option for it and enable it by default
  - Add config option for this, and disable it by default
- Anything [arthur.silvasens@grafana.com](mailto:arthur.silvasens@grafana.com)was working on that we nee
  - Otlptranslator: [https://github.com/open-telemetry/opentelemetry-collector-contrib/pull/39827](https://github.com/open-telemetry/opentelemetry-collector-contrib/pull/39827)
    - Owen has picked up some stuff, figuring out what is easy to keep going
  - Type and unit as labels: [https://github.com/prometheus/prometheus/issues/16610](https://github.com/prometheus/prometheus/issues/16610)
    - Dashpole to pick this up
  - Prometheus receiver scope attributes: [https://github.com/open-telemetry/opentelemetry-collector-contrib/pull/40060](https://github.com/open-telemetry/opentelemetry-collector-contrib/pull/40060)
- Something about content negotiation.

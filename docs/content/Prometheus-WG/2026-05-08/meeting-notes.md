## Meeting Notes

### Attendees
- arthur
- david
- krajo

### Agenda
- [arthur] DotNet OTel SDK Maintainer is trying to stabilize their Prometheus exporter implementation. He is trying to use the ***promtool metrics check*** in CI to validate what the SDK produces, but realized that promtool doesn't support OpenMetrics. He opened a [PR here](https://github.com/prometheus/common/pull/904) and is looking for feedback. If we can't help him there, what can we suggest to him to validate their implementation?
  - Ideally, OTel SDKs shouldn't need to implement the whole exposition formats. Prometheus SDKs should handle that, and OTel SDKs should use them.
  - Is the Prometheus team interested in maintaining the protobuf definition and generated code for several languages?
  - Prometheus would provide language specific thin libraries that turn the Protobuf (i.e. DTO) into various formats and expose them for scrape.
  - The OTEL SDK or anyone else could focus on just writing the collection part and then just hand over the exposure to the thin library.
- [arthur] Looks like a vibe-coded PR managed to get merged and has tons of incorrect or irrelevant documentation [here](https://github.com/open-telemetry/opentelemetry-collector-contrib/blob/main/receiver/prometheusreceiver/README.md#troubleshooting-and-best-practices). Can I delete the whole thing? 🙈
  - [dashpole] Yes, sorry!
- [krajo] Working on Prometheus/Mimir metadata store, but negotiated that I can dedicate my Monday afternoons to OTEL work, so I could take on NHCB in spec after all.
- PRs to review:
  - [https://github.com/open-telemetry/opentelemetry-specification/pull/4956](https://github.com/open-telemetry/opentelemetry-specification/pull/4956)

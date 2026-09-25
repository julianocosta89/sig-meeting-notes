## Meeting Notes

### Attendees
- Lukas Hering (Oracle)
- Diego Hurtado (Dash0)
- Riccardo Magliocchetti (Elastic)
- Dylan Russell
- Tammy Baylis (SolarWinds)
- Emídio (independent)
- Aaron Abbott (Google)
- Mike Goldsmith (Honeycomb)
- Hector Hernandez (Microsoft)
- Leighton Chen (Microsoft)

### Agenda
- [Tammy] Discussed previously: SQLAlchemy instrumentation metrics update (breaking)
  - [https://github.com/open-telemetry/opentelemetry-python-contrib/pull/5063](https://github.com/open-telemetry/opentelemetry-python-contrib/pull/5063)
- [Tammy] BatchSpanProcessor ValueError if `export_timeout_millis <= 0` ?
  - [https://github.com/open-telemetry/opentelemetry-python/pull/5650](https://github.com/open-telemetry/opentelemetry-python/pull/5650)
  - `Math.inf` for “continuous” export in Python. But `0` for Java, .NET
  - Carlos: what about other components? 0 for infinity was added later
    - [https://github.com/open-telemetry/opentelemetry-python/blob/1fe31a9bd00c88c824060506aed49b0611fe6e9c/docs/examples/metrics/reader/synchronous_gauge_read.py#L42](https://github.com/open-telemetry/opentelemetry-python/blob/1fe31a9bd00c88c824060506aed49b0611fe6e9c/docs/examples/metrics/reader/synchronous_gauge_read.py#L42)
    - Aaron: Maybe we can support both
    - Dylan: we are not passing `export_timeout_millis` to the exporter though
- [Lukas] Logs stability
  - [https://github.com/open-telemetry/opentelemetry-python/issues/3361](https://github.com/open-telemetry/opentelemetry-python/issues/3361)
  - How do we want to go about adding/removing import paths.
    - Consensus on keeping it and drop it on major bump
- [carlos] opentelemetry-exporter-otlp-proto-grpc: tolerate invalid timeout env vars - needs maintainers review.
  - [https://github.com/open-telemetry/opentelemetry-python/pull/5448](https://github.com/open-telemetry/opentelemetry-python/pull/5448)
- [aaron] PTAL [https://github.com/open-telemetry/opentelemetry-specification/pull/5308](https://github.com/open-telemetry/opentelemetry-specification/pull/5308)
  - Specifically [Jack’s comment](https://github.com/open-telemetry/opentelemetry-specification/pull/5308#discussion_r4009993077)
  - Biggest delta is
    - Safely exit on old python versions (no SyntaxErrors)
    - Vendoring dependencies

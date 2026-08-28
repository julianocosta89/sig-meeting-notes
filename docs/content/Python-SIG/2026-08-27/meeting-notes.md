## Meeting Notes

### Attendees
- Tammy Baylis (SolarWinds)
- Dylan russell (google)
- Aaron Abbott (Google)
- Diego Hurtado (Dash0)
- Riccardo Magliocchetti (Elastic)
- Lukas Hering (Oracle)
- Shuwen Pan (Cisco)

### Agenda
- [dylan] Move bedrock instrumentation to genai repo [**https://github.com/open-telemetry/opentelemetry-python-contrib/issues/4999**](https://github.com/open-telemetry/opentelemetry-python-contrib/issues/4999)
  - Liudmila: two strategies
    - Suppression
    - Keep both at the same time and choose which one to run based on the env var set
  - Diego: If you are going to drop this please have a release of the -contrib instrumentation without an hard pin dependency (== same ver) on another otel component  (e.g. opentelemetry-instrumentation)
- [Lukas] Add Valkey support to Redis instrumentation? [https://github.com/open-telemetry/opentelemetry-python-contrib/tree/main/instrumentation/opentelemetry-instrumentation-redis](https://github.com/open-telemetry/opentelemetry-python-contrib/tree/main/instrumentation/opentelemetry-instrumentation-redis)
  - Previous PR for dedicated instrumentation package: [https://github.com/open-telemetry/opentelemetry-python-contrib/pull/3478](https://github.com/open-telemetry/opentelemetry-python-contrib/pull/3478)
  - Lukas: [https://glide.valkey.io/getting-started/quickstart/?lang=python](https://glide.valkey.io/getting-started/quickstart/?lang=python) may also have native OTel
  - Riccardo: unsure about code reuse

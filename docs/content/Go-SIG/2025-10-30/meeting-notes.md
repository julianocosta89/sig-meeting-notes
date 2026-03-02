## Meeting Notes

### Attendees
- Tyler Yahn (Splunk)
- Damien Mathieu (Elastic)
- Alex Boten (Honeycomb)
- Robert Pająk (Splunk)
- David Ashpole (Google)
- Bryan Boreham (Grafana Labs)
- Mike Blum (Toast)

### Agenda
- [dashpole] [Monitoring bugs reported by OSS Fuzz #7549](https://github.com/open-telemetry/opentelemetry-go/issues/7549)
- [Tyler] [Stabilization of otelgrpc](https://github.com/open-telemetry/opentelemetry-go-contrib/issues/8078)?
  - Related: [https://github.com/grpc/grpc-go/issues/8265](https://github.com/grpc/grpc-go/issues/8265)
  - We need the semconv to stabilize
  - There needs to be involvement from gRPC to progress this
  - [dashpole] Update: I’m told that the SIG is active and is working towards stabilization. Not sure if gRPC is involved.
- [Damien] stabilization of otelhttp?
  - Blocker (only one I think): [https://github.com/open-telemetry/opentelemetry-go-contrib/issues/7254](https://github.com/open-telemetry/opentelemetry-go-contrib/issues/7254)
- [Mike] otel explorer go docs:
  - Context: [https://github.com/open-telemetry/community/pull/3000](https://github.com/open-telemetry/community/pull/3000)
  - Meeting notes: [Ecosystem Explorer Project](https://docs.google.com/document/d/1QBpFmSR54fGus8q6RraUj0-mEjSoX7S7fdlgsvxZsuk/edit?usp=sharing)
  - [https://github.com/mikeblum/otel-explorer-go-docs/blob/3797539be4f5a760e99586c0de72496019f5e6b0/instrumentation-list.yaml](https://github.com/mikeblum/otel-explorer-go-docs/blob/3797539be4f5a760e99586c0de72496019f5e6b0/instrumentation-list.yaml)
- [Robert] [https://github.com/open-telemetry/sig-security/issues/164](https://github.com/open-telemetry/sig-security/issues/164)
  - AI (pellared): Update releasing docs and ask for enabling for OTel Go

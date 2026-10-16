## Meeting Notes

### Attendees
- Denys Sedchenko (Grafana Labs)
- Ted Young (Grafana Labs)
- Antoine Toulme (Splunk)

### Agenda
- [Ted] SBOM discussion
  - [https://github.com/open-telemetry/opentelemetry-specification/issues/5353](https://github.com/open-telemetry/opentelemetry-specification/issues/5353)
  - Many SIGs are already releasing some form of SBOM
  - .NET, Collector, OBI
  - [https://github.com/open-telemetry/opentelemetry-packaging/pull/136](https://github.com/open-telemetry/opentelemetry-packaging/pull/136)
  - K8s has a tool for managing SBOMs:
    - [https://github.com/kubernetes-sigs/bom](https://github.com/kubernetes-sigs/bom)
    - Not sure if it matches our use case, needs investigation
- [Denys] COPR integration
  - [PR](https://github.com/open-telemetry/opentelemetry-packaging/pull/160) is ready for a review
  - Can’t access Cloudflare R2 still
  - Opening [https://github.com/open-telemetry/community/issues/3783](https://github.com/open-telemetry/community/issues/3783) to get access

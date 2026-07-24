## Meeting Notes

### Attendees
- Tyler Yahn (Splunk)
- David Ashpole (Google)
- Lewis Lewis (Datadog)
- Puneet Singh
- Bryan Boreham (Grafana Labs)

### Agenda
- [Tyler] [v1.45.0](https://github.com/open-telemetry/opentelemetry-go/milestone/81) milestone
  - Ready to merge:
    - [https://github.com/open-telemetry/opentelemetry-go/pull/8620](https://github.com/open-telemetry/opentelemetry-go/pull/8620)
  - Needs Review:
    - [https://github.com/open-telemetry/opentelemetry-go/pull/8599](https://github.com/open-telemetry/opentelemetry-go/pull/8599)
    - [https://github.com/open-telemetry/opentelemetry-go/pull/8611](https://github.com/open-telemetry/opentelemetry-go/pull/8611)
    - [https://github.com/open-telemetry/opentelemetry-go/pull/8415](https://github.com/open-telemetry/opentelemetry-go/pull/8415)
    - [https://github.com/open-telemetry/opentelemetry-go-contrib/pull/9337](https://github.com/open-telemetry/opentelemetry-go-contrib/pull/9337)
  - Fix-or-defer:
    - [https://github.com/open-telemetry/opentelemetry-go/pull/8443](https://github.com/open-telemetry/opentelemetry-go/pull/8443)
  - Address or drop:
    - [https://github.com/open-telemetry/opentelemetry-go/issues/7083](https://github.com/open-telemetry/opentelemetry-go/issues/7083)
    - [https://github.com/open-telemetry/opentelemetry-go/issues/2547](https://github.com/open-telemetry/opentelemetry-go/issues/2547)
- [Tyler] [2026 goals](https://github.com/open-telemetry/opentelemetry-go/issues?q=label%3A%22goal%3A+2026%22)
  - **Logs API GA:** [#7801](https://github.com/open-telemetry/opentelemetry-go/issues/7801)
    - Define the remaining GA exit criteria after the current Logs lifecycle fixes.
    - Commit to a target release.
  - **SDK self-observability:** [#2547](https://github.com/open-telemetry/opentelemetry-go/issues/2547), [#7017](https://github.com/open-telemetry/opentelemetry-go/issues/7017), [PR #7124](https://github.com/open-telemetry/opentelemetry-go/pull/7124)
    - Decide whether #2547 is genuinely a v1.45.0 deliverable.
    - Assign review and merge ownership for #7124.
  - **Metric SDK optimization:** [#7796](https://github.com/open-telemetry/opentelemetry-go/issues/7796), [#7743](https://github.com/open-telemetry/opentelemetry-go/issues/7743)
    - Decide which remaining optimizations define completion.
    - Assign reviewers for [#8598](https://github.com/open-telemetry/opentelemetry-go/pull/8598).
    - Assign an owner and date for the performance-results blog post.
  - **Prometheus exporter GA:** [#7799](https://github.com/open-telemetry/opentelemetry-go/issues/7799)
    - Specification stabilization and compliance work in [#4515](https://github.com/open-telemetry/opentelemetry-go/issues/4515), [#4516](https://github.com/open-telemetry/opentelemetry-go/issues/4516), and [#6718](https://github.com/open-telemetry/opentelemetry-go/issues/6718).
  - **Go runtime metrics stabilization**
- [Lewis] +2 Azure Resource Detectors
  - [[issue](https://github.com/open-telemetry/opentelemetry-go-contrib/issues/9285)] [https://github.com/open-telemetry/opentelemetry-go-contrib/pull/9289](https://github.com/open-telemetry/opentelemetry-go-contrib/pull/9289)
  - [[issue](https://github.com/open-telemetry/opentelemetry-go-contrib/issues/9286)] [https://github.com/open-telemetry/opentelemetry-go-contrib/pull/9290](https://github.com/open-telemetry/opentelemetry-go-contrib/pull/9290)
- [Puneet]
  - Docker Detector Review; [https://github.com/open-telemetry/opentelemetry-go-contrib/pull/9001](https://github.com/open-telemetry/opentelemetry-go-contrib/pull/9001)
  - MeterConfigurator
    - OpAMP
    - Declarative Config
    - Spec (Configurator characteristics, Producer)

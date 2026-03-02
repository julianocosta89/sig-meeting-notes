## Meeting Notes

### Attendees
- [Andrzej Stencel](mailto:andrzej.stencel@elastic.co) (Elastic)
- Tiffany Hrabusa (Grafana Labs)
- Edmo Vamerlatti (Elastic)
- Israel Blancas (Coralogix)
- Curtis Robert (Splunk)
- Evan Bradley (Dynatrace)
- [Paulo Janotti](mailto:pjanotti@splunk.com) (Splunk)
- [Jade Guiton](mailto:jade.guiton@datadoghq.com) (Datadog)
- Pablo Baeyens (Datadog) [only for the first 10 mins]
- David Ashpole (Google)
- [Sam DeHaan](mailto:sam.dehaan@grafana.com)(Grafana Labs)
- Pavol Loffay (Red Hat)
- Arianna Vespri (OllyGarden) [only for the first 15 mins]
- Dakota Paasman (Bindplane)
- Kyle Eckhart (Grafana Labs)
- [Yang Song](mailto:yang.song@datadoghq.com) (Datadog)
- Braydon Kains (Google)

### Agenda
- [15 min] Go through high priority issues for [stability phase 1](https://github.com/open-telemetry/opentelemetry-collector-contrib/issues/44130) listed on the [**board**](https://github.com/orgs/open-telemetry/projects/178)
- [Evan] Provide access to `context.Context` in OTTL
  - Should we put things like this under `otelcol`? (`external`?)
  - Or does a top-level path like `request` or `client` make sense?
  - We don’t want `ctx` or `context` since that term is already overloaded and doesn’t have an explicit meaning to end users who are not Go programmers.
- [Evan] If any Prometheus community members are around: are there opportunities to simplify configuring metric start times with the Prometheus receiver?
  - [dashpole] The prometheus receiver has removed all unknown start time handling to make this cleaner, and moved all start time handling to the [metricstarttime processor](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/main/processor/metricstarttimeprocessor). The prometheus receiver does support start time for scrape protocols that include it (currently openmetrics 1.0, but it is extremely expensive), but it is generally not common to have start times in Prometheus scrape formats. We are working on [improving this in OpenMetrics 2.0](https://prometheus.io/docs/specs/om/open_metrics_spec_2_0/#counter-1), by including the start timestamp on each line.
  - See [https://github.com/open-telemetry/opentelemetry-collector-contrib/issues/37186](https://github.com/open-telemetry/opentelemetry-collector-contrib/issues/37186) for discussion on the component being a receiver helper. There were no strong opinions at the time from my recollection.
    - [Evan] Thank you. I’ll reach out again if I have any concrete proposals for attempting to improve UX here.
  - [Kyle] Long term prometheus is [intending to natively support starttime + delta](https://github.com/prometheus/prometheus/issues/17649) but as noted by [dashpole] this won’t help the receiver use case
    - [dashpole] This is only for the OTLP -> Prometheus path.This is about Prometheus -> OTLP. There are no plans for Prometheus scrape protocols to support delta.
- [Tiffany] Update on Collector docs refactoring - Phase 2 about to begin
  - [Project description](https://github.com/open-telemetry/opentelemetry.io/blob/main/projects/collector-docs-refactor/collector-docs-refactor.md)
  - [Project board](https://github.com/orgs/open-telemetry/projects/174/views/2?sliceBy%5Bvalue%5D=otelcol-phase-1)
- [Tiffany] OTel Unplugged - Feb 2 - Brussels - the day after FOSDEM
  - [Registration](https://events.humanitix.com/otelunplugged-eu2026)
- [Pavol] Collector config JSON schema using the mdatagen: [https://github.com/open-telemetry/opentelemetry-collector/pull/14288](https://github.com/open-telemetry/opentelemetry-collector/pull/14288)
  - Another solution  [https://github.com/open-telemetry/opentelemetry-collector-contrib/pull/45123](https://github.com/open-telemetry/opentelemetry-collector-contrib/pull/45123)
- [Israel] Can you take a look at this ticket for awsecsattributesd processor? We would like to get some consensus to continue with the work
  - [https://github.com/open-telemetry/opentelemetry-collector-contrib/issues/44476](https://github.com/open-telemetry/opentelemetry-collector-contrib/issues/44476)

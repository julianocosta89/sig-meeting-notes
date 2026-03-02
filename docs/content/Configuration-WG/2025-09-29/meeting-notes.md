## Meeting Notes

### Attendees
- Tyler Yahn (Splunk)
- [Gregor Zeitlinger](mailto:gregor.zeitlinger@grafana.com) (Grafana)
- Alex Boten (Honeycomb)

### Agenda
- [Gregor] [default value handling not specified](https://github.com/open-telemetry/opentelemetry-specification/issues/4662)
  - [https://github.com/open-telemetry/opentelemetry-specification/blob/main/specification/configuration/sdk-environment-variables.md#batch-span-processor](https://github.com/open-telemetry/opentelemetry-specification/blob/main/specification/configuration/sdk-environment-variables.md#batch-span-processor)
  - In long run, spec will refer to declarative config directly
  - AI Gregor answer - done
- [alex] enable/disable pretty print [https://github.com/open-telemetry/opentelemetry-configuration/issues/300](https://github.com/open-telemetry/opentelemetry-configuration/issues/300)
  - Use stdout_otlp (or otlp_file) instead if you want to rely on the format
- [alex] Consistency in `ExperimentalTracerConfig` and `ExperimentalTracerMatcherAndConfig` [https://github.com/open-telemetry/opentelemetry-configuration/issues/304](https://github.com/open-telemetry/opentelemetry-configuration/issues/304) [https://github.com/open-telemetry/opentelemetry-configuration/issues/305](https://github.com/open-telemetry/opentelemetry-configuration/issues/305)
- [Triage project board](https://github.com/orgs/open-telemetry/projects/38)
- Who to ping for documentation
  - Go: Alex Boten [https://github.com/codeboten](https://github.com/codeboten)
  - PHP: Brett [https://github.com/brettmc](https://github.com/brettmc)
  - C++: Marc [https://github.com/marcalff](https://github.com/marcalff)
  - JS: [Marylia Gutierrez](mailto:marylia.gutierrez@grafana.com) [https://github.com/maryliag](https://github.com/maryliag)
  - Erlang: Tristan [https://github.com/tsloughter](https://github.com/tsloughter)
  - AI Gregor to ping people - [https://github.com/open-telemetry/opentelemetry-configuration/issues/309](https://github.com/open-telemetry/opentelemetry-configuration/issues/309)

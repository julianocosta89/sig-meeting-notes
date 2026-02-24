## Meeting Notes

### Attendees
- [Ivo Anjo](mailto:ivo.anjo@datadoghq.com) (Datadog)
- Jay DeLuca (Grafana Labs)
- [John Watson](mailto:jkwatson@gmail.com)(Sublime Security)
- Jonathan Halliday (IBM)
- Jason (Splunk)
- [Gregor Zeitlinger](mailto:gregor.zeitlinger@grafana.com) (Grafana Labs)
- Jack Shirazi (Elastic)
- Peter Findeisen (Cisco)
- Bruno Baptista (IBM)

### Agenda
- Standing topic: issue triage
  - [is:open -label:"needs u feedback","needs repro","contribution welcome"](https://github.com/open-telemetry/opentelemetry-java-instrumentation/issues?q=is%3Aissue+is%3Aopen+-label%3A%22needs+author+feedback%22%2C%22needs+repro%22%2C%22contribution+welcome%22)
  - [is:open label:"needs triage"](https://github.com/open-telemetry/opentelemetry-java-instrumentation/issues?q=is%3Aissue+is%3Aopen+label%3A%22needs+triage%22)
- Standing topic: [stackoverflow questions](https://stackoverflow.com/search?tab=newest&q=%5bopen-telemetry%5d%20java)
- [Jonathan/Ivo] PoC for OTEP: Process Context: Sharing Resource Attributes with External Readers.  see prev notes in Jan 22nd 2026 and Oct 30th 2025 meetings, spec at [https://github.com/open-telemetry/opentelemetry-specification/pull/4719](https://github.com/open-telemetry/opentelemetry-specification/pull/4719)  and Java demo using panama FFM at [https://github.com/ivoanjo/proc-level-demo/tree/main/otel-java-extension-demo](https://github.com/ivoanjo/proc-level-demo/tree/main/otel-java-extension-demo) - everyone ok with this going forward as ‘requires Java 25+’ only ?
  - [jack s] How does this relate to [https://github.com/open-telemetry/opentelemetry-specification/pull/4855](https://github.com/open-telemetry/opentelemetry-specification/pull/4855) and that approach? [jh: see [https://github.com/open-telemetry/opentelemetry-specification/pull/4855#discussion_r2768535087](https://github.com/open-telemetry/opentelemetry-specification/pull/4855#discussion_r2768535087) ? ]
  - Elastic implementation – [https://github.com/elastic/apm/blob/bd5fa9c1/specs/agents/universal-profiling-integration.md](https://github.com/elastic/apm/blob/bd5fa9c1/specs/agents/universal-profiling-integration.md)
- [jack b] opentelemetry-java release
  - Planning on merging stabilize complex attribute [https://github.com/open-telemetry/opentelemetry-java/pull/7973](https://github.com/open-telemetry/opentelemetry-java/pull/7973)
  - Nice to have
    - Split out cumulative vs. delta storage [https://github.com/open-telemetry/opentelemetry-java/pull/8015](https://github.com/open-telemetry/opentelemetry-java/pull/8015)

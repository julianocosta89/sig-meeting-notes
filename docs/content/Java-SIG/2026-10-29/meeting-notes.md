## Meeting Notes

### Attendees
- [Gregor Zeitlinger](mailto:gregor.zeitlinger@grafana.com)(Grafana)
- [John Watson](mailto:jkwatson@gmail.com)(Sublime Security)
- Jason (Splunk)
- Jack Berg (Grafana Labs)
- Trask Stalnaker (Microsoft)
- Jonathan Halliday (IBM)
- Bruno Baptista (IBM)
- Pranav Sharma (Google)
- Peter Findeisen (Cisco)

### Agenda
- Java Instrumentation v3 review
- Some Spec issues
  - [https://github.com/open-telemetry/opentelemetry-specification/pull/4809](https://github.com/open-telemetry/opentelemetry-specification/pull/4809)
  - [https://github.com/open-telemetry/opentelemetry-specification/pull/5393](https://github.com/open-telemetry/opentelemetry-specification/pull/5393)
- Potential interactive review candidates?
  - Context scoped attributes [https://github.com/open-telemetry/opentelemetry-java/pull/8947](https://github.com/open-telemetry/opentelemetry-java/pull/8947)
  - Opt in metric advice [https://github.com/open-telemetry/opentelemetry-java/pull/8979](https://github.com/open-telemetry/opentelemetry-java/pull/8979)
    - Could be nice but instrumentation not clamoring for it
    - [jack] Would prefer a feature that had more symmetry across signals
- [trask/jack] [Prepare for host entity by merging HostResource and HostIdResource](https://github.com/open-telemetry/opentelemetry-java-instrumentation/pull/20816#discussion_r4363557499)

## Meeting Notes

### Attendees
- Trask Stalnaker (Microsoft)
- Jay DeLuca (Grafana Labs)
- [Gregor Zeitlinger](mailto:gregor.zeitlinger@grafana.com) (Grafana Labs)
- Luke Zhang (AWS)
- Jason (Splunk)
- cleverchuk(solarwinds)
- [John Watson](mailto:jkwatson@gmail.com)(Cloudera)
- Tyler Benson (ServiceNow)
- Peter Findeisen (Cisco)
- Jonathan Halliday (IBM)
- Pranav Sharma (Google)
- Robert Niedziela (Splunk)
- Jack Shirazi (Elastic)
- Lauri Tulmin (Splunk)

### Agenda
- [Gregor] Classloading with bridge
  - [https://github.com/open-telemetry/opentelemetry-java-instrumentation/pull/14497](https://github.com/open-telemetry/opentelemetry-java-instrumentation/pull/14497) (already merged)
  - Instrumentation-api-incubator now has part of its content in agent classloader (was all bootstrap before)
  - Should it be in SDK vs API?
- [Jay] Gradle 9 PSA: [https://github.com/open-telemetry/opentelemetry-java-instrumentation/issues/14541](https://github.com/open-telemetry/opentelemetry-java-instrumentation/issues/14541)
- [Tyler] Making Disk Buffering contrib more efficient [https://github.com/open-telemetry/opentelemetry-java-contrib/pull/2190](https://github.com/open-telemetry/opentelemetry-java-contrib/pull/2190)
- [Gregor] Declarative config milestones

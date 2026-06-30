## Meeting Notes

### Attendees
- [John Watson](mailto:jkwatson@gmail.com)(Sublime Security)
- Jack Berg (Grafana Labs)
- Jay DeLuca (Grafana Labs)
- Trask Stalnaker (Microsoft)
- Peter Findeisen (Cisco)
- Pranav Sharma (Google)
- Lauri Tulmin (Splunk)
- [Gregor Zeitlinger](mailto:gregor.zeitlinger@grafana.com) (Grafana Labs)
- Jason (splunk)
- Jack Shirazi (Elastic)

### Agenda
- New Java repo approvers: Jay and Pranav
  - New Android approver: David
- Java Instrumentation V3
  - Targeting July release, so get things in before then if you can!
- [Jay] Inform: play with this: [https://explorer.opentelemetry.io/java-agent/configuration/builder](https://explorer.opentelemetry.io/java-agent/configuration/builder)
- [jack][inform] spec seems poised to deprecate opencensus shim: [https://github.com/open-telemetry/opentelemetry-specification/issues/5109](https://github.com/open-telemetry/opentelemetry-specification/issues/5109)
  - With this, we have a path to stop publishing zipkin exporter, opentracing shim, opencensus shim.
- [jack] opentelemetry-java release 1.63.0 tomorrow. Any requests?

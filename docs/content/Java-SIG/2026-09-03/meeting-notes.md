## Meeting Notes

### Attendees
- [John Watson](mailto:jkwatson@gmail.com)(Sublime Security)
- Jack Shirazi (Elastic)
- Jason (Splunk)
- Sylvain Juge (Elastic)
- Trask Stalnaker (Microsoft)
- Jonathan Halliday (IBM)
- Robert Niedziela (Splunk)
- Pranav Sharma (Google)
- Peter Findeisen (Cisco)
- Lauri Tulmin (Splunk)

### Agenda
- [jason] JMX metrics
  - [https://github.com/open-telemetry/opentelemetry-java-instrumentation/pull/19889](https://github.com/open-telemetry/opentelemetry-java-instrumentation/pull/19889)
  - [https://github.com/open-telemetry/opentelemetry-java-instrumentation/pull/19890](https://github.com/open-telemetry/opentelemetry-java-instrumentation/pull/19890)
  - Let’s stabilize what’s already there first before adding the new stuff
    - Change the 99p (etc) thing first then PR on top of that
  - Breaking changes? If so 3.0 would be a good target.
    - The p99 vs. 99p
  - Try and call these out in the PRs.
- [sylvain] JMX metrics again
  - [https://github.com/open-telemetry/opentelemetry-java-instrumentation/pull/19782](https://github.com/open-telemetry/opentelemetry-java-instrumentation/pull/19782)
  - [https://github.com/open-telemetry/opentelemetry-java-instrumentation/pull/19783](https://github.com/open-telemetry/opentelemetry-java-instrumentation/pull/19783)
- Kafka has a lot of metrics [https://kafka.apache.org/30/operations/monitoring/](https://kafka.apache.org/30/operations/monitoring/)

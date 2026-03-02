## Meeting Notes

### Attendees
- Jonathan Halliday (Red Hat)
- Jay DeLuca
- [Gregor Zeitlinger](mailto:gregor.zeitlinger@grafana.com)(Grafana)
- Jack Berg (New Relic)
- Trask Stalnaker (Microsoft)
- Jean Bisutti (Microsoft)
- Pranav Sharma (Google)
- Jack Shirazi (Elastic)
- Bruno Baptista (Red Hat)
- Lauri Tulmin (Splunk)

### Agenda
- [lauri] fixing 2.17 agent release
  - JReleaser
- [gregor] Declarative config
  - [Disallow old config file when declarative config is used](https://github.com/open-telemetry/opentelemetry-java-instrumentation/issues/14131)?
    - Deprecate old file long term
    - Mutually exclusive
  - [declarative config: property translation gaps](https://github.com/open-telemetry/opentelemetry-java-instrumentation/issues/14132)
    - Instrumentation - java - javaagent
      - Or instrumentation - java - agent - let’s discuss in PR
    - Thread details should be a named processor that needs to be added explicitly
      - Or otel.instrumentation.java.**thread-details**.enabled
    - otel.instrumentation.java.**http**.somethingjavaspecific…
    - otel.instrumentation.java.**common.**http.
    - Otel.instrumentation.java.**common.**thread-details.enabled - use this
    - otel.instrumentation.**common**.http.*
- [jay] metadata project
  - For documenting telemetry emitted by instrumentations that have both a javaagent implementation and also a library option, should we split the telemetry out by library vs javaaagent? Do we expect there to be any differences in each implementation that would result in differences to the telemetry?
  - Does [the current representation of span data](https://github.com/open-telemetry/opentelemetry-java-instrumentation/blob/main/docs/instrumentation-list.yaml#L33-L59) make sense in terms of including a set of attributes by span kind?
- [sylvain] jmx metrics with multiple mbeans [#14070](https://github.com/open-telemetry/opentelemetry-java-instrumentation/issues/14070) ([#14067](https://github.com/open-telemetry/opentelemetry-java-instrumentation/pull/14067) for jetty), should we remove gauge metrics that are fine most of the time but could potentially report invalid data ?

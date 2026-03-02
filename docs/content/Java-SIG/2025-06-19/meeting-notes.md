## Meeting Notes

### Attendees
- Jonathan Halliday (Red Hat)
- [Gregor Zeitlinger](mailto:gregor.zeitlinger@grafana.com)(Grafana)
- Jack Shirazi (Elastic)
- Peter Findeisen (Cisco)
- Trask Stalnaker (Microsoft)
- Lauri Tulmin (Splunk)

### Agenda
- Standing topic: issue triage
  - [is:open -label:"needs author feedback","needs repro","contribution welcome"](https://github.com/open-telemetry/opentelemetry-java-instrumentation/issues?q=is%3Aissue+is%3Aopen+-label%3A%22needs+author+feedback%22%2C%22needs+repro%22%2C%22contribution+welcome%22)
  - [is:open label:"needs triage"](https://github.com/open-telemetry/opentelemetry-java-instrumentation/issues?q=is%3Aissue+is%3Aopen+label%3A%22needs+triage%22)
- Standing topic: [stackoverflow questions](https://stackoverflow.com/search?tab=newest&q=%5bopen-telemetry%5d%20java)
- [jack s] Make “methods” instrumentation dynamic or create a new duplicate-ish instrumentation for that?
  - Most likely turn on instrumentation for added methods but just stop reporting for deleted ones
- [trask] GitHub projects?
  - 3.0
  - Stable database semconv
  - [Declarative configuration](https://github.com/orgs/open-telemetry/projects/151/views/1)
- [gregor] Declarative config should be good to go for Java agent
  - autoconfig customizer doesn’t work with declarative configuration?
    - Is this missing?
      - [https://github.com/open-telemetry/opentelemetry-java-instrumentation/blob/main/javaagent-tooling/src/main/java/io/opentelemetry/javaagent/tooling/AddThreadDetailsSpanProcessor.java](https://github.com/open-telemetry/opentelemetry-java-instrumentation/blob/main/javaagent-tooling/src/main/java/io/opentelemetry/javaagent/tooling/AddThreadDetailsSpanProcessor.java)
    - MDC resource attributes may not work with declarative config
    - Custom agent distributions with autoconfig customizers won’t work
  - How to (should we?) run integration tests with declarative configuration?
    - Is there a way to centralize this so we can matrix it out in GitHub actions
    - (and only run against latest LTS Java version - or Java 8)
  - Smoke test with declarative config
    - thread details
    - MDC resource attributes
- [Jack s/Sylvain] JMX metrics, asking for feedback/ideas on [#14070](https://github.com/open-telemetry/opentelemetry-java-instrumentation/issues/14070) as it prevents progress on [#14067](https://github.com/open-telemetry/opentelemetry-java-instrumentation/pull/14067)
  - [https://github.com/open-telemetry/opentelemetry-java/blob/2eb84bf41752c85ceee17ed91b0140253d3c1cac/sdk/metrics/src/main/java/io/opentelemetry/sdk/metrics/InstrumentBuilder.java#L124C8-L124C27](https://github.com/open-telemetry/opentelemetry-java/blob/2eb84bf41752c85ceee17ed91b0140253d3c1cac/sdk/metrics/src/main/java/io/opentelemetry/sdk/metrics/InstrumentBuilder.java#L124C8-L124C27)

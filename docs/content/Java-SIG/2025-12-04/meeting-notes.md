## Meeting Notes

### Attendees
- Jonathan Halliday (IBM)
- Jack Berg (Grafana Labs)
- John Watson (Cloudera)
- Jay DeLuca (Grafana Labs)
- Jack Shirazi (Elastic)
- Trask Stalnaker (Microsoft)
- cleverchuk(solarwinds)
- Lauri Tulmin (Splunk)
- Peter Findeisen (Cisco)
- Jason (Splunk)

### Agenda
- Standing topic: issue triage
  - [is:open -label:"needs author feedback","needs repro","contribution welcome"](https://github.com/open-telemetry/opentelemetry-java-instrumentation/issues?q=is%3Aissue+is%3Aopen+-label%3A%22needs+author+feedback%22%2C%22needs+repro%22%2C%22contribution+welcome%22)
  - [is:open label:"needs triage"](https://github.com/open-telemetry/opentelemetry-java-instrumentation/issues?q=is%3Aissue+is%3Aopen+label%3A%22needs+triage%22)
- Standing topic: [stackoverflow questions](https://stackoverflow.com/search?tab=newest&q=%5bopen-telemetry%5d%20java)
- [jack b] 1.57.0 SDK release
  - Ready to go!
- c/o from 20-nov [trask] [https://github.com/open-telemetry/opentelemetry-specification/pull/4738](https://github.com/open-telemetry/opentelemetry-specification/pull/4738)
  - Proposal for remote control via OpAmp
  - Example
    - Want to be able to update the sampler (e.g. composite / rule-based sampler)
    - Leverage specific sampler declarative configuration type definitions
- [Jack s] [dynamic update callbacks](https://github.com/open-telemetry/opentelemetry-java-instrumentation/issues/15228#issuecomment-3543289401) etc
  - Goal is to autocreate declarative config via system properties: [https://github.com/open-telemetry/opentelemetry-java-instrumentation/pull/15339](https://github.com/open-telemetry/opentelemetry-java-instrumentation/pull/15339)
- [jack b] Working on log bridge story: How do logs / events recorded via OpenTelemetry log API end up in standard log4j2 / logback output (i.e. console)?
  - Without agent: LogRecordProcessor which bridges to SLF4J + cycle detection code
  - With agent: need to do something like we do with `otel.javaagent.logging=application`
    - Should restrict to requiring SLF4J 2.0 API to maintain structure, which is heavily emphasized in OpenTelemetry log API

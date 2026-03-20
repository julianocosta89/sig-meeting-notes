## Meeting Notes

### Attendees
- Jay DeLuca (Grafana Labs)
- [Bruce Bujon](mailto:bruce.bujon@datadoghq.com) (Datadog)
- Trask Stalnaker (Microsoft)
- Jack Berg (Grafana Labs)
- Jonathan Halliday (IBM)
- [Gregor Zeitlinger](mailto:gregor.zeitlinger@grafana.com) (Grafana Labs)
- Jack Shirazi (Elastic)
- Pranav Sharma (Google)
- Cleverchuk (Solarwinds)
- Peter Findeisen (Cisco)
- Bruno Baptista (IBM)
- Robert Niedziela (Splunk)
- Lauri Tulmin (Splunk)

### Agenda
- Standing topic: issue triage
  - [is:open -label:"needs u feedback","needs repro","contribution welcome"](https://github.com/open-telemetry/opentelemetry-java-instrumentation/issues?q=is%3Aissue+is%3Aopen+-label%3A%22needs+author+feedback%22%2C%22needs+repro%22%2C%22contribution+welcome%22)
  - [is:open label:"needs triage"](https://github.com/open-telemetry/opentelemetry-java-instrumentation/issues?q=is%3Aissue+is%3Aopen+label%3A%22needs+triage%22)
- Standing topic: [stackoverflow questions](https://stackoverflow.com/search?tab=newest&q=%5bopen-telemetry%5d%20java)
- [Jay] Metadata population for agent instrumentation is just about done! Starting to build out tools that use it
  - Working on a Declarative configuration builder UI for the java agent in the [ecosystem explorer](https://github.com/open-telemetry/opentelemetry-ecosystem-explorer) project ([Sketch / POC](https://deploy-preview-151--otel-ecosystem-explorer.netlify.app/java-agent/configuration))
    - Similar - converter to set up DC: [https://github.com/open-telemetry/opentelemetry.io/pull/9456](https://github.com/open-telemetry/opentelemetry.io/pull/9456) (Gregor)
    - Sampler seems to be missing - but it’s in the getting started snippet
  - Agent report card for tracking 3.0 progress ([WIP](https://jaydeluca.github.io/agent-report-card/))
- [Gregor] Speed up builds - is it worth it? [https://github.com/open-telemetry/opentelemetry-java-instrumentation/pull/16436](https://github.com/open-telemetry/opentelemetry-java-instrumentation/pull/16436)
  - Smoke tests: one for each app server (e.g. tomcat / jdk 8, tomee 11, ..)
  - Plugin for caching docker images - 10G cache limit
    - Test containers - not smoke tests
    - No easy answers there
- [jack] Java specific property for declarative config: [https://github.com/open-telemetry/opentelemetry-java/pull/8164#discussion_r2926999917](https://github.com/open-telemetry/opentelemetry-java/pull/8164#discussion_r2926999917)

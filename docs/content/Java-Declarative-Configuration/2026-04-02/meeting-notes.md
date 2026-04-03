## Meeting Notes

### Attendees
- Jack Berg (Grafana Labs)
- Jason (Splunk)
- Jay DeLuca (Grafana Labs)
- Lauri Tulmin (Splunk)
- Pranav Sharma (Google)
- John Watson (Sublime Security)

### Agenda
- Standing topic: issue triage
  - [is:open -label:"needs u feedback","needs repro","contribution welcome"](https://github.com/open-telemetry/opentelemetry-java-instrumentation/issues?q=is%3Aissue+is%3Aopen+-label%3A%22needs+author+feedback%22%2C%22needs+repro%22%2C%22contribution+welcome%22)
  - [is:open label:"needs triage"](https://github.com/open-telemetry/opentelemetry-java-instrumentation/issues?q=is%3Aissue+is%3Aopen+label%3A%22needs+triage%22)
- Standing topic: [stackoverflow questions](https://stackoverflow.com/search?tab=newest&q=%5bopen-telemetry%5d%20java)
- [Jay] [marylia.gutierrez@grafana.com](mailto:marylia.gutierrez@grafana.com) is collecting questions SIG’s might want included in an upcoming end-user survey. If you have any ideas, send them along to her.
  - Example: What versions of Java are you running?
  - [jason] ideas
    - What was the hardest part of installing/configuring the agent?
    - Are you planning on migrating to declarative yaml config for your java instrumentation? Why?
    - Are you using libraries that are missing auto-instrumentation?
  - [jack] Ideas
    - Most important semantic convention domains
    - Most important instrumentation libraries
    - Interested / prefer in library or auto or native instrumentation?
    - What OTLP protocol is used? gRPC vs. http/protobuf
    - Are you using zipkin exporter?
    - If we had a user facing log API (with routing to SLF4J problem solved) would you want to use it?
    - Are you using declarative configuration?
    - If you could snap your fingers and solve one problem with the otel java ecosystem, what would it be?
- [jack] Could use some eyes
  - [https://github.com/open-telemetry/opentelemetry-java/pull/8180](https://github.com/open-telemetry/opentelemetry-java/pull/8180)
  - [https://github.com/open-telemetry/opentelemetry-java/pull/7964](https://github.com/open-telemetry/opentelemetry-java/pull/7964)

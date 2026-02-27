## Meeting Notes

### Attendees
- Jay DeLuca (Grafana Labs)
- Trask Stalnaker (Microsoft)
- Jack Shirazi (Elastic)
- [Gregor Zeitlinger](mailto:gregor.zeitlinger@grafana.com)(Grafana Labs)
- Jason (Splunk)
- Jonathan Halliday (IBM)
- Pranav Sharma (Google)
- Jack Berg (Grafana Labs)
- Peter Findeisen (Cisco)
- Bruno Baptista (IBM)
- Cleverchuk (Solarwinds)
- Lauri Tulmin (Splunk)

### Agenda
- Standing topic: issue triage
  - [is:open -label:"needs u feedback","needs repro","contribution welcome"](https://github.com/open-telemetry/opentelemetry-java-instrumentation/issues?q=is%3Aissue+is%3Aopen+-label%3A%22needs+author+feedback%22%2C%22needs+repro%22%2C%22contribution+welcome%22)
  - [is:open label:"needs triage"](https://github.com/open-telemetry/opentelemetry-java-instrumentation/issues?q=is%3Aissue+is%3Aopen+label%3A%22needs+triage%22)
- Standing topic: [stackoverflow questions](https://stackoverflow.com/search?tab=newest&q=%5bopen-telemetry%5d%20java)
- [Sylvain/Jack] Request for feedback on [HTTP request body capture PoC](https://github.com/open-telemetry/opentelemetry-java-instrumentation/pull/16006)
- Jason - OpAMP client in the instrumentation agent?
  - [https://github.com/open-telemetry/opentelemetry-configuration/issues/544](https://github.com/open-telemetry/opentelemetry-configuration/issues/544)
  - Related
    - [https://github.com/open-telemetry/opentelemetry-specification/pull/4738](https://github.com/open-telemetry/opentelemetry-specification/pull/4738)
    - [https://github.com/open-telemetry/opentelemetry-java/pull/8076](https://github.com/open-telemetry/opentelemetry-java/pull/8076)
    - [https://github.com/open-telemetry/opentelemetry-specification/pull/4900](https://github.com/open-telemetry/opentelemetry-specification/pull/4900)
- [Jonathan] Student placement, working on observability overhead measurement
  - (jason) I thought there were some interesting ideas for this here: [https://github.com/open-telemetry/opentelemetry-java-instrumentation/issues/13855](https://github.com/open-telemetry/opentelemetry-java-instrumentation/issues/13855)
- [Jonathan] profiling signal goes alpha for KubeCon (late March), profiling support in Java SDK should fill out and start shipping soon-ish.
- [https://docs.google.com/document/d/1hrfElwEdoUQbj-fY0vVVN7kmWmlmn9F_eZzxMuVnVwo/edit?usp=sharing](https://docs.google.com/document/d/1hrfElwEdoUQbj-fY0vVVN7kmWmlmn9F_eZzxMuVnVwo/edit?usp=sharing) outlines the architecture options
  - Async Profiler
    - Can write OTLP to disk
    - Q: grab from memory and pass to Profiling SDK to allow updating in SDK pipeline
    - (Inferred spans using today)
  - JFR
  - eBPF profiler (context correlation via native, Java 25+)
- [jack] Status update on benchmarking: [https://open-telemetry.github.io/opentelemetry-java/benchmarks/](https://open-telemetry.github.io/opentelemetry-java/benchmarks/)
  - Next:
    - Tune display, i.e. make it easier to see series & select which are visible
    - Contextualize the test cases so viewers know how to interpret
    - Link / discuss about on [opentelemetry.io](http://opentelemetry.io)
    - Reduce variance?
    - Export benchmarks

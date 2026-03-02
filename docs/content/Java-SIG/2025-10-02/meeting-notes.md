## Meeting Notes

### Attendees
- [John Watson](mailto:jkwatson@gmail.com)(Cloudera)
- Jay DeLuca (Grafana Labs)
- Trask Stalnaker (Microsoft)
- Jason (Splunk)
- Peter Findeisen (Cisco)
- cleverchuk(solarwinds)
- Jonathan Halliday (IBM)

### Agenda
- [Jonathan] people with an interest in the profiling signal type may wish to read [https://docs.google.com/document/d/1hrfElwEdoUQbj-fY0vVVN7kmWmlmn9F_eZzxMuVnVwo/edit?usp=sharing](https://docs.google.com/document/d/1hrfElwEdoUQbj-fY0vVVN7kmWmlmn9F_eZzxMuVnVwo/edit?usp=sharing) in preparation for discussion. (we probably want JackBerg back from leave before discussing?)
  - What are main use cases for profiling signal
  - What functionality would we want to put into the SDK
  - Use cases
    - Ebpf (nothing needed in the SDK)
    - Collector can scrape JFR files (nothing needed in the SDK)
    - AsyncProfiler
      - There is no Profiling SDK
      - Has to be bound directly to OTLP profiling exporter
      - Has to be responsible for instantiating and configuring the OTLP profiling exporter
    - JFR
      - Splunk distro activates JFR in an agent listener
        - [https://github.com/signalfx/splunk-otel-java/blob/main/profiler/src/main/java/com/splunk/opentelemetry/profiler/JfrActivator.java](https://github.com/signalfx/splunk-otel-java/blob/main/profiler/src/main/java/com/splunk/opentelemetry/profiler/JfrActivator.java)
      - Splunk distro does JFR and maps into pprof
        - [https://github.com/signalfx/splunk-otel-java/blob/main/profiler/src/main/java/com/splunk/opentelemetry/profiler/exporter/PprofLogDataExporter.java](https://github.com/signalfx/splunk-otel-java/blob/main/profiler/src/main/java/com/splunk/opentelemetry/profiler/exporter/PprofLogDataExporter.java)
    - Drive profiler configuration through the SDK
      - Export pipeline
      - OTLP export endpoint
  - Signal correlation
    - How to get process level or thread level down to profiler
    - Splunk uses a custom [ContextAttached](https://github.com/signalfx/splunk-otel-java/blob/main/profiler/src/main/java/com/splunk/opentelemetry/profiler/events/ContextAttached.java) event in JFR to help facilitate this.
- [trask] [https://github.com/open-telemetry/opentelemetry-java-contrib/pull/1957](https://github.com/open-telemetry/opentelemetry-java-contrib/pull/1957)
  - Is everyone comfortable with this being in the vanilla Java agent distro?
  - [https://github.com/open-telemetry/opentelemetry-java-instrumentation/pull/14677](https://github.com/open-telemetry/opentelemetry-java-instrumentation/pull/14677)
- [Jay] PR and Issue cleanup progress to reduce noise & help us prioritize:
  - From 386 issues to 280
  - ![][image4]
- [Jay] Should we create a 3.0 project at some point? [Similar to the 2.0 one](https://github.com/orgs/open-telemetry/projects/54)
- [jason] When can we expect the [ExtendedLogger](https://github.com/open-telemetry/opentelemetry-java/blob/main/api/incubator/src/main/java/io/opentelemetry/api/incubator/logs/ExtendedLogger.java) to come out of the incubator?
- [Jay] (if we have time) PR / issue triage & discussions
  - [When should config properties include the word experimental? #13487](https://github.com/open-telemetry/opentelemetry-java-instrumentation/issues/13487)
    - Thoughts on if we want to pursue this, and if so, what action should be taken?
  - [Getting Micrometer Metrics Bridge from Alpha to Stable #13867](https://github.com/open-telemetry/opentelemetry-java-instrumentation/issues/13867)
    - Anything we should do here?
  - [MuzzleCodeGenerationPlugin is not a proper Byte Buddy plugin #13611](https://github.com/open-telemetry/opentelemetry-java-instrumentation/issues/13611)
    - Is this something we want to do? (Should we add “contribution welcome” ?)
  - [Request for VAPT Report for Open-Telemetry Agent, Otel Collector  #13029](https://github.com/open-telemetry/opentelemetry-java-instrumentation/issues/13029)
    - What is needed for something like this?

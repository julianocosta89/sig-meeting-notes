## Meeting Notes

### Attendees
- Jonathan Halliday (IBM)
- [John Watson](mailto:jkwatson@gmail.com)(Sublime Security)
- Jay DeLuca (Grafana Labs)
- Bruno Baptista (IBM)
- Jason (AppDynamics)
- [Pranav Sharma](mailto:sharmapranav@google.com) (Google)
- [Gregor Zeitlinger](mailto:gregor.zeitlinger@grafana.com) (Grafana Labs)
- Trask Stalnaker (Microsoft)
- Peter Findeisen (Cisco)
- Robert Niedziela (Splunk)
- Sylvain Juge (Elastic)
- Jack Shirazi (Elastic)

### Agenda
- Java Instrumentation v3 review
- [jason] [https://github.com/open-telemetry/opentelemetry-java-instrumentation/issues/19954](https://github.com/open-telemetry/opentelemetry-java-instrumentation/issues/19954)
  - What can we do about this?
  - Look at how core does it with ComponentLoader
  - OTLP exporter builders allow for supplying a custom ComponentLoader
  - Could do something similar with the InstrumenterBuilder
- [jack] Rewrote PMR to more closely match BatchSpanProcessor / BatchLogRecordProcessor [https://github.com/open-telemetry/opentelemetry-java/pull/8827](https://github.com/open-telemetry/opentelemetry-java/pull/8827)
  - Pros:
    - Simpler to understand / more symmetry with traces and logs
    - Much simpler to extend to add export timeout feature
  - Cons
    - New dedicated worker thread, analog to BSP / BLRP work thread
  - Consider:
    - 10k metrics, with batch configuration of 1000
    - Each collection (every 60s), 10 exports of 1000 metrics each
    - These 10 exports are sequential
      - Export 1 blocks export 2 until export 1 completable future resolves success, and so on
    - If we no timeout, then the 10 exports can block subsequent collections in perpetuity
    - If PMR/BSP don’t block on CompletableFuture, then
    - We need current world because of lack of back pressure contract
- [Jonathan] [Thread Context OTEP](https://github.com/open-telemetry/opentelemetry-specification/blob/main/oteps/profiles/4947-thread-ctx.md%20) requires an ELF symbol. That seems to mean shipping a native binary. Urg! Support or not in the SDK? (Process Context can use panama, doesn’t need JNI)
- [gregor] [Use declarative config throughout dynamic-control](https://github.com/open-telemetry/opentelemetry-java-contrib/pull/3013)
  - Required for agent 3.0 because the old DC bridge will be removed
  - Unrelated to that is cleans up a violation of DC semantics - reading the YAML file and system properties at the same time
    - DC says that the file is the only source of truth (but env var references can be used)
    - On top of that - it’s not possible to get the service name out of a loaded YAML file (because not in spec)
    - So you need to specify the service name twice
      - resource attributes
      - ID of service in OpAMP
- [Sylvain] jmx include stable by default PR [#19783](https://github.com/open-telemetry/opentelemetry-java-instrumentation/pull/19783)
  - Has been reworked to now only rely on metric names and not target system name
  - A follow-up PR will be required in contrib to accommodate for resource path change for jvm metrics now split in two.

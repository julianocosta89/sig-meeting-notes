## Meeting Notes

### Attendees
- Jay DeLuca (Grafana Labs)
- Trask Stalnaker (Microsoft)
- Jonathan Halliday (IBM)
- [Gregor Zeitlinger](mailto:gregor.zeitlinger@grafana.com) (Grafana Labs)
- Peter Findeisen (Cisco)
- Jack Shirazi (Elastic)
- Pranav Sharma (Google)
- Jason (Splunk)
- cleverchuk(solarwinds)
- Lauri Tulmin (Splunk)
- Antoine Toulme (Splunk)

### Agenda
- [Trask for Ziming] Extension for OpenTelemetry Installation
- startHttpSpan(...)
- Tracer.spanBuilder().setAttributeStruct(HttpReqAttr)
- TracerProviderExt.setAttributeStruct(...)
- For customizing TracerProvider could use
  - [https://github.com/open-telemetry/opentelemetry-java/blob/9631f5462b548a46c8bb3bd78cad06a0471da65f/sdk-extensions/autoconfigure/src/main/java/io/opentelemetry/sdk/autoconfigure/AutoConfiguredOpenTelemetrySdkBuilder.java#L418](https://github.com/open-telemetry/opentelemetry-java/blob/9631f5462b548a46c8bb3bd78cad06a0471da65f/sdk-extensions/autoconfigure/src/main/java/io/opentelemetry/sdk/autoconfigure/AutoConfiguredOpenTelemetrySdkBuilder.java#L418)
  - Would require SDK modification to load TracerProvider
- [Jay] [https://github.com/open-telemetry/opentelemetry-java-instrumentation/pull/14342](https://github.com/open-telemetry/opentelemetry-java-instrumentation/pull/14342)
  - [https://github.com/open-telemetry/community/pull/2684](https://github.com/open-telemetry/community/pull/2684)
- [Trask/Gregor] Move instrumentation repo’s DeclarativeConfigPropertiesBridge out of javaagent extension and into somewhere that library instrumentation (and spring boot starter) can use it
  - Move to instrumentation-api-incubator
  - AI Gregor
- [Trask] [https://github.com/open-telemetry/opentelemetry-java-contrib/pull/2146](https://github.com/open-telemetry/opentelemetry-java-contrib/pull/2146)
- [Trask/Gregor] Moving a couple of components to instrumentation repo
  - Baggage
  - Rule-based Sampler
  - Probability Sampler
    - Flakiness - what is acceptable?
  - Explore adding to specification
- [Antoine] [https://github.com/open-telemetry/opentelemetry-java-contrib/issues/2124](https://github.com/open-telemetry/opentelemetry-java-contrib/issues/2124)

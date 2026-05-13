## Meeting Notes

### Attendees
- Jason (Splunk)
- Cesar (Elastic)
- Hanson Ho [late] (Embrace)

### Agenda
- (jason) Release automation in java-instrumentation is leveraging LLMs to do nice summary/categorization of PRs (based on how terrible PR names always are). Should we adopt that too?
  - AI: Jason to create a tracking issue for this and to find out details
  - Should we also think about copilot reviews
  - AI: Cesar to create tracking issue for enabling copilot reviews
- [Cesar] Next modules to stabilize
  - Instrumentation api?
    - Next release [https://breedx-splk.github.io/when-is-the-next/](https://breedx-splk.github.io/when-is-the-next/)
    - Milestone [https://github.com/open-telemetry/opentelemetry-android/issues?q=is%3Aissue%20state%3Aopen%20milestone%3A%22Stabilize%20instrumentation%20API%22](https://github.com/open-telemetry/opentelemetry-android/issues?q=is%3Aissue%20state%3Aopen%20milestone%3A%22Stabilize%20instrumentation%20API%22)
    - 2 items remain, both non-critical but we want to include them just because
  - What comes next then?
    - Services but maybe we need to split off the pure api and keep the implementation internal?
    - Common is a bit of a hodgepodge
- [Cesar] Declarative config support
  - Have we had users ask for this?
  - Java has support for this
  - Kotlin does not
  - [https://opentelemetry.io/blog/2026/stable-declarative-config/](https://opentelemetry.io/blog/2026/stable-declarative-config/)
  - Has anyone explored doing pre-parsing of the yaml file at build time to pregenerate the objects?
    - A gradle plugin to help here?
  - Is there a plan to make any of it dynamic at runtime?
    - Some art happening in upstream:
      - [https://github.com/open-telemetry/opentelemetry-java-contrib/issues/2416](https://github.com/open-telemetry/opentelemetry-java-contrib/issues/2416)
      - [https://github.com/open-telemetry/opentelemetry-java-contrib/issues/2546](https://github.com/open-telemetry/opentelemetry-java-contrib/issues/2546)
  - Java spi [https://github.com/open-telemetry/opentelemetry-java/blob/main/sdk-extensions/declarative-config/src/main/java/io/opentelemetry/sdk/autoconfigure/declarativeconfig/DeclarativeConfigurationCustomizer.java](https://github.com/open-telemetry/opentelemetry-java/blob/main/sdk-extensions/declarative-config/src/main/java/io/opentelemetry/sdk/autoconfigure/declarativeconfig/DeclarativeConfigurationCustomizer.java)
- (jason) scheduled work / disk buffering

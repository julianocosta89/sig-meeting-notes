## Meeting Notes

### Attendees
- [Dario Castañé](mailto:dario.castane@datadoghq.com)
- [Dario Castañé](mailto:dario.castane@datadoghq.com) (Datadog); facilitator
- Azhar Momin
- Ishan Ghosh

### Agenda
- [https://github.com/open-telemetry/opentelemetry-go-compile-instrumentation/issues/1260](https://github.com/open-telemetry/opentelemetry-go-compile-instrumentation/issues/1260)
  - Related: [https://github.com/open-telemetry/opentelemetry-ecosystem-explorer/pull/1023/](https://github.com/open-telemetry/opentelemetry-ecosystem-explorer/pull/1023/)
  - Import URLs: Should we fully align our module path naming with opentelemetry-go-contrib?
    - Dario: it might be confusing to have URLs that are different from each other by one character (otelmongo/otelcmongo)
    - Third option: [http://go.opentelemetry.io/otelc-contrib/go.mongodb.org/mongo-driver/mongo/otelcmongo](http://go.opentelemetry.io/otelc-contrib/go.mongodb.org/mongo-driver/mongo/otelcmongo)
    - **Update: we go for [go.opentelemetry.io/otelc-contrib/instrumentation/go.mongodb.org/mongo-driver/mongo/otelcmongo](http://go.opentelemetry.io/otelc-contrib/instrumentation/go.mongodb.org/mongo-driver/mongo/otelcmongo)**
  - instrumentation/go.mod Dependency Leaks: Should we stop having a top-level go.mod in instrumentation/?
    - Dario: I agree, and we should introduce `crosslink` into the project to make sure any contrib depending on another doesn’t get out of sync when developing.
  - We will also need a way to declare the minimum otelc version required for an instrumentation to work since we are decoupling
    - Dario: 100% agree
  - Whole issue reviewed: LGTM
  - Reviewed [https://github.com/open-telemetry/opentelemetry-ecosystem-explorer/pull/1023/](https://github.com/open-telemetry/opentelemetry-ecosystem-explorer/pull/1023/): LGTM

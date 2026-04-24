## Meeting Notes

### Attendees
- Christos Markou (Elastic)
- Braydon Kains (Google)
- Dónal O’Sullivan (Elastic)

### Agenda
- [Dónal] Versioned metrics: [https://github.com/open-telemetry/opentelemetry-collector-contrib/issues/45592#issuecomment-4304702563](https://github.com/open-telemetry/opentelemetry-collector-contrib/issues/45592#issuecomment-4304702563)
  - Set strict validation around the slash, for example if there is slash force that the name override field should be used.
  - Another example component configs, using @ symbol.
  - Don’t use slash use @ symbol and just take everything before the @.
  - Emitting both legacy and new will provide issues with backends, potentially aggregating etc.
    - Need to properly design this.
    - https://github.com/open-telemetry/opentelemetry-collector/blob/main/docs/rfcs/semconv-feature-gates.md#handling-conflicts-during-double-publishing
- [Braydon] Settling `process.executable` discussion
- [Braydon] The otel-arrow collector has a proposal for their own `host_metrics` receiver implementation [https://github.com/open-telemetry/otel-arrow/issues/2741](https://github.com/open-telemetry/otel-arrow/issues/2741)
  - It will explicitly be supporting our conventions from the get-go
  - It's making a lot of design decisions that we would likely make if we were to redesign the Collector hostmetrics from the ground up

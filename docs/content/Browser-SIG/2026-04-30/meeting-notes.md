## Meeting Notes

### Attendees
- Jared Freeze (Embrace)
- Joaquin Diaz (Embrace)
- Abinet Debele (Cisco)
- Hugo Levy (Datadog)
- Maxime Quentin (Datadog)
- David Luna (Elastic)

### Agenda
- [david] fetch & XHR instrumentations
  - SDK 3.0 aims to have a single @opentelemetry/sdk-trace package with no utils
  - [https://github.com/open-telemetry/opentelemetry-js/pull/6630](https://github.com/open-telemetry/opentelemetry-js/pull/6630) based on [this comment](https://github.com/open-telemetry/opentelemetry-js/issues/6591#issuecomment-4266682684)
  - Sooner or later XHR & fetch should be moved to the browser repo. Could it be sooner?
    - Wondering if span events are needed now that we have resource timings instrumentation
    - Is there a way to add span context to resource timing logs? (different instrumentations sharing info)
    - … or just place shared code for now in `@opentelemetry/web-common` and be it a challenge for our future selves
    - Notes:
      - If moving to browser they should be refactored.
      - High usage of both (fetch , XHR)
      - By patching the methods (span based) we could get more data related o headers, size, etc…
- [Joaquin] Demo metrics [https://github.com/open-telemetry/opentelemetry-browser/issues/250](https://github.com/open-telemetry/opentelemetry-browser/issues/250)
- [Abinet] discuss on ​​[https://github.com/open-telemetry/opentelemetry-browser/discussions/243](https://github.com/open-telemetry/opentelemetry-browser/discussions/243)

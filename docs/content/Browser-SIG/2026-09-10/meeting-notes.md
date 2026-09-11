## Meeting Notes

### Attendees
- Bryan Atkinson (Firebase/Google)
- David Luna (Elastic)
- Maxime Quentin (Datadog)
- Wolfgang Therrien (Honeycomb.io)

### Agenda
- [david] Moving sdk-trace-web utils to web-common. Please review
  - [https://github.com/open-telemetry/opentelemetry-js/pull/7058](https://github.com/open-telemetry/opentelemetry-js/pull/7058)
- [bryan] Sampling - Looking for some context on
  - [https://github.com/open-telemetry/opentelemetry-browser/blob/94da2c5463f2ed455d2485dc1f521567ca7fbbee/packages/sdk/src/core/types.ts#L133-L138](https://github.com/open-telemetry/opentelemetry-browser/blob/94da2c5463f2ed455d2485dc1f521567ca7fbbee/packages/sdk/src/core/types.ts#L133-L138)
- [david] register instrumentations. Okay to merge it now and maybe change the behavior later?
  - [https://github.com/open-telemetry/opentelemetry-browser/pull/415](https://github.com/open-telemetry/opentelemetry-browser/pull/415)

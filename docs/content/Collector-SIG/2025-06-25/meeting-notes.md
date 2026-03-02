## Meeting Notes

### Attendees
- [Andrew Wilkins](mailto:axw@elastic.co) (Elastic)
- Josh MacDonald (Microsoft)
- [Jeff Alder](mailto:jalder@newrelic.com) (New Relic)
- [Paulo Janotti](mailto:pjanotti@splunk.com) (Splunk)

### Agenda
- Rate limiting conversation, referring to Josh’s recently opened PR.
- Discussion about where to bind weight keys, thinking about
  - The PR in question: [https://github.com/open-telemetry/opentelemetry-collector/pull/13265](https://github.com/open-telemetry/opentelemetry-collector/pull/13265)
  - In the limiters,
  - In the middleware,  yes: replace “id” with “limiters::request_bytes” e.g.,
  - In the receivers: we may want non-standard limiters
  - Thank you Andrew for the discussion.
- Josh adds for your entertainment: [https://github.com/open-telemetry/opentelemetry-collector/pull/13263](https://github.com/open-telemetry/opentelemetry-collector/pull/13263)
- Andrew asks about multi-tenant deployments of OTel Collector
  - Situation is that tenants are dynamic, come and go. Would like to monitor tenants.
  - Want to be able to monitor by tenant
  - Josh: see we have a prototype of the “MeasurementProcessor” idea here. [https://github.com/lightstep/otel-launcher-go/blob/main/lightstep/sdk/metric/README.md#measurementprocessor](https://github.com/lightstep/otel-launcher-go/blob/main/lightstep/sdk/metric/README.md#measurementprocessor)
  - Andrew will consider looking at a Collecto-specific solution, pursued here: [https://github.com/open-telemetry/opentelemetry-collector-contrib/issues/36809](https://github.com/open-telemetry/opentelemetry-collector-contrib/issues/36809)
  - Thanks all!

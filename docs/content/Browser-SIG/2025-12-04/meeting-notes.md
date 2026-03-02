## Meeting Notes

### Attendees
- David Luna (Elastic)
- Ted Young (Grafana Labs)
- Benoit Zugmeyer (Datadog)
- Marco Schaefer (Grafana Labs)
- Jared Freeze (Embrace)
- Joaquin Diaz (Embrace)
- Trent Mick (Elastic)
- Wolfgang Therrien (Honeycomb)

### Agenda
- [martin] [Navigation instrumentation](https://github.com/open-telemetry/opentelemetry-js-contrib/pull/3148)
  - do we want [sanitizing URLs](https://github.com/open-telemetry/opentelemetry-js-contrib/pull/3148/files#diff-3b105ff410519bc930d12b870994f2e31d06380be1ffa6fdeb8dbbff2898b22dR24) to be enabled by default?
    - Decision : off by default. Could be turned on in the future
    - Export the default function and document how to use it
- [Ted] Github projects kind of suck, the Collector is making good use of pinned issues and sub issues
  - [https://github.com/open-telemetry/opentelemetry-collector/issues](https://github.com/open-telemetry/opentelemetry-collector/issues)
  - [https://github.com/open-telemetry/opentelemetry-collector/issues/14065](https://github.com/open-telemetry/opentelemetry-collector/issues/14065)
- [david] Should we move on with [https://github.com/open-telemetry/opentelemetry-js-contrib/pull/3220](https://github.com/open-telemetry/opentelemetry-js-contrib/pull/3220)
  - Done!! 🎉
- [Jared] a few for review [https://github.com/open-telemetry/opentelemetry-browser/pulls](https://github.com/open-telemetry/opentelemetry-browser/pulls)

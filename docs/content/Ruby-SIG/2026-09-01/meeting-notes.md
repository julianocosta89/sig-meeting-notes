## Meeting Notes

### Attendees
- [Josef Šimánek](mailto:josef.simanek@gmail.com)
- Xuan Cao
- Hannah Ramadan
- Robb Kidd
- Matt Wear
- Kayla Reopelle

### Agenda
- [Spec SIG](https://docs.google.com/document/d/1pdvPeKjA8v8w_fGKAN68JjWBmVJtPCpqdi9IZrd6eEo/preview) Update (max 15 min)
  - More awareness with Entity SIG and resource detectors
  - [Clarify database `server.address` for multi-server clients](https://github.com/open-telemetry/semantic-conventions/pull/4058)
    - [https://github.com/trask/semantic-conventions/blob/11c6ff98678d840812808f84d973f6606cf6029e/docs/db/database-spans.md#database-server-endpoints](https://github.com/trask/semantic-conventions/blob/11c6ff98678d840812808f84d973f6606cf6029e/docs/db/database-spans.md#database-server-endpoints)
- Core ([Issues](https://github.com/open-telemetry/opentelemetry-ruby/issues) / [PRs](https://github.com/open-telemetry/opentelemetry-ruby/pulls))
  - OTLP Common gem getting released today
- Contrib ([Issues](https://github.com/open-telemetry/opentelemetry-ruby-contrib/issues) / [PRs](https://github.com/open-telemetry/opentelemetry-ruby-contrib/pulls))
  - [OpenAI Logs Implementation / CI not running OpenAI tests](https://github.com/open-telemetry/opentelemetry-ruby-contrib/pull/2552)
    - Currently installing the Logs API
    - Do we want to leave this package out of instrumentation-all?
      - No! Include it!
    - Do we want to add configs to protect against events being emitted?
      - Go ahead with PR above to guard logging on the presence of the unstable Logs API gem to opt-in
- Auto Instrumentation ([Issues](https://github.com/open-telemetry/opentelemetry-ruby-instrumentation/issues) / [PRs](https://github.com/open-telemetry/opentelemetry-ruby-instrumentation/pulls))
  - Yay! First release!
- Burning questions?
- ✨ Happy Reports ✨

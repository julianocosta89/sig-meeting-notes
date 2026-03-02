## Meeting Notes

### Attendees
- Kayla Reopelle
- Hannah Ramadan
- Xuan Cao

### Agenda
- [Spec SIG](https://docs.google.com/document/d/1pdvPeKjA8v8w_fGKAN68JjWBmVJtPCpqdi9IZrd6eEo/preview) Update (max 15 min)
- Core ([Issues](https://github.com/open-telemetry/opentelemetry-ruby/issues) / [PRs](https://github.com/open-telemetry/opentelemetry-ruby/pulls))
  - ​[https://github.com/open-telemetry/opentelemetry-ruby/pull/1822](https://github.com/open-telemetry/opentelemetry-ruby/pull/1822)
    - Slack + Spec SIG as next steps
    - Generally in discussion, our preference is gzip, but it seems strange that we have a default for an environment variable that isn’t required to be consistent in the spec
  - [https://github.com/open-telemetry/opentelemetry-ruby/issues/1658#issuecomment-2980293975](https://github.com/open-telemetry/opentelemetry-ruby/issues/1658#issuecomment-2980293975)
    - Comment isn’t quite about the issue
    - We have exponential retries already in the HTTP OTLP exporter
    - Share the links
    - Don’t have the max retries – could consider adding them
  - Async metrics PR
- Contrib ([Issues](https://github.com/open-telemetry/opentelemetry-ruby-contrib/issues) / [PRs](https://github.com/open-telemetry/opentelemetry-ruby-contrib/pulls))
  - HTTP span name fix: [https://github.com/open-telemetry/opentelemetry-ruby-contrib/pull/1570](https://github.com/open-telemetry/opentelemetry-ruby-contrib/pull/1570)
    - Would like another review, will merge on Wednesday otherwise
  - Request to add comments around the attribute updates on the dup/stable
  - HTTP clients in progress, HTTP server (Rack) is coming – let’s see where we get with clients and check in. Ideally they’re all up to date within a tight timeframe to drop support for the environment variable around the same time.
- Burning questions?
- ✨ Happy Reports ✨

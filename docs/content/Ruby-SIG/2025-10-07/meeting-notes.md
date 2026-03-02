## Meeting Notes

### Attendees
- Kayla Reopelle
- Hannah Ramadan
- Wendy Smoak
- Eric Mustin
- Robb Kidd
- Xuan Cao

### Agenda
- [Spec SIG](https://docs.google.com/document/d/1pdvPeKjA8v8w_fGKAN68JjWBmVJtPCpqdi9IZrd6eEo/preview) Update (max 15 min)
- Core ([Issues](https://github.com/open-telemetry/opentelemetry-ruby/issues) / [PRs](https://github.com/open-telemetry/opentelemetry-ruby/pulls))
  - ​​Review:  [https://github.com/open-telemetry/opentelemetry-ruby/pull/1869](https://github.com/open-telemetry/opentelemetry-ruby/pull/1869)
  - Review: [https://github.com/open-telemetry/opentelemetry-ruby/pull/1894](https://github.com/open-telemetry/opentelemetry-ruby/pull/1894)
  - [https://github.com/open-telemetry/opentelemetry-ruby/issues/1931](https://github.com/open-telemetry/opentelemetry-ruby/issues/1931)
    - Metrics Reporter has a hacky workaround
    - Eric will respond to Hazel
    - Sample metrics reporter in a code comment example. https://github.com/open-telemetry/opentelemetry-ruby/blob/23c5aaf445244b6b634ccdf8d557a56feda98831/sdk/lib/opentelemetry/sdk/trace/export/metrics_reporter.rb#L18-L29
    - I think user can customize the error_handler from:
    - https://github.com/open-telemetry/opentelemetry-ruby/blob/main/api/lib/opentelemetry.rb#L44
- Contrib ([Issues](https://github.com/open-telemetry/opentelemetry-ruby-contrib/issues) / [PRs](https://github.com/open-telemetry/opentelemetry-ruby-contrib/pulls))
  - [https://github.com/open-telemetry/opentelemetry-ruby-contrib/pull/1637](https://github.com/open-telemetry/opentelemetry-ruby-contrib/pull/1637)
    - Shutdown method not defined in the API
    - Add more protection around the method? &. Or respond to? Or defined or whatever
- Burning questions?
  - Ruby logger bridge? [https://github.com/open-telemetry/opentelemetry-ruby-contrib/pull/983](https://github.com/open-telemetry/opentelemetry-ruby-contrib/pull/983)
    - SHIP IT
    - May consider adding progname in the future, either as an extra attr or by including formatted_message
- ✨ Happy Reports ✨

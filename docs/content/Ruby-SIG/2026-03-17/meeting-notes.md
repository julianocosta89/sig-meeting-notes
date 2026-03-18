## Meeting Notes

### Attendees
- Daniel Azuma (~~Google~~)
- Kayla Reopelle (New Relic)
- Robb Kidd (Honeycomb)
- Arjun Rajappa (IBM Instana)
- Hannah Ramadan (New Relic)
- Ariel Valentin (GitHub)

### Agenda
- [Spec SIG](https://docs.google.com/document/d/1pdvPeKjA8v8w_fGKAN68JjWBmVJtPCpqdi9IZrd6eEo/preview) Update (max 15 min)
- Core ([Issues](https://github.com/open-telemetry/opentelemetry-ruby/issues) / [PRs](https://github.com/open-telemetry/opentelemetry-ruby/pulls))
  - ​​[Xuan] [https://github.com/open-telemetry/opentelemetry-ruby/pull/1609](https://github.com/open-telemetry/opentelemetry-ruby/pull/1609) (updated description with visual example)
  - [Robb] Got some updates to make to semconv templates.
    - Simplify yard doc output
    - Downgrade to 1.36
  - [everybody] How about scope-level schemaurl … and later attributes?
    - Instrumentation Scope PR [https://github.com/open-telemetry/opentelemetry-ruby/pull/2037](https://github.com/open-telemetry/opentelemetry-ruby/pull/2037)
- Contrib ([Issues](https://github.com/open-telemetry/opentelemetry-ruby-contrib/issues) / [PRs](https://github.com/open-telemetry/opentelemetry-ruby-contrib/pulls))
  - [kayla] Switching to rspec-mocks? ([#2059](https://github.com/open-telemetry/opentelemetry-ruby-contrib/pull/2059))
    - A bit concerned about the licensing related to diff-lcs (a transitive dependency)
    - Question about FOSSA scan: [https://cloud-native.slack.com/archives/C01NJ7V1KRC/p1773440075970859](https://cloud-native.slack.com/archives/C01NJ7V1KRC/p1773440075970859)
    - Need to fill out a license exception form: [https://github.com/open-telemetry/community/issues/2558](https://github.com/open-telemetry/community/issues/2558)
    - However, it’s unclear if those gems actually have a GPL-2.0 license
    - [robb] will also look for ways to appease the scanner
    - [arielvalentin] Will experiment with replacing rspec-mocks with minitest-mock.
  - [arielvalentin]
    - Change in_span helper to allow skipping recordException
      - [https://github.com/open-telemetry/opentelemetry-ruby-contrib/pull/2087](https://github.com/open-telemetry/opentelemetry-ruby-contrib/pull/2087)
- Burning questions?
- ✨ Happy Reports ✨

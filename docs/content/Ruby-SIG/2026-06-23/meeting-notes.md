## Meeting Notes

### Attendees
- Kayla Reopelle
- Matt Wear
- Arjun Rajappa
- Hannah Ramadan
- Xuan Cao
- Bart de Water

### Agenda
- [Spec SIG](https://docs.google.com/document/d/1pdvPeKjA8v8w_fGKAN68JjWBmVJtPCpqdi9IZrd6eEo/preview) Update (max 15 min)
- Core ([Issues](https://github.com/open-telemetry/opentelemetry-ruby/issues) / [PRs](https://github.com/open-telemetry/opentelemetry-ruby/pulls))
  - Semconv update / auto-release
    - Generally not risky
    - As long as rubocop and cspell pass, we’re good
    - Auto-release would need to verify that we don’t release something bad (semconv workflows, linting workflows, etc. are all green)
    - [https://github.com/open-telemetry/opentelemetry-ruby/pull/2185](https://github.com/open-telemetry/opentelemetry-ruby/pull/2185​)
    - Related issue: release of 1.41.0 gem is actually for 1.41.1 version
      - Defer the teeny change for now
      - Let’s use the auto-release to help us be more on top of things
      - Also change renovate to make sure we have a separate release even for patch versions (Kayla)[​](https://github.com/open-telemetry/opentelemetry-ruby/pull/2185​)
    - [https://github.com/open-telemetry/opentelemetry-ruby/pull/2195](https://github.com/open-telemetry/opentelemetry-ruby/pull/2195)
      - Before merging this one, Kayla will look into how difficult it is to push an empty/same 1.41.1 release
- Contrib ([Issues](https://github.com/open-telemetry/opentelemetry-ruby-contrib/issues) / [PRs](https://github.com/open-telemetry/opentelemetry-ruby-contrib/pulls))
  - [https://github.com/open-telemetry/opentelemetry-ruby-contrib/pull/2410](https://github.com/open-telemetry/opentelemetry-ruby-contrib/pull/2410)
    - Trilogy PR [#1290](https://github.com/open-telemetry/opentelemetry-ruby-contrib/pull/1290)
    - PTAL this week
  - PTAL: [https://github.com/open-telemetry/opentelemetry-ruby-contrib/pull/2407](https://github.com/open-telemetry/opentelemetry-ruby-contrib/pull/2407)
- Auto Instrumentation ([Issues](https://github.com/open-telemetry/opentelemetry-ruby-instrumentation/issues) / [PRs](https://github.com/open-telemetry/opentelemetry-ruby-instrumentation/pulls))
- Burning questions?
- ✨ Happy Reports ✨

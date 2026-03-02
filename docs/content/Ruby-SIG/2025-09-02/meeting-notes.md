## Meeting Notes

### Attendees
- Kayla Reopelle
- Hannah Ramadan
- Wendy Smoak
- Xuan Cao
- Arjun Rajappa
- Robb Kidd

### Agenda
- [Spec SIG](https://docs.google.com/document/d/1pdvPeKjA8v8w_fGKAN68JjWBmVJtPCpqdi9IZrd6eEo/preview) Update (max 15 min)
- Core ([Issues](https://github.com/open-telemetry/opentelemetry-ruby/issues) / [PRs](https://github.com/open-telemetry/opentelemetry-ruby/pulls))
  - ​​[Xuan] [https://github.com/open-telemetry/opentelemetry-ruby/pull/1891](https://github.com/open-telemetry/opentelemetry-ruby/pull/1891)
    - merged
  - [Xuan] [https://github.com/open-telemetry/opentelemetry-ruby/pull/1894](https://github.com/open-telemetry/opentelemetry-ruby/pull/1894) + [https://github.com/open-telemetry/opentelemetry-ruby/pull/1912](https://github.com/open-telemetry/opentelemetry-ruby/pull/1912)
    - Please review
  - [Robb] [semconv](https://github.com/open-telemetry/opentelemetry-ruby/pull/1651) - It’s happening!!!(?)
    - Some cleanup happening in PRs to Robb’s fork.
    - May get to some README work this afternoon, if not, merge the big one
  - Release the logs SDK separate from the API, wait til Thursday to merge the major version bump
- Contrib ([Issues](https://github.com/open-telemetry/opentelemetry-ruby-contrib/issues) / [PRs](https://github.com/open-telemetry/opentelemetry-ruby-contrib/pulls))
  - Puma PR
    - Use Try api?
      - Robb will look into it/comment
    - Still not sure why shutdown isn’t in the API
      - Wendy looking into history of shutdown being added to SDK spec
  - Six months until we remove OTEL_SEMCONV_STABILITY_OPT_IN from HTTP instrumentation! (target: February 26, 2026)
- Burning questions?
  - Have we implemented schema_url yet?
    - If/when we do, instrumentation authors could define that in their scope
    - Depend on the semconv gem only in tests (so it’s not a dev dependency), so it still validates the attribute names
    - Maintain their own constant strings within the instrumentation that point to the version
    - [https://opentelemetry.io/docs/specs/otel/schemas/](https://opentelemetry.io/docs/specs/otel/schemas/)
    - Otel collector has a processor in it that would transform upwards if the telemetry coming in is annotated with a particular schema level (may be in beta still?)
    - Kind of related to racecar messaging conventions update PR: [https://github.com/open-telemetry/opentelemetry-ruby-contrib/pull/1613](https://github.com/open-telemetry/opentelemetry-ruby-contrib/pull/1613)
- ✨ Happy Reports ✨

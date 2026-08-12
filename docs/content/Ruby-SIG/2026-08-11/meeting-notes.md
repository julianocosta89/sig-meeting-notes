## Meeting Notes

### Attendees
- Matt Wear
- Xuan Cao

### Agenda
- [Spec SIG](https://docs.google.com/document/d/1pdvPeKjA8v8w_fGKAN68JjWBmVJtPCpqdi9IZrd6eEo/preview) Update (max 15 min)
- Core ([Issues](https://github.com/open-telemetry/opentelemetry-ruby/issues) / [PRs](https://github.com/open-telemetry/opentelemetry-ruby/pulls))
  - Packaging blocked on declarative config support and opentelemetry-ruby-instrumentation release
- Contrib ([Issues](https://github.com/open-telemetry/opentelemetry-ruby-contrib/issues) / [PRs](https://github.com/open-telemetry/opentelemetry-ruby-contrib/pulls))
  - [James] What versions should we be testing in Appraisals? Currently gems follow different approaches and they are not being maintained. Options
    - Min supported + latest + additional added manually
    - Every min & major supported
    - Min of each major supported + Max of each major supported ie 2.2.0, 2.7.0, 3.0.0 & 3.4.0
    - We’ll discuss this next week when there are more attendees
      - Q: Is the reason for this question to align on a consistent approach, or something else?
      - A: Consistent approach which renovate can also follow. Renovate is now set to the first to mirror usage of using unpinned gems in a latest appraisal but can be changed
  - PTAL: [https://github.com/open-telemetry/opentelemetry-ruby-contrib/pull/2475](https://github.com/open-telemetry/opentelemetry-ruby-contrib/pull/2475)
  - Semantic conventions conformance
    - [https://github.com/open-telemetry/semantic-conventions-conformance](https://github.com/open-telemetry/semantic-conventions-conformance)
    - [https://trask.github.io/semantic-conventions-conformance-prototype/](https://trask.github.io/semantic-conventions-conformance-prototype/)
- Auto Instrumentation ([Issues](https://github.com/open-telemetry/opentelemetry-ruby-instrumentation/issues) / [PRs](https://github.com/open-telemetry/opentelemetry-ruby-instrumentation/pulls))
  - PTAL: [https://github.com/open-telemetry/opentelemetry-ruby-instrumentation/pull/39](https://github.com/open-telemetry/opentelemetry-ruby-instrumentation/pull/39)
- Burning questions?
- ✨ Happy Reports ✨

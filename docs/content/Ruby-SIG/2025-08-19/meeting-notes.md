## Meeting Notes

### Attendees
- Eric Mustin
- Kayla Reopelle
- Arjun Rajappa
- Wendy Smoak
- Xuan Cao
- Hannah Ramadan

### Agenda
- [Spec SIG](https://docs.google.com/document/d/1pdvPeKjA8v8w_fGKAN68JjWBmVJtPCpqdi9IZrd6eEo/preview) Update (max 15 min)
  - [kayla] [https://github.com/open-telemetry/opentelemetry-ruby/issues/1896](https://github.com/open-telemetry/opentelemetry-ruby/issues/1896)
    - Brought this up in the spec SIG
    - Erlang has something like this
    - The remove implementation got lost, still open to it
      - [https://github.com/open-telemetry/opentelemetry-specification/issues/2232](https://github.com/open-telemetry/opentelemetry-specification/issues/2232)
    - Suggestion for next step was the DevEx SIG (Wed @ 11PT)
      - I’ll need to wait until next week to join
- Core ([Issues](https://github.com/open-telemetry/opentelemetry-ruby/issues) / [PRs](https://github.com/open-telemetry/opentelemetry-ruby/pulls))
  - [kayla] Fix log env var for spec compliance:​​ [https://github.com/open-telemetry/opentelemetry-ruby/pull/1895](https://github.com/open-telemetry/opentelemetry-ruby/pull/1895)
  - [kayla] Update to spec-compliance-matrix: [https://github.com/open-telemetry/opentelemetry-specification/pull/4628](https://github.com/open-telemetry/opentelemetry-specification/pull/4628)
- Contrib ([Issues](https://github.com/open-telemetry/opentelemetry-ruby-contrib/issues) / [PRs](https://github.com/open-telemetry/opentelemetry-ruby-contrib/pulls))
  - [kayla] CI release workflows on core and contrib are slightly broken. The workaround is to manually add the `release: pending` label. This PR with new app-specific tokens should fix the problem: [https://github.com/open-telemetry/opentelemetry-ruby-contrib/pull/1639](https://github.com/open-telemetry/opentelemetry-ruby-contrib/pull/1639)
    - I’ll request a similar token for core if this solves the problem in contrib
  - [kayla] A few small PRs:
    - [https://github.com/open-telemetry/opentelemetry-ruby-contrib/pull/1632](https://github.com/open-telemetry/opentelemetry-ruby-contrib/pull/1632)
    - [https://github.com/open-telemetry/opentelemetry-ruby-contrib/pull/1639](https://github.com/open-telemetry/opentelemetry-ruby-contrib/pull/1639)
    - [https://github.com/open-telemetry/opentelemetry-ruby-contrib/pull/1641](https://github.com/open-telemetry/opentelemetry-ruby-contrib/pull/1641)
  - [arjun] FOSSA Scans PR: [https://github.com/open-telemetry/opentelemetry-ruby-contrib/pull/1640](https://github.com/open-telemetry/opentelemetry-ruby-contrib/pull/1640)
  - [kayla] Semconv for messaging: [https://github.com/open-telemetry/opentelemetry-ruby-contrib/pull/1613](https://github.com/open-telemetry/opentelemetry-ruby-contrib/pull/1613)
    - Eric will take a look
- Burning questions?
- ✨ Happy Reports ✨
  - [kayla] Instrumentation all is released with all the new semconv opt in variables! (Only Rack and Net::HTTP remain for HTTP conventions)
  - [kayla] Asynchronous metrics are live!

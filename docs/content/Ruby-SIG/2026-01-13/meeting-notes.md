## Meeting Notes

### Attendees
- Daniel Azuma
- Kayla Reopelle
- Hannah Ramadan
- Xuan Cao
- Ariel Valentin

### Agenda
- [Spec SIG](https://docs.google.com/document/d/1pdvPeKjA8v8w_fGKAN68JjWBmVJtPCpqdi9IZrd6eEo/preview) Update (max 15 min)
- Core ([Issues](https://github.com/open-telemetry/opentelemetry-ruby/issues) / [PRs](https://github.com/open-telemetry/opentelemetry-ruby/pulls))
  - ​​[https://github.com/open-telemetry/opentelemetry-ruby/pull/2023](https://github.com/open-telemetry/opentelemetry-ruby/pull/2023)
    - We’ll comment on the PR about what new cops to adopt
  - Schema URL PR - take another look, try to get that integrated before we remove the HTTP client semconv env var switches
- Contrib ([Issues](https://github.com/open-telemetry/opentelemetry-ruby-contrib/issues) / [PRs](https://github.com/open-telemetry/opentelemetry-ruby-contrib/pulls))
- Burning questions?
  - Going to stop running CI on forks
    - PR merged in core
    - Still needs review in contrib
  - Ariel getting test suite running on Ruby 4 and dropping support for 3.2
  - Releases
    - Release system we’re currently using was written by Daniel a few years ago
    - PRs in both repos to update the system to the new version of the release system
    - Should fix some of our current issues and make new improvements easier
    - Moving to release please?
      - Written by Daniel’s team when he was at Google when it was more community friendly
      - Google + his team has evolved considerably since then
      - Current leadership doesn’t have open source as a priority
      - A lot of the tooling that was open source initially is in the process of being moved back internally or minimal support for external users
      - Original writer left Google a few years ago
      - Expect current maintainer to retire soon
      - Skeptical of the support we could receive for that product
      - Best case scenario would be for someone to fork it and release it separately
    - Looking at a system that’s dependent on Daniel to maintain without a lot of community use or a system that has a lot of community use, but the current maintenance of it is uncertain
    - Available to make changes to the release system if there are things bothering them, features they want; but also willing to support us moving to release please if that’s what people would prefer
- ✨ Happy Reports ✨

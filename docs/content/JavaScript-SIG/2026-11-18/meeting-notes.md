## Meeting Notes

### Attendees
- Marc Pichler (Dynatrace)
- Trent Mick (Elastic)
- Jamie Danielson (Honeycomb)
- Jackson Weber (Microsoft)
- David Luna (Elastic)

### Agenda
- Feel free to add your topics below ↙️ 🙂
- [marc] Security Advisories:
  - [https://github.com/open-telemetry/opentelemetry-js/security/advisories/GHSA-qmwq-c476-x7q2](https://github.com/open-telemetry/opentelemetry-js/security/advisories/GHSA-qmwq-c476-x7q2)
  - [https://github.com/open-telemetry/opentelemetry-js-contrib/security/advisories/GHSA-hgpx-52j8-8gq2](https://github.com/open-telemetry/opentelemetry-js-contrib/security/advisories/GHSA-hgpx-52j8-8gq2)
- [marc] new renovate config in core gets rid of dashboard approval
  - Please let me know if you notice renovate grouping being incorrect/not easily mergable - I’ll update the config accordingly to make these PRs lower-friction.
- [marc] [https://github.com/open-telemetry/opentelemetry-js/pull/7302](https://github.com/open-telemetry/opentelemetry-js/pull/7302)
  - Trades off memory for faster OTLP serialization.
  - Any objections to doing this?
- [marc] some concerns around config types and stability [https://github.com/open-telemetry/opentelemetry-js/pull/7351#issuecomment-6977814377](https://github.com/open-telemetry/opentelemetry-js/pull/7351#issuecomment-6977814377)
  - There are a few cases (see comment) that may be breaking to users in the future because they’re explicitly mentioned as “non-breaking” in the config spec - we may want to address these early, before lots of packages start depending on these types
- [marc] should we go ahead with [https://github.com/open-telemetry/opentelemetry-js/pull/7014](https://github.com/open-telemetry/opentelemetry-js/pull/7014) now that 3.0 is out? :)
- [marc] (if there’s some time left) componentProviderRegistries [https://github.com/open-telemetry/opentelemetry-js/pull/7352](https://github.com/open-telemetry/opentelemetry-js/pull/7352)
- [trent] where should we share a match-wildcard-patterns: [https://github.com/open-telemetry/opentelemetry-js/pull/7106](https://github.com/open-telemetry/opentelemetry-js/pull/7106)
- [Untriaged bugs](https://github.com/open-telemetry/opentelemetry-js/issues?q=is%3Aissue+is%3Aopen+label%3Atriage+label%3Abug+-label%3Apriority%3Ap1++-label%3Apriority%3Ap2++-label%3Apriority%3Ap3++-label%3Apriority%3Ap4+)
- [Untriaged contrib bugs](https://github.com/open-telemetry/opentelemetry-js-contrib/issues?q=is%3Aissue+is%3Aopen+label%3Atriage%2Cbug+-label%3Apriority%3Ap1++-label%3Apriority%3Ap2++-label%3Apriority%3Ap3++-label%3Apriority%3Ap4)
- [Old Contrib PR Triage](https://github.com/open-telemetry/opentelemetry-js-contrib/pulls?q=is%3Apr+is%3Aopen+sort%3Acreated-asc)
- [Old Core PR Triage](https://github.com/open-telemetry/opentelemetry-js/pulls?q=is%3Apr+is%3Aopen+sort%3Acreated-asc)

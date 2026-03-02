## Meeting Notes

### Attendees
- Marc Pichler (Dynatrace)
- Andrei Borza (Sentry)
- Hector Hernandez (Microsoft)
- Marylia Gutierrez (Grafana Labs)
- Trent Mick (Elastic)
- Jackson Weber (Microsoft)

### Agenda
- [marc] huge thanks to everyone who has been reviewing and merging PRs recently ❤️
  - you’ve been crushing it, and thanks to your efforts we’ve been able to get down to one page of PRs (🤯) per repo intermittently for what feels like the first time in the last few years :)
- [andrei]: Any plans to graduate the experimental packages to a proper major version? It's difficult for library maintainers that rely on OTel to not be able to rely on proper semver and now that some contrib instrumentations are not part of the repo anymore (e.g. fastify, prisma) it's even easier to end up with multiple versions of `@opentelemetry/instrumentation` which often conflicts and leads to wrong data or broken instrumentations ([prisma is still on 0.203.0](https://github.com/prisma/prisma/blob/9b1a91b044baf878e257d00f24eeb2e30e407d69/packages/instrumentation/package.json#L35)). Do you have any recommendations for library/instrumentation maintainers?
- [marc] ongoing publishing issue in contrib. GitHub releases created, but nothing published to npm yet.
- [Untriaged bugs](https://github.com/open-telemetry/opentelemetry-js/issues?q=is%3Aissue+is%3Aopen+label%3Atriage+label%3Abug+-label%3Apriority%3Ap1++-label%3Apriority%3Ap2++-label%3Apriority%3Ap3++-label%3Apriority%3Ap4+)
- [Untriaged contrib bugs](https://github.com/open-telemetry/opentelemetry-js-contrib/issues?q=is%3Aissue+is%3Aopen+label%3Atriage%2Cbug+-label%3Apriority%3Ap1++-label%3Apriority%3Ap2++-label%3Apriority%3Ap3++-label%3Apriority%3Ap4)
- [Old Contrib PR Triage](https://github.com/open-telemetry/opentelemetry-js-contrib/pulls?q=is%3Apr+is%3Aopen+sort%3Acreated-asc)
- [Old Core PR Triage](https://github.com/open-telemetry/opentelemetry-js/pulls?q=is%3Apr+is%3Aopen+sort%3Acreated-asc)

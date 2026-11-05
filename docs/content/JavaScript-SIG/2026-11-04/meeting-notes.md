## Meeting Notes

### Attendees
- Marc Pichler (Dynatrace)
- Adi
- Trent Mick (Elastic)
- Raphaël Thériault (Solarwinds)
- Matt Wear (Dash0)
- Jackson Weber (Microsoft)
- Jamie Danielson (Honeycomb)
- David Luna (Elastic)

### Agenda
- [Adi] PTAL [https://github.com/open-telemetry/opentelemetry-js/pull/7210](https://github.com/open-telemetry/opentelemetry-js/pull/7210)  sdk-logs: wait for overlapping flushes (open since Oct 15, review comments answered)
- [Adi] PTAL [https://github.com/open-telemetry/opentelemetry-js-contrib/pull/3832](https://github.com/open-telemetry/opentelemetry-js-contrib/pull/3832)   web-exception deprecation docs: the three requested changes are in, needs a re-review
- [Adi] related to the next item: [https://github.com/open-telemetry/opentelemetry-js/pull/7253](https://github.com/open-telemetry/opentelemetry-js/pull/7253)  migration note that API 1.10.0 needs SDK 3.x
  - [marc] merged - thank you! :)
- [marc]: we will have to raise the minimum supported API version on all instrumentations to ^1.10.0 - the reason being that we use `logs` in the instrumentation base. For users, most contrib packages become unusable unless they upgrade to SDK 3.0 + API 1.10.0. This is effectively true today as not using that API version breaks on runtime.
  - Ref (PR): [https://github.com/open-telemetry/opentelemetry-js/pull/7259](https://github.com/open-telemetry/opentelemetry-js/pull/7259)
  - Ref (issue): [https://github.com/open-telemetry/opentelemetry-js/issues/7258](https://github.com/open-telemetry/opentelemetry-js/issues/7258)
- [marc]: focus topics discussion
  - Many of the topics need refinement and I think that’s be best done in public - I’m planning to move focus topic definition to the `doc/` directory so that we can use PRs for
    - Discussing/changing topics in the backlog
    - Promotion of backlog topics to active topics
  - That also allows folks that usually don’t attend the SIG meeting to voice their opinions.
  - Current state: I’m migrating the topics that I’ve already defined in the past to actual files and updating them
- Notes re: exporters
  - The exporters currently act on environment variables even if a config file is provided, so it needs to be changed. In the process of changing them, we may be able to consolidate into 1-2 packages.
  - gRPC might need to be separate, but worth looking at the microtel PR that adds gRPC support without adding gRPC dependencies
- [Untriaged bugs](https://github.com/open-telemetry/opentelemetry-js/issues?q=is%3Aissue+is%3Aopen+label%3Atriage+label%3Abug+-label%3Apriority%3Ap1++-label%3Apriority%3Ap2++-label%3Apriority%3Ap3++-label%3Apriority%3Ap4+)
- [Untriaged contrib bugs](https://github.com/open-telemetry/opentelemetry-js-contrib/issues?q=is%3Aissue+is%3Aopen+label%3Atriage%2Cbug+-label%3Apriority%3Ap1++-label%3Apriority%3Ap2++-label%3Apriority%3Ap3++-label%3Apriority%3Ap4)
- [SDK 3.0 Milestone Triage and Refinement](https://github.com/open-telemetry/opentelemetry-js/milestone/20)
- [Old Contrib PR Triage](https://github.com/open-telemetry/opentelemetry-js-contrib/pulls?q=is%3Apr+is%3Aopen+sort%3Acreated-asc)
- [Old Core PR Triage](https://github.com/open-telemetry/opentelemetry-js/pulls?q=is%3Apr+is%3Aopen+sort%3Acreated-asc)

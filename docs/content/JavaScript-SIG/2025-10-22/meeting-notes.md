## Meeting Notes

### Attendees
- Marylia Gutierrez (Grafana Labs)
- Hector Hernandez (Microsoft)
- Andrei Borza (Sentry.io)
- David Luna (Elastic)
- Jamie Danielson (Honeycomb)
- Raphaël Thériault (SolarWinds)
- Jackson Weber (Microsoft)

### Agenda
- [marylia] Feedback from survey:
  - Contrib repo is making people confused about approvals/merge. Not clear who should be pinged to get a review, and how to get your PR merged after that
- [marylia] we need more issues tagged as “good first issue”
- [marylia] otel graduation, things that we can do to help:
  - Add documentation that only exists in github to [otel.io](http://otel.io)
  - Check all packages and see what we can change to stable, flag what is “stable” but not following the latest semantic convention (so we can update it)
  - [Recommendations for OpenTelemetry](https://docs.google.com/document/d/1SQMdfYpCiBfpxtWDwASXVIl-PIzD9X4vdDPXYUphAF0/edit?tab=t.0#heading=h.fn06amgn4poq)
  - Wait for guidance on how to explain stable vs unstable (possible separation of semantic conventions vs instrumentation packages stability)
  - Performance improvements
- [Untriaged bugs](https://github.com/open-telemetry/opentelemetry-js/issues?q=is%3Aissue+is%3Aopen+label%3Atriage+label%3Abug+-label%3Apriority%3Ap1++-label%3Apriority%3Ap2++-label%3Apriority%3Ap3++-label%3Apriority%3Ap4+)
- [Untriaged contrib bugs](https://github.com/open-telemetry/opentelemetry-js-contrib/issues?q=is%3Aissue+is%3Aopen+label%3Atriage%2Cbug+-label%3Apriority%3Ap1++-label%3Apriority%3Ap2++-label%3Apriority%3Ap3++-label%3Apriority%3Ap4)
- [Old Contrib PR Triage](https://github.com/open-telemetry/opentelemetry-js-contrib/pulls?q=is%3Apr+is%3Aopen+sort%3Acreated-asc)
- [Old Core PR Triage](https://github.com/open-telemetry/opentelemetry-js/pulls?q=is%3Apr+is%3Aopen+sort%3Acreated-asc)

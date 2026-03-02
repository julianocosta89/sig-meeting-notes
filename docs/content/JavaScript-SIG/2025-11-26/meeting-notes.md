## Meeting Notes

### Attendees
- Marc Pichler (Dynatrace)
- Andrei Borza (Sentry)
- Trent Mick (Elastic)
- Marylia Gutierrez (Grafana Labs)
- Jackson Weber (Microsoft)
- Hector Hernandez (Microsoft)

### Agenda
- **Feel free to add your topics below ↙️ 🙂**
- [marc] too many different things to do currently, so I’m looking for people to review the PRs to add new instrumentations:
  - langchain [https://github.com/open-telemetry/opentelemetry-js-contrib/pull/3132](https://github.com/open-telemetry/opentelemetry-js-contrib/pull/3132)
  - mcp [https://github.com/open-telemetry/opentelemetry-js-contrib/pull/3186](https://github.com/open-telemetry/opentelemetry-js-contrib/pull/3186)
- [marc] FYI: Browser SIG now has approver access to all web-targeted packages in both core and contrib
- [marylia] new function for SDK start. Decision on parameters [SDK Options - JS SDK](https://docs.google.com/document/d/1VVBvlfRNg5BWjfGnmBg0nUiABLoKTKhcGqQzonMC-kQ/edit?tab=t.0)
- [marylia] we have default resources, do we want to add anything custom on top of that or is one of the other? [https://github.com/open-telemetry/opentelemetry-js/pull/6152/files#diff-44b3cba79d8ee04c3efd823142cf926e5effe45f31c1199ff8eae607c3500885R93-R94](https://github.com/open-telemetry/opentelemetry-js/pull/6152/files#diff-44b3cba79d8ee04c3efd823142cf926e5effe45f31c1199ff8eae607c3500885R93-R94)
- [marylia] PRs for review [https://github.com/open-telemetry/opentelemetry-js/pull/6166](https://github.com/open-telemetry/opentelemetry-js/pull/6166) and [https://github.com/open-telemetry/opentelemetry-js/pull/6152](https://github.com/open-telemetry/opentelemetry-js/pull/6152)
- [marc] new startNodeSDK function - how should we deal with experimental packages? Especially in reference to [https://github.com/open-telemetry/opentelemetry.io/pull/8208](https://github.com/open-telemetry/opentelemetry.io/pull/8208)
- [Untriaged bugs](https://github.com/open-telemetry/opentelemetry-js/issues?q=is%3Aissue+is%3Aopen+label%3Atriage+label%3Abug+-label%3Apriority%3Ap1++-label%3Apriority%3Ap2++-label%3Apriority%3Ap3++-label%3Apriority%3Ap4+)
- [Untriaged contrib bugs](https://github.com/open-telemetry/opentelemetry-js-contrib/issues?q=is%3Aissue+is%3Aopen+label%3Atriage%2Cbug+-label%3Apriority%3Ap1++-label%3Apriority%3Ap2++-label%3Apriority%3Ap3++-label%3Apriority%3Ap4)
- [Old Contrib PR Triage](https://github.com/open-telemetry/opentelemetry-js-contrib/pulls?q=is%3Apr+is%3Aopen+sort%3Acreated-asc)
- [Old Core PR Triage](https://github.com/open-telemetry/opentelemetry-js/pulls?q=is%3Apr+is%3Aopen+sort%3Acreated-asc)

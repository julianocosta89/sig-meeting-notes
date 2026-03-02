## Meeting Notes

### Attendees
- Marc Pichler (Dynatrace)
- Trent Mick (Elastic)
- Andrei Borza (Sentry)
- Marylia Gutierrez (Grafana Labs)
- Raphaël Thériault (SolarWinds)
- Jackson Weber (Microsoft)
- Hector Hernandez (Microsoft)
- Darragh Sherwin (Globalization Partners)

### Agenda
- **Feel free to add your topics below ↙️ 🙂**
- [david] where to place the sdk-logs config?
  - [https://github.com/open-telemetry/opentelemetry-js/issues/6074](https://github.com/open-telemetry/opentelemetry-js/issues/6074)
  - [marc] 3 possible options (there may be more)
    - Place in NodeSDK, do not expose to end-users, they must migrate to NodeSDK if they want to keep using it
    - Place in sdk-logs, do expose a function to end-users
    - Place in sdk-node, use in NodeSDK by default but also expose the function to end-users, they may use it with sdk-logs without using NodeSDK directly.
    - **Decision:** option 1
- [david] more tunning to contrib CI
  - [https://github.com/open-telemetry/opentelemetry-js-contrib/pull/3318](https://github.com/open-telemetry/opentelemetry-js-contrib/pull/3318)
- [andrei] process.argv0 in @opentelemetry/resources still causing build warnings on vercel edge 😓
  - [https://github.com/open-telemetry/opentelemetry-js/pull/6257#pullrequestreview-3678061350](https://github.com/open-telemetry/opentelemetry-js/pull/6257#pullrequestreview-3678061350)
- [carlos][offline today] OTEL_RESOURCE_ATTRIBUTES update: [https://github.com/open-telemetry/opentelemetry-specification/issues/4847](https://github.com/open-telemetry/opentelemetry-specification/issues/4847)
  - Initial discussion towards 1) making it fail fast, instead of try to recover valid keys/values, 2) No unescaping, but allow characters outside baggage-octet valid. This would make the user history friendlier. Opinions?
  - Consider commenting on the issue itself.
- [Untriaged bugs](https://github.com/open-telemetry/opentelemetry-js/issues?q=is%3Aissue+is%3Aopen+label%3Atriage+label%3Abug+-label%3Apriority%3Ap1++-label%3Apriority%3Ap2++-label%3Apriority%3Ap3++-label%3Apriority%3Ap4+)
- [Untriaged contrib bugs](https://github.com/open-telemetry/opentelemetry-js-contrib/issues?q=is%3Aissue+is%3Aopen+label%3Atriage%2Cbug+-label%3Apriority%3Ap1++-label%3Apriority%3Ap2++-label%3Apriority%3Ap3++-label%3Apriority%3Ap4)
- [Old Contrib PR Triage](https://github.com/open-telemetry/opentelemetry-js-contrib/pulls?q=is%3Apr+is%3Aopen+sort%3Acreated-asc)
- [Old Core PR Triage](https://github.com/open-telemetry/opentelemetry-js/pulls?q=is%3Apr+is%3Aopen+sort%3Acreated-asc)

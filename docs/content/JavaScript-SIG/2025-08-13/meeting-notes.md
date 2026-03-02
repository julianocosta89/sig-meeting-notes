## Meeting Notes

### Attendees
- Marc Pichler (Dynatrace)
- Trent Mick (Elastic)
- [Daniel Dyla](mailto:dyladan@gmail.com)
- Andrei Borza (Sentry)
- Marylia Gutierrez (Grafana Labs)
- Jackson Weber (Microsoft)

### Agenda
- [marc] bringing up an old topic again - ditching export via `XMLHttpRequest` for `fetch` in the browser exporters
  - Q to browser SIG folks - is this still off the table?
  - Asking due to [https://github.com/open-telemetry/opentelemetry-js/pull/5807](https://github.com/open-telemetry/opentelemetry-js/pull/5807)
    - This PR would increase bundle size + complexity, removing `XMLHttpRequest` as an option in favor of `fetch` would keep bundle size roughly the same.
  - [https://caniuse.com/fetch](https://caniuse.com/fetch)
  - [https://caniuse.com/](https://caniuse.com/fetch)xhr2
- [marylia] [https://github.com/open-telemetry/community/pull/2911](https://github.com/open-telemetry/community/pull/2911) is looking for feedback
- [marylia] regarding [comment](https://github.com/open-telemetry/opentelemetry-js/pull/5809#discussion_r2257522243), should it be similar to MetricProvider with an interface on api package and class implementation sdk-metric package, or can both interface and class implementation be on the new config package?
- [Untriaged bugs](https://github.com/open-telemetry/opentelemetry-js/issues?q=is%3Aissue+is%3Aopen+label%3Atriage+label%3Abug+-label%3Apriority%3Ap1++-label%3Apriority%3Ap2++-label%3Apriority%3Ap3++-label%3Apriority%3Ap4+)
- [Untriaged contrib bugs](https://github.com/open-telemetry/opentelemetry-js-contrib/issues?q=is%3Aissue+is%3Aopen+label%3Atriage%2Cbug+-label%3Apriority%3Ap1++-label%3Apriority%3Ap2++-label%3Apriority%3Ap3++-label%3Apriority%3Ap4)
- [Old Contrib PR Triage](https://github.com/open-telemetry/opentelemetry-js-contrib/pulls?q=is%3Apr+is%3Aopen+sort%3Acreated-asc)

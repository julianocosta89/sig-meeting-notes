## Meeting Notes

### Attendees
- Trent Mick (Elastic)
- Hector Hernandez (Microsoft)
- Jamie Danielson (Honeycomb)
- Maxime David (AWS - Lambda Runtimes)
- Jan Peer Stöcklmair (Sentry)
- Abhinav Mathur ( Splunk / Appdynamics )
- Jackson Weber (Microsoft)
- Raphaël Thériault (SolarWinds)
- Marylia Gutierrez (Grafana Labs)

### Agenda
- **Feel free to add your topics below ↙️ 🙂**
- [feat(configuration): refactoring config loader to print warning message #6524](https://github.com/open-telemetry/opentelemetry-js/pull/6524)
  - Currently updates for env vars, need to consider file config. Mike is working on updating the way these are used, maybe there are merge conflicts / opinions to consider?
- [jamie] genai instrumentations - prefer to keep in contrib or separate repo?
  - There is discussion in LLM Semconv SIG about potentially adding a separate repo to allow for faster iteration on semantic conventions and instrumentations. Python is almost definitely doing it, but they have an easier way of adding third party instrumentations with their bootstrap agent. JS does not have this.
  - 🤷 No rush to do it, no real objection. TBD, maybe start with Python as planned and go from there. May help push the priority on current issues with registering instrumentations.
- [maxday] sync with the author of : [https://github.com/open-telemetry/opentelemetry-js-contrib/pull/2981](https://github.com/open-telemetry/opentelemetry-js-contrib/pull/2981)
- [Untriaged bugs](https://github.com/open-telemetry/opentelemetry-js/issues?q=is%3Aissue+is%3Aopen+label%3Atriage+label%3Abug+-label%3Apriority%3Ap1++-label%3Apriority%3Ap2++-label%3Apriority%3Ap3++-label%3Apriority%3Ap4+)
- [Untriaged contrib bugs](https://github.com/open-telemetry/opentelemetry-js-contrib/issues?q=is%3Aissue+is%3Aopen+label%3Atriage%2Cbug+-label%3Apriority%3Ap1++-label%3Apriority%3Ap2++-label%3Apriority%3Ap3++-label%3Apriority%3Ap4)
- [Old Contrib PR Triage](https://github.com/open-telemetry/opentelemetry-js-contrib/pulls?q=is%3Apr+is%3Aopen+sort%3Acreated-asc)
- [Old Core PR Triage](https://github.com/open-telemetry/opentelemetry-js/pulls?q=is%3Apr+is%3Aopen+sort%3Acreated-asc)

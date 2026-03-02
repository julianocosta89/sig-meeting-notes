## Meeting Notes

### Attendees
- Marc Pichler (Dynatrace)
- Marylia Gutierrez (Grafana Labs)
- Raphaël Thériault (SolarWinds)
- Trent Mick (Elastic)
- David Luna (Elastic)

### Agenda
- [marc] should we do Old PR triage based on which repo has more open PRs currently? We’ve been doing contrib triage first, but the core repo has now more open PRs
- [marylia] PR for review is big, but straight forward and I added a test for every single env variable to make sure I didn't make any mistakes [https://github.com/open-telemetry/opentelemetry-js/pull/5862](https://github.com/open-telemetry/opentelemetry-js/pull/5862)
  - [ ] Got good feedback from the declarative config working group
- [marc] looking for more people that are interested in moderating the SIG meeting - if you’re an approver and interested in doing so, feel free to reach out :)
- [marylia] pick [package with ISC](https://www.npmjs.com/package/yaml) license (recently published) VS [package with MIT](https://www.npmjs.com/package/js-yaml) license (last published 4 years ago)
  - [ ] [https://github.com/cncf/foundation/blob/main/policies-guidance/allowed-third-party-license-policy.md#approved-licenses-for-allowlist](https://github.com/cncf/foundation/blob/main/policies-guidance/allowed-third-party-license-policy.md#approved-licenses-for-allowlist)
  - [ ] ISC is good :)
- [Untriaged bugs](https://github.com/open-telemetry/opentelemetry-js/issues?q=is%3Aissue+is%3Aopen+label%3Atriage+label%3Abug+-label%3Apriority%3Ap1++-label%3Apriority%3Ap2++-label%3Apriority%3Ap3++-label%3Apriority%3Ap4+)
- [Untriaged contrib bugs](https://github.com/open-telemetry/opentelemetry-js-contrib/issues?q=is%3Aissue+is%3Aopen+label%3Atriage%2Cbug+-label%3Apriority%3Ap1++-label%3Apriority%3Ap2++-label%3Apriority%3Ap3++-label%3Apriority%3Ap4)
- [Old Contrib PR Triage](https://github.com/open-telemetry/opentelemetry-js-contrib/pulls?q=is%3Apr+is%3Aopen+sort%3Acreated-asc)
- [Old Core PR Triage](https://github.com/open-telemetry/opentelemetry-js/pulls?q=is%3Apr+is%3Aopen+sort%3Acreated-asc)

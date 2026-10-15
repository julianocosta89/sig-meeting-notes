## Meeting Notes

### Attendees
- David Luna (Elastic)
- Marc Pichler (Dynatrace)
- Trent Mick (Elastic)
- Jared Freeze (Palo Alto Networks)
- Jackson Weber (Microsoft)
- Hector Hernandez (Microsoft)

### Agenda
- **Feel free to add your topics below** ↙️ 🙂
- [david] GH `pull_request_target` policy for public repos
  - [Securely using pull_request_target - GitHub Docs](https://docs.github.com/en/actions/reference/security/securely-using-pull_request_target)
  - We use it in
    - Core: [survey](https://github.com/open-telemetry/opentelemetry-js/blob/main/.github/workflows/survey-on-merged-pr.yml) , [first time pr](https://github.com/open-telemetry/opentelemetry-js/blob/main/.github/workflows/first-time-pr.yml)
    - Contrib: [pr title](https://github.com/open-telemetry/opentelemetry-js-contrib/blob/main/.github/workflows/pr-title.yml), [first time pr](https://github.com/open-telemetry/opentelemetry-js-contrib/blob/main/.github/workflows/first-time-pr.yml), [survey](https://github.com/open-telemetry/opentelemetry-js-contrib/blob/main/.github/workflows/survey-on-merged-pr.yml), [label prs](https://github.com/open-telemetry/opentelemetry-js-contrib/blob/main/.github/workflows/label-prs.yml)
- [trent]
  - opentelemetry.io docs update for sdk-trace-star: [https://github.com/open-telemetry/opentelemetry.io/pull/12084](https://github.com/open-telemetry/opentelemetry.io/pull/12084)
  - TODO: contrib prep PR for 3.0 compat
  - TODO: another run through the migration doc
  - do a real release ... NOW or Monday next week?
- [Untriaged bugs](https://github.com/open-telemetry/opentelemetry-js/issues?q=is%3Aissue+is%3Aopen+label%3Atriage+label%3Abug+-label%3Apriority%3Ap1++-label%3Apriority%3Ap2++-label%3Apriority%3Ap3++-label%3Apriority%3Ap4+)
- [Untriaged contrib bugs](https://github.com/open-telemetry/opentelemetry-js-contrib/issues?q=is%3Aissue+is%3Aopen+label%3Atriage%2Cbug+-label%3Apriority%3Ap1++-label%3Apriority%3Ap2++-label%3Apriority%3Ap3++-label%3Apriority%3Ap4)
- [SDK 3.0 Milestone Triage and Refinement](https://github.com/open-telemetry/opentelemetry-js/milestone/20)
- [Old Contrib PR Triage](https://github.com/open-telemetry/opentelemetry-js-contrib/pulls?q=is%3Apr+is%3Aopen+sort%3Acreated-asc)
- [Old Core PR Triage](https://github.com/open-telemetry/opentelemetry-js/pulls?q=is%3Apr+is%3Aopen+sort%3Acreated-asc)

## Meeting Notes

### Attendees
- Trent Mick (Elastic)
- David Luna (Elastic)
- Marc Pichler (Dynatrace)
- Marylia Gutierrez (Grafana Labs)
- Jamie Danielson (Honeycomb)
- Ian Ferrier (Pax8)
- Jackson Weber (Microsoft)
- Raphaël Thériault (SolarWinds)

### Agenda
- [david] ping to review
  - user-agent [https://github.com/open-telemetry/opentelemetry-js/pull/5928](https://github.com/open-telemetry/opentelemetry-js/pull/5928)
- [david] Contrib CI testing after the workflow changes (nodejs)
  - it compiles all node packages always because of auto-instrumentations
    - instr-x affects auto-instrumentations and this depends on all instrumentations
    - we are spending same time as before
  - tests only for the affected packages
    - example: [https://github.com/open-telemetry/opentelemetry-js-contrib/actions/runs/18164557906/job/51703708028?pr=3126](https://github.com/open-telemetry/opentelemetry-js-contrib/actions/runs/18164557906/job/51703708028?pr=3126)
    - we are spending less time than before 🎉
  - dependency updates have become more expensive
    - because they change package-lock.json
    - It’s correct but PRs take about 1h to get a green build
    - example: [https://github.com/open-telemetry/opentelemetry-js-contrib/actions/runs/17800908077/job/50600808607](https://github.com/open-telemetry/opentelemetry-js-contrib/actions/runs/17800908077/job/50600808607)
    - we are spending more time than before 😿
      - prev workflow was running TAV based on labels
  - Possible improvements
    - Cache the compilation of the last commit in main
    - go back to using labels for TAV tests
      - testing auto-instrumentations also (for correctness)
    - [marc] do not TAV if only `package-lock.json` is affected and trigger it via label
  - David to create an issue to discuss these options and decide how to move forward
- [ian] req for debug suggestions for export (?) requests getting stuck in Network browser dev tools tab.
  - May be version mismatch or an older honeycomb web sdk
  - Try updating to a new version… if it’s still an issue, open an issue with the details and we’ll dig in more
  - Also see if similar to this [old issue](https://github.com/open-telemetry/opentelemetry-js/issues/3489)
- [marylia] example was changed a lot by this PR [https://github.com/open-telemetry/opentelemetry.io/pull/7937](https://github.com/open-telemetry/opentelemetry.io/pull/7937) , not sure if that is the right approach
  - Let’s compare to the other language docs - there is intended to be consistency across the docs
- [marylia] [https://github.com/open-telemetry/opentelemetry-js/issues/5916#issuecomment-3352138925](https://github.com/open-telemetry/opentelemetry-js/issues/5916#issuecomment-3352138925)
- [Untriaged bugs](https://github.com/open-telemetry/opentelemetry-js/issues?q=is%3Aissue+is%3Aopen+label%3Atriage+label%3Abug+-label%3Apriority%3Ap1++-label%3Apriority%3Ap2++-label%3Apriority%3Ap3++-label%3Apriority%3Ap4+)
- [Untriaged contrib bugs](https://github.com/open-telemetry/opentelemetry-js-contrib/issues?q=is%3Aissue+is%3Aopen+label%3Atriage%2Cbug+-label%3Apriority%3Ap1++-label%3Apriority%3Ap2++-label%3Apriority%3Ap3++-label%3Apriority%3Ap4)
- [Old Contrib PR Triage](https://github.com/open-telemetry/opentelemetry-js-contrib/pulls?q=is%3Apr+is%3Aopen+sort%3Acreated-asc)
- [Old Core PR Triage](https://github.com/open-telemetry/opentelemetry-js/pulls?q=is%3Apr+is%3Aopen+sort%3Acreated-asc)

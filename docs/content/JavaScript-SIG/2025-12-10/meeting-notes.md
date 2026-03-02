## Meeting Notes

### Attendees
- Jamie Danielson (Honeycomb)
- Jackson Weber (Microsoft)
- David Luna (Elastic)
- Marc Pichler (Dynatrace)
- Trent Mick (Elastic)
- Marylia Gutierrez (Grafana Labs)
- Hector Hernandez (Microsoft)
- Raphaël Thériault (SolarWinds)

### Agenda
- **Feel free to add your topics below ↙️ 🙂**
- [david] Proposal of a new API to create instrumentations
  - Decouples from `InstrumentationBase` and `InstrumentationAbstract` classes
  - Fixes [#1989](https://github.com/open-telemetry/opentelemetry-js/issues/1989) (very old issue InstrumentationBase calls init on partly initialized Instrumentations)
  - Will affect web instrumentations also (going to share in browser SIG)
  - [https://github.com/open-telemetry/opentelemetry-js/pull/6163](https://github.com/open-telemetry/opentelemetry-js/pull/6163)
  - Reviews needed
- [marylia] Do we have any guidelines for skipping parts of instrumentation? Context: [https://github.com/open-telemetry/opentelemetry-js-contrib/pull/3280](https://github.com/open-telemetry/opentelemetry-js-contrib/pull/3280)
  - There is some prior art for this: see graphql which has options for `ignoreTrivialResolveSpans` and `ignoreResolveSpans`
  - Nothing in spec for it
  - “Skip” is used mostly for internal methods, “ignore” is used in more of the instrumentations for this sort of thing.
  - Let’s do it!
- [marylia] reminder for lightning talk cpf ends this week for kubecon eu: [https://sessionize.com/project-benefits-kubecon-eu-2026/](https://sessionize.com/project-benefits-kubecon-eu-2026/)
- [jamie] SIG focus topics/priorities
  - [https://github.com/open-telemetry/opentelemetry-js/issues/5149](https://github.com/open-telemetry/opentelemetry-js/issues/5149)
  - Semconv updates for HTTP/DB top priority - let’s get them done
  - Logs Stabilization next top focus, required for config
  - Jamie will update this topic
- [trent] Dev opinions on “TODO: …” comments in files: E.g. [https://github.com/open-telemetry/opentelemetry-js-contrib/pull/3273/files/8410e0eef8db29370693e259df166685693ab920#diff-ab6cb1c5f67e17675538802a97a1f14f03521836f696f57a046f33cf6d863ca8](https://github.com/open-telemetry/opentelemetry-js-contrib/pull/3273/files/8410e0eef8db29370693e259df166685693ab920#diff-ab6cb1c5f67e17675538802a97a1f14f03521836f696f57a046f33cf6d863ca8)
  - Create issue for todos, keep todos in there with url for issue e.g. “TODO(1234): add blabla”
- [React-native instrumentation](https://github.com/open-telemetry/opentelemetry-js-contrib/pull/2359) is still stalled, with no clear idea on how to move forward with it
  - There was a request for a separate WG last year but it didn’t materialize because of lack of staffing.
  - There is a separate browser SIG that has started up because of similar needs on the web side… but there is more staffing there. Perhaps we can learn from that group how best to do testing, etc so there is not significant drift, and then we can use what we learn there and apply to a react-native project.
  - Adding the instrumentation to the repo adds a lot of dependencies and there is a lot of potential maintenance required. Right now the priority is to get the web side set up and then revisit react-native.
  - Jamie add notes to issue in core repo and link to it in the PR.
- [Untriaged bugs](https://github.com/open-telemetry/opentelemetry-js/issues?q=is%3Aissue+is%3Aopen+label%3Atriage+label%3Abug+-label%3Apriority%3Ap1++-label%3Apriority%3Ap2++-label%3Apriority%3Ap3++-label%3Apriority%3Ap4+)
- [Untriaged contrib bugs](https://github.com/open-telemetry/opentelemetry-js-contrib/issues?q=is%3Aissue+is%3Aopen+label%3Atriage%2Cbug+-label%3Apriority%3Ap1++-label%3Apriority%3Ap2++-label%3Apriority%3Ap3++-label%3Apriority%3Ap4)
- [Old Contrib PR Triage](https://github.com/open-telemetry/opentelemetry-js-contrib/pulls?q=is%3Apr+is%3Aopen+sort%3Acreated-asc)
- [Old Core PR Triage](https://github.com/open-telemetry/opentelemetry-js/pulls?q=is%3Apr+is%3Aopen+sort%3Acreated-asc)

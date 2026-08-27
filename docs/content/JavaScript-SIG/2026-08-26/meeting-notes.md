## Meeting Notes

### Attendees
- Trent Mick (Elastic)
- [Daniel Dyla](mailto:dyladan@gmail.com)(Dynatrace)
- Marylia (Grafana)
- David Luna (Elastic)
- Marc Pichler (Dynatrace)
- Jackson Weber (Microsoft)
- Pranav Sharma (Google)
- Surya Teja
- Matt Wear (Dash0)
- Hector Hernandez (Microsoft)

### Agenda
- **Feel free to add your topics below ↙️ 🙂**
- [marc] Welcome Marylia to JS SIG Maintainers!
  - [https://github.com/open-telemetry/opentelemetry-js/pull/7024](https://github.com/open-telemetry/opentelemetry-js/pull/7024)
- [marylia] discussion on the approach of [https://github.com/open-telemetry/opentelemetry-js/pull/6999](https://github.com/open-telemetry/opentelemetry-js/pull/6999)
- [JacksonWeber] Need maintainer review on this OpenInference migration skill: [docs: add OpenInference migration skill](https://github.com/open-telemetry/opentelemetry-js-contrib/pull/3671)
- [trent] Possibly discuss ConfigProvider PR proposed changes: [https://github.com/open-telemetry/opentelemetry-js/pull/6868#issuecomment-5418162758](https://github.com/open-telemetry/opentelemetry-js/pull/6868#issuecomment-5418162758) (most likely wait until/if mwear is able to attend)
- [trent] Opinions on API for [https://github.com/open-telemetry/opentelemetry-specification/pull/4900#discussion_r3798892484](https://github.com/open-telemetry/opentelemetry-specification/pull/4900#discussion_r3798892484)?  Would others be fine with a design where a `configProvider.registerChangeListener(...)` must return a function or object with a `.close()` or similar to *unregister*? This is as opposed to the spec language allowing a `configProvider.unregisterChangeListener(...)` – similar to `removeEventListener(...)`.
- [Pranav] GenAI Utils Library: Review
  - [https://github.com/open-telemetry/opentelemetry-js-contrib/pull/3677](https://github.com/open-telemetry/opentelemetry-js-contrib/pull/3677)
- [Surya] Anthropic Instrumentation Review
- [Untriaged bugs](https://github.com/open-telemetry/opentelemetry-js/issues?q=is%3Aissue+is%3Aopen+label%3Atriage+label%3Abug+-label%3Apriority%3Ap1++-label%3Apriority%3Ap2++-label%3Apriority%3Ap3++-label%3Apriority%3Ap4+)
- [Untriaged contrib bugs](https://github.com/open-telemetry/opentelemetry-js-contrib/issues?q=is%3Aissue+is%3Aopen+label%3Atriage%2Cbug+-label%3Apriority%3Ap1++-label%3Apriority%3Ap2++-label%3Apriority%3Ap3++-label%3Apriority%3Ap4)
- [SDK 3.0 Milestone Triage and Refinement](https://github.com/open-telemetry/opentelemetry-js/milestone/20)
- [Old Contrib PR Triage](https://github.com/open-telemetry/opentelemetry-js-contrib/pulls?q=is%3Apr+is%3Aopen+sort%3Acreated-asc)
- [Old Core PR Triage](https://github.com/open-telemetry/opentelemetry-js/pulls?q=is%3Apr+is%3Aopen+sort%3Acreated-asc)

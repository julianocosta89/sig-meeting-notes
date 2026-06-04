## Meeting Notes

### Attendees
- Marc Pichler (Dynatrace)
- Marylia Gutierrez (Grafana)
- David Luna (Elastic)
- Trent Mick (Elastic)
- Pranav Sharma (Google)
- Jackson Weber (Microsoft)

### Agenda
- [trent] sdk-trace package: [https://github.com/open-telemetry/opentelemetry-js/pull/6775](https://github.com/open-telemetry/opentelemetry-js/pull/6775)
  - Adds a sdk-trace package that eventually can replace all sdk-trace-*.
  - Do we need to export functions that do the same envvar reading as sdk-trace-base? If so, where would they live? If in sdk-node, then the user takes the same large dep. Perhaps that is fine.
  - After this I can get sdk-node using sdk-trace. I'm currently blocked on [https://github.com/open-telemetry/opentelemetry-js/pull/6765](https://github.com/open-telemetry/opentelemetry-js/pull/6765) for this.
- [trent] configuration: [https://github.com/open-telemetry/opentelemetry-js/pull/6757](https://github.com/open-telemetry/opentelemetry-js/pull/6757) reviews please
- [marylia] reviews welcome, they're looking to make the spec stable [https://github.com/open-telemetry/opentelemetry-js/pull/6774](https://github.com/open-telemetry/opentelemetry-js/pull/6774)
- [pranav] any more feedback on this?
  - Discuss the expected behavior (would help me address [this comment](https://github.com/open-telemetry/opentelemetry-js/pull/6655#discussion_r3349786684)).
- [jamie] genai semantic conventions will be released from a new repo on a different cadence (with different versioning from core semconv)
  - We need to be sure to update our generating script, and plan on creating a new semconv-genai package: [https://github.com/open-telemetry/opentelemetry-js/issues/6783](https://github.com/open-telemetry/opentelemetry-js/issues/6783)
  - [https://cloud-native.slack.com/archives/C01NJ7V1KRC/p1780449446268529](https://cloud-native.slack.com/archives/C01NJ7V1KRC/p1780449446268529) genai semconv will show as deprecated in the next release, until the genai semconv release happens
- [trent] Doing a release this week?
- [trent] (if time) Chat about widening Attributes type in the API.
- [Untriaged bugs](https://github.com/open-telemetry/opentelemetry-js/issues?q=is%3Aissue+is%3Aopen+label%3Atriage+label%3Abug+-label%3Apriority%3Ap1++-label%3Apriority%3Ap2++-label%3Apriority%3Ap3++-label%3Apriority%3Ap4+)
- [Untriaged contrib bugs](https://github.com/open-telemetry/opentelemetry-js-contrib/issues?q=is%3Aissue+is%3Aopen+label%3Atriage%2Cbug+-label%3Apriority%3Ap1++-label%3Apriority%3Ap2++-label%3Apriority%3Ap3++-label%3Apriority%3Ap4)
- [Old Contrib PR Triage](https://github.com/open-telemetry/opentelemetry-js-contrib/pulls?q=is%3Apr+is%3Aopen+sort%3Acreated-asc)
- [Old Core PR Triage](https://github.com/open-telemetry/opentelemetry-js/pulls?q=is%3Apr+is%3Aopen+sort%3Acreated-asc)

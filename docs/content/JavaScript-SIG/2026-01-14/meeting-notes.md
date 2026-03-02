## Meeting Notes

### Attendees
- Marc Pichler (Dynatrace)
- Andrei Borza (Sentry)
- Marylia Gutierrez (Grafana Labs)
- David Luna (Elastic)
- Jamie Danielson (Honeycomb)
- Jackson Weber (Microsoft)
- Marten Hennoch (Splunk)
- Trent Mick (Elastic)

### Agenda
- **Feel free to add your topics below ↙️ 🙂**
- [marylia] can we get a new release to have the fix from [https://github.com/open-telemetry/opentelemetry-js/pull/6295](https://github.com/open-telemetry/opentelemetry-js/pull/6295) ?
  - [marc] on it :)
- [marylia] fyi proposal [https://github.com/open-telemetry/opentelemetry-specification/pull/4813](https://github.com/open-telemetry/opentelemetry-specification/pull/4813)
- [marylia] new focus topics
  - Jamie will update Focus Topic issue
  - Logs are top priority
  - Core implementation for declarative config (unblocks stability for config spec)
  - Add SDK 3.0 to backlog
  - Consider ESM bucket (separate from publishing) for docs, testing, etc
- [marc] please review (fixes test failures in contrib, unblocks contrib release)
  - [https://github.com/open-telemetry/opentelemetry-js-contrib/pull/3337](https://github.com/open-telemetry/opentelemetry-js-contrib/pull/3337)
  - one approval, lets see if the owner approves
- [andrei] looking for reviews to support instrumenting libraries that use subpath exports
  - [https://github.com/open-telemetry/opentelemetry-js/pull/6246](https://github.com/open-telemetry/opentelemetry-js/pull/6246)
  - Currently under review, there is some weirdness with our current implementation of RITM/IITM that likely needs to be updated for this.
- [carlos] Update on [feat(opentelemetry-resources): Update the Env Var Parsing Logic](https://github.com/open-telemetry/opentelemetry-js/pull/6261) after started talking to the Spec group.
  - Not all SIGs try to recover, and people seem supportive of failing fast instead
  - Will prepare a small report for the Spec call (later today) so we can discuss alternatives with a list of behavior for all different SIGs
  - There’s a big chance that we will define the _good_ expected input, and leave anything else unspecified.
- [marten] Codeowners mia for months [https://github.com/open-telemetry/opentelemetry-js-contrib/pull/3226](https://github.com/open-telemetry/opentelemetry-js-contrib/pull/3226)
  - Try to find on cncf slack
- [Untriaged bugs](https://github.com/open-telemetry/opentelemetry-js/issues?q=is%3Aissue+is%3Aopen+label%3Atriage+label%3Abug+-label%3Apriority%3Ap1++-label%3Apriority%3Ap2++-label%3Apriority%3Ap3++-label%3Apriority%3Ap4+)
- [Untriaged contrib bugs](https://github.com/open-telemetry/opentelemetry-js-contrib/issues?q=is%3Aissue+is%3Aopen+label%3Atriage%2Cbug+-label%3Apriority%3Ap1++-label%3Apriority%3Ap2++-label%3Apriority%3Ap3++-label%3Apriority%3Ap4)
- [Old Contrib PR Triage](https://github.com/open-telemetry/opentelemetry-js-contrib/pulls?q=is%3Apr+is%3Aopen+sort%3Acreated-asc)
- [Old Core PR Triage](https://github.com/open-telemetry/opentelemetry-js/pulls?q=is%3Apr+is%3Aopen+sort%3Acreated-asc)

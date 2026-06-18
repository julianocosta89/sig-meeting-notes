## Meeting Notes

### Attendees
- Trent Mick (Elastic)
- Raphaël Thériault (SW)
- Marc Pichler (Dynatrace)
- Pranav Sharma (Google)
- Jackson Weber (Microsoft)
- Hector Hernandez (Microsoft)
- Marylia Gutierrez (Grafana)
- David Luna (Elastic)

### Agenda
- [pellared (offline)] PTAL [feat(propagator-env-carrier): add environment variable carrier helpers #6774](https://github.com/open-telemetry/opentelemetry-js/pull/6774)
  - [marc] merged :)
- [trentm] Objections to renaming `interface BufferConfig` in `sdk-trace` and `sdk-logs` (breaking change)?
  - See [https://github.com/open-telemetry/opentelemetry-js/pull/6817](https://github.com/open-telemetry/opentelemetry-js/pull/6817)
  - See the “Two arguments or one to the constructor” section. Preferences for which form?
- [marylia] plans for [prom-client to move to Prometheus org](https://github.com/siimon/prom-client/issues/697), but they need help to maintain (existing ones won't have time). Anyone interested in helping maintain/provide support?
- [trentm] I can haz re-review on [https://github.com/open-telemetry/opentelemetry-js/pull/6785](https://github.com/open-telemetry/opentelemetry-js/pull/6785) (a start at fail-fast handling for declarative config parsing)?
  - [marylia] approved
- [marc] I’ll be ooo from July 6 - July 10; anybody up for running the SIG meeting on July 8?
  - Trent will run the SIG meeting :) Thanks!
- [pranav] Any more feedback on [https://github.com/open-telemetry/opentelemetry-js/pull/6655](https://github.com/open-telemetry/opentelemetry-js/pull/6655) before we can get it merged?
- [carlos] SDK Logs review (we can create issues from these comments if/as needed?)
  - Logger SHOULD be created only via LoggerProvider. Since it’s a SHOULD rather than a MUST, we are fine (mostly).
    - [trent] Discussed, and because `Logger` class is not exported we are fine. Users of `sdk-logs` do not have access to create Logger instances directly. The only current `new Logger` is by the LoggerProvider impl.
  - Consider renaming SdkLogRecord to ReadWriteLogRecord.
    - Added [https://github.com/open-telemetry/opentelemetry-js/issues/6821](https://github.com/open-telemetry/opentelemetry-js/issues/6821) for this
  - SdkLogRecord should allow more members to be modified: [https://github.com/open-telemetry/opentelemetry-specification/blob/main/specification/logs/sdk.md#readwritelogrecord](https://github.com/open-telemetry/opentelemetry-specification/blob/main/specification/logs/sdk.md#readwritelogrecord)
    - Added [https://github.com/open-telemetry/opentelemetry-js/issues/6822](https://github.com/open-telemetry/opentelemetry-js/issues/6822) for this
  - Logger.emit() doesn’t prevent side work to happen in case its LoggerProvider has shutdown, e.g. metrics reporting.
    - Added [https://github.com/open-telemetry/opentelemetry-js/issues/6823](https://github.com/open-telemetry/opentelemetry-js/issues/6823) for this.
- [hector] Console Instrumentation and OpenAI support Responses API PRs
- [Untriaged bugs](https://github.com/open-telemetry/opentelemetry-js/issues?q=is%3Aissue+is%3Aopen+label%3Atriage+label%3Abug+-label%3Apriority%3Ap1++-label%3Apriority%3Ap2++-label%3Apriority%3Ap3++-label%3Apriority%3Ap4+)
- [Untriaged contrib bugs](https://github.com/open-telemetry/opentelemetry-js-contrib/issues?q=is%3Aissue+is%3Aopen+label%3Atriage%2Cbug+-label%3Apriority%3Ap1++-label%3Apriority%3Ap2++-label%3Apriority%3Ap3++-label%3Apriority%3Ap4)
- [Old Contrib PR Triage](https://github.com/open-telemetry/opentelemetry-js-contrib/pulls?q=is%3Apr+is%3Aopen+sort%3Acreated-asc)
- [Old Core PR Triage](https://github.com/open-telemetry/opentelemetry-js/pulls?q=is%3Apr+is%3Aopen+sort%3Acreated-asc)

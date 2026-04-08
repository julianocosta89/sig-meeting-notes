## Meeting Notes

### Attendees
- Hannah Ramadan (New Relic)
- Kayla Reopelle (New Relic)
- Xuan Cao (Solarwinds)
- Arjun Rajappa (IBM Instana)

### Agenda
- [Spec SIG](https://docs.google.com/document/d/1pdvPeKjA8v8w_fGKAN68JjWBmVJtPCpqdi9IZrd6eEo/preview) Update (max 15 min)
  - If you/your customers would like to have a system package to install OTel, please chime in on this PR: [https://github.com/open-telemetry/community/pull/3252](https://github.com/open-telemetry/community/pull/3252)
- Core ([Issues](https://github.com/open-telemetry/opentelemetry-ruby/issues) / [PRs](https://github.com/open-telemetry/opentelemetry-ruby/pulls))
  - [kayla] ​ [Requires in the wrong place in opentelemetry-logs-sdk and opentelemetry-metrics-sdk · Issue #1955 · open-telemetry/opentelemetry-ruby](https://github.com/open-telemetry/opentelemetry-ruby/issues/1955)
  - [arjun] opened 3 new exporter-related PRs that are ready for review:
    - [feat(otlp-grpc): add retry logic and comprehensive error handling to …](https://github.com/open-telemetry/opentelemetry-ruby/pull/2076)
    - [test(otlp-common): expand test coverage for OTLP common exporter](https://github.com/open-telemetry/opentelemetry-ruby/pull/2075)
    - [feat(otlp-http): improve endpoint handling, add User-Agent header, an…](https://github.com/open-telemetry/opentelemetry-ruby/pull/2074)
- Contrib ([Issues](https://github.com/open-telemetry/opentelemetry-ruby-contrib/issues) / [PRs](https://github.com/open-telemetry/opentelemetry-ruby-contrib/pulls))
  - [hannah] - Chat on db stable migration span names
    - [PR convo](https://github.com/open-telemetry/opentelemetry-ruby-contrib/pull/2095#discussion_r2962685547)
    - [Slack convo](https://cloud-native.slack.com/archives/C01NWKKMKMY/p1774363670490889)
    - Hannah will work on doc that lays out our options and present during next week’s meeting
  - [xuan] Please review the operator PR: [https://github.com/open-telemetry/opentelemetry-ruby-contrib/pull/1384](https://github.com/open-telemetry/opentelemetry-ruby-contrib/pull/1384)
- Burning questions?
- ✨ Happy Reports ✨

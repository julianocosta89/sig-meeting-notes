## Meeting Notes

### Attendees
- Sven Cowart (ElastiFlow)
- Josh Suereth
- Armin Ruech (Dynatrace)
- Christophe Kamphaus
- Ruediger Schulze (IBM)
- Liudmila Molkova (Google)
- Kathie Huang (Datadog)
- Daniel Dyla (Dynatrace)

### Agenda
- timebox 7 min) Project Status + Triage + Blockers
  - Stability Blockers
  - PR Triage Board: [https://github.com/orgs/open-telemetry/proje](https://github.com/orgs/open-telemetry/projects/67/views/1)
  - [cts/67/views/1](https://github.com/orgs/open-telemetry/projects/67/views/1)
  - Issue Triage Board: [https://github.com/orgs/open-telemetry/projects/131/views/1](https://github.com/orgs/open-telemetry/projects/131/views/1)
- (timebox 50 min) General topics
  - [Sven] [Network SIG project proposal](https://github.com/open-telemetry/community/pull/3560)
  - [Sven] [`hw` area metrics](https://opentelemetry.io/docs/specs/semconv/hardware/network/)
  - [Kathie] Azure Container App replica name PR [https://github.com/open-telemetry/semantic-conventions/pull/3860](https://github.com/open-telemetry/semantic-conventions/pull/3860)
- [Liudmila] V2 migration
  - [https://github.com/open-telemetry/semantic-conventions/pull/3905](https://github.com/open-telemetry/semantic-conventions/pull/3905)
  - [https://github.com/open-telemetry/semantic-conventions/pull/3904](https://github.com/open-telemetry/semantic-conventions/pull/3904)
    - [https://github.com/open-telemetry/opentelemetry-java-instrumentation/pulls?q=is%3Apr+is%3Aopen+messaging+in%3Atitle+author%3Atrask](https://github.com/open-telemetry/opentelemetry-java-instrumentation/pulls?q=is%3Apr+is%3Aopen+messaging+in%3Atitle+author%3Atrask)
  - [https://github.com/open-telemetry/semantic-conventions/pull/3903](https://github.com/open-telemetry/semantic-conventions/pull/3903)
  - Makefile change - needed to remove `–future`.  Can we find a way to keep `--future` *and* use `--v2`.
- [Liudmila] Self-observability event
  - [https://github.com/open-telemetry/semantic-conventions/pull/3723](https://github.com/open-telemetry/semantic-conventions/pull/3723)
  - For context - prototype on getting data off-process quickly and without allocating new memory (ideally) - [https://github.com/jsuereth/otlp-mmap](https://github.com/jsuereth/otlp-mmap)
- [Liudmila] Shared templates are out of draft and looking for reviews [https://github.com/open-telemetry/opentelemetry-weaver-packages/pull/38](https://github.com/open-telemetry/opentelemetry-weaver-packages/pull/38)
  - Note: need to cut release of weaver for full set of features.

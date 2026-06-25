## Meeting Notes

### Attendees
- Tyler Yahn (Splunk)
- Nikola Grcevski (Grafana)
- Rafael Roquetto (Grafana)
- Stephen Lang (Grafana)
- Mike Dame (Odigos)
- Roy Reshef (Kubex)
- [Florian Lehner](mailto:florian.lehner@elastic.co) (Elastic)
- Mattia Meleleo (Coralogix)
- Rob Cowart (ElastiFlow)
- Nimrod Avni (Coralogix)
- Giuseppe Ognibene (Coralogix)
- Antonio Jimenez (ThousandEyes)

### Agenda
- [Tyler] [Import config v2 capture rules](https://github.com/open-telemetry/opentelemetry-ebpf-instrumentation/pull/2462)
- [Tyler] [Guard Docker major Renovate updates](https://github.com/open-telemetry/opentelemetry-ebpf-instrumentation/pull/2463)
- [Nimrod] [Stale issues](https://github.com/open-telemetry/opentelemetry-ebpf-instrumentation/issues?q=is%3Aissue%20state%3Aopen%20label%3Astale%20-label%3A%22goal%3A%202026%22%20sort%3Acreated-asc)
- [Rafael + Stephen] PR review bandwidth, assignees and triage
  - Add a limited time Triage meeting.
    - Let’s keep it async in slack
    - AI (Nimrod): setup automation
  - PRs merging while doing a review is frustrating
  - 2 Reviewers
    - Maybe wait a full day for smaller PR only 1 PR
  - If a PR has an assignee they need to have reviewed the PR before it is merged
  - AI (Rafael): capture this in our policy docs
- [Nikola] New minor release [v0.10.0](https://github.com/open-telemetry/opentelemetry-ebpf-instrumentation/milestone/12)
  - [Cloud node metadata is exported to Prometheus and OTLP without sensitivity filtering](https://github.com/open-telemetry/opentelemetry-ebpf-instrumentation/issues/2014)
  - [Documentation for parent-child association limitations](https://github.com/open-telemetry/opentelemetry-ebpf-instrumentation/issues/903)
  - [Support receiver-side span links for Go channel handoffs](https://github.com/open-telemetry/opentelemetry-ebpf-instrumentation/issues/2238)
    - [Track buffered Go channel handoffs](https://github.com/open-telemetry/opentelemetry-ebpf-instrumentation/pull/2432)
  - [Robert] Consider [Sign release artifacts with cosign bundles #2480](https://github.com/open-telemetry/opentelemetry-ebpf-instrumentation/pull/2480) it *may* help [[cmd/builder] Support components whose module source is published as a release artifact #15430](https://github.com/open-telemetry/opentelemetry-collector/issues/15430)
  - [Nimrod] [Emit url.query with automatic redaction for non-Go HTTP spans](https://github.com/open-telemetry/opentelemetry-ebpf-instrumentation/pull/2415) 🙏
- [Tyler] Please comment on [[cmd/builder] Support components whose module source is published as a release artifact](https://github.com/open-telemetry/opentelemetry-collector/issues/15430#top)
- [Nimrod] [https://github.com/open-telemetry/opentelemetry-specification/pull/5116](https://github.com/open-telemetry/opentelemetry-specification/pull/5116)

## Meeting Notes

### Attendees
- Robert Pająk (Splunk)
- Tyler Yahn (Splunk)
- Sam Xie (Splunk)
- David Ashpole (Google)
- Sonal Gaud
- Bryan Boreham (Grafana Labs)

### Agenda
- [Sonal] Discuss [https://github.com/open-telemetry/opentelemetry-go-contrib/issues/8582](https://github.com/open-telemetry/opentelemetry-go-contrib/issues/8582)
- [Tyler] [Add Finish on synchronous instruments](https://github.com/open-telemetry/opentelemetry-go/pull/8050)
- [Robert] Discuss “What's Up, OTel?”. Quoting: “Speak with one SIG maintainer every month to learn about cool stuff going on in the SIG, whether it's a new release, call for more maintainers, etc.”
  - Slack message [https://cloud-native.slack.com/archives/C01NJ7V1KRC/p1772747659502499](https://cloud-native.slack.com/archives/C01NJ7V1KRC/p1772747659502499)
  - Google form: [https://docs.google.com/forms/d/e/1FAIpQLSfkW3wBNuIm-HLj2vpAiOErEcm6WEHU9sKkcBZoHiVhfuNIQA/viewform](https://docs.google.com/forms/d/e/1FAIpQLSfkW3wBNuIm-HLj2vpAiOErEcm6WEHU9sKkcBZoHiVhfuNIQA/viewform)
- [Robert/Bryan] [attribute: add String method to Value and KeyValue #7812](https://github.com/open-telemetry/opentelemetry-go/pull/7812)
- [David] Update on metrics SDK optimization:
  - Exp histogram optimization:
    - First small change: [https://github.com/open-telemetry/opentelemetry-go/pull/8025](https://github.com/open-telemetry/opentelemetry-go/pull/8025)
    - More tests:
      - [https://github.com/open-telemetry/opentelemetry-go/pull/8024](https://github.com/open-telemetry/opentelemetry-go/pull/8024)
      - [https://github.com/open-telemetry/opentelemetry-go/pull/8021](https://github.com/open-telemetry/opentelemetry-go/pull/8021)
  - Attributes passing:
    - Benchmarks: [https://github.com/open-telemetry/opentelemetry-go/pull/7768](https://github.com/open-telemetry/opentelemetry-go/pull/7768)

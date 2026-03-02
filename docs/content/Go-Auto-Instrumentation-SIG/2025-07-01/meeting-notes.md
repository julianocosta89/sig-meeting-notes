## Meeting Notes

### Attendees
- ~~Nikola Grcevski (Grafana)~~ (Holiday in Canada)
- ~~Rafael Roquetto (Grafana)~~ (Holiday in Canada)
- Tyler Yahn (Splunk)
- Mike Dame (Odigos)
- Ron Federman (Odigos)

### Agenda
- [Tyler] [v0.22.1 milestone](https://github.com/open-telemetry/opentelemetry-go-instrumentation/milestone/22) check-in
  - Plan to get a release out this afternoon
- Shifting probe management to manager [https://github.com/open-telemetry/opentelemetry-go-instrumentation/pull/2029](https://github.com/open-telemetry/opentelemetry-go-instrumentation/pull/2029)
  - AI: work on a "steel thread" poc showing a probe imported in OBI
    - Odigos uses NewInstrumentation machinery already
- [Ron] should we return some docker/k8s minimal test (because of the arm64 bug)?

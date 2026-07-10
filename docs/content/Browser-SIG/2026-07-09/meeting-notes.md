## Meeting Notes

### Attendees
- Jared Freeze (Embrace)
- Martin Kuba (Grafana)
- Trent Mick (Elastic)
- Jared Lewis
- Maxime Quentin (Datadog)
- Hugo Levy (Datadog)
- Rebecca He (Google/Firebase)
- Ted Young (Grafana Labs)

### Agenda
- [martin] SDK package release
  - [https://github.com/open-telemetry/opentelemetry-browser/pull/341](https://github.com/open-telemetry/opentelemetry-browser/pull/341)
  - [trent] I’d like to use the Browser SDK package as a replacement for WebTracerProvider from sdk-trace-web, so I can deprecate the sdk-trace-web package.
  - [Maxime] update the sandbox to use the new released SDK package
    - See how to better give visual feedbacks on data sent to intake
- [Ted] Working more with semconv, spec sig, other client sigs
  - Example federated semconv repo for clients
    - [https://github.com/bidetofevil/end-user-client-semantic-conventions](https://github.com/bidetofevil/end-user-client-semantic-conventions)
  - Presenting at spec meeting
  - #otel-client-side-telemetry [https://cloud-native.slack.com/archives/C0239SYARD2](https://cloud-native.slack.com/archives/C0239SYARD2)
  - #otel-mainainers ​​[https://cloud-native.slack.com/archives/C01NJ7V1KRC](https://cloud-native.slack.com/archives/C01NJ7V1KRC)
- [Ted] Network timing event:
  - [https://github.com/open-telemetry/semantic-conventions/pull/3727/changes#r3455632132](https://github.com/open-telemetry/semantic-conventions/pull/3727/changes#r3455632132)

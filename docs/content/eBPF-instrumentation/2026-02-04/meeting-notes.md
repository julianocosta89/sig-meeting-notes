## Meeting Notes

### Attendees
- Nikola Grcevski (Grafana)
- [Florian Lehner](mailto:florian.lehner@elastic.co) (Elastic)
- Giuseppe Ognibene (Coralogix)
- Tyler Yahn (Splunk)
- [Mario Macías](mailto:mario.macias@grafana.com)
- Mike Dame (odigos)
- Mattia Meleleo (Coralogix)
- Antonio Jimenez (ThousandEyes)
- Rafael Roquetto (Grafana)
- Stephen Lang (Grafana)
- Marc Tuduri (Grafana)

### Agenda
- [Mario] OTEL Unplugged topics
  - Packaging (future) SIG
  - Auto-instrumentation in OTEL demo
  - USDTs
    - [https://github.com/oxidecomputer/tokio-dtrace](https://github.com/oxidecomputer/tokio-dtrace)
    - [https://www.polarsignals.com/blog/posts/2025/12/10/usdt-deep-dive](https://www.polarsignals.com/blog/posts/2025/12/10/usdt-deep-dive)
  - Log export
  - Doc: when to use/tradeoffs section
  - Otel-go-autoinstrumentation project
    - It should be seen as a library
    - Stop publishing image
    - Redirect to OBI
    - [https://github.com/open-telemetry/opentelemetry-go-instrumentation/issues/2500](https://github.com/open-telemetry/opentelemetry-go-instrumentation/issues/2500)
- [Antonio Jimenez] New contributor [ajimenez1503](https://github.com/ajimenez1503)
  - I am interested in OpenTelemetry and eBFP and I would like to help.
  - If you see any simple Github issue please let me know and I will try to work on it 🙂 Thanks
    - There are not more (Good first issue) I took the last one.
- [Tyler] [2026 Goals](https://github.com/orgs/open-telemetry/projects/187/views/1) Check-in
- [Rafael] Updates on Traceparent handling
  - [https://github.com/open-telemetry/opentelemetry-ebpf-instrumentation/pull/1162](https://github.com/open-telemetry/opentelemetry-ebpf-instrumentation/pull/1162)
- [Nikola] Span events are being deprecated and impact on what we wanted to achieve
- [Tyler] [Open PRs Review](https://github.com/open-telemetry/opentelemetry-ebpf-instrumentation/pulls)

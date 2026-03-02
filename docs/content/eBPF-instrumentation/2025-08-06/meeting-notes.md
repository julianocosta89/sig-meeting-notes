## Meeting Notes

### Attendees
- Tyler Yahn (Splunk)
- Rafael Roquetto (Grafana)
- Nikola Grcevski (Grafana)
- Mattia Meleleo (Coralogix)
- Nimrod Avni (Coralogix)
- Marc Tuduri (Grafana)

### Agenda
- [Nimrod] OTel Demo instrumentation
  - [https://github.com/open-telemetry/opentelemetry-demo](https://github.com/open-telemetry/opentelemetry-demo)
  - Issues:
    - Does not work with cgroups v1 (Amazon Linux 5.10)
    - Newer Kafka versions don’t send the topic any more, just an ID meaning [`messaging.destination.name`](http://messaging.destination.name) doesn’t get populated
      - Maybe able to resolve this in userspace
    - Kafka Java clients' split packets (header then body) may be causing communication from some services (kafka to Fraud Detection) to be missing.
    - Modern instrumentation for sarama may be over batching. The checkout service is not reporting “orders published” as frequently as expected
    - Missing Frontend to Checkout because it is using gRPC
- [Tyler] [Open PRs Review](https://github.com/open-telemetry/opentelemetry-ebpf-instrumentation/pulls)
- [Rafael] Copyright headers
- [Rafael] sockops/msg/stream verdict  programs
- [Nimrod] [Http payload extraction](https://github.com/open-telemetry/opentelemetry-ebpf-instrumentation/issues/396)

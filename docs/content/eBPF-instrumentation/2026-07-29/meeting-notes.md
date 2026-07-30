## Meeting Notes

### Attendees
- Tyler Yahn (Splunk)
- Mario Macias (Grafana)
- Giuseppe Ognibene (Coralogix)
- Mattia Meleleo (Coralogix)
- Stephen Lang (Grafana)
- Roy Reshef (Kubex)
- Nimrod Avni (Coralogix)
- Marc Tudurí (Grafana)

### Agenda
- [Mario] Deno support
  - Using not-yet-standard telemetry.sdk.language==deno-rust
    - [https://docs.deno.com/runtime/fundamentals/open_telemetry/](https://docs.deno.com/runtime/fundamentals/open_telemetry/)
    - [https://github.com/open-telemetry/opentelemetry-js/issues/2293](https://github.com/open-telemetry/opentelemetry-js/issues/2293)
  - Shall we rename configV2 “nodejs.enabled” to “js.enabled”?
- [Mario] ARM integration tests: should we run all the tests?
  - We didn’t realized this bug until I hit it locally [https://github.com/open-telemetry/opentelemetry-ebpf-instrumentation/pull/2825](https://github.com/open-telemetry/opentelemetry-ebpf-instrumentation/pull/2825)
    - Let’s run all tests! [Stephen Lang](mailto:stephen.lang@grafana.com) to pick this up
- [Tyler] Requesting review:
  - [Enable standalone Config v2 runtime loading](https://github.com/open-telemetry/opentelemetry-ebpf-instrumentation/pull/2682)
  - [Limit NestJS route harvesting expansion](https://github.com/open-telemetry/opentelemetry-ebpf-instrumentation/pull/2813)
  - [Stabilize YAML export mode ordering](https://github.com/open-telemetry/opentelemetry-ebpf-instrumentation/pull/2816)
  - [Keep language detection skips internal](https://github.com/open-telemetry/opentelemetry-ebpf-instrumentation/pull/2818)
  - [Add optional Go probe orchestration](https://github.com/open-telemetry/opentelemetry-ebpf-instrumentation/pull/2820)
- [Tyler] [Make OBI head-sampling decisions in eBPF](https://github.com/open-telemetry/opentelemetry-ebpf-instrumentation/issues/2793)
- [Nimrod] Requesting Reviews
  - [Weaver validation for internal telemetry](https://github.com/open-telemetry/opentelemetry-ebpf-instrumentation/pull/2723)
  - [Node.js manual spans support](https://github.com/open-telemetry/opentelemetry-ebpf-instrumentation/pull/2661)

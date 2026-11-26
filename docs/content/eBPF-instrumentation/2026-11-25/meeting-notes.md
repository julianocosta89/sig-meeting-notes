## Meeting Notes

### Attendees
- ~~Tyler Yahn (Splunk)~~ – OoO
- Stephen Lang (Grafana)
- [Gregor Zeitlinger](mailto:gregor.zeitlinger@grafana.com) (Grafana)
- Mario Macias (Grafana)
- Mike Dame (Odigos)
- Nikola Grcevski (Grafana)
- Rafael Roquetto (Isovalent)
- Aryan Bakliwal (AccuKnox)
- Mattia Meleleo (Coralogix)
- Marc Tudurí (Grafana)
- Giuseppe Ognibene (Coralogix)
- Roy Reshef (Kubex)

### Agenda
- [Gregor] Use experimental/opt-in for dynamic instrumentation? [https://github.com/open-telemetry/opentelemetry-ebpf-instrumentation/pull/3922](https://github.com/open-telemetry/opentelemetry-ebpf-instrumentation/pull/3922)
  - Feature flag? How to track alpha/beta stability. Long-lived integration branches can drift easily from main.
    - Use prior art from Java instrumentation
  - Look into adding API differ in a separate PR
- [Mattia] GPU device metrics - [https://github.com/open-telemetry/opentelemetry-ebpf-instrumentation/pull/4350](https://github.com/open-telemetry/opentelemetry-ebpf-instrumentation/pull/4350)
  - Consensus around new GPU metrics and attributes needed between Mattia and Marc’s work
  - KubeCon talk around Inspektor Gadget/CPU integration [GPU Observability with eBPF: From Kernel Hooks to... Qasim Sarfraz & Michael Friese, Microsoft](https://www.youtube.com/watch?v=F1_mt2wx8LA)
  - See also for testing/mocking: [Fake It Until You Make It: Mocking... Eduardo Arango Gutierrez, NVIDIA & John Belamaric, Google](https://youtu.be/umTWiqnXtjg?si=Q5ELGm3rC8cgvUnW&t=1220)
  - Prometheus exporters for reference:
    - [https://github.com/densify-dev/gpu-process-exporter](https://github.com/densify-dev/gpu-process-exporter)
    - [Nvidia DCGM exporter](https://github.com/NVIDIA/dcgm-exporter)
  - CUDA + TPU + AMD?
  - Mattia Meleleo + Marc - Issue to capture decisions
- [Mattia] Release v1.1.0?
  - [https://github.com/open-telemetry/opentelemetry-ebpf-instrumentation/milestone/22](https://github.com/open-telemetry/opentelemetry-ebpf-instrumentation/milestone/22)
  - Call for review: [https://github.com/open-telemetry/opentelemetry-ebpf-instrumentation/pull/4149](https://github.com/open-telemetry/opentelemetry-ebpf-instrumentation/pull/4149)
- [Giuseppe] PTAL [https://github.com/open-telemetry/opentelemetry-ebpf-instrumentation/discussions/4295](https://github.com/open-telemetry/opentelemetry-ebpf-instrumentation/discussions/4295)
- [Nikola/Giuseppe] Rust (instrumentation) support
  - Gotcha with memory pages not yet loaded
- Rust vs Go
  - Memory efficiency is tempting, could it apply to the OBI pipeline? If so, how?
  - What can we achieve in Go first of all? Can a columnar approach (like Apache Arrow) help here?
- [Rafael] [https://github.com/open-telemetry/opentelemetry-ebpf-instrumentation/pull/4339](https://github.com/open-telemetry/opentelemetry-ebpf-instrumentation/pull/4339)
  - Truncated payload support is required, json.Valid may be the way to go
- [Nikola] [https://github.com/open-telemetry/opentelemetry-ebpf-instrumentation/pull/4353](https://github.com/open-telemetry/opentelemetry-ebpf-instrumentation/pull/4353)
  - Ok to reduce ring buf size for net o11y

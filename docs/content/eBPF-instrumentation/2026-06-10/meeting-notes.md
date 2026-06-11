## Meeting Notes

### Attendees
- Rob Cowart (ElastiFlow)
- Nikola Grcevski (Grafana)
- Rafael Roquetto (Grafana)
- Stephen Lang (Grafana)
- Giuseppe Ognibene (Coralogix)
- Nimrod Avni (Coralogix))
- Roy Reshef (Kubex)
- Tyler Yahn (Splunk)
- Mattia Meleleo (Coralogix)
- Antonio Jimenez (ThousandEyes)
- Vivek Akupatni (in personal capacity: Not authorized to put in company name)
- Mario Macias (Grafana)
- Mike Dame (Odigos)
- Endre Sara (Causely)
- Haibin Zhang(Alibaba Cloud)

### Agenda
- [Tyler (10-min)] [Roadmap](https://github.com/orgs/open-telemetry/projects/187/views/1) check-in
- [mike] rpc metric attributes/labels across multiple systems – discussion started in [https://github.com/open-telemetry/opentelemetry-ebpf-instrumentation/pull/2210](https://github.com/open-telemetry/opentelemetry-ebpf-instrumentation/pull/2210)
  - We have "rpc_client_duration"/"rpc_server_duration" metrics with 3 labels:
    - rpc.method / rpc.system / rpc.grpc.status_code
  - "grpc.status_code" becomes an issue with new RPC systems, and vice versa
  - should this be "rpc.response.status_code"? grpc.status_code is a [trace attribute](https://github.com/open-telemetry/opentelemetry-ebpf-instrumentation/pull/2210#discussion_r3351038373)
  - AI: mike fix
- [Nikola] Haibin is proposing increasing the limits [https://github.com/open-telemetry/opentelemetry-ebpf-instrumentation/issues/2267#issuecomment-4646965621](https://github.com/open-telemetry/opentelemetry-ebpf-instrumentation/issues/2267#issuecomment-4646965621)
- [Roy] Survey mode feature request: [https://github.com/open-telemetry/opentelemetry-ebpf-instrumentation/issues/2285](https://github.com/open-telemetry/opentelemetry-ebpf-instrumentation/issues/2285)
- [Nimrod] New patch / minor release?
  - [Tyler] [v0.10.0 milestone](https://github.com/open-telemetry/opentelemetry-ebpf-instrumentation/milestone/12)
    - [Cloud node metadata is exported to Prometheus and OTLP without sensitivity filtering](https://github.com/open-telemetry/opentelemetry-ebpf-instrumentation/issues/2014)
    - [In-memory PID cache is never cleared on BlockPID](https://github.com/open-telemetry/opentelemetry-ebpf-instrumentation/issues/2021)
    - [Failed SSL reads still flow into protocol parsing](https://github.com/open-telemetry/opentelemetry-ebpf-instrumentation/issues/2029)
      - [fix(2029): harden SSL payload guards](https://github.com/open-telemetry/opentelemetry-ebpf-instrumentation/pull/2237)
    - [Timeout does not cancel blocked Java extraction](https://github.com/open-telemetry/opentelemetry-ebpf-instrumentation/issues/2034)
    - [avoided_services has unbounded service-identity cardinality](https://github.com/open-telemetry/opentelemetry-ebpf-instrumentation/issues/2037)
    - [HTTP/2 preface skip shifts pointer without shrinking length](https://github.com/open-telemetry/opentelemetry-ebpf-instrumentation/issues/2040)
    - [Document the new selective telemetry and sampler](https://github.com/open-telemetry/opentelemetry-ebpf-instrumentation/issues/365)
    - [Document application_span_otel](https://github.com/open-telemetry/opentelemetry-ebpf-instrumentation/issues/366)
    - [Documentation for parent-child association limitations](https://github.com/open-telemetry/opentelemetry-ebpf-instrumentation/issues/903)
    - [eBPF agent saturates internal queue (sending queue is full) on one Kubernetes node even with restricted instrumentation](https://github.com/open-telemetry/opentelemetry-ebpf-instrumentation/issues/957)
    - [Blocked Upgrade: github.com/cilium/ebpf v0.21.0](https://github.com/open-telemetry/opentelemetry-ebpf-instrumentation/issues/1505)
    - [Support receiver-side span links for Go channel handoffs](https://github.com/open-telemetry/opentelemetry-ebpf-instrumentation/issues/2238)
      - [Add Go channel-link event parsing](https://github.com/open-telemetry/opentelemetry-ebpf-instrumentation/pull/2281)
- [Nimrod] OCB support for OBI ([Issue](https://github.com/open-telemetry/opentelemetry-collector/issues/15430), [Draft implementation](https://github.com/open-telemetry/opentelemetry-collector/pull/15431))

## Meeting Notes

### Attendees
- Steve
- Trask
- Liudmila
- James

### Agenda
- Which protocols / frameworks ? [https://github.com/open-telemetry/semantic-conventions/issues/2921](https://github.com/open-telemetry/semantic-conventions/issues/2921)
- Which layer ? (fx/library vs protocol, logical / physical)
  - [https://github.com/open-telemetry/semantic-conventions/pull/2961](https://github.com/open-telemetry/semantic-conventions/pull/2961) and [https://github.com/open-telemetry/semantic-conventions/issues/674](https://github.com/open-telemetry/semantic-conventions/issues/674)
  - Grpc call level - supported by OTel and gRPC otel plugin
    - Attempt layer - gRPC otel plugin
  - Connect RPC - ? (does not seem they differentiate call vs attempt)
  - Assuming logical
    - rpc.system.name = grpc | jsonrpc | connect-rpc | dubbo
      - Dubbo client can talk to grpc server
        - Similar to mongodb client talking to cosmos db server, etc
        - Http client -> dubbo server
    - network.protocol.name = dubbo2 | triple (or http ?)
    - Duration = call duration
    - There could be per-try spans specific to system
  - Assuming physical
    - What is physical layer? Triple / grpc / HTTP
    - Less practical - not something users observe directly
    - Hard to instrument physical
  - Let's do logical and leave retries for fx-specific convention
- Review open PRs

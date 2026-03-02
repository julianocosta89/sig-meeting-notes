## Meeting Notes

### Attendees
- Liudmila
- James Thompson
- Trask Stalnaker
- Steve Rao(Alibaba)

### Agenda
- [https://github.com/open-telemetry/semantic-conventions/issues/2921](https://github.com/open-telemetry/semantic-conventions/issues/2921)
  - Triple server supports multiple types of the clients (gRPC and HTTP)
    - Over the write, when client is gRPC, traffic is compatible with gRPC
    - `rpc.system` vs `rpc.protocol.name`
    - Opt1:
      - rpc.protocol.name = triple | dubbo2 | jsonrpc
        - But dubbo is probably (also) a network protocol
      - network.protocol.name = http (only when transport is HTTP) | dubbo2  | websockets ?
        - JSON RPC is a RPC protocol, but not a network protocol
      - network.transport = tcp
      - Content-type
        - http.request.header.content-type
        - Http.response.header.content-type
      - We can have additional dubbo-specific attributes
    - Triple (grpc-like, http, etc):
      - All network.protocol.name are http
      - Content-type is different (application/json etc)
    - Grpc
      - rpc.protocol.name = grpc
      - network.protocol.name = http
    - Record specific server (e.g. tomcat)
    - How many layers
      - Library / framework
        - RPC protocol (this is where interop happens)
          - Network protocol
- [https://github.com/open-telemetry/semantic-conventions/pull/2842](https://github.com/open-telemetry/semantic-conventions/pull/2842)
- [https://github.com/open-telemetry/semantic-conventions/issues/674](https://github.com/open-telemetry/semantic-conventions/issues/674)
- Rpc duration metrics
  - [https://github.com/open-telemetry/semantic-conventions/pull/2961](https://github.com/open-telemetry/semantic-conventions/pull/2961) & [https://github.com/open-telemetry/semantic-conventions/issues/2814](https://github.com/open-telemetry/semantic-conventions/issues/2814)

## Meeting Notes

### Attendees
- Trask
- Liudmila
- Steve

### Agenda
- Triage board [https://github.com/orgs/open-telemetry/projects/161/views/1](https://github.com/orgs/open-telemetry/projects/161/views/1)
- To discuss
  - Dubbo [https://github.com/open-telemetry/semantic-conventions/pull/3292](https://github.com/open-telemetry/semantic-conventions/pull/3292)
    - dubbo 2
      - network.protocol.name = dubbo
      - .version = 2 # if not 2
      - .transport = tcp # opt-in
    - dubbo 3
      - network.protocol.name = http
      - .version = 2  # if not 2
      - .transport = tcp # opt-in
    - Also can mention attachment as metadata
  - gRPC:
    - network.protocol.name = http # default? Conditionally_required if not HTTP
    - Network.protocol.version if not 2
    - network.transport : opt_in ?
    - we should make these 3 opt-in
  - Connect RPC and dubbo - might be useful to know if accessed over HTTP 1.1 vs gRPC (http/2)
    - Is it even possible?
    - HTTP client <-> Triple server
    - gRPC <-> Triple server
  - gRPC target  [https://github.com/open-telemetry/semantic-conventions/pull/3317](https://github.com/open-telemetry/semantic-conventions/pull/3317)

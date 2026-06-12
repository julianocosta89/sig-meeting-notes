## Meeting Notes

### Attendees
- Trask
- Steve
- Matthew

### Agenda
- Project board: [https://github.com/orgs/open-telemetry/projects/161](https://github.com/orgs/open-telemetry/projects/161)
- Concerns from gRPC team
  - rpc.response.status_code
    - Prefer rpc.status_code or rpc.result.status_code
  - server.address
    - Why do we have this escription in gRPC semconv on the Server span ([https://github.com/open-telemetry/semantic-conventions/blob/main/docs/rpc/grpc.md](https://github.com/open-telemetry/semantic-conventions/blob/main/docs/rpc/grpc.md))
      - “May contain a DNS name, an endpoint and path in the service registry, local socket name or an IP address”
  - error.type
    - What is this for given we already have status?
    - For metrics - whether error or not
    - Consistent across all spans and duration metrics
    - Exceptions thrown where there is no status code
  - network.peer.address / network.peer.port
    - IP address, leave blank if missing
  - rpc.request.metadata
    - Not part of RC

## Meeting Notes

### Attendees
- Liudmila
- Trask Stalnaker (Microsoft)
- James Thompson

### Agenda
- Project board
- Can we auto added issues/pr to the board based on label
- Add [#2799](https://github.com/open-telemetry/semantic-conventions/pull/2799) & [#2810](https://github.com/open-telemetry/semantic-conventions/pull/2810) to the board
- [https://github.com/open-telemetry/semantic-conventions/issues/2784](https://github.com/open-telemetry/semantic-conventions/issues/2784) -> metric investigation
  - Let's deprecate now and maybe add new alternative later when we work on streaming
- RPC status/error  codes
  - Rpc.connect_rpc.error_code - string
  - Rpc.grpc.status_code - integer in OTel, string in gRPC native instr
  - Rpc.jsonrpc.error_code - integer
  - Is it important for consistent dashboards?
    - Error.type
    - Rpc.response.status_code
  - How would we refine metrics
    - The paved path is to unify
    - The downsides - int to string (can be done efficiently)

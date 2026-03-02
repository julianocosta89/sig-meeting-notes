## Meeting Notes

### Attendees
- Liudmila
- Matthew
- Steve
- Trask

### Agenda
- Triage board [https://github.com/orgs/open-telemetry/projects/161/views/1](https://github.com/orgs/open-telemetry/projects/161/views/1)
  - Pls review: [https://github.com/open-telemetry/semantic-conventions/pull/3203](https://github.com/open-telemetry/semantic-conventions/pull/3203)
- Do we need a distinct rpc.service and rpc.method? [https://github.com/open-telemetry/semantic-conventions/issues/3196](https://github.com/open-telemetry/semantic-conventions/issues/3196)
  - No counter arguments for now
- RPC method/operation/call type [https://github.com/open-telemetry/semantic-conventions/issues/2864](https://github.com/open-telemetry/semantic-conventions/issues/2864)
  - Used to distinguish calls, especially on metrics
    - Unary
    - Client streaming
    - Server Streaming
    - Both streaming
  - gPRC https://github.com/grpc/grpc-go/blob/v1.77.0/server.go#L792
- ConnectRPC [https://github.com/connectrpc/connect-es/blob/main/packages/connect/src/interceptor.ts](https://github.com/connectrpc/connect-es/blob/main/packages/connect/src/interceptor.ts)
- Naming:
  - `rpc.method.type` (collides with `rpc.method`, another reason to rename it to `rpc.method.name`)
    - `unary | client_streaming | server_streaming | bidi_streaming`
    - `unary | streaming`
  - `rpc.call.type`
  - `rpc.streaming.type = client | server | bidi`
    - `rpc.streaming = true | false`
- We can have default value: e.g. rpc.streaming = false by default
- RPC is not evolving much, if we did rpc.streaming = false , once could still have `rpc.stream.type = client | server | bidi` in the future
- It won't be breaking to add attribute after because it would not result in splitting existing time series
  - Grpc don't have this flag
  - We haven't got any feedback to add split
  - Default grouping would be by method anyway

## Meeting Notes

### Attendees
- Liudmila
- Steve
- Trask

### Agenda
- [Liudmila] network protocol on rpc spans (do we need it and can we determine it):
  - [https://github.com/open-telemetry/semantic-conventions/pull/3350](https://github.com/open-telemetry/semantic-conventions/pull/3350)
  - Connectrpc: tight to content-type - [https://connectrpc.com/docs/multi-protocol](https://connectrpc.com/docs/multi-protocol), accessible as a header on interceptors
  - Dubbo: we can probably remove protocol name|version, transport too
  - Can add opt-in attribute later
    - Not interesting for most people
- Dubbo conventions [https://github.com/open-telemetry/semantic-conventions/pull/3292](https://github.com/open-telemetry/semantic-conventions/pull/3292)
- gRPC Target [https://github.com/open-telemetry/semantic-conventions/pull/3317](https://github.com/open-telemetry/semantic-conventions/pull/3317)

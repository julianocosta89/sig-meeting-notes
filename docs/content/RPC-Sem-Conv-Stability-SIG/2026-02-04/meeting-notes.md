## Meeting Notes

### Attendees
- Trask
- Liudmila
- Matthew
- Steve

### Agenda
- Dubbo - [https://github.com/open-telemetry/semantic-conventions/pull/3292](https://github.com/open-telemetry/semantic-conventions/pull/3292)
  - server.address vs network.peer.address
  - In client-side load-balancing scenario, is individual address logical (server.address) or physical (network.peer.address)?
- For both RPC and Database
  - If we know individual server being contacted, would we capture that in server.address
  - What to do with retries
    - network.peer.address -
  - Client-side load balance across 1.1.1.1 and 2.2.2.2
    - Forward proxy 3.3.3.3
    - network.peer.address = 3.3.3.3
    - server.address = (blank, if we say no logical server for client-side load balancing)
    - server.address = 1.1.1.1
- What are the harms of capturing non-logical addresses in server.address?
  - Cardinality
- TODO make general semconv recommendation around whether to capture server.address when doing client-side load balancing
- Grpc.target - ready to merge: [https://github.com/open-telemetry/semantic-conventions/pull/3317](https://github.com/open-telemetry/semantic-conventions/pull/3317)
- gRPC mapping - ready once above is merged: [https://github.com/open-telemetry/semantic-conventions/pull/3229](https://github.com/open-telemetry/semantic-conventions/pull/3229)
- Editorial:
  - [https://github.com/open-telemetry/semantic-conventions/pull/3390](https://github.com/open-telemetry/semantic-conventions/pull/3390)
  - [https://github.com/open-telemetry/semantic-conventions/pull/3391](https://github.com/open-telemetry/semantic-conventions/pull/3391)

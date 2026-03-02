## Meeting Notes

### Attendees
- Matthew
- Steve
- Liudmila

### Agenda
- Triage board [https://github.com/orgs/open-telemetry/projects/161/views/1](https://github.com/orgs/open-telemetry/projects/161/views/1)
- To review
  - Migration guide [https://github.com/open-telemetry/semantic-conventions/pull/3224](https://github.com/open-telemetry/semantic-conventions/pull/3224)
  - Merging method and service: [https://github.com/open-telemetry/semantic-conventions/pull/3223](https://github.com/open-telemetry/semantic-conventions/pull/3223)
    - rpc.method.name (low-cardinality) and rpc.method.name_orginial (unbounded cardinality) similar to http
      - Should we make it more like HTTP? `Rpc.request.method` ?
    - Opt-in on JSON-RPC because there are no means to have known methods
  - To review: span events [https://github.com/open-telemetry/semantic-conventions/pull/3226](https://github.com/open-telemetry/semantic-conventions/pull/3226)
    - Events will stay experimental and will be able to change to logs in the future

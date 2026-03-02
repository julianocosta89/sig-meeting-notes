## Meeting Notes

### Attendees
- Liudmila
- Trask Stalnaker (Microsoft)
- James Thompson
- Matthew Hensley (Grafana Labs)
- Steve Rao(Alibaba)

### Agenda
- Project board
- Review
  - [https://github.com/open-telemetry/semantic-conventions/issues/2311](https://github.com/open-telemetry/semantic-conventions/issues/2311)
  - [https://github.com/open-telemetry/semantic-conventions/pull/2503](https://github.com/open-telemetry/semantic-conventions/pull/2503)
- Move 2228, 2719 & 2720 to in-progress
  - [https://github.com/open-telemetry/semantic-conventions/pull/2228](https://github.com/open-telemetry/semantic-conventions/pull/2228)
    - Still need to update req level to conditionally required
  - [https://github.com/open-telemetry/semantic-conventions/pull/2719](https://github.com/open-telemetry/semantic-conventions/pull/2719)
    - Let's only add network.protocol.name | version to the common section
    - Let's deprecate `rpc.(client|server).(requests|responses)_per_rpc	and not touch them`
  - [https://github.com/open-telemetry/semantic-conventions/pull/2720](https://github.com/open-telemetry/semantic-conventions/pull/2720)
    - Depends on 2228 (common group)
- Rpc.system -> rpc.framework.name
  - Dubbo over grpc - what rpc.system should be
    - Dubbo is a framework
    - Would we have grpc status codes on dubbo spans?
      - E.g. Client is dubbo, server is grpc
      - Protocol is the same on both sides
      - Frameworks can be different on different sides

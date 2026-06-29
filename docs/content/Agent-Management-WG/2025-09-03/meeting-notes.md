## Meeting Notes

### Attendees
- Dakota Paasman (Bindplane)
- Michel Laterman (Elastic)
- Tigran Najaryan (Splunk)
- Evan Bradley (Dynatrace)
- Andy Keller (Bindplane)
- Jack Peterson (Datadog)

### Agenda
- [Dakota] Supervisor ignoring remote config messages from server
  - Notes: Create an issue for opamp-spec to add a response required in this case and an issue for the supervisor to fix the problem.
- [Dakota] OpAMP websocket heartbeats - was a Ping/Pong pattern considered?
  - [tigran] See [https://github.com/open-telemetry/opamp-spec/issues/28](https://github.com/open-telemetry/opamp-spec/issues/28) and [https://github.com/open-telemetry/opamp-spec/issues/183](https://github.com/open-telemetry/opamp-spec/issues/183)
  - Notes: Create an issue to discuss updating current heartbeats to require a resopnse from the server.

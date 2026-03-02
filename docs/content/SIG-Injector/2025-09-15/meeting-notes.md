## Meeting Notes

### Attendees
- [Antoine Toulme](mailto:atoulme@splunk.com) (Splunk)
- Bastian (Dash0)
- Michele (Dash0)
- Jack (Elastic)

### Agenda
- Discussion of Jack comments on the #otel-injector channel.
  - Operator vs host.
  - [https://cloud-native.slack.com/archives/C09025GKPAL/p1757671295017739](https://cloud-native.slack.com/archives/C09025GKPAL/p1757671295017739)
  - Every language used.
- Ted Young
  - Summit alongside Fosdem Feb 2026
  - Help with dependencies
- Working with SDKs
  - Python is hard
  - Flavors and libraries such as gRPC
- Tests
  - Preinstall and postuninstall.
  - Open an issue for postuninstall checks.
  - End to end tests
    - SDKs can help contribute?
  - Scope of the tests
    - Most time intensive and fragile.
- Packaging effort across OpenTelemetry
  - Previewing the idea of a packaging SIG
- Zig SDK to help with resource detection
  - [https://github.com/zig-o11y/opentelemetry-sdk](https://github.com/zig-o11y/opentelemetry-sdk)

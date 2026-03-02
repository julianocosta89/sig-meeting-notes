## Meeting Notes

### Attendees
- Dakota Paasman (Bindplane)
- Braydon Kains (Google)
- Juande Manjon
- Israel Blancas (Coralogix)
- Tigran Najaryan (Splunk)
- Evan Bradley (Dynatrace)
- Raphael Menderico (Google)
- Michel Laterman (Elastic)
- Antoine Toulme (Splunk)
- Marko Bachvarovski (Grafana Labs)
- Aashish Nehete
- Aunsh Chaudhari (Splunk)

### Agenda
- [braydonk] Discussing the clash between package-managed and opamp-managed Collector updating
- [Juande] [Add REST API to OpAMP Server Example #497](https://github.com/open-telemetry/opamp-go/pull/497)
  - The API exposes programmatic access to connected agents, allowing modern web applications, CLI tools, and third-party clients to interact seamlessly with the OpAMP server.
  - Do we need opamp-contrib?
- [Michel] [example agent scale test mode pr](https://github.com/open-telemetry/opamp-go/pull/481) ready for review
  - [Example server metrics has been split into a separate pr](https://github.com/open-telemetry/opamp-go/pull/499/)
- [Tigran] Change SIG call day/time: [https://github.com/open-telemetry/community/pull/3231](https://github.com/open-telemetry/community/pull/3231)
- [Israel] Proposal: add CrashDiagnostics field to ComponentHealth [https://github.com/open-telemetry/opamp-spec/issues/277](https://github.com/open-telemetry/opamp-spec/issues/277)
- [Antoine] Discuss opampsupervisord [https://github.com/open-telemetry/opentelemetry-collector-contrib/pull/45100](https://github.com/open-telemetry/opentelemetry-collector-contrib/pull/45100)

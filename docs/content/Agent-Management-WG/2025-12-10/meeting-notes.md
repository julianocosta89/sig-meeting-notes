## Meeting Notes

### Attendees
- [Jade Guiton](mailto:jade.guiton@datadoghq.com) (Datadog)
- Tigran Najaryan (Splunk)
- Andy Keller (Bindplane)
- Juande Manjon
- Evan Bradley (Dynatrace)
- Dakota Paasman (Bindplane)
- Michel Laterman (Elastic)

### Agenda
- [Jade] Advice on detecting or gracefully dealing with duplicate UIDs with HTTP transport
  - → Duplicate UIDs are a real problem in production. Best option is a heuristic that “fingerprints” Agents based on IP/attributes
- [Jade] Advice on enforcing HTTP polling intervals for TTLs and active agent detection
  - → Simplest option is just setting a fixed TTL. Otherwise, a long TTL can be set for the first message, and a more precise one can be inferred from later messages.
- [Juande] [Feature Request: Official Docker image for OpAMP server #443](https://github.com/open-telemetry/opamp-go/issues/443)
  - [PR473 in review](https://github.com/open-telemetry/opamp-go/pull/473) I had addressed Tigran feedback
- [Juande] Open issue [Add CustomMessages demo to server and agent examples #468](https://github.com/open-telemetry/opamp-go/issues/468)
- [Juande] Open spec issue [Add schema_version field to CustomMessage for fine-grained data schema versioning](https://github.com/open-telemetry/opamp-spec/issues/276)
  - Enables fine-grained, per-message data schema versioning within a single capability, allowing multiple schema versions to coexist without requiring separate capability declarations.
  - This decouples capability evolution (adding/removing message types) from data schema evolution (changing message formats), enabling each to evolve independently and simplifying version management for custom capabilities.

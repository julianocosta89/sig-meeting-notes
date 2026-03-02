## Meeting Notes

### Attendees
- Josh Suereth
- Laurent Querel
- Jeremy Blythe
- Arianna Vespri
- Liudmila Molkova

### Agenda
- [Liudmila] Live-check for OTel instrumentations - prototype and feedback [https://github.com/open-telemetry/weaver/issues/1100](https://github.com/open-telemetry/weaver/issues/1100)
- [Liudmila] Schema v2 OTEP draft ([https://github.com/open-telemetry/opentelemetry-specification/pull/4815](https://github.com/open-telemetry/opentelemetry-specification/pull/4815))  questions:
  - Schemas: [https://github.com/open-telemetry/weaver/pull/1106](https://github.com/open-telemetry/weaver/pull/1106)
  - Would appreciate help with importing
    - https://github.com/lmolkova/opentelemetry-specification/blob/2c6366cbfc2c1c3dc284bd42bbad38f25b6e9cc4/oteps/4815-semantic-conventions-schema-v2.md#do-we-need-to-talk-about-importing-and-decentralization-in-details
  - We should expect resolved schema to be provided in `--registry`  and `--baseline-registry` and should heavily optimize for it (no resolution, no validation beyond deserialization)
    - We should support `weaver registry * -r http://otel.io/schemas/schema-vfuture.tar.gz ...` (suboptimal) and `weaver registry diff -r ./path/to/resolved/vfuture/schema.yaml`
- [jeremy] How do we unblock this schemars PR?: [https://github.com/open-telemetry/weaver/pull/1048](https://github.com/open-telemetry/weaver/pull/1048)
  - AI - Looks like we can just drop OrderedFloat library
- [jeremy] MCP Server: [https://github.com/open-telemetry/weaver/pull/1113](https://github.com/open-telemetry/weaver/pull/1113)
- [suereth] Doc Agent Demos - What do we think?
  - [https://github.com/open-telemetry/weaver/pull/1116](https://github.com/open-telemetry/weaver/pull/1116)
  - [https://github.com/open-telemetry/weaver/pull/1102](https://github.com/open-telemetry/weaver/pull/1102)
- [suereth] package-lock.json - Stability and tooling requirements

## Meeting Notes

### Attendees
- [late, 5-10min] Josh S
- Laurent Querel
- Jeremy Blythe
- Arianna Vespri
- Arthur Sens (for the first 30 mins)
- Liudmila

### Agenda
- [arthur] Do we want Weaver live-check in collector?
  - Arianna prototype using Test Containers - runs live check *beside* collector
    - This is for testing the collector itself
    - [https://github.com/open-telemetry/opentelemetry-collector-contrib/pull/46315](https://github.com/open-telemetry/opentelemetry-collector-contrib/pull/46315)
  - JMacD prototype using WASM - a receiver for the collector, loads rust as WASM.
  - Rewrite live-check in Go?
  - [https://github.com/open-telemetry/opentelemetry-weaver-examples/blob/main/emit_otlp_logs/README.md](https://github.com/open-telemetry/opentelemetry-weaver-examples/blob/main/emit_otlp_logs/README.md)
  - OTAP weaver policy - [https://github.com/open-telemetry/otel-arrow/blob/5b0912579fa9871a40a5e9a87fd23dfb139fa277/rust/otap-dataflow/docs/telemetry/README.md?plain=1#L178](https://github.com/open-telemetry/otel-arrow/blob/5b0912579fa9871a40a5e9a87fd23dfb139fa277/rust/otap-dataflow/docs/telemetry/README.md?plain=1#L178)
  - Weaver "samples" would need to be made external/public interface / schema.
- [jeremy] What happened to this? [https://github.com/open-telemetry/weaver/pull/978](https://github.com/open-telemetry/weaver/pull/978) - we need to be able to fetch securely from various hosted locations for internal / private.
  - Any url that doesn't end in `.zip` is assumed to be a git repo, and you can use git auth settings to pull published repos.
  - Would be better if we can pull artifacts/zips via `http` with non-git auth.
  - [https://github.com/open-telemetry/weaver/issues/1344](https://github.com/open-telemetry/weaver/issues/1344) added to “to be considered…” in the project
- [josh] Provenance, lineage, next steps - [https://github.com/open-telemetry/weaver/pull/1313](https://github.com/open-telemetry/weaver/pull/1313)
  - What to add in weaver forge?
    - Make sure schema_url + path show up.
  - Do we need any other lineage tracking?
    - Can add things later.
    - We think removing some information here is fine, and desired.
- [josh] FYI - weaver-packages build fix - [https://github.com/open-telemetry/opentelemetry-weaver-packages/pull/27](https://github.com/open-telemetry/opentelemetry-weaver-packages/pull/27)
- [liudmila] v2 OTEP: do we need publication manifest at all? Can we just publish resolved schema (with extra props in the future for additional schemas)

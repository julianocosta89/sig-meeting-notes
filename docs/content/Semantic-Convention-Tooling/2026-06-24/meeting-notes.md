## Meeting Notes

### Attendees
- Josh Suereth
- Liudmilla
- Arianna (last 45 mins)

### Agenda
- [suereth] Release Process
  - We need to validate weaver packages on release - [https://github.com/open-telemetry/opentelemetry-weaver-packages/actions/runs/27922764515/job/82619298487?pr=37](https://github.com/open-telemetry/opentelemetry-weaver-packages/actions/runs/27922764515/job/82619298487?pr=37)
- [suereth] Resolver next steps
  - [https://github.com/open-telemetry/weaver/pull/1504](https://github.com/open-telemetry/weaver/pull/1504)
  - Next Steps
    - Rebase - [https://github.com/open-telemetry/weaver/pull/1442](https://github.com/open-telemetry/weaver/pull/1442)
    - Add `dependencies` to forge schema and pull from Cache
      - After this need to figure out how to do codegen such that semconv package dependency leads to code package dependency
    - Handle diamond-dependency version conflict resolution
    - <future> Weaver live-check dynamically pulling in SchemaUrl / using registry defined by schema-url when checking telemetry.
    - V2 - handling forward compatibility
    - doc generation - URL for schemas / overrides.
- [suereth] Definition Manifest vs. Published Manifest
  - What should "schema_url" be for definition?

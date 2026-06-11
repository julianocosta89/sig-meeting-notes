## Meeting Notes

### Attendees
- Arianna
- Liudmila
- Jeremy
- Josh

### Agenda
- Requirement level for all signals [https://github.com/open-telemetry/weaver/issues/1484](https://github.com/open-telemetry/weaver/issues/1484)
  - AI: Liudmila to revert metric req level since we're going to break it
- UI in docker, connection refused, Josh will take a look
  - No test
  - Playwright test suite
    - AI: Jeremy
- Release
  - A few small issues to resolve
  - And we should release ASAP
- [suereth] Multi-Dependencies
  - A few large decisions
    - Updating "Resolver" to be a major component
      - Allow taking a `schema_url` and resolving a registry of it.
      - Caching previously seen `schema_url`s
      - Allowing `live-check` to pull in schemaurl dynamically
      - Major decisions
        - Should this be concurrent friendly?
        - Should we use Async?
        - Should we have a blocking / simple core - and wrap it for live-check?
    - "Template" Schema decisions
      - Tentative: include additional resolved schemas -
      - *only* resolved dependencies show up, *one* version per name.
- [suereth] Using `package` on semantic-conventions?
  - It's missing `manifest.yaml` today.

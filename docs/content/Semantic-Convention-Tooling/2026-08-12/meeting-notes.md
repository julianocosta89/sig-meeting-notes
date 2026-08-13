## Meeting Notes

### Attendees
- Jeremy
- Arianna
- Josh S
- Liudmila

### Agenda
- [Jeremy] What scope do we want for this PR? It’s growing. [https://github.com/open-telemetry/weaver/pull/1684](https://github.com/open-telemetry/weaver/pull/1684)
  - Part 1 - Issue warning/error if `entity-ref` refers to an entity that cannot be found
  - **Part 2 - Weaver Resolved Schema - EntityRef should keep provenance**
  - Part 3 - We should fix "expansion helpers" for finding Entity in various places
    - Live-Check would look up entities and make sure they're available for rego polices
    - Jinja template helper to lookup entity by ref in current schema/dependencies
    - Rego helper to lookup entity by ref in current schema/dependencies
  - Fix #1 - imports would silently fail if you had a typo
  - Fix #2 (josh) - Get schema_url repository override config into weaver.toml and improve test suite.
- [Arianna] Just started working on this [https://github.com/open-telemetry/weaver/issues/970](https://github.com/open-telemetry/weaver/issues/970)
  - just V2 for now
  - for `ref` should have provenance.

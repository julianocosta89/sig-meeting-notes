## Meeting Notes

### Attendees
- Josh Suereth
- Laurent Querel
- Liudmila Molkova
- Arianna Vespri

### Agenda
- [suereth] What do we want before release?
  - live-check /health
  - Unified output handling
  - registry infer
  - Weaver Packages work
    - git reference
  - v2 syntax "beta"?
    - v2 refinements working in definition syntax (caveat events)
    - schema_url for manifests
    - Replace version: "2" with file_format: definition/2
    - Add weaver registry package
  - Need to fix resolution bugs.
    - Issue with imports and re-exporting.
- [suereth] Lineage in V2 - [https://github.com/open-telemetry/weaver/pull/1277](https://github.com/open-telemetry/weaver/pull/1277)
  - Quick sketch
    - Add dependencies (list of schema_url) in resolved schema.
    - SignalLineage
      - Uses `Provenance`
        - Has data file, but does not serialize it to resolved schema.
        - Has SchemaURL - but uses a "dictionary lookup" on resolved schema.
    - AttributeLineage
      - On attributes in catalog
      - Similar shape to SignalLineage - just provenance for now.
- [suereth] [https://github.com/open-telemetry/weaver/pull/1260](https://github.com/open-telemetry/weaver/pull/1260) - Ready to merge?
  - We need to work through the ideas.  Liudmilla has good idea around manifest having policy definitions, e.g.
- [suereth] Agent instructions to fix renovate version bump issues - [https://github.com/open-telemetry/weaver/pull/1269](https://github.com/open-telemetry/weaver/pull/1269)

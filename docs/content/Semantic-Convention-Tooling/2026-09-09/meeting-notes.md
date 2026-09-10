## Meeting Notes

### Attendees
- Jeremy Blythe
- Liudmila Molkova
- Laurent Querel

### Agenda
- [suereth] Fixes to cargo dist?
  - [https://github.com/open-telemetry/weaver/issues/1746](https://github.com/open-telemetry/weaver/issues/1746) - Check github attestations when installing weaver.
  - Add validation to cargo–dist as a explicit config step, not a hackery workaround
  - [lmolkova] There's open bug we could focus on:
    - [https://github.com/axodotdev/cargo-dist/issues/2420](https://github.com/axodotdev/cargo-dist/issues/2420)
  - [jerbly] We're still using ugly "patch after regenerate" for cargo-dist - we need to fix that.
    - version-locking
    - privileges for steps
- [suereth] V2 stabilization and manifest
  - File Name differences
    - **registry_manifest.yaml -gives access to name/version deprecated fields.**
    - manifest.yaml
  - File Format
    - manfiest/2.0.0
    - *definition_manifest/2.0.0*
    - **<empty>**
  - Strawman proposal
    - **Filename - registry_manifest.yaml** - ALWAYS parses as V1
    - Filename is manifest.yaml
      - `manifest/2.0.0` - ALWAYS published manifest.
      - `definition_manifest/2.0.0` - ALWAYS V2 definition manifest
      - **<empty> - Assumed to always be definition V1 manifest -> Make this V2**
- [jerbly] Live-check Matchers - semconv v2 compatibility - [https://github.com/open-telemetry/weaver/pull/1721](https://github.com/open-telemetry/weaver/pull/1721)
- [laurent] [crates.io](http://crates.io) ?
- [laurent] annotation conventions?
- [liudmila]

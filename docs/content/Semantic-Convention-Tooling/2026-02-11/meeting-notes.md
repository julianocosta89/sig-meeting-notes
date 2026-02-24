## Meeting Notes

### Attendees
- Josh Suereth
- Arianna Vespri
- Laurent Querel
- Jeremy Blythe

### Agenda
- [josh / liudmila] multi-registry manifests / dependency conflicts / naming  [https://github.com/open-telemetry/weaver/issues/1197](https://github.com/open-telemetry/weaver/issues/1197)
- [liudmila] `file_format: definition/2` vs `version: "2"` [https://github.com/open-telemetry/weaver/pull/1154](https://github.com/open-telemetry/weaver/pull/1154)
  - Give up on semver here - not helpful
  - Support version: "2" too
- [josh] Next steps on V2 syntax
  - Refinements
  - Imports
- [josh] Do we like the doc bot?
  - [https://github.com/open-telemetry/weaver/pull/1190](https://github.com/open-telemetry/weaver/pull/1190)
  - *We don't have good end-to-end tests for the bot to use.*
  - Update instructions
    - Don't include how Rust names things
    - use `--v2` syntax for all new docs.
  - Close the current PR - Reopen with same prompt once manifest changes land with better end-to-end integration tests.
- [https://github.com/open-telemetry/weaver/projects?query=is%3Aopen](https://github.com/open-telemetry/weaver/projects?query=is%3Aopen)

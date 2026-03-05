## Meeting Notes

### Attendees
- Jeremy Blythe
- Laurent Querel
- Arianna Vespri
- Liudmila Molkova

### Agenda
- [Jeremy] Dog-fooding PR, good to go? Or do we want to move generation outside of the crate? [https://github.com/open-telemetry/weaver/pull/1232](https://github.com/open-telemetry/weaver/pull/1232)
  - AIs
    - Figure out the "bootstrap" issue - can we build weaver if the weaver build is broken? How do we pin to a stable version?
    - Can we allow users to provide a schema_url? - probably non-blocking
    - We should NOT allow xtask to depend on weaver itself… or find a way to keep this healthy
    - How many "schemas" should weaver have? ONE
- [Liudmila] Registry package [https://github.com/open-telemetry/weaver/pull/1254](https://github.com/open-telemetry/weaver/pull/1254)
  - Followed up with deprecating resolve [https://github.com/open-telemetry/weaver/pull/1255](https://github.com/open-telemetry/weaver/pull/1255)
  - Let's figure out names of `file-format` and have a separate one for definition manifest vs. published manifest.
  - let's move weaver registry json-schema eventually
- [Liudmila] Docs-related improvements (trivial):
  - Resolved json schema - [https://github.com/open-telemetry/weaver/pull/1261](https://github.com/open-telemetry/weaver/pull/1261)
  - Add file_format to definition JSON schema v2 [https://github.com/open-telemetry/weaver/pull/1262](https://github.com/open-telemetry/weaver/pull/1262)
- [Jeremy] Package vs Project config proposal: [https://github.com/open-telemetry/weaver/pull/1260](https://github.com/open-telemetry/weaver/pull/1260)
- [suereth] Refinements [https://github.com/open-telemetry/weaver/pull/1250](https://github.com/open-telemetry/weaver/pull/1250)

## Meeting Notes

### Attendees
- Josh Suereth
- Laurent Querel
- Liudmila Molkova
- Jeremy Blythe

### Agenda
- [suereth] SchemaURL instead of registry id - [https://github.com/open-telemetry/weaver/pull/1298](https://github.com/open-telemetry/weaver/pull/1298)
- [suereth] lineage discussions
  - Dictionary of schema_urls / schemas that were used in the resolved_schema
  - Lineage becomes an index into that dictionary for the SchemaUrl part.
  - For example:
  - v2-resolved-registry.yaml
  - dependency: 0 # This only exists if the attribute came from a dependency
- [suereth] Filter playground and future of weaver serve
  - [https://github.com/open-telemetry/weaver/pull/1299](https://github.com/open-telemetry/weaver/pull/1299)
  - UI Is bugging right now
    - We should add some automated tests to verify it.
  - weaver serve allowing multiple registries pulled in (same w/ live check)
  - Future of MCP
    - -> skills/
      - [SKILL.md](http://SKILL.md) that describes how to use weaver cli / serve etc. to get information
      - Dump weaver itself or describe how to download it.
    - Jeremy is using SKILLS w/ MCP.
    - If CLI is fast enough, w/ cache, can we just re-invoke the CLI repeatedly for this instead of a `weaver serve`.
    - MCP server w/ state offers some interesting properties - We may struggle with this otherwise.  Would CLI need to be updated to have a transitory state?
    - Next steps
      - Let's try a CLI-only skill
      - Let's try a API+CLI-only skill
      - Let's decide on MCP, API, CLI after toying.
- [liudmila] Docs pr - [https://github.com/open-telemetry/weaver/pull/1106](https://github.com/open-telemetry/weaver/pull/1106)

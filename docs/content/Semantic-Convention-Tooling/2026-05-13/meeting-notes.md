## Meeting Notes

### Attendees
- Josh Suereth
- Jeremy Blythe
- Liudmila Molkova

### Agenda
- [Liudmila] Conflict resolution
  - GenAI moving out - two copies of everything
  - [https://github.com/open-telemetry/weaver/pull/1377](https://github.com/open-telemetry/weaver/pull/1377)
  - [josh] Whether to "import all" in a downstream registry.
  - Decision -
    - We can add some kind of "visibility: local" or "dependency_resolution: ignore" annotation so that we do NOT provide these when looking up "dependency" attributes / groups.
- Forward compatibility:
  - Resolved & manifest - [https://github.com/open-telemetry/weaver/pull/1365](https://github.com/open-telemetry/weaver/pull/1365)
  - Definition [https://github.com/open-telemetry/weaver/pull/1422](https://github.com/open-telemetry/weaver/pull/1422)

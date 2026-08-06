## Meeting Notes

### Attendees
- Jeremy
- Josh
- Liudmila
- Laurent

### Agenda
- [Jeremy] Live-check v2 for multi-registry (more than one) is broken:
  - Issue with fix options:  [https://github.com/open-telemetry/weaver/issues/1658](https://github.com/open-telemetry/weaver/issues/1658)
  - PR with failing tests ready to fix: [https://github.com/open-telemetry/weaver/pull/1665](https://github.com/open-telemetry/weaver/pull/1665)
  - Fix #1 - use signal to determine key attributes (@jeremy)
  - Fix #2 - Finish having dependencies in Forge schema (@josh)
  - CI against semconv and weaver examples
- [josh] Follow-up on multi-dependency bugs
  - Next step - clean up / improve integration tests.

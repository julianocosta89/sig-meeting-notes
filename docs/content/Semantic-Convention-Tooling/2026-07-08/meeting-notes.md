## Meeting Notes

### Attendees
- Josh
- Liudmilla
- Jeremy
- Joao

### Agenda
- Parallelization failures of unit tests
  - Onto third attempt to fix these
  - AI - jsuereth - Fix up test so that we split forge helper method - 1 which is not safe for parallel execution/reuse and 1 which is fine.
- Dependency Resolution
  - Discussion on resolved schema format.
  - Going to keep v2 schema as-is
  - Will add `dependencies` section to forge schema.
- [joao] If time allows, discuss v2 migration in semconv
  - What are the problems we're working on.
  - Folks are migrating definitions first
  - Let's migrate v2 *output* first.

## Meeting Notes

### Attendees
- Xuan Cao
- Matt Wear
- Hannah Ramadan
- Kayla Reopelle

### Agenda
- [Spec SIG](https://docs.google.com/document/d/1pdvPeKjA8v8w_fGKAN68JjWBmVJtPCpqdi9IZrd6eEo/preview) Update (max 15 min)
- Core ([Issues](https://github.com/open-telemetry/opentelemetry-ruby/issues) / [PRs](https://github.com/open-telemetry/opentelemetry-ruby/pulls))
  - [kayla] Declarative Configuration - Some questions about behavior so far
- Contrib ([Issues](https://github.com/open-telemetry/opentelemetry-ruby-contrib/issues) / [PRs](https://github.com/open-telemetry/opentelemetry-ruby-contrib/pulls))
  - From Slack: Should our appraisals use = instead of ~> for versioning to avoid unexpected failures on patch releases? (CI general feedback too)
    - Specific Q: Nothing should break in theory on a patch. Should be rare, when it happens we want to know and have it be our fault.
    - Both will work, no strong feelings
- Auto Instrumentation ([Issues](https://github.com/open-telemetry/opentelemetry-ruby-instrumentation/issues) / [PRs](https://github.com/open-telemetry/opentelemetry-ruby-instrumentation/pulls))
- Burning questions?
- The spec allows INTERNAL for "in-memory" databases
- Recommends CLIENT when the DB "runs in a different process" or is reached over a protocol.
- LMDB is neither, it's on disk, and in-process. Both options could be right.
- ✨ Happy Reports ✨

## Meeting Notes

### Attendees
- Hannah Ramadan
- Kayla Reopelle
- Wendy Smoak
- Daniel Azuma

### Agenda
- [Spec SIG](https://docs.google.com/document/d/1pdvPeKjA8v8w_fGKAN68JjWBmVJtPCpqdi9IZrd6eEo/preview) Update (max 15 min)
- Core ([Issues](https://github.com/open-telemetry/opentelemetry-ruby/issues) / [PRs](https://github.com/open-telemetry/opentelemetry-ruby/pulls))
  - ​​api version numbers:
    - (wendy) If it’s a problem, just make the breaking change clear in the release notes
- Contrib ([Issues](https://github.com/open-telemetry/opentelemetry-ruby-contrib/issues) / [PRs](https://github.com/open-telemetry/opentelemetry-ruby-contrib/pulls))
  - Renaming sql-obfuscation -> sql-processor. PRs opening soon!
    - [feat: intro sql-processor](https://github.com/open-telemetry/opentelemetry-ruby-contrib/pull/1673)
    - [feat!: deprecate sql-obfuscation gem](https://github.com/open-telemetry/opentelemetry-ruby-contrib/pull/1674)
    - [feat: introduce sql-processor gem](https://github.com/open-telemetry/opentelemetry-ruby-contrib/pull/1675)
    - Will test out post-install message
    - Working on a few more things, but almost ready
    - Will look at collector-contrib repo for examples of deprecation/removal of libraries
    - Consider that this is an internal dependency of some well-used instrumentation; what would create appropriate concern?
- Burning questions?
- ✨ Happy Reports ✨

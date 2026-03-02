## Meeting Notes

### Attendees
- Eric Mustin
- Arjun Rajappa
- Wendy Smoak
- Xuan Cao
- Hannah Ramadan

### Agenda
- [Spec SIG](https://docs.google.com/document/d/1pdvPeKjA8v8w_fGKAN68JjWBmVJtPCpqdi9IZrd6eEo/preview) Update (max 15 min)
- Core ([Issues](https://github.com/open-telemetry/opentelemetry-ruby/issues) / [PRs](https://github.com/open-telemetry/opentelemetry-ruby/pulls))
  - ​​[https://github.com/open-telemetry/opentelemetry-ruby/pull/1917](https://github.com/open-telemetry/opentelemetry-ruby/pull/1917)
- Contrib ([Issues](https://github.com/open-telemetry/opentelemetry-ruby-contrib/issues) / [PRs](https://github.com/open-telemetry/opentelemetry-ruby-contrib/pulls))
  - [https://github.com/open-telemetry/opentelemetry-ruby-contrib/pull/1660/files](https://github.com/open-telemetry/opentelemetry-ruby-contrib/pull/1660/files)
    - Seems like a valid use case we ought to support, will add a comment asking for clarification and will investigate async
- Burning questions?
  - Discussion: thoughts on renaming sql-obfuscation gem -> sql-processor
    - This is a supported idea. The gem is used mostly internally anyways, it likely wouldn’t be an issue for users. It is good to get names set up for long term, flexible use. We would need to ensure that this change is publicized and also check existing docs that point to the old gem name.
- ✨ Happy Reports ✨

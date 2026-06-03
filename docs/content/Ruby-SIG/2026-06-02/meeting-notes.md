## Meeting Notes

### Attendees
- Bart de Water
- Hannah Ramadan
- Kayla Reopelle
- Arjun Rajappa
- Xuan Cao

### Agenda
- [Spec SIG](https://docs.google.com/document/d/1pdvPeKjA8v8w_fGKAN68JjWBmVJtPCpqdi9IZrd6eEo/preview) Update (max 15 min)
- Core ([Issues](https://github.com/open-telemetry/opentelemetry-ruby/issues) / [PRs](https://github.com/open-telemetry/opentelemetry-ruby/pulls))
  - ​​[Xuan] [https://github.com/open-telemetry/opentelemetry-ruby/pull/2158/changes](https://github.com/open-telemetry/opentelemetry-ruby/pull/2158/changes)
    - Having three separate exporter gems can cause discrepancies between common functions that could be shared
    - It’s an extra burden for the maintainer
    - Xuan will open an issue for the refactor plan
    - Kayla will release the code with these fixes
- Contrib ([Issues](https://github.com/open-telemetry/opentelemetry-ruby-contrib/issues) / [PRs](https://github.com/open-telemetry/opentelemetry-ruby-contrib/pulls))
  - [Bart] [https://github.com/open-telemetry/opentelemetry-ruby-contrib/pull/2361](https://github.com/open-telemetry/opentelemetry-ruby-contrib/pull/2361)
    - Please take a look!
    - Relates to: [Move active_job out of messaging domain #2368](https://github.com/open-telemetry/opentelemetry-ruby-contrib/issues/2368)
    - Should the attributes remain under the messaging domain or move to a Rails domain? What does the process look like?
    - Leaning toward keeping things consistent for now (using the `messaging.*` prefix), but need to look more closely at the artifacts
- Burning questions?
  - Kayla request to change renovate PRs to a monthly cadence (2x thumbs up)
    - Kayla will open a PR to do that
- ✨ Happy Reports ✨
  - opentelemetry-ruby-instrumentation repo is almost ready for auto-instrumentation

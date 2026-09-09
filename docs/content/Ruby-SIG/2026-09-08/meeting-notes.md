## Meeting Notes

### Attendees
- [Josef Šimánek](mailto:josef.simanek@gmail.com)
- Xuan Cao
- Matt Wear

### Agenda
- [Spec SIG](https://docs.google.com/document/d/1pdvPeKjA8v8w_fGKAN68JjWBmVJtPCpqdi9IZrd6eEo/preview) Update (max 15 min)
- Core ([Issues](https://github.com/open-telemetry/opentelemetry-ruby/issues) / [PRs](https://github.com/open-telemetry/opentelemetry-ruby/pulls))
  - ~~Metrics and Logs Stabilization Process~~
    - ~~Link to metrics milestone (TBD)~~
    - ~~Link to logs milestone (TBD)~~
    - ~~How do we divide up the work? Work on both simultaneously?~~
    - ~~Timeline goals for completion~~ (kayla out sick today, will present next week)
  - Maintaining otlp proto types [james]
    - Are we ok to switch to new code generation style? See diff in [https://github.com/open-telemetry/opentelemetry-ruby/actions/runs/33965569461/job/101304980459#step:9:1](https://github.com/open-telemetry/opentelemetry-ruby/actions/runs/33965569461/job/101304980459#step:9:1)
    - Pr will automate updates & releases the same as semantic conventions. Note Is dedicated gem due to lack of protobuf support on jruby
    - Matt and Xuan will try to review this week
- Contrib ([Issues](https://github.com/open-telemetry/opentelemetry-ruby-contrib/issues) / [PRs](https://github.com/open-telemetry/opentelemetry-ruby-contrib/pulls))
  - Ruby version release toys should be using? [james]
    - Should it be latest or min we support. Currently it is latest.
    - PR to use common version definition is [https://github.com/open-telemetry/opentelemetry-ruby-contrib/pull/2562](https://github.com/open-telemetry/opentelemetry-ruby-contrib/pull/2562)
    - Latest, if it works. If we have questions we should ping Daniel Azuma.
  - Only emit stable http [james]
    - Are happy with commencing Only stable Http instrumentation aka [https://github.com/open-telemetry/opentelemetry-ruby-contrib/issues/1650](https://github.com/open-telemetry/opentelemetry-ruby-contrib/issues/1650)
    - Most likely, but let’s confirm at next week’s SIG meeting
- Auto Instrumentation ([Issues](https://github.com/open-telemetry/opentelemetry-ruby-instrumentation/issues) / [PRs](https://github.com/open-telemetry/opentelemetry-ruby-instrumentation/pulls))
- Burning questions?
- ✨ Happy Reports ✨

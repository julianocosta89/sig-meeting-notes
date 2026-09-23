## Meeting Notes

### Attendees
- Robb Kidd
- Xuan Cao
- Ted Young

### Agenda
- [Spec SIG](https://docs.google.com/document/d/1pdvPeKjA8v8w_fGKAN68JjWBmVJtPCpqdi9IZrd6eEo/preview) Update (max 15 min)
- Core ([Issues](https://github.com/open-telemetry/opentelemetry-ruby/issues) / [PRs](https://github.com/open-telemetry/opentelemetry-ruby/pulls))
  - [xuan] [https://github.com/open-telemetry/opentelemetry-ruby/pull/2388](https://github.com/open-telemetry/opentelemetry-ruby/pull/2388) (may need to wrap this up soon since it will affect people who want to mutate span metadata before on_finish (e.g. on_finishing)
- Contrib ([Issues](https://github.com/open-telemetry/opentelemetry-ruby-contrib/issues) / [PRs](https://github.com/open-telemetry/opentelemetry-ruby-contrib/pulls))
- Auto Instrumentation ([Issues](https://github.com/open-telemetry/opentelemetry-ruby-instrumentation/issues) / [PRs](https://github.com/open-telemetry/opentelemetry-ruby-instrumentation/pulls))
- Burning questions?
- ✨ Happy Reports ✨
- [Ted] What about binding to C++?
- [Ted] How are metrics and logs coming along?
  - Would a C++ binding save some time at this point?
- [Ted] How dangerous are Ruby OTel dependencies?
  - For auto-injection, we can’t have things blowing up
    - Spec proposal for auto-injection criteria
      - [https://github.com/open-telemetry/opentelemetry-specification/pull/5308](https://github.com/open-telemetry/opentelemetry-specification/pull/5308)
  - Can we “vendor” dependencies in a way that avoids this?
  - Can we hand-roll our proto dependency if that one is causing problems?
    - That’s gone very well in Node, Python, and Java.

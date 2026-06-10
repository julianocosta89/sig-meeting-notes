## Meeting Notes

### Attendees
- Matt Wear
- Xuan Cao
- Hannah Ramadan
- Bart de Water
- Kayla Reopelle

### Agenda
- [Spec SIG](https://docs.google.com/document/d/1pdvPeKjA8v8w_fGKAN68JjWBmVJtPCpqdi9IZrd6eEo/preview) Update (max 15 min)
  - Arrow presentation slides: [https://docs.google.com/presentation/d/1D-KN-ro2CllAUdx3zj5XF38sR4mcvrLgjLbx6MM4_FA/edit?slide=id.g3ea705bd2f3_0_30&pli=1#slide=id.g3ea705bd2f3_0_30](https://docs.google.com/presentation/d/1D-KN-ro2CllAUdx3zj5XF38sR4mcvrLgjLbx6MM4_FA/edit?slide=id.g3ea705bd2f3_0_30&pli=1#slide=id.g3ea705bd2f3_0_30)
- Core ([Issues](https://github.com/open-telemetry/opentelemetry-ruby/issues) / [PRs](https://github.com/open-telemetry/opentelemetry-ruby/pulls))
  - ​​PTAL: [https://github.com/open-telemetry/opentelemetry-ruby/pull/2080](https://github.com/open-telemetry/opentelemetry-ruby/pull/2080)
  - PTAL: [https://github.com/open-telemetry/opentelemetry-ruby/issues/2170](https://github.com/open-telemetry/opentelemetry-ruby/issues/2170)
  - [https://github.com/open-telemetry/opentelemetry-ruby/issues/2162](https://github.com/open-telemetry/opentelemetry-ruby/issues/2162)
    - Look at self-observability project to compare with this proposal
    - When self-observability goes stable, we should probably remove the unspec’d metrics reporter
    - What’s the timeline for the self-observability project?
- Contrib ([Issues](https://github.com/open-telemetry/opentelemetry-ruby-contrib/issues) / [PRs](https://github.com/open-telemetry/opentelemetry-ruby-contrib/pulls))
  - [https://github.com/open-telemetry/opentelemetry-ruby-contrib/pull/2361/](https://github.com/open-telemetry/opentelemetry-ruby-contrib/pull/2361/)
    - Sticking point is the attribute names
    - Naming things is hard
    - Look at the other language SIGs to see what they’re doing
    - See if we have full license to introduce a rails or active job namespace for things
    - If that seems like a permitted route, then doing that makes a lot of sense for a lot of things
    - Matt will try to look at some other implementations this week and will report back at the next SIG what he finds
    - Kayla will add comment to the PR summarizing SIG discussion
    - Bart will update PR to switch back to the messaging namespace
- Burning questions?
  - auto-instrumentation repo: [https://github.com/open-telemetry/opentelemetry-ruby-instrumentation](https://github.com/open-telemetry/opentelemetry-ruby-instrumentation)
  - See contrib original PR if you have questions
- ✨ Happy Reports ✨

## Meeting Notes

### Attendees
- Xuan Cao
- Matt Wear
- Bart de Water
- Kayla Reopelle

### Agenda
- **Canceled next week for KubeCon**
- [Spec SIG](https://docs.google.com/document/d/1pdvPeKjA8v8w_fGKAN68JjWBmVJtPCpqdi9IZrd6eEo/preview) Update (max 15 min)
  - [https://github.com/open-telemetry/opentelemetry-specification/pull/5378](https://github.com/open-telemetry/opentelemetry-specification/pull/5378)
  - [https://github.com/open-telemetry/opentelemetry-specification/pull/5399](https://github.com/open-telemetry/opentelemetry-specification/pull/5399)
  - [https://github.com/open-telemetry/opentelemetry-configuration/pull/798](https://github.com/open-telemetry/opentelemetry-configuration/pull/798)
- Core ([Issues](https://github.com/open-telemetry/opentelemetry-ruby/issues) / [PRs](https://github.com/open-telemetry/opentelemetry-ruby/pulls))
  - Continued reviews on Metrics PRs
  - Will add a comment to the Ractors PR
  - [https://github.com/open-telemetry/opentelemetry-ruby/pull/2464](https://github.com/open-telemetry/opentelemetry-ruby/pull/2464)
    - Do we want to wait for the full implementation, or release with warnings and update as things get merged?
    - We’ll keep the PR open until we meet post-Kubecon and if related PRs aren’t merged by then, we’ll merge this PR
- Contrib ([Issues](https://github.com/open-telemetry/opentelemetry-ruby-contrib/issues) / [PRs](https://github.com/open-telemetry/opentelemetry-ruby-contrib/pulls))
  - Debugging recently and could have used the IP address to help resolve the issue more quickly. These PRs add it:
    - [https://github.com/open-telemetry/opentelemetry-ruby-contrib/pull/2667](https://github.com/open-telemetry/opentelemetry-ruby-contrib/pull/2667)
    - [https://github.com/open-telemetry/opentelemetry-ruby-contrib/pull/2666](https://github.com/open-telemetry/opentelemetry-ruby-contrib/pull/2666)
  - Net::HTTP metrics - Will merge without semconv changes, can update later on
- Auto Instrumentation ([Issues](https://github.com/open-telemetry/opentelemetry-ruby-instrumentation/issues) / [PRs](https://github.com/open-telemetry/opentelemetry-ruby-instrumentation/pulls))
  - [https://github.com/open-telemetry/opentelemetry-ruby-instrumentation/pull/142](https://github.com/open-telemetry/opentelemetry-ruby-instrumentation/pull/142) - to support alpine docker images
  - [https://github.com/open-telemetry/opentelemetry-ruby-instrumentation/pull/39](https://github.com/open-telemetry/opentelemetry-ruby-instrumentation/pull/39) - xuan will take one last look today
- Burning questions?
  - Trouble with co-pilot on OTel repos, ‘unavailable per opentelemetry policy’
    - Kayla will look into this
- ✨ Happy Reports ✨

## Meeting Notes

### Attendees
- Eric Mustin
- Hannah Ramadan
- Xuan Cao
- Arjun Rajappa
- Wendy Smoak
- Kayla Reopelle

### Agenda
- ***Small update – posted on GH issues with tags to people rather than Slack (kayla)***
- [Spec SIG](https://docs.google.com/document/d/1pdvPeKjA8v8w_fGKAN68JjWBmVJtPCpqdi9IZrd6eEo/preview) Update (max 15 min)
- Core ([Issues](https://github.com/open-telemetry/opentelemetry-ruby/issues) / [PRs](https://github.com/open-telemetry/opentelemetry-ruby/pulls))
  - [kayla] [https://github.com/open-telemetry/opentelemetry-ruby/pull/1907](https://github.com/open-telemetry/opentelemetry-ruby/pull/1907)
    - Does this need to be a new major version? (removing attributes and events apis)
    - Let Ariel, Francis, Robert know about the break (hold release until we get their comment)
      - Tagged ruby-maintainers in a comment on the PR
    - [https://opentelemetry.io/docs/specs/otel/versioning-and-stability/#version-numbers](https://opentelemetry.io/docs/specs/otel/versioning-and-stability/#version-numbers)
  - [kayla] ​​[https://github.com/open-telemetry/opentelemetry-ruby/issues/1904](https://github.com/open-telemetry/opentelemetry-ruby/issues/1904)
    - Post in the channel to get more feedback
    - Messaging SIG concerns might be relevant here
    - Concerns about the tri-boolean state: true and nil vs false
  - ​​​​[kayla] [https://github.com/open-telemetry/opentelemetry-ruby/pull/1905](https://github.com/open-telemetry/opentelemetry-ruby/pull/1905)
  - Semconv PR
    - Check in with Robb about the changes I made
    - Seems helpful to folks here at the SIG
- Contrib ([Issues](https://github.com/open-telemetry/opentelemetry-ruby-contrib/issues) / [PRs](https://github.com/open-telemetry/opentelemetry-ruby-contrib/pulls))
  - [kayla] [https://github.com/open-telemetry/opentelemetry-ruby-contrib/pull/983](https://github.com/open-telemetry/opentelemetry-ruby-contrib/pull/983)
    - Creating a separate bridge directory has some issues:
      - The logger instrumentation currently depends on instrumentation-base; does it make sense to depend on instrumentation-base outside of the instrumentation directory?
      - Should we make a separate registry for log bridges? Does it make more sense to manage a single registry for all prepending libraries?
    - Post the PR on Slack to get feedback
  - [kayla] [https://github.com/open-telemetry/opentelemetry-ruby-contrib/pull/1637](https://github.com/open-telemetry/opentelemetry-ruby-contrib/pull/1637)
    - Is this something Puma would want to support? Tag one of their maintainers
    - Need to have a way to retire
    - Need to have a way to remove gems
    - Ask spec about why shutdown isn’t in there
    - Check back in on how to protect namespace in RubyGems
      - Discussion here:  ​[https://github.com/orgs/rubygems/discussions/8935](https://github.com/orgs/rubygems/discussions/8935)
  - [kayla] [https://github.com/open-telemetry/opentelemetry-ruby-contrib/pull/1634](https://github.com/open-telemetry/opentelemetry-ruby-contrib/pull/1634)
  - ​​​​[kayla] [https://github.com/open-telemetry/opentelemetry-ruby-contrib/pull/1533](https://github.com/open-telemetry/opentelemetry-ruby-contrib/pull/1533)
    - Next step: okay to allow the config, but don’t remove the other config right away
  - [kayla] Taking a look at Goutham’s Jaeger Sampling work this week too
- Burning questions?
- ✨ Happy Reports ✨
  - Taylor and Travis are engaged!

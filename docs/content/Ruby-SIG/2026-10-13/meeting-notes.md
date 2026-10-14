## Meeting Notes

### Attendees
- Kayla Reopelle
- Hannah Ramadan
- Josef Simanek
- Xuan Cao
- Robb Kidd

### Agenda
- [Spec SIG](https://docs.google.com/document/d/1pdvPeKjA8v8w_fGKAN68JjWBmVJtPCpqdi9IZrd6eEo/preview) Update (max 15 min)
- Core ([Issues](https://github.com/open-telemetry/opentelemetry-ruby/issues) / [PRs](https://github.com/open-telemetry/opentelemetry-ruby/pulls))
  - Structure of semantic convention gem. How can we structure it so that we support generating the below without conflict (Follow-ups on PR, will also share in Slack to get end-user feedback on current usage) [https://github.com/open-telemetry/opentelemetry-ruby/pull/2132](https://github.com/open-telemetry/opentelemetry-ruby/pull/2132) [james]:
    - Attribute names
    - Entity type
    - Event names
    - Log record
    - Metric names/descriptions
    - Metric Instruments
    - Span type
  - [https://github.com/open-telemetry/opentelemetry-ruby/issues/2170](https://github.com/open-telemetry/opentelemetry-ruby/issues/2170) Is progressing with 3 pr’s inflight atm & centralised encoding already merged will be in next release (Not ready for any decisions, will look at the PRs and comment on issue)
    - Centralized types with ci regeneration on proto version [https://github.com/open-telemetry/opentelemetry-ruby/pull/2236](https://github.com/open-telemetry/opentelemetry-ruby/pull/2236)
    - Common http client [https://github.com/open-telemetry/opentelemetry-ruby/pull/2432](https://github.com/open-telemetry/opentelemetry-ruby/pull/2432) looking for implementation feedback
    - Rename of grpc exporter to otlp-{{transport}}-{{signalType}}, http exporters will also follow this pattern eventually [https://github.com/open-telemetry/opentelemetry-ruby/pull/2448](https://github.com/open-telemetry/opentelemetry-ruby/pull/2448)
- Contrib ([Issues](https://github.com/open-telemetry/opentelemetry-ruby-contrib/issues) / [PRs](https://github.com/open-telemetry/opentelemetry-ruby-contrib/pulls))
  - [Kayla] Net::HTTP metrics PR: [https://github.com/open-telemetry/opentelemetry-ruby-contrib/pull/2630](https://github.com/open-telemetry/opentelemetry-ruby-contrib/pull/2630)
    - Do we like the structure? Any concerns about the current setup?
    - Will review this week
  - [Robb] [sidekiq: add options to record job timestamps as span attributes and job queue latency](https://github.com/open-telemetry/opentelemetry-ruby-contrib/issues/2631)
    - Next steps:
      - Look into config naming
      - Make a draft PR with open-ended names so we can decide what to name
      - Use metrics by default for latency
      - Change ms to s
      - Look into convention/attribute naming, possibly looping in Mike Perham
- Auto Instrumentation ([Issues](https://github.com/open-telemetry/opentelemetry-ruby-instrumentation/issues) / [PRs](https://github.com/open-telemetry/opentelemetry-ruby-instrumentation/pulls))
- Burning questions?
  - [Kayla] Do we need to keep metrics / logs pinned at three places in the SDK? This makes releases/updates to dependencies more complex. We do not pin to three places in instrumentation base. (Will talk with Matt about this on Slack)
- ✨ Happy Reports ✨

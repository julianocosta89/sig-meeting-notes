## Meeting Notes

### Attendees
- Kayla Reopelle
- Hannah Ramadan

### Agenda
- [Spec SIG](https://docs.google.com/document/d/1pdvPeKjA8v8w_fGKAN68JjWBmVJtPCpqdi9IZrd6eEo/preview) Update (max 15 min)
- Core ([Issues](https://github.com/open-telemetry/opentelemetry-ruby/issues) / [PRs](https://github.com/open-telemetry/opentelemetry-ruby/pulls))
  - (James) Being able to Deprecate/turn-off [https://open-telemetry.github.io/opentelemetry-ruby/](https://open-telemetry.github.io/opentelemetry-ruby/) is nearly possible. (James)
  - The otel registry via [https://github.com/open-telemetry/opentelemetry.io/pull/10606](https://github.com/open-telemetry/opentelemetry.io/pull/10606) will now contain links to the rubydocs pages which is what the [gh.io](http://gh.io) page was being used for with the links, descriptions etc being synced with each gem release
    - Preview of updated registry can be seen at [https://deploy-preview-10606--opentelemetry.netlify.app/ecosystem/registry/?language=ruby](https://deploy-preview-10606--opentelemetry.netlify.app/ecosystem/registry/?language=ruby)
  - (James) [https://github.com/open-telemetry/opentelemetry-ruby/pull/2210](https://github.com/open-telemetry/opentelemetry-ruby/pull/2210) (MERGED)
  - Semconv release:
    - Couldn’t figure out how to release 1.41.1
    - Need to merge PR for 1.42.0 semconv changes
    - Then open new release PR
- Contrib ([Issues](https://github.com/open-telemetry/opentelemetry-ruby-contrib/issues) / [PRs](https://github.com/open-telemetry/opentelemetry-ruby-contrib/pulls))
  - (James) [https://github.com/open-telemetry/opentelemetry-ruby-contrib/pull/2424](https://github.com/open-telemetry/opentelemetry-ruby-contrib/pull/2424) (MERGED)
  - (James) [https://github.com/open-telemetry/opentelemetry-ruby-contrib/pull/2429](https://github.com/open-telemetry/opentelemetry-ruby-contrib/pull/2429)
- Auto Instrumentation ([Issues](https://github.com/open-telemetry/opentelemetry-ruby-instrumentation/issues) / [PRs](https://github.com/open-telemetry/opentelemetry-ruby-instrumentation/pulls))
- Burning questions?
  - Is it possible to manually release a patch after above pr’s for: exporter-otlp, exporter-zipkin, api & sdk in addition to gruf & grpc in contrib
    - [Kayla] Yes. I can take care of that. - Need to do some extra effort since the conventional commits were “Chore”, they won’t initiate a release.
  - Do we need to add a redirect from gh pages to registry or don’t need to bother given it hasn’t been maintained etc
    - [Kayla] - James, can you check in with chalin or svrnm (Severin Neumann) on the docs side to see what they prefer?
- ✨ Happy Reports ✨

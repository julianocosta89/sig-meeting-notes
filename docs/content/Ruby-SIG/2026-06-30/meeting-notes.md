## Meeting Notes

### Attendees
- Being able to Deprecate/turn-off [https://open-telemetry.github.io/opentelemetry-ruby/](https://open-telemetry.github.io/opentelemetry-ruby/) is nearly possible. (James)
- The otel registry via [https://github.com/open-telemetry/opentelemetry.io/pull/10606](https://github.com/open-telemetry/opentelemetry.io/pull/10606) will now contain links to the rubydocs pages which is what the [gh.io](http://gh.io) page was being used for with the links, descriptions etc being synced with each gem release
- Preview of updated registry can be seen at [https://deploy-preview-10606--opentelemetry.netlify.app/ecosystem/registry/?language=ruby](https://deploy-preview-10606--opentelemetry.netlify.app/ecosystem/registry/?language=ruby)
- Pr’s needing merge by sig:
- [https://github.com/open-telemetry/opentelemetry-ruby/pull/2210](https://github.com/open-telemetry/opentelemetry-ruby/pull/2210)
- [https://github.com/open-telemetry/opentelemetry-ruby-contrib/pull/2424](https://github.com/open-telemetry/opentelemetry-ruby-contrib/pull/2424)
- Open question:
- Is it possible to manually release a patch after above pr’s for: exporter-otlp, exporter-zipkin, api & sdk in addition to gruf & grpc in contrib
- Do we need to add a redirect from gh pages to registry or don’t need to bother given it hasnt been maintained etc
- [Spec SIG](https://docs.google.com/document/d/1pdvPeKjA8v8w_fGKAN68JjWBmVJtPCpqdi9IZrd6eEo/preview) Update (max 15 min)
- Core ([Issues](https://github.com/open-telemetry/opentelemetry-ruby/issues) / [PRs](https://github.com/open-telemetry/opentelemetry-ruby/pulls))
- Contrib ([Issues](https://github.com/open-telemetry/opentelemetry-ruby-contrib/issues) / [PRs](https://github.com/open-telemetry/opentelemetry-ruby-contrib/pulls))
- Transitive dependency has broken CI yet again. Fix available [https://github.com/open-telemetry/opentelemetry-ruby-contrib/pull/2417](https://github.com/open-telemetry/opentelemetry-ruby-contrib/pull/2417)
- Auto Instrumentation ([Issues](https://github.com/open-telemetry/opentelemetry-ruby-instrumentation/issues) / [PRs](https://github.com/open-telemetry/opentelemetry-ruby-instrumentation/pulls))
- Burning questions?
- ✨ Happy Reports ✨

### Agenda
- Being able to Deprecate/turn-off [https://open-telemetry.github.io/opentelemetry-ruby/](https://open-telemetry.github.io/opentelemetry-ruby/) is nearly possible. (James)
  - The otel registry via [https://github.com/open-telemetry/opentelemetry.io/pull/10606](https://github.com/open-telemetry/opentelemetry.io/pull/10606) will now contain links to the rubydocs pages which is what the [gh.io](http://gh.io) page was being used for with the links, descriptions etc being synced with each gem release
  - Preview of updated registry can be seen at [https://deploy-preview-10606--opentelemetry.netlify.app/ecosystem/registry/?language=ruby](https://deploy-preview-10606--opentelemetry.netlify.app/ecosystem/registry/?language=ruby)
  - Pr’s needing merge by sig:
    - [https://github.com/open-telemetry/opentelemetry-ruby/pull/2210](https://github.com/open-telemetry/opentelemetry-ruby/pull/2210)
    - [https://github.com/open-telemetry/opentelemetry-ruby-contrib/pull/2424](https://github.com/open-telemetry/opentelemetry-ruby-contrib/pull/2424)
  - Open question:
    - Is it possible to manually release a patch after above pr’s for: exporter-otlp, exporter-zipkin, api & sdk in addition to gruf & grpc in contrib
    - Do we need to add a redirect from gh pages to registry or don’t need to bother given it hasnt been maintained etc
- [Spec SIG](https://docs.google.com/document/d/1pdvPeKjA8v8w_fGKAN68JjWBmVJtPCpqdi9IZrd6eEo/preview) Update (max 15 min)
- Core ([Issues](https://github.com/open-telemetry/opentelemetry-ruby/issues) / [PRs](https://github.com/open-telemetry/opentelemetry-ruby/pulls))
- Contrib ([Issues](https://github.com/open-telemetry/opentelemetry-ruby-contrib/issues) / [PRs](https://github.com/open-telemetry/opentelemetry-ruby-contrib/pulls))
  - Transitive dependency has broken CI yet again. Fix available [https://github.com/open-telemetry/opentelemetry-ruby-contrib/pull/2417](https://github.com/open-telemetry/opentelemetry-ruby-contrib/pull/2417)
- Auto Instrumentation ([Issues](https://github.com/open-telemetry/opentelemetry-ruby-instrumentation/issues) / [PRs](https://github.com/open-telemetry/opentelemetry-ruby-instrumentation/pulls))
- Burning questions?
- ✨ Happy Reports ✨

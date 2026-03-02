## Meeting Notes

### Attendees
- Kayla Reopelle
- Wendy Smoak
- Xuan Cao
- Hannah Ramadan

### Agenda
- [Spec SIG](https://docs.google.com/document/d/1pdvPeKjA8v8w_fGKAN68JjWBmVJtPCpqdi9IZrd6eEo/preview) Update (max 15 min)
- Core ([Issues](https://github.com/open-telemetry/opentelemetry-ruby/issues) / [PRs](https://github.com/open-telemetry/opentelemetry-ruby/pulls))
  - ​​[kayla] Bump semantic conventions: [https://github.com/open-telemetry/opentelemetry-ruby/pull/1952](https://github.com/open-telemetry/opentelemetry-ruby/pull/1952)
    - Version 1.38.0 is already out, so would like to get 1.37.0 out to stay up to date
  - [kayla] Working on a logs release to address [https://github.com/open-telemetry/opentelemetry-ruby/pull/1953](https://github.com/open-telemetry/opentelemetry-ruby/pull/1953)
  - [kayla] Xuan, should the metrics PRs that have been merged initiate a release?
- Contrib ([Issues](https://github.com/open-telemetry/opentelemetry-ruby-contrib/issues) / [PRs](https://github.com/open-telemetry/opentelemetry-ruby-contrib/pulls))
  - Consider documenting lifecycle process. Inspo: [https://github.com/open-telemetry/opentelemetry-js-contrib/blob/main/CONTRIBUTING.md#component-lifecycle](https://github.com/open-telemetry/opentelemetry-js-contrib/blob/main/CONTRIBUTING.md#component-lifecycle)
- Burning questions?
  - [Xuan] How to move the sem conv to somewhere that ready to use: [https://github.com/open-telemetry/opentelemetry-ruby/blob/main/semantic_conventions/lib/opentelemetry/semconv/http/metrics.rb](https://github.com/open-telemetry/opentelemetry-ruby/blob/main/semantic_conventions/lib/opentelemetry/semconv/http/metrics.rb)
    - Python example: [https://github.com/open-telemetry/opentelemetry-python/blob/main/opentelemetry-semantic-conventions/src/opentelemetry/semconv/metrics/http_metrics.py](https://github.com/open-telemetry/opentelemetry-python/blob/main/opentelemetry-semantic-conventions/src/opentelemetry/semconv/metrics/http_metrics.py)
    - JS example: [https://github.com/open-telemetry/opentelemetry-js/blob/main/semantic-conventions/src/stable_metrics.ts](https://github.com/open-telemetry/opentelemetry-js/blob/main/semantic-conventions/src/stable_metrics.ts)
    - Lets get Robb’s feedback async
  - [Xuan] Introduce runtime metrics: https://opentelemetry.io/docs/specs/semconv/runtime/
    - Let’s open an issue and start work. All other languages have runtime metrics
  - [Xuan] GenAI Instrumentation
    - Python GenAI: [https://github.com/open-telemetry/opentelemetry-python-contrib/tree/main/instrumentation-genai](https://github.com/open-telemetry/opentelemetry-python-contrib/tree/main/instrumentation-genai)
- ✨ Happy Reports ✨

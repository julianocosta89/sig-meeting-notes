## Meeting Notes

### Attendees
  - Ridhima Satam (Cisco/Splunk)
  - Dylan Russell (google)
  - Hector Hernandez (Microsoft)
  - Munir Abdinur (Datadog)
  - Joshua Winerman (Cisco/Splunk)
  - Riccardo Magliocchetti (Elastic)
  - Aaron Abbott (Google)
  - Marcelo Trylesinski (Pydantic)
  - Mani Yazdankhah (JP Morgan)
  - James Rowe(JP morgan)
  - Tammy Baylis (SolarWinds)
  - Keith Decker (Cisco/Splunk)
  - Shuwen Pan (Cisco)
  - Lukas Hering (Capital One)

### Agenda
  - Riccardo: logs stabilization:
  - https://github.com/open-telemetry/opentelemetry-python-contrib/pull/4112
  - https://github.com/open-telemetry/opentelemetry-python/issues/4330#issuecomment-3767228092
  - Riccardo: would appreciate some reviews
  - Rule based experimental sampler https://github.com/open-telemetry/opentelemetry-python/pull/4882
  - TracerConfigurator (would also like to add LogConfigurator and MeterConfigurator) https://github.com/open-telemetry/opentelemetry-python/pull/4861
  - Same PR should also fix NoOpTracer wrt context propagation
  - More configuration in autoinstrumentation https://github.com/open-telemetry/opentelemetry-python/pull/4806
  - Riccardo: WIP sdk health metrics https://github.com/open-telemetry/opentelemetry-python/pull/4880
  - Riccardo: PRs from Tammy to handle http stable semconv in server instrumentations:
  - https://github.com/open-telemetry/opentelemetry-python-contrib/pull/3982
  - https://github.com/open-telemetry/opentelemetry-python-contrib/pull/3993
  - All converted but starlette not tested?
  - Marcelo: Pyramid is not maintained since 2 years
  - Think on the process of dropping instrumentation or dropping support for older versions
  - Riccardo: More information to samplers from http instrumentations https://github.com/open-telemetry/opentelemetry-python-contrib/issues/4111
  - Good first issue after http semconv PRs go in?
  - Tammy: PTAL at PR to support Labeler / custom attributes
  - https://github.com/open-telemetry/opentelemetry-python-contrib/pull/3689
  - Includes documentation of basic usage: https://github.com/open-telemetry/opentelemetry-python-contrib/pull/3689/changes#diff-b2707393717a18c1b594e56d574562f0e23ce56e9655a669115b50242bd5f5dcR16
  - Should be ok with semconv. Easier to use than baggage. Useful for (e.g.) querying metrics by value known only after HTTP request received, without changing span name. https://github.com/open-telemetry/opentelemetry-python-contrib/issues/3695
  - Riccardo: PRs for next release
  - https://github.com/open-telemetry/opentelemetry-python/pull/4825
  - Ridhima - Asking for maintainers reviews/approval
  - Langchain llm invocation using genai utils https://github.com/open-telemetry/opentelemetry-python-contrib/pull/3889
  - Workflow operation name in agent span https://github.com/open-telemetry/semantic-conventions/pull/3249
  - Keith: - Reviews on this PR
  - https://github.com/open-telemetry/opentelemetry-python-contrib/pull/3994
  - Mani: PR review for supporting addition and removal of metric readers at run-time https://github.com/open-telemetry/opentelemetry-python/pull/4863

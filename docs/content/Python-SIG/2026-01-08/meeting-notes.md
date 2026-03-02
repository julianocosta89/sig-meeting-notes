## Meeting Notes

### Attendees
  - Liudmila Molkova (Grafana Labs)
  - Lukas Hering (Capital One)
  - Riccardo Magliocchetti (Elastic)
  - Dylan Russell (google)
  - Keith Decker (Cisco/Splunk)
  - Aaron Abbott (Google)

### Agenda
  - Riccardo: logs stabilization https://github.com/open-telemetry/opentelemetry-python/issues/4750
  - haven’t had time to work on the logs stabilization last tasks myself but the plan is to move the logging handler out of the sdk in the next release
  - Riccardo: plenty of PRs to review in -contrib and core
  - Liudmila: demo weaver live-check for GenAI https://github.com/open-telemetry/opentelemetry-python-contrib/compare/main...lmolkova:opentelemetry-python-contrib:add-weaver-live-check-for-gen-ai
  - Riccardo not working POC https://github.com/xrmx/opentelemetry-python-contrib/tree/e2e-validation-weaver
  - Will chat on slack with Liudmila
  - Liudmila: OpenAI latest-experimental updates
  - Moving to gen-ai utils for new semconv version https://github.com/open-telemetry/opentelemetry-python-contrib/pull/3715
  - GenAI utils  https://github.com/open-telemetry/opentelemetry-python-contrib/pull/4069
  - Lukas: adding aiobotocore instrumentation to botocore (questions around general approach)
  - https://github.com/open-telemetry/opentelemetry-python-contrib/pull/4049
  - Riccardo: will take another look

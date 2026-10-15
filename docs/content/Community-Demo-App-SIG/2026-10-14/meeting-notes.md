## Meeting Notes

### Attendees
- Maxime Quentin (Datadog)
- Felix George (IBM)
- Dónal O’Sullivan (Elastic)
- Juliano Costa (Datadog)
- Shenoy Pratik (AWS OpenSearch)

### Agenda
- [maxime] Migrate the Demo frontend app from the NodeJs SDK to the [https://github.com/open-telemetry/opentelemetry-browser](https://github.com/open-telemetry/opentelemetry-browser)
  - Current state of the opentelemetry-browser can be lived demoed already in this sandbox: [https://open-telemetry.github.io/opentelemetry-browser](https://open-telemetry.github.io/opentelemetry-browser)
  - How can such a migration be done as some new instrumentation will introduce braking collector changes ?
  - Any suggestions to measure the impacts on the Demo collectors ?
  - I will still double check during our Browser SIG if maintainers approve the migration
  - Notes: CI tests are running / main source of truth for the change
- [https://github.com/open-telemetry/opentelemetry-demo/pull/4034#issuecomment-5947771823](https://github.com/open-telemetry/opentelemetry-demo/pull/4034#issuecomment-5947771823)

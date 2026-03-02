## Meeting Notes

### Attendees
- Tyler Yahn (Splunk)
- Tristan Sloughter
- [Gregor Zeitlinger](mailto:gregor.zeitlinger@grafana.com) (Grafana Labs)
- Marylia Gutierrez (Grafana Labs)
- Alex Boten (Honeycomb)
- Jay DeLuca (Grafana Labs)

### Agenda
- [Gregor] Development parts of declarative config can apparently not be changed anymore
  - See recording of [OpenTelemetry SIG: Specifications](https://docs.google.com/document/d/1pdvPeKjA8v8w_fGKAN68JjWBmVJtPCpqdi9IZrd6eEo/edit?pli=1&tab=t.0#heading=h.roncxiv382fe)
    - Reason: OTel collector embeds declarative config and has declared itself stable
  - This is a major change to the development flow
  - See [https://github.com/open-telemetry/opentelemetry-configuration/pull/262](https://github.com/open-telemetry/opentelemetry-configuration/pull/262)
  - From meeting
    - Some parts are de-facto stable, because many users use it
    - “Stable” in this context means to support the feature gates in collector
    - What parts are affected
      - We don’t know - will have to check on a case by case basis
    - For the prom exporter, we have to support the collector with feature gates (even though it’s in development section)
      - Should support a migration path
- [Gregor] ConfigProvider can also be based on env vars, at least that’s what JS is doing now
  - What is the best practice? Seems to be a good idea
- [Gregor] Add ability to configure dynamic auth headers: [https://github](https://github.com/open-telemetry/opentelemetry-configuration/issues/257)
- [.com/open-telemetry/opentelemetry-configuration/issues/257](https://github.com/open-telemetry/opentelemetry-configuration/issues/257)
  - AI (Tyler): find related spec issue.
    - [https://github.com/open-telemetry/opentelemetry-specification/issues/1344](https://github.com/open-telemetry/opentelemetry-specification/issues/1344)
  - Discuss in spec meeting
- [Triage project board](https://github.com/orgs/open-telemetry/projects/38)
- [marylia] Project board for JS [https://github.com/orgs/open-telemetry/projects/157/views/1](https://github.com/orgs/open-telemetry/projects/157/views/1)
  - Java [https://github.com/orgs/open-telemetry/projects/151](https://github.com/orgs/open-telemetry/projects/151)
- [Gregor] Known HTTP methods: [https://github.com/open-telemetry/opentelemetry-configuration/pull/244](https://github.com/open-telemetry/opentelemetry-configuration/pull/244)
  - Continue working on semconv ticket

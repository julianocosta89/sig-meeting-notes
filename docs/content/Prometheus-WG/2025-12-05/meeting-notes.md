## Meeting Notes

### Attendees
- arthursens
- dashpole
- owen
- krajo
- ## Prometheus Receiver stabilization -
  - ## Check-in and progress review
  - Backlog review
- Krajo: anyone working on putting OTEL->Promtheus model into a separate lib like (otlptranslator)?
- Krajo: prometheus remote write exporter missing option to send NHCB instead of classic histograms
  - Krajo to write issue for this
  - Might go into otlptranslator if it has truely multiple uses
- Krajo: [https://github.com/open-telemetry/opentelemetry-collector-contrib/pull/44732](https://github.com/open-telemetry/opentelemetry-collector-contrib/pull/44732) Turns out that we don't treat `_info` series that we scrape  in any special way (except target_info), but we cut the _info suffix so when we export the metric to Prometheus, it loses the suffix.
  - For otel the metric name is the Prometheus metric **family** name

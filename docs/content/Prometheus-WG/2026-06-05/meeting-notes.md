## Meeting Notes

### Attendees
- arthur
- david
- krajo
- arve
- kyle
- andreas gkizas
- himanshu singh

### Agenda
- [andreas] [https://github.com/open-telemetry/opentelemetry-collector-contrib/issues/33137#issuecomment-4577020119](https://github.com/open-telemetry/opentelemetry-collector-contrib/issues/33137#issuecomment-4577020119) (related to [https://github.com/open-telemetry/opentelemetry-collector-contrib/pull/48767](https://github.com/open-telemetry/opentelemetry-collector-contrib/pull/48767))
  - Metadata information is lost when requests are batched. Brakes route-based routing.
  - Replaced WAL with exporter helper, and it worked for our backend.
  - Plan:
    - Open an issue in collector-core, requesting in-order support in exporterhelper sending queue.
    - Land metadataKeys' PR in the existing Prometheus exporter.
    - Once we have buy-in from Collector maintainers for the in-order support, we can open PRs adding exporterhelper to the Prometheus remote write exporter.
- Review project boards

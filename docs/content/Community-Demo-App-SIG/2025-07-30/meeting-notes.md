## Meeting Notes

### Attendees
- [Juliano Costa](mailto:juliano.costa@datadoghq.com)(Datadog)
- Shenoy Pratik (OpenSearch)
- Pierre Tessier (Honeycomb)

### Agenda
- Shenoy will take a look at OpenSeach to reduce the footprint. Also looking into ISM policy for reducing memory on storage.
- Pierre will take a closer look at helm chart and Jaeger
  - [https://github.com/open-telemetry/opentelemetry-demo/pull/2389](https://github.com/open-telemetry/opentelemetry-demo/pull/2389)
  - Do we stop using the Jaeger Helm chart as a sub-chart?
- Juliano will investigate the kafka logic for checkout service to be able to change kafka addr with docker profiles
- Maybe changing loadgen to a nodejs with playwright will reduce the size of the service.

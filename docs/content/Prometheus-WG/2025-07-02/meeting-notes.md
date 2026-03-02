## Meeting Notes

### Agenda
- [arthur] How to correlate Prometheus metrics with OTel Logs/Traces
  - `service.name` , `service.namespace`, `service.instance.id` are translated to job/instance, and that's not what Logs/Traces are using and that’s what a growing number of OTel practitioners want to see in their queries.
  - Should we update the spec to add the config option “`keep_indentifying_resource_attributes`” (which promotes `service.name`, `service.namespace`, and `service.instance.id)`, similar to what Prometheus does? It will keep the original resource attribute names, and that should be enough for Log/Trace correlation
- [arthur] Delta Working Group depends on type/unit labels being added through the OTLP endpoint. Seeing that switching the OTLP ingestion path from RWv1 to RWv2 is not that easy, would it be ok if I re-opened my [old PR](https://github.com/prometheus/prometheus/pull/16630) and added those labels through the OTLP code path instead of RW?
  - [dashpole] OTLP endpoint in Prometheus PRW2.0?
    - [https://github.com/prometheus/prometheus/pull/16784](https://github.com/prometheus/prometheus/pull/16784)
    - Krajo: commented
    - [https://github.com/prometheus/prometheus/tree/main/storage/remote/otlptranslator/prometheusremotewrite](https://github.com/prometheus/prometheus/tree/main/storage/remote/otlptranslator/prometheusremotewrite)
    - David+Krajo to POC using Appender interface between OTLP endpoint and storage to
- [arthur] Review status of Spec changes
  - [https://github.com/open-telemetry/opentelemetry-specification/pull/4561](https://github.com/open-telemetry/opentelemetry-specification/pull/4561)
    - Histogram MetricPoints with Native Buckets MUST have a Schema value. The Schema is an 8 bit signed integer between -4 and 8. Schemas between -9 and 52 are called Standard (exponential) Schemas, the currently unused Schemas -9 to -5 and 9 to 52 are reserved to be used as Standard Schemas later.
    - NHCB is Remote-Write 2.0 or specifically shows up in the Prometheus receiver.  AI: Add a note to the Histogram section
  - [https://github.com/open-telemetry/opentelemetry-specification/pull/4533](https://github.com/open-telemetry/opentelemetry-specification/pull/4533)
  - [https://github.com/open-telemetry/opentelemetry-collector-contrib/pull/40060](https://github.com/open-telemetry/opentelemetry-collector-contrib/pull/40060)
- Action Item
  - [Cyrille Le Clerc](mailto:cyrille.leclerc@grafana.com) to open an issue on the OTel spec to add `keep_identifying_resource_attribute` to otel2prometheus OpenTelemetry specs
    - [[OTel to Prometheus] Promote resource attr `service.name`, `service.namespace`, and `service.instance.id` as Prometheus metric labels #4577](https://github.com/open-telemetry/opentelemetry-specification/issues/4577)
    - Check behaviour of “Prometheus Exporter”, maybe “keep” is a questionable naming

## Meeting Notes

### Attendees
- [Bartłomiej Płotka](mailto:bwplotka@gmail.com) (Google)
- Brian Sapozhnikov (Microsoft)
- Drew Relmas (Microsoft)
- Albert Lockett (F5)
- Aaron Marten (Microsoft)
- Niamh Gowran (Microsoft)
- Jake Dern (F5)
- Bhala Ranganathan (Microsoft)
- Swapnil Ashtekar (Microsoft)

### Agenda
- [Triage]
  - [Issues that need to be discussed](https://github.com/open-telemetry/otel-arrow/issues?q=is%3Aissue%20state%3Aopen%20sort%3Aupdated-deswc%20label%3Atriage%3Aneeds-discussion)
  - [Issues that have just been marked as stale](https://github.com/open-telemetry/otel-arrow/issues?q=is%3Aissue%20state%3Aopen%20sort%3Aupdated-desc%20label%3Astale%20)
  - [Issues that need deciding](https://github.com/open-telemetry/otel-arrow/issues?q=is%3Aissue%20state%3Aopen%20sort%3Aupdated-desc%20label%3Atriage%3Adeciding)
- **[Bartek / @bwplotka]** Thanks for an amazing project: [https://lnkd.in/p/ekk7YaVz](https://lnkd.in/p/ekk7YaVz)
  - ![][image1]
  - This literally triggered conversations about Thanos and Prometheus in Rust and columnar ([we are starting new SIG](https://docs.google.com/document/d/1uZjrWeAfRaN6fIp4L7pd-lMqc650bClJeg7jGO3gerE/edit?tab=t.ok8vuqesxwve#heading=h.ht6fktvkrxsh)).
- [scrape.rs](http://scrape.rs)
  - Different formats vs OTLP
    - Std proto lib
    - Interpret protobytes directly
- **[Bartek / @bwplotka]** Some contributions:
  - [#4684](https://github.com/open-telemetry/otel-arrow/pull/4684) `docs(otap-dataflow): add self-observability guide and metrics reference` (Ready for review) - Operator guide for the embedded web UI, admin HTTP endpoints, Prometheus/OTLP mapping rules, and reference catalog of all 127 `#[metric_set]` scopes.
    - Some other metric additions and fixes [#4670](https://github.com/open-telemetry/otel-arrow/pull/4670) [#4672](https://github.com/open-telemetry/otel-arrow/pull/4672)
  - [#4690](https://github.com/open-telemetry/otel-arrow/pull/4690) `feat(core-nodes): add metric_start_time processor with subtract_initial_point` (Draft) - Columnar `urn:otel:processor:metric_start_time` processor operating directly on `OtapArrowRecords::Metrics` (`subtract_initial_point` strategy for cumulative series without `_created`).
  - Optimizations:
    - [#4688](https://github.com/open-telemetry/otel-arrow/pull/4688) `perf(pdata): preserve child row order and fast-path sorted IDs in BatchSorter` (Draft) - Preserves child attribute row order across sibling data points during OTLP encoding and fast-paths sorted native IDs; cuts compressed OTLP metrics wire size after `upsert_attributes` by 61% (gzip) and 94% (zstd) while speeding up gzip/zstd encoding by 41-54%.
    - [#4689](https://github.com/open-telemetry/otel-arrow/pull/4689) `fix(attributes-processor): exclude MetricAttrs from signal domain and add ExpHistogramDpAttrs` (Draft) - Stops `apply_to: ["signal"]` from mutating `Metric.metadata` (`MetricAttrs`) and adds missing `ExpHistogramDpAttrs` / `ExpHistogramDpExemplarAttrs`.
- **[Bartek / @bwplotka]**  Would you be up for trying [benchfmt.rs](https://github.com/bwplotka/benchfmt.rs)? Happy to help with migration. Issue: [https://github.com/open-telemetry/otel-arrow/issues/4691](https://github.com/open-telemetry/otel-arrow/issues/4691)
  - Example output:
  - ![][image2]
- [Laurent]: KubeCon news
- .
- .
- ..

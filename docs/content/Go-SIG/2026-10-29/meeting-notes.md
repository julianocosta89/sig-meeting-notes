## Meeting Notes

### Attendees
- Puneet Singh
- Tyler Yahn (Splunk)
- David Ashpole (Google)
- Damien Mathieu (Elastic)

### Agenda
- Core Exporter:
  - **Has 1 Approval (Needs 2nd Approver)**:
    - [#9296](https://github.com/open-telemetry/opentelemetry-go/pull/9296): Do not emit `target_info` for empty Resource *(approved by @dmathieu)*
    - [#9294](https://github.com/open-telemetry/opentelemetry-go/pull/9294): Order colliding sanitized label values by original key *(approved by @dmathieu)*
    - [#9275](https://github.com/open-telemetry/opentelemetry-go/pull/9275): Remove deprecated `WithoutUnits` and `WithoutCounterSuffixes` options *(approved by @dmathieu)*
    - [#9248](https://github.com/open-telemetry/opentelemetry-go/pull/9248): Avoid redundant slice and map allocations *(approved by @dmathieu)*
  - **Needs Review**:
    - [#9297](https://github.com/open-telemetry/opentelemetry-go/pull/9297): Set created timestamp on counter and histogram metrics
    - [#9295](https://github.com/open-telemetry/opentelemetry-go/pull/9295): Omit empty `trace_id` and `span_id` exemplar labels
- Contrib Prometheus Bridge (`bridges/prometheus`):
  - **Has 1 Approval (Needs 2nd Approver)**:
    - [#10041](https://github.com/open-telemetry/opentelemetry-go-contrib/pull/10041): Decode hex trace/span IDs in exemplars & support native histogram exemplars *(approved by @dmathieu)*
    - [#10043](https://github.com/open-telemetry/opentelemetry-go-contrib/pull/10043): Return concrete `*Producer` from `NewMetricProducer` *(approved by @dmathieu)*
  - **Needs Review (Addressed Comments)**:
    - [#10042](https://github.com/open-telemetry/opentelemetry-go-contrib/pull/10042): Convert Prometheus unit metadata to UCUM *(re-requested @dmathieu)*
    - [#10044](https://github.com/open-telemetry/opentelemetry-go-contrib/pull/10044): Handle native histogram and gatherer edge cases *(re-requested @dmathieu)*
- **Has 1 Approval (Needs 2nd Approver)**:
  - [#8510](https://github.com/open-telemetry/opentelemetry-go/pull/8510): `[sdk/metric/x]` Add Experimental Composable Views *(approved by @MrAlias)*
- **Needs Review**:
  - [#9278](https://github.com/open-telemetry/opentelemetry-go/pull/9278): Add internal bound Sum aggregation (bound instruments tracking [#8759](https://github.com/open-telemetry/opentelemetry-go/issues/8759), spec [#8409](https://github.com/open-telemetry/opentelemetry-go/issues/8409))
  - [#9277](https://github.com/open-telemetry/opentelemetry-go/pull/9277): Refactor `expoBuckets` to fixed-position circular storage
  - [#9298](https://github.com/open-telemetry/opentelemetry-go/pull/9298): Add experimental metric `WithOptIn` and View `Enabled` configuration (pairs with file-based config view stream [#724](https://github.com/open-telemetry/opentelemetry-configuration/pull/724))
- **Draft / In Progress**:
  - [#8276](https://github.com/open-telemetry/opentelemetry-go/pull/8276): Lazily delete map elements for delta metrics to re-use storage
- **Has 1 Approval (Needs 2nd Approver)**:
  - [#10067](https://github.com/open-telemetry/opentelemetry-go-contrib/pull/10067): Set `SchemaURL` on Meter and Producer scope *(approved by @dmathieu)*
  - [#10060](https://github.com/open-telemetry/opentelemetry-go-contrib/pull/10060): Remove deprecated runtime metrics *(approved by @dmathieu)*
  - [#10021](https://github.com/open-telemetry/opentelemetry-go-contrib/pull/10021): Add opt-in detailed memory and CPU attributes *(approved by @dmathieu)*
- **Needs Review (Addressed Comments)**:
  - [#10066](https://github.com/open-telemetry/opentelemetry-go-contrib/pull/10066): Add `WithMinimumRefreshInterval` and deprecate `WithMinimumReadMemStatsInterval` *(re-requested @dmathieu)*
- **Needs Review**:
  - [#10052](https://github.com/open-telemetry/opentelemetry-go-contrib/pull/10052): Deprecate `WithPublicEndpoint` in favor of `WithPublicEndpointFn`
  - [#10053](https://github.com/open-telemetry/opentelemetry-go-contrib/pull/10053): Align server span name and `http.route` with HTTP semconv
  - [#10054](https://github.com/open-telemetry/opentelemetry-go-contrib/pull/10054): Preserve `MultipartForm` on original request after `WithContext`
  - [#10055](https://github.com/open-telemetry/opentelemetry-go-contrib/pull/10055): Support HTTP server metrics and `WithMeterProvider`
- **Needs Review**:
  - [#9311](https://github.com/open-telemetry/opentelemetry-go/pull/9311): Support per-series start timestamps for cumulative async instruments *(spec clarification [opentelemetry-specification#5394](https://github.com/open-telemetry/opentelemetry-specification/pull/5394) merged)*
- **Has 1 Approval (Needs 2nd Approver)**:
  - [#10030](https://github.com/open-telemetry/opentelemetry-go-contrib/pull/10030): Deprecate `propagators/opencensus` module and package *(approved by @dmathieu)*
  - [#10020](https://github.com/open-telemetry/opentelemetry-go-contrib/pull/10020): Add `WithGCEInstanceLabelKeyFilter` for GCE instance labels in `detectors/gcp` *(approved by @dmathieu)*
  - [#10034](https://github.com/open-telemetry/opentelemetry-go-contrib/pull/10034): `test(zpages)`: Use `SetStatus` instead of `RecordError` for error span test *(approved by @dmathieu)*

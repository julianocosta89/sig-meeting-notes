## Meeting Notes

### Attendees
- Kayla Reopelle
- Eric Mustin
- Goutham
- Xuan Cao

### Agenda
- [Spec SIG](https://docs.google.com/document/d/1pdvPeKjA8v8w_fGKAN68JjWBmVJtPCpqdi9IZrd6eEo/preview) Update (max 15 min)
- Core ([Issues](https://github.com/open-telemetry/opentelemetry-ruby/issues) / [PRs](https://github.com/open-telemetry/opentelemetry-ruby/pulls))
  - [kayla] – Left feedback on [https://github.com/open-telemetry/opentelemetry-ruby/pull/1865](https://github.com/open-telemetry/opentelemetry-ruby/pull/1865)
  - [eric] some vendors are shipping ruby auto instrumentation before the operator PR is merged, may cause bug reports to come our way [https://github.com/odigos-io/odigos/pull/3037](https://github.com/odigos-io/odigos/pull/3037)
  - [Xuan] Missing feature from otlp exporter
    - POST requests to default paths: /v1/traces, /v1/metrics, /v1/logs, /v1development/profiles.
      - Yes, but no /v1development/profiles for ExportProfilesServiceRequest
    - Supports both HTTP/1.1 and HTTP/2 (should fallback to HTTP/1.1 if needed).
      - ruby seems only support HTTP/1.1 because net/http doesn’t support HTTP/2.
    - JSON encoding uses lowerCamelCase field names, hex-encoded IDs, integer enums.
      - No JSON support
- Contrib ([Issues](https://github.com/open-telemetry/opentelemetry-ruby-contrib/issues) / [PRs](https://github.com/open-telemetry/opentelemetry-ruby-contrib/pulls))
  - [Eric] [https://github.com/open-telemetry/opentelemetry-ruby/issues/1252#issuecomment-3067033941](https://github.com/open-telemetry/opentelemetry-ruby/issues/1252#issuecomment-3067033941)
  - [kayla] Zero-code/Auto instrumentation PR configuration options
    - Compatibility with file-based configuration – want to make sure the names are consistent, was the current process inspired by Node?
    - Will these configs apply outside of an auto-instrumentation context?
    - How does the `OTEL_RUBY_INSTRUMENTATION_REDIS_CONFIG_OPTS` variable work?
    - **TODO: Kayla to look at Node configs**
  - [kayla] OTelbot token for Release PRs?
    - [https://github.com/open-telemetry/opentelemetry-ruby-contrib/pull/1598](https://github.com/open-telemetry/opentelemetry-ruby-contrib/pull/1598)
  - [kayla] Net::HTTP suite failure: [https://github.com/open-telemetry/opentelemetry-ruby-contrib/pull/1599](https://github.com/open-telemetry/opentelemetry-ruby-contrib/pull/1599)
  - [kayla] I broke the CI for HTTPClient semconv :(
  - [kayla] GraphQL problems: [https://github.com/open-telemetry/opentelemetry-ruby-contrib/issues/127#issuecomment-3073153024](https://github.com/open-telemetry/opentelemetry-ruby-contrib/issues/127#issuecomment-3073153024)
  - **Kayla Todo:** Move Logger Instrumentation out of the instrumentation packages into a separate bridge package
- Burning questions?
- ✨ Happy Reports ✨

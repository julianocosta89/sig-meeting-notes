## Meeting Notes

### Attendees
- Kayla Reopelle
- Wendy Smoak
- Xuan Cao
- Michal Kazmierczak
- Hannah Ramadan
- Eric mustin

### Agenda
- [Spec SIG](https://docs.google.com/document/d/1pdvPeKjA8v8w_fGKAN68JjWBmVJtPCpqdi9IZrd6eEo/preview) Update (max 15 min)
- Core ([Issues](https://github.com/open-telemetry/opentelemetry-ruby/issues) / [PRs](https://github.com/open-telemetry/opentelemetry-ruby/pulls))
  - [kayla] ​​[https://github.com/open-telemetry/opentelemetry-ruby/pull/1881](https://github.com/open-telemetry/opentelemetry-ruby/pull/1881)
    - Will review this week
  - [kayla] [https://github.com/open-telemetry/opentelemetry-ruby/pull/1883](https://github.com/open-telemetry/opentelemetry-ruby/pull/1883)
  - [kayla] Drop aggregation question -  [https://opentelemetry.io/docs/specs/otel/metrics/sdk/#drop-aggregation](https://opentelemetry.io/docs/specs/otel/metrics/sdk/#drop-aggregation)
  - [kayla] Merge order for the new metrics PRs?
- Contrib ([Issues](https://github.com/open-telemetry/opentelemetry-ruby-contrib/issues) / [PRs](https://github.com/open-telemetry/opentelemetry-ruby-contrib/pulls))
  - [kayla] Logger Instrumentation
    - Other examples:
      - Go - bridges
      - Java - instrumentation
      - JS - packages (same as our instrumentation)
    - Nice in collector contrib to have separate receiver organization
    - Could be nice to have separate directories for signal instrumentation
    - Look at CI workflows to see if we’ll encounter any problems
      - Create a wishlist ticket?
  - [eric] DB Semconv Opt in
    - Dotnet has a similar milestone they’re tracking (milestones ftw!) [https://github.com/open-telemetry/opentelemetry-dotnet-contrib/milestone/6](https://github.com/open-telemetry/opentelemetry-dotnet-contrib/milestone/6)
  - [michal] gRPC instrumentation - currently we only have the client tracing instrumentation, is there interest in adding the server instrumentation as well?
    - Yes, would be helpful to have server instrumentation as well
    - Also a gRPC exporter that could be prepared for release
    - Michal will start with the server instrumentation and will look at gRPC exporter next
- Burning questions?
  - Where are we at with metrics?
    - Kayla will update the project board to make sure it’s accurate
- ✨ Happy Reports ✨
  - [wendy] Logs - exporting up to 100K logs a minute (consolidated from multiple servers) and it’s fine!
    - Kayla will look into what’s needed for moving to stability

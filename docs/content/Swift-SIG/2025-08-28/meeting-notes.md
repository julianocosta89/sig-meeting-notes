## Meeting Notes

### Attendees
- Ariel Demarco
- Bryce Buchanan
- Vinod Vydier
- Alex Cohen
- Bee Klimt
- Martin Holman
- Billy Zhou

### Agenda
- Repository Division Follow Up
  - package.swift ifdefs
    - This was a dead end
  - Action item: create swift-core, initially only API & SDK (with plans for OTLP exporters) Bryce TODO
    - GRPC-swift not the biggest offender (~5MB)
    - Prometheus dependencies is ~90MB
    - swift-protobuf is ~31MB (Otlp common dependency)
- [Billy] Session PR, please review: https://github.com/open-telemetry/opentelemetry-swift/pull/899
- ~~Discuss Timeline for [https://github.com/open-telemetry/opentelemetry-swift/issues/808](https://github.com/open-telemetry/opentelemetry-swift/issues/808)~~
- ~~DataCompression Follow Up ([PR for context](https://github.com/mw99/DataCompression/pull/38) and [the issue generated](https://github.com/open-telemetry/opentelemetry-swift/actions/runs/16502731654/job/46665441671))~~
- ~~Sessions - [https://github.com/open-telemetry/opentelemetry-swift/pull/899](https://github.com/open-telemetry/opentelemetry-swift/pull/899)~~

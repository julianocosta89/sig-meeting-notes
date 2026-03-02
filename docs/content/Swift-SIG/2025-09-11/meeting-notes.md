## Meeting Notes

### Attendees
- Billy Zhou
- Bryce Buchanan
- Martin Holman
- Nacho Bonafonte
- Arriana Blais
- Bee Klimt
- Vinod Vydier

### Agenda
- Discuss Timeline for [https://github.com/open-telemetry/opentelemetry-swift/issues/808](https://github.com/open-telemetry/opentelemetry-swift/issues/808) ( I can look into this next week - Vinod)
- DataCompression Follow Up ([PR for context](https://github.com/mw99/DataCompression/pull/38) and [the issue generated](https://github.com/open-telemetry/opentelemetry-swift/actions/runs/16502731654/job/46665441671))
  - Fixed in [PR](https://github.com/open-telemetry/opentelemetry-swift/pull/905)
- core version & releasing discussion
- todo: new slack channel for swift notification [Bryce]
- todo: document release behavior for swift-core / swift
- [bryce] semconv update
- Sessions - [https://github.com/open-telemetry/opentelemetry-swift/pull/899](https://github.com/open-telemetry/opentelemetry-swift/pull/899)
- [martin] is this a path worth continuing with? [https://github.com/open-telemetry/opentelemetry-swift/pull/903](https://github.com/open-telemetry/opentelemetry-swift/pull/903)
- todo: match core version to main repo for the initial core release (to satisfy cocoapod assumptions)
  - wait for semconv PR
- [Ari] Release OTel-Swift with new Core version (2.1.1)
- [Ari] Prereleases? - process is set to release as prelease and then manually set it as release.
- Sessions SemConv - [https://github.com/open-telemetry/opentelemetry-swift/pull/899](https://github.com/open-telemetry/opentelemetry-swift/pull/899) - Billy
- SemConv for screen load, app launch, app attribute - Grace
  - [app.screen.name](http://app.screen.name) semConv PR: [https://github.com/open-telemetry/semantic-conventions/pull/2744](https://github.com/open-telemetry/semantic-conventions/pull/2744)

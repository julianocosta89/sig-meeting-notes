## Meeting Notes

### Attendees
- [Bryce Buchanan](mailto:bryce.buchanan@elastic.co)
- [Arriana Blais](mailto:arriblais@honeycomb.io)
- Ariel Demarco
- Martin Holman
- Vinod Vydier

### Agenda
- [bryce] document issue discussed in [https://github.com/open-telemetry/opentelemetry-swift/issues/919](https://github.com/open-telemetry/opentelemetry-swift/issues/919)
- Nightly builds from Nacho
- [cocoa pods issue in slack this morning](https://cloud-native.slack.com/archives/C01NCHR19SB/p1761234598646409)
  - looks like a compilation error: Ari to look into it.
- [deploy OS version](https://github.com/open-telemetry/opentelemetry-swift-core/issues/23)
- Billy summary on issues, to add crash reporter instrumentation, app kit metrics
  - crash reporting: use either existing log event `exception` semconv or review crash specific experimental semconv [here](https://github.com/open-telemetry/semantic-conventions/pull/1576/files) if discussion seems settled enough.
- next release daterb
  - asap 2.2.1 or 2.3.0
- Bryce out next week

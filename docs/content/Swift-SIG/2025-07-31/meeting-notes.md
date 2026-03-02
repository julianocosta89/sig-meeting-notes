## Meeting Notes

### Attendees
- Bryce Buchanan
- Arriana Blais
- Bee Klimtf
- Alex Cohen
- Vinod Vydier
- Ariel Demarco

### Agenda
- release 2.0 pre-release
- Platform Specific issues - Ari
  - Remove VisionOS?
    - if we can’t resolve data compression issues or new issues pop up
- DataCompression - Ari
  - [cocoapods issue](https://cloud-native.slack.com/archives/C01NCHR19SB/p1753452881078079)
  - [https://github.com/mw99/DataCompression/pull/37](https://github.com/mw99/DataCompression/pull/37)
    - Add a +1
  - ~~use Ari’s fork until PR merged~~
  - do we still need data compression? Can we replace it with a built in library? - Ari to investigate
- AC: There's a class/struct named `View` which seems to cause issues with SwiftUI.View if imported directly into SwiftUI code. ([issue](https://github.com/open-telemetry/opentelemetry-swift/issues/880))
- Metrics warning??? ([Link](https://github.com/open-telemetry/opentelemetry-specification/issues/4604))

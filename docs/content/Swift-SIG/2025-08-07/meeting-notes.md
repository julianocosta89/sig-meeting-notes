## Meeting Notes

### Attendees
- Bryce Buchanan
- Arriana Blais
- Nacho Bonafonte
- Vinod Vydier
- Alex Cohen
- Ariel Demaco

### Agenda
- DataCompression issue: [follow up PR](https://github.com/mw99/DataCompression/pull/38) - Ari
  - let’s thumbsup this PR
- AC: There's a class/struct named `View` which seems to cause issues with SwiftUI.View if imported directly into SwiftUI code. ([issue](https://github.com/open-telemetry/opentelemetry-swift/issues/880))
  - MetricView
  - typealias view
    - Notifications uses this structure
- Metrics warning??? ([Link](https://github.com/open-telemetry/opentelemetry-specification/issues/4604))
- Split repo.
  - 1. Api + SDK
  - 2. Contrib + other stuff built upon api and SDK
  - automatic dependency update in contrib
  - ci in API/SDK that runs Contrib tests in new PRs
  - Todo: create contrib repo
    - Opentelemetry-swift-contrib
      - Bryce to follow up
    - contrib work to be done in `3.0` branch

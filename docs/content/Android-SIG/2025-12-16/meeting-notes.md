## Meeting Notes

### Attendees
- Jason (Splunk)
- Mustafa (Honeycomb)
- Jamie Lynch (Embrace)
- Hanson Ho (Embrace)
- Surbhi A (Cisco)cleverchuk(solarwinds)

### Agenda
- [surbhi] has a PR :) [https://github.com/open-telemetry/opentelemetry-java-instrumentation/pull/15664](https://github.com/open-telemetry/opentelemetry-java-instrumentation/pull/15664)
  - Network phase timestamps
  - Introduces a new API
  - Looking for reviews, specifically around the API and overall everything
  - Will also need semantic conventions, and then eventually merge into android
  - Would we want to enable this by default?
- [jason] - resource PR (?)
  - [https://github.com/open-telemetry/opentelemetry-android/pull/1476](https://github.com/open-telemetry/opentelemetry-android/pull/1476)
  - Approved but would appreciate additional reviews
- [jason] - asking about client TLS [https://github.com/open-telemetry/opentelemetry-android/issues/1475](https://github.com/open-telemetry/opentelemetry-android/issues/1475)
  - Users could expect to deploy apps with their own client certs
  - Jason has an implementation started, but WIP (probably not until next year)
- [jason] - gradle conventions thinger
  - [https://github.com/open-telemetry/opentelemetry-android/pull/1453](https://github.com/open-telemetry/opentelemetry-android/pull/1453)
  - We like the idea, but Jason is very skeptical about it passing the sonatype close/release
  - The transitive conventions dep may not work for sonatype even tho it works for compile and runtime
- [jason] - 1.0.0 release
  - Delay until first full week of Jan
  - We will release 1.1.0 a week or two after that
    - It’s kinda stacking up already
  - Then we’re back on track
- [https://github.com/open-telemetry/community/issues/2975](https://github.com/open-telemetry/community/issues/2975) is progressing!

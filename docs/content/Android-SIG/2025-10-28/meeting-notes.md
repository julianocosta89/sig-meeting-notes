## Meeting Notes

### Attendees
- Jason (Splunk)
- Jamie Lynch (Embrace)
- Cesar (Elastic)
- Mustafa Haddara (Honeycomb)
- cleverchuk(solarwinds)

### Agenda
- Well, we got 0.16.0 out anyway….
- rc.1 pushed back due to [https://github.com/open-telemetry/opentelemetry.io/pull/8208/files#diff-e0b3f3c57e5e75133e79ed2200e22cbabf2f5b8c8a7aee3b5aed254359fdaae2R57](https://github.com/open-telemetry/opentelemetry.io/pull/8208/files#diff-e0b3f3c57e5e75133e79ed2200e22cbabf2f5b8c8a7aee3b5aed254359fdaae2R57)
  - How will this work for java?
  - Is this going to be a guideline vs. a requirement?
- Gzip by default?
  - [https://github.com/open-telemetry/opentelemetry-android/issues/1324#issuecomment-3452729412](https://github.com/open-telemetry/opentelemetry-android/issues/1324#issuecomment-3452729412)
  - This is important to reduce size on the wire
  - …but should it be enabled by default - probably yes
  - Does the spec say anything about this?
    - Yes! [https://opentelemetry.io/docs/specs/otlp/#protocol-details](https://opentelemetry.io/docs/specs/otlp/#protocol-details) servers need to support gzip
- [https://github.com/open-telemetry/opentelemetry-android/issues/1347](https://github.com/open-telemetry/opentelemetry-android/issues/1347)
  - Yes, we probably should remove rum.sdk.version
  - We should probably replace [telemetry.sdk.name/version/etc](http://telemetry.sdk.name/version/etc). with android values
  - This PR shows what the resource looked like recently (as a reference) [https://github.com/open-telemetry/opentelemetry-android/pull/1064](https://github.com/open-telemetry/opentelemetry-android/pull/1064)
- Have we made a decision about metrics?
  - Issue is still open: [https://github.com/open-telemetry/opentelemetry-specification/issues/4604](https://github.com/open-telemetry/opentelemetry-specification/issues/4604)
  - Still need some description here [https://opentelemetry.io/docs/platforms/client-apps/](https://opentelemetry.io/docs/platforms/client-apps/)
    - Help wanted :)

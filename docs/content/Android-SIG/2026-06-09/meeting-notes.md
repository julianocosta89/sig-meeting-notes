## Meeting Notes

### Attendees
- Jason Splunk (Splunk)
- Hanson Ho [Embrace)
- Jason Morris (Embrace)
- David

### Agenda
- David - Interesting older issues: seem simple to close
  - [https://github.com/open-telemetry/opentelemetry-android/issues/1195](https://github.com/open-telemetry/opentelemetry-android/issues/1195)
  - [https://github.com/open-telemetry/opentelemetry-android/issues/379](https://github.com/open-telemetry/opentelemetry-android/issues/379)
    - This is done
    - Will eventually show up here: [https://play.google.com/sdks/categories/analytics](https://play.google.com/sdks/categories/analytics)
    - Curious if we can automate access to this, even if only partial, even if only periodic?
      - Probably see how helpful it actually is first
  - [https://github.com/open-telemetry/opentelemetry-android/issues/1286](https://github.com/open-telemetry/opentelemetry-android/issues/1286)
    - We are all a little suspicious about cpu count and these events
    - This comment [https://github.com/open-telemetry/opentelemetry-android/issues/1286#issuecomment-3370537803](https://github.com/open-telemetry/opentelemetry-android/issues/1286#issuecomment-3370537803) about monitoring thermal status and power save mode.
      - We should get issues open for these two
      - AI: Jason to take this issue creation
  - Jason is open to picking up new instrumentations around all of this, even tho it is more maintenance
    - Even if opt in or experimental and without semconv
      - That can come later.
- David - revisiting networking - an older related PR
  - [https://github.com/open-telemetry/opentelemetry-android/issues/1772](https://github.com/open-telemetry/opentelemetry-android/issues/1772)
    - We did a terrible job with this and basically ignored this person.
    - This seems like a good change to jason
    - AI: Jason to follow up with this and apologize and try and remedy.
- Hanson: [https://github.com/open-telemetry/opentelemetry-android/pull/1785/](https://github.com/open-telemetry/opentelemetry-android/pull/1785/)
  - Do we all like this approach?

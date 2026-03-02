## Meeting Notes

### Attendees
- Hanson Ho (Embrace)
- Jason (Splunk)
- Cesar (Elastic)
- Manoel (PostHog)
- cleverchuk(solarwinds)

### Agenda
- [Cesar] Disk buffering new api impl: [https://github.com/open-telemetry/opentelemetry-java-contrib/pull/2183](https://github.com/open-telemetry/opentelemetry-java-contrib/pull/2183)
  - Please review!
- [Hanson] Crash stuff
  - Related to [https://github.com/open-telemetry/opentelemetry-android/pull/1172](https://github.com/open-telemetry/opentelemetry-android/pull/1172) and last week’s discussion
  - (recap of some of last week)
  - session id’s relation to spans could/should be clarified – a span simply gets the session id at span start time.
  - Embrace keeps “state” of running spans and flushes to disk every 2 seconds.
    - And on launch these can be resurrected.
  - We still don’t have a great definition of Session.
  - But at least we have stubs on the website now if people want to start working on those:
    - [https://opentelemetry.io/docs/platforms/client-apps/](https://opentelemetry.io/docs/platforms/client-apps/)
  - [https://github.com/open-telemetry/opentelemetry-specification/issues/4604](https://github.com/open-telemetry/opentelemetry-specification/issues/4604)
- Feedback to the community README doesn’t mention clearly
- The release process updates the versions in the READMEs for instrumentation is not happening in the merge to main branch
  - AI: Jason to fix this
- Strict mode violation this issue [https://github.com/open-telemetry/opentelemetry-java/issues/7600](https://github.com/open-telemetry/opentelemetry-java/issues/7600)

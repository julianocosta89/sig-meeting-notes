## Meeting Notes

### Attendees
- Jason (Splunk)
- Hanson Ho (Embrace)
- Cesar (Elastic)
- Jamie Lynch (Embrace)
- Jairo (Honeycomb)
- [Gregor Zeitlinger](mailto:gregor.zeitlinger@grafana.com)(Gregor)

### Agenda
- Release v0.12.0 today
  - These need merge:
    - contrib/disk buffering [https://github.com/open-telemetry/opentelemetry-android/pull/1042](https://github.com/open-telemetry/opentelemetry-android/pull/1042)
    - Nice to have / build warnings [https://github.com/open-telemetry/opentelemetry-android/pull/1046](https://github.com/open-telemetry/opentelemetry-android/pull/1046)
      - AI: Jason to open issue to explore toolchains to see if we can get to a place where constant is only defined once. [https://docs.gradle.org/current/userguide/toolchains.html](https://docs.gradle.org/current/userguide/toolchains.html)
      - [https://github.com/open-telemetry/opentelemetry-android/issues/1051](https://github.com/open-telemetry/opentelemetry-android/issues/1051)
    - Prepare changelog: [https://github.com/open-telemetry/opentelemetry-android/pull/1048](https://github.com/open-telemetry/opentelemetry-android/pull/1048)
- Disk buffering PR [https://github.com/open-telemetry/opentelemetry-android/pull/1042/files](https://github.com/open-telemetry/opentelemetry-android/pull/1042/files)
  - Is there an opportunity to move some of the setup/configuration into contrib
    - It’s currently a little bit cumbersome
    - Can we find a balance?

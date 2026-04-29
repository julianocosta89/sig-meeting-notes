## Meeting Notes

### Attendees
- Jason (Splunk)
- Martin Kuba (Grafana Labs)
- João Oliveira (Datadog)
- Santosh Cheler (Splunk)

### Agenda
- (Jason) Please add feedback to crash handling semantic convention
  - This PR: [https://github.com/open-telemetry/semantic-conventions/pull/3448](https://github.com/open-telemetry/semantic-conventions/pull/3448)
  - Android PR: [https://github.com/open-telemetry/opentelemetry-android/pull/1691](https://github.com/open-telemetry/opentelemetry-android/pull/1691)
- [santosh] Metrics API in RUM - I am turning around as well and am now in favor of using it.
  - Devs often want to measure how long something takes
  - Usually aggregated (broadly)
    - Where to drop dimensions tho?
    - [https://github.com/open-telemetry/opentelemetry-android/pull/1064](https://github.com/open-telemetry/opentelemetry-android/pull/1064) (one bad idea maybe doing this on the client side)
    - Doing this in the pipeline/backend is way more powerful, but comes with the cost to the users (bandwidth, connections in unstable networks, etc)
- (jason) FYI Android has stabilized the session API
  - [https://github.com/open-telemetry/opentelemetry-android/releases/tag/v1.3.0](https://github.com/open-telemetry/opentelemetry-android/releases/tag/v1.3.0)

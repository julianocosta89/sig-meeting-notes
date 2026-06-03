## Meeting Notes

### Attendees
- Hanson Ho (Embrace)
- Jason Plumb (Splunk)
- Cesar (Elastic)

### Agenda
- [Jason P] - Network change detection limitations
  - [https://github.com/open-telemetry/opentelemetry-android/issues/1772](https://github.com/open-telemetry/opentelemetry-android/issues/1772)
  - Maybe the underlying platform API doesn’t report all of them?
  - [https://developer.android.com/reference/android/net/ConnectivityManager#getAllNetworks()](https://developer.android.com/reference/android/net/ConnectivityManager#getAllNetworks())
  - So maybe it’s fine as is after all
    - We should at least document this better
  - You can be on one network, but when it’s degraded another may be used
- [Jason P] - Do we like using the kotlin semconv even though they are young?
  - Merged yesterday before I logged in….so yes!? LOL
  - AI: Jason to open issue in kotlin to recreate [https://github.com/open-telemetry/semantic-conventions-java/pull/489/changes#diff-530dcf8176986b8f0e53f1c6b02978cf4d50f5b2173c3ceae6788db2e8a0dbb5](https://github.com/open-telemetry/semantic-conventions-java/pull/489/changes#diff-530dcf8176986b8f0e53f1c6b02978cf4d50f5b2173c3ceae6788db2e8a0dbb5) in kotlin
- [David] Is “view-click” still a correct name at this point?
  - [https://github.com/open-telemetry/opentelemetry-android/pull/1780](https://github.com/open-telemetry/opentelemetry-android/pull/1780)
  - Sounds like we like “gesture” as a new module
    - May necessitate a common between view-click
- Hanson - Google play services stuff?
  - Never been closer…
- Cesar is out next week

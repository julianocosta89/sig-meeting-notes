## Meeting Notes

### Attendees
- Martin Kuba (Grafana Labs)
- Hanson Ho (Embrace)
- Jason (Splunk)
- João Oliveira (Datadog)
- Cleo Schneider (Firebase/Google)
- Bryan Atkinson (Firebase/Google)

### Agenda
- [Hanson] “Async” telemetry
  - Async may not be the right word – perhaps buffered, replayed, or delayed telemetry?
  - The problem is that the thing reporting the telemetry may not be the same thing as what generated it
    - One example: tombstones and app exit info on android
    - …and if the next launch were to export that tombstone it would be associated with the wrong session/resource.
    - Profiling / profetto artifacts?
    - ANR exit
  - The instrumentation/agent probably needs to persist a record of { session, resource } for the next thing to pick up.
  - Would be interesting to see an experiment that tries to do this,
    - Could help identify where the rough edges are
  - Can we bypass the apis and just build data to pass to an exporter?
  - AI: Hanson to open issue to discuss
    - Spec an attribute that indicates that a crash came from a “prior” session/instance/run/launch
    - Is it a boolean? Or is it the whole darn resource? Or a subset of resource?
- [jason] Crash event semconv was merged, so please use it :) [https://github.com/open-telemetry/semantic-conventions/pull/3448](https://github.com/open-telemetry/semantic-conventions/pull/3448)

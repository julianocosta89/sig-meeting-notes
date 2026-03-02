## Meeting Notes

### Attendees
- Tyler Yahn (Splunk)
- Robert Pająk (Splunk)
- [Owen Williams](mailto:owen.williams@grafana.com)(Grafana)
- [dashpole@google.com](mailto:dashpole@google.com) (Google)

### Agenda
- [[David Ashpole](mailto:dashpole@google.com)] [https://github.com/open-telemetry/opentelemetry-go/pull/7175](https://github.com/open-telemetry/opentelemetry-go/pull/7175)
  - Benchmarks show a massive improvement (>90% when 10 attributes are used, single threaded) for the metrics SDK.
  - Questions for the meeting:
    - [David Ashpole](mailto:dashpole@google.com) thinks we should adopt this. Do others agree?
      - Yes.  The consensus is that we should move this forward.
    - Tyler, what else needs to be done to the PR before it is ready? (seems ready to me, but haven’t looked closely at fnv).
      - Left comments
    - Should we add this behind a feature gate, or can we go ahead and make the change?
      - No
- [Tyler] Milestone v1.38.0:
  - [Otel](https://github.com/open-telemetry/opentelemetry-go/milestone/73)
  - [Contrib](https://github.com/open-telemetry/opentelemetry-go-contrib/milestone/32)
- [Owen] final notes on [https://github.com/open-telemetry/opentelemetry-go/pull/7111](https://github.com/open-telemetry/opentelemetry-go/pull/7111) , do we need to worry about handling invalid "translation strategy" strings? And any other thoughts before merge?

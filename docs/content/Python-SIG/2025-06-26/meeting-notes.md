## Meeting Notes

### Attendees
- Radhika Gupta(Microsoft)
- Riccardo Magliocchetti (Elastic)
- Dylan Russell (google)
- Ezzio Moreira
- Shuwen Pan (Cisco)
- Leighton Chen (Microsoft)
- Aaron Abbott (Google)
- Pablo Collins (Splunk/Cisco)
- Jeremy Voss (Microsoft)

### Agenda
- [aaron] The GC and TC are collecting feedback from all SIGs in order to put together a roadmap (past and future) to share with the community:
  - What were the SIG's biggest achievements during the last 12 months?
    - [emidio] Support opt-in for stable http semconv in instrumentations (-contrib)
    - [emidio] Support for Python 3.13 (both)
    - [emidio] Implementation of Exemplars (-core)
    - Genai stuff?
  - What work is the SIG planning for the upcoming 12 months?
    - [aaron] Configuration SDK yaml? Brought up in GenAI SDK
    - [emidio] Stabilize Logs:
  - Are there any areas and/or sub projects that the GC/TC can help with? (e.g. cross-SIG blockers, prioritization, etc)
    - [emidio] [https://github.com/open-telemetry/community/issues/2127](https://github.com/open-telemetry/community/issues/2127) – this was opened for .net but we can also benefit this to have an app like opentelemetrybot to do more automations for release (like working with labels) – See also [https://github.com/open-telemetry/opentelemetry-python-contrib/issues/3444](https://github.com/open-telemetry/opentelemetry-python-contrib/issues/3444)
- [riccardo]  Merge logs / events PR for next release?
  - [https://github.com/open-telemetry/opentelemetry-python/pull/4647](https://github.com/open-telemetry/opentelemetry-python/pull/4647)
  - [https://github.com/open-telemetry/opentelemetry-python/pull/4654](https://github.com/open-telemetry/opentelemetry-python/pull/4654)
  - Looks like we’re merging after review
- [dylan]
  - How long between deprecation warning and deprecating events API/SDK ?
    - We haven’t removed anything deprecated yet
  - We usually never removed deprecated code but will revisit after every instrumentation is updated
    - [riccardo] I have an out-of-tree instrumentation using events :)
  - [dylan] should we keep using the event_name attribute?
    - [leighton] check with genai people
    - [spec people] should be fine to switch because it was experimental but check with instrumentations devs
    - [aaron] if they stay with old events api they would be fine for now
- [riccardo] Proper-ish http user agent for grpc exporter  [https://github.com/open-telemetry/opentelemetry-python/pull/4658](https://github.com/open-telemetry/opentelemetry-python/pull/4658)
  - Distros would be able to override the value with [https://github.com/open-telemetry/opentelemetry-python/pull/4659](https://github.com/open-telemetry/opentelemetry-python/pull/4659)

## Meeting Notes

### Attendees
- Hector Hernandez (Microsoft)
- Riccardo Magliocchetti (Elastic)
- Aaron Abbott (Google)
- Keith Decker (Cisco/Splunk)
- Dylan russell (google)
- Lukas Hering (Capital One)

### Agenda
- [Riccardo] Logs stabilization update
  - [https://github.com/open-telemetry/opentelemetry-python/pull/4647](https://github.com/open-telemetry/opentelemetry-python/pull/4647) merged! Thanks Hector!
  - Next steps:
    - go after documentation / examples / [opentelemetry.io](http://opentelemetry.io), [https://github.com/open-telemetry/opentelemetry-python/issues/4750#issuecomment-3556824627](https://github.com/open-telemetry/opentelemetry-python/issues/4750#issuecomment-3556824627)
    - Ping downstream users to check main:
      - Pinged Alex@logfire and one reporter of missing replacement for deprecations for feedback
      - Filed [https://github.com/traceloop/openllmetry/issues/3451](https://github.com/traceloop/openllmetry/issues/3451) for sending logrecords instead of events on recent sdks (1.37.0+), so we can deprecate that too :)
    - @Hector: Need to update -contrib PR to work with both as we are testing against older api/sdks [https://github.com/open-telemetry/opentelemetry-python-contrib/pull/3589](https://github.com/open-telemetry/opentelemetry-python-contrib/pull/3589)
- [Riccardo] Fellow distro maintainers PTAL on being able to provide your own processor to sdk config with autoinstrumentation [https://github.com/open-telemetry/opentelemetry-python/pull/4806](https://github.com/open-telemetry/opentelemetry-python/pull/4806)
  - Aaron: take a look at entry points
- [Keith] - GenAI Inference Metrics PR for review : [https://github.com/open-telemetry/opentelemetry-python-contrib/pull/3891/](https://github.com/open-telemetry/opentelemetry-python-contrib/pull/3891/)
- [Riccardo] Adding Liudmila as an approver

## Meeting Notes

### Attendees
- Ted Young (Grafana Labs)
- Daniel Dyla
- Dmitry Anoshin
- Josh Suereth
- Martin Kuba

### Agenda
- Reminder - review [https://github.com/open-telemetry/opentelemetry-specification/pull/4836](https://github.com/open-telemetry/opentelemetry-specification/pull/4836)
- SDK - [https://github.com/open-telemetry/opentelemetry-specification/pull/5057](https://github.com/open-telemetry/opentelemetry-specification/pull/5057)
  - Long discussion on startup async vs. sync
    - Most SDKs can make HTTP calls sync - everything is fine
    - JS may need explicit callout here
    - AI
      - Relax wording for entities version of what JS already does. (Could alleviate issues with resource processor)
      - Try to make a version of Spec that relaxes wording that allows an async export pipeline - see if this works or is broken.
- Identity - [https://github.com/open-telemetry/opentelemetry-specification/pull/5067](https://github.com/open-telemetry/opentelemetry-specification/pull/5067)
  - Do we want to emit entities with existing detectors?
  - When specifying list of detectors for SDKs using configuration, we should try to have these work with Entities.
- [martin] Browser update
  - [Updated prototype](https://github.com/open-telemetry/opentelemetry-browser/pull/269)
  - Discussions
    - [Mutable entities](https://github.com/open-telemetry/opentelemetry-browser/discussions/265)
    - [Metrics in browser](https://github.com/open-telemetry/opentelemetry-browser/discussions/266)
- [dmitry]
  - [https://github.com/open-telemetry/opentelemetry-specification/pull/4836](https://github.com/open-telemetry/opentelemetry-specification/pull/4836)

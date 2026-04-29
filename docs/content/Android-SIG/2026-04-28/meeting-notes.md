## Meeting Notes

### Attendees
- Jason (Splunk)
- Cesar (Elastic)
- Cleverchuk (Solarwinds)
- <you>

### Agenda
- [David] - Double Tap PR: [https://github.com/open-telemetry/opentelemetry-android/pull/1681](https://github.com/open-telemetry/opentelemetry-android/pull/1681)
  - (jason) Looks good to me is there anything else remaining?
  - Can we get this also wired into the demo app?
    - AI: Jason to create issue after merging
- Crash PR is awaiting [https://github.com/open-telemetry/semantic-conventions/pull/3448](https://github.com/open-telemetry/semantic-conventions/pull/3448)
  - Needs more approvals, please review
- Stabilization – what’s next?
  - Instrumentation API stability
- (cleverchuk)
  - Will Android have declarative config?
    - Yes, but probably not too soon, but we should be working toward it
  - Kotlin project?
    - Moving ahead pretty quickly
    - Help wanted.
- (doing some issue triaging)
  - Looking at [https://github.com/open-telemetry/opentelemetry-android/issues/1378](https://github.com/open-telemetry/opentelemetry-android/issues/1378)
    - Brings up some interesting ideas around what should be in the agent
      - Should we allow customization of tracer provider to inject custom SpanProcessors
    - We can/should expand the agent, but only where really needed
  - (jason) Might be nice to have some prescriptive use-case based docs around using the agent for certain scenarios
    - Common scenarios / use cases
    - On the docs/io site
  - Session id callback provider:
    - [https://github.com/open-telemetry/opentelemetry-android/issues/328](https://github.com/open-telemetry/opentelemetry-android/issues/328)
    - There’s no simple way to do this today through the agent, but we think we probably should add it to the DSL to make it more convenient, especially now that the session api is stable.
  - Milestone for instrumentation api stabilization
    - [https://github.com/open-telemetry/opentelemetry-android/milestone/5](https://github.com/open-telemetry/opentelemetry-android/milestone/5)
    - [https://github.com/open-telemetry/opentelemetry-android/issues/411](https://github.com/open-telemetry/opentelemetry-android/issues/411) programmatically disable instrumentation on classpath

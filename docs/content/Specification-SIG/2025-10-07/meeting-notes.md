## Meeting Notes

### Attendees
- Josh
- Nathan Smith
- Dmitry Anoshin
- [Daniel Dyla](mailto:dyladan@gmail.com)

### Agenda
- [josh] OTEP -  [https://github.com/open-telemetry/opentelemetry-specification/pull/4665](https://github.com/open-telemetry/opentelemetry-specification/pull/4665)
  - [daniel] Why resource initializer has to handle waiting for initialization and notifying rest of SDK
    - Javascript Resource today -  All detectors are synchronous, but attributes can be promises or values.
    - Conflicts on configuration-order / detection-order basis.
    - What do you do if we don't know which entities are being returned?
      - You should know what's possible and provide "stub values" ahead of time.
    - In Java we try to avoid having everyone need to know about async/await and limit the need to deal with this to certain specific pieces.   This is not viable for JavaScript.
  - Principles
    - Specification needs to allow synchronous startup, should not block for certain types of entity lookup (e.g. hitting GCP metadataserver, or any remote API like k8s)
    - Uninitialized / Async should NOT bleed across the entire SDK
      - We want the first time you need to understand async startup is *export* or interaction with resource via samplers/proccessors
  - Resource w/ Entity vs. InstrumentationScope with Entity.
    - Usability issues
    - Breaking change issues
      - Would we need to push a lot of attributes from Resource -> InstrumentationScope
  - Alternative:
    - SDK has a "core" Resource
      - meterProvider.get(...) <- uses core resource
    - You can add/layer additional resource information on the SDK.
      - meterProvider.for(entity).get(...) <- Layers a specific entity on resource
- Lifetime APIs
  - We need some way to mark a "sub provider" as done
    - We can just re-use shutdown here.
  - Other TODOs
    - What is the relationship implied with multiple entities on a resource?

## Meeting Notes

### Attendees
- [Surbhi] (Cisco Systems)
- Jason - Splunk
- Jamie - Embrace
- Cesar - Elastic
- Hanson Ho - Embrace
- Francisco - Embrace
- Cleverchuk - Solarwinds

### Agenda
- [Surbhi] - Discuss new updates on network timing attributes and get reviews for the following PR:
  - [https://github.com/open-telemetry/opentelemetry-java-instrumentation/pull/15664](https://github.com/open-telemetry/opentelemetry-java-instrumentation/pull/15664)
  - LogRecordBuilder.setContext() - [https://github.com/open-telemetry/opentelemetry-java/blob/main/api/all/src/main/java/io/opentelemetry/api/logs/LogRecordBuilder.java#L68](https://github.com/open-telemetry/opentelemetry-java/blob/main/api/all/src/main/java/io/opentelemetry/api/logs/LogRecordBuilder.java#L68)
  - Ensure that the context is correct, awesome.
  - Let’s just make it an event - set the eventName field instead of attribute.
  - Semconv issue: [https://github.com/open-telemetry/semantic-conventions/issues/2827](https://github.com/open-telemetry/semantic-conventions/issues/2827)
  - Should we use spans for these durations? Are we mixing up signals?
    - Using spans is definitely larger (IDs)
  - Is this feature opt-in? Jason doesn’t want this to be turned on by default.
  - Separate issue to wire up config to build-time autoinstrumentation?
    - [https://github.com/open-telemetry/opentelemetry-android/issues/1267](https://github.com/open-telemetry/opentelemetry-android/issues/1267)
  - Let’s also put the copying of attributes  behind a
- [Cesar] Proposal for instrumentation api changes before going stable: [https://github.com/open-telemetry/opentelemetry-android/issues/1541](https://github.com/open-telemetry/opentelemetry-android/issues/1541)
  - Option 1: [https://github.com/open-telemetry/opentelemetry-android/pull/1539](https://github.com/open-telemetry/opentelemetry-android/pull/1539)
  - Option 2: [https://github.com/open-telemetry/opentelemetry-android/pull/1540](https://github.com/open-telemetry/opentelemetry-android/pull/1540)
  - Should the shutdown/flush just be part of the sdk?
    - Why build it into the instrumentation?
  - Does the current implementation create a race between the two flushes?
- Please take a look at io/docs site PR: [https://github.com/open-telemetry/opentelemetry.io/pull/8713](https://github.com/open-telemetry/opentelemetry.io/pull/8713)

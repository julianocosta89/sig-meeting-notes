## Meeting Notes

### Attendees
- Jason - Splunk
- Jamie - Embrace
- Cesar - Elastic
- Francisco - Embrace
- Mustafa - Honeycomb

### Agenda
- AGP 9
  - Breaks backwards compatibility
  - Google makes it hard to stay on old versions
  - Do we need a compatibility matrix / supportability table?
  - AGP 9 wants you to not include kotlin manually, kotlin version is built-in now
  - Can we built CI integration to verify the min versions?
    - Alway test the latest version (at some point it was tested/verified with older ones)
  - AGP 9.0 bring kotlin 2.2 [https://docs.gradle.org/current/userguide/compatibility.html](https://docs.gradle.org/current/userguide/compatibility.html) for internal
    - Is it uset at runtime or only compile time?
    - Upgrade guide [https://docs.gradle.org/current/userguide/upgrading_version_9.html#changes_9.3.0](https://docs.gradle.org/current/userguide/upgrading_version_9.html#changes_9.3.0)
- Min required versions
- ‘Escape hatch’ for allowing folks to configure OpenTelemetry via OpenTelemetryRumInitializer
  - Exposing the OTel Java API via the initializer?
  - Adding custom processors
  - Should we expose the [sdk builder?](https://github.com/open-telemetry/opentelemetry-java/blob/main/sdk/all/src/main/java/io/opentelemetry/sdk/OpenTelemetrySdkBuilder.java)
  - If we go with this route, would it make “core” apis redundant?
  - Do we need to expose the whole API or only a case by case as needed
  - [https://github.com/open-telemetry/opentelemetry-android/issues/1482](https://github.com/open-telemetry/opentelemetry-android/issues/1482) related
  - For the use case above, exposing the whole OTel Java builder wound’t help, as our exporters wouldn’t be modifiable from the outside.
- Bump minSdk version to 23
- Creating a new release this week.

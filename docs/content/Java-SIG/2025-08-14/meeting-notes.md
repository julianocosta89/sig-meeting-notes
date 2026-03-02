## Meeting Notes

### Attendees
- [John Watson](mailto:jkwatson@gmail.com) (Cloudera)
- Jason (Splunk)
- Jay DeLuca (Grafana Labs)
- Jonathan Halliday (IBM)
- Trask Stalnaker (Microsoft)
- Jack Shirazi (Elastic)
- Robert Niedziela (Splunk)
- Evan Torrie (self)
- Pranav Sharma (Google)

### Agenda
- [Gregor] What are impediments to dynamic loading for Java agent?
  - Attaching agent after starting the process
  - Maybe related? [https://github.com/raphw/byte-buddy/issues/1845](https://github.com/raphw/byte-buddy/issues/1845)
  - [https://github.com/open-telemetry/opentelemetry-java-instrumentation/issues/1932](https://github.com/open-telemetry/opentelemetry-java-instrumentation/issues/1932)
  - Would need test coverage for that
  - Sometimes we instrument the builder method (or something else that only runs at app startup
    - so a different instrumentation would be needed
- [jkwatson] What is the goal of the collector/prometheus integration test? [https://github.com/open-telemetry/opentelemetry-java/issues/7544](https://github.com/open-telemetry/opentelemetry-java/issues/7544)
  - AI Gregor to pin collector version with renovate updates
- [Gregor] renaming attributes in contrib [https://github.com/open-telemetry/semantic-conventions/pull/2589](https://github.com/open-telemetry/semantic-conventions/pull/2589)
  - Are we allowed to do that? Yes, just call out in changelog
- [Antoine] IBM MQ metrics [https://github.com/open-telemetry/opentelemetry-java-contrib/pull/1960](https://github.com/open-telemetry/opentelemetry-java-contrib/pull/1960)
- Instrumentation release
- [Gregor] naming of enabled instrumentations in declarative configuration (see previous meeting notes)
  - Split off into a new PR [https://github.com/open-telemetry/opentelemetry-java-instrumentation/issues/14432](https://github.com/open-telemetry/opentelemetry-java-instrumentation/issues/14432)
- [jason] Shadow major upgrade [https://github.com/open-telemetry/opentelemetry-java-instrumentation/pull/14388](https://github.com/open-telemetry/opentelemetry-java-instrumentation/pull/14388)
  - Might benefit from gradle 9 first? Not sure. [https://github.com/open-telemetry/opentelemetry-java-instrumentation/pull/14355](https://github.com/open-telemetry/opentelemetry-java-instrumentation/pull/14355)
  - Here’s what android had: [https://github.com/open-telemetry/opentelemetry-android/pull/1126](https://github.com/open-telemetry/opentelemetry-android/pull/1126)

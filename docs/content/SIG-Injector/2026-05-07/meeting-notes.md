## Meeting Notes

### Attendees
- Jack Berg (Grafana Labs)
- Nikola Grcevski (Grafana Labs)
- Bastian Krol (Dash0)
- Michele

### Agenda
- ~~[Nikola] Make a new release with the .NET fixes?~~
- [Bastian] [https://github.com/open-telemetry/opentelemetry-injector/issues/332](https://github.com/open-telemetry/opentelemetry-injector/issues/332) – base image versions used in tests
  - We might need to support a rather large set of distros (also older ones) ultimately
  - Other dimensions:
    - language versions ([Node.js](http://Node.js) version, .NET version, JVM version, …)
  - Large matrix on CI is fine, locally the default should be to run latest/current-stable/…
  - the “large” test matrix should probably not be in the packaging tests, but in a faster/smaller test setup (e.g. injector-integration-test or something new entirely)
    - ideally we get notified automatically when a new version of something comes out, e.g. via Renovate (see [https://github.com/open-telemetry/opentelemetry-java/blame/b29f3df1ff7dea14b8372999f54af40eca6c1fbb/.github/workflows/build.yml#L34](https://github.com/open-telemetry/opentelemetry-java/blame/b29f3df1ff7dea14b8372999f54af40eca6c1fbb/.github/workflows/build.yml#L34) for and example)
  - the packaging test might go to another repo somewhat soon anyway

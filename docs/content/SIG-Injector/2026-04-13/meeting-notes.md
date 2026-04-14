## Meeting Notes

### Attendees
- Ted Young (Grafana Labs)
- Jack Berg (Grafana Labs)
- Nikola Grcevski (Grafana Labs)

### Agenda
- [Ted] Configuration
  - Multiple packages contributing to the same conf file will be painful
  - Split the file up in a conf.d approach, using a directory per conf file
  - This would break compatibility, but that could be acceptable because it is still experimental
  - Two options:
    - Support both directory structures for a time, with a warning
    - Just rip the bandaid off
      - We’re (genuine) 0.X, so we’re going with this approach
- [jack] Fixing issues running on RHEL, and release schedule [https://github.com/open-telemetry/opentelemetry-injector/issues/311](https://github.com/open-telemetry/opentelemetry-injector/issues/311)
  - Four separate issues
    - Fix include/exclude evaluation (merged): [https://github.com/open-telemetry/opentelemetry-injector/pull/312](https://github.com/open-telemetry/opentelemetry-injector/pull/312)
    - Evaluate include/exclude before libc detection [https://github.com/open-telemetry/opentelemetry-injector/pull/313](https://github.com/open-telemetry/opentelemetry-injector/pull/313)
    - Fix RHEL libc detection: TODO
    - Ship default include/exclude config: [https://github.com/open-telemetry/opentelemetry-injector/pull/315](https://github.com/open-telemetry/opentelemetry-injector/pull/315)
- [Ted] System packaging proposal update, copied from [here](https://github.com/open-telemetry/community/pull/3252):
  - We want to have each language have a monolith that works something like the java agent, that has a single version number and chooses which packages to include based on stability.
- Build an `opentelemetry` package that installs all of the sub-packages.
- Design a release cadence and configuration for the `opentelemetry` package.
- Design all of the configuration, scaffolding and layout to start adding individual sub-packages.
- Build a package for the Collector.
- Build a package for OBI.
- Identify which languages have blocking issues, and cannot be added. Record these blockers as issues, and discuss them with language maintainers to determine a viable timeline for improvement in each language.
- For languages that do not have blocking issues, add the SDK, plugins, and instrumentation behind the `unstable` flag. During phase 1, no languages should be installable without the `unstable` flag as we still may break any piece of our design.
- Identify which instrumentation packages are ready to be marked as stable.
- Only marking packages as stable once there is a plan for how they will be maintained.

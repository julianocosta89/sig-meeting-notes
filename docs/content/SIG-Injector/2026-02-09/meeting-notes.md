## Meeting Notes

### Attendees
- Nikola Grcevski (Grafana)
- Ted Young (Grafana Labs)
- Bastian Krol (Dash0)
- Antoine Toulme (Splunk)

### Agenda
- [Ted] System packages SIG
  - [https://github.com/open-telemetry/community/pull/3252](https://github.com/open-telemetry/community/pull/3252)
  - Staffing?
    - We need a point of contact for each Language SIG.
      - AI: Ted will find someone for Java, .NET, Python, Ruby, and Go
      - AI: Nikola will look into adding selection criteria to OBI to support Go
  - If we are going to add a new column to the Status table for all languages, what would that column be? “Linux”?
- [Nikola] Python SIG update on the http/json export:
  - *Update from the SIG meeting on Feb 5th 2026. We want to go with a code generation approach with a protoc plugin. [@herin049](https://github.com/herin049) already has a prototype for this and thinks it is feasible, will open a draft PR. -> [https://github.com/open-telemetry/opentelemetry-python/pull/4902](https://github.com/open-telemetry/opentelemetry-python/pull/4902)*
- [Antoine] Release cycle
  - [https://github.com/open-telemetry/opentelemetry-injector/pull/237](https://github.com/open-telemetry/opentelemetry-injector/pull/237)
    - We can formalize a release process a bit later
    - Just want to make sure we don’t have just one person know how to release
    - Last release some good learnings
    - Packaging SIG will eventually build SDKs and there will be no need for regular releases
    - Blocker: renovate
- [Michele] Ruby support?
  - Ted: not much bandwidth
  - Antoine: problem is testing
  - Seems like a good idea as a compatibility matrix for language support
  - Project infra SIG - ask for deb/rpm support or come up with gh-pages
- [Bastian]
  - Release with Github app otelbot? (see [Slack thread](https://cloud-native.slack.com/archives/C09025GKPAL/p1770208660407039?thread_ts=1770115609.569199&cid=C09025GKPAL)) -> [https://github.com/open-telemetry/opentelemetry-injector/issues/252](https://github.com/open-telemetry/opentelemetry-injector/issues/252)
  - Anyone has cycles to look into [https://github.com/open-telemetry/opentelemetry-injector/issues/73](https://github.com/open-telemetry/opentelemetry-injector/issues/73)? (Renovate updates for auto-instrumentation agents)

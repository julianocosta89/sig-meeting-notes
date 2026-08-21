## Meeting Notes

### Attendees
- [John Watson](mailto:jkwatson@gmail.com)(Sublime Security)
- Sylvain Juge (Elastic)
- Jack Berg (Grafana Labs)
- Jason (Splunk)
- Trask Stalnaker (Microsoft)
- [Gregor Zeitlinger](mailto:gregor.zeitlinger@grafana.com) (Grafana Labs)
- Pranav Sharma (Google)
- Peter Findeisen (Cisco)
- Mohammed Abdessetar Elyagoubi (Sofrecom)
- Jonathan Halliday (IBM)
- Cleverchuk (Solarwinds)
- Surya Teja
- Jack Shirazi (Elastic)

### Agenda
- [jason] Would otlp-http be a welcome addition to the smoke-test-fake-backend?
  - Checking before offering to help with that work.
  - In android, we’re starting to build some [on-device smoke tests](https://github.com/open-telemetry/opentelemetry-android/pull/1972) and want to be able to reuse the smoke-test-fake-backend from the instrumentation repo.
  - As seen [here](https://github.com/breedx-splk/opentelemetry-android/pull/7), we can work around it with a collector, but it’s heavier and unfortunate.
- [jack] Can we make progress on this PR to add OTLP option to setEnabledProtocols? [https://github.com/open-telemetry/opentelemetry-java/pull/8610](https://github.com/open-telemetry/opentelemetry-java/pull/8610)
- [trask] JVM semantic conventions
  - [https://github.com/open-telemetry/semantic-conventions/pull/3970](https://github.com/open-telemetry/semantic-conventions/pull/3970)
  - [https://github.com/open-telemetry/semantic-conventions/pull/4019](https://github.com/open-telemetry/semantic-conventions/pull/4019)
- [Surya] PR for introducing genai semantic conventions in java instrumentation
  - [https://github.com/open-telemetry/opentelemetry-java-instrumentation/pull/19124](https://github.com/open-telemetry/opentelemetry-java-instrumentation/pull/19124)
- AI generated contributions?
  - [https://cloud-native.slack.com/archives/C01NJ7V1KRC/p1787153432689459](https://cloud-native.slack.com/archives/C01NJ7V1KRC/p1787153432689459)
  - Umbrella project policy [https://github.com/open-telemetry/community/blob/main/policies/genai.md](https://github.com/open-telemetry/community/blob/main/policies/genai.md)
  - [https://github.com/trask/copilot-plugins/tree/main/plugins/pr-reviewer](https://github.com/trask/copilot-plugins/tree/main/plugins/pr-reviewer)
  - [https://github.blog/changelog/2026-08-12-agent-plugins-1-0-in-vs-code-copilot-cli-and-the-copilot-app/](https://github.blog/changelog/2026-08-12-agent-plugins-1-0-in-vs-code-copilot-cli-and-the-copilot-app/)

## Meeting Notes

### Attendees
- Trent Mick (Elastic)
- David Luna (Elastic)
- Marc Pichler (Dynatrace)
- Marten Hennoch (Cisco)
- Marylia (Grafana)
- Jackson Weber (Microsoft)
- Hector Hernandez (Microsoft)

### Agenda
- [Trent] Perhaps chat about [https://github.com/open-telemetry/opentelemetry-js/pull/6640](https://github.com/open-telemetry/opentelemetry-js/pull/6640) plan for a bit: sdk-trace sans envvars.
- [Trent] could also talk about Marc’s PluginComponentProvider PoC ([https://github.com/open-telemetry/opentelemetry-js/pull/6730](https://github.com/open-telemetry/opentelemetry-js/pull/6730))
- [Marten] [https://github.com/open-telemetry/opentelemetry-js-contrib/pull/3454](https://github.com/open-telemetry/opentelemetry-js-contrib/pull/3454)
  - Needs rerun and merge
  - TODO(trent): open issue to have contrib repo docs:test link check that only runs against changes. Or just move docs:test to weekly separate run. -> [https://github.com/open-telemetry/opentelemetry-js/issues/6766](https://github.com/open-telemetry/opentelemetry-js/issues/6766)
  - TODO: open issue to retry starting docker services in “unit-test” CI in contrib repo -> [https://github.com/open-telemetry/opentelemetry-js-contrib/issues/3550](https://github.com/open-telemetry/opentelemetry-js-contrib/issues/3550)
- [Trent] Perhaps review work for [SDK 3.0 milestone](https://github.com/open-telemetry/opentelemetry-js/milestone/20)? (And the [Logs API/SDK milestone](https://github.com/open-telemetry/opentelemetry-js/milestone/19).) June is next week.
  - Add issue(s) for releasing from a 2.x branch -> [https://github.com/open-telemetry/opentelemetry-js/issues/6767](https://github.com/open-telemetry/opentelemetry-js/issues/6767)
  - Add prerelease workflow for main branch -> [https://github.com/open-telemetry/opentelemetry-js/issues/6768](https://github.com/open-telemetry/opentelemetry-js/issues/6768)
  - Create issue for 3.0 announcement
    - Ask folks to bring their issues that would be breaking
- …
- [Untriaged bugs](https://github.com/open-telemetry/opentelemetry-js/issues?q=is%3Aissue+is%3Aopen+label%3Atriage+label%3Abug+-label%3Apriority%3Ap1++-label%3Apriority%3Ap2++-label%3Apriority%3Ap3++-label%3Apriority%3Ap4+)
- [Untriaged contrib bugs](https://github.com/open-telemetry/opentelemetry-js-contrib/issues?q=is%3Aissue+is%3Aopen+label%3Atriage%2Cbug+-label%3Apriority%3Ap1++-label%3Apriority%3Ap2++-label%3Apriority%3Ap3++-label%3Apriority%3Ap4)
- [Old Contrib PR Triage](https://github.com/open-telemetry/opentelemetry-js-contrib/pulls?q=is%3Apr+is%3Aopen+sort%3Acreated-asc)
- [Old Core PR Triage](https://github.com/open-telemetry/opentelemetry-js/pulls?q=is%3Apr+is%3Aopen+sort%3Acreated-asc)

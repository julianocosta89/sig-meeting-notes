## Meeting Notes

### Attendees
- [Andrzej Stencel](mailto:andrzej.stencel@elastic.co) (Elastic)
- Antoine Toulme (Splunk)
- [Evan Bradley](mailto:google@evanbradley.org) (Dynatrace)
- [Yang Song](mailto:yang.song@datadoghq.com) (Datadog)
- Pablo Baeyens (Datadog)
- Israel Blancas (Coralogix)
- Yasmine Elayyat (Ex-Microsoft)
- Tiffany Hrabusa (Grafana Labs)
- [Jade Guiton](mailto:jade.guiton@datadoghq.com) (Datadog)
- Mohammed ElDegwi
- Alex Boten (Honeycomb)
- Andy Keller (Dynatrace)
- Edmo Vamerlatti (Elastic)
- Dakota Paasman (Dynatrace)
- Douglas Camata (Coralogix)
- Josh MacDonald (Microsoft)

### Agenda
- [15 min] Go through high priority issues for [stability phase 1](https://github.com/open-telemetry/opentelemetry-collector-contrib/issues/44130) listed on the [**board**](https://github.com/orgs/open-telemetry/projects/178)
- Inform [announcement][Pablo] Bloomberg mentorship is starting; expect to see new faces from Bloomberg contributing to the Collector
  - See [https://www.bloomberg.com/company/stories/sustaining-opentelemetry-cncf-moving-from-dependency-management-to-stewardship/](https://www.bloomberg.com/company/stories/sustaining-opentelemetry-cncf-moving-from-dependency-management-to-stewardship/)
- Discuss [Pablo] Improving async experience for Collector contributions
  - Minimal change: We could have a rotating person that acts as a 'scribe'/'notetaker' and posts notes on #otel-collector-dev for the most important topics
    - Sounds like a good idea but there were not volunteers to do this
  - We can change the meeting notes structure also to make them more useful (separate announcements, PR review/merge asks)
    - From Tiffany: we can use Decide-Action-Discuss-Inform:
      - Decide - Time sensitive, consensus needed from the whole group
      - Action - Single owner sought, or someone to own answering/responding
      - Discuss - General discussion, may lead to an action;
      - Inform - Can be read async if you’ve run out of time, requires no input at all
    - We can try that out today
- Inform [Evan] I want to stabilize confmap’s validation functionality. It’s gone largely untouched for a year now without issues that I’m aware of.
- Discuss [Pablo] Slack reminders for ready-to-merge and RFC final comment period on #otel-collector-dev. Good idea? Spammy? Anything else you would like to see?
  - [https://github.com/open-telemetry/opentelemetry-collector/pull/15172](https://github.com/open-telemetry/opentelemetry-collector/pull/15172)
  - We will go ahead and try this out and discuss again in the future
- Discuss[Yasmine] Introduction and guidance on donating Cardinality Guardian processor. Donation Issue: [https://github.com/open-telemetry/opentelemetry-collector-contrib/issues/47368#issuecomment-4255976620](https://github.com/open-telemetry/opentelemetry-collector-contrib/issues/47368#issuecomment-4255976620)
- Discuss[Evan] configoptional scalar unmarshaling revival PR:
- Inform [Dakota] Need reviewer for new component telemetry metric PR: [https://github.com/open-telemetry/openhttps://github.com/TheFoxAtWork/toc/blob/980496083ba7538f1269b99773ae125e6f50d242/projects/open-telemetry/otel-graduation-dd.mdtelemetry-collector/pull/15068](https://github.com/open-telemetry/opentelemetry-collector/pull/15068)
- Discuss[Mikołaj] [Stabilizing confighttp](https://github.com/open-telemetry/opentelemetry-collector/issues/9380)
  - [Evan] Want clarification related to this on [https://github.com/open-telemetry/opentelemetry-collector/pull/14203#issuecomment-3589124097](https://github.com/open-telemetry/opentelemetry-collector/pull/14203#issuecomment-3589124097)
  - [Antoine] worth getting this in first? [https://github.com/open-telemetry/opentelemetry-collector/pull/15130](https://github.com/open-telemetry/opentelemetry-collector/pull/15130)
    - Also [https://github.com/open-telemetry/opentelemetry-collector/pull/14058](https://github.com/open-telemetry/opentelemetry-collector/pull/14058)
- Inform [Mikołaj] Supporting windows named pipes as a transport in confignet ([#15805](https://github.com/open-telemetry/opentelemetry-collector/issues/15085))
- Inform [Tiffany] Collector docs refactoring update - please get involved in writing/reviewing/suggesting, if you have an interest.
  - [Phase 2 plan](https://github.com/open-telemetry/opentelemetry.io/blob/main/projects/collector-docs-refactor/collector-docs-refactor.md#phase-2-create-sections-that-require-new-content)
  - [Phase 2 issues](https://github.com/open-telemetry/opentelemetry.io/issues?q=is%3Aissue%20state%3Aopen%20label%3Asig%3Acollector%3Arefactor%20milestone%3Aotelcol-phase-2)t
- Inform [Mikołaj] Partial config reload RFC [https://github.com/open-telemetry/opentelemetry-collector/pull/14640](https://github.com/open-telemetry/opentelemetry-collector/pull/14640)

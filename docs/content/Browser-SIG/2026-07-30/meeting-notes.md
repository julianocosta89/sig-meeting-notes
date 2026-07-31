## Meeting Notes

### Attendees
- Jared Freeze (Embrace)
- David Luna (Elastic)
- Rebecca He (Google/Firebase)
- Cleo Schneider (Google/Firebase)
- Martin Kuba (Grafana Labs)
- Trent Mick (Elastic)
- Carlos Cortez (Dash0)
- Maxime Quentin (Datadog)
- Hugo Levy (Datadog)

### Agenda
- [david] ContextRegistry max items? [https://github.com/open-telemetry/opentelemetry-browser/pull/281/changes#r3673021010](https://github.com/open-telemetry/opentelemetry-browser/pull/281/changes#r3673021010)
  - PR [https://github.com/open-telemetry/opentelemetry-browser/pull/368](https://github.com/open-telemetry/opentelemetry-browser/pull/368)
- [maxime] feat(sdk): validate all export URLs before starting the SDK
  - Config type change to be discussed
  - [https://github.com/open-telemetry/opentelemetry-browser/pull/357#discussion_r3614420596](https://github.com/open-telemetry/opentelemetry-browser/pull/357#discussion_r3614420596)
    - Other SDK tend to drop fast if there is a malformed config
    - Action: if trace url is malformed, it should not prevent logs to be sent, same is log’s url is malformed it should not prevent trace to be sent
    - Check the impact of such a permissive misconfiguration and assert
- [martin] Roadmap doc - please review
  - [https://github.com/open-telemetry/opentelemetry-browser/pull/361](https://github.com/open-telemetry/opentelemetry-browser/pull/361)
- [Chris]
  - Follow up on [browser lifecycle slack thread;](https://cloud-native.slack.com/archives/C093P0AMP0T/p1784820115448189) what should the next steps be to get this proposed?
- [Carlos] Spec SIG presentation?
- [Rebecca] onboarding guide?

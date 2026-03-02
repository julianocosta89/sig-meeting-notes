## Meeting Notes

### Attendees
- Ted Young (Grafana)
- Jared Freeze (Embrace)
- Joaquin Diaz (Embrace)
- David Luna (Elastic)
- Wolfgang Therrien (Honeycomb)
- Martin Kuba (Grafana Labs)
- Abinet Debele(Cisco)
- Benoit Zugmeyer (Datadog)
- Kareem Cambridge (Capital One)
- Hector Hernandez (Microsoft)

### Agenda
- [david] Bundler support issue
  - [https://github.com/open-telemetry/opentelemetry-browser/issues/10](https://github.com/open-telemetry/opentelemetry-browser/issues/10)
  - Feel free to add comments 🙂
- [Joaquin] Widely available browser features vs Browser market share
  - Does it make sense to miss out features from Chrome when ~70% of users are on Chrome?
    - Yes, let’s not omit useful information just because is only available in a certain browser but let’s be careful when dealing with these APIs to not break the SDK in run time. I.e. a global API that is only available in a browser
- [Jared] Added tooling with Bun and Biome: [https://github.com/open-telemetry/opentelemetry-browser/pull/8](https://github.com/open-telemetry/opentelemetry-browser/pull/8)
  - No need for discussion during the meeting
  - Bundler support: [https://github.com/open-telemetry/opentelemetry-browser/issues/10](https://github.com/open-telemetry/opentelemetry-browser/issues/10)
- [Wolfgang] Admin- I cant be assigned issues? Who can help?
- [Ted] Combine entities prototype with session manager prototype?
  - session manager was just merged [https://github.com/open-telemetry/opentelemetry-js/pull/5173](https://github.com/open-telemetry/opentelemetry-js/pull/5173)
- [Abinet] - Review for [https://github.com/open-telemetry/opentelemetry-js-contrib/pull/3148](https://github.com/open-telemetry/opentelemetry-js-contrib/pull/3148) (Navigation event instrumentation)
- [Kareem] - Intro and guidance on current status and where help is needed

## Meeting Notes

### Attendees
- Pavol Loffay (Red Hat)
- Mikołaj Świątek (Elastic)
- Ozzy Walsh (Red Hat)
- Tyler Helmuth (Grafana Labs)
- Andy Keller (Bindplane)
- Jacob Aronoff (Tero)
- Marc Schäfer (T&A SYSTEME)

### Agenda
- [Mikołaj] Decide what to do about [https://github.com/open-telemetry/opentelemetry-operator/issues/5493](https://github.com/open-telemetry/opentelemetry-operator/issues/5493).
  - Please review [https://github.com/open-telemetry/opentelemetry-operator/pull/5559](https://github.com/open-telemetry/opentelemetry-operator/pull/5559)
  - Pavol will build, run and test locally and ensure success
  - Decision by 11.09.2026, if not fixed, then switch it back to alpha
- [Tyler]: whats next for [https://github.com/open-telemetry/opentelemetry-operator/pull/5526](https://github.com/open-telemetry/opentelemetry-operator/pull/5526)?
- Review [feature gate](https://github.com/open-telemetry/opentelemetry-operator/blob/main/pkg/featuregate/featuregate.go) stability
- [Andy] Cannot start OpAMP bridge: missing patch permission for apps/deployments: access denied (as of 0.157.0)
  - Do we have an issue for this? Not yet
  - Caused by [https://github.com/open-telemetry/opentelemetry-operator/pull/5306](https://github.com/open-telemetry/opentelemetry-operator/pull/5306) I believe
  - Makes sense
  - 👍
  - Is this only if the bridge has the AcceptsRestartCommand mode? No ☑️
  - Can you open an issue and i can fix today, should be very simple to get this patch out in the next release
- [all] [Issues to discuss at sig](https://github.com/open-telemetry/opentelemetry-operator/issues?q=is%3Aopen%20label%3Adiscuss-at-sig) (always last)

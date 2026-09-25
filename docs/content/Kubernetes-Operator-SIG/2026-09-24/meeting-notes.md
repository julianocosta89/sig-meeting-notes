## Meeting Notes

### Attendees
- Mikołaj Świątek (Elastic)
- Tyler Helmuth (Grafana Labs)
- Jerry Leung (Solarwinds)

### Agenda
- [Mikołaj] Should we revert the netpol feature gates back to alpha? This seems like a problem whose complexity we [underestimated](https://github.com/open-telemetry/opentelemetry-operator/issues/5654).
  - Disable this for 0.160.0
  - Needs more testing, maybe rethinking
- [Mikołaj] Related to the above, I think this should go in before the release: [https://github.com/open-telemetry/opentelemetry-operator/issues/5654](https://github.com/open-telemetry/opentelemetry-operator/issues/5654)
- [Mikołaj] Ruby autoinstrumentation
  - PR: [https://github.com/open-telemetry/opentelemetry-operator/pull/5562](https://github.com/open-telemetry/opentelemetry-operator/pull/5562)
  - This one feels ready, and the author is working on having the image be owned by the Ruby SIG. The main question for us is whether we want to merge it before Instrumentation v1beta1
- [Mikołaj] PHP autoinstrumentation
  - PR: [https://github.com/open-telemetry/opentelemetry-operator/pull/5220](https://github.com/open-telemetry/opentelemetry-operator/pull/5220)
  - This one already has the image published, but the mechanism is problematic; it needs to know the PHP version, so either the user needs to set it, or there’s a mechanism to clone the app container and run a command inside.
  - How do we feel about this? I’d like to go back to the PHP SIG and ask if there’s no better way of doing this. Michele said the injector doesn’t want to sniff on language runtimes, so that path is blocked for the time being.
  - [Jerry]
    - Create another PR to remove current autoinstrumentation-php
    - Remove the app clone logic in the PR, set php as opt-in
- Review [feature gate](https://github.com/open-telemetry/opentelemetry-operator/blob/main/pkg/featuregate/featuregate.go) stability
- [all] [Issues to discuss at sig](https://github.com/open-telemetry/opentelemetry-operator/issues?q=is%3Aopen%20label%3Adiscuss-at-sig) (always last)

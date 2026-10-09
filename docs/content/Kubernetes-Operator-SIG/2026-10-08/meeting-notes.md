## Meeting Notes

### Attendees
- Mikołaj Świątek (Elastic)
- Pavol Loffay (Red Hat)
- Jacob Aronoff (Tero)
- Jerry Leung (Solarwinds)
- Andy Keller (Bindplane)

### Agenda
- Reminder to review the Ruby and PHP instrumentation PRs
- [Mikołaj] FYI: I filed a few issues after an AI-assisted audit of our webhooks
  - [https://github.com/open-telemetry/opentelemetry-operator/issues/5733](https://github.com/open-telemetry/opentelemetry-operator/issues/5733) is probably the most serious
- [Jacob] Injector Beta status
  - We’re going to say best effort for s390x and ppc64le
    - You’ll need to flip a flag to disable this
  - We will need to maintain both codepaths for now
  - We will initially do this for dotnet with a featureflag that we hope to bring to stable quickly
    - This can be done without s390x and ppc64le because dotnet does not support this
  - Eventually all languages will be through the injector path
- Review [feature gate](https://github.com/open-telemetry/opentelemetry-operator/blob/main/pkg/featuregate/featuregate.go) stability
- [all] [Issues to discuss at sig](https://github.com/open-telemetry/opentelemetry-operator/issues?q=is%3Aopen%20label%3Adiscuss-at-sig) (always last)

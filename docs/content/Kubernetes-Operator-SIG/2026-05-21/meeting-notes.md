## Meeting Notes

### Attendees
- Mikołaj Świątek (Elastic)
- Antoine Toulme (Splunk)

### Agenda
- [Mikołaj Świątek](mailto:mikolaj.swiatek@elastic.co)Switching completely to renovate from dependabot
  - Renovate is nicer and more featureful
  - It’s much better at handling monorepos with multiple Go modules
  - We’re adding a new module in [#5077](https://github.com/open-telemetry/opentelemetry-operator/pull/5077)
  - Decision: Yes, let’s do it.
- [Mikołaj Świątek](mailto:mikolaj.swiatek@elastic.co) Please review [#5105](https://github.com/open-telemetry/opentelemetry-operator/pull/5105)
- [Mikołaj Świątek](mailto:mikolaj.swiatek@elastic.co)I’d like to enable reviewer assignments from the approvers group
  - Two approvers assigned
  - What do we do about maintainer review and merge?
    - Add the maintainers group as additional codeowners?
    - Use a ready-to-merge label like the collector repo does?
  - Decision: Done
- [Pavol Loffay](mailto:ploffay@redhat.com): Instrumentation v1beta1 CRD RFC [https://github.com/open-telemetry/opentelemetry-operator/pull/5079](https://github.com/open-telemetry/opentelemetry-operator/pull/5079)
  - See what other projects aside from cert-manager did here
  - Decision deadline: end of May
- [Antoine Toulme](mailto:antoine.toulme@gmail.com) flakey test related to no CRDs - didn't get a chance to review
- Review [feature gate](https://github.com/open-telemetry/opentelemetry-operator/blob/main/pkg/featuregate/featuregate.go) stability [https://github.com/open-telemetry/opentelemetry-operator/pull/5077](https://github.com/open-telemetry/opentelemetry-operator/pull/5077)
- [Puneet Singh](mailto:puneet.mir@gmail.com) Readiness condition on FG stability [#5037](https://github.com/open-telemetry/opentelemetry-operator/issues/5037)
- [all] [Issues to discuss at sig](https://github.com/open-telemetry/opentelemetry-operator/issues?q=is%3Aopen%20label%3Adiscuss-at-sig) (always last)

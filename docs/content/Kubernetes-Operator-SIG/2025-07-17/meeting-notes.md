## Meeting Notes

### Attendees
- Mikołaj Świątek (Elastic)
- Benedikt Bongartz (Red Hat)
- Yuri Oliveira (OllyGarden)

### Agenda
- [Mikołaj] Let’s resolve the HTTP semantic convention breaking change somehow. [https://github.com/open-telemetry/opentelemetry-operator/issues/2542](https://github.com/open-telemetry/opentelemetry-operator/issues/2542)
  - Not upgrading the Java/.NET versions but using latest versions for new CRDs is something we can do without much risk
- [Mikołaj] Run E2E test with the latest contrib image daily and report errors in an issue
  - We’ve had two release blocking bugs recently that weren’t caught upstream. Both of them would’ve been caught by the operator’s E2E tests.
  - [Mikołaj Świątek](mailto:mikolaj.swiatek@elastic.co)will create an issue to do this
  - We should also bump the collector version asap, using renovate
- Review [feature gate](https://github.com/open-telemetry/opentelemetry-operator/blob/main/pkg/featuregate/featuregate.go) stability
- [all] [Issues to discuss at sig](https://github.com/open-telemetry/opentelemetry-operator/labels/discuss-at-sig) (always last)

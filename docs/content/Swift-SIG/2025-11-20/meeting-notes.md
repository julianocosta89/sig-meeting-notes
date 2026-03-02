## Meeting Notes

### Attendees
- Ari Demarco
- Bryce Buchanan
- Alex Cohen
- Arriana Blais
- Bee Klimt
- Vinod Vydier

### Agenda
- Crashing issue discussion (Skipped)
- Billy aws otel release, yay!
  - [https://github.com/aws-observability/aws-otel-swift](https://github.com/aws-observability/aws-otel-swift)
- Ktor instrumentation
  - Bee investigated a related issue where URLSession instrumentation is not instrumenting when it used to.
- TODO: update tests to not run for workflow changes, etc. [Bryce]
- TODO: PRs should merge when files changed not different on main (no branch update needed) [Bryce]
- Swift 6 - create new package.swift for 6.0 in core to start. [Billy]
- Logs sampling?

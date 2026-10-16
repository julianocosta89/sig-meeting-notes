## Meeting Notes

### Attendees
- Maxime Quentin (Datadog)
- Jared Freeze (Palo Alto Networks)
- Joaquin Diaz (Palo Alto Networks)
- Martin Kuba (Grafana Labs)
- Hector Hernandez (Microsoft)
- David Luna (Elastic)
- Mike Kozicki (Corridora)

### Agenda
- [martin] OTel JS v3 releasing next Monday
- [maxime] Migrate [https://github.com/open-telemetry/opentelemetry-demo](https://github.com/open-telemetry/opentelemetry-demo) out of the NodeJs SDK to the [opentelemetry-browser](https://github.com/open-telemetry/opentelemetry-browser)
  - Sounds reasonable to me but I would like maintainers approval first
  - Needs to measure the impact on the Demo collectors as such a migration has breaking changes
  - I opened the discussion with the OpenTelemetry Demo SIG
- [Adi] (async, conflicting call): migration guide for #468 is up as draft PR #479, covers package and import mapping (incl. packages with no direct replacement), fetch and XHR first with the config changes and outcome differences, events (navigation, exceptions, user interactions), SDK setup. Document-load section is still pending. Plan is to run every snippet against the final packages once JS SDK 3.0 is out, then mark it ready for review. Comments on the structure are welcome on the draft before then.
  - Update Oct 15: #479 is out of draft and ready for review. It now includes the document-load event setup and load-duration calculation. Trace grouping and paint coverage still depend on the open document-load decision in #327, so those gaps stay open.
  - Both install commands and both TypeScript examples passed on released Browser SDK 0.5.0 and instrumentation 0.8.2. The Chromium harness passed 87 checks, including 81 browser assertions across 22 HTTP outcomes, and the SDK example exported 11 trace spans and 17 log records. These packages resolve JS 2.12.0 and experimental 0.223.0. Final 3.0 is still unpublished this morning (npm latest is 2.12.0), so the final-package run waits on that release and compatible Browser dependency ranges.
  - Could a Browser approver review #448, #450, #451, #453 and #479? #453 has two approvals and passing checks, and still needs code-owner approval.
  - #239: the contrib side is up in [https://github.com/open-telemetry/opentelemetry-js-contrib/pull/3832](https://github.com/open-telemetry/opentelemetry-js-contrib/pull/3832) and the web-exception README has the deprecation notice and the move to ./experimental/errors with before and after examples. Martin’s three review points (deprecated tag on the class, scope name change, config type rename) are in 2bd6093. The final publish and npm deprecate need someone with rights there, source removal follows after that. Can do the same for navigation (#238) once this one looks right.
  - migration guide [https://github.com/open-telemetry/opentelemetry-browser/pull/479](https://github.com/open-telemetry/opentelemetry-browser/pull/479)
    - Jared: Add table calling out all key changes explicitly
- [martin] Proposal on document-load migration
  - [https://github.com/open-telemetry/opentelemetry-browser/issues/327#issuecomment-6182847349](https://github.com/open-telemetry/opentelemetry-browser/issues/327#issuecomment-6182847349)
- [martin] Versioning doc and deprecation policy
  - [https://github.com/open-telemetry/opentelemetry-browser/pull/497](https://github.com/open-telemetry/opentelemetry-browser/pull/497)
- [hector] Support resource detectors in the browser SDK
  - [https://github.com/open-telemetry/opentelemetry-browser/issues/460](https://github.com/open-telemetry/opentelemetry-browser/issues/460)
- [hector] Move opentelemetry-browser-detector from contrib to this repo
  - [https://github.com/open-telemetry/opentelemetry-browser/pull/459](https://github.com/open-telemetry/opentelemetry-browser/pull/459)
- [Jared] Base instrumentation class
  - should we have enable?
    - initialize vs enable
    - GDPR, runaway instrumentation
  - Should the SDK have global enable() / disable()?
    - Action item: create an issue

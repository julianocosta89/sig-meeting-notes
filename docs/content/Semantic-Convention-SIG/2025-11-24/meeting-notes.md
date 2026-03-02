## Meeting Notes

### Attendees
- [Daniel Dyla](mailto:dyladan@gmail.com) (Dynatrace)
- Josh Suereth
- Armin Ruech (Dynatrace)
- Christophe Kamphaus
- Liudmila

### Agenda
- Liudmila, 3 min: Folder name must match area name: [https://github.com/open-telemetry/semantic-conventions/pull/3108](https://github.com/open-telemetry/semantic-conventions/pull/3108)
  - No objections on the call
- Liudmila, 3 min: allow chore PRs on inactive areas:  [https://github.com/open-telemetry/semantic-conventions/pull/3109](https://github.com/open-telemetry/semantic-conventions/pull/3109)
  - Sounds good, maintainers can fix title if not chore
  - Liudmila will verify whether updating the title will trigger the workflow again
- Liudmila, 5 min: mark container inactive?  [https://github.com/open-telemetry/semantic-conventions/pull/3105](https://github.com/open-telemetry/semantic-conventions/pull/3105)
  - Sentiment seems to be to merge it into k8s
    - Liudmila will check with them
- [suereth, 5-10min] Weaver schema v2 + federation
  - V2 Progress - [https://github.com/open-telemetry/weaver/issues/994](https://github.com/open-telemetry/weaver/issues/994)
  - Goals in federation
    - We want components of semconv to be re-usable across otel
    - We want to do a "readability" / "usability" bump
    - We need to iron out our CI/CD pipeline for re-use

## Meeting Notes

### Attendees
- Marc Pichler (Dynatrace)
- Trent Mick (Elastic)
- Jared Freeze (Palo Alto Networks)
- David Luna (Elastic)
- Jamie Danielson (Honeycomb)
- Jackson Weber (Microsoft)

### Agenda
- **Feel free to add your topics below ↙️ 🙂**
- [marc] new releases on NPM now:
  - SDK 1.12.0/0.223.0 (makes migration to sdk-trace possible for sdk-trace-web users - thank you Trent for backporting the changes)
  - Pre-releases including the most recent API changes:
    - API `1.10.0-development.1`
      - (thanks to Trent and Hector)
    - SDK `3.0.0-development.1`
    - Experimental `0.300.0-development.1`
- [trent] Browser reviewer on [https://github.com/open-telemetry/opentelemetry-js/pull/7153](https://github.com/open-telemetry/opentelemetry-js/pull/7153) please?
  - Old things we should probably remove
- [jared] #platform review needed [https://github.com/open-telemetry/opentelemetry-js/pull/7141](https://github.com/open-telemetry/opentelemetry-js/pull/7141)
  - Mostly same change just over and over again in each package
- [trent] gaxios considered harmful? [https://github.com/googleapis/google-cloud-node/issues/8868](https://github.com/googleapis/google-cloud-node/issues/8868)
  - Rip it out
- [trent] perhaps last thing for Logs GA: [https://github.com/open-telemetry/opentelemetry-js/pull/7163](https://github.com/open-telemetry/opentelemetry-js/pull/7163)
- Todo: request TC review for logs
  - Example issue from python: [https://github.com/open-telemetry/community/issues/1751](https://github.com/open-telemetry/community/issues/1751)
- [jamie] Anybody going to KubeCon NA 26 in SLC next month?
  - Nope.
  - FYI there is a Contribfest happening, if anything is worth flagging as contribfest label or good first issue
- [Untriaged bugs](https://github.com/open-telemetry/opentelemetry-js/issues?q=is%3Aissue+is%3Aopen+label%3Atriage+label%3Abug+-label%3Apriority%3Ap1++-label%3Apriority%3Ap2++-label%3Apriority%3Ap3++-label%3Apriority%3Ap4+)
- [Untriaged contrib bugs](https://github.com/open-telemetry/opentelemetry-js-contrib/issues?q=is%3Aissue+is%3Aopen+label%3Atriage%2Cbug+-label%3Apriority%3Ap1++-label%3Apriority%3Ap2++-label%3Apriority%3Ap3++-label%3Apriority%3Ap4)
- [SDK 3.0 Milestone Triage and Refinement](https://github.com/open-telemetry/opentelemetry-js/milestone/20)
- [Old Contrib PR Triage](https://github.com/open-telemetry/opentelemetry-js-contrib/pulls?q=is%3Apr+is%3Aopen+sort%3Acreated-asc)
- [Old Core PR Triage](https://github.com/open-telemetry/opentelemetry-js/pulls?q=is%3Apr+is%3Aopen+sort%3Acreated-asc)

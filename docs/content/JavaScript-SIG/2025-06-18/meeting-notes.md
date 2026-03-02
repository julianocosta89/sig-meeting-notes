## Meeting Notes

### Attendees
- Marc Pichler (Dynatrace)
- Hector Hernandez (Microsoft)
- David Luna (Elastic)
- Trent Mick (Elastic)
- Marylia Gutierrez (Grafana)
- Jackson Weber (Microsoft)
- Andrei Borza (Sentry)

### Agenda
- **Feel free to add your topics below ↙️ 🙂**
- [david] please review
  - [https://github.com/open-telemetry/opentelemetry-js-contrib/pull/2886](https://github.com/open-telemetry/opentelemetry-js-contrib/pull/2886)
  - TL;DR add docker compose file to test locally. Remove MySQL setup from workflows
  - Required to continue with [PR workflow improvements](https://github.com/open-telemetry/opentelemetry-js-contrib/pull/2866)
- [hector] looking for reviews
  - Added logic for Url redaction #[5743](https://github.com/open-telemetry/opentelemetry-js/pull/5743)
- [marylia] just curious, what is the current state of http migration/implementation. Is that being done both for traces and metrics?
  - Core repo coordinating issue: [https://github.com/open-telemetry/opentelemetry-js/issues/5646](https://github.com/open-telemetry/opentelemetry-js/issues/5646)
  - Contrib repo meta issue: [https://github.com/open-telemetry/opentelemetry-js/issues/5663](https://github.com/open-telemetry/opentelemetry-js/issues/5663)
- [marylia] FYI, in case people don't know, that CNCF Slack is changing (likely migration to discord soon) [https://www.cncf.io/blog/2025/06/16/cncf-slack-workspace-changes-coming-on-friday-june-20/](https://www.cncf.io/blog/2025/06/16/cncf-slack-workspace-changes-coming-on-friday-june-20/)
  - A note with suggestion to use `slackdump` to save private channels and DMs: [https://notes.cncf.io/s/327vyVAil#](https://notes.cncf.io/s/327vyVAil#)
- [andrei] api v2 timeline?
  - Nope 🙂
- [dan] Browser Phase 1 [https://github.com/open-telemetry/community/blob/main/projects/browser-phase-1.md](https://github.com/open-telemetry/community/blob/main/projects/browser-phase-1.md)
- [marylia] JS maintainer review of [https://github.com/open-telemetry/community/pull/2817/files#diff-2b1b69303b927a484e02c7fad9fc87d0d3ff0dc22ae1da0ecd0dc935d922a23cR53](https://github.com/open-telemetry/community/pull/2817/files#diff-2b1b69303b927a484e02c7fad9fc87d0d3ff0dc22ae1da0ecd0dc935d922a23cR53)
- [Untriaged bugs](https://github.com/open-telemetry/opentelemetry-js/issues?q=is%3Aissue+is%3Aopen+label%3Atriage+label%3Abug+-label%3Apriority%3Ap1++-label%3Apriority%3Ap2++-label%3Apriority%3Ap3++-label%3Apriority%3Ap4+)
- [Untriaged contrib bugs](https://github.com/open-telemetry/opentelemetry-js-contrib/issues?q=is%3Aissue+is%3Aopen+label%3Atriage%2Cbug+-label%3Apriority%3Ap1++-label%3Apriority%3Ap2++-label%3Apriority%3Ap3++-label%3Apriority%3Ap4)
- [Old Contrib PR Triage](https://github.com/open-telemetry/opentelemetry-js-contrib/pulls?q=is%3Apr+is%3Aopen+sort%3Acreated-asc)

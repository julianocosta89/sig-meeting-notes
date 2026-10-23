## Meeting Notes

### Attendees
- Martin Kuba (Grafana Labs)
- Cleo Schneider (Google/Firebase)
- Jackson Weber (Microsoft)
- David Luna (Elastic)
- Jared Freeze (Palo Alto Networks)
- Joaquin Diaz (Palo Alto Networks)
- Trent Mick (Elastic)

### Agenda
- [Adi] Browser semconv decision list, confirm #327 document-load scope first, agree owners and one decision per SIG, then INP attribution (#471/#486). Proposal: [https://github.com/open-telemetry/semantic-conventions-client-side/issues/34](https://github.com/open-telemetry/semantic-conventions-client-side/issues/34)
  - Decision: move forward with the proposal
  - Split the work into smaller PRs
    - span instrumentation
    - context for resource-timing events
    - link document-load span to server context (meta tag)
- [david] Discuss on config [becoming static](https://github.com/open-telemetry/opentelemetry-browser/pull/278#discussion_r4338918587) from now on in instrumentations
  - When the config changes will apply. Next session? Next log/trace? We need to define that.
  - [Node.js](http://Node.js) ConfigProviders may be a way forward.
- [martin] FYI, Pull request dashboard
  - [https://github.com/open-telemetry/opentelemetry-browser/issues/517](https://github.com/open-telemetry/opentelemetry-browser/issues/517)
- Release this week

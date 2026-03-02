## Meeting Notes

### Attendees
- Ted Young [Grafana Labs]
- Jared Freeze (Embrace)
- Joaquin Diaz (Embrace)
- David Luna (Elastic)
- Trent Mick (Elastic)
- Maryam Saeidi (Elastic)
- Martin Kuba (Grafana Labs)
- Wolfgang Therrien (Honeycomb)
- Benoit Zugmeyer (Datadog)
- Dan Gomez Blanco (New Relic)
- Karlie L (Microsoft)

### Agenda
- [Ted] If you haven't become a github org member yet, here's how to do it:
  - Ask two existing members to be your sponsors
  - Fill out a membership request: [https://github.com/open-telemetry/community/issues/new?template=membership.md](https://github.com/open-telemetry/community/issues/new?template=membership.md)
- [martin] Page view semantic conventions
  - [https://github.com/open-telemetry/semantic-conventions/pull/1910](https://github.com/open-telemetry/semantic-conventions/pull/1910)
  - Pending questions:
    - rename the event to browser.page.view?
    - Is an attribute for page title useful?
    - state_change attribute
      - What is it for? the effect it had on history stack or what API was used to change the URL?
      - Is it useful?
      - If related to history, I think we should use better name, something like history_entry_change
      - Would it make more sense to use navigation namespace than page_view? So, something like “browser.navigation.history_entry_change”
    - page_view.type attribute
      - rename to navigation.type?
- [david] Issue [https://github.com/open-telemetry/opentelemetry-js/issues/5724](https://github.com/open-telemetry/opentelemetry-js/issues/5724)
  - Review the Log API for browser-related issues
- [Joaquin] Help creating a semconv PR
- [Ted] Github repo for browser?
  - Opentelemetry-browser?
  - Who wants to be maintainer/approver?
    - Joaquin and Jared
    - Martin (open to maintainer)
    - Karlie (approver)
    - David (open to maintainer)
- [Ted] What additional semconv and instrumentation issues can we create?
- [Karlie] need to reopen PR [https://github.com/open-telemetry/semantic-conventions/pull/1943](https://github.com/open-telemetry/semantic-conventions/pull/1943)

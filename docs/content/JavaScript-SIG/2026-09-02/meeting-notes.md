## Meeting Notes

### Attendees
- Marc Pichler (Dynatrace)
- Pranav Sharma (Google)
- Matt Wear (Dash0)
- Abhinav Mathur (Splunk)
- Jackson Weber (Microsoft)
- Surya
- Hector Hernandez (Microsoft)
- David Luna (Elastic)
- Trent Mick (Elastic)

### Agenda
- **Feel free to add your topics below ↙️ 🙂**
- [Pranav] GenAI utils library split: [https://github.com/open-telemetry/opentelemetry-js-contrib/pull/3709](https://github.com/open-telemetry/opentelemetry-js-contrib/pull/3709)
  - Can we enable stacked PRs ?
  - Should I split it further? Also requesting reviews **🙂**
- [mwear] Declarative config for instrumentation:
  - [Trent] I saw your last comment and *started* looking at your changes. Haven’t finished that review yet.
- [Trent] Let’s briefly discuss each SDK 3.0 milestone issue: [https://github.com/open-telemetry/opentelemetry-js/milestone/20](https://github.com/open-telemetry/opentelemetry-js/milestone/20)
  - [david] removing HrTime from browser instrumentations can be closed IMHO (new instrumentations do not use it anymore) [https://github.com/open-telemetry/opentelemetry-js/pull/6555](https://github.com/open-telemetry/opentelemetry-js/pull/6555)
  - Also, whether Logs stabilization milestone ([https://github.com/open-telemetry/opentelemetry-js/milestone/19](https://github.com/open-telemetry/opentelemetry-js/milestone/19)) is considered part of this.
  - sdk-trace-web removal. It might be possible to move the utils used in fetch and XHR instrumentations in core repo to the web-common package. Then we are good to remove it
    - [David Luna Bistuer](mailto:david.luna@elastic.co) to validate this and propose in Browser SIG
- [Trent] Discuss plan for widening `Attributes`: [https://github.com/open-telemetry/opentelemetry-js/pull/6780](https://github.com/open-telemetry/opentelemetry-js/pull/6780)
  - Carlos will review this and ask others for general TC review of the Logs API and SDK packages (perhaps Jack Berg and/or Robert Pająk)
- [Trent]: Reviews on this PR that is the current blocker on env/config-based configuration would be welcome: [https://github.com/open-telemetry/opentelemetry-js/pull/6999](https://github.com/open-telemetry/opentelemetry-js/pull/6999)
- [Surya] Review on

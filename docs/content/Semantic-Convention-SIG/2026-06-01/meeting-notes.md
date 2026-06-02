## Meeting Notes

### Attendees
- Christophe Kamphaus
- Armin Ruech (Dynatrace)
- Trask Stalnaker
- Sylvain Juge (Elastic)
- Antonio  Jimenez (Cisco ThousandEyes)
- Liudmila Molkova

### Agenda
- [Antonio Jimenez] I would like to propose the following new [network attributes:](https://opentelemetry.io/docs/specs/semconv/registry/attributes/network/)
- IP Prefix [https://github.com/open-telemetry/semantic-conventions/issues/3731](https://github.com/open-telemetry/semantic-conventions/issues/3731)
- AS (Autonomous System) Number [https://github.com/open-telemetry/semantic-conventions/issues/3740](https://github.com/open-telemetry/semantic-conventions/issues/3740)
- Reverse DNS [https://github.com/open-telemetry/semantic-conventions/issues/3741](https://github.com/open-telemetry/semantic-conventions/issues/3741)
- Let's start with an issue with scenarios
  - Liudmila will link related proposals
    - [https://github.com/open-telemetry/semantic-conventions/pull/3656](https://github.com/open-telemetry/semantic-conventions/pull/3656)
  - Let's discuss the scope we want to tackle
  - Depending on the scope we can decide if we need a full project proposal or a lightweight codeowners group
  - We can share meeting time with network SIG
- [Liudmila] opt-in network.peer.address on http connection metrics
- [Liudmila] require attributes on a signal to be of the same stability or higher [https://github.com/open-telemetry/semantic-conventions/pull/3752](https://github.com/open-telemetry/semantic-conventions/pull/3752)
- [https://github.com/open-telemetry/semantic-conventions/pull/3448](https://github.com/open-telemetry/semantic-conventions/pull/3448) basic end-user app crash event Ready to merge?

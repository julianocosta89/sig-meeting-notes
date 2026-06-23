## Meeting Notes

### Attendees
- Michele Mancioppi (Dash0)
- Braydon Kains (Google)
- Arve Knudsen (Grafana)
- Matthieu Noirbusson
- Krajo (Grafana)
- Josh Suereth (Google)
- Dmitry Anoshin (Splunk)

### Agenda
- delay '30
- [braydonk] Discussing "host" entity
  - Want to mark system metrics stable - this relies on host entity
  - Relies on things not fully landed in Entities
  - Goals
    - `[host.id](http://host.id)` - cannot think of consistent way to uniquely identify a machine under any context
      - /etc/machine/id only works on linux
      - Plan to use "whatever context you're in, use the one that makes the most sense"
        - e.g. AWS ARN, VMWare machine id
      - Could use entity relationships - "is-a" `host` to `ec2.instance`.
      - We also have no idea what universal rule to set for filling `[host.id](http://host.id)` today at all.
  - People continue to suggest things on host entity, but they only make sense on virtualization providers.
  - *Consensus: We need to find a way for other detectors / instrumentation to contribute `[host.id](http://host.id)` where a generic host resource attribute detector cannot discover its own id.  We'll work in Entities SIG to take existing collector behavior and formalize it.*
- [krajo] Informational: native metadata proposal open to suggest better support for (among other things) OTel resource attributes and OTel entities in Prometheus: [proposal](https://docs.google.com/document/d/1yYnyD7oJDvJhzFaigdniq6y302Mvp9gDcJUeAj3pJ0s/edit?tab=t.0#heading=h.mvctwq9htott) . Includes major points from this SIG
  - ease of use in PromQL
  - left hand navigation
- [suereth] SDK PRs
  - [https://github.com/open-telemetry/opentelemetry-specification/pull/5057](https://github.com/open-telemetry/opentelemetry-specification/pull/5057)
  - [https://github.com/open-telemetry/opentelemetry-specification/pull/5147](https://github.com/open-telemetry/opentelemetry-specification/pull/5147)

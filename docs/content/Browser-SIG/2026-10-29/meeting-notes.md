## Meeting Notes

### Attendees
- Martin Kuba (Grafana Labs)
- Joaquin Diaz (Palo Alto Networks)
- Jared Freeze (Palo Alto Networks)
- David Luna (Elastic)
- Mike Kozicki (Corridora)
- Ted Young (Grafana Labs)
- Aditya Reddy (Northwestern Mutual)

### Agenda
- [martin] Client semantic conventions
  - first release [https://github.com/open-telemetry/semantic-conventions-client-side/releases/tag/v0.1.0-dev](https://github.com/open-telemetry/semantic-conventions-client-side/releases/tag/v0.1.0-dev)
  - contains browser conventions
- [david] sessions and propagation
  - TL;DR makes sense to propagate [session.id](http://session.id) to downstream services?
  - yes
  - A common pattern is to use baggage. Instrumentation on the downstream service could read it to add new attributes. Not sure if we used it officially.
  - W3C [https://w3c.github.io/baggage/](https://w3c.github.io/baggage/)
  - Add a baggage header should be enough
- LinkedIn added their own browser/client concepts to OTel
  - [https://www.linkedin.com/blog/engineering/infrastructure/from-membertap-to-backend-how-linkedin-traced-the-member-journey-with-opentelemetry/](https://www.linkedin.com/blog/engineering/infrastructure/from-membertap-to-backend-how-linkedin-traced-the-member-journey-with-opentelemetry/)
  - pageForestId is an example of modelling sessions.

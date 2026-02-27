## Meeting Notes

### Attendees
- [Janhvi Gohri](mailto:janhvi@google.com)(Google)
- Josh Suereth
- Braydon Kains (Google)
- Dmitry Anoshin (Splunk)
- [Ankit Bhadu](mailto:ankitbhadu@google.com)(Google)
- Dotan Horovits (AWS)
- Anthony Mirabella (AWS)
- Ayushi Asthana (Google)

### Agenda
- [Arnav] Deployment.environment:
  - [https://github.com/open-telemetry/semantic-conventions/pull/3339](https://github.com/open-telemetry/semantic-conventions/pull/3339)
  - Arnav to split the PR into 2 parts and send it out for review
- [Ayushi] data entity proposal
  - [Introduce "data" entity in OTEL](https://docs.google.com/document/d/13jCkwYxS6pHTFTAPXqMljp2lTkO3FXKzKf34BFB2YEA/edit?usp=sharing)
- [Ayushi] criticality next steps?
  - Demo PR is raised [https://github.com/open-telemetry/opentelemetry-demo/pull/2950](https://github.com/open-telemetry/opentelemetry-demo/pull/2950)
  - Will follow up on next steps.
    - Propose this in the demo SIG and advertise this there.
    - [https://github.com/open-telemetry/opentelemetry-demo](https://github.com/open-telemetry/opentelemetry-demo)
    - [https://github.com/open-telemetry/community?tab=readme-ov-file#sig-community-demo](https://github.com/open-telemetry/community?tab=readme-ov-file#sig-community-demo)
- [Braydon] service name and instance ID on process metrics
  - [https://github.com/open-telemetry/opentelemetry-collector-contrib/issues/46207](https://github.com/open-telemetry/opentelemetry-collector-contrib/issues/46207)
- [Ankit] Service.business_unit.id:
  - [https://github.com/open-telemetry/semantic-conventions/issues/3475](https://github.com/open-telemetry/semantic-conventions/issues/3475)
- [trask] [Rename `service.peer.name`/`.namespace` to `server.service.name`/`.namespace` and](https://github.com/open-telemetry/semantic-conventions/issues/3472) [`client.service.name`/`.namespace`](http://client.service.name/.namespace)[?](https://github.com/open-telemetry/semantic-conventions/issues/3472)

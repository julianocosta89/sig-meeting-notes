## Meeting Notes

### Attendees
- Janhvi (Google)
- Josh Suereth (Google)

### Agenda
- Active PRs
  - [https://github.com/open-telemetry/semantic-conventions/pull/2963](https://github.com/open-telemetry/semantic-conventions/pull/2963) - Service Namespace, Service + Instance entity
    - Major comment themes
      - Descriptions being precise
      - "Application" vs. "Namespace"
  - [https://github.com/open-telemetry/semantic-conventions/pull/3088](https://github.com/open-telemetry/semantic-conventions/pull/3088) - Service Criticality
    - What prototypes do we need to showcase this?
      - Update the OTEL-demo to show usage - [https://github.com/open-telemetry/opentelemetry-demo](https://github.com/open-telemetry/opentelemetry-demo)
        - Inject criticality via ENV variables in the docker/k8s config
        - We update collector components to have high/low criticality pipelines that automatically are created based on the existence of this attribute.
      - Can we find sources of truth to pull this information from?
        - We should look for prior art where people tag resources with criticality
        - AI - [Ayushi Asthana](mailto:ayushiasthana@google.com)
  - [https://github.com/open-telemetry/semantic-conventions/pull/3097](https://github.com/open-telemetry/semantic-conventions/pull/3097) - Service Peer
    - This is breaking - what communication do we need to do around this?
      - Java supports this via config
        - map of hostname -> peer.service
        - lightstep was using this heavily
      - Can we do something of  "don't use this change until we stabilize?"
      - Let's outline what needs to happen to stabilize this and make sure that work will be committed to before merging.
- Topics
  - Request to change Asia friendly time: [https://github.com/open-telemetry/community/issues/3155](https://github.com/open-telemetry/community/issues/3155)
- Issue Triage / Next steps
  - Let's look at deployment - What would it take to stabilize
- AIs:
  - Create a group of PR reviewers for our SIg: [Josh Suereth (Big Nerd)](mailto:joshuasuereth@google.com)

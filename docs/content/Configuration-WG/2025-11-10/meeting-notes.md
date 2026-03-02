## Meeting Notes

### Attendees
- Alex Boten (Honeycomb)
- [Gregor Zeitlinger](mailto:gregor.zeitlinger@grafana.com) (Grafana Labs)
- [Jack Berg](mailto:jack.berg@grafana.com) (Grafana Labs)
- Jamie Danielson (Honeycomb)

### Agenda
- [Triage project board](https://github.com/orgs/open-telemetry/projects/38)
- [Gregor] Service detector by default?
  - [https://github.com/open-telemetry/opentelemetry-java-instrumentation/pull/14639](https://github.com/open-telemetry/opentelemetry-java-instrumentation/pull/14639)
  - As an alternative, could add service detector to examples
    - It’s experimental (detectors), but it has limited downsides
      - Implementations should log a warning if they don’t support this detector (but not crash)
      - Ideally, promote detection to stable
  - Related discussion
    - Starter template (from docs) should be configuration repository
  - [jack’s position]
    - Add `detection/development` to all the starter templates, and include standard detectors (resource, os, host, container)
    - Add a minimalist starter template to `/examples`, and reference in the [opentelemety.io](http://opentelemety.io) docs via snippet. Would include standard detectors as well as propagators.
    - Also publish [`schema-docs.md`](http://schema-docs.md) to [opentelemetry.io](http://opentelemetry.io) as supplementary reference for users
  - [alex’s position]
    - Do less now, and wait for more user feedback on the defaults
    - Work on stabilizing the resource detectors in the spec (and implementations)
- [Gregor] Why are there no default propagators in yaml? No default exporters?
  - Has caused confusion - most recently for the blog post: [https://opentelemetry.io/blog/2025/declarative-config/#getting-started](https://opentelemetry.io/blog/2025/declarative-config/#getting-started)
  - I know it was discussed at length, but I can’t recall why this was discarded
  - The spec calls out default propagators for platforms that pre-configure propagators: [https://opentelemetry.io/docs/specs/otel/context/api-propagators/#global-propagators](https://opentelemetry.io/docs/specs/otel/context/api-propagators/#global-propagators)
  - [gregor] what if the block was left out, this could be the signal to configure a default of w3c/baggage
- [Gregor] Spec issues that are need some attention
  - [https://github.com/open-telemetry/opentelemetry-configuration/issues/257](https://github.com/open-telemetry/opentelemetry-configuration/issues/257)
    - [https://github.com/open-telemetry/opentelemetry-java/pull/7605](https://github.com/open-telemetry/opentelemetry-java/pull/7605)
- [jack] Snippets!
  - [https://github.com/open-telemetry/opentelemetry-configuration/issues/393](https://github.com/open-telemetry/opentelemetry-configuration/issues/393)
- [alex] could we put descriptions back into the schema? [https://github.com/open-telemetry/opentelemetry-configuration/pull/396](https://github.com/open-telemetry/opentelemetry-configuration/pull/396)
  - Consensus: yes. Open PR to split defaultBehavior and nullBehavior into separate fields for better accuracy. Open conversation for how description gets updated in jsonschema as long as it gets updated. To be continued…

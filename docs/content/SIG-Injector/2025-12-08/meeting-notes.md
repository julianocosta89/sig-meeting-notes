## Meeting Notes

### Attendees
- Antoine Toulme (Splunk)
- Nikola Grcevski (Grafana)
- Bastian Krol (Dash0)
- Jack Berg (Grafana)

### Agenda
- [Nikola] wanted to see if [this PR](https://github.com/open-telemetry/opentelemetry-injector/pull/151)  is something that we would like to consider
  - [jack] Food for thought: [https://github.com/open-telemetry/opentelemetry-configuration/blob/d8c751c5baec2fd8c7541e88db11c05c8c3750d4/schema/common.yaml#L2-L27](https://github.com/open-telemetry/opentelemetry-configuration/blob/d8c751c5baec2fd8c7541e88db11c05c8c3750d4/schema/common.yaml#L2-L27)
- [jack] Things I’m thinking about
  - Instrumentation management: how do we manage multiple versions of multiple agents for upgrades?
    - [https://github.com/open-telemetry/opentelemetry-injector/issues/83](https://github.com/open-telemetry/opentelemetry-injector/issues/83)
    - Mention of [https://mise.jdx.dev/lang/java.html](https://mise.jdx.dev/lang/java.html)
    - [https://github.com/open-telemetry/opentelemetry-operator/blob/main/autoinstrumentation/java/version.txt](https://github.com/open-telemetry/opentelemetry-operator/blob/main/autoinstrumentation/java/version.txt)
  - Fine grain configuration: how do we use different configurations for different languages, different processes?
  - Fine grain control over what gets instrumented: how do we turn off instrumentation for certain processes?
    - [https://github.com/open-telemetry/opentelemetry-injector/issues/83](https://github.com/open-telemetry/opentelemetry-injector/issues/83)
    - [https://github.com/open-telemetry/opentelemetry-injector/issues/84](https://github.com/open-telemetry/opentelemetry-injector/issues/84)
  - No reboot required: how to we allow configuration without requiring system reboot?
    - [https://github.com/open-telemetry/opentelemetry-injector/issues/82](https://github.com/open-telemetry/opentelemetry-injector/issues/82)
    - Philosophy:
      - intercept getenv
      - Allow list of env variable names we’ll inject (i.e. standard OTEL_*)
      - Ignore injector env var if the env var is already set in the process
  - [`service.name`](http://service.name) detection and control: how do we provide more useful [service.name](http://service.name) values?
    - [https://github.com/open-telemetry/opentelemetry-injector/issues/146](https://github.com/open-telemetry/opentelemetry-injector/issues/146)

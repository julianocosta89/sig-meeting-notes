## Meeting Notes

### Attendees
- [John Watson](mailto:jkwatson@gmail.com)(Sublime Security)
- Jonathan Halliday (IBM)
- Jack Berg (Grafana Labs)
- Pranav Sharma (Google)
- Jay DeLuca (Grafana Labs)
- Mohammed Abdessetar Elyagoubi (Sofrecom)
- Trask Stalnaker (Microsoft)
- Peter Findeisen (Cisco)
- Jason (Splunk)
- Yuanfan Peng(Cisco)
- Felix Wong (IBM)

### Agenda
- [Jonathan] SDK support for [Process Context OTEP](https://github.com/open-telemetry/opentelemetry-specification/blob/main/oteps/profiles/4719-process-ctx.md) - requiring 25+ (panama), required for [Thread Context OTEP](https://github.com/open-telemetry/opentelemetry-specification/blob/main/oteps/profiles/4947-thread-ctx.md)
  - Directly to core repo
  - Need Spec for SDK hooks
  - Existing ContextStorage hook
  - Java 25
    - Some prior art in core repo for multijar
- [jack] AttributeLimits in opentelemetry-api, with depth limit: [https://github.com/open-telemetry/opentelemetry-java/pull/8656](https://github.com/open-telemetry/opentelemetry-java/pull/8656)
  - See if we can structure the API implementation of Attributes / AttributesBuilder to facilitate SDK subclassing that would allow for limits enforcement without having to expose new AttributeLimits in opentelemetry-api
- Backporting CVEs to different versions
  - Adjusted policy dimensions to consider
    - Can we mark specific different minor versions as “LTS”
      - Which minor versions?
      - What is the litmus test going forward?
    - Can we have separate policies for API vs SDK?
    - What is the definition of LTS?
      - 1 year? 2 year? 3 year? Version 1.19.0 is already 3+ years old.
      - Microprofile’s LTS definition:
        - Its just a specification, up to vendor to dictate policy
        - 2 year policy??
      - How many years of LTS support would satisfy the requirements of this predicament. Unlimited is off the table.
  - Is there anything Microprofile can do going forward to prevent this type of problem?
  - Felix to discuss internally and open an issue

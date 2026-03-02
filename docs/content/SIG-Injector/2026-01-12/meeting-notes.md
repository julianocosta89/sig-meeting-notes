## Meeting Notes

### Attendees
- Bastian Krol (Dash0)
- Jack Berg (Grafana Labs)
- Nikola Grcevski (Grafana Labs)

### Agenda
- [Bastian] rolling out the OpenTelemetry injector to the Dash0 customer base
- [Bastian] Version number: should we go to 1.0.0 with the next release?
  - What constitutes a breaking change for the injector?
    - Adding support for a new python
  - Some changes to the default configurations
    - Excluding new processes
    - Including new processes
  - What about changing the version of instrumentation which is included?
    - Is updating from otel java agent 1.1.0 to 1.2.0?
    - Is updating from otel java agent 1.1.0 to 2.0.0?
  - Maybe go to 0.1.0 now and do 1.0.0 after Python
    - …and ruby
      - Antoine has run into issues getting simple ruby app setup for testing
  - Before 1.0, make an attempt at defining stability guarantees
- [jack] Injector integration into the OpenTelemetry operator?
  - Benefits
    - Removes duplicate effort in operator and injector
    - Big lever to increase injector adoption
    - Removes the requirement for pod annotations
      - This is both a breaking change and a usability improvement for the operator.
      - I think operator should evolve towards opt out instrumentation rather than opt in
      - For a gradual change, introduce a new global flag to “opt in to the new opt out behavior”
      - Operator maintainers are interested in self update clusters

## Meeting Notes

### Attendees
- Josh
- Nathan Smith
- Dmitry Anoshin
- [Daniel Dyla](mailto:dyladan@gmail.com)

### Agenda
- [josh] API prototype updates
  - Status: Delayed startup prototype - Java complete
    - interface EntityDetector {
    - EntityProvider.builder().setInitialDetectors(...).setInitializationTimeout(...).build();
    - class LatestResourceSupplier implements EntityListener, Supplier<Resource> {
  - Questions
    - Default timeout for resource startup?
      - ~1s in node.js
    - Catastrophic failure logging?
    - Overall Concerns
- [josh] ENV variable
  - Do we need (another?) OTEP describing the PUSH-identity we need with ENV variables
- … other topics…
- triage: [https://github.com/orgs/open-telemetry/projects/85](https://github.com/orgs/open-telemetry/projects/85)

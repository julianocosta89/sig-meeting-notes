## Key Topics
- **Instrumentation Issues**: Discussion on failing tab tests for SQLized instrumentation in CI, with a focus on Node version discrepancies.
- **Component Label Map Update**: Need for updating the component label map and adding a script for regeneration to ensure proper test coverage.
- **Self-Metrics Development**: Progress on self-metrics for the OTEL SDK, with emphasis on metrics related to exporters and potential simplification of the core package.
- **Exporter Maintenance**: Debate on the necessity of maintaining Jaeger and Zipkin exporters given their deprecation, and the potential to consolidate exporter logic.

## Action Items
- Review the draft PR for updating the component label map and regenerating scripts.
- Investigate the failing tab tests further to identify discrepancies in Node module builds.
- Consider splitting functionalities from the core package to reduce complexity and improve maintainability.

## Participants
Trent Mick, Hector Hernandez, Marc Pichler, Daniel Dyla, Carlos Alberto Cortez

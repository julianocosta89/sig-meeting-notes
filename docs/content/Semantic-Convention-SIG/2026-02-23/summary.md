## Key Topics
- Discussion on the deprecation of span events, particularly around exceptions and the introduction of log-based exceptions.
- Consideration of whether to duplicate attributes in exception events or rely on correlation.
- Exploration of span identity and categorization for better identification of spans.
- Review of AWS Lambda invocation and its instrumentation within OpenTelemetry conventions.
- Clarification on naming conventions for function as a service (FaaS) and AWS-specific implementations.

## Action Items
- Follow up on the decision regarding making certain attributes an enum.
- Further define and document the log-based exceptions and their configurations.
- Investigate the potential for a standardized span identity property.
- Review AWS SDK instrumentation for Lambda and its implications on OpenTelemetry conventions.

## Participants
Trask Stalnaker, Liudmila Molkova, Michele Mancioppi, Josh Suereth, Christophe Kamphaus

## Key Topics
- **Instrumentation Naming and Scope**: Discussion on improving the naming conventions for instrumentation and ensuring consistency across different libraries.
- **HTTP Telemetry and Semantic Conventions**: Review of the current status of HTTP telemetry and plans for adopting stable semantic conventions by default.
- **OTLP JSON Protocol Support**: Consideration of adding support for the OTLP JSON protocol without introducing a Protobuf dependency, focusing on code generation instead.
- **Performance Improvements for AWS Lambda**: Discussion on reducing cold start times by potentially replacing the `requests` library with `urllib3` in the OTLP HTTP span exporter.

## Action Items
- Create an issue to track the proposal for consistent instrumentation naming.
- Further investigate the implications of switching to stable semantic conventions for HTTP telemetry.
- Explore the feasibility of generating code for OTLP JSON without Protobuf dependency and draft a plan for implementation.
- Assess the impact of replacing `requests` with `urllib3` on performance and compatibility.

## Participants
Riccardo Magliocchetti, Yazdankhah Mani, Tammy Baylis, Liudmila Molkova, Lukas, Aaron Abbott, Emídio, Dylan Russell, Pablo Colli

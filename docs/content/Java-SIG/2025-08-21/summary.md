## Key Topics
- Discussion on the implementation of a customizable parent class loader for the Java agent.
- Crash log collection mechanisms and the use of the `-XX:OnError` parameter for executing scripts on JVM crashes.
- Strategies for filtering out unnecessary spans (e.g., ping and hello spans) in Redis instrumentation.
- Optimization of the SDK span attributes to reduce overhead and improve performance.
- Exploration of extending the OpenTelemetry SDK to allow deeper customization of trace providers.

## Action Items
- Steve Rao to send a PR regarding the crash data collector implementation.
- Ziming Liu to add tests for capturing ping and hello commands in Redis instrumentation.
- Trask Stalnaker to add discussions on tracer provider customization to the agenda for the next meeting.

## Participants
Trask Stalnaker, Steve Rao, Jared, Antoine Toulme, Ziming Liu, Huxing Zhang

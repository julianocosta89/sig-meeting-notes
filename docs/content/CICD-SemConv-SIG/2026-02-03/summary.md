## Key Topics
- Updates on SDK support for environment variable context propagation, including progress on Python and Go implementations.
- Discussion on CI/CD producing long-running traces and the proposed approach for reporting span lifecycle events.
- Consideration of how observability backends might handle new event types and their implications for existing systems.
- Exploration of the handling of attributes within spans and the future of span events in the context of the OpenTelemetry specification.

## Action Items
- Adriel Perkins to post the Dagger implementation details regarding in-progress spans.
- Carlos Alberto Cortez to finalize and submit a PR related to the span lifecycle event reporting.
- Alan Clucas to investigate the environment variable length limitations in the Go implementation and how to handle them appropriately.

## Participants
Adriel Perkins, Christophe Kamphaus, Neil Yashinsky, Carlos Alberto Cortez, Alan Clucas

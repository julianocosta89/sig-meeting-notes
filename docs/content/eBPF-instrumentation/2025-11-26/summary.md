## Key Topics
- Discussion on HTTP2 and gRPC context propagation challenges.
- Proposed solutions for extracting trace parent information from gRPC binary protocol.
- Considerations for handling dynamic table indices in gRPC communication.
- Potential side effects and validation strategies for trace parent extraction.
- Next steps for extending data structures to track stream IDs and connections.

## Action Items
- Nikola to explore the feasibility of extracting trace parent values based on their format.
- Team to consider implementing heuristics to validate extracted trace parent values.
- Further discussions on tracking stream IDs and connections in eBPF instrumentation.

## Participants
Mattia Meleleo, Rafael Roquetto, Giuseppe Ognibene, Nikola Grcevski, Tyler Yahn

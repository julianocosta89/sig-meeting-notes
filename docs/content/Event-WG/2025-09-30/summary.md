## Key Topics
- Proposal to transition from span events to standalone events for better granularity in HTTP request tracking.
- Discussion on backward compatibility and deprecation strategies for existing Java SDK APIs.
- Consideration of performance implications and use cases for standalone events versus spans.
- Examination of existing semantic conventions and their application in the proposed model.

## Action Items
- Evaluate the feasibility of implementing a configuration option for using either standalone events or span events in the Java SDK.
- Further investigate the potential performance impacts of adding numerous events and their implications on query time.
- Review existing implementations in .NET for insights on handling DNS, TCP, and TLS events.

## Participants
Trask Stalnaker, Austin Parker, Surbhi A, Liudmila Molkova

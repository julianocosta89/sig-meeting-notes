## Key Topics
- Discussion on the behavior of the enabled API calls in OpenTelemetry, particularly regarding logger configuration and visibility of changes.
- Concerns about the performance implications of making certain fields volatile in Java, balancing correctness and efficiency.
- Debate on the introduction of complex attributes in metrics and whether they should be universally supported or selectively implemented based on use cases.
- The importance of maintaining forward compatibility in API changes, especially in JavaScript, and the potential reputational risks of breaking existing implementations.
- Strategies for communicating changes to the SDK implementation community to mitigate backlash from breaking changes.

## Action Items
- Robert Pająk to revise the PR regarding the enabled API calls to clarify visibility guarantees.
- Daniel Dyla to explore options for implementing extended attributes in JavaScript without breaking existing SDKs, potentially using a new API method.
- Participants to consider outreach to third-party SDK maintainers regarding upcoming API changes to ensure they are prepared.

## Participants
Liudmila Molkova, Bogdan Drutu, Carlos Alberto Cortez, Trask Stalnaker, Robert Pająk, Ted Young, Josh Suereth, Daniel Dyla

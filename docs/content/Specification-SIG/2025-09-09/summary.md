## Key Topics
- Discussion on the behavior of the enabled API calls in OpenTelemetry, particularly regarding logger configuration and visibility of changes.
- Concerns about the performance implications of using volatile reads in Java and the need for a balance between correctness and performance.
- The potential introduction of extended attributes for metrics in JavaScript and the implications for backward and forward compatibility.
- The importance of ensuring that changes to the API do not disrupt existing third-party SDKs.

## Action Items
- Robert Pająk to revise the PR based on feedback regarding the visibility of changes in the enabled API calls.
- Daniel Dyla to explore options for introducing extended attributes in a way that maintains backward compatibility, potentially by creating a new API method.
- Participants to review the implications of proposed changes across different languages and SDKs.

## Participants
Liudmila Molkova, Bogdan Drutu, Carlos Alberto Cortez, Trask Stalnaker, Ted Young, Robert Pająk, Josh Suereth, Daniel Dyla

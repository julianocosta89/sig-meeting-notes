## Key Topics
- Discussion on the use of Glob vs. regex for policy matching in OpenTelemetry SDKs.
- Proposal to separate redaction policies using regex from other policies using Glob.
- Challenges with implementing regex support across different programming languages.
- Need for a clear policy structure that handles partial support for matchers.
- Consideration of how to manage sampling policies in relation to head and tail sampling.

## Action Items
- David Ashpole to investigate why certain languages do not support regex.
- Further discussions on policy syntax to allow coexistence of Glob and regex matchers.
- Isha Bhardwaj to share findings from her probe on SDK sampling compatibility.

## Participants
Jacob, David Ashpole, Isha Bhardwaj

## Key Topics
- Discussion on the implementation of complex attribute types versus multiple simple attributes in OpenTelemetry for Android.
- The need for capturing additional HTTP request metrics that occur outside of the span lifecycle, leading to the proposal of using standalone events.
- Clarification on the deprecation of span events and the introduction of a new API for capturing network timing metrics.
- Challenges related to the compatibility of the current OKHTTP version with the new network listener implementation.

## Action Items
- Surbhi Agarwal to create a draft PR for the proposed changes and share it for review.
- Participants to review the existing PR related to the network timing event listener and provide feedback.

## Participants
Cesar Munoz, Surbhi Agarwal, Jason, Hansen

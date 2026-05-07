## Key Topics
- Discussion on the policy regarding note-takers in meetings and privacy concerns.
- Updates on the OpenTelemetry SDK, including plans for a unified SDK by summer and discussions about code duplication in XHR and Fetch instrumentations.
- Debate on whether to move certain utilities into a shared package or keep them within their respective instrumentations.
- Proposal to separate XHR and Fetch traces from user interactions to improve backend correlation.
- Importance of maintaining loose coupling in OpenTelemetry's design philosophy while addressing context issues in web instrumentation.

## Action Items
- Explore the possibility of moving utility code into a shared package for XHR and Fetch instrumentations.
- Create a draft PR to visualize the proposed instrumentation changes in the browser repo.
- Consider creating a configuration flag to separate traces for XHR and Fetch from user interactions.
- Schedule a follow-up discussion on spans, logs, and events for the next meeting.

## Participants
Martin Kuba, Jared Freeze, Maxime Quentin, Ted Young, Daniel Dyla, David Luna Bistuer, Joaquín Díaz, Abinet Debele

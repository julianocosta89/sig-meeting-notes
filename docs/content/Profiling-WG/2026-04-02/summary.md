## Key Topics
- **KubeCon Feedback**: Positive reception of the Profiling Alpha Lounge and discussions on protocol negotiation for profiling.
- **Protocol Versioning**: Discussion on the implications of versioning for unstable protocols and how to handle backward compatibility.
- **Data Model and Specification PRs**: Updates on open pull requests related to profiling specifications and data formats, with a focus on ensuring they are reviewed and approved.
- **Body Size Limitations**: Concerns raised about the limits for profiling data sizes in gRPC and HTTP, with suggestions for increasing these limits to accommodate real-world usage.
- **SDK Engagement**: Strategies to encourage SDK maintainers to implement and experiment with the new profiling protocol, including creating a meta issue to track progress.

## Action Items
- **Felix Geisendörfer**: Open an issue regarding protocol negotiation for profiling.
- **Christos Kalkanis**: Review and provide feedback on the open specification PRs.
- **Nayef Ghattas**: Propose a higher default size limit for profiling data in gRPC and HTTP.
- **Frederic Branczyk**: Create a meta issue to track SDK engagement and progress on implementing profiling.
- **Florian Lehner & Felix Geisendörfer**: Collaborate on exploring the use of unit indices in key-value pairs for profiling.

## Participants
Felix Geisendörfer, Tigran Najaryan, Nayef Ghattas, Frederic Branczyk, Christos Kalkanis, Ivo Anjo, Jonathan Halliday, Florian Lehner.

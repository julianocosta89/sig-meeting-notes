## Key Topics
- **Spec SIG recap:** Discussion of span lifecycle events, which would represent spans as start and end logs. Participants questioned the problem it solves (long-running traces) and whether shared IDs would be a simpler alternative. Concerns were raised about backend stitching and adding a second way to create spans.
- **Exporter naming and gem structure:** Proposal to standardize names as exporter, protocol/transport, variant, and signal. Matt favored separate gems to avoid forcing protobuf/gRPC dependencies on users, and the group leaned toward HTTP protobuf and HTTP JSON as separate gems. A migration and deprecation policy for existing gem names is still needed. The OTLP types gem (PR 2236) depends on protobuf, so it should be reviewed before the JSON exporter lands.
- **Ruby GC metrics:** Bart is exploring periodic `GC.stat` reporting as a gem, but it is blocked by a bug in asynchronous instruments that has a fix PR. He also noted his memory investigation turned out to be a malloc configuration issue, not a GC signal.
- **Sidekick queue latency proposal:** Robb proposed reducing span event volume by recording queue latency as a span attribute, with timestamps optional. Participants agreed on the latency attribute. Whether to keep or drop the timestamp span events, and how that fits with the deprecation of span events, was left for a future discussion. Naming conventions for background jobs were also flagged as a gray area.
- **Contrib updates:** Hannah's schema URL PR is ready for an agent review, then team review. Kayla shared CI-related PRs needing review. Rack and Action Pack IP attribute releases will go out after the meeting.

## Action Items
- Kayla: Review the async instruments fix PR for GC metrics this week and set up the workflows.
- Kayla: Find or create an issue to track exporter naming discussion notes, and investigate whether the JSON exporter still depends on protobuf.
- Kayla: Review the CI PRs (Dockerfile pinning, appraisals, Ruby version consolidation).
- Kayla: Release Rack and Action Pack IP attributes after the meeting.
- Kayla: Add span event deprecation to next meeting's agenda.
- Matt: Verify whether the OTLP types gem's protobuf dependency would leak into JSON exporters before the PR merges.
- Robb: Update the Sidekick issue description with the trimmed proposal, survey other background job instrumentations and Sidekick's own dashboard metric names, and investigate adding queue latency to the Rack span.
- Hannah: Run an agent review on the schema URL PR, then ping the channel for review.

## Participants
Robb Kidd, Kayla Reopelle, Bart de Water, Hannah, Matt Wear

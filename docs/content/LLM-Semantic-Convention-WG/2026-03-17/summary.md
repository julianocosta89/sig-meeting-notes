## Key Topics
- Discussion on the separation of span definitions for Invoke Agent into client and internal spans for better attribute precision.
- Exploration of the relationship between internal spans and server spans, particularly in the context of different protocols (HTTP, gRPC).
- Introduction of a PR for extracting span attributes from OpenAI responses to improve type safety and readability in the codebase.
- Updates on pending PRs related to GenAI utilities and the need for collaboration on releases.

## Action Items
- Review and provide feedback on the PR regarding the separation of Invoke Agent spans.
- Investigate the implementation of skills and their loading in the context of OpenTelemetry.
- Follow up on the PR for extracting span attributes to ensure it aligns with existing models and practices.
- Coordinate efforts to release compatible versions of different AI instrumentations.

## Participants
Trask Stalnaker, Keith Decker, Erdenesaikhan Tserendavga, Aaron Abbott, Liudmila Molkova, Ankit Singh, Surya Teja, Neil Yashinsky, Matt Kumar, Keith Decker.

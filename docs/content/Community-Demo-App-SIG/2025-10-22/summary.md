## Key Topics
- Discussion on PR for adding MySQL and MongoDB to the demo app, with concerns about Docker implementation and potential use of Dapr for database switching.
- Introduction of a GenAI service by Derek Mitchell, showcasing OpenTelemetry support for AI-generated product reviews.
- Consideration of using HTTP protobuf instead of gRPC for service communication, aiming for better compatibility and ease of use.
- Plans for improving Helm chart installation process and integrating OpenTelemetry operator for configuration management.

## Action Items
- Juliano to reach out to Lukash regarding the PR and discuss potential integration with Dapr.
- Derek to clean up the GenAI PR and remove K8s demo YAML changes.
- Team to create an issue for transitioning services to HTTP protobuf and document the process.
- Explore the possibility of allowing users to switch between mock and real LLM services in future PRs.

## Participants
Juliano Costa, Pierre Tessier, Derek Mitchell, Cyril Le Clerc, Jonathan Munz

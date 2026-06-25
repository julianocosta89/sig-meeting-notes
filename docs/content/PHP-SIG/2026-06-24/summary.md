## Key Topics
- Proposal to split CI workflows for different components (Laravel, MySQL, Kafka) to improve flexibility and reduce interdependencies.
- Discussion on the implications of maintaining separate workflows and the potential for duplication when adding new versions.
- Recent release of the OpenTelemetry PHP SDK and its implications for dependency management, particularly concerning security vulnerabilities in the Guzzle HTTP package.
- Consideration of enabling metrics functionality in the SDK and its impact on performance and latency.

## Action Items
- Chris Lightfoot-Wild to trial the proposed CI workflow changes for Laravel, MySQL, and Kafka.
- Bob Strecansky to work on releasing the SDK and potentially include metrics in the distribution.
- Sergey Kleyman to explore the possibility of running Snyk on the upstream OpenTelemetry repository to catch vulnerabilities earlier.

## Participants
Sergey Kleyman, Pawel Filipczak, Bob Strecansky, Chris Lightfoot-Wild

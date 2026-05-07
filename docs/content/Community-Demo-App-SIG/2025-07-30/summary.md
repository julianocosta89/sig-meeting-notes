## Key Topics
- Discussion on Java memory settings for OpenSearch and related container issues.
- Strategies for minimizing Docker image size by removing unnecessary plugins.
- Concerns regarding Jaeger version compatibility and the need for updates in Helm charts.
- Proposal to implement basic authentication for UI endpoints using Envoy proxy.
- Plans to consolidate Docker Compose files into a single file with profiles for easier deployment.

## Action Items
- Shenoy to explore options for reducing OpenSearch memory usage and log retention.
- Pierre to investigate the Jaeger Helm chart and consider removing the sub-chart for better control.
- Juliano to implement a new environment variable for Kafka usage in the demo.
- Documentation improvements to include SSL setup and basic auth for security.

## Participants
Juliano Costa, Shenoy Pratik, Pierre Tessier

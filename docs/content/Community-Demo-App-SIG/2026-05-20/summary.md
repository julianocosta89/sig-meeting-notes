## Key Topics
- **Attribute Renaming**: Discussion on migrating attributes from `app.something` to `demo.something` due to `app` becoming a reserved key, impacting integrations with tools like Grafana.
- **Major Release Plans**: Planning for a major release (demo 3.0) to coincide with the attribute changes and potential inclusion of the agentic demo.
- **Integration with Prometheus**: Consideration of a PR adding a Prometheus Java library to the demo, facilitating migration from Prometheus to OpenTelemetry.
- **Local LLM Features**: Discussion on adding local LLM capabilities and preloaded questions to improve user experience in the demo.
- **Host Metadata Addition**: Proposal to add host CPU metadata to the upstream collector for better visibility in Grafana dashboards.

## Action Items
- Review and finalize the PRs related to attribute renaming and the layered Docker Compose file.
- Evaluate the inclusion of the Prometheus integration in the demo.
- Implement preloaded questions in the chat UI for better user interaction.
- Open an issue for adding host CPU metadata to the upstream collector.

## Participants
Juliano Costa, Donal O'Sullivan, Felix George, Shenoy Pratik Gurudatt, Pierre Tessier

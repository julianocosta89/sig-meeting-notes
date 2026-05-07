## Key Topics
- **RFC for Migration of Semantic Conventions**: Discussion on the RFC that clarifies handling conflicts during migration from one semantic convention to another.
- **Extension Interfaces**: Ongoing conversation about the need for new storage extension interfaces to support various storage types, including Pebble.
- **Partial Pipeline Reloads**: Proposal for enabling partial reloads of the OpenTelemetry collector to reduce downtime and lost events during configuration changes.
- **Scraper Receivers Interface**: Introduction of a new interface for scraper receivers to allow different invocation methods, aiming for better horizontal scaling.
- **Resource Attributes Management**: Discussion on how receivers should handle resource attributes and the need for consistency across different data sources.

## Action Items
- **Josh Macdonald**: File a core collector issue regarding the new storage extension interface and its implications.
- **Blake Rouse**: Work on an RFC for the partial reload feature in the collector.
- **Liudmila Molkova**: Reach out to Postgres receiver owners for feedback on proposed changes to resource attributes.
- **Dmitrii Anoshin**: Review the RFC for the scraper receivers interface and provide feedback.

## Participants
Liudmila Molkova, Andrew Wilkins, Josh Macdonald, Dmitrii Anoshin, Blake Rouse, Antoine Toulme

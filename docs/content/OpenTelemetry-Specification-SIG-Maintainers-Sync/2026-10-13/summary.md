## Key Topics
- **Collector V1 Update**: Discussion on the progress and challenges faced by the Collector SIG, including the release roadmap and component stability.
- **QBatch Processor**: Introduction of a new configuration for the batch processor that combines queuing and batching, addressing concurrency and error propagation issues.
- **Declarative Config for Resource Attributes**: Exploration of how to handle null values in the new declarative configuration for resource attributes, seeking input from the spec SIG.
- **SBOM Compliance**: Discussion on the importance of Software Bill of Materials (SBOM) for regulatory compliance and the need for a clear checklist for artifacts shipped by different SIGs.
- **SIG Heartbeats**: Proposal for regular updates from all SIGs to enhance communication and cross-pollination of ideas within the OpenTelemetry community.

## Action Items
- **RFC Proposal for Collector V1**: Finalize and implement the proposed changes to focus on end users and prepare for a core distro release by KubeCon Europe 2027.
- **Open Issue on Declarative Config**: Create an issue in the configuration repository to clarify how null values should be handled in the new declarative config.
- **SBOM Checklist Development**: Collaborate on a pull request to establish a clear checklist for SBOM requirements across all SIGs.
- **Schedule SIG Heartbeat Updates**: Create a Google Sheet to track and schedule updates from various SIGs, encouraging participation from maintainers.

## Participants
Reiley Yang, David Ashpole, Alex Boten, Joshua MacDonald, Pablo Baeyens, Tigran Najaryan, Jade Guiton, Ted Young, Jack Berg, Daniel Dyla, Jason Plumb, others.

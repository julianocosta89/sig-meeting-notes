## Key Topics
- **Documentation Updates**: The hotel docs for Obi are published, marking a significant milestone.
- **Release Planning**: Discussion on whether to include ongoing documentation items in the upcoming 0.1 release.
- **Helm Chart Stability**: Need for stable image tagging for releases and potential branching for patches.
- **Internal vs. External Packages**: Consideration of moving certain Go packages to internal to avoid versioning issues.
- **eBPF Instrumentation Integration**: Exploration of integrating eBPF instrumentation with the OpenTelemetry collector and handling Kubernetes attributes.

## Action Items
- Define stability and versioning policies for the project.
- Review and finalize the Helm chart for the upcoming release.
- Investigate and possibly restructure Go packages to internal.
- Enable internal metrics for troubleshooting network degradation issues.
- Continue discussions on context propagation in cgroups and document limitations.

## Participants
Tyler Yahn, Mattia Meleleo, Nikola Grcevski, Nimrod Avni, Florian Lehner, Rafael Roquetto

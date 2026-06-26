## Key Topics
- Discussion on stabilizing OpenTelemetry semantic conventions for system metrics, specifically host ID and associated attributes.
- Clarification on the relationship between host ID and cloud provider attributes, with a focus on AWS and GCE instances.
- Review of attributes for stabilization, including system.device, network interface name, and file system attributes.
- Examination of PRs related to CPU attributes, including discussions on opt-in vs. opt-out configurations and potential breaking changes.

## Action Items
- Pablo to file an issue for stabilizing system.device, network interface name, and file system attributes.
- Dmitrii to post a message in the channel regarding concerns about the breaking change related to CPU attributes.
- Braydon to verify the terminology used for mount points in the context of NTFS.
- Braydon to investigate the handling of CPU frequency attributes and their implications.

## Participants
Pablo Baeyens, Dmitrii Anoshin, Braydon Kains, Igor Peschinskii

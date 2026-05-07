## Key Topics
- Release readiness of OpenTelemetry Swift version 2.0, including discussions on race condition fixes and necessary PRs.
- Consideration of minimum iOS version support, with data on market share and user impact from dropping support for iOS 13 and 14.
- Issues with the Prometheus exporter, particularly regarding metric duplication and clearing behavior.
- Discussion on session IDs and how to incorporate them into resource objects without disrupting the system.

## Action Items
- Review and finalize the race condition PR before the version 2.0 release.
- Investigate the minimum supported iOS version for Xcode and its implications for the project.
- Charlie to share relevant Prometheus exporter specifications to clarify expected behavior.
- Billy to draft a proposal for handling session IDs in the resource object for review.

## Participants
Bryce Buchanan, Arri Blais, Charlie Le, Vinod Vydier, Nacho, Martin Holman, Billy

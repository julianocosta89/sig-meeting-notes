## Key Topics
- Discussion on updating OpenTelemetry libraries in Grafana from version 1.9 to 1.12, addressing compatibility issues with .NET 9 and .NET Framework.
- Challenges faced by .NET Framework users regarding binding redirects and the implications of adopting the latest versions of packages.
- Consideration of future strategies for managing package versions in relation to .NET Framework and upcoming .NET versions (10, 11, and 12).
- Proposal for implementing GitHub attestations for software provenance in builds.
- Review of issues related to Prometheus metrics and resource attributes.

## Action Items
- Martin to summarize data points and create a document regarding the friction experienced by .NET Framework users for discussion with Microsoft.
- Martin to explore the feasibility of adjusting the PR to allow diagnostic source to remain at the latest version while pinning other extension packages.
- Mike to follow up with the .NET team regarding the current policy on package versioning and its impact on users.
- Alan to leave comments on PRs regarding adherence to the specification and the need for further review.

## Participants
Alan West, Martin Costello, Mike "Blanch" Blanchard, Matthew Hensley, Peter

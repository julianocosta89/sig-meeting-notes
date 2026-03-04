## Key Topics
- Discussion on changes to service telemetry, including splitting the service telemetry package for better interface management.
- The need for dynamic dimensions in telemetry metrics and challenges faced in implementation.
- Concerns about documentation and visibility of components in distributions, with suggestions for CI checks.
- Proposal to move certain structs (Watcher and Instance ID) to more appropriate packages for better organization.

## Action Items
- Andrew Wilkins to continue work on service telemetry and open an issue to propose moving the interface out to a new package.
- Antoine Toulme to find or create an issue regarding the documentation of components in distributions.
- Dmitrii Anoshin to explore automation for synchronizing metadata YAML with the releases repository.

## Participants
Andrew Wilkins, Antoine Toulme, Dmitrii Anoshin

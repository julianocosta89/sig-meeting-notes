## Key Topics
- **Data Compression Issues**: Discussion on conflicts arising from a data compression library conflicting with OpenTelemetry SDK due to naming issues.
- **CocoaPods Failures**: Ongoing issues with CocoaPods and synchronization problems in CI jobs were addressed.
- **Metrics PR Review**: Review of a pull request aimed at extending span data and removing old metrics references, with concerns about attribute accessibility and thread safety.
- **Persistent Metrics Exporter**: Introduction of a persistent metric exporter for stable metrics and the challenges faced in implementation.

## Action Items
- Address the data compression naming conflict in a branch for user resolution.
- Document CocoaPods issues and propose fixes to avoid waiting for the next release.
- Create a pull request to improve span attribute accessibility and ensure thread safety.
- Review and finalize the metrics pull request, focusing on persistent metrics and encoding/decoding tests.

## Participants
Bryce Buchanan, Ariel Demarco, Martin Holman

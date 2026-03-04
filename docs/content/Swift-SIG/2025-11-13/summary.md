## Key Topics
- Discussion on Dependabot issues with core dependencies and the addition to the ignore list.
- Updates on nightly builds and the challenges faced with modifying packages for environment considerations.
- Introduction of a new participant, Eric, who raised concerns about crashes related to data races in the iOS SDK.
- Recommendations for Eric to check the SDK version and utilize Thread Sanitizer for debugging race conditions.
- Confirmation of recent instrumentation merges for Metric Kit.

## Action Items
- Eric to check if the SDK is updated to the latest version to resolve potential data race issues.
- Eric to run the app with Thread Sanitizer in Xcode to identify any race conditions.
- Follow-up on any remaining issues in the CNFC Slack channel and consider opening an issue on the repo if problems persist.

## Participants
Bryce Buchanan, Nacho, ES Erick Sanchez, Billy Zhou, Bee Klimt

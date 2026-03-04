## Key Topics
- **CocoaPods Compilation Issues**: Discussion on fixing compilation errors related to CocoaPods and updating version dependencies.
- **Crash Reporting**: Implementation of KS Crash Reporter and its integration challenges within the main repository.
- **Metric Kit Support**: Addressing issues with Metric Kit support on macOS and potential solutions for CI compatibility.
- **Stack Trace Formats**: Debate on the appropriate format for stack traces in exception reporting, including the use of native formats versus Metric Kit formats.

## Action Items
- **Ariel Demarco**: Work on removing macOS support for Metric Kit until the CI can be fully migrated to Xcode 26.
- **Billy Zhou**: Finalize and submit PRs related to crash reporting and stack trace formats.
- **Team**: Review and address comments on the Metric Kit PR to ensure compatibility and functionality.

## Participants
Bee Klimt, Billy Zhou, Ariel Demarco, Vinod Vydier, Alex Cohen

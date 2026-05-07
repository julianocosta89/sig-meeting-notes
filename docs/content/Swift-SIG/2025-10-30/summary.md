## Key Topics
- **CocoaPods Compilation Issue**: Resolved a compilation error related to versioning and dependencies.
- **Crash Reporting**: Discussion on the implementation of KS Crash Reporter and its integration.
- **Metric Kit Support**: Addressed issues with compiling Metric Kit and the decision to temporarily remove macOS support.
- **Stack Trace Formats**: Debated the structure of stack traces for exceptions and metrics, including potential standardization.
- **Use of Spans vs Metrics**: Discussed the rationale for capturing data as spans instead of metrics due to aggregation complexities.

## Action Items
- **Ariel Demarco**: Edit the codebase to remove macOS support until migration to Xcode 26 is complete.
- **Billy Zhou**: Address comments on the PR regarding stack trace formats and crash messaging.
- **Vinod Vydier**: Confirm the status of the README update PR.

## Participants
Ariel Demarco, Billy Zhou, Bee Klimt, Vinod Vydier, Alex Cohen

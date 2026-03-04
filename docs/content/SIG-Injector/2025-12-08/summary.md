## Key Topics
- Discussion on the importance of including and excluding specific programs in the OpenTelemetry injector based on executable paths and command line arguments.
- Review of two open PRs: one for adding inclusion/exclusion features and another for upgrading the Zig version.
- Challenges related to merging changes with multiple contributors and maintaining code integrity.
- The need for a default exclusion list for certain applications (e.g., IntelliJ, PowerShell) to prevent unintended instrumentation.
- The potential impact of instrumentation on system performance and application stability.

## Action Items
- Nikola Grcevski to work on the inclusion/exclusion feature and consider a default exclusion list for future PRs.
- Bastian Krol to find time to merge changes and address the challenges posed by multiple PRs.
- Participants to review the implementation details regarding the semantics of including and excluding applications.

## Participants
Antoine, Nikola Grcevski, Bastian Krol, Jack Berg

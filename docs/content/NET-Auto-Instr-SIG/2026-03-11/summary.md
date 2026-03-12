## Key Topics
- Discussion on the new ASDK pull request and the need to upgrade Alpine packages.
- Issues related to assembly version conflicts and reflection calls in .NET 9 impacting OpenTelemetry initialization.
- Ongoing discussions about file-based configuration behavior when the configuration file is missing.
- Internal testing results for assembly loading and the implications for .NET Framework installations.
- Clarification on the behavior of file-based configuration overriding environment variables.

## Action Items
- Review and merge the pull request related to assembly version conflicts.
- Implement a fix for handling reflection calls in the native profiler redirection.
- Document steps to reproduce issues related to assembly loading in .NET Framework.
- Discuss the behavior of file-based configuration and its interaction with environment variables in future meetings.

## Participants
Piotr Kiełkowicz, Alexey Pukhov, Zach Montoya, Yevhenii Solomchenko, Igor Kiselev

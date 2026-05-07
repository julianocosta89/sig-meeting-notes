## Key Topics
- Discussion on the need for updates to the native profiler redirection due to reflection calls in .NET 9.
- File-based configuration behavior when the configuration file is missing; consensus on logging errors and continuing operation without crashing.
- Ongoing issues with assembly loading in .NET Framework and potential fixes.
- Review of PRs related to multiple application polls and assembly version conflicts.
- Consideration of how file-based configuration interacts with environment variables.

## Action Items
- Alexey Pukhov to include the fix for reflection handling in the current PR.
- Igor Kiselev to document steps to reproduce the assembly loading issue and reference specific tests.
- Participants to review PRs related to multiple application polls and assembly version conflicts.

## Participants
Piotr Kiełkowicz, Alexey Pukhov, Zach Montoya, Yevhenii Solomchenko, Igor Kiselev, Chris, Caesar, Jim, Steve Guineau.

## Key Topics
- Discussion on the stability proposal and version management strategy for OpenTelemetry .NET.
- Challenges with dependencies in NuGet packages and their impact on auto-instrumentation.
- Issues related to the new reflection API introduced in .NET 10 and its implications for future versions.
- Ongoing work on out-of-process instrumentation and its potential benefits.
- Updates on pull requests and the need for further improvements in the auto-instrumentation framework.

## Action Items
- Create a separate issue to document the current state of the startup hook and gather user feedback.
- Investigate the failure in the Mac OS pipeline related to startup hook-only solutions.
- Report the issues with the new reflection API to the .NET Runtime team and share updates in the Slack channel.
- Matthew Hensley to submit a PR addressing resource attribute handling and resolve flaky tests.

## Participants
Piotr Kiełkowicz, Matthew Hensley, Alexey Pukhov, Yevhenii Solomchenko, Igor Kiselev, Rajkumar Rangaraj, Chris Ventura

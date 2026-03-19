## Key Topics
- Discussion on the stability proposal and its relation to no-code instrumentation.
- Version management strategy and the implications of removing dependencies from the default NuGet package.
- Challenges with startup hook-only solutions and their impact on end users, particularly in relation to Azure Monitor.
- The introduction of unsafe accessor types in .NET 10 and its effects on dependency loading and profiler deployment.
- Ongoing work on out-of-process instrumentation and its potential to resolve existing issues.

## Action Items
- Create a separate issue to describe the current state of the startup hook and gather feedback from users.
- Rajkumar Rangaraj to provide a demo on out-of-process instrumentation in a future meeting.
- Continue discussions on the implications of unsafe accessor types and how to manage dependency loading effectively.

## Participants
Piotr Kiełkowicz, Matthew Hensley, Alexey Pukhov, Yevhenii Solomchenko, Igor Kiselev, Rajkumar Rangaraj

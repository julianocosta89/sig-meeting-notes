## Key Topics
- Discussion on the implementation of new semantic conventions for logging events in OpenTelemetry, specifically the transition from `device.crash` to `app.crash`.
- Consideration of how to handle legacy naming conventions and potential strategies for rolling out changes, including fallback modes.
- Challenges faced by client instrumentation due to varying app versions and the difficulty of upgrading users' apps.
- The need for a mapping layer to handle different versions of semantic conventions and ensure data consistency.
- Exploration of schema versions in telemetry and their potential role in addressing backward compatibility issues.

## Action Items
- Investigate the implementation of a fallback mechanism for legacy naming conventions in OpenTelemetry SDKs.
- Explore the possibility of using schema versions to enhance compatibility and data mapping on the collector side.
- Prepare for further discussions on async features and persistence in the next meeting.

## Participants
Hanson Ho, Cleo Schneider, Bryan Atkinson, João Oliveira, Ben Joseph

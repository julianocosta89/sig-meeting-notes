## Key Topics
- Discussion on backporting CVE fixes to earlier versions of OpenTelemetry Java, particularly for MicroProfile compatibility.
- Clarification of OpenTelemetry's policy on backporting security vulnerabilities and the challenges due to resource constraints.
- Updates on issues related to the transition to version 3.0 and the need for tracking dependencies in the contrib repository.
- Ongoing discussions about declarative configuration and its integration with OpenTelemetry SDK, including handling experimental properties.
- Review of a PR aimed at stabilizing types in declarative config by separating stable and experimental types.

## Action Items
- Felix Wong to open an issue on GitHub regarding the policy for backporting CVE fixes.
- Gregor Zeitlinger to create a label for tracking issues related to the transition to version 3.0.
- Jack Berg and Jason Plumb to collaborate on ensuring that the instrumentation module can handle property promotions from experimental to stable.

## Participants
Gregor Zeitlinger, Jason Plumb, Jack Berg, Felix Wong, Jonathan Halliday, Jay DeLuca, Jack Shirazi, David Grath

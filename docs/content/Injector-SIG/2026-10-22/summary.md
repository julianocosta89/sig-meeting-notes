## Key Topics
- Discussion on publishing container images for OpenTelemetry packages and the use of structured shims for operator compatibility.
- The role of init containers in consuming the images and considerations for image size and structure.
- The potential for using image volumes in newer Kubernetes versions and the implications for the injector's design.
- The need for a standardized versioning strategy for the operator and its implications for user experience.
- Ongoing efforts to integrate the injector into the operator and the challenges of maintaining backward compatibility.

## Action Items
- Jack to follow up on the use of BusyBox in the injector images and explore alternatives.
- Jacob to discuss the idea of annual major version bumps in the operator SIG and at KubeCon.
- Nikola to prepare a demo for KubeCon showcasing the injector's functionality.

## Participants
Jack Berg, Jacob, Antoine Toulme, Michele Mancioppi, Bastian Krol, Nikola Grcevski

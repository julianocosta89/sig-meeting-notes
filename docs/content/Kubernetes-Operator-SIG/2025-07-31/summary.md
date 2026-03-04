## Key Topics
- Ongoing issues with the Prometheus receiver and its impact on releases.
- Discussion on running daily end-to-end tests on the latest contrib image to catch issues early.
- Plans for releasing a new version of instrumentation CRDs with a manual upgrade process to manage breaking changes.
- Consideration of switching from Prometheus metrics to OTLP for improved reliability in tests.

## Action Items
- Jacob to write a PR for running daily end-to-end tests on the latest contrib image.
- Tyler to implement a replace statement in the manifest file to address dependency issues and prepare for a 1.31.1 release of artifacts.
- Follow up on the progress of the instrumentation CRDs upgrade process and communicate breaking changes to users.

## Participants
Jacob Aronoff, Benedikt Bongartz, Tyler Helmuth

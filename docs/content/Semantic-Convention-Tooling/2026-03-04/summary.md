## Key Topics
- Discussion on the generation of telemetry and its organization within the project crates.
- Consideration of whether to maintain separate registries for each crate or a single registry for the entire Weaver project.
- Challenges related to maintaining stable builds while using the current build system for code generation.
- The need for a solution to manage dependencies and ensure that builds are reproducible despite local changes.

## Action Items
- Explore the possibility of using a previous version of the crate for building to avoid dependency issues.
- Investigate how to allow users to provide schema URLs for better integration in monorepo setups.
- Review the current implementation of X task to ensure it operates independently of the main project build.

## Participants
ariannavespri, Jeremy Blythe, Laurent Querel, Josh Suereth, Liudmila Molkova

## Key Topics
- Discussion on PR for adding options to include/exclude programs based on executable paths.
- Upgrade considerations for the ZIG version and implications for existing contributions.
- Importance of having default configurations for excluding certain applications to prevent instrumentation issues.
- Exploration of version management for instrumentation and potential integration with existing tools like Mize.
- Need for improved handling of environment variables to avoid requiring reboots for changes to take effect.

## Action Items
- Nikola to work on the PR for include/exclude functionality and consider default exclusion lists.
- Team to document the OEM process for the injector and clarify how to manage instrumentation versions.
- Investigate the handling of environment variables to ensure they can be set without rebooting the system.
- Explore the possibility of templating OTEL resource attributes for better service name detection.

## Participants
Antoine Atoulme, Nikola Grcevski, Bastian Krol, Jack Berg

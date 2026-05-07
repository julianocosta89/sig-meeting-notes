## Key Topics
- Discussion on feature gates and their stability, including Golang flags and MTLS.
- Instrumentation V1 Beta 1 CR and the challenges of supporting declarative configuration across different languages.
- Transition from annotations to labels for pod instrumentation and the implications of this change.
- Semantic conventions and the potential for users to specify versions to avoid breaking changes.
- The need for better documentation and discoverability of instrumentation images and their versions.

## Action Items
- Open a pull request for V1 Beta 1 that includes cleanup and introduces declarative config as a raw field.
- Explore the implementation of a schema processor to assist with semantic convention upgrades.
- Improve documentation regarding instrumentation images and their release processes.

## Participants
Mikołaj Świątek, Israel Blancas, Benedikt Bongartz, PL Pavol Loffay, jea

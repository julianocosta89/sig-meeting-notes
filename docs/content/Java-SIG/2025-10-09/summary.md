## Key Topics
- Discussion on the new versions of OKHTTP and dependency management issues across different build systems (Gradle vs. Maven).
- Evaluation of the OpenTelemetry ZIO instrumentation, with concerns about its functionality and potential removal.
- Consideration of disabling problematic instrumentation by default, including Kotlin coroutines instrumentation.
- Suggestions for providing guidance on alternative libraries or solutions for users affected by disabled instrumentation.

## Action Items
- Jason to test the snapshot version of the OKHTTP dependency to confirm if it resolves the issues.
- Jay to open an issue regarding the ZIO instrumentation and discuss its potential removal.
- Consider creating guidance for users on alternatives if certain instrumentation is disabled by default.

## Participants
Gregor Zeitlinger, Trask Stalnaker, Jason Plumb, Jack, Lauri Tulmin, Jay DeLuca

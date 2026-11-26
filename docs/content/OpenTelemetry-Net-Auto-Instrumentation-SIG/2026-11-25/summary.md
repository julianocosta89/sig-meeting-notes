## Key Topics
- Startup hooks issue was deferred from the prior meeting; Igor Kiselev is reworking the fix because the current approach can load the wrong profiler DLL under certain edge conditions.
- The proposed approach has the profiler, on the managed-code model-loaded event, rewrite the initialization check to return true.
- Eftiquar Shaikh stressed that the profiler-attached check must remain, since without it the code cannot confirm the profiler is active and could crash.
- Eftiquar identified a pre-existing bug in OTel .NET: the startup hooks-only mode can install hooks without the profiler loaded. The hybrid mode is not affected because it doesn't rely on startup hooks.

## Action Items
- Igor Kiselev: finish the revised startup hooks fix (he already has a draft) and submit it for review.

## Participants
Piotr Kiełkowicz, Mateusz, Eftiquar Shaikh, Igor Kiselev, Rhynier Myburgh

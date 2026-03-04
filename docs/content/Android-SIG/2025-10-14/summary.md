## Key Topics
- Discussion on two PRs related to CPU attributes and semantic conventions for screen load.
- Clarification on the distinction between app start and initial draw events in instrumentation.
- Analysis of app start performance and its correlation with OpenTelemetry client initialization, specifically regarding OKHTTP.
- Consideration of platform-agnostic terms in semantic conventions to avoid Android/iOS-specific terminology.

## Action Items
- Participants to review and provide feedback on the two PRs discussed.
- Leonardo to create a separate SEMCONE PR to refine the definitions of nodes and depth.
- Hanson to investigate the complexities of Android activity and window lifecycles in relation to screen load spans.
- Leonardo to share Profetto traces for further analysis of app start performance.

## Participants
Hanson Ho, Jason Plumb, Mustafa Haddara, Cesar Munoz, Leonardo Serrano

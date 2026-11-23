## Key Topics
- **Stabilizing the trace state probability sampling spec:** Implementations from KubeCon suggest at least 3 (possibly 4), enough to move the spec out of experimental.
- **Telemetry policies:** David Ashpole introduced portable, mergeable, idempotent rules for telemetry. Consistent probability sampling fits well. The group renamed the SDK-only concept to "span sampler," reserving "trace sampler" for future whole-trace policies.
- **Recording unsampled spans and zero count:** Exporting spans without context propagation is possible but has no clear OTLP representation. Peter Findeisen noted the zero-count concept could mark such spans, and Joshua MacDonald pointed to an older issue from Chris. The group leaned toward propagating "not sampled" context, then deciding later whether to keep a span.
- **Preserving trace structure when spans are dropped:** Dropping intermediate spans breaks parent-child links. Peter proposed storing the last sampled ancestor's span ID in trace state, and Otmar Ertl suggested also recording the skip count.
- **Span importance and cost control:** David raised the lack of a way to express span importance in the trace API, such as a debug-span concept. The group discussed symbolic categories (basic/normal/detailed, as in the Go Collector) and using sampling rate as the knob. Robb Kidd (Honeycomb) noted that current tail samplers cannot prune interstitial spans.

## Action Items
- Joshua MacDonald: Review and comment on the zero-count/export issue, and submit a spec PR to move trace state probability sampling out of experimental (before the next meeting).
- Group: Continue the span-export and zero-count discussion in the GitHub issue or Slack.
- Group: Think about solutions for span importance and interstitial span handling, and revisit in two weeks.

## Participants
Joshua MacDonald, Peter Findeisen, David Ashpole, Otmar Ertl, Robb Kidd

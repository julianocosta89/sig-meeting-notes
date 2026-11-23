## Key Topics
- Evaluation result event: Steve asked how the OTel GenAI evaluation result event relates to evaluation systems that store results separately. Trask said traces let the event correlate with other telemetry, and that emitting it is optional. Use cases include customer-written evaluators and instrumented evaluation libraries sending to observability backends like OpenSearch.
- Trajectories: Trask explained that a Google contributor proposed a Version 2 trajectories format and that OTel and trajectories need alignment. No decisions have been made; the next step is an issue analyzing gaps.
- GenAI semantic conventions release: Steve asked for an RC or a new release so Alibaba can update its instrumentation. Trask said the earlier RC-before-KubeCon target was missed, the goal is now an RC by year end, and many breaking changes make an RC premature. Instrumentations should wait for stabilization or gate changes behind a flag.
- Meeting logistics: Trask was returning from KubeCon North America, and KubeCon videos are expected to be posted.

## Action Items
- Trask Stalnaker: Raise the GenAI semantic conventions release timing as a topic at tomorrow's SIG call.
- Trask Stalnaker: Raise the evaluation result event question with the wider group on tomorrow's call.
- Steve Rao: Review the evaluation-related issues in the OTel GenAI repository and the Google Doc notes.

## Participants
Trask Stalnaker, Steve Rao, Huxing Zhang

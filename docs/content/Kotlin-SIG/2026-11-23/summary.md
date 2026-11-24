## Key Topics
- **Release cadence:** The last release was about 3 weeks ago. Nothing is urgent, but the group agreed to release this week to keep a steady cadence.
- **API stabilization:** Jamie is reviewing context and propagator API changes against the spec. Carlos's feedback covers an `extract` naming clash with propagators, unclear nesting docs for context activation, and an open question on coroutines. Jamie proposed reviewing 2-3 API items per week, with removing the annotation as the step toward stability. Jason noted there's no strong reason not to consider 2.0.
- **Semantic conventions versioning:** Hanson found that the Kotlin SDK's semantic convention constants are tied to whichever version the SDK points to, so downstream users can't pick a specific version. Options raised include documenting that users should generate their own constants with Weaver, sharing Weaver templates, and having the Java repo generate Kotlin. No decision was made.
- **Android meeting cancellation:** Thursday's Android meeting will be skipped due to Thanksgiving next week.

## Action Items
- Jason: Post a Slack note cancelling Thursday's Android meeting and try to remove it from the calendar.
- Jamie: Cut a release this week.
- Jamie: Review Carlos's API feedback (extract naming, context nesting docs) and create 2-3 API review issues per week.
- Carlos: Double-check the coroutines section of the context API after the call.
- Hanson: Think through options for semantic convention versioning and the Kotlin constants problem.

## Participants
Jason Plumb, Hanson Ho, Jamie Lynch, Carlos Alberto Cortez

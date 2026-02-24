## Meeting Notes

### Attendees
- Jason Plumb (Splunk)
- Hanson Ho (Embrace)
- Cesar (Elastic)
- Jamie (Embrace)
- Surbhi A (Cisco)
- Manoel (PostHog)
- Cleverchuk (Solarwinds)

### Agenda
- Revisit Google Play SDK Console:
  - [https://github.com/open-telemetry/community/issues/3188](https://github.com/open-telemetry/community/issues/3188)
  - Does anybody have cycles to help out with this?
    - Hanson can help – Jason will put them in touch
- We talked about LLMs and copilot stuff.
  - Reviewers don’t wanna sift thru a ton of copilot reviews before reviewing.
  - We should write something down about this – submitters who request a copilot review should resolve all AI comments before getting repo human reviews.
  - Copilot *can* review draft PRs.
  - Still need PR template
    - For reference: [https://github.com/renovatebot/renovate/blob/main/.github/pull_request_template.md#ai-assistance-disclosure](https://github.com/renovatebot/renovate/blob/main/.github/pull_request_template.md#ai-assistance-disclosure)
- (Surbhi) Inviting feedback and approvals on this proposal - [https://github.com/open-telemetry/semantic-conventions/issues/2827#issuecomment-3827130424](https://github.com/open-telemetry/semantic-conventions/issues/2827#issuecomment-3827130424)
  - Don’t get hung up on the monotonic clock too much – it’s an implementation detail
  - Computing deltas is more work for both instrumentation and consumer alike
  - Other modeling options?
    - Spans
    - What about a complex attribute on the span?
    - Are we mixing up two concerns? Instrumentation and timeout and how to model the network timing info.
  - Surbhi has researched and found that it’s possible for the span to be closed before the response body is completely read.

## Meeting Notes

### Attendees
- [Romain Marcadier](mailto:romain.marcadier@datadoghq.com) (Datadog); **Facilitator**
- Przemek Delewski (Quesma)
- [Kemal Akkoyun](mailto:kemal.akkoyun@datadoghq.com) (Datadog)
- Huxing Zhang (Alibaba)
- Ziming Liu (Alibaba)
- Yi Yang (Alibaba)

### Agenda
- [Huxing] Progress check
  - [https://github.com/open-telemetry/opentelemetry-go-compile-instrumentation/issues/29](https://github.com/open-telemetry/opentelemetry-go-compile-instrumentation/issues/29)
  - Most of the setup phase was handled by Yi Yang, thanks for that :)
  - For MVP we need to reach ability to instrument basic HTTP application
  - Tasks depend on each other, so parallelization is possible but requires tight coordination
    - Can leverage the existing contrib’s instrumenter API
    - Key: help Yi Yang implement the instrumentation part
    - Need to define interfaces before work can be parallelized; but bottom-up so interfaces likely to change as we go & require adjustments throughout the stack
    - Are all taks assigned or are any pending? All are pending at the moment.
    - Yi Yang - setup phase is essentially complete. Next phase is injecting those functions into the targets. Instrumentation phase is ready for implementation.
      - Romain - busy on other tasks for the next ~2 weeks, can’t really spend a lot of time on this until then unfortunately
      - Przemek & Kemal in similar situations (+ vacations)
      - Option: Yi Yang can give it a shot for the next 2 weeks, no pressure; and then we can swarm on it with more folks once current affairs + vacations are flushed.
- [Przemek] Potential conflicts between packages used by the instrumented app and those introduced by our tool
  - Problem was brought up in one of the meetings with Gophers
  - Wondering if we have some solutions for that; there seems to be opinion/ideas on this, we should discuss and derive an ADR from conclusions there?
  - We can progress on this offline, too – collaborate on a document + discuss next time over?
  - Orchestrion - have issues around this regularly, and is solved by checking in a `go.mod` file that includes all dependencies (app’s + instruments), so everything resolves canonically, in a predictable & user-controllable manner.
    - Romain will share some links to the kind of issues they’ve had so far (DD tracer’s v0.x dependency getting breaking changes; OTel dependencies causing upgrade issues, etc…)
  - Seems we have a consensus on what a solution may look like – formalize this into a doc + circulate it back with the Gophers to make sure they don’t see a way this is insufficient/inadequate.
- KubeCon talk submission by [Kemal Akkoyun](mailto:kemal.akkoyun@datadoghq.com) was unfortunately rejected (maybe too specialized for the audience?) – maybe we can try again for next KubeCon, re-working the wording a little bit + the tool will hopefully be released by then.
- Huxing is working on organizing KCP in CN (~November), will try to submit a talk there

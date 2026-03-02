## Meeting Notes

### Attendees
- Martin Kuba - will not attend, out of office
- Arriana Blais (honeycomb)
- Ram Thiru - Will have to skip this due to conflict.  *Comments on questions below.*
- Jared Freeze (Embrace)
- Joaquin Diaz (Embrace)
- [Daniel Dyla](mailto:dyladan@gmail.com)
- [Thomas Hunter II](mailto:thomas.hunter@datadoghq.com) (Datadog)
- Dan Gomez Blanco (New Relic)

### Agenda
- [martin] Request for feedback on the Page View event semconv PR
  - [https://github.com/open-telemetry/semantic-conventions/pull/1910](https://github.com/open-telemetry/semantic-conventions/pull/1910)
  - please add comments on the PR
  - questions
    - use human-readable values for type instead of 0 and 1? If so, which ones? *[Ram] See comments*
      - hard / soft
      - page_load / route_change
      - physical_page / virtual_page
    - I renamed the change_state field to state_change. I am also inclined to update the values to “push” and “replace”; pushState/replaceState was confusing to me as it mirrors the history function names rather than just what happens to the state. Any objections?
    - the page title field could have PII data. Per a comment on the PR, the field may not be that useful. Should we remove it for now?
- [Joaquin] [Test Harness Plan](https://docs.google.com/document/d/15AJAo_aU7BFDLPq47FP_eo-tyGI7uZ9jnHaRUSS1Q2M/edit?tab=t.0)
- [Ted] Let’s get the semconv backlog set up for success!
  - Consolidate namespace UA & Browser namespace
    - [https://github.com/open-telemetry/semantic-conventions/issues/2385](https://github.com/open-telemetry/semantic-conventions/issues/2385)
  - What info should we have in each semconv issue?
    - PageLoadSpan
    - FetchTiming
    - Exceptions
    - XHR

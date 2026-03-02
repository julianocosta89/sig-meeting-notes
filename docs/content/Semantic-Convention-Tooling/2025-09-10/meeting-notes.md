## Meeting Notes

### Attendees
- Josh Suereth
- [Nathan Smith](mailto:nathan.smith@elastic.co)
- Jeremy Blythe
- Liudmila

### Agenda
- Triage Project board: [https://github.com/orgs/open-telemetry/projects/84](https://github.com/orgs/open-telemetry/projects/84)
  - Start merging schema fixes into V2 project board for weaver,
  - start using weaver project board to track things instead of both
- Weaver Project board: [https://github.com/orgs/open-telemetry/projects/74](https://github.com/orgs/open-telemetry/projects/74)
  - Two bugs to look at for next release
- General Discussion
  - Update on attribute groups
    - Let’s do public and internal groups
      - internal groups removed from resulting schema
      - public groups remain
      - *If two groups are referenced that use the SAME attribute - we consider this a failure.*
    - Sampling-relevant
      - Two concerns:
        - Sampling relevant is ALWAYS filled out for Spans
          - Need syntax or policy
        - Sampling relevant isn't accidentally inherited.
      - Rename to something like ‘head-sampling’  / ‘provided - at span start time’
        - "start span operation" <- specification term.
      - Strawman:
        - attribute_groups:
  - Live-check - level and report
    - [https://github.com/open-telemetry/weaver/pull/923](https://github.com/open-telemetry/weaver/pull/923)
      - sets a minimum level of advise for what the report will include.
    - How to report issues?
      - e.g. linter and showing line-of-code where things fail
      - Don't want to overload with errors from tons of spans
    - Current Design - you have it in CI/CD so you have limited set of spans/attributes being reported

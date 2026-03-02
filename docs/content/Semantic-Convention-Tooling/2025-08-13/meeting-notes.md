## Meeting Notes

### Attendees
- Josh Suereth
- Jeremy Blythe

### Agenda
- Triage:
  - [https://github.com/orgs/open-telemetry/projects/74](https://github.com/orgs/open-telemetry/projects/74)
- Topics
  - [suereth] Schema validation
    - Enhancement: Warning if `version: X` is not specified
    - Enhancement: Create a tool that takes V1 and turns it into V2.
  - V2 Schema
    - Plan - V2 resolved schema may look like "simple" V2 definition schema
    - We have no "sharing" right now, e.g. `extends`, so V2 resolved schema from V2 definition is basically just grouping stuff from files.

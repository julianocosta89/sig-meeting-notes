## Meeting Notes

### Attendees
- Liudmila Molkova (Grafana Labs), first 30 mins
- Dave Cadwallader (Oracle), first 30 mins
- Josh Suereth
- Alexandra Konrad (Elastic)

### Agenda
- (timebox 7 min) Project Status + Triage + Blockers
  - Stability Blockers
  - PR Triage Board: [https://github.com/orgs/open-telemetry/projects/67/views/1](https://github.com/orgs/open-telemetry/projects/67/views/1)
  - Issue Triage Board: [https://github.com/orgs/open-telemetry/projects/131/views/1](https://github.com/orgs/open-telemetry/projects/131/views/1)
- (timebox 50 min) General topics
  - Dave Cadwallader from Oracle would like to propose an Oracle Cloud Infrastructure approvers group for the semconv repo.  See: [https://github.com/open-telemetry/semantic-conventions/issues/3177](https://github.com/open-telemetry/semantic-conventions/issues/3177)
    - Naming conventions?
      - Other vendor prefixes - use _ to separate words.  Directory uses snake-case.
        - Keep `_` in yaml files.
    - Need org membership
  - Attribute registry v2, what's changing:
    - No groups: brief/notes are gone
      - Mostly not interesting
      - Some groups have good descriptions: server, artifact, etc - future public groups?
    - Display name: weaver config can do the trick
    - All attrs within the root namespace are rendered together: e.g. aws
      - Can in the future break down by sub-namespaces
    - How does extends work now?
    - attributes:
    - How to use for YAML definitions
    - version: "2"
  - Evolution
    - weaver … –v2 <- Output is in V2 format, Policies are in V2 format, Templates are V2 format
    - File header - `version: "2" - definition is in V2 format.

## Meeting Notes

### Attendees
- Adriel Perkins (Grainger)

### Agenda
- (timebox 7 min) Project Status + Triage + Blockers
  - Project Board: [https://github.com/orgs/open-telemetry/projects/171](https://github.com/orgs/open-telemetry/projects/171)
- General
  - [christophe - 10 min] - stabilization updates
    - Adriel will move github receiver metrics to beta and traces to alpha
    - Adriel will add work on the board to track stabilization of metrics (vcs) and span (cicd)
      - 1 item for cicd span + attributes
      - 1 item for cicd metric + attributes
      - 1 item for vcs metric + attributes
      - Validate that all attributes from registry in CICD & VCS are covered by the respective signal
      - 1 item for logs (entities) + attributes
    - Do we want to have stage, queue, exec, and finalied span types to group tasks together
      - The gitHub receiver includes queue and features are being asked for exec
      - Stage / exec could be the same thing
      - We really need the different run states correlated with run duration
      - Adriel action item : take a look and compile an issue for this with references to the issues requested

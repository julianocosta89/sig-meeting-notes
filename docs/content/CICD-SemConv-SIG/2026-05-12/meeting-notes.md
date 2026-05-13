## Meeting Notes

### Attendees
- Adriel Perkins (Grainger)
- Christophe Kamphaus
- Alan Clucas (Pipekit)
- Dotan Horovits (AWS, OpenSearch)

### Agenda
- (timebox 7 min) Project Status + Triage + Blockers
  - Project Board: [https://github.com/orgs/open-telemetry/projects/171](https://github.com/orgs/open-telemetry/projects/171)
- General
  - [adriel] - still have the following remaining todos
    - Do we want to have stage, queue, exec, and finalized span types to group tasks together
      - The gitHub receiver includes queue and features are being asked for exec
      - Stage / exec could be the same thing
      - We really need the different run states correlated with run duration
      - Adriel action item : take a look and compile an issue for this with references to the issues requested
    - Create issue to Validate that all attributes from registry in CICD & VCS are covered by the respective signal
    - Reach out async to Carlos and Josh about the processor for span events
    - Check C++ and Python implementations and whether or not they’re matching the latest env spec - update spec compliance as necessary
  - Adoption of CICD conventions in Jenkins: maintainer changes on Jenkins OTel plugin side delayed things, a new maintainer is being onboarded, Dotan reached out to him, to get his attention to the open PRs by Christophe ready for review

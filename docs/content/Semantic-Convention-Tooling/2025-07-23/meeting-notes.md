## Meeting Notes

### Attendees
- Josh Suereth
- Laurent Querel
- Alexandra Konrad
- Jeremy Blythe

### Agenda
- Triage
  - Expanding relative links to full links
    - [josh] Proposal
      - `weaver registry generate –docs_base_url=...`
      - Resulting resolved schema:
        - registry_url: ""
    - [laurent] Ask templates to use a parameter for expanding urls.
    - Could do this in weaver registry resolve (--docs_base_url) or something to resolve relative links always
    - Still need a way to import resolved registries going forward
  - Documentation PR.
- [suereth] Cleaning up YAML loading and schema v2
  - Want to clean up SemconvSpec helper methods.
  - [laurent] Multi-registry support
    - Started to explore apply a more structural approach for semantic convention groups
  - #[serde(untagged)]
- [laurent] Multi-registry support on more than 2 levels.

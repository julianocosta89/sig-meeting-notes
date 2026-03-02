## Meeting Notes

### Attendees
- Patrice Chalin (CNCF)
- [Vitor Vasconcellos](mailto:vvasconcellos1@gmail.com) (Mercado Libre)
- Severin Neumann (Causely)
- Marylia Gutierrez (Grafana Labs)
- Tiffany Hrabusa (Grafana Labs)
- Sophia Solomon (Elastic)
- [Fabrizio Ferri Benedetti](mailto:fabri@elastic.co) (Elastic)
- [Aleksandra Spilkowska](mailto:aleksandra.spilkowska@elastic.co) (Elastic)
- Leandro Caracciolo (OllyGarden)
- Lukasz Ciukaj (Splunk)

### Agenda
- [Vitor] Activity review for locale members ([vitor.vasconcellos@mercadolivre.com](mailto:vitor.vasconcellos@mercadolivre.com))
  - Explore whether there's an existing process to check in with locale members and identify inactive participants.
  - Consider moving inactive members to emeritus status if appropriate.
  - Workflow from JS repo: [https://github.com/open-telemetry/opentelemetry-js/blob/main/scripts/move-to-emeritus.js](https://github.com/open-telemetry/opentelemetry-js/blob/main/scripts/move-to-emeritus.js)
  - Vitor is going to create a PR
- [Severin] Assets for Social Media / Graphics & Visualizations, etc.
  - Three problems:
    - Make accessible to non-designers
    - Make accessible to designers
    - Maintain OTel ownership of the design files forever
  - What should the creation and preservation processes be?
    - Create a file that can be shared (which tool? TBD), preserve that file somewhere in OTel-owned directory, and make a version for non-designers (in Google drive)
  - [Leandro] As a designer, can use whatever tool is best for the community
  - We should be looking for places to add new visuals or improve existing ones
- [Severin] New Triage Process Review
  - [Fabrizio] What about project boards?
    - Most people don’t use them
    - Maybe better for specific projects
      - [Marylia] Declarative config project has a well-used project board, but JS SIG has no other boards
      - [Fabrizio] We should create more projects designed to meet the SIG’s goals
        - [Patrice] Use milestones for quarterly evaluation of the top three improvements we’d like to proactively address
  - [Severin] Would like to move from reactive to proactive so we can actually start writing docs instead of just keeping these running
    - K8s uses a triage rotation process, where one person does triaging a week and all others can focus on other things
  - [Patrice] Meeting early in the year to decide on our top three priorities
  - [Fabrizio] Make buckets of project ideas
    - Can the GC give us ideas about project-wide updates or agendas or themes?
    - [Severin] Collector docs refactoring, Getting Started project, Ecosystem Explorer, Concept page updates
    - [Tiffany] We could consider proposing one of these projects for an LFX mentorship
  - [Patrice] Let’s add some automation and AI assistance: document processes in the /site directory for our own benefit and to point AI agents to
  - [Severin] If anyone is interested in becoming a triager, become a member of the org first. We’d be happy for help with adding labels to issues.

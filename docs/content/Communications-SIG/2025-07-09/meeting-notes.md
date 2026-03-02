## Meeting Notes

### Attendees
- Tiffany Hrabusa (Grafana Labs)
- Lisa Jung (Grafana Labs)
- Sophia Solomon (Elastic)

### Agenda
- [Tiffany] Collector docs refactoring
  - [Tiffany] Starting to do research to find which areas of the docs we should target
    - Four years of Slack messages
    - Site analytics
    - Small question in the Collector survey (to be published)
    - [Kapa.ai](http://Kapa.ai) data?
  - [Tiffany] Following research, I’ll come up with a plan of attack, create issues, and start looking for volunteers to help.
  - [Tiffany] Do you have any thoughts on resources I should consult or changes we should make?
    - [Lisa] Findability is key. The component documentation is hard to find. Adding hyperlinks to the website would at least make them findable, maybe from the navigation menu or a landing page. Also maybe create a list of components with brief descriptions.
    - [Sophia] Agree on findability. Would it be possible to automatically pull in some of the information from the component documentation to the website, for example, the lists of components and descriptions?
      - [Tiffany] There is talk about expanding the registry to import more metadata about the components, such as:
        - Stability
        - Code coverage
        - Which signals are supported
        - Warnings (i.e. stateful, so account for state)
        - Which distros include it
        - Currently seeking codeowners
        - How many codeowners and who they are
        - Component ID used for configuration
        - Which OSs are supported
        - Which resource attributes the component adds

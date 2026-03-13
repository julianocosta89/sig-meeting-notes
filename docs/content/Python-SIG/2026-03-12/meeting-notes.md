## Meeting Notes

### Attendees
- Lukas Hering
- Aaron Abbott (Google)
- Nagkumar Arkalgud (Microsoft)
- Keith Decker (Cisco/Splunk)
- Surya
- Liudmila
- Erdenesaikhan Tserendavga (Cisco/Splunk)
- Hector Hernandez (Microsoft)
- Riccardo Magliocchetti (Elastic)
- Pablo Collins (Cisco/Splunk)
- Josh Winerman (Cisco/Splunk)
- https://github.com/orgs/open-telemetry/projects/88/views/1
  - Filter for stale vs non-stale on the board
  - Would be nice to have a blocked column

### Agenda
- * [Keith] - Need review on this small PR for updating ToolCall types to match semconvs. - https://github.com/open-telemetry/opentelemetry-python-contrib/pull/4218/
- [Erden] - Asking review on Agent types PR for utils
  - Create_agent - https://github.com/open-telemetry/opentelemetry-python-contrib/pull/4217
  - Invoke_agent - https://github.com/open-telemetry/opentelemetry-python-contrib/pull/4274
- [Lukas] Alignment on whether to release random trace id changes github.com/open-telemetry/opentelemetry-python/pull/4854
  - Take a look at whether other SIGs have already implemented that
  - W3C spec needs prototypes so this is helpful
  - Lets bring this to OTel Tues Specification SIG https://groups.google.com/a/opentelemetry.io/g/calendar-spec-general
  - We could merge this as opt-in or as a subclass if we don't want to wait on this PR.
  - We could update the ID generators to still return False so nothing would change for now.
  - The W3C spec has something
- [Liudmila] Completion hook in GenAI Utils https://github.com/open-telemetry/opentelemetry-python-contrib/pull/4315/
- [Aaron] https://github.com/open-telemetry/opentelemetry-python/issues/4957
- [Aaron] contrib releasing process and boilerplate improvements
  - Draft https://github.com/open-telemetry/opentelemetry-python-contrib/pull/4328
  - Alternatively, how do we feel about release-please?
      - Requires you do https://www.conventionalcommits.org/en/v1.0.0
  - Let’s go ahead with first PR that gets rid of boilerplate and look into release-please next
  - Mar 5, 2026

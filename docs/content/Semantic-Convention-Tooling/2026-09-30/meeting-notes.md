## Meeting Notes

### Attendees
- Josh Suereth
- Yordis Prieto
- Liudmila
- Jeremy

### Agenda
- [jerbly] Hard code `.` as the namespace separator? Just want to check as this goes against advice given when I first started live-check. [https://github.com/open-telemetry/weaver/pull/1775](https://github.com/open-telemetry/weaver/pull/1775) - I’m very happy to bake this in as `.` if we want to close that door.
  - We are inconsistent today, e.g MCP's browse by namespace
  - Decision: We should bake-in '.' to match the semconv schema syntax.
  - Decision: Write down project principles
- Yordis: Why -packages in the name in opentelemetry-weaver-packages repo? Seeking to use the same naming across orgs so we know right away what to expect
  - Policies
    - 2 types of policies
    - Owners files
    - Etc
  - [scope]-weaver-packages good name
- Yordis: Should repos have the weaver files to share with others or centralized? Any recommendations
  - Central repo, any app define semconv upstream to the central
  - Each service defines its own and push to central repo for non-service specific
  - Service namespaced
  - Can use provenance (it's buried, but you can find out where an attribute/convention is defined)
  - Critical to use schema v2 and use the schema URL!
- [suereth] Release this week.
  - One more bug fix
- Does weaver support logs?
  - Events = Logs

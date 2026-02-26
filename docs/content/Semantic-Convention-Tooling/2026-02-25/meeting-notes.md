## Meeting Notes

### Attendees
- Alex Van Boxel
- Liudmila Molkova
- Arianna Vespri
- Neil Yashinsky
- [will be late] Josh Suereth
- Jeremy Blythe
- Matthew Hensley (Grafana Labs)

### Agenda
- Rich event body typing [Alex Van Boxel](mailto:alex.vanboxel@gmail.com)
  - Blocked in v2 on [https://github.com/open-telemetry/weaver/issues/892](https://github.com/open-telemetry/weaver/issues/892) - type system
  - Example of nested types bodies [https://github.com/open-telemetry/semantic-conventions/blob/v1.30.0/model/gen-ai/events.yaml](https://github.com/open-telemetry/semantic-conventions/blob/v1.30.0/model/gen-ai/events.yaml)
  - Making a proposal like [https://github.com/open-telemetry/weaver/blob/main/docs/specs/default-templates/default_templates.md](https://github.com/open-telemetry/weaver/blob/main/docs/specs/default-templates/default_templates.md) could be helpful and would help us know what you depend on
- Notes vs. Description [Alex Van Boxel](mailto:alex.vanboxel@gmail.com)
  - description: for telemetry consumers
  - Note: for instrumentations
  - Next steps: issue
- Becoming OTel member: [https://github.com/open-telemetry/community/issues/new?template=membership.md](https://github.com/open-telemetry/community/issues/new?template=membership.md)
- [https://github.com/orgs/open-telemetry/projects/74](https://github.com/orgs/open-telemetry/projects/74)
- Agent.md/claude.md:
  - E.g. don't call unwrap, use expect with reason
  - DRY code
  - Change clippy to flag unwrap even in tests
  - Automation to fmt and clippy after updates

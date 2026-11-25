## Meeting Notes

### Attendees
- Diana Todea (VictoriaMetrics)
- Tiffany Hrabusa (Grafana Labs)
- Severin Neumann (Bronto)
- Reese Lee (New Relic)
- Heather Cloward (Grafana Labs)
- Clayton Cornell (Grafana Labs)
- Leandro Caracciolo (O11yGarden)
- Marylia (Grafana Labs)

### Agenda
- [Tiffany] Mermaid diagrams are becoming integral to OTel blueprints. We’d like to be able to customize the formatting *and* keep them compatible with dark mode. Where does this work need to happen (i.e. where should I raise an issue)?
  - For reference, [this is the PR](https://github.com/open-telemetry/opentelemetry.io/pull/6013) that fixed the customized formatting when we realized the diagrams were unreadable in dark mode.
  - Tiffany to raise an issue in the Comms repo and will check with Grafana platform folks to see if their solution is portable.
    - [https://github.com/open-telemetry/opentelemetry.io/issues/12827](https://github.com/open-telemetry/opentelemetry.io/issues/12827)
- [Diana] RO localization approver workflow is doing well, we can remove the existing docs maintainers. Update on this SIG: new contributors already adding PRs/issues to the main docs repo as well.
  - Removed Severin and Marylia from the approvers group for now
- [Diana] Consult for [https://github.com/open-telemetry/opentelemetry.io/issues/10945](https://github.com/open-telemetry/opentelemetry.io/issues/10945), Patrice, Vitor, Marylia have access to the dashboard and raw data - any feedback?
- [Diana] Consult for [https://github.com/open-telemetry/opentelemetry.io/issues/12080](https://github.com/open-telemetry/opentelemetry.io/issues/12080). I’ll start working on it next - checking on the actual proposed repo structure. Should I go with performance? A bit of a context explanation would be great.
- [Severin] Where people can help!
  - Review open PRs - jump in on any open PR; you don’t need to be an approver to review!
  - Getting started in OTel - big project, long needed
  - Collector docs refactoring - big project, was planned but now possibly out of date
  - Adding graphics and diagrams to docs
  - Editing existing docs pages for style, clarity, consistency

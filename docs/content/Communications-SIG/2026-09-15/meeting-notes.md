## Meeting Notes

### Attendees
- Marylia (Grafana)
- Jay DeLuca (Grafana Labs)
- Severin (Bronto)
- Diana Todea (VictoriaMetrics)
- Julia Furst Morgado (Dash0)
- Vivek Anandaraman (Cloudelu Labs)
- Vitor Vasconcellos

### Agenda
- [severin] Freeze of Ecosystem Section, discuss next steps
  - Vendor Page
    - See Jack’s proposal
  - Integrations Page
    - Depends on the registry
  - Adopters Page
    - [https://www.cncf.io/case-studies?_sft_lf-project=opentelemetry](https://www.cncf.io/case-studies?_sft_lf-project=opentelemetry) – it seems that k8s moved that way
    - Blueprints “Reference Implementations”
  - Registry
    - Limit to Instrumentation Libraries + Collector Components
    - Add a form that asks people to provide details and then we (AI) scan it
      - Make sure you follow semantic conventions, etc.
      - Make sure people create quality components
    - Move it to a dedicated repository so people can step up and become maintainers/approvers for it separately?
      - How does this compete with the ecosystem explorer? We need to make sure that this is not a permanent “work around”
- [severin] Getting Started Project, Revive, how can we make this happen?
  - Julia interested to lead the project with 1-2 more people
  - Check with Blueprints/End User SIG project if there is interest to collaborate, need to make sure to see the boundaries
  - [https://github.com/open-telemetry/opentelemetry.io/blob/main/projects/2026/getting-started-redesign/_index.md](https://github.com/open-telemetry/opentelemetry.io/blob/main/projects/2026/getting-started-redesign/_index.md)
  - Should we fork this out of hugo?

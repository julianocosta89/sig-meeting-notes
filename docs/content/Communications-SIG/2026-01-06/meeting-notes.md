## Meeting Notes

### Attendees
- Patrice Chalin (CNCF)
- Tiffany Hrabusa (Grafana Labs)
- Vitor Vasconcellos (Mercado Libre)
- Leandro Caracciolo (OllyGarden)

### Agenda
- [Tiffany] Question about Phase 2 of Collector docs refactoring: how best to create issues?
  - Tiffany will create all issues for Phase 2 but she will assign them to herself and mark them blocked until the work is ready to be done
  - Tiffany will also create a tracking issue for Phase 2 that includes a comment explaining how the work will proceed. This comment can be referred to when contributors ask to work on issues that are still blocked.
    - Tracking issue: [https://github.com/open-telemetry/opentelemetry.io/issues/8791](https://github.com/open-telemetry/opentelemetry.io/issues/8791)
- [Vitor] PR: AI-generated content detection workflow: [https://github.com/open-telemetry/opentelemetry.io/pull/8637](https://github.com/open-telemetry/opentelemetry.io/pull/8637)
  - Workflow documentation: [https://github.com/vitorvasc/opentelemetry.io/blob/c7f4269dc54e795a0e9dbb274bc995b4385be742/scripts/ai-content-detection/README.md](https://github.com/vitorvasc/opentelemetry.io/blob/c7f4269dc54e795a0e9dbb274bc995b4385be742/scripts/ai-content-detection/README.md)
  - Still needs review, security concerns (are we using **pull_request_target** correctly?)
  - Fine-grained organization token with Copilot access: [https://github.com/open-telemetry/community/issues/3195](https://github.com/open-telemetry/community/issues/3195)
- [Vitor] Link checker is failing due to private Google Docs on specs repo: [https://github.com/open-telemetry/opentelemetry-specification/issues/4812](https://github.com/open-telemetry/opentelemetry-specification/issues/4812)
  - I've temporarily manually set the HTTP status to 206 in latest refcache updates: [https://github.com/open-telemetry/opentelemetry.io/pull/8735](https://github.com/open-telemetry/opentelemetry.io/pull/8735)
- [Tiffany] Arthur Silva Sens, Victoria Nduka, and I will be serving as mentors in the upcoming LFX Mentorship cohort. The goal is to improve the interoperability documentation in both Prometheus and OTel
  - Tiffany will create a tracking issue with links to all artifacts once things are finalized.
- Blog post: 2025 in review
  - Draft: [https://docs.google.com/document/d/1gPHhBCALjku4H6ZoYDCYDfMK4spEarutnfjh5Xo1uho/edit?tab=t.d0z950okmgiy#heading=h.g4rprffphq8b](https://docs.google.com/document/d/1gPHhBCALjku4H6ZoYDCYDfMK4spEarutnfjh5Xo1uho/edit?tab=t.d0z950okmgiy#heading=h.g4rprffphq8b)
  - Example of metrics we can also include in the blog post:
    - Scripts are available at the following repo: [https://github.com/vitorvasc/opentelemetry-contribution-metrics](https://github.com/vitorvasc/opentelemetry-contribution-metrics)
    - ![][image1]
  - Add a looking ahead note to the conclusion about the Collector docs refactoring and graduation
  - Tiffany will finish this up with an aim to publish by end of week or next week
- New landing page:
  - PR: [https://github.com/open-telemetry/opentelemetry.io/pull/8652](https://github.com/open-telemetry/opentelemetry.io/pull/8652)
  - Preview: [https://deploy-preview-8652--opentelemetry.netlify.app/](https://deploy-preview-8652--opentelemetry.netlify.app/)
    - Leandro is also working on the illustrations, currently shown as placeholders

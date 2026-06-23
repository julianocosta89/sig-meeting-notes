## Meeting Notes

### Attendees
- Rob Cowart (ElastiFlow)
- Liudmila Molkova (Google)
- Christophe Kamphaus
- Michele Mancioppi (Dash0)
- Joao Grassi (Dynatrace)
- [15 min late] Josh Suereth (Google)
- [30 min late] Braydon Kains (Google)
- Armin Ruech (Dynatrace)

### Agenda
- (timebox 7 min) Project Status + Triage + Blockers
  - Stability Blockers
  - PR Triage Board: [https://github.com/orgs/open-telemetry/proje](https://github.com/orgs/open-telemetry/projects/67/views/1)
  - [cts/67/views/1](https://github.com/orgs/open-telemetry/projects/67/views/1)
  - Issue Triage Board: [https://github.com/orgs/open-telemetry/projects/131/views/1](https://github.com/orgs/open-telemetry/projects/131/views/1)
- [Surbhi A, 30-45 mins] Generate a final list of open questions and concerns from the semantic convention WG on HTTP Network Timing semantic conventions - [https://github.com/open-telemetry/semantic-conventions/pull/3727](https://github.com/open-telemetry/semantic-conventions/pull/3727)
  - These semantic conventions have been in discussion since Sept 2025, we’ve gone over multiple iterations with browser and android SIG and presented to semantic conventions group a couple times as well.
    - [https://github.com/open-telemetry/semantic-conventions/issues/3385](https://github.com/open-telemetry/semantic-conventions/issues/3385)
    - [https://github.com/open-telemetry/semantic-conventions/issues/2827](https://github.com/open-telemetry/semantic-conventions/issues/2827)
  - Have alignment and approval on the PR from Browser and Mobile folks. Need semantic convention WG approval now.
  - Start/end time and duration -> span
  - Liudmila to leave a comment on the PR or issue with possible options
    - Explore HTTP client spans
  - ALL: Please share other suggestions
    - Michele: each of them should be a span
- [Christophe, 5m] [https://github.com/open-telemetry/semantic-conventions/pull/3793](https://github.com/open-telemetry/semantic-conventions/pull/3793) VCS span conventions - prototype blocking?
- [Liudmila] HTTP route normalization [https://github.com/open-telemetry/semantic-conventions/pull/3806](https://github.com/open-telemetry/semantic-conventions/pull/3806)
- [Liudmila] Schema v2 migration plans
  - Tracking issue [https://github.com/open-telemetry/semantic-conventions/issues/3808](https://github.com/open-telemetry/semantic-conventions/issues/3808)
  - [joao] AFAIK migrating to v2 should be a “no-breaking” change (yaml/definition side) as weaver internally still maps v2 to v1 for processing?

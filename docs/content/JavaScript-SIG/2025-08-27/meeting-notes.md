## Meeting Notes

### Attendees
- Marylia Gutierrez (Grafana Labs)
- Marc Pichler (Dynatrace)
- Luke Zhang (AWS)
- Andrei Borza (Sentry)
- Eric Han (AWS)
- Hector Hernandez (Microsoft)
- Jackson Weber (Microsoft)
- Jonathan Munz (Embrace)

### Agenda
- [david] PR CI improvements ready for review
  - [ ] [https://github.com/open-telemetry/opentelemetry-js-contrib/pull/2866](https://github.com/open-telemetry/opentelemetry-js-contrib/pull/2866)
  - [ ] Testing on push
        - We could use this new workflow to run unit & tav tests on push to main
        - Upload reports on push?
        - We could continue to use “test-all-versions” workflow to run manually
- [david] Should we add the incubator folder in workspaces (contrib)?
  - [ ] [https://github.com/open-telemetry/opentelemetry-js-contrib/pull/2866/files#r2298167938](https://github.com/open-telemetry/opentelemetry-js-contrib/pull/2866/files#r2298167938)
- [marylia] 🥺review please
  - [ ] [https://github.com/open-telemetry/opentelemetry-js/pull/5862](https://github.com/open-telemetry/opentelemetry-js/pull/5862)
  - [ ] [https://github.com/open-telemetry/opentelemetry-js/pull/5875](https://github.com/open-telemetry/opentelemetry-js/pull/5875)
- [marylia] new instrumentation [https://github.com/open-telemetry/opentelemetry-js-contrib/pull/2995](https://github.com/open-telemetry/opentelemetry-js-contrib/pull/2995)
- [marylia] PSA, you might wanna check if your own repos got affected by: [https://semgrep.dev/blog/2025/security-alert-nx-compromised-to-steal-wallets-and-credentials/](https://semgrep.dev/blog/2025/security-alert-nx-compromised-to-steal-wallets-and-credentials/)
- ~/.bashrc - Contains appended sudo shutdown -h 0
- ~/.zshrc - Contains appended sudo shutdown -h 0
- /tmp/inventory.txt - Contains paths to sensitive files
- /tmp/inventory.txt.bak - Backup of inventory file
- Nx build system npm package (@nrwl/nx, nx) in the following versions: 20.9.0, 20.10.0, 20.11.0, 20.12.0, 21.5.0, 21.6.0, 21.7.0, 21.8.0
- @nx/devkit in versions: 21.5.0, 20.9.0
- @nx/enterprise-cloud version 3.2.0
- @nx/eslint version 21.5.0
- @nx/js in versions: 21.5.0, 20.9.0
- @nx/key version 3.2.0
- @nx/node in versions 21.5.0, 20.9.0
- @nx/workspace in versions 21.5.0, 20.9.0
- [luke] feat(instrumentation-aws-sdk): Add semconv attributes for AWS Step Functions #2977 [https://github.com/open-telemetry/opentelemetry-js-contrib/pull/2977](https://github.com/open-telemetry/opentelemetry-js-contrib/pull/2977)
- [Untriaged bugs](https://github.com/open-telemetry/opentelemetry-js/issues?q=is%3Aissue+is%3Aopen+label%3Atriage+label%3Abug+-label%3Apriority%3Ap1++-label%3Apriority%3Ap2++-label%3Apriority%3Ap3++-label%3Apriority%3Ap4+)
- [Untriaged contrib bugs](https://github.com/open-telemetry/opentelemetry-js-contrib/issues?q=is%3Aissue+is%3Aopen+label%3Atriage%2Cbug+-label%3Apriority%3Ap1++-label%3Apriority%3Ap2++-label%3Apriority%3Ap3++-label%3Apriority%3Ap4)
- [Old Contrib PR Triage](https://github.com/open-telemetry/opentelemetry-js-contrib/pulls?q=is%3Apr+is%3Aopen+sort%3Acreated-asc)
- [Old Core PR Triage](https://github.com/open-telemetry/opentelemetry-js/pulls?q=is%3Apr+is%3Aopen+sort%3Acreated-asc)

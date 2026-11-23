## Key Topics
- **OTLP transformer buffer sizing:** Marc proposed dropping the double-pass size calculation in favor of naive buffer doubling. The group agreed the CPU and event-loop gains outweigh the higher worst-case memory use, and Marc will approve the PR.
- **Versioning risk in generated config types:** Experimental config types are embedded in stable types, so a later minor version could break type-checking when two package versions are installed. There's no clean fix yet, so Trent will open a tracking issue.
- **GenAI semantic conventions package:** The package will get a dev/pre-release (e.g., a dash-dev version) before the official release, since the current release scripts would publish unreleased main-branch content. Jamie will confirm the version number, and Marc will generalize the release scripts for future SemConv packages.
- **Shared utilities and redaction:** Wildcard matching (needed by declarative config) and URL redaction are being consolidated. Wildcard matching will go in core, and URL redaction will be shared from instrumentation, with the Contrib implementation preferred. Follow-up work will add a common include/exclude interface.
- **Node 27 and ESM instrumentation:** Node 27 removes `module.register` loader flags in favor of `module.registerHook`, making ESM instrumentation advice a likely focus topic for this year. Focus topics are also moving to the docs, and a new instrumentation package is planned for the stable utilities.

## Action Items
- Trent: Open a tracking issue for experimental-type versioning risks in generated config types.
- Marc: Approve the OTLP transformer PR that removes the double-pass buffer sizing.
- Marc: Prototype workarounds for the config type versioning problem.
- Marc: Adjust the Renovate config if grouped or unmergeable PRs appear.
- Marc: Open PRs moving focus topics to the docs and drafting focus-topic proposals by end of next week.
- Marc: Generalize the release scripts for additional SemConv packages.
- Marc: Review the URL redaction PR and move the utility to the instrumentation package.
- Jamie: Confirm the GenAI SemConv pre-release version number after this afternoon's meeting.
- Trent: Review the GenAI SemConv PR, then coordinate the release with Jamie.
- Trent: Finish the wildcard matcher PR in core, and follow up with a shared include/exclude interface.
- Trent: Ask the Python maintainers how they handle provider conflicts, and check the Java SPI behavior.
- Trent: Ping Dan to rework instrumentation-http using the diagnostic-channel template.
- Trent: Add declarative config support to auto-instrumentations after the start-node-sdk PR lands.
- Jamie: Decide whether to attend the Thanksgiving-week meeting.

## Participants
Trent Mick, Marc Pichler (Dynatrace), Jamie Danielson, Jackson Weber

## Key Topics
- **PHP distro delivery:** Brett's Docker image (copy distro via `COPY --from`) was tagged and works. Michele proposed moving DEB/RPM packaging into the Packaging SIG, with publishing to a CNCF registry.
- **Injector integration:** Michele and Paweł discussed how the OTel injector should activate the PHP distro, preferring a loader extension via `PHP_INI_SCAN_DIR` over patching `fopen`. They will coordinate on a proposal.
- **Semantic conventions versioning:** The SIG discussed whether to bump the semconv version reported by instrumentation, the risks of attribute constants versus hard-coded strings, and using Weaver and the conformance repo to automate checks. Brett has a PR that keeps deprecated attributes and fails the build if attributes are dropped.
- **Span suppression for long-running jobs:** Chris described Laravel queue workers creating unwanted spans and traces. Tobias suggested a rule-based sampler, and Chris will build a reproduction.
- **Roadmap and PHP 8.6:** Brett plans to share his roadmap (SDK 2 via SPI) as issues or wiki content. Paweł will start PHP 8.6 support and thread-safe (ZTS) work, and reviewed the extension's global-state safety.

## Action Items
- Brett: Publish roadmap plans to the OTel PHP wiki or repo, and convert bullets into issues.
- Brett: Chase Severin about the CNCF Claude subscription program submission.
- Brett: Check whether PHP 8.6 polyfills are needed and fix the Slack meeting-notification workflow.
- Paweł and Michele: Sort out the injector proposal via DMs.
- Michele: Check how the PHP SIG integrates the conformance repo into CI, and reply in Slack.
- Chris: Open a meta-issue cataloguing past semconv-related breakages, review Brett's semconv PR, and build a Laravel span-suppression reproduction.
- Paweł: Start PHP 8.6 and thread-safe support, and verify extension global-state safety.

## Participants
Brett McBride, Chris Lightfoot-Wild, Michele Mancioppi, Paweł (Elastic), Tobias Bachert

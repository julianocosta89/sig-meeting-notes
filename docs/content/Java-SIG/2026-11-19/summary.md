## Key Topics
- **JMX inline rules in declarative config (Robert Niedziela):** A PR proposes letting users define JMX metric rules inline, matching the YAML external-file format, so they can ship one file instead of several. Open questions are whether the rule-adding method belongs in the public API or an internal package, and whether to use a list of maps or `ConfigProperties`. The external-file option stays for backward compatibility, and Trask suggested writing up the options.
- **Kafka batch context propagation (Aditya Kousik, Apple):** Current OTel instrumentation of Kafka's record iterator creates duplicate spans and loses trace context when an exception is thrown mid-iteration. Aditya proposed an annotation (or helper API) that extracts the parent context from each consumer record, which would also apply to SQS and other carriers. Alternatives include a shared helper library and an upstream Kafka KIP (KIP-1305) adding per-record context handling. The issue, from 2020, is still open.
- **Next steps on the Kafka proposal:** Trask asked for a PR so the design can be evaluated in code and tests, and wants the OTel-wide approach settled before commenting on the proposal. Lauri noted that a plain Java method call is an alternative to an annotation.
- **CI image security (John Watson):** Concern that the Java and shell CI images should be kept up to date and that CI shell access could expose secrets. Trask confirmed that Renovate auto-updates the images.

## Action Items
- Robert Niedziela: Write up the public vs. internal API options and the `ConfigProperties` vs. list-of-maps options for the JMX rules PR.
- Aditya Kousik: Test whether context propagates to executor threads, as Trask questioned, and summarize the approaches on the issue or mailing list. Submit a PR if the design looks right.
- Trask Stalnaker: Confirm that all CI images are being updated by Renovate.

## Participants
Trask Stalnaker, Robert Niedziela, Aditya Kousik, Lauri Tulmin, John Watson

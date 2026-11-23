## Key Topics
- **Weaver resolver V2 rewrite:** Josh Suereth's large PR (about two weeks of work) restructures dependency resolution into an 11-step algorithm, adds a shared graph library, and keeps V1 as a fallback. Unit tests run V1 test cases through V2 to confirm matching output. The team agreed the algorithm spec is the main thing to review.
- **Breaking changes and deprecations:** Duplicate refs are now errors, dependency upgrades check the new version, and the API cache changed (breaking for API users, not Weaver users). Deprecated signal ref groups remain allowed because GenAI conventions use them. Fixes were made for entity association and event name inheritance in refinements.
- **Release timing:** The team will wait for this PR, aiming to review and release next week. If review can't finish in a week, they'll release the current version this week.
- **Conformance and live check:** Liudmila Molkova demoed conformance coverage reports built from Weaver live check output. Discussion covered versioning the live check JSON output, which has no schema, and a possible OTel conformance badge for libraries and products.
- **Rust tooling and crate publishing:** Jeremy Blythe described a Rust proc-macro library that generates type-checked code from a Weaver registry. The team discussed publishing Weaver crates to crates.io and stabilizing the CLI, though the public API needs design work first.

## Action Items
- Liudmila Molkova: Check whether GenAI conventions intentionally use refgroups that target non-attribute-group signals.
- Liudmila Molkova: Run the filed bugs against the PR using AI and report which still apply.
- Josh Suereth: Restore the method doc comments, clean up function signatures, verify the V2 fallback error no longer appears in the downstream check, and make the algorithm spec available for review.
- Jeremy Blythe: Review the spec and battle-test it with feedback loops, review the linearization change and its impact on Forge and live check, and continue squashing live check issues.
- Team: Review and release the Weaver resolver PR next week.

## Participants
Josh Suereth, Jeremy Blythe, Liudmila Molkova

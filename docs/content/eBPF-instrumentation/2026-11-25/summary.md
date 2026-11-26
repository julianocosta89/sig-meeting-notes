## Key Topics
- **Experimental features in main:** Gregor proposed merging dynamic instrumentation early behind experimental flags in config and an internal Go package, instead of maintaining a drifting feature branch. The group agreed to try it.
- **GPU device metrics:** Mattia and Marc have overlapping NVML-based GPU metric PRs. The group discussed metric naming, the NVML linking approach, and overlap with Inspector Gadget and Roy's open-source exporter. They agreed to proceed and document decisions in an issue.
- **Release 1.1.0:** Two PRs remain before the release. Mattia will merge them and start the release process.
- **Rust support and performance:** Nikola and Pablo are adding partial Rust support, with gotchas around memory loading. The group discussed whether rewriting parts of the eBPF event pipeline in Rust is worthwhile, and concluded that Go optimization should come first.
- **JSON parsing and ring buffer sizing:** Rafael's JSON scanner PR was held because it drops truncated payloads, and the group leaned toward encoding/json/v2 or a similar library. They also agreed to reduce the ring buffer from 16MB to 1MB, with a possible stress test.

## Action Items
- Gregor: Open a PR to main with experimental dynamic instrumentation features, kept in an internal package, and look into automation to detect public API changes.
- Mattia and Marc: Open a GitHub issue to document GPU metrics decisions, agree on metric names, and merge both PRs.
- Mattia: Review Inspector Gadget and Roy's exporter for ideas, and collect links.
- Mike: Find and share the Inspector Gadget KubeCon talk link.
- Mattia: Merge the two 1.1.0 release PRs and start the release process.
- Giuseppe: Request reviews on the OBCLI/OPAM discussion.
- Rafael: Investigate whether a JSON library can handle truncated payloads, and hold the scanner PR until then.
- Rafael and Nikola: Move the ring buffer to 1MB and consider a stress test next week.
- Nikola and Rafael: Follow up on KubeCon EU and related conference talk submissions.

## Participants
Aryan Bakliwal, Stephen Lang, Giuseppe Ognibene, Gregor Zeitlinger, Mike Dame, Rafael Roquetto, Nikola Grcevski, Mattia, Marc Tudurí, Roy Reshef

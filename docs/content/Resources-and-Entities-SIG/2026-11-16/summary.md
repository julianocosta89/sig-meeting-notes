## Key Topics
- **Dmitrii's Entity Identity Scope PR:** Reviewed new reviewer feedback. The group agreed that relative IDs (e.g., a container name) need to be paired with their parent entity (e.g., pod UID) to form a unique identity, and that entity events need clearer definition in the spec.
- **Resource vs. entity modeling:** Jake Dern raised concerns that tying entities to resources limits how OTel Arrow represents multiple internal entities of the same type. Discussion covered the logical/physical blurring in resources and the cost of repeating resource attributes for profiling data.
- **Wording of the spec:** Agreed to reword the guidance on global vs. local IDs so it doesn't tell implementers to ignore documentation. Also clarified that an entity can replace another entity's identity through the entity merge algorithm.
- **Alpha maturity milestone:** Reviewed remaining blockers for marking Entities alpha. Non-blockers include VM semantic conventions, entity class differentiation, cross-telemetry guidance, and MDGen config links. Go fine-grained resource detectors and the OTel Entities env resource detector default are deferred to beta.

## Action Items
- Dmitrii Anoshin: Address PR review comments offline, including the entity events gap; Splunk team member to continue collector work.
- Josh Suereth: Reword the ID scope/documentation text; confirm status of the SDK startup spec PR; build a demo of collector processors distinguishing remote vs. local entities; follow up with the Go SIG on fine-grained resource detectors; find the Apache project link for entity relationship storage; update the milestone board, notify the group, and open PRs to mark Entities alpha.
- Jake Dern: Share the data flow engine RFC draft with the SIG.
- krajo (Grafana Labs): Review the entity merge comment in the PR.
- Remove the MDGen config-link item from the board (Dmitrii/Josh).

## Participants
Josh Suereth (Google LLC), krajo (Grafana Labs), Dmitrii Anoshin (Individual), Jake Dern (F5, Inc.), Arve Knudsen (Raintank, Inc. – Grafana Labs)

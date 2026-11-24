## Key Topics
- Proposed "post-transformation filter": a second filter pass after transforms run, reusing the same filter logic; Jacob came to accept it since policy definitions are now separated.
- Policy delivery structure over OpAMP, HTTP, and file: the spec needs to define the body structure and a typed/versioned key (or header) so backends know the expected format; JSON chosen for file-based policies over protobuf and YAML.
- Policy merging and priority: full-policy overrides by ID, file as lowest priority and OpAMP as highest; open question on handling conflicts between same-priority providers (error vs. deterministic convergence).
- Existing implementations and scope: Jack has production implementations (Elastic, Contrib) driven by customer requests and is concerned about unspecified features; Jacob favors a tight initial scope and merging the base PR quickly.
- Conformance suite: Jacob plans a cross-implementation conformance test suite (OTLP in, policies applied, outputs and stats checked) to keep implementations consistent.

## Action Items
- Jacob: write up a PR defining delivery structures (OpAMP keys, HTTP headers and body, file JSON) in the proto spec.
- Jack: review the post-transformation filter PR and the enablement PR comments.
- Jacob, Raphael, and David: update the proof-of-concept collector implementation once the base PR merges.
- Raphael: review the merge/conflict discussion and the PR.
- Jacob: rewrite his proof-of-concept conformance suite against the spec and propose a new OTel repo for it.
- Jacob: read through Jack's delivery and merge notes.

## Participants
Jacob Aronoff (Cribl), Jack Shirazi, Raphael Menderico

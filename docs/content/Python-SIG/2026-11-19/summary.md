## Key Topics
- Triage of open PRs and issues, including a request to open a tracking issue for HTTP client TODOs (URL/scheme handling) rather than separate PRs.
- Proposal to add the missing `kind` attribute to the API span ABC for custom span implementations. Leighton is fine with the trivial change if the messaging is clear.
- Riccardo's WSGI PR to capture HTTP request/response body content per the new semantic convention. Aaron raised questions on size limits, truncation config, streaming versus buffering, and the `_ref` convention for large payloads.
- Riccardo asked whether to wait on the Bedrock instrumentation deprecation PR until pending GenAI bug fixes land. Dylan agreed to wait for the next release.
- Sajid, a new contributor, introduced himself, flagged a docs PR on declarative configuration, and got guidance on contributing and reviewing PRs.

## Action Items
- Tammy: ask for more context on a PR involving context vars and tracing.
- Leighton: comment on the old logging docs issue to reflect the logging API/SDK/instrumentation split.
- Riccardo: open a tracking issue for the HTTP client TODOs requested from the contributor.
- Aaron: review the WSGI body-capture PRs and the GCP resource detector PR.
- Tammy: review the SQLAlchemy PR and look at the gRPC AIO cancel propagation PR later.
- Dylan and Riccardo: hold the Bedrock deprecation PR until the next release.
- Sajid: review the FastAPI PR on deprecating OTLP export in contrib.

## Participants
Riccardo Magliocchetti, Diego Hurtado, Pablo Collins, Tammy Baylis, Emídio Neto, Leighton Chen, Aaron Abbott, Dylan Russell, Sajid Ali Syed, Liudmila Molkova

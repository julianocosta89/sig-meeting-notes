## Key Topics
- Discussion on the deployment type and target attributes, emphasizing the need for expert input from Kubernetes and CICD SIGs.
- Proposal for a declarative configuration structure to manage semantic conventions, including YAML structures for better validation.
- Review of GCP AppHub conventions and the need for clarity on attributes related to spans and their usage.
- SQL Commenter propagator behavior and the potential need for a dedicated propagator for SQL serialization.
- Consideration of event.name attributes and their implications for consistency in OpenTelemetry.

## Action Items
- Form a group of experts to stabilize deployment attributes and discuss with relevant SIGs.
- Update the comment on the CICD scope link regarding deployment attributes.
- Michael Safyan to add GCP AppHub destination attributes to the PR and document them in YAML.
- Create an issue in the spec repo to discuss the SQL commenter propagator.
- Trask Stalnaker to provide feedback on the event.name attribute proposal.

## Participants
Liudmila Molkova, Christophe Kamphaus, Trask Stalnaker, Josh Suereth, Michael Safyan, Gregor, Robert

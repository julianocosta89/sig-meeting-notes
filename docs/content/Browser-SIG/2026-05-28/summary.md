## Key Topics
- Discussion on handling URL mutations in OpenTelemetry browser signals, including whether to include query strings in the full URL.
- Consideration of entity identification for browser documents and the potential need for new attributes.
- Review of a PR regarding the removal of exclusivity between user agent data and URL user agent.
- Proposal for configurable max attempts for sending signals from the browser to the collector to address rate limits.
- Updates on two PRs for migrating special instrumentation and their differing approaches.

## Action Items
- Create an issue to further discuss the attributes for browser document entities.
- Review and provide feedback on the PRs related to special instrumentation.
- Check with the JavaScript SIG regarding the impact of configurable max attempts on transport protocols.

## Participants
Maxime Quentin, Martin Kuba, Jared Freeze, Joaquín Díaz, David Luna Bistuer, Christopher Arredondo

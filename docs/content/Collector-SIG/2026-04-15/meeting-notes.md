## Meeting Notes

### Attendees
- [Andrew Wilkins](mailto:axw@elastic.co) (Elastic)
- Josh MacDonald (Microsoft)
- Dmitry Anoshin (Splunk)

### Agenda
- [15 min] Go through high priority issues for [stability phase 1](https://github.com/open-telemetry/opentelemetry-collector-contrib/issues/44130) listed on the [**board**](https://github.com/orgs/open-telemetry/projects/178)
- [Andrew] Challenges with the scraper interface
  - Streaming large batches
  - Committing cursors
  - [discussion] this sounds like what the stanza package helps to do, it will wait for the consume function to return (with success) before updating a checkpoint
  - Related to [https://github.com/open-telemetry/opentelemetry-collector/pull/14469](https://github.com/open-telemetry/opentelemetry-collector/pull/14469), for scrapers, however the new extension does not help coordinate updating the checkpoint.
  - Possible to bridge the gap between stanza receivers and the scraper extensions to signal the availability of logs data. This is because stanza currently watches files to trigger itself.

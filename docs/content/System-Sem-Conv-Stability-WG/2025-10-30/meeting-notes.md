## Meeting Notes

### Attendees
- Braydon Kains (Google)
- Dmitry Anoshin (Splunk)
- Christos Markou (Elastic)
- Roger Coll (Elastic)

### Agenda
- [braydonk] Identifying files [https://github.com/open-telemetry/semantic-conventions/pull/2657#discussion_r2474290953](https://github.com/open-telemetry/semantic-conventions/pull/2657#discussion_r2474290953)
  - [suereth] Executable ids are used to tie symbol-tables -> profiles.  Executable name is used to group flame graphs in profiling.
  - Let's make sure we're coordinating discussions between Profiling SIG + System SIG
- [braydonk] How to adjust guidance to explain counter resets [https://github.com/open-telemetry/opentelemetry.io/issues/8275](https://github.com/open-telemetry/opentelemetry.io/issues/8275)
  - I wonder if something for our group would be helpful, explaining that a machine reboot is the type of event that would reset counters
- [braydonk] Should all metrics that measure time be in seconds? [https://github.com/open-telemetry/semantic-conventions/pull/2996#discussion_r2475159778](https://github.com/open-telemetry/semantic-conventions/pull/2996#discussion_r2475159778)

## Meeting Notes

### Attendees
- **Bob Strecansky**
- **Chris Lightfoot-Wild**
- **Pawel Filipczak**
- **Sergey Kleyman**
- **Marylia Gutierrez**
- **Samuel Arogbonio**

### Agenda
- [MG] - Declarative config - ready for primetime?
- [MG] - Database semantics - has been stable since the beginning of the year (migration) - feel free to reach out to Marylia Gutierrez
  - ENV variable - “opt in” - for the HTTP and the DB semantic conventions (they have become stable recently).  Let people know this exists (with release notes).   After 6 months, these can be removed.
  - Example of transition being done in postgres in JS: [https://github.com/open-telemetry/opentelemetry-js-contrib/pull/2881](https://github.com/open-telemetry/opentelemetry-js-contrib/pull/2881)
  - Guide on how to do that: [https://github.com/open-telemetry/opentelemetry-js/blob/main/doc/semconv-stable-http-and-database.md](https://github.com/open-telemetry/opentelemetry-js/blob/main/doc/semconv-stable-http-and-database.md)
  - Env variable: OTEL_SEMCONV_STABILITY_OPT_IN=http/dup,database/dup
- [MG] - Contributor experience - a survey appears for new contributors with new PRs.  This repo does not have that yet.  Marylia will add to our repo and come back later with responses.
- [SA] - Trying to build
  - Gateway collector, event collector, agent
  - Gateway seems to consume lots of memory
  - Setup a soft limit to ensure we don’t lose data
  - When we get to the soft limit, we drop data (miss out on metrics and logs)
    - Is it normal for the gateway collector to consume lots of memory?
      - Processing, enriching data
  - Is OT sensitive to issues with the backend

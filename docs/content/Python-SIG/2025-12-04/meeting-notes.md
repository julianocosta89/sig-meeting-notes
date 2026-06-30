## Meeting Notes

### Attendees
- Dylan Russell (google)
- Hector Hernandez (Microsoft)
- Joshua Winerman (Cisco/Splunk)
- Aaron Abbott (Google)
- Keith Decker (Cisco/Splunk)
- Riccardo Magliocchetti (Elastic)
- Shuwen Pan (Cisco)
- Tammy Baylis (SolarWinds)

### Agenda
- [Riccardo] Logs stabilization update
  - 1.39.0 is out!
    - Merged [https://github.com/open-telemetry/opentelemetry-python-contrib/pull/3589](https://github.com/open-telemetry/opentelemetry-python-contrib/pull/3589)
    - Merged Events API deprecation [https://github.com/open-telemetry/opentelemetry-python/pull/4654](https://github.com/open-telemetry/opentelemetry-python/pull/4654)
      - Released open-ai-v2 2.2b0, dropping use of Events API (and a bunch more changes)
      - Traceloop moved to plain log records (from 0.48.1) [https://github.com/traceloop/openllmetry/pull/3453](https://github.com/traceloop/openllmetry/pull/3453)
      - opentelemetry-instrumentation-google-genai was still importing Event [https://github.com/open-telemetry/opentelemetry-python-contrib/pull/3973](https://github.com/open-telemetry/opentelemetry-python-contrib/pull/3973)
  - Next steps:
    - sort out logging handler in the next release
      - [aaron] +1
    - First regression reported: warnings in test utils from _events import [https://github.com/open-telemetry/opentelemetry-python/issues/4836](https://github.com/open-telemetry/opentelemetry-python/issues/4836) (added feedback table in the tracking issue description [https://github.com/open-telemetry/opentelemetry-python/issues/4750](https://github.com/open-telemetry/opentelemetry-python/issues/4750))
    - Azure monitor regression [https://github.com/open-telemetry/opentelemetry-python/issues/4838](https://github.com/open-telemetry/opentelemetry-python/issues/4838)
    - [dylan] do we eventually remove the `_` from logs package. Do we bump the major release?
      - Keep _logs around but deprecated once we’re ready for unprefixed logs
- [Riccardo] 1.39.0 regressions:
  - Synthetic sources [https://github.com/open-telemetry/opentelemetry-python-contrib/issues/4001](https://github.com/open-telemetry/opentelemetry-python-contrib/issues/4001)
    - Hector: I can take a look
- [Riccardo] langchain instrumentation PRs without component owners review, are we missing notifications or lost interest in the instrumentation? [https://github.com/open-telemetry/opentelemetry-python-contrib/pulls?q=is%3Apr+is%3Aopen+langchain+](https://github.com/open-telemetry/opentelemetry-python-contrib/pulls?q=is%3Apr+is%3Aopen+langchain+)
  - Not sure component_owners.yml is working fine all the time: on a botocore PR the owners where not reviewers but worked fine for an urllib3 PR
    - Liudmila: I’ll cleanup the generic genai list and instead just use specific ones for instrumentations
    - Looks like that’s the cause of missing reviewers:
      - *Ignoring error: RequestError [HttpError]: Reviews may only be requested from collaborators. One or more of the users or teams you specified is not a collaborator of the open-telemetry/opentelemetry-python-contrib repository. - [https://docs.github.com/rest/pulls/review-requests#request-reviewers-for-a-pull-request](https://docs.github.com/rest/pulls/review-requests#request-reviewers-for-a-pull-request)*
- [Mani] PTAL  [https://github.com/open-telemetry/opentelemetry-python/issues/4818](https://github.com/open-telemetry/opentelemetry-python/issues/4818)
  - Aaron: AFAIR we have a different API for avoiding a global lock
- Mani: sounds good

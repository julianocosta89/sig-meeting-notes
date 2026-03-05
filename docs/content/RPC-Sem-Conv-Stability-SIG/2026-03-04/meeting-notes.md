## Meeting Notes

### Attendees
- Trask
- Liudmila
- Matthew
- Steve

### Agenda
- Project board: [https://github.com/orgs/open-telemetry/projects/161](https://github.com/orgs/open-telemetry/projects/161)
- Remove client.address | port ? [https://github.com/open-telemetry/semantic-conventions/pull/3488](https://github.com/open-telemetry/semantic-conventions/pull/3488)
- Do we want to record rpc status code when an operation has failed? [https://github.com/open-telemetry/semantic-conventions/issues/3478](https://github.com/open-telemetry/semantic-conventions/issues/3478)
  - Now:
    - Success case:
      - `rpc.response.status_code` = OK // DEADLINE_EXCEEDED, etc - not an error without `error.type`
    - Failure case
      - `error.type` = INTERNAL
      - `rpc.response.status_code` = INTERNAL
  - What if didn't require recording response code when it's the same as error type
    - Pros: less duplication
    - Cons: consistency.
      - E.g. I want to # of calls per status code or find all calls with status X, need to use different attribute names depending
      - HTTP uses both
      - `Error.type` note says to use both
- Python prototype [status](https://github.com/open-telemetry/semantic-conventions/issues/3477#issuecomment-3986791850)
- server.address in Dubbo Client LB: [https://github.com/open-telemetry/semantic-conventions/issues/3408#issuecomment-3962979434](https://github.com/open-telemetry/semantic-conventions/issues/3408#issuecomment-3962979434)

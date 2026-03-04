## Key Topics
- Discussion on the usefulness of internal metrics and whether to export traces each time new trace data is sent.
- Proposal to disable internal trace metrics by default due to potential confusion and verbosity.
- Examination of whether connection info should include network namespace for better identification of connections.
- Consideration of network interfaces and potential duplication of metrics in Kubernetes environments.

## Action Items
- Nikola to propose an issue to disable internal trace metrics by default.
- Mattia to consider proposing a change to include network namespace in connection info struct.

## Participants
Mike Dame, Nikola Grcevski, Tyler Yahn, Nimrod Avni, MM Mario Macias, Mattia Meleleo, Rafael Roquetto

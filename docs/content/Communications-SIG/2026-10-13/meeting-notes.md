## Meeting Notes

### Attendees
- Tiffany Hrabusa (Grafana Labs)
- Severin Neumann (Bronto)
- Vivek Anandaraman
- Jack Baldry (Grafana Labs)

### Agenda
- [All] Distributed docs Q&A
  - Context: Large, growing project. Other SIGs should own their docs, but not all do. For those that do work with Comms, we have become a bottleneck. How can we make our docs decentralized to avoid the bottleneck? We have submodules, but they are problematic.
    - [Jack] Subtrees are a similar process to submodules that can allow you to contribute upstream more easily.
  - [Jack] We have a job that fetches/clones the repositories. All changes by PRs so org workflows can run. We have a monorepo, but going from mono back to source repos is not very efficient.
    - Because we don’t use git primitives, we have to reinstate metadata to allow us to work backwards.
  - [Jack] Does OTel have private repos?
    - [Severin] No, not that are involved in our docs publishing.
  - [Jack] We can help review/poke holes in a design doc to help OTel docs implement a distributed docs setup
  - [Jack] It’s a good idea to share data/background on what is “important” for linting/reviewing documentation, so when you impose checks, you can back it up.
  - [Jack] Linkchecking is complicated - we had to check only a subset of links. We needed a whole separate process for whole-site checking. Edge cases are still an issue.
  - [Severin] We urgently need to fix our CODEOWNER situation. We tried component owners, but their PR reviews are not mandatory. Back to the beginning. Maybe we just need to accept that there is no good solution and we need to give many people write permissions.
    - [Jack] We’ve used policybot but it might not work for OTel. Invalidates maintainer approval if they’ve committed to PR.
    - [Jack] Opa - could be open-sourced?
  - [Severin] We will scope out our plan and share it with Grafana docs platform to see what they think.

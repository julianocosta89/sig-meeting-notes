## Meeting Notes

### Attendees
- Kayla Reopelle
- Matt Wear
- Robb Kidd
- Xuan Cao
- Hannah Ramadan

### Agenda
- [Spec SIG](https://docs.google.com/document/d/1pdvPeKjA8v8w_fGKAN68JjWBmVJtPCpqdi9IZrd6eEo/preview) Update (max 15 min)
- Core ([Issues](https://github.com/open-telemetry/opentelemetry-ruby/issues) / [PRs](https://github.com/open-telemetry/opentelemetry-ruby/pulls))
  - Relocate api projects into an api folder to enable introducing an api common & eventually have log/metric api as dependency of the api gem once stable [james] [https://github.com/open-telemetry/opentelemetry-ruby/pull/2390](https://github.com/open-telemetry/opentelemetry-ruby/pull/2390)
    - Intention would be to replicate it to sdk.
    - Not quite time for this refactor. Would like to revisit once we have the technical committee review metrics and logs for stability.
    - In the future, need to think about what we want to do with the API gem (do we keep the signals separate? Bring them together? What are other sigs doing?)
  - Logs and metrics API milestones
    - [https://github.com/open-telemetry/opentelemetry-ruby/pull/2378](https://github.com/open-telemetry/opentelemetry-ruby/pull/2378)
    - [Logs Stability Milestone](https://github.com/open-telemetry/opentelemetry-ruby/milestone/12)
    - [Metrics Stability Milestone](https://github.com/open-telemetry/opentelemetry-ruby/milestone/11)
    - PR reviews for these issues should update the spec compliance document
    - We’ll run a weekly compliance check to catch anything we missed from the updates
    - Check in next month to see if it makes sense to add the same spec compliance work for Traces. Let’s focus on Metrics and Logs for now since they’re not stable yet.
- Contrib ([Issues](https://github.com/open-telemetry/opentelemetry-ruby-contrib/issues) / [PRs](https://github.com/open-telemetry/opentelemetry-ruby-contrib/pulls))
  - Define devcontainer environments [https://github.com/open-telemetry/opentelemetry-ruby-contrib/pull/2315](https://github.com/open-telemetry/opentelemetry-ruby-contrib/pull/2315) and verify them in ci
    - Robb will review
  - Make unstable metrics and logs APIs available to instrumentation
    - [https://github.com/open-telemetry/opentelemetry-ruby/pull/2384](https://github.com/open-telemetry/opentelemetry-ruby/pull/2384)
    - [https://github.com/open-telemetry/opentelemetry-ruby-contrib/pull/2569](https://github.com/open-telemetry/opentelemetry-ruby-contrib/pull/2569)
    - Matt will open an issue that documents the release process and start breaking up the draft PRs into other PRs
    - Would also benefit this PR: [https://github.com/open-telemetry/opentelemetry-ruby-contrib/pull/1785](https://github.com/open-telemetry/opentelemetry-ruby-contrib/pull/1785)
    - OpenAI instrumentation (kayla)
      - Update the name at a minimum
      - Matt will think about this as part of the sequencing
- Auto Instrumentation ([Issues](https://github.com/open-telemetry/opentelemetry-ruby-instrumentation/issues) / [PRs](https://github.com/open-telemetry/opentelemetry-ruby-instrumentation/pulls))
- Burning questions?
  - Bots and low effort PRs
    - Remove the “good first issue” label
    - Discussions are for humans as a policy - PR descriptions should be written by humans or not directly by LLM
    - The collector has a checkbox you need to check for AI usage in the PR template. Claude won’t check the box by default. Could also be benefitted by a minimal PR template. (Matt will take care of this)
    - If the template is replaced with a wall of AI text or the box isn’t checked, we kind of know. If a human opens the PR, there’s an obligation to review. If a bot opens a low-effort PR, can let the stalebot handle it or close it ourselves if it’s obnoxiously bad.
- ✨ Happy Reports ✨

## Meeting Notes

### Attendees
- Hannah Ramadan
- Kayla Reopelle
- Xuan Cao
- Matt Wear

### Agenda
- [Spec SIG](https://docs.google.com/document/d/1pdvPeKjA8v8w_fGKAN68JjWBmVJtPCpqdi9IZrd6eEo/preview) Update (max 15 min)
  - [https://github.com/open-telemetry/opentelemetry-specification/pull/4738](https://github.com/open-telemetry/opentelemetry-specification/pull/4738) - Request to look at the OTEP, read it, provide feedback
  - [https://github.com/open-telemetry/opentelemetry-specification/pull/4931](https://github.com/open-telemetry/opentelemetry-specification/pull/4931) - How would we actually implement this/make it work? Been discussed for a long time
  - [https://github.com/open-telemetry/opentelemetry-specification/pull/5104](https://github.com/open-telemetry/opentelemetry-specification/pull/5104) - expand span processor
- Core ([Issues](https://github.com/open-telemetry/opentelemetry-ruby/issues) / [PRs](https://github.com/open-telemetry/opentelemetry-ruby/pulls))
  - ​​[xuan] [https://github.com/open-telemetry/opentelemetry-ruby/pull/2161](https://github.com/open-telemetry/opentelemetry-ruby/pull/2161)
    - Discussion over the last few weeks
    - Ruby cannot have an extension similar to Java / PHP because of how the language works
    - Most similar to the Go agent
    - Look at the feedback overall
    - Please take a look
- Contrib ([Issues](https://github.com/open-telemetry/opentelemetry-ruby-contrib/issues) / [PRs](https://github.com/open-telemetry/opentelemetry-ruby-contrib/pulls))
  - [https://github.com/open-telemetry/opentelemetry-ruby-contrib/issues/2368](https://github.com/open-telemetry/opentelemetry-ruby-contrib/issues/2368)
    - Python is probably the most similar. They have celery, rebelaid?
    - For the most part, the only semantic convention Matt found them using was [messaging.id](http://messaging.id), the rest was in a library-specific namespace
    - We’re probably an oddball at the moment
    - We’re defining a lot of custom attributes in the messaging namespace and haven’t seen that in the other implementations
    - Ultimately, whatever namespace is owned by semantic conventions, they could add an attribute of the same name and there could be a conflict
    - Anything we’re adding should go under a different namespace
    - We may have been too hesitant in the past to use our own namespace
    - In the future, know that this is the rule:
      - Don’t add new attributes under semantic conventions
      - If we have a new attribute, add it in our own namespace
      - We have more liberty than we probably think
    - We also have access to the Ruby/Rails namespace in semconv now, so we could try to document things there too
- Burning questions?
  - [xuan] [https://github.com/open-telemetry/opentelemetry-ruby-instrumentation/pull/15](https://github.com/open-telemetry/opentelemetry-ruby-instrumentation/pull/15) - PTAL
  - Renovate
    - Kayla - The updates are running too frequently and it’s difficult to manage
      - No other repos use monthly updates, so wanted to check in
      - Matt, Hannah comfortable with moving to monthly
    - Rebase doesn’t always work
    - Button to merge into main - Kayla will fix (also merge queues too)
      - UPDATE: [https://github.com/open-telemetry/community/issues/3530](https://github.com/open-telemetry/community/issues/3530)
  - [https://github.com/open-telemetry/opentelemetry-ruby-contrib/pull/1797](https://github.com/open-telemetry/opentelemetry-ruby-contrib/pull/1797)
    - Concerned about setting a bad precedent for moving things into contrib
    - Idea to try to get it as a native instrumentation
    - Other languages have this in contrib
    - Kayla will finish her PR review and read through the comments
- ✨ Happy Reports ✨

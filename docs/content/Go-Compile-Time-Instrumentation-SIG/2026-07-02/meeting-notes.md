## Meeting Notes

### Attendees
- [Dario Castañé](mailto:dario.castane@datadoghq.com) (Datadog); **Facilitator**
- Kemal Akkoyun (Datadog)
- Huxing Zhang (Alibaba)
- Haibin Zhang (Alibaba)
- Azhar Momin
- Xabier Martinez (Cabify)

### Agenda
- [Xabier Martinez](mailto:x42.martinez@gmail.com)roadmap v1 review
  - [Kemal] Maintainers should take over stopped PRs
  - [Xabier] Agreed.
  - [Dario] Conclusion: asynchronous work, pushing as much as possible during this week
- [Xabier Martinez](mailto:x42.martinez@gmail.com) v1 release creation tasks (+ ownership):
  - [Xabier] Should we do this async or now?
  - [Kemal] Let’s do it now.
  - [Kemal] I can take the blog post and announcement.
  - [Kemal] I can also take care of the release cut (by tag).
  - [Xabier] I can help with the blog post.
- Azhar Momin: Switch to [go.opentelemetry.io/](http://go.opentelemetry.io/compile-instrumentation)otelc module path for v1?
  - [Kemal] We should check other projects and act accordingly
  - [Azhar] Other projects use [go.opentelemetry.io](http://go.opentelemetry.io)
  - [Kemal] Then let’s do it
  - [Kemal] We should also check with admins if we need to do something to use [go.opentelemetry.io](http://go.opentelemetry.io)
  - [All] Agreed on using [go.opentelemetry.io/otelc](http://go.opentelemetry.io/otelc) as module path
- [Xabier Martinez](mailto:x42.martinez@gmail.com) OBI vs otelc
  - [Xabier] How can we collaborate with them and clarify when to use one or the other?
  - [Kemal] We could write a blog post to send a clear message between both projects, explaining cons/pros and goals of each tool.
  - [Kemal] In the future we can collaborate further with the OBI team, finding ways to work together.

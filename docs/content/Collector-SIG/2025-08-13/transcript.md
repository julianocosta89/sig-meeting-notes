SIG: Collector SIG
Date: 2025-08-13
Duration: 50 minutes
============================================================

## Zoom Recording Transcript

**Sylvain** 00:48 Hello, everybody.
**Antoine Toulme** 00:51 Good morning.
Afternoon.
**Sean Marciniak** 00:58 Good friends.
**Andrzej Stencel** 02:57 Hello.
**Antoine Toulme** 03:09 Hey, can we get started?
Is Pablo here.
Should we go over his announcements?
Okay, so if he wants to add debug-level log for each error returned by a consume call… I don't know what that means, but that sounds scary, but at the same time, it's a debug level.
Anything we should do about that?
**Jade Guiton** 03:48 I think the announcement maybe should have been not for this PR, but for the corresponding RFC amendment.
**Antoine Toulme** 03:57 Oh, yeah.
**Jade Guiton** 03:58 ….
**Antoine Toulme** 03:59 separate PR.
**Jade Guiton** 04:01 Yeah, I'll add the… The link in the… There we go.
**Antoine Toulme** 04:06 I… I see it.
**Jade Guiton** 04:10 There was already, something in the RFC suggesting that we should add a debug log for all outcomes of a consume call, and essentially this amendment restricts it to just errors, because Success outcomes don't really have much… there's not much information to log anyway.
**Antoine Toulme** 04:32 Thank you, Shade.
Okay?
**Jade Guiton** 04:45 So, if there are any objections to the… to the URL team, and please, leave a comment on the GitHub issue.
**Antoine Toulme** 05:02 Awesome.
**Sean Marciniak** 05:03 And the expectation that every… Call on the call chain little login error.
So, say if the exporter fails, is that going to cause each a third Processors, connectors, and receivers to also emit an error?
**Jade Guiton** 05:23 I think the internal implementation here is that it would make use of the… The new downstream error wrapper, which allows us to determine whether the pipeline has seen an error, before or not. So, in principle, we should only get an error log for the very first consume call that fails, not for all the parent consume calls.
**Sean Marciniak** 05:46 Yep. Okay.
**Arthur Silva Sens** 06:02 Should I go to the next topic, then?
**Antoine Toulme** 06:05 do it.
**Arthur Silva Sens** 06:07 ….
**Pablo Baeyens** 06:09 Good here, Lee, … Should it do my topic, or have you already started?
**Antoine Toulme** 06:15 Gerard did the work of, kind of, laying… tying that up to your RFC.
So you… yeah.
**Pablo Baeyens** 06:21 Okay, yep. Thank you, Rashad.
**Arthur Silva Sens** 06:26 Alright, so my topic is I'm still looking At that problem where metrics… Metrics are changing their names without others realizing.
Thanks to Israel, we already have some sort of, end-to-end tests, and I think that's great.
But I wanted this to be broader, and we kind of built a platform for all the components that needs them, and not only the Hotel collector service metrics.
I brought this topic to Grafina Labs, and they shared with me that they already have something like this. It's called OATS.
This automation builds, … starts a whole storage stack.
That can store metrics, logs, traces, And we can query those… The telemetry back, and assert that they have a certain value.
… If this is in interest of the collector, we could build some automation like this. We can add in the CI, Something that spins up by storage for the telemetry data.
We build, like, we build some load testing that generates metrics, traces, logs.
And we assert those somehow.
**Antoine Toulme** 07:47 Yeah.
**Arthur Silva Sens** 07:48 Right.
**Dmitrii Anoshin** 07:49 How do you feel about it?
Within.
**Israel Blancas** 07:52 Wouldn't it make more sense to try to go into the path of using Weber? I don't remember exactly who, but somebody suggested doing that, right? What will be also aligned with also other things that we are doing, right, at the Open Thermity organization.
**Arthur Silva Sens** 08:12 Yeah, yeah, I… I think Weaver would be a… would be great, but my understanding is that Weaver is not ready yet.
But, I'm all in favor of using Weaver if it's… Weaver is ready.
**Dmitrii Anoshin** 08:28 We currently have a framework for end-to-end validation, and it's based on the… … thing called.
Golden, one of them, and another is, … I believe it's OTLP test or something. So, essentially, we just, … export to a GLP.
And then we validate the output based on that. So we validate OTLP output against expected.
definition in, like, this format, in this golden format, which is essentially YAML representation of OTLP data.
In that case, we don't need to have any backend to store that, because we only need it during the test run.
And it's… It's… it's been working.
But it… it doesn't have enough attention, and maybe we… it would be good to have some more… Like… People, like, helping with that? Because, for example, it's currently, it's complicated to have some… complex checks, like, whether… value should be in the range of something, or… typically, what we can do is just to ignore particular fields. We would say, hey, ignore the value, because it can change during the test, ignore this resort attribute, because it changes every time a collector is deployed, etc.
That's the only functionality, but if we can have more, that would be great. So, I would like to understand Like, what we gain by using that tool, what is not… What would be additional functionality that would improve test coverage that we currently have with the existing framework.
Because, like, just bringing something new doesn't mean that it'll improve our life, because it has to be maintained going forward. And given that we already have a solution, we either need to replace it, or maintain two, which is gonna be much more complicated.
**Arthur Silva Sens** 10:43 Yeah.
To be honest, I didn't know this automation already existed. That's probably why I suggested something new.
So I probably need to do some research on what is there.
**Dmitrii Anoshin** 10:58 Yeah, please take a look at the end-to-end test. We have end-to-end tests for Kubernetes components.
At least.
like, probably for attributes… attribute… Kubernetes Attributes Processor, or Kubernetes, … cluster receiver.
So, it essentially would spin up the receiver and a TLP exporter, and we will validate the output of our TLP exporter against what we expect.
And we also have integration tests for all of the receivers, which would scrape data from external services, like Regis, or Regis Metrics Receiver, or anything like that. So we will spin up Docker Regis image, Docker container, and we would validate against expected output.
**Arthur Silva Sens** 11:49 Yeah, like… Could somebody clarify why this is not running on PRs?
**Antoine Toulme** 11:57 It runs on PRs today. So, the way Golden works is, it runs on all the MySQL receiver, PostgreSQL receiver, all the scrapers, Redis receiver, all the integration tests use Golden today. They load up a YAML file and make all sorts of fuzzy assertions on whether the data matches.
And recently, we also made this, we compiled it so it would be available as a Docker image, and I, a week ago, I merged into the releases repository a check that runs for the contrib, release to check that it's actually exporting the metrics the way it should.
That this fails right now?
Which, you know, we need to look at.
**Dmitrii Anoshin** 12:38 Yeah, but the….
**Antoine Toulme** 12:38 ….
**Dmitrii Anoshin** 12:39 That image is not being used. We don't really need….
**Antoine Toulme** 12:42 Is it used? Yes, it is used in the releases repo.
**Dmitrii Anoshin** 12:46 And releases Reaper.
**Antoine Toulme** 12:47 Yes, because the problem is the contrib manifest is completely different from whatever we have in collector contribib, and we had a regression where the contribib manifest was pulling the wrong version of the Prometheus library, even though we tried not to.
So we had to add the replace statement in the country manifest in releases.
And now we have to check that it's actually taking.
**Dmitrii Anoshin** 13:10 I see, that's great.
**Antoine Toulme** 13:12 Yeah.
It would be great if the test passed, but that's… I need to go fix it.
**Arthur Silva Sens** 13:18 Yeah, what I… what I don't understand is why we had to build some, like, another automation, like, what Israel did in the….
**Sean Marciniak** 13:27 share that young chair in the chat here.
**Arthur Silva Sens** 13:29 We had to build a whole new automation to assert metric names.
**Antoine Toulme** 13:33 I don't know, what is that?
**Sean Marciniak** 13:36 So, Arthur, there's also the point that some, like, if someone's making a change to metric names into a receiver, they can update the integration test to reflect that changes as well.
So….
**Arthur Silva Sens** 13:46 Yeah.
**Sean Marciniak** 13:47 They could carry forward that they have Corrected the tests, but… From a user's perspective, that they are breaking changes.
**Antoine Toulme** 13:59 I would go and say that it's probably because Collector Core does not have access to collector contrib stuff by default.
So, it's difficult for them to get access to Golden.
**Arthur Silva Sens** 14:17 I see.
**Sean Marciniak** 14:19 Arthur, do you have a specific example of where this has broken for you?
**Arthur Silva Sens** 14:24 No, like, for me, specifically, it's not… nothing… everything is great. The problem is that… the problem is that people are complaining that metrics are changing from one version to the other.
Yeah. And, we are not catching that, because, like, usually those changes when we are doing a bump in some other library.
It's not something that is very obvious to us.
**Antoine Toulme** 14:47 Yes, agreed.
So, but the test should be at the point where you actually build the binary that is finally being, you know, consumed by customers, because in our case, as was shown.
the Prometheus library that was used.
underneath from the Go SDK that was being imported by contribib was a transitive dependency that you could not catch until the very end of your contrib build. So you have to almost… you have to check that on a snapshot of the build binary of your contribution to make sure that somehow you didn't sneak into it in the wrong version of the library.
Does that make sense?
**Arthur Silva Sens** 15:25 I understand that this is what we had to do right now.
**Antoine Toulme** 15:28 Yep.
**Arthur Silva Sens** 15:29 But I think we would… would be better to capture by actually running the collector And seeing what is being exposed.
**Antoine Toulme** 15:36 That's what we do in that test. So in that test, we run a Docker Compose, where we run the collector, we collect to its telemetry port, and make it exposed metrics, and those metrics get sent to the golden container that runs side-by-side to it.
and the golden containers and checks it against the YAML file, which is the expected outcome, and will actually tell you whether you match what you think you should be exporting or not.
Alright. It's….
**Arthur Silva Sens** 15:59 I'll take a look at this and see how we can get that to the collector core and contribute during PRs.
**Antoine Toulme** 16:05 Contributes in there. It's all there.
**Arthur Silva Sens** 16:07 Okay.
**Antoine Toulme** 16:08 Contrib. I think Core just didn't know, or doesn't have access to Golden, because it's in Contrib. So you can't have Core depend on Contrib that way. However, Core could, let's say, run… a, you know, CMD Golden, which is now a binary, which could be Go installed, and could run against a YAML file. But it's kind of crude compared to what you can do when you have access to the Go API, because the Go API of Golden allows you to do all sorts of fuzzy matching.
And you can manipulate the data so that you can check, like, if the value is in range or something like that, like… what Jimmy said, you can do things programmatically in that case.
if Golden makes it so that it becomes available and it's becoming more central, it could be considered to be moved to core. We've done that with other things, like mdataGen and other things, right? So, that's an option if there is interest for that.
**Arthur Silva Sens** 17:00 Yeah, Pablo suggested to move to the tools ripple.
**Antoine Toulme** 17:04 That works too.
**Arthur Silva Sens** 17:05 To me as well, yeah.
**Antoine Toulme** 17:06 Yeah, but, I mean… Yeah, I don't know, ….
**Sean Marciniak** 17:11 But… so… going to the opposite side of this, like, talking about discovery of deprecated and modified metrics. Should we be publishing those into the changelog as well, or making it part of, like, the releases as an additional file?
would that help with catching those name changes? Like, say, for example, like, I changed Docker to go to cgroups as a prefix instead of Docker.
Having that as part of the release artifacts, would that be helpful?
**Antoine Toulme** 17:41 Yes.
**Sean Marciniak** 17:41 Because what I'm going to do is, like, if it breaks my test, I'm just gonna go update the thing that says it's broken.
But I'm not fixing the problem of… I've changed a metric, but no one can discover what's changed unless they know where to look.
**Arthur Silva Sens** 17:55 If we end up with Weaver, Weaver also has this concept of telemetry evolution.
in one version, it looks like X, and the next version looks like Y, and people can just see how things are changing over time.
**Pablo Baeyens** 18:14 ….
**Dmitrii Anoshin** 18:15 But the….
**Pablo Baeyens** 18:16 Am I understanding… sorry, go ahead.
**Dmitrii Anoshin** 18:18 I just want to say, I like Sean's idea, at least we can start with that. We currently publish the changes, but it's manually written as changelog items, right? And it's pretty hard to find in the huge changelog.
But if we can have a separate artifact, let's say, like, separate, maybe, changelog document or wherever, with just the metric changes from everywhere, that would be a pretty nice feature.
**Arthur Silva Sens** 18:46 For this evolution, I would love to see the Weaver schema, like… Yeah. The artifact would be the schema of Weaver is the… how metrics are changing, yeah.
**Antoine Toulme** 18:56 So, yeah, Weaver has a validate function, and it's known to be able to get and validate metrics as it goes, and I think eventually it might be a replacement for Golden, if it's able to kind of do that.
I think also using Weaver, you could generate a golden file, because you have the ability, using the metric registry given by Weaver, to generate pretty much any YAML.
So, you could do that as an intermediate step at first, if you're not sure that Weaver's going to do the job.
It's, it's, it's really not too much work.
Okay, I'll put my foot, my mouth right there, but yeah, it should… it should work. … So… Anyway, options, options.
But if you want to start somewhere else, do you want to go fix that, thing I just pushed in releases, because it's been broken now, and I need to kind of get back into it and make sure it's working right? So if you want to go do a deep dive in Golden.
The open temperature collector releases repository right now, the YAML file does not match 1-1. What is being exported by Contrib, we need to check again.
**Arthur Silva Sens** 20:01 Alright, I'll take a look.
Appreciate that.
**Antoine Toulme** 20:04 Thank you.
**Pablo Baeyens** 20:10 maybe… I don't know if this suggestion is useful, but, some of the issues we had were related to some sort of bot from Ethfuse, … Is there any way we can help the Fuse people test our particular setup better?
Or are you already testing it, and it's a different problem?
**Arthur Silva Sens** 20:36 I'm not sure if I understood the question.
**Pablo Baeyens** 20:40 Right, ideally, these things would have been caught at the Prometheus library level, like the OTLP translator. They were not caught there. I wonder if there's some… help we can give to Prometheus people to test our particular setup on We're using some options that are unusual, some protector.
**Arthur Silva Sens** 21:05 Yeah, I… I think that what… We… we intentionally broke… the OTLP translator, because it's still not stable, and we… the problem was that We are trying to support a lot of people. And some people wanted one thing, and other people wanted another.
And I think we did a bad job at, like.
making everybody happy. We, like, we chose one particular group, and we made another group unhappy.
Yeah, we, we learned.
**Pablo Baeyens** 21:38 I mean….
**Arthur Silva Sens** 21:39 and Wilson, yeah.
**Pablo Baeyens** 21:41 I guess at least knowing what changes Prometheus is going to make would have been helpful here, and, like, if you have some sort of way of saying, like.
This will break this set of people, and tell that set of people, hey, you're going to be broken, that… Would that help us?
**Arthur Silva Sens** 21:58 Yeah.
**Pablo Baeyens** 21:59 Even if….
**Arthur Silva Sens** 22:00 Yeah, yeah, we're definitely not gonna break anything without prior doors anymore, like… We didn't know the adoption grew so fast, and then, like, all of a sudden, we have… 20 people complaining that we broke something, and we didn't know that people were using.
**Pablo Baeyens** 22:18 You're too popular, yeah.
**Arthur Silva Sens** 22:33 If you want to go to the next topic?
**Antoine Toulme** 22:36 Yeah.
**Raj Nishtala** 22:37 Alright, thank you. I think that's… I put in the next topic. Hey, everyone. So, … So, essentially, we got this request recently where, there were batched JSON logs being sent.
to the backend, and the customer wanted to see those bad JSON logs as… so there's… they're coming from CloudTrail, right? CloudTrail batches up these JSON events, distinct events together, and then sends it off to a backend, and they wanted to… So it's essentially a single log record with a slice of entries at that point. So they want to see that as individual events in, … In the back end, so to speak. So the closest thing I've seen currently to something that splits a log slice, a slice in the log record is an experimental processor called the unroll processor in one of the distributions.
And there was a suggestion that maybe this, this could be an OTTL function, that does something like this. Essentially, yeah, which is splitting up that slice into multiple log records. So I wanted to, I guess, propose this as a new OTTL function and see if, you know, there's… If I could find a sponsor for this, or… yeah, yeah.
If that makes sense.
So, yep.
I think that's all I had to say about that. So, again, to summarize, it's just a slice of CloudTrail events, imagine that being the source, and then passing it through the hotel pipeline. It passes through maybe a processor which splits it based on a delimiter, right?
And then you can see multiple distinct events on… in whatever backend, … That the customer is using.
So that's… that's… that's pretty much what the use case here is, yeah.
if… if there's no questions on it, or, I think, yeah.
we can probably move on to the next topic, but I just wanted to bubble this up to find a sponsor, potentially, yeah.
**Antoine Toulme** 25:02 You don't need a sponsor for a function in that case, right? It's not a whole new component.
So, I would hope that you're able to kind of, … get about this with the component discussion, the function discussion on the TCCL, which is complex. OTTL has a lot of moving pieces. If you look at the issues in the pull request for that, there's quite a few going on.
So… … Yeah, you're asking the right questions, you're in the right place, you're doing the right things.
If there's any….
**Tyler Helmuth** 25:34 It looks like there's a discussion in the issue as well that's… that's been good.
**Antoine Toulme** 25:38 This would be the most similar to the copy metric function.
**Tyler Helmuth** 25:41 I think that's the only function we have.
That produces telemetry.
as part of the transformation, like, it makes a new… the copy metric makes a new metric. This would be doing something similar. So we have precedence for OTTL to create Items in the batch.
**Raj Nishtala** 26:01 ….
**Tyler Helmuth** 26:02 But there are… there's, like, additional considerations when we do that, because it affects, like, how the loop of that particular transform context occurs. Like, when we make that metric, it ends up being included in the list of things that are being made, so it's kind of risky, so we just need to think through that.
**Raj Nishtala** 26:20 Yeah.
**Tyler Helmuth** 26:21 We typically would want to do this type of thing in Stanza. That's where we have done this type of log manipulation in the past, where it comes to, like, parsing and creating different log records. Stanza's already set up really, really well to do that, but it sounds like this data source, like many data sources for logs, isn't running through Stanza.
In which case, it probably would fall into the transform processor.
**Raj Nishtala** 26:47 Right, yeah, and then under the transform process, this would be specific to the transform processor, I guess, and only for the log signal at this point.
**Tyler Helmuth** 26:54 Yes, it sounds like there's… It must be only for the log signal. We do not have a way for, example, for a function to take a string from an attribute of a trace and produce logs. I do think the original creator of OTTL wanted that kind of cross-signal interactions, but we do not have support for that today, so yes, this function would need to be logs only.
**Raj Nishtala** 27:21 Yeah, and about the copy metric, which adds new metric… appends new metrics to the end, which… so essentially, you know, making it, you know, infinite, right? I don't think we have that risk here, because we just… Splitting it, … splitting, you know, you don't… you don't end up being recursively, doing that for, forever, right? That infinite.
bit that you were talking about with the copy metric. I guess that that part… that risk is probably not present in this use case, unless I'm missing something, yeah.
**Tyler Helmuth** 28:00 Okay. Yeah, we can continue to discuss in the issue.
**Raj Nishtala** 28:03 Okay, cool, alright.
Yeah, I think that's all I had, yeah.
Over to the next one.
**Antoine Toulme** 28:13 Alright, I want to talk about something that's, … in December of last year, I've opened an issue to deprecate OpenCensus Receiver and exporter, because… We are just hanging on to those bits, and would like to have a bit of a roadmap about it.
… there was some consensus at the time, it's like, okay, this is probably a good idea. I gave it 6 months, right? And we marked the components as duplicated at the time, we gave it 6 months.
The date came… Start to make noise about it again, and lo and behold, people are waking up and saying, actually, we need this.
So, the way they want this is, there are some folks who said, in May that they needed that, but eventually Knative moved away from OpenCensus and last release, so… That could be good. And there is a complex thing going on with a service, which is a cloud provider service called GCP NFOS Service Mesh that only supports OpenCensus.
… So… Apparently, there was a discussion with, specifically the vendors themselves. I also reached out to members of, of OpenTeometry, who I know work at Google, to just let them know. I don't want this to be a surprise.
… And I don't think that they've come back.
there's a message of two days ago, a comment that says, I find it massively variable if keeping the OpenCensus receiver was possible. So I think this is specifically for the receiver part.
… As of yesterday, we removed the OpenCensus receiver and exporter from the construe release, and all other releases that were using it by default.
… And looks like, you know, that's Alex Troll saying, well, that's not cool.
… Any feedback, folks? How do you want to do this?
**Tyler Helmuth** 30:15 Are the people that are asking for it to stay around?
Asking to be code owners?
**Antoine Toulme** 30:23 I think that's the right thing to say, right? It's like, no such thing as free lunch, if you want to stick around and you want to deploy, because right now, it's actually not owned by anyone, but anybody who is an approver of the collector.
I don't find that model of ownership to work. … Yeah.
**Tyler Helmuth** 30:42 And all the approvers of Collector are saying we'd like to get rid of it, so… at least that's what I'm hearing.
**Antoine Toulme** 30:48 Yeah, it's very clearly, I mean, I am not interested in that component. I do not want to push it. I think removing it from Contrib is also sending a very clear signal. It's like, this is not something you're getting for free anymore. If you want it, go build it in your distro. No one is stopping you from doing that. By the way, you can also just fork the repo and do stuff, right? It's fine.
Right. I… I would welcome any comments on this. I want to make sure this is not something that I push on people. We also have the whole month. I, you know, put myself up for the whole month of August to kind of come up with a plan.
And this is just starting to bubble up. I think we'll have a lot more feedback from folks when they realize that this version doesn't have OpenCensus anymore.
**Tyler Helmuth** 31:29 So….
**Antoine Toulme** 31:30 One thing we could do is give it, like, another 3 months, just to wait until, like, the… this has been a bit more digested by the community, but, you tell me.
Okay.
I'm gonna move on to my next thing, because I have to run to another meeting.
**Andrzej Stencel** 31:52 Sorry, Braden has his….
**Antoine Toulme** 31:54 I've got….
**Braydon Kains** 31:55 Oh, sorry. Sorry, it won't take long. Even though I'm a Googler, I can't give a good answer here. I don't actually know, but what was… can you remind me what the product was that they were talking about? Was it Anthos Mesh?
**Antoine Toulme** 32:05 Yeah, it's mentioned in the… in the bug itself, it says… the name, this guy called Alex Troll, who mentioned that.
… GCP infus something… Yeah, it's in the… it's in this call. It's been hidden.
**Arthur Silva Sens** 32:28 Excellent.
**Andrzej Stencel** 32:29 And a service manager.
**Braydon Kains** 32:31 Anthos Service Manage, so that… The people asking for this aren't?
Google… It looks like, so… I don't know, I'll figure it out. We've been trying to make sure nobody's using OpenCensus at Google either, so I don't know.
**Antoine Toulme** 32:47 I'm surprised to see this, actually. I reached out to David on your team, he knows. He mentioned that he was looking into it, but I think he's trained also not to volunteer time from folks who work on OpenTelemetry to support that, if possible, so that makes sense.
I mean, I get it, right? It's not… it's not easy.
**Braydon Kains** 33:06 Like, we don't want it either. I am actually surprised that there's… it's still a product that, like, was forcing the usage of it, so….
**Antoine Toulme** 33:14 I think in general, we need to have this type of healthy discussions on a regular basis, so that we stop having to support stuff that's just going to cram us into the past otherwise.
But there's a equilibrium to strike here, so, I mean, tell me.
**Tyler Helmuth** 33:28 You're following the procedure. We had it… it's been deprecated for over 6 months. Removing it from the public… the community release images is correct. If people are interested in this.
… There's options for them, which are the code still exists, the other version still exists, it can still be built into a custom collector.
If people want to volunteer to help maintain it, that's fine, but this community is saying right now, we are not interested in maintaining this as a community component anymore, and we have followed our procedures, so I don't think there's anything else for us to do at this moment.
**Antoine Toulme** 34:06 Yeah, and by the way, the reason I'm also bringing this up is that this particular component is also failing our tests on a regular basis.
**Tyler Helmuth** 34:13 Right, it's causing us pain.
**Antoine Toulme** 34:15 I don't like it, right? And I don't know how to fix it, nor do I have the time or the interest to go fix type of test, this is not fun, I don't… I don't think it's… it's dragging us down, and… If someone wants to be a code owner for this, then, oh, my… this is fixed by my standard, right? Because then they're responsible for fixing the test.
We're good.
Yep.
Alright, I'm really going over my time here, I have to run, but I wanted to mention one more thing. I have a small issue for an improvement. It's more like a triage thing. I would like people to, when they open their first pull request on the contribository, to get a little welcome message.
a little link to the contributing MD document, if they have any questions, this way they can kind of see a little bit what's what. But also, put a label on the PR that says this is a first-time user, because their CI will not run until we go and kick it manually. And every time they push, we'll have to go back and kick it.
And, I find that there's a lot of these type of PRs that just, like, languish over time otherwise, because we don't know to watch for them, and so you don't know until you click on the PRs, like, oh, you're just waiting on someone to go click a button.
it's aggravating, right? It's bad, but also, like, … It's… it's kind of a problem with, like, the way things run. So, would that make sense for everybody?
This can be a first-time, like, issue for someone. Like, this is… This is nice.
It's just nice to have.
**Arthur Silva Sens** 35:48 Sounds good to me.
**Andrzej Stencel** 35:50 I mean, the tests, the CI doesn't kick off, not only for first-time contributors, but for anyone outside of OpenTelemetry.org, is that right?
**Antoine Toulme** 35:59 No, so there are multiple states. There's none, contributor, member, and maintainer. If you're none, that's your first time. By default, security-wise, we don't want people to run crypto mining on our stuff. We don't let them to… the CI does not kick, right, at all. If they have contributed at least one PR, they're considered reputable, and then on the PR, it will run the CI moving forward.
**Andrzej Stencel** 36:21 Oh, okay.
**Antoine Toulme** 36:21 That's when they get a contributor, yeah.
Okay.
Yeah, Evan, go ahead, and I'll drop now, but I have a topic down below, you can just take a look at it. Have a good one.
**Evan Bradley** 36:37 You can feel free to talk about it beforehand if you want, but, if you're good, then I can.
**Antoine Toulme** 36:42 Very simple. I have started to be on a rampage, just want people to just move their component to better. If your stuff is in there, can you move your component to Beta, or tell us… tell me why.
Or tell anybody why you don't want to move it to Beta, so we can work to move it to Beta.
Like, literally no reason. If your stuff has been in alpha for over a year, why is it not moving to beta? Just a simple question, right?
Yes, you need at least one PRB for crypto mining.
Boys.
Alright, good to see you.
**Evan Bradley** 37:22 Alright, thanks. Okay, I'm up next. I've been, digging around in configGRPC, and I found a… like, a deprecated method call that I was a little surprised by, so I dug into it, and it looks like there was an issue with proxies that required us to… stay on the deprecated method. … I've linked the PR here. Unfortunately, there weren't any regression tests added, but from what I understand, we should be good to use the… the non-deprecated function now, but I don't feel confident that if I update it to use that, that we won't hit this issue again. I was just wondering… it's a bit of a shot in the dark, but I was wondering if anybody has any more, information on this. Yang, I saw that you were involved in the PR, but… If you or anybody else knows anything, I wouldn't mind, trying to switch to the undeprecated method before we go to, Stable for this component, but… you know, if not, then it doesn't happen.
**Andrzej Stencel** 38:31 Which is the duplicated? The gRPC dial context is duplicated?
**Evan Bradley** 38:35 Right, dial contacts in favor of new client.
**Andrzej Stencel** 38:39 But there's an issue with new clients, so we need to….
**Evan Bradley** 38:43 There was an issue with new client. My understanding is that they fixed that upstream now.
**Andrzej Stencel** 38:47 Okay, okay.
**Evan Bradley** 38:49 So, I think it's been fixed since February or so? I didn't dig into it. Again, I was mostly concerned about just making sure that I could easily validate the, … Validate that it's been fixed.
I mean, worst case, I just have to dig into it and see if I can replicate the problem and go from there, but, … Or create an issue and have somebody else do it, but I just wanted to check and see if anybody else had any more before I, started down that path.
**Andrzej Stencel** 39:26 Maybe ideally, we can find… the creator of that original PR, Alex Katz, and asked him to create the revert. He says he, verified this manual, apparently, right? Right.
**Evan Bradley** 39:39 Yeah.
Okay, if not, I will hand it off to the next person.
**Heitor (Huawei)** 40:00 Hello, I think that's me. My name is Eiter. First time here, so nice to meet you, everyone.
And then, I have a kind of simple request. It's just, like, I work for Huawei. We're, building, different, components to integrate with Huawei Cloud.
The next one is LTS, logs receiver, and then I would like, to find a sponsor for it.
**Dmitrii Anoshin** 40:50 Hi, Heather, … What's the model for pulling the logs? Is it… Like, gonna be watch… watching logs from the cloud, or…?
Like, some on-pool-based model?
**Heitor (Huawei)** 41:06 Yeah, for this one, it will be pool-based.
… no.
**Dmitrii Anoshin** 41:12 Any… any work… do you represent that cloud? Do you work with that? Yeah, yeah.
Is there any work done to support the TLP in any way? Have you considered that?
**Heitor (Huawei)** 41:28 We… so the… the services, CES, which is metrics, and LTS, are working on it internally. We have been… I have been talking to, like, the service owners, and they… they plan to release, at least to start.
With CS. I'm not sure about the full roadmap, but then, meanwhile, the idea is to use, like, the current APIs, and then enable, like, these different components.
For, like, metrics, logs, and traces.
The metrics one is already there, and then, now we build the LTS, which is logs, and then next will be traces.
**Dmitrii Anoshin** 42:22 So I'm asking, that… is that work, like, to produce metrics and traces in a TLP format so we don't have a receiver, right? So we don't need to have a receiver.
Because if you produce matrices and metrics in OTLP format, you can just send it to OTLP receiver instead of having Introducing your own receiver.
**Heitor (Huawei)** 42:45 Yeah, but, yeah, the issue is that, we don't have, like, a clear roadmap, for that, until now.
And, like, the services themselves are pushing us, like, to, develop, like, these, custom receivers.
**Dmitrii Anoshin** 43:04 So you're saying it's gonna be a temporary solution?
**Heitor (Huawei)** 43:07 he… I'm not sure, that that's, what I'm saying, because, even with the OTLP, There might be, like, Still need for, like, this component.
**Dmitrii Anoshin** 43:25 It would be good to have clear reasoning for having to have a separate receiver, if you can.
**Heitor (Huawei)** 43:33 Oh, cow.
**Dmitrii Anoshin** 43:33 Figure it out and put it in the issue, to get some more clarity and potential sponsors.
And, … It's hard to get sponsors… sponsored with that, with all, like… Lack of, … Details like that.
And also… You would need to be engaged in… OpenTelemetry collector in general, if you want to have it in this… like, maintained by the community, you would need to be the co-donor, and potentially maybe some of your co-workers would need to contribute.
**Heitor (Huawei)** 44:15 I'm already a member, and then… yeah.
And the idea is that me and some other folks on my team would, maintain and own this component.
**Dmitrii Anoshin** 44:29 Okay. I'm just saying that we used to have, like.
required rotation of the sponsors for cloud, … for vendor-specific companies, but now we don't have that anymore, and now it's volunteer-based, and it's gonna be hard to find the volunteer.
for a… like… For a product, that… if no one else is working with that product, right?
You will….
**Heitor (Huawei)** 44:57 Oh, God.
**Dmitrii Anoshin** 44:58 And you… so you would find a volunteer.
From approvers, only if that approver have some, like, interest in that cloud, whether it's an employee, or whether it's a user, etc. But if not, it's gonna be hard to find that.
So there are some several ways. You can have… you can become an approver, or you… you're, … Your co-worker can become an approver in that way. But it's… again, it's pretty hard.
**Heitor (Huawei)** 45:29 And also… Yeah.
**Dmitrii Anoshin** 45:31 there are other options. You can always build your own distribution of the collector and keep this company.
Somewhere outside on… in your repository, for example.
**Heitor (Huawei)** 45:42 Yeah.
That's… that's good feedback. I'll… I'll, talk internally, and, figure out, the way, then.
Thank you.
**Andrzej Stencel** 45:56 I have one more question. If I understand correctly, this log tank service, this is a logs backend, where people send their logs into, right?
**Heitor (Huawei)** 46:06 Yeah, the idea is that, if people are… wanting to integrate, like, the logs from Huawei Cloud to other services, like Datadog or, like, other log services, they could use this receiver to pull the data to other places. That's the idea. The metrics is the same case.
**Andrzej Stencel** 46:32 Okay. If you can add that use case, like, describe that use case in the issue, that would help as well. Thanks, of course.
Okay.
**Heitor (Huawei)** 46:40 Yeah, thank you.
**Paulo Janotti** 46:47 Okay, I'm next there. Just a quick announcement that I'm working on building, the Windows arm. We do have some users on Windows clients, and we expect eventually for them to get on… on Windows Arm, so we are anticipating that and starting that. So, if you want, anyone is interested in me in Slack or something, but I should be trying to… right now, it seems everything is going smooth, is… is my PRs to… enable and build this stuff, before I go through the releases, … repository. I do expect a bit more of concurrence issues in tests, because Windows exposes a bunch of Not… problems on the tests themselves. I think, Young was very close to me when I was fixing a bunch of those. But with ARM, I do expect more of them. The combination of Windows and ARM should dispose more concurrency issues, but I'll be in work on that. Anyone that's interested, ping me via Slack, and we can collaborate or sync on that.
**Tyler Helmuth** 48:07 This is exciting, but I'm a little worried about, the releases repo getting, like, supporting this new feature. It's… it seems like the last couple… Months? Maybe, like, the last two releases, maybe the last three releases.
have been really rough in the release of the repo for getting everything to get outright. I'm a little worried about adding another architecture.
While we're… while the releases repo feels like it's in a… A rough state at the moment, … I guess I've not… I've not been super close to the releases recently, other than the operator release. Does that sentiment feel right to the other maintainers?
**Andrzej Stencel** 48:56 Doesn't look like we have actual releases maintainers here on the call.
**Tyler Helmuth** 49:05 Okay, well, I guess, when we go to put it into the releases repo.
would want to do a lot of testing. I feel like… I know it's hard to test in a releases repo, it requires, like, forks and special keys and, like, changing destinations to not be the hotel destination or something, but, yeah, we'll need a lot. I just want to make sure we have a lot of testing, because our releases right now have been kind of rough.
**Paulo Janotti** 49:37 Thanks for the heads up.
**Tyler Helmuth** 49:39 Yep.
I can't believe that's our last topic. There's a topic on the… In the Sign Notes for another, processor.
If you're interested in sponsoring another processor, take a look at that issue.
Thanks, everyone.

SIG: Arrow SIG
Date: 2026-10-06
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

**Pierre Mariani** 00:40 Hello, Drew.
**Drew Relmas** 00:43 Hey, Pierre.
Good afternoon.
**Pierre Mariani** 00:47 Good afternoon.
**Laurent Quérel** 01:11 Hi, guys.
**Drew Relmas** 01:13 Hey, Laurent.
**Pierre Mariani** 01:14 Hello.
**Laurent Quérel** 01:16 Hello?
**Albert Lockett** 01:46 Yes.
**Laurent Quérel** 01:48 Hello?
**Drew Relmas** 01:48 Hey.
**Pierre Mariani** 01:51 Hello.
**Laurent Quérel** 02:13 Drew, do you… Do you drive the session today, or you…
**Drew Relmas** 02:17 start.
**Laurent Quérel** 02:18 boots.
**Drew Relmas** 02:19 I can do that.
**Laurent Quérel** 02:20 Okay, great.
**Drew Relmas** 02:24 Let me share… Screen… All right, can you go ahead and see that?
**Pierre Mariani** 02:38 Yes.
**Laurent Quérel** 02:39 Yes.
**Drew Relmas** 02:40 Great.
So feel free, as we always do, to fill in your names.
We have some issues that needs discussion.
There's a few that are stale, but again, I don't think we want to spend too much time on stale in this meeting.
And… Then there's a whole bunch of deciding… We should probably look at… Oh, it actually looks like we don't have much.
These aren't sorted by time. Anyway.
Why don't we go ahead with needs discussion?
Let's see, we have… start at the bottom.
**Joshua MacDonald (Microsoft)** 03:32 I went through and accepted most of the issues because they looked acceptable, and I… I'm the one who set these needs discussion labels within the last half hour.
Yeah, the bottom one there, Linux and Windows perf testing, I agree with that. I don't know what to discuss about it, other than it's probably hard.
to do.
**Drew Relmas** 03:58 I mean, yeah, this would be an escalation to Trask, probably in the community repo or something like that.
**Joshua MacDonald (Microsoft)** 04:05 That was… that's at least one way to do it.
**Drew Relmas** 04:07 way to do it.
Oh, Trask already replied. Yeah, open a community issue. Okay. So, I don't know if we need to discuss this.
**Joshua MacDonald (Microsoft)** 04:17 Great.
**Drew Relmas** 04:18 Great.
**Joshua MacDonald (Microsoft)** 04:22 Since you're presenting, I'll let you continue.
**Drew Relmas** 04:24 Let you continue.
Okay, feel free to, Stop me at any time.
**Laurent Quérel** 04:31 Joshua, we have just, just to let you know, we have echo when you are talking… when we are speaking.
Oh, WTV wasn't.
**Drew Relmas** 04:43 All right, moving right along, we have an issue from Chanley, I think, here, about pipeline permissions. So this… I only took a very brief look at it before we started, but…
**Laurent Quérel** 04:57 Yeah.
**Drew Relmas** 04:58 Laura, you want to speak to it?
**Laurent Quérel** 05:00 Yeah, just, because… just to let you know that I, already entered into one of the… Topic that we can discuss today, this specific issue.
**Drew Relmas** 05:11 Okay, got it.
**Laurent Quérel** 05:11 I think you can just keep it, and hopefully Chanley will be there.
To talk about it, otherwise I will, I will present it.
**Drew Relmas** 05:21 Okay.
We have a bunch of additional work from the OTLP exporter summary recovery that you implemented.
**Laurent Quérel** 05:33 Yeah.
**Drew Relmas** 05:35 Do you, Josh.
**Laurent Quérel** 05:36 Talk about that, yes, so the… that's basically, so the… as a reminder, we, or I introduced into the OTLP exporter.
The ability to create, basically, a summarized diagnostic when we enter into a situation where the OTLP exporter is not able to reach Or to send data to a backend.
Instead of generating warnings for every incoming Pdata message. The idea is to.
To have a state machine that will give us a way to.
Dramatically reduce the number of, warnings, and just having the beginning of this scenario, issue, not being able to reach, for example, the back end, then every one minute.
A summary of the situation.
And then, once the scenario ends, so we are again able to reach the… the backend, then there is a, like, a closure event, or an exit event. So… It's only currently applied to the OTLP exporter, and this entire set of.
GitHub issue are related to the fact that we could, and we should, in my opinion, extend that to all the exporters, and progressively also to multiple other components in the system.
That… could be applied to some processors, to some receiver. So that's about that, and I also, if I remember well, also integrated Or maybe, Joshua integrated some, possible refinement that he had in mind regarding the… this specific, proposal.
So, that's… that is represented by this, GitHub issue umbrella.
**Joshua MacDonald (Microsoft)** 07:34 Yeah, so I became interested in this and have proposed.
well, in my opinion, it would be nice if we could turn this into kind of a normal-looking logging apparatus, and I have drafted it in a PR, which is too big. I've now drafted a proposal for a log sampler.
Which I included under this umbrella as well. My goal is that we, make what you've done look like really close to ordinary logging, with configurable suppression policies.
Where the suppression policy will be exactly the same as the policy that you wrote, but you'll see a plain old log statement, basically speak at the call site. And this will, I think, make things a little bit more coherent.
a little bit faster, and a little bit less code. It's not that much of a big deal, though, to me. So that's what I've been working on, and I don't think we need to debate it anymore, unless anyone wants to.
**Laurent Quérel** 08:33 The only thing, when you say faster, I mean, I will be happy to see that. For me, that's… I totally, like the other one that you mentioned, I just want to see if it will be faster.
If that's okay, that will be, excellent.
**Joshua MacDonald (Microsoft)** 08:50 The… the starting point I had was that, more or less, that the existing logging apparatus, what we call the ITS logging, it's using the Tokyo Tracing Library.
has all.
at least my premise is that we have a lot of optimization in there to avoid allocations, or to get exactly one allocation, or to encode a buffer only once, and then not copy it again. And I think we can benefit from all of that. I was… at first, what I found in 4151 confused me at first, and then I unpacked it a little bit, and I found that there are really two policies in play there. There's the one for The notifications and the preparation errors, which are kind of, like.
I don't have the best wording yet, but those are plain suppression, and then there was the episode compression, or suppression, which was based on the success and failure, so you have a result in the second case. Yep.
And, I… That… that was a little bit… I didn't quite see that at first.
And again, I think this can be a plain old logging interface.
What I was envisioning would allow the… existing Tokyo tracing support, which is how we turn off logging statements, or how we set a compile time level, I was thinking that that stuff should take effect first. So that you would say, is this logging site enabled?
Okay, are we… now, would you like to see my result? Are we in an episode or not? So if you turn off the logging site, you should turn off all the episode calculation.
And if you turn off the logging site, you should turn off all the suppression, I guess, is what I'm saying. The logic.
and I am glad to… try and show you this in a PR, and I will pay attention to performance, as you noted. I think that's what we should do, is look at the performance.
**Drew Relmas** 10:57 Yeah, my only comment on this is, Laurent, I had left it on the first PR, which was, I'd love to make To Josh's point about code duplication reduction, I want to make this as easy to adopt for.
**Laurent Quérel** 11:10 Yeah.
**Drew Relmas** 11:11 As little boilerplate in each integration as possible.
**Laurent Quérel** 11:14 That's the topic of the 4232, simplify and unify bonded agnostic integration. Yeah.
I totally agree with that, and I just postponed this effort in a future PR just because I want to see an integration with additional Exporter to make the right decision in terms of simplification. And generalization.
Yeah, I think, I think we will figure out the… The right way to simplify and to keep performance, and to ideally reuse the… Like you said.
to make that as close as a logging approach, the initial version that we had, but still getting the benefits of having something that is not flooding ITS with Individual messages that we have to re-aggregate. I want to avoid that at any cost.
**Joshua MacDonald (Microsoft)** 12:09 I think we… I think we can do that, and I think I can satisfy you, at least on… on that.
Point. Yep.
So, I think we should move on, basically. This isn't too much to disagree about.
**Drew Relmas** 12:24 I see we have an issue here about component inventory baseline. I think this is from Camila.
who I don't believe is in the call right now, but I think she mentioned it to me offline. Should the component inventory, check be required in the CI? It seems we've had a few new components added without Adding to the inventory, and then… Cargo XTask check locally is failing, so do we want to bring this into parity with CI?
I don't think I have a problem with that. Josh, you added needs discussion.
**Joshua MacDonald (Microsoft)** 13:02 Oh yeah, I just I figured we should discuss it, but I don't have a problem either.
**Laurent Quérel** 13:06 Yeah, me too. I don't have any problem with that because it's.
**Drew Relmas** 13:09 Okay.
**Laurent Quérel** 13:10 We are using the component inventory already for our own TMA process internally, so that will really surprise.
Anyway, if we enable that into the CA pipeline.
**Drew Relmas** 13:24 Oh, we said we're talking about this one as a topic. Josh, last one for you.
**Joshua MacDonald (Microsoft)** 13:31 I…
**Drew Relmas** 13:31 Is this what we were just talking about?
**Joshua MacDonald (Microsoft)** 13:33 This is related. When I was starting to work on this log sampler that you see, it's a pretty small PR, what I discovered was I didn't follow how this, OTEL component scope macro was added a few months ago. So, to bring everyone up to speed, this macro If you declare it at the top of your file.
It means that you are going to get.
different versions of the macros that know the name of your module that you then can control. So instead of taking the package name from cargo.
Based on the root crate.
You instead get to choose your module name, your target name.
And what I discovered is that there's still a bunch of old code that doesn't do it that way, and we never made a decision on whether to consolidate or unify, and I couldn't find another issue that says either way whether we should or shouldn't. And I think we should. For example, in my PR, the… this little ITS logging sampler that I added.
to make some of that stuff we discussed easier.
if I don't have… consistency, I have to generate macros in two places, which makes twice as much macro, and I don't want more macros, I want fewer macros. So, if we force people to use the OTEL component scope, then I can simplify my macros, and I would like that.
**Drew Relmas** 14:51 Okay, sounds good. Look forward to reviewing that.
**Joshua MacDonald (Microsoft)** 14:57 It implies pinning down a component name in a bunch of places, but it shouldn't be very hard to do.
updated.
**Drew Relmas** 15:04 issue.
**Joshua MacDonald (Microsoft)** 15:04 instructions.
**Drew Relmas** 15:06 Got it.
That takes care of needs discussion. If we don't really want to go through stales at the moment, let me look at the agenda. We have… at least 3 items there. Is there anything on here that we do want to cover?
I don't think anything here is super important.
Based on my quick read.
**Laurent Quérel** 15:41 For me, the… if we are reviewing sale, and I'm not saying that we should do that now, but what we should avoid is to see What we see there, close automatically by the process, without us reviewing it.
So, if we don't do it today, that's okay, but we should do it next week. I don't remember exactly the grace period we have for that, but I don't think it's multiple months.
**Drew Relmas** 16:13 Okay, and to some degree, we can also do it.
Asynchronously, not on the… on the meeting. As long as we, as you say, remember to do it.
**Joshua MacDonald (Microsoft)** 16:23 time at the end of this meeting as well.
**Drew Relmas** 16:25 Sure, I'll keep that in mind. It doesn't look like we have… Any new, triage decidings.
Oh, sorted the… Nope.
I'm not unsure… oh, it's sorted.
**Joshua MacDonald (Microsoft)** 16:49 Decisions we haven't made yet.
**Drew Relmas** 16:52 Okay.
Perhaps we just move on to our topics.
If everyone's good with that.
Oh, look at that, it's me for the first two. Okay, so my first topic of the day is a PR out I have for release automation. This… It might be of less interest to a lot of our non-maintainer contributors, but I still think it's worth talking about.
Today, you know, as Hotel Arrow started, we have some Go.
We have some Go code in our repo still, a Go module that's consumed by an Arrow receiver and exporter pair in the Go collector contrib repo. So we are still, you know, we still own this code, and we're… we have Renovate dependency upgrades to it, and we have to release it. However, up until now.
Since we started releasing Rust crates, we've been coupling those versions and the releases together. This has led to a few releases where we wanted to release Rust because we're iterating fast on it, but we pushed a new Go mod version without any actual change in it.
So, that felt bad to me, and in addition, I would like to reduce some of the manual toil that I do when we… when it is time to release. So, I'm proposing a weekly cadence for the moment, because of the amount of activity we have, and the interested parties at Microsoft and F5 who want to be consuming these changes quickly.
The Go collector and collector contrib, as I'm sure we're all aware, has, every other week releases. But I don't think there's a huge risk in us doing weekly, especially when we're at the pre-1.0 cadence. So… I would request people, if you have an opinion, to leave a comment here, but I don't know how much we have to actually discuss. I'm just trying to create the awareness.
okay… That was easy.
**Laurent Quérel** 19:05 So, just to make sure, because I remember we had a discussion, it was on Slack.
And I didn't see it there.
We will still be able, as a maintainer, to… to…
**Drew Relmas** 19:19 Oh, yes.
**Laurent Quérel** 19:21 Okay.
**Drew Relmas** 19:21 Yep.
**Laurent Quérel** 19:22 Oh, okay.
**Drew Relmas** 19:23 So basically, to elaborate for everyone, the way it works today is a maintainer runs a prepare-release job, which creates a PR that bumps the versions.
and, like, accumulates the changelog together. And then once that merges, the maintainer again runs a push release job, which is what actually publishes the GoMod tag, the crates, and the GitHub release object.
What I'm proposing we change to is, essentially, that prepare release PR will just go automatically every Monday morning, so then we approve it, merge it, and also, once that PR merges, the push-release flow will automatically start.
It still requires the protected maintainer approval, so we're not… Doing it. We're not skipping that, but just… it simplifies a couple of things, a little fewer button clicks for us.
**Laurent Quérel** 20:24 Let's.
**Drew Relmas** 20:25 So, yep, that's… that was my first topic.
**Joshua MacDonald (Microsoft)** 20:27 So the net result is we really go less often.
**Drew Relmas** 20:32 What was that, Josh?
**Joshua MacDonald (Microsoft)** 20:33 It sounds like the net result is that we will release Go less often.
**Drew Relmas** 20:38 Yes, that is correct.
**Joshua MacDonald (Microsoft)** 20:39 That's great.
**Drew Relmas** 20:39 Only when there's Dependabot or Renovate, fixes, mainly.
There's very rarely any active development on there, unless we're doing some core changes to the OTAP contract.
**Joshua MacDonald (Microsoft)** 20:54 Sounds good.
**Utkarsh** 20:55 So, does this also take care of the, you know, merge queue?
Being empty for the prepare release job to run.
**Drew Relmas** 21:04 It… That is a great point, Utkarsh. I need to account for that. Thank you for bringing that up.
**Laurent Quérel** 21:13 That remind me some issues today, Inkas.
**Utkarsh** 21:17 Yeah, yeah, that's why I'm… I still have to do the push-release job, but yeah, I… that's when I really.
**Drew Relmas** 21:23 Push release, luckily, is completely uncoupled from the merge queue, so…
**Utkarsh** 21:28 But my, one of my, one of the prepared release, runs that I.
**Drew Relmas** 21:31 Failed because something else was in the process of merging. Yeah, that's mainly to protect and make sure the changelog is accurate. We can revisit that if we think it's overkill, but it's the semantically correct thing to do.
**Utkarsh** 21:45 Sounds good.
**Drew Relmas** 21:47 One thing, I chose Monday morning, like, first thing, because odds are, probably not a lot is in the merge queue at that time, so it might be safe.
**Joshua MacDonald (Microsoft)** 22:00 For your all… just for the room, the Go collector has a much more elaborate release procedure because of its contrib repository, so you have to lockstep the release of one and then check the other, and it's very complicated, and it also stalls PR merges, like, once every two weeks.
For the same reason. So, it can only get worse from here.
**Drew Relmas** 22:21 you Well, we'll get better before we get worse.
Yeah.
Okay, the second topic I wanted to raise was something that just popped up a few minutes before SIG, but I thought it would be good to chat. I'm unsure, do we have Ben in the call? We do not. So… As we're all aware, Ben and some folks from Microsoft are working on poll-based receivers. Specifically, they're focusing on Oracle as the first integration.
So Ben had raised this PR. Josh, I haven't talked about this with you yet. I saw you approved it. But Ben was adding a sort of extended integration test for this specific receiver.
And while I'm okay with that in principle, as we add more and more… kind of contrib style nodes, we need a scalable way to allow them to declare extended tests. Josh, perhaps you have a good suggestion for this for how collector contrib works in terms of workflows.
But… Up until now, I know we have existing kind of ad hoc tests for user events, ETW, and host metrics, and those are in the core Rust CI.
workflow, which is just getting bigger and bigger and bigger. And as more core contrib components add their own dependencies and setup steps, it's gonna get way too big to actually maintain. So… Instead of adding a new workflow for a specific receiver integration test, I think we should… I mean, for the moment, we can stick it in REST CI next to all the others, but I would like us to think about a more maintainable approach.
Gaurav, you have your hand up.
**Laurent Quérel** 24:10 Yeah. But remind me what we are doing for the Kafka, exporter receiver test.
Because we have to integrate, so we… we move from… we… we follow different direction there. At some point, we used test containers.
approach.
I don't know if those test containers support Oracle or whatever database we want to… To test here, but that could be an approach.
So basically, you are still writing a unit test.
But this unit test basically defines the entire configuration that you want to… to deploy.
And the system takes care of killing the process if something bad happens, and so on.
The other approach is the one that we use, at least for some of the integration tests with Kafka. We are using some kind of simulator for Kafka.
Which is lightweight.
Not necessarily reproducing exactly all the… the behavior of Kafka, but, good enough for some, some, some integration tests.
So I think we are in the same kind of areas there, and I suggest to look at these containers, maybe.
**Drew Relmas** 25:30 Yeah, that's a fair idea. I can, if you think to leave a comment on here, explaining what you're doing with, Kafka, that'd be helpful.
**Laurent Quérel** 25:40 Okay.
**Joshua MacDonald (Microsoft)** 25:43 Sounds like that would only work if we can find Oracle or an Oracle simulator in a container.
**Drew Relmas** 25:53 Yeah.
**Laurent Quérel** 25:54 Taylor is running the real thing, so it's two separate approach.
The simulator could be outside of a container.
Or could be inside a container, and the test container is really taking the… The existing product or the existing system, and putting that into a container, and you have some kind of orchestration solution to integrate that into a unit test.
**Joshua MacDonald (Microsoft)** 26:25 Got it. I'm not familiar with how Oracle is tested in the world, but I think we can ask Ben to follow up.
**Andres Borja** 26:32 What about licenses for those things?
**Joshua MacDonald (Microsoft)** 26:36 That's kind of what I'm wondering.
**Laurent Quérel** 26:37 I think it's a good idea.
Indeed. Yeah.
**Drew Relmas** 26:43 I think there's this, I mean, from the PR, this installs some version of Oracle Free.
**Laurent Quérel** 26:50 Hmm.
**Drew Relmas** 26:50 Which I assume might have different license, allowances, but…
**Joshua MacDonald (Microsoft)** 26:57 So to me, the phrase Oracle 3 sounds better than that.
Nevermind.
My system is Oracle free. So there.
**Drew Relmas** 27:04 Ha ha ha!
Oh.
Okay, well, that was it for this topic.
And with that, I think Chanley and or Laurent, if we want to go over to the pipeline permission topic.
**Laurent Quérel** 27:20 Yeah, I will actually present the issue, and I will follow up if necessary.
**Chanly** 27:26 No, I think we could keep it here, yeah.
So this is basically.
idea I had to basically restrict certain pipeline nodes that people might want to use in various pipelines. So this is coming from for a Somebody had an idea for the Kafka receiver.
Regarding the DLQ feature, where instead of having the… Entire DLQ thing all wrapped inside the Kafka receiver against said expose.
a DOQ output, and then basically we just send all the… bad messages down to that using the codec that Laurent worked on.
And then users can just basically.
pipe that to whatever exporters like they could use the Kafka exporter like file log exporter.
But the problem with that would be, basically we would need a way to, like, restrict access to the codec, since they are bad messages, so, like, so users can't, like, access, but, like, I don't know, like, a transform note, transform processor in that.
Pipeline.
And try to access those messages.
So this is why… Thought of.
**Drew Relmas** 28:38 Oh, okay, so you're saying, like.
Because, you know, going to a dead letter, we want to maintain the original Payload.
We should be able to specify that, hey, once something reaches this point in execution.
We're not actually allowed to change it further.
**Chanly** 29:00 Well.
Considering it's, like, it could also be, like, invalid messages, so, like, it can't be… let's say it got, like, a decode error, so we can't properly represent it in, like, OTAP or TLP as well.
So it'd be wrong to have, I don't know, like, a transform process try to manipulate that data when it can't really do anything with it.
**Laurent Quérel** 29:23 I think there are… Multiple use cases for this capability.
The one that, Chani just expressed.
like he said, it's related to the fact that when we started to integrate DAQ into the Kafka receiver, we started, in fact, to integrate a lot of the Kafka exporter inside the Kafka receiver, and that didn't… look very good to do that. So we look together at how can we decouple Really, the… where we want to send this message… messages that are invalid.
For whatever reason, we are not able to pass them, they are not following the… the, the OTAP, specification, or the OTLP specification, or whatever is the problem.
So how can we express an output for any node into the pipeline system that come with some, signature? And in this case, the signature is, okay, we emit a message.
There is the PDATA abstraction around it, but the message can't be read.
I mean, it can be read, but it can't be processed.
So, and the idea is, how can we have a prepare… the pipeline preparation phase, looking at the signature of the sport?
And making sure that whatever we connect to this DLQ port for this Kafka receiver is compatible with the specification of this port.
So, okay, you can only read, but you can't Decode or process?
Okay, that should be expressed, and that's the permission system that Chanley started to specify here. Maybe we will have to review the wording and the… but basically, the essence of this thing is, how can we express Contract between an output port.
And… and seeing that we want to connect to this output port. And that, at the… compilation phase. Not the compilation phase, but the pipeline build phase.
Another, example of usage for that will be If we… if we.
Enable some high-level policies saying, oh, this branch of the pipeline Should never, after this point, should not be, updated.
You can read it, you can root it.
But you can't update it. So if we want to apply some permission, and making sure that based on declaration of what the… The individual nodes that are downstream to this point.
Exposed. We should be able… To verify during the pipeline creation or construction that there is no component that will update this key data message.
But I think it's a very powerful approach.
We… in my opinion, we need to create an LFC, and go much deeper into the specification of this system. There are some, in my opinion, some elements in this first proposal that are overstating what we can really do, because there… it's not like, we… we create a sandbox, a room PDATA, And we prevent any kind of modification. It's more declared-based.
So when we create the pipeline, we can check the contract, but we can't effectively enforce, the fact that Let's see, a processor declaring that it's not doing anything on PDATA, but in fact doing it.
On purpose, we will not be able to stop that, but we will be able to stop misconfiguration of pipeline based on those contracts.
**Drew Relmas** 33:34 Yeah, I was gonna say one thing, but I think you maybe addressed it in your last few sentences, but I'm just trying to wrap my head around… the different personas involved here. Like, if I'm an operator that is setting up this collector.
you would assume it's on me to do it properly. Like, there's an aspect of… dataflow engine configuration that I expect wouldn't necessarily be exposed to an end customer. Like, a lot of… a lot of this config might be generated based on another artifact or some other thing like that. So, to some degree.
like, I don't know where I was going with that, but I think operators…
**Laurent Quérel** 34:19 I think I know where you want to go. I think.
**Drew Relmas** 34:21 Yeah.
**Laurent Quérel** 34:22 To expand the policy.
The concept of policy to declare those permissions.
And if they are outside of the pipeline configuration, that specific user, pipeline owner, team, whatever.
Project is able to do, and if this policy could be applied externally to that.
Then we have two types of operators. We have the pipeline operator, which is responsible to manage this pipeline and to declare it, and we have an infrastructure guy that could specify What is authorized, in terms of the payment?
**Drew Relmas** 35:02 Yeah, yeah, I think that's where I was going. Josh or anyone else. Josh, go ahead.
**Joshua MacDonald (Microsoft)** 35:08 I just wanted to add, I put a comment on the bottom of the issue here, saying that this fits very well with the RFC that I wrote, number 4, on context, PData context and conditional context entries.
I had proposed a slightly different, but doesn't matter, like, structurally equivalent to saying that there is a… we want, essentially, an easy way to To declare that this pipeline must have this context, and if the data does not have this context, it does not belong in this pipeline.
So that you could, force a tenancy model onto a pipeline, for example.
And you can even sort of think of these as constraints. Like, if you have a situation where there's a receiver that we know, like, it's going to configure which context entries it tries to evaluate, and then you have a batch processor, and you say it's partitioning by a particular context entry.
If that context entry is not produced by the receiver, like.
it's not… the request will not make it, so it better be at least possible for that request… that receiver to produce the thing that the batch processor is partitioning by, or else you have an invalid, configuration.
And likewise, if there's an exporter that must have, like, a particular context entry, then the thing must, before it has to produce it. So either we can infer configuration, or we can check configuration, or both. But I like this idea in general.
Got it.
**Drew Relmas** 36:38 I guess seems reasonable, unless anyone else on the call wants to chime in.
**Laurent Quérel** 36:44 I think in general, Those approach, the one that you discussed, just now.
Joshua, thing that we did before.
We have some contract-based approach where we are trying to validate Maximum of things.
During the… Creation of pipeline, configuration time.
In order to eliminate, to get rid of runtime validation as much as possible. So what you did on the context is exactly following this principle. What we are trying there to do also is Basically, adding a kind of type system on top of the pipeline configuration to prevent misconfiguration, misuse in general. I think we should do that as much as possible.
That's exactly what we do with OPL. I think with OPL, we… We are following this principle from day one.
With an even more granular approach, where we try to Detect.
When someone is trying to access to a field that could not be accessed.
Just by design, because the pipeline is, for example.
Filled with logs, and we know that logs does not expose, Some fields that are only exposed for span or metric, like metric name, for example.
So that will be discovered not during the runtime, but just you can't deploy this pipeline because it's incorrect. So we should be able to be in such position And I think that is also going in the same direction like you are doing for the context.
**Joshua MacDonald (Microsoft)** 38:36 Very nice.
Yeah, so we're inventing a type system for pipelines.
And some of us like to think about compilers.
I see that we've reached the end of the agenda. This is a good time to insert something in the agenda, if you have it.
Or…
**Drew Relmas** 39:02 Or we can look at sale issues.
**Joshua MacDonald (Microsoft)** 39:05 Begin throwing, yes, there are the stale issues. Begin throwing your favorite PR that needs review into the chat, perhaps.
Why don't you take us to the stale issues?
**Drew Relmas** 39:17 Sure.
All right, updated two days ago.
These were all updated. Oh yeah, of course they were updated two days ago.
Let's see, we have a problem with Kubernetes.
Something about CRD and serialization of config.
**Laurent Quérel** 39:39 Oh, I think that…
**Joshua MacDonald (Microsoft)** 39:40 I remember.
**Laurent Quérel** 39:41 I think this one is fixed.
**Drew Relmas** 39:43 Yeah.
**Laurent Quérel** 39:44 Yeah, this one has been fixed, either by David or Chris, but we no longer have this issue.
I.
**Drew Relmas** 39:51 I also think it's fixed, it's just not, linked.
**Laurent Quérel** 39:55 Yeah, we… we… Maybe you can add, David and Chris, because it's one of… We went on.
**Joshua MacDonald (Microsoft)** 40:08 There is a test now that forces this CRD correctness. I've definitely run into it and scratched my head a couple times, like, why do I have to do this weird thing? But it's… Okay.
**Drew Relmas** 40:21 All right.
**Laurent Quérel** 40:22 Looks like Pierre also added a message.
Pierre, do you want to talk about.
**Pierre Mariani** 40:31 Yeah, that'd be great. I mean, if, you know, if you're…
**Laurent Quérel** 40:34 I think we have time, so that's probably interesting to discuss that because it's an ongoing PR.
**Pierre Mariani** 40:41 Awesome. Drew, I think that's your screening. Would you scroll down a little bit until you see Lauren's, comment.
Yes, right there.
Lauren, it's your comment, so you might…
**Laurent Quérel** 41:00 Yeah, so the.
So, I really like the direction of this work, but I was thinking, can we generalize that a little bit more?
And the idea is the following.
So what we want to achieve, or what Pierre tried to achieve initially was Validating, basically, the decoding, component that we have, for example, Protobytes.
to, to internal, our representation, or that representation.
And, And also, we have sometimes… we don't, because of the pass-through mode, we don't decode the, the OTLP protobytes directly.
We are more in the lazy mode, but we still accept to implement some command, like, or function, like, new Meetings.
That will basically look at the byte representation without decoding.
And we discovered, some issues, or incompatibilities, incompatibilities, incompatibilities of… So basically, we found some issues, and And then this fear is about, let's try to be more In compliance with the Protobuf, specification.
And let's try also to discover how the system is behaving when we have invalid, buffers, or buffers… they are either invalid because we can't decode them, or we could decode them, but we have to follow the… the convention and the rules that PortoBEF is defining. So, an example of it is when you have a one-off.
If you have multiple variants, if I remember well, you have to report the last one.
Not the first, or the… if you have multiple of them, just the last one.
And that's, that's what… That's not what was done before, and we had also some invalid behavior for the num item.
In this case.
So, my proposal here is to express.
Thing that we want to check, conformance rule, or, some situation where things are totally invalid.
And the idea is we already have a traffic generator, so we already know how to generate a bunch of metrics, logs, and span.
And can we express those rules with a clear API? So there is an example here in this.
God section.
Where we say, okay, there is a… I want to test the case of.
the one-off, so the first one is about the one-off. Let's introduce a second variant for the one-off.
And, so we specify the target. I want to target a metric with a gauge in that case, and then there is a way to use a closure to basically append a second variant, and then we express the… what we expect to see.
And we expect to see, following the… Cotoberf specification, we should see the last one that has been happened in that case.
And we can, with this approach, we can also express some corruption.
So we want, for example, to To change a tag and use a tag that does not exist, or to.
change the length of a specific buffer with something that is invalid. And we should see… and we should express what is expected in the system. Do we ex… obviously, we should never panic.
And we should, express, okay, we, this… the following error message should, should, should, Be raised in that case.
So, I'm just trying to make… This proposal a little bit more declarative and expressive, and covering not only the non-conformant photograph message, but also the totally invalid, corrupted messages, which was not, I think, in the initial.
the perimeter of this PR.
**Pierre Mariani** 45:33 Can I ask you clarifying questions?
**Laurent Quérel** 45:35 Yep.
**Pierre Mariani** 45:36 You said you have a system to generate traffic.
Is it… is it like a fuzzer, and you generate all type of valid and invalid traffic, or is it more of a, you know.
Something compliant only.
**Laurent Quérel** 45:52 Compliant only. And that's why the… so the, the… You can see that, yeah, there is a receiver named Traffic Generator.
That could generate traffic either from semantic conventions.
So you have some control on what will be generated.
Or it will be just template-based, relatively static.
But those all will basically inject mutation.
**Pierre Mariani** 46:20 isn't.
**Laurent Quérel** 46:21 inject corruption.
On any traffic, and we could use, either… In the test, we define our own, protobuf message, or we use the traffic generator to generate a few messages, and we inject those mutations, and we And then we check that the expectations are effectively, observed.
**Pierre Mariani** 46:43 So.
Yeah, there were some similar concepts in the research I was doing. I'd like to take your take on this.
What… We could think about… Finding interesting mutated payloads differently from Maintaining the unit tests and keeping, you know, and making them clear to understand and read, as part of a regression test.
If we push that reasoning, you know.
Okay, and if we have a… reference implementation of a protobuf parser, right? Let's say PROS, for example.
We could use, you know, very heterogeneous tooling, right? C++ and whatnot, Python and all that jazz.
To fuzz a lot of messages.
Compare, the expected parsing based on the reference parser and the actual parsing based on our, you know, our own.
our own implementation.
Capture the one where there's a delta.
And then it becomes a matter of Quote-unquote, merely tracking or regenerating those Binary payloads as simply as… as possible, right?
I think it's diff… so I can see some advantage in doing that versus us creating our own API to mutate payloads and go hunting for, you know, broken… broken test cases. I was worried about you know.
there's probably many ways to break a payload, right? And I don't know what's gonna… that's going to mean for the API, and… and I don't know if it's the most efficient way of finding issues in a large scale.
**Laurent Quérel** 48:54 For me, these two approaches are totally complementary, because A fuzzing-like approach.
So, first, it's… it's less… less efficient in terms of.
Processing, because you have to do a lot of mutations that are usually relatively random.
So, being able to observe exactly what you are trying to fix.
two variants instead of one. I don't know even when that will happen. Maybe that will happen, but we have no control on it.
So… For me, it's more solving the co-option part.
We… the contract being, oh, the system should not panic, and we should react properly in terms of error message. When we are in front of this kind of invalid traffic.
In that case, for me, the first Reason of using such approach is to be very declarative and to express properly the… the conformance test.
Instead of relying on random, generation.
And fuzzing.
We could imagine that the same system is… is… could be also used as an input for a further, because if we are able to to add some randomness into this API.
You could have something like every two message, or… Different verb there that will basically express some randomness, and then you corrupt, Either random element into the protobuf, or some specific element.
So for me, it's, it's like the… it's not incompatible, and I think there are, complementary approaches.
**Pierre Mariani** 50:48 Okay, yeah, that sounds… that sounds good. One thing I came across, which I put in the bucket of further, maybe it's incorrect, but there are some projects that are, quote-unquote, structure-aware mutation, which I think… At least based on those three words, make me think, like, there is an element of randomness that understands the structure of the message.
At a minimum, I think it would be instructive to, you know, I could read those APIs to see, you know, if we can map them there and understand those concepts a little bit better, see if they make sense.
**Laurent Quérel** 51:25 Yeah, I think if we can avoid to reinvent the wheel, I'm not against it, obviously. If there are such.
Stricture the world.
Boozer Earl.
Would be super interesting to integrate that.
Yeah, and…
**Joshua MacDonald (Microsoft)** 51:42 I just Googled it. Google has a C++ protobuf.
Buzzer library.
I also agree that the two approaches make sense, the random fuzzing approach to discover cases, and then, like, encoding them as readable mutations, maybe. It sounds pretty elaborate, but it also sounds nice.
**Pierre Mariani** 52:03 Well, thank you. I I'll file this as a separate issue, or I'll use the GitHub feature for that so that we track it separately. And maybe we can see from there.
Thank you.
**Joshua MacDonald (Microsoft)** 52:15 Great, thank you Pierre.
**Laurent Quérel** 52:18 Thank you.
**Joshua MacDonald (Microsoft)** 52:22 Guess it's the last chance for your favorite PR that we should all review. Oh, here's one. Looks actually stale.
Should we continue with Quiver Dictionary Max Key?
**Drew Relmas** 52:38 Max Kiewit.
This feels like a pretty good… First issue, Aaron.
**Joshua MacDonald (Microsoft)** 52:50 And what I'm hearing from Laurent is that we just shouldn't close the… let these close, and it's okay to just remove stale and come back to them if you want.
**Aaron Marten** 52:59 Yeah, we don't.
**Laurent Quérel** 53:00 Right.
Sorry, Greg.
**Aaron Marten** 53:02 I was just gonna say, yeah, we definitely should keep this issue.
**Drew Relmas** 53:18 Utkarsh This one…
**Utkarsh** 53:24 April 6, okay.
**Drew Relmas** 53:29 Ha ha ha ha!
**Utkarsh** 53:30 Yeah, I think, like, from what I remember, yeah, there's inconsistency around how, We… Deal with optional fields, like… So there's 3 places where we… Do these proto parsing, so… Some places, it was, like, an optional field is… encoded as none, or, like, sum of zero. I'll have to go through it again, but I think, yeah, it's been quite some time, but I remember the issue being that Our custom parsing logic.
Are not consistent.
With each other in… with respect to how they deal with this.
**Drew Relmas** 54:15 Definitely sounds like a keep.
**Joshua MacDonald (Microsoft)** 54:18 Yeah, and there was a PR by this Uros Stefanovic from Databricks, who tried to fix something like this, and then I pointed something out, and they closed it, because it was hard. So, there definitely are issues here. Trying to find that.
And But we should keep it open.
**Drew Relmas** 54:41 I suspect this one should be kept open too.
Traffic gen improvements.
We've done a bunch of this.
Looks like there's a closed one from CJOE.
**Laurent Quérel** 54:59 What was the list initially? The… okay, into this iteration test, but, like.
Yeah, I think we did a lot of things there. I'm not sure that we covered 100%. Maybe that's a question for Sidro.
But I'm sure that we covered multiple of those items.
**Drew Relmas** 55:33 Ha!
**Laurent Quérel** 55:35 Yeah.
**Drew Relmas** 55:36 Actually, this is already kind of being handled by my metrics work, so.
I will close this.
**Joshua MacDonald (Microsoft)** 55:47 Nice when some of these issues can be closed. Well done, Drew.
**Laurent Quérel** 55:50 Good.
**Joshua MacDonald (Microsoft)** 55:54 And Laurent, you and I were talking about Exporter Helper as well this morning.
**Laurent Quérel** 55:58 Yeah.
**Joshua MacDonald (Microsoft)** 55:59 This keeps coming back.
**Drew Relmas** 56:16 Wasn't there just an, maybe from Noah about startup?
Oh, also, there was… a PR merged, and I think we can probably close this.
**Laurent Quérel** 56:32 Do we have Lalit with us?
**Drew Relmas** 56:35 We do not, I believe he's out of office.
**Laurent Quérel** 56:37 Can you show me again quickly the description initially?
Oh.
Yeah, I think we can close it. I remember the work that has been done there, yes.
**Joshua MacDonald (Microsoft)** 56:58 Hi, Russ.
**Drew Relmas** 57:00 Great. By the way, I see we're getting very close to under 50 PRs again, so we must be reviewing well.
Flaky tests.
Thank you. Validation tests.
Some of these are probably fixed, and I think we should continue using Aaron's…
**Laurent Quérel** 57:21 Yeah.
**Drew Relmas** 57:23 Machinery instead of this. Closing… Follow flaky test.
It's.
Three more minutes, can we finish? Export engine level metrics.
Yeah, this.
**Laurent Quérel** 57:45 I think we.
**Drew Relmas** 57:46 Metrics ITS, right?
**Laurent Quérel** 57:48 Obviously, nice.
**Drew Relmas** 57:56 OTLP exporter, we…
**Joshua MacDonald (Microsoft)** 58:01 This stuff is embarrassingly old.
**Drew Relmas** 58:03 Do you think we have? Yes, 2020.
**Laurent Quérel** 58:05 Yeah, I think we can say yes, it's closed, and we can close it.
I don't remember even a time where the OTAC exporter was not,
**Joshua MacDonald (Microsoft)** 58:20 This one down for, like, 18 months, it looks like.
**Drew Relmas** 58:26 And abnormal.
byte rates with OTLP, something from the benchmark.
**Joshua MacDonald (Microsoft)** 58:33 Very old.
**Drew Relmas** 58:35 a.
**Laurent Quérel** 58:35 I would assume that he's…
**Drew Relmas** 58:37 It's been marked sale twice, so.
**Laurent Quérel** 58:39 Yeah, yeah, yeah, I think it's fixed.
**Drew Relmas** 58:42 Okay.
Look at us, we finish all of them with 2 minutes to spare.
**Joshua MacDonald (Microsoft)** 58:49 Well done.
**Drew Relmas** 58:51 Why don't we all get two minutes back then?
**Noah Falk (Microsoft Corporation)** 58:54 Right.
**Joshua MacDonald (Microsoft)** 58:56 Thanks all. See you next time.
**Laurent Quérel** 58:57 Thank you. Bye.
**Drew Relmas** 58:59 Thank you.

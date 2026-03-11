SIG: Arrow SIG
Date: 2026-03-10
Duration: 95 minutes
Zoom Recording URL: https://zoom.us/rec/share/yfCJNLmN47w0DjrTjofejpYYf-GkLDD1P7wPmGYZrTSkwUAKl1vK9jVO9ALz6x6F.DYd08M6D--nW908l
============================================================

## Zoom Recording Transcript

**Albert Lockett** 01:49 You guys…
**drewrelmas** 01:53 Hello.
**Laurent Querel** 02:03 Hello, guys?
**Albert Lockett** 02:11 Hello.
**Laurent Querel** 02:16 I don't know. What a week.
so many PR…
**drewrelmas** 02:21 Yeah, they've been, flying.
**Laurent Querel** 02:24 Yeah, bug fixed, and… bugs, bug notified, so many things. That's really cool.
So, if I understood well, Joshua, we will not be able to join today.
**drewrelmas** 02:45 I believe he is still out of office, yes.
**Laurent Querel** 02:47 Yeah, okay.
So, I will share my screen.
Or maybe, Drew, do you want to start with the bug triage, maybe?
**drewrelmas** 03:02 yes, you mean, me, share, or.
**Laurent Querel** 03:08 Yeah.
And, and for the other, don't hesitate to add some, items on the agenda.
**drewrelmas** 03:24 is the screen coming through properly?
**Laurent Querel** 03:27 Yep.
Yes, sir.
**drewrelmas** 03:30 should look at issues, not PRs. So,
We have a couple… let's see, since last week… Looks like we ended up…
about here, I see some accepteds. There's not actually a whole lot of new triage deciding issues since then.
But… we can go through. So, first, there's something for Kalner Query Engine from Albert.
I see no issue with this.
**Laurent Querel** 04:09 Yeah, me too.
**drewrelmas** 04:13 triage, okay?
We have some reports of flaky bug tests, that CJO's been running into.
A lot of them are actually in the validation suite. They seem to be timing out, running too long. I know I've approved a couple times for him. Oh, this one's actually Durable buffer. This is something different that I have sent to Aaron directly.
But in general, the CI has been not performing very well the past few days. I think we have a lot of churn there, so I'm not going to dig into those here, but obviously we should not be ignoring tests, and we should work to get rid of those.
Another commoner query engine.
**Laurent Querel** 05:04 Just a question regarding that, Drew, and for the others also.
What we observed for the last few days,
It's because we introduced some new elements, or they were just not visible before, and they are now issued that are more visible in the build.
**drewrelmas** 05:26 That is…
a great question. I feel like I've seen these transiently before. So, for example, this one's validation test debug processor, that runs for over…
60 seconds, you know, a couple of these validation ones, run.
quite slowly. I think we recently turned on more of these, if I'm not mistaken. Does anyone else on the call know, or have more context on this? Maybe CJO?
**Cijo Thomas** 06:01 Yeah, I think the validation tests are, like, pretty new, like, 2 weeks old, maybe 3 weeks.
**Laurent Querel** 06:08 Okay.
**Cijo Thomas** 06:10 Yeah, and we.
**Laurent Querel** 06:11 Oh, yes.
**Cijo Thomas** 06:12 GitHub Actions slowness, so it may help.
Amplified some of these issues, but definitely they are new, like, it's, like, less than 3 weeks out.
**Laurent Querel** 06:22 Okay, yes, I see. I don't think Shen Li is there today…
So, I will take an action on my side.
talk, who is Shen Li, Which…
He's the owner of the Radiation Framework.
And, and look at those, OTAPDF validation tests that… Or not working very well.
**drewrelmas** 06:52 Yes, I've, I've merged,
Well, for example, this is CJ doing one, just, he's been adding a flaky, ignore tag on top, pointing to an issue. So, if you look at this issue, 2227, I think it's been referenced every time,
Every time this has been done.
**Laurent Querel** 07:18 Okay.
**drewrelmas** 07:21 Okay, back to issues.
commodore Query Engine, Albert, I see this is another one. It's actually not ready for work.
**Albert Lockett** 07:30 Yeah, so,
This, this one is just to kind of… we implemented in column Rexion the ability to do simple arithmetic on floats and ints, but, we didn't implement the ability to do arithmetic on date and time span type, types. So this is just kind of per posterity to remember to do that.
And the reason I marked it not ready for work was just because we had a contributor that was, like, hoping to pick it up, and I kind of had to say to them, hey, you know, hold up a little bit, because we still need to do a little bit of analysis around, like, what the type system would be, you know, what the type is if you add two dates, what the type is if you subtract two dates, things like that, so that's why I marked it not ready for work, just to… just to avoid someone, like, picking it up, spending much time on it, and then, like, doing something that we didn't actually want.
**drewrelmas** 08:15 As a point of order, do we want that to be counted as triage, accepted, or…
Needs triage still.
**Albert Lockett** 08:27 Oh, I think, I think in Canada, Triage accepted. This is definitely something that we want to do, it's just not ready for, like…
Someone to just start coding on with a little bit of analysis around, like, you know, what we're actually.
**drewrelmas** 08:39 Okay.
Sounds good.
This is actually an interesting one, that I think… who left feedback on this? Jake left feedback on this. Lalit opened it…
I mean, it's somewhat self-explanatory. For certain compliance things, we should support different
libraries for our TLS. I… we don't need to go super into this, but, I don't think it's,
I don't think it would be very contentious to do, and we have a new contributor from Microsoft's side, Pratish, who's not here today, who is interested in taking up this work.
but if there's no other thoughts on this, I can move it to accepted.
**Laurent Querel** 09:33 Sounds good.
**drewrelmas** 09:40 Alrighty.
We have…
This, is something that I definitely want, Laurent, this is a follow-up from the topic PR, talking about, broadcast all, so we wait on Aconex from all.
Subscribers of the topic.
I definitely think this is accepted.
**Laurent Querel** 10:06 So, just to, to,
gauge the priority and, yeah, the importance on your side for that. My understanding was…
That right now, the main… Scenario that you'd like to…
For which you like to use topics was, the…
the support for, multi-tenancy isolation, so you have, like, a… This one, go ahead.
**drewrelmas** 10:37 We have two…
And I'm sharing my screen, so I'm not sure if Lalit is actually in the call, but we actually have two different scenarios. His is on the specific tenancy split, whereas
I am more interested in the broadcast function. With the pattern we talked about with ingress.
Multiple processor pipelines, and, like, an ex… a shared egress or exporter pipeline.
So…
it's hard for me to give a priority ranking between them. I'm sure Josh could give a better answer, but…
for the moment, without this broadcast ACNAC support and topics, for my scenario… I think Lalit is good. For my scenario, I'm unable to move to using topics. I need to continue doing a single pipeline.
Discussed in the past.
So it's not… this isn't, I would say, a hard blocker, but it is a blocker for my scenario to adopt topics.
**Laurent Querel** 11:46 Yeah, understood.
Could you maybe, Add, comment to this, 2252 issue.
A description of your, scenario.
Yes. And what you expect in terms of behavioral…
Especially when… for the coroner cases. What happens if, you have one of the…
**drewrelmas** 12:13 Mine acts while another one acts.
**Laurent Querel** 12:15 Yeah, yeah, this, yeah. So I described,
a proposal for that, but I just want to make sure that, because we could imagine some more advanced
Policies?
I think this one, the… the Ahmed first, and, Ul, It is,
probably good enough for most of the scenarios, but I can definitively imagine some scenarios where we need some intermediary, let's say a quorum… a quorum approach.
Where we say, oh, we… we just want, we… let's say we have 10, subscribers on this broadcast channel, and we are okay with 3.
That, are returning, AC.
**drewrelmas** 13:01 Right.
**Laurent Querel** 13:01 In that case, the… The conclusion will be an act for the upstream nodes.
If we don't reach the 3, then it will be a knock. This kind of stuff.
It's becoming very, very complicated at some point if we want to cover all the scenarios, so I'd like to get, for your specific case.
A reasonable description of what you expect.
**drewrelmas** 13:26 Sounds good. I will make sure I do that within the next day or so. I might also chat with Josh when he's back tomorrow, but yes, and I will do that.
Then we just have, something with perf test, Looks like Jake… Someone already…
has a work-in-progress draft out for this. I assume this is just a test optimization.
**Jake Dern** 13:57 Yeah, there's, like, some, like, issue, with the, the draining, logic, basically, detecting when all the pipelines were, were finished draining, so I think I have a solution, but, Laurent can tell me if what I did is sensible.
**Laurent Querel** 14:14 Yeah, so that's one of my tabs open. I need to focus on that after this meeting.
Thank you, Jake.
**drewrelmas** 14:24 Alright, and then, I think this is just, this one is an improvement to the validation framework.
**Laurent Querel** 14:34 Yeah, so the… That's the idea here is to add support for test containers.
The test container project.
That will give us a way to…
To basically, test the pipeline with…
Let's say, a backend that is delivered as a container, and the validation process will We'll basically connect,
The pipelines running with the… this,
container. Let's say that you have, I don't know,
what could be, reasonable, in terms of description. So, let's imagine that we, we, we have,
An exporter that is able to export to a specific backend that exists,
As a container, so we could imagine that we have a validation process
Starting this specific container, the pipeline.
Filling the… sending the traffic to this container, and then we can check and validate what was
Stored into this, backend running into a Docker container. So that's the idea behind this test container.
**drewrelmas** 15:55 So, essentially, a deeper thing than a no-op exporter.
**Laurent Querel** 16:00 Yes.
Yeah.
Okay. Instead of having an op-exporter, you could have,
Right now, the exporters we have are not really, backend specific.
Except for the Azure, the, Geneva stuff.
**drewrelmas** 16:20 Yes. So let's imagine… yeah, let's take Geneva as an example.
**Laurent Querel** 16:24 If you have, a Geneva container, simulating a Geneva backend.
with this, extension of the validation framework, you could test your Geneva exporter.
sending traffic to this Docker image where, a Geneva simulator will be.
And then check that everything that has been sent to this container
Is, corresponding to your expect… that corresponding to your expectations.
**drewrelmas** 16:59 Yep.
Okay, that makes sense.
And finally another Blakey Tech Tests thing, which I've already forwarded to Aaron.
And I think that's it.
**Laurent Querel** 17:18 Great, thank you. No.
So I think we have, let's see… Yeah, share my screen now.
Okay, so in the agenda, we have two… To ATM…
So, do we have, Utkarsh, and I guess we have Gokan in the meeting, do we have also Utkarsh there?
**Utkarsh** 17:58 Yep.
**Laurent Querel** 17:59 Okay.
So, I read, so, Gokan, you… maybe you want to open the discussion and let you describe what was the… I think I have an idea of what you want to discuss, but…
Sure. The flow is for you.
**Gokhan Uslu** 18:20 Okay, thanks. So, I think the one thing that I wanted to talk about was
That seems like the main concern in the design.
document that I created is the fact that shared state needs to be handled by the expansion altercin, which requires
Arc grabbing those fields.
And I've just looked at all the other alternatives, and just because of the fact that we have sand-only
types.
That boundary creates a lot of friction on… probably Ken.
Share an instance.
Quote-unquote.
or share state…
like, if it was ARC, you could clone easily. If it was RC, you could clone easily, but when it is sent.
Neither works.
So I settled on just regular cloning.
To keep the design simple, mostly, and also avoid
This art mutex thing that happens with the handle-based design.
And I also looked at other alternatives that created other trade-offs that I don't want an extensively talk about right now. If you want, I can dig into it, but just wanted to talk about how big of an issue would that be to say that extension authors
Should be responsible of the shared state.
My last comment, very briefly.
Yeah, you know, explains.
Where I am at.
**Utkarsh** 19:59 So I had a question. What is, the concern with ArcMutex?
What is the concern with handle-based approach requiring authentic?
**Gokhan Uslu** 20:12 I mean, I don't exactly have any problem with what it causes in terms of performance, other than there be, like, at least
There's a blocking await there, it seems like.
But, it is mostly about the simplicity, of the…
overall design. Like, when, when you try to create a… an extension.
Type, you would need to create an extension trait, and then you need to create a handle that
Does all that plumbing for you to handle that wrap paint.
of ARC, and… Which gives you this,
Signaling to the extension rider, hey, you cannot share any state if you do not wrap it
in ArcMutex, whatever, the shared state, because if your start method, the lifecycle method, is updating
A field that you need to also sh… Share.
With the handle.
Then, that puts you in a situation where
You need to satisfy, it seems like, both send and sync bonds for that
Object that you're sharing the state for.
So… That require… it seems like that requirement is clear, that error-proness is gone in this design.
But it also… Again, creates that requirement, adds that boilerplate, adds that indirection, etc.
And I'm not sure… I cannot talk too much about the performance overhead or anything.
Without actually specially doing any benchmarking, but… And, it, it…
In my design, you don't have to deal with
Like, you would, have, only a single lead table look up to, apparently around the…
methods, instead of going through the Archmutex, lock, indirection, through the handle, there seems to be multiple calls there.
And also… Your, your trade impla… the way that you can create traits.
in the… to define an extension contract and implement it is quite main… mainstream, and I like that pos… those two things about it.
**Utkarsh** 23:01 So a few things,
Firstly, the art mutex thing is completely hidden from both the extension author and the consumer node, be it receiver or the exporter.
whoever.
**Gokhan Uslu** 23:14 No doubt.
**Utkarsh** 23:15 So, they don't have to worry about arcmutex at all. They just implement their extension logic without
without us.
Imposing any clone constraint on them, or sync constraint on them.
And, the other thing about performance, it shouldn't be an issue. I mean, there'll be a few more
I don't know, maybe, like, some more nanoseconds?
But there's no contention.
Since it would be the same thread that's running start method and also then coming on to the
consumer node logic to use that handle. So, it's always an uncontained log.
And, yeah, I think the… what I like about that approach is that, like.
It's more easy for the… Users, extension authors, and the… consumer notes. They don't…
They don't have to make… worry about, like.
Making sure that they are crap, they're mutable.
data.
**Gokhan Uslu** 24:20 So, how would you, for example, share
State between the handle and the lifecycle method with the handle-based approach.
**Utkarsh** 24:37 The handle… The inner data of handle is the concrete implementation of the extension.
So…
you could be using all of those things which you've used in your extension implementation, like the Tokyo Sync watch receiver, and…
other, primitives can always be used in this approach as well.
**Gokhan Uslu** 25:03 Well, what I'm trying to ask is, for example, if you were to store a string, and you wanted to update it
For example, in the…
lifecycle in the start method, but be able to access it through the handle. How would that be possible? It seems like you would,
Need to do some wiring up for that field at some place.
**Utkarsh** 25:28 So the handle will give you access to whatever methods the trade defines, and
So you don't have to operate at an individual data field level. If that's what's required, then you
Then your trade extend… your trade needs to have a method for Get me that string.
Get me the latest value of that string, or whatever, and then the start method can keep updating it whenever it wants to.
And when the… That is running the consumer node logic, when it will call that method.
Take that mutex and see whatever is the latest value there.
**Gokhan Uslu** 26:05 Yeah, so what I realized is that you would need to have, for example, say you want to share
You, you want to update, Stringfield.
Inside your start method.
And you want your handle to be able to access that string fuel.
So you would need to, first of all, Right? Create a… Arc wrapped.
are actually… ArcMutex, so, yeah, wrapped…
**Utkarsh** 26:42 Not, not the extension author.
They don't have to arcmutex.
**Gokhan Uslu** 26:48 Yeah, they would have to arc at least, that's right. And then you would need to…
**Utkarsh** 26:52 they wouldn't… What I'm saying is.
The extension author doesn't have to… do that.
**Gokhan Uslu** 27:01 Not at all. Okay, maybe my understanding is wrong there, but…
**Utkarsh** 27:06 Then we create the handle, so the handle takes…
The extension trait as an… the implementation of the extension trait as an input.
So there, it arc wraps it, arcmutex wraps it.
**Gokhan Uslu** 27:17 So that's done by the framework.
The expansion instance is separate from the lifecycle instance, so if they have to update the same field, it needs to be archived, is my understanding. And there's nothing that you're doing there to avoid that, it seems like. That's been my…
Discovery, but again… You can click it.
**Laurent Querel** 27:38 Suggest, something, guys,
Do you think that would be nice… interesting to have, from both of you,
A complete example of an extension with some background, processing.
And… The, the consumer part of this, capability extension able to…
To interact with, with this background task to get some… some information.
**Gokhan Uslu** 28:17 So, I actually have implemented something like that on my local environment. I can share my screen if you have time to discuss about that for a few minutes.
**Laurent Querel** 28:25 I think… why not? But I think that what would be nice, maybe… I know… I mean, this extension system, to be honest, is fundamental, and I think that's why we are spending so much time on this thing, because we want to make it… to have the right design.
And it's far from… straightforward.
I didn't read the last, exchange you had, you and, and, Karch.
on that, so I'm not sure to follow entirely, but what I see is,
some friction… some potential friction that you… you think, there is, maybe there is not. But, on the…
On the, author of extensions.
So…
if you already have an example, that's nice. I think that would be cool to… to, maybe to add a link to the… into this thread, directing to this, example. And you, Utkarch, if you have,
Already something, or if you don't, maybe if you can create an example to illustrate the… Such,
extension and handle with a similar capability. That would be nice to… for us to compare the two variations and…
That, that will give us,
Yeah, that will ease the…
The analysis, and we could make some decision.
**Utkarsh** 30:04 Sure.
**Laurent Querel** 30:07 Okay, I think that would be great.
So, if I understand well, Gokuan, on your side, you already have an example.
So please add it to the… to the thread there.
And.
**Gokhan Uslu** 30:23 Yeah, so…
**Laurent Querel** 30:25 Okay.
**Gokhan Uslu** 30:26 Oh, sorry for interrupting. I have an example of mine, but I also, wrote
this is an extension on Utkarsh design, this is where I was, like, seeing… you know, there is some plumbing and wiring up that I don't like, and I like it more like a clean API surface, that's the main thing that I'm arguing for, but… and also, you know, with some minimal, maybe, advantages over…
like, minimal performance-related aspects, but besides that, I don't see any issues with what Utkarsh has come up with either. I just… it's more like maybe a style question.
But yeah, that's fine.
**Laurent Querel** 31:05 Okay, so share the… so, I don't know how easy it is, to share the… this one example that you have based on the Otcarch branch.
Anyway, and encourage, please look at that also to…
To see if, that's the way that you were seeing the…
**Utkarsh** 31:27 Your approach used?
**Laurent Querel** 31:31 And, I think I need to, to look at that again, sleep on it a little bit. Maybe exchange tomorrow with,
with Joshua, and and, and we, we, we need to, to, to take a decision,
ideally to all… Maybe the day after, Max.
**Gokhan Uslu** 31:56 Sounds good to me.
**Laurent Querel** 32:01 Okay, great. But, anyway, thank you so much, both of you, to work on that.
There are so many, views of it, so the…
the… the bureau token, extension, that…
We already have there. It's definitively, a great one.
I think a GWT token-based,
Authentication system will be another, Option.
Another extension.
I don't remember if there is a such extension, I guess there is a such extension for…
for the Google Collector.
Okay,
Okay, so next, we have, okay, Prometus Exporter.
So, before I'm talking about that, is there any additional feedback from others to this extension support?
Okay, I guess it's a no. So,
permitous exporter, so the… I didn't prepare anything, I just want to
To explain why I'm working on that.
And to collect feedback from you guys.
So, as you know, we… We decided, more than 1 month ago.
To generalize the… our internal pipeline engine, But our pipeline engine.
And to use it also for, the processing and the delivery of internal telemetry.
So we already have a first instance of that, and we have some… Additional approach
That we implemented before that need to be migrated.
So the, So we have a…
A pipeline group system, which runs an obsolability pipeline that could be configured now directly from the
The engine, section inside the configuration model.
And,
And this pipeline is based on exactly the same mechanism that we have for the rest of the regular pipelines.
Except that we have some, special, receivers.
We can leverage any processor node and any exporter nodes.
That gives us a way, for example, to export events.
Via the OTLP exporter, or via the OTAP exporter.
In parallel, we have the, this new UI that has been merged recently that is leveraging
the, let's say, a pool-based, endpoint.
Currently exposing primitives, metrics, and
a G zone variation of that, and basically the UI is leveraging the GZON metric set.
So, the reason why I'm… I like to work on a primatus exporter
is to be closer… I mean… If we want to…
Make the matrix, the internal matrix.
Following the same approach that we are currently using for the internal events.
We knew… we need the metric set, captured by this internal pipeline.
Flowing through the, the pipeline, this pipeline, and, and be exposed.
directly, to be consumed, for example, by the UI.
So…
That means that we need some new exporter that will work differently, instead of being pushed-based exporter, that will be a
a pool-based exporter, like a Prometus exporter, the regular one.
Or, like, a variation of that to expose,
LG's own, endpoint compatible with the UI.
So that's why I'm working, exploring this… this space, and see
How we can create a search exporter that will be used first.
For the internal, pipeline system.
And, and potentially could be also used for regular pipelines.
So, I'm interested by having your feedback on that.
I didn't implement it a lot yet, so it's definitely,
I can change my mind, and I just want to give you the… where I am, and what I intend to do.
Makes sense for you guys?
**drewrelmas** 37:54 We're all shocked into silence.
I see some thumbs up. Yeah, I don't see any…
issue with that off the top of my head. I don't know if we have… You know, a compelling…
Use case for it ourselves, but,
I mean, anyone else working on more of the internal telemetry system have anything to say?
**Laurent Querel** 38:28 Okay, so in that case, I think I will continue on that.
We definitely have issues here and there, so,
This Prometus Exporter is different… oh…
Is there someone that wants to say something?
**Andres Borja** 38:50 Yeah, sorry to interrupt. No, I'm just curious… first of all, yes, does…
That's something we definitely need. I'm curious about what are you thinking in terms of, I mean.
I guess it will have some sort of storage, right? Because… because…
It will… that the exporter itself is going to be holding the data, right?
**Laurent Querel** 39:14 Yes, indeed.
That will be,
a new kind of exporter, I mean, same interface, I'm not introducing a new type of node, but
That will be an exporter where,
We share… we are sharing a state across, pipeline instances, in order to… To expose,
an aggregated state.
For it.
permitous endpoint that will be reported on demand.
And, I think we can implement it.
So, the, the, the, the…
the part where I'm still hesitating is I definitely see a way to implement that in a very… in a very efficient way, just for the internal pipeline purpose.
Where I'm hesitating is to make this, exporter available for regular pipelines.
The difference is… For internal, for the internal telemetry pipeline.
We, we know that, I think we have two deployment models that are…
So first, we don't need… I mean, I don't expect to see,
Such big, internal, telemetry stream that,
we will require more than one CPU, for example, to handle it.
The second, if we are running on…
a NUMA architecture. We could imagine that we have one internal telemetry pipeline per pneuma node.
And, and, and so, we could imagine a such primitives, like, exporter.
that is able to run either on one CPU or one CPU per luminode.
And, and we could try to, to minimize the…
the communication between the new nodes.
If we… If we expose this, primitive Slack exporter as a regular exporter for any pipeline, then…
Nothing will prevent to deploy it on…
as many CPUs you have into your system.
And… and then we… we are diverging a little bit from the…
From the existing set of constraints that we are trying to follow, or the principle that we are trying to follow.
Being… that we are trying to eliminate as much as possible any synchronization mechanism.
So… that's what… that's why it's an open question. Do we want to enter into this,
Do we just want to focus on, first, the internal needs and optimize for it, or do we want to think about an approach where we try to
Partition, for example, this internal state as much as possible in order to reduce the… the possible contention.
I'm still debat- debating about that.
My first need is definitely for the internal pipeline. So, I'm curious if you have,
a need for such, Prometus-like exporter, for other…
Purposes that are not aligned with this internal telemetry pipeline.
**Andres Borja** 43:24 I think, as you explained in the introduction, it's, the way it designed the internal telemetry pipeline is yet another pipeline with its own
Configuration block, but it's yet another pipeline, and then, yeah, you might agree that
I mean, you may say that it's, A single threat, right?
the components…
just another component, you know? They are… they are sharing the same component, so… so they should…
Behaved in the same way.
So… Yes, the… I mean, maybe the first…
usage is the internal telemetry problem, but the Prometheus exporter is yet another exporter, right? So…
I can see a use case, for example, in Psydoc.
a Kubernetes cluster where you can use it, right? You can just use.
It's export it and use it with your own metrics.
**Laurent Querel** 44:23 Yes.
**Andres Borja** 44:25 So… My question about the storage was actually because of those complexities, you know, because
Today, we are having collisions in the memory storage for the metrics when we use both, because that is used by the…
by the SDK, and by the…
this admin endpoint that we are exposing, right? So…
**Laurent Querel** 44:50 Yeah, because of the reset,
there is that behavior, which has been… which is no longer required for the UI, so… This problem should…
will be… will be, should not be there now, I think.
You're talking about the problem that we had with the fact that on one side, we…
We had a default, reset for the metric, and on the other side, we…
We were just expecting to see,
**Andres Borja** 45:24 Yeah.
**Laurent Querel** 45:24 native values.
**Andres Borja** 45:26 the SDK is consuming those metrics from the shared storage, right? So…
So… Yeah, it's kind of like a race conditions on who consumes them first, right?
So, and that is because, you know, in the SDK world, and even in the other exporters, the exporter itself is the one that holds the…
the metrics, right? So they can accumulate them in the export and not before that.
**Laurent Querel** 45:56 Yep.
**Andres Borja** 45:57 So, I guess we do have that problem. There is kind of like a new problem, but… But we…
Once we are in multi-core, right, multi-thread, For the same exporter,
Then, yes, we have the problem of the… how do we share that?
You know, memory, between the different threads.
That's… that's an interesting problem to resolve there.
**Laurent Querel** 46:27 Yeah, the… I mean… I think it is not really… I mean, there is no…
Yeah, if you say it's an interesting problem because we need to figure out what will be the best approach.
to minimize the risk of contention, I agree.
I don't think that the…
I don't think there is a problem right now to implement that.
But, there is an interesting challenge to make it As much as,
Not impactful on the overall system.
So that's why I was mentioning partitioning.
as, like, we… the approach that is used in distributed ash map Where we try to partition
stings, in order to reduce contention.
I was thinking about a such approach in this specific case.
But I don't have the detail, right? I need to analyze that a little bit more.
And that's why I was saying
I fully agree, we need to…
To create a general solution that could be used into any pipeline.
But we could… deliver that in different phases. The first phase could be focused on
We… we deliver this Prometheus-like exporter in experimental mode.
Only for, deployment into the internal pipeline system, because in that case, we…
we know that, for now, we only have one CPU core, so we don't really have this problem of
Dealing with multiple, cores accessing the same state.
the same storage.
And then, Phase 2, Phase 3, we could,
introduce or generalize the system to be used inside any kind of pipeline. That was my point, I think.
I think it's clear on that.
Do you agree?
**Andres Borja** 48:53 Yeah, that makes sense, that makes sense.
**Laurent Querel** 48:54 Okay.
Okay, kudos. If there are any other,
Topic that, you'd like to discuss, guys?
**drewrelmas** 49:14 The only thing I'll say is, I am going to try and keep up with
those… assigning those, issue types. Tom, we did merge in the issue templates that Tom worked on, so if anyone has feedback, or something as strange as you're creating new issues,
let us know, and we'll take a look. But I think it's a good step in the right direction.
Someday, maybe we'll even assign people to issues. That was something Pratish asked me. He didn't see that happening in the repo.
But… Yeah.
**Laurent Querel** 49:54 I had the opportunity this morning to create an issue, or yesterday, I don't remember, but
for me, the experience was, was good, so I don't have any, I mean, for me, it's well-structured.
I'm interested by having, additional, feedback, but…
No complaint on my side, at least.
**drewrelmas** 50:19 And they're checked in to the repo, so anyone can make a PR to it if you have an idea.
**Laurent Querel** 50:25 Yeah.
Yeah.
I think, I don't remember if that was discussed during the previous SIG meeting, or just with Joshua.
So, on our side, we are trying to…
So, I don't know if you saw the feedback,
So, in the hotel, I would have, a guy named Anton.
I don't think Anton is with us today.
**drewrelmas** 51:03 There's a question about publishing crates, right?
**Laurent Querel** 51:06 Yes, so, I, I,
I basically, used this, message also as an opportunity to
To describe for me what are the…
The current priorities, the important thing on which we are all working.
So if you didn't see the, my answer, I will just share that now, and maybe that could be,
A good use of the remaining time to get some additional feedback.
So let me share a different window.
**drewrelmas** 51:51 So, I just commented, we actually do have an issue for this.
**Laurent Querel** 51:56 Okay, great. Yeah, and I know that you also have,
an in-progress PR, for the renaming of the, OTAP,
**drewrelmas** 52:11 So, I did a rename on the… I've done the rename on the contrib components. The core ones are a little tougher, and I haven't quite had the opportunity to focus on it, but it's still something I want to get done, absolutely.
**Laurent Querel** 52:27 Me too.
Yeah.
Yeah, so, so my feedback,
was that we, we are… before to publish on Creates.io, we, we, right now, I think.
let me know if you disagree with that, on the Microsoft side. But it looks like…
Microsoft NF5. We both have the same kind of
let's say, focus to, to deliver, I mean, to… to have…
stabilize, more robust, version of this system by end of March, beginning of April.
If I understood well what Joshua told me last week.
And… and that means that we… sorry.
**drewrelmas** 53:21 I was just, agreeing. Yes, I think that.
**Laurent Querel** 53:23 Okay.
**drewrelmas** 53:24 our assessment.
**Laurent Querel** 53:25 So that means that… We… we have basically 20 days, minus the… the weekend, to…
implement the missing feature. I think a big one was Topic, will be emerged soon.
I'm still working on, the last feedback from,
I'm Nanit. And thanks, by the way, for the review.
I… I think the… if we… if we don't have the…
the uniformization of the internal telemetry pipeline. It's not a big deal for this milestone.
But that will be better if we have.
I think… An important aspect is the stabilization of the configuration model.
We are, we moved, a lot. We improved a lot of things recently in this space.
I would be interested to have, feedback from everyone.
Take a look at the current configuration model, and if you see… we definitely still have things that are not fully square.
Maybe not super consistent.
I think, it's… so, the one that I'm fully aware of are the… the ones that are related to this,
dual mechanism we have to, for the internal telemetry pipelines, or the internal telemetry reporting.
There, we definitively have,
inconsistency and redundancy. If you see, this kind of inconsistency, or…
yeah, fiction, in other places. That would be interesting to,
to, enumerate them into a GitHub issue.
Because we definitely need to focus on that.
Because that represents, basically, the… the…
the API surface for people that will just use the system, not implement anything, but just use the system. That's, for me, the top priority.
This effort I'm doing and this, produce, like, exporter.
Is just to stabilize the internal telemetry system.
We have a… definitively a lot of issues.
I know that Siju and many others are working on that.
Related to relinability and scalability.
Again, if you…
If you see some important bug that need my attention, please feel free to ping me.
So we have this renaming for the crates.
I think we already discussed that. You have things on your bucket to, To finalize that.
And I think we agree that the…
Those crates will be 0.something, so we still have the opportunity to… change the public API.
Not the configuration model, but the public API.
From… for a moment, even after the publication on Cresa Tayo.
And finally, I think, it will be a really, Nice to have.
Making sure that the benchmark… so we already have a long list of benchmarks.
I have someone in my team working on the…
comparison between the Go Collector and this, Rust and gene.
Hopefully that will be available by end of March.
And we could run that, I don't know, every week, or whatever will be the frequency.
And directly visible on the… Vidable on the same,
Benchmark input that we already have.
So that's what… that's my plan, basically, for by,
thing that I think we need to, to finalize by end of March.
Is there anything else that you think we need to, to take into account.
**drewrelmas** 58:20 I… sorry, I apologize, I was typing a message as well.
I… nothing else completely springs to mind. I think Josh
It probably has a higher mental model picture.
Than I do at the moment.
but… it all sounded good.
**Laurent Querel** 58:41 Okay.
Right.
Okay.
**drewrelmas** 58:46 And, Laurent, I would say
there is that issue we have that Josh opened a long time ago in October about releasing. If you want to add subtasks.
There, to track anything else, it would be a good place to do it.
**Laurent Querel** 59:01 And that's the… Is it the…
**drewrelmas** 59:05 That one day.
**Laurent Querel** 59:05 That's the one that you… okay, perfect. I will,
Look at that and, add subtask. Okay.
It's all good.
Great! I think we… we reached the end of the meeting. Thank you so much for all the work.
That has been achieved during the last few weeks.
And, see you next week.
**Andres Borja** 59:32 Thank you.
**drewrelmas** 59:33 Alright, bye-bye, everyone.
**Utkarsh** 59:36 Thank you all.

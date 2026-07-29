SIG: Arrow SIG
Date: 2026-07-28
Duration: 69 minutes
============================================================

## Zoom Recording Transcript

Joshua MacDonald 00:02:58 my machine is on the edge of crashing for being out of memory, because I'm writing code again.
So welcome, everybody. It could be a small meeting today. I have a feeling a bunch of folks are on vacation.
But a few of us are here.
Alright… Today is… Looks like a full agenda already.
Unless this was copied. No. Looks good.
Alright.
Laurent Querel 00:03:45 Hi, everyone. Sorry to be late.
Joshua MacDonald 00:03:49 Saw your name there, and didn't see you here. Very good.
Laurent Querel 00:03:53 Yeah, I prepared the document before, and Or in order to be played.
Joshua MacDonald 00:03:59 Great. I'm gonna add one for myself at the end. I guess we could get started.
I am… My machine is actually dying. I'm not sure that I should try and do this.
Laurent Querel 00:04:21 I can share if you want.
Joshua MacDonald 00:04:22 Unless I'm gonna have to reboot.
Laurent Querel 00:04:28 I'm not even sure… okay.
So… I guess you can see my screen.
Joshua MacDonald 00:04:36 Yes.
Laurent Querel 00:04:37 Okay.
Great. So, yes, we, we, we do the classic, the classic triage.
Joshua MacDonald 00:04:51 Triage, sure.
Laurent Querel 00:04:52 Yes, so we have, so those things are… Yeah, that's the new… The new entry.
into the GitHub issues.
That still need, triage lead discussion.
So I can go over them, and someone can change the status, maybe, because otherwise I'm sure that I will, I will definitely forget to do it.
So Phase 3, I think, is still, something where we need to discuss. We had a discussion this morning with Joshua.
We need to discuss that with, trust, so I will let… We left this, This entry is still, in this state.
We have this standardized request lifecycle matrix using active or in-flight.
And completed instruments, so… Very quickly, right now we have this, kind of pattern For some metrics, especially in the, in the receiver side.
And, so, it's not ideal because there is an overlap between started and completed.
So I was suggesting to… Move, to, something like… For example, receiver or TLP request active, so number of active requests Or in-flight requests.
And then the number of completed. So it's just, The same thing, except that the way that we cook them is slightly different, and because we are in the… In the middle of, stabilizing, the… The metric set and the corresponding attributes, especially with this effort that we… on which we are working now for two weeks.
the… the alien-based attribute. I think that could be, nice to… Can we think about that? So, Let me know if you disagree, agree.
Just a proposal.
Joshua MacDonald 00:07:07 Any comments?
I like this formulation.
Obviously we could, or not, maybe not obviously, we could compute the in-flight from subtracting.
Laurent Querel 00:07:20 Yeah.
Joshua MacDonald 00:07:21 started from completed, but that just makes everyone's life hard, and I think the goal with the metrics instrumentation library is to choose the instrument values that are most useful.
Indeed. Like, directly useful.
Laurent Querel 00:07:36 Yeah, that's the… one of the main motivations behind that.
Okay, so we consider that, We… we adopt that.
So then we have a collection of, Chanly issue related to the Kafka receiver, and there is this, Kafka receiver, Kafka exporter announcement.
It's all relative to the validation, so, As you know, we have, a beta alpha version.
of the KFK receiver exporter. It's not ready for production, and in order to reach this level, we have multiple things to… to check and to validate.
One is to make sure that, for example, the Kafka receiver is behaving well when there is a rebalance situation.
So, I think, yeah, the, It's all about that, making sure that we have the right test in place.
And, so Chanly, do you want… is Chan Ly with us first?
Chanly Ly 00:08:43 Yeah, I'm here.
Laurent Querel 00:08:44 Okay, great.
I remember that you… we discussed, and you'd like to discuss maybe about the extension system, or no. Maybe that's a second… a second discussion. Let's start with the cafe receiver enhancement and cafe exporter announcement.
Chanly Ly 00:09:03 Yeah, so these are basically just outlining, like, specific areas of focus that we should, test for the Kafka receiver and exporter, just to make sure they handle these, edge cases well.
Laurent Querel 00:09:15 Yeah, so the… all those sections correspond to the… the focus that you… yeah, basically the… Type of tests that you like to, to, To check with your evaluation framework.
for the receiver side, and I guess you have the same thing for the exporter, right?
Chanly Ly 00:09:34 Yeah.
Laurent Querel 00:09:37 Yeah, that makes entirely sense for me.
Excellent.
Joshua MacDonald 00:09:46 The comprehensive report.
Chanly Ly 00:09:50 of the country.
Laurent Querel 00:09:52 Okay, so I… No objection on my side.
The rest of the…
Joshua MacDonald 00:09:58 I think we can accept this? Very good.
Laurent Querel 00:10:00 Okay, great. John,
Aaron Marten 00:10:03 Chan Lee, did you want me to break that down into sub-issues?
Chanly Ly 00:10:08 I think I already started working on all those tests, but I wouldn't mind an additional eye on those, yeah.
Aaron Marten 00:10:17 No, no, sorry, I meant just, like, breaking down this one giant one on the Kafka exporter into a bunch of sub-issues.
Chanly Ly 00:10:23 Yeah, that would, that would help a lot.
Aaron Marten 00:10:26 I know it. Thanks.
Laurent Querel 00:10:28 Great, great. We can also…
Joshua MacDonald 00:10:30 add Chanley to the triage role, and then… or approver's role, and give him the power to do that himself.
Laurent Querel 00:10:36 I think that would be a good idea.
Joshua MacDonald 00:10:39 I think that actually might be easier, just to take that off of Aaron's plate and let Chanly manage those himself.
on the spot, I would be glad to promote you, Chanley, to any of either of those roles, if you're willing. It's sort of a workload, question.
Can take that offline.
Chanly Ly 00:10:58 How do you do that.
Laurent Querel 00:11:01 Okay, so… I will just skip this one for now, we'll go back there, but just to continue on you, Chan Li.
Can you introduce this, extension system for validation framework?
So I read most of it, I think it's a good idea, but I'd like you to present that properly.
Chanly Ly 00:11:20 This was just an idea I had for, the validation framework.
Or… I was mainly trying to think about, like, a way to test the Kafka receiver with how it interacts with the other components, and trying to extend that to, being able to use the validation framework for other types of, exporters and receivers that might require an, like, an external system, like a Kafka broker. So this is just an idea of, like, having… introducing, like, a… like, a trait that we can expose the, validation framework that other developers can, use and define to be able to use the validation framework to test their, components, meaning, like, the contribib nodes type stuff.
Laurent Querel 00:12:02 Yeah, and maybe, I remember reading the summary with the rational, My understanding is, right now.
The level of flexibility that was offered by the validation framework was relying on the test container, Vapor?
But there are situations where You'd like to… To write, validation… Script… let's say, scenarios that, rely on something that is not necessarily available as a container. And one example, I think that's what motivated This idea on your side was the fact that a Kafka broker… a mock Kafka broker exists.
That totally bypassed the need for a real Kafka broker, started with a container. That would be good enough and much faster for a set of scenarios, not everything.
But that is a set of us… a set of them. So the… That's why you want to introduce this, Extension system for the validation framework, right?
Chanly Ly 00:13:16 Yeah.
Laurent Querel 00:13:17 Yeah, okay.
And did you specify the bit the… because I stopped to read the, I think, close to there, in there, after that… oh, yes, there is the trade.
Yeah, so that's how you will add the extension.
Chanly Ly 00:13:52 Yeah, it's good to, like, be fleshed out more, but I was just trying to gauge an idea of whether this would be something we want to explore.
Laurent Querel 00:13:59 yeah, okay. So I think the, So, if that's the beginning of it, maybe you could, the next action will be to create maybe an RFC that will be more detailed.
And, and you could always have, maybe, A proof of concept in parallel to validate this, that some… some ideas that you could emit into the RFC.
But, personally, I like the idea.
what I see is here you explicitly add, an extension.
Which is different from the other type of extension we have in the system.
Where… what we do is, we have the… we use the LinkMe mechanism.
To discover automatically the available extension, and then we we, we instantiate them by name, and we provide their configuration.
It's working well when the configuration has to be provided Via, let's see, configuration file.
Because we… we don't really have access to… in fact, the user will not, recompile. In your case, it's, it could be different.
I think I… in fact, I think I like this approach for this type of extension.
It's probably the, more direct… Yeah, let's, I think let's, finalize the differential of that, but I like the, the direction, personally.
Any question or feedback on that?
Joshua MacDonald 00:15:57 I wonder if, like, it would just reduce confusion to call this something more like Harness, or, like, it's a… it's a… test harness.
plugin of some sort. I was thinking about the Go Collector has such a thing in its testbed, but I don't think it has a special name for it. It's sort of like, you expect to find, for every protocol that you implement, an adapter that takes the protocol you want to test and plug it into the validation framework.
So that you can test the exporter with a receiver, or the receiver with an exporter.
Chanly Ly 00:16:32 Yeah, that could work. I think I… yeah, I don't want to get, like, the naming confused between this extension system and what's available for the engine.
Joshua MacDonald 00:16:41 I was gonna add that, on our side, the Azure monitor exporter, which Gokhan wrote, we also encountered essentially wanting what you've described, wanting to be able to plug in a fake backend or a realistic backend for testing and validation purposes in cases where we don't have a proper receiver, I guess you'd say.
Laurent Querel 00:17:04 Yeah.
Yeah, and I think, Chanly you mentioned, I don't remember if it was Univer.
all the other monitoring, blah, but, I remember some argumentation, or some, yeah, You mentioned something like that, so…
Chanly Ly 00:17:22 I think… We'll.
Laurent Querel 00:17:25 Okay, sounds good. I think we could revise maybe the naming, and obviously, refining the trait and what needs to be exposed.
But, personally, I think it's, it's nice to have that.
Okay, so, the last one is, from SIGO. Do we have SIGO with us?
Joshua MacDonald 00:17:59 I don't see… Let's see, Joe, what do you… which… What are you, referring to?
Laurent Querel 00:18:08 I was talking about the structured security for RMS for DF&G.
Veli… I didn't read it, so I don't know… If we are not ready, we can always keep that for the next meeting.
Up to you.
Joshua MacDonald 00:18:28 I haven't read this one.
Laurent Querel 00:18:32 Okay, so I think we can just keep it for the next, the next meeting, have a, having a discussion with Siju, I'll take the time in between to read it.
Based on the discussion.
Joshua MacDonald 00:18:47 I don't remember what this is.
Laurent Querel 00:18:49 So many things happened in between. Please check if this is what you had in mind.
Okay, I will leave that open, and try to, to read that, This week.
Right now, I think we can just move to the… to the sale, the new sale, GitHub issues.
I think we did all the… Let me double check, yes, we did everything there.
Oh, no, we, we skipped this one.
Add durability idempotency keys, So, it's from Mike Sedon.
Do we have Mike with us today?
So it's about what exporter needs an identity assign?
Joshua MacDonald 00:19:57 I have seen this sort of request in the past.
Laurent Querel 00:20:00 Oh, no.
Joshua MacDonald 00:20:01 My last company, we really wanted to have such a thing as was called an idempotency key.
In cases of… To prevent double counting.
of a report. So, when you retry something, it'll have the same item potency key. You can then dedu… deduplicate it at your backend.
Laurent Querel 00:20:29 And, I'll… So, Aron, is Aaron with us today?
Aaron Marten 00:20:34 Yep.
Laurent Querel 00:20:35 I think, yes, Aaron. So, did you read this, Specific issue. I see your message there.
Aaron Marten 00:20:44 Yeah, so this is, this kind of relates a little bit to Quiver, but it's also kind of orthogoning to Quiver. So Quiver does have its own method of identifying bundles in a unique fashion within a given Quiver store, but we have unique Quiver stores that get created per core.
And so… but he's asking for a globally unique identifier.
Laurent Querel 00:21:11 I think when you say globally, not on… not only at the process level, but globally, globally. If you have a cluster of DFN gene.
On different machines, machine, that's also what… is looking for.
Aaron Marten 00:21:26 I believe so.
Laurent Querel 00:21:26 Globally at the… yeah, I believe, yeah.
Aaron Marten 00:21:29 Yep.
Laurent Querel 00:21:32 So, yeah, that needs to be something, ideally…
Joshua MacDonald 00:21:37 I believe… in the OpenTelemetry specification repo, a request for this at some point as well. It really… it's independent of OTel Arrow versus OTLP. It's sort of a request to have Something that… It's not really a resource level, it's sort of like a payload level, like.
deduplicator that people have asked for.
I'm sure we could go find that. I don't think it's specific to this group, though.
Laurent Querel 00:22:06 Could you, could you add that when,
Joshua MacDonald 00:22:10 I can do that.
Laurent Querel 00:22:12 Great.
Yeah.
I think that will be interesting, if we can find a way to do it without synchronization across server.
Joshua MacDonald 00:22:25 what I remember doing was to make a hash value of a deterministic subset that were identifying fields only in a certain order, and then, like, just make that be the value, but it felt like… It… it was not making my backend team happy at the time. I'm gonna go look up that issue.
Laurent Querel 00:22:45 Me too.
Thank you.
Okay, so, let's keep this one open for now, I think, and we will, we'll discuss it once, once we have, This additional information, so we can, we can make some decision.
Okay, great. Let's go to the STEM… lists.
Human readable from… for entities.
Oh, I think that's… so, Joshua, I think I understand what it was, but, I think that was, format for the entities themselves.
Knowing that those entities are hierarchical in our system.
Joshua MacDonald 00:23:41 I guess that's right.
Laurent Querel 00:23:43 I think we shouldn't keep that for… is it already done, or… I think we should remove the stale, at least, or consider that it's closed if it's effectively closed.
Joshua MacDonald 00:23:53 I can't remember… I can follow up if you'd like.
Laurent Querel 00:24:03 Yeah.
Joshua MacDonald 00:24:06 Yeah, I think we can keep it open, but it does need more detail, given that 6 months has passed, and I can't quite remember.
Laurent Querel 00:24:15 Okay, so I removed the trail, and I'll let you, conflict the… With more detail, finite processor add configurable overflow policy.
I think that one is for Lalit. I would not be surprised if we need to keep it.
Is Laurent with us today?
Joshua MacDonald 00:24:41 Yeah, let's keep that.
Laurent Querel 00:24:43 I think so, you know.
Joshua MacDonald 00:24:44 I can… I can ping him about it.
Laurent Querel 00:24:47 Okay.
The therapy attack loan to dispatch time, I think that's in the same… So we are.
Yeah, if you can also ask him the… The 1905.
Joshua MacDonald 00:25:08 190.
Laurent Querel 00:25:09 I'm saying, I'm pretty sure it's, still something we need to… to do.
In terms of improvement.
Querel processor or stateful options.
Joshua MacDonald 00:25:34 I wouldn't mind closing this. If anyone can make it… finds the issue themselves, they will reopen or find a new one.
Laurent Querel 00:25:42 Yeah.
Joshua MacDonald 00:25:43 It's… there's probably a comment in the code as well, and I don't know what I would recommend doing about it. There's this… Retry processor will not always work, requires some collaboration with the exporter, and there's something there about this.
Laurent Querel 00:26:01 So, in conclusion, you want to keep… you want to close it, or you… you want to close it until we have someone that.
Joshua MacDonald 00:26:06 Yeah, I want to close it, because it's not clear, and I'm not sure it's a real problem.
Thank you.
Laurent Querel 00:26:25 Rakuten… Panic value is less than produce value.
Whoa.
Jake Dern 00:26:59 Oh, this kind of rings a bell. I think I've seen this issue before.
Or… is this because they're running into the maximum size that we can represent for an ID?
Laurent Querel 00:27:10 At least there is this U16 that is going in this direction.
Yeah.
So, can I let you, check that, on your side, Jake, and, And, either complete the, providing, A more final direction.
conclusion on that?
Jake Dern 00:27:35 Yeah, let me take a look at it. I don't remember where we landed. I kind of thought we fixed this, but maybe it slipped through the cracks.
Laurent Querel 00:27:43 So I'll let you, either you keep it down so we can discuss it with your conclusion next week, or you remove the sale if it's already, fixed.
Jake Dern 00:27:55 Yep, I will do that.
Laurent Querel 00:27:59 Okay, combine attribute transformation, pipeline stage… Whoa.
I think this one needs to be… Yeah, I think, that's one of those, nice to have optimization that, Albert was, of sorts, at some point, so I think we need to keep it.
For now.
Okay, okay, all the other ones are the ones that we need to discuss.
Okay, so now go back to this… Agenda.
So I think we are… we already discussed the extension system for the validation framework, What, so there is… update on multi-tenancy. I think this one, it's important to discuss it.
So… Joshua, I'm suggesting the following. I will do a very quick update on this one.
Just to see if we have people in the… In the audience that are interested to… Collaborate with us.
And then you, and if we have enough time, we can talk about that in depth.
Okay, so, let's see… Yeah, that's the list. So, Drew… is Drew with us today?
It was not true.
Joshua MacDonald 00:29:44 He's not gonna be with us today.
Laurent Querel 00:29:46 Yeah, okay, that's what he thought. He was not sure… 20 minutes ago. So, so Drew created this list, basically to, to provide, an easy way to Determine the, the… what has been already achieved in terms of migration to this new album attribute instrumentation.
system. So we, as we can see, we… I already have a lot of merged PR.
Some of them are still work in progress.
So the… So we are looking for people to help us on that. Basically, it's… I think it'll feel like there is some… Usually, it's either Drew, myself, sometimes CJ, sometimes Joshua, and we are basically reviewing this kind of, PR, and the goal is to… leverage the… let's take an example to see something concrete. Let's say this one, for example.
I think that would be easier to show.
Oh… Yeah.
So… I think we don't need to look at the code, that will be enough. What we had initially, before we introduced the enum attribute.
was… One metric per combination of states.
Or signal. So we… in that case, what we had initially was something like a produce message, or produce logs.
Success tutor, something like that.
And then we… and then we had the same metric, but for metric, success, and so on, and we obviously multiply that by the number of type of outcome.
So, there is, the opposite of success, I don't remember how we name it, but, something like y'all.
So now that we introduced the ability to specify Alien-based attributes during the reporting of the corresponding metric.
We can simplify a lot the instrumentation and reduce the number of metrics.
That will require, basically, to do some kind of refactoring for every Basically, every, every, node listed here. So, if you are interested by working on that, it's not the sexiest work to do, but that will help.
Feel free to… To add your name here.
And, and open a PR.
Or open a PR directly, depending on how you work, and and then that will inform us that we don't need to focus on it. Otherwise, we… We try to take, one sometimes, and transforming it, at least you will go faster.
Who is more people?
Benny, question on that?
Joshua MacDonald 00:33:12 B.
I know that Drew was going to, was considering creating new issue, like, issues to do new first issue To make it appear that they're good.
Laurent Querel 00:33:21 To make that even more readable.
Joshua MacDonald 00:33:23 specific ones, but he wasn't sure whether it was worthwhile. In any case, we are aware that this is there, and anybody listening, these are good places to get involved.
Laurent Querel 00:33:33 Yeah.
And there are plenty of examples, so, you will see that it's usually very easy that the decision is more to Most of the time, the difficulty is to determine if the… The enum declarations are generic, and either already exist, and then you can reduce them, or if you have to introduce a new generic one.
Sometimes you just have to use an enum that is local to your node because it's too specific.
But, things like signal type, outcome are obviously generic, and there are a few other examples.
Okay.
I think we should…
Joshua MacDonald 00:34:16 We should pin this issue. My machine is still not responding properly, so I can't…
Laurent Querel 00:34:20 That's a good idea, dependency dashboard… I don't know if we can pick…
Joshua MacDonald 00:34:28 Go to the issue and pin it, I can't make mine…
Laurent Querel 00:34:32 Yeah, I was… I was just…
Joshua MacDonald 00:34:33 into Twitter.
Laurent Querel 00:34:34 To figure out if we can pin more than 3.
Let's see, I tried… I think it's there. PIN issue, yes, we can't.
Except if we do some,
Joshua MacDonald 00:34:47 Okay.
Laurent Querel 00:34:47 Some cleanup here. Lacky test, I think it's a report, we need to keep it. This one, we need to keep it. Dependency dashboard, what is this?
Joshua MacDonald 00:34:56 This is why we should create new issues.
Let's not worry about it now.
Laurent Querel 00:35:04 Yeah, yeah, I agree. Okay, so let's go with your, update on mute tenancy design.
Joshua MacDonald 00:35:10 Okay, let's see if I can get my machine to work through this. I'm gonna try and steal the share from you for a second.
Laurent Querel 00:35:15 Oh, okay, okay.
Joshua MacDonald 00:35:17 Here we go. So, the main thing I want to say here is, this document or set of documents now has become Oh, I'm sharing… which one am I sharing? Can you see multi.
Laurent Querel 00:35:33 It doesn't see super basic CPU memory limits, I don't know.
Joshua MacDonald 00:35:37 Okay, and you see the notes. Okay, good. The main thing I want to say is this document, which is actually four documents now, is too large, really, for anyone to review in a comprehensive way. And, what I'm finding is that I've written enough that no one wants to read it, which is, I think, okay.
what I plan to do, with the feedback I've received so far, is to begin implementing this in a priority order, so that we can see how it unfolds and, and actually be able to look at the first step as we evaluate this. So I wanted to kind of, really not encourage anyone to really read it, but to discuss it here and talk with me right now is a good thing that we can do. And so, I have linked to the document, and of course, it has if you've seen it already, then you might know it has a couple of diagrams. I've proposed something that I've already received feedback from Laurent, is little bit heavy weight. So what I want to do is step back a moment and say, I have to make priorities, and I'm trying to make priorities that everyone here will agree to.
And, the words that came out of our conversation earlier was that there's essentially a macro scale of tenant and a micro scale of tenant that are both present in this design.
Because we can see so many different ways of doing tenancy. And I think while the design can be complete and comprehensive, it's important that we start with a subset that's… that will deliver some value and lets us measure it and evaluate it. So, what I wanted to do was, not to show you this PR, and I have… But there are some basic ideas here. Like, you can see the diagram in front of us that's kind of talking about how we take tenant tokens from that… from an extension in the receiver and put them in the context so that you can use them anywhere for anything.
This is not a great diagram, but the concepts of sticking something in the context that's our tenant token is present.
And, so then, what I wanted to show was that I had created these diagrams that didn't make it into my document, and I'm just kind of clicking through them to see that, like.
when I think of multi-tenancy for our system, it's lots of different things. It's different users with different requirements, making different configurations.
And we have… and so now it's becoming clear that we have this macro scale of design and micro scale of design. And so I'm going to start with the macro scale, and I wanted to put this diagram up first. This is sort of, like.
one of the more simple arrangements that we can imagine from this design that I've written up, where there's a shared port and some shared receiver, which is going to be sending requests after identifying which token to different pipelines running on different threads. And the goal, when we think of the macro scale here is that we're not going to do fine-grained tracking of anything. We're really just going to route to these three pipelines, and if they block, they block, and that will cause back pressure to happen. I think… I guess the requirement that we have is that blocking will be independent somehow. When the… when the, and we have to figure out how to make the topic router non-blocking, for example.
I think it already is.
Laurent Querel 00:39:03 We could consider the durable processor in front of the… so on the right, core 1, core 2, that are assigned to a specific tenant.
If you put the durable processor, you basically solve your problem, I think.
Joshua MacDonald 00:39:16 So, putting the durable processor in a per-tenant configuration.
Laurent Querel 00:39:20 this, yeah.
Joshua MacDonald 00:39:21 Much of my document was aimed at saying a lot of our… a lot of our multi-tenancy problem is just configuration. You can give each tenant their own pipeline, for example, and that gives you a lot of control over multi-tenancy that's not… fine-grained, in other words, not microscale. I did look at how, you know, one of our end goals is to do a shuffle, and that could be shuffle by tenant, or shuffle by tenant and something else, like trace ID, or… metric name or something like that. That's definitely a lower priority, once we get the fine-grained stuff. I… this is a case that I'm not going to prioritize. This is, like, within a single pipeline, if you had fine-grained tenants, you might want to have different tenant limits, like saying, I want to have like, for each module in my system, I want to give each of them a bandwidth limit of 100 kilobytes per second, so that with 50 journal… with 50 SystemD modules, I never exceed 5 megabytes per second. That's because I gave each unit a limited amount. That's something that we should be able to do But it's micro scale, it's not macro scale.
And just to reinforce the thing I said about configuration, the idea that Sometimes we're going to configure a dedicated port and a dedicated thread for each tenant. That's totally, like, perfect isolation. It's not even a multi-tenancy solution, it's just configuration at that level. Or you could decide to have one pipeline open three ports. There's just, like, there's lots of ways to assemble pieces of our of our data flow engine.
I just wanted to show that I had these documents, but I didn't… I didn't want to keep adding to my… my… my set, and I really want to just begin implementing and showing you what I have. So this is open for your review, but I'm not sure that it's going to be reviewable yet.
And then I wanted to start in a very concrete way. I know that we have folks on the call, especially wanted to bring in Gokhan and ask him to speak. The PR here that I've got linked in the notes, I think it's still in draft, it may not be. This is a draft where we begin looking at how would we concretely Or at least this… this forced me to ask the question he and I were discussing it. How would you use an auth extension as the source of multi-tenancy information, at least that's part of what's present here. And I think that that's what I want to start with.
This is like a scenario where the receiver is going to take the headers, ask them to the auth extension, the auth extension will do whatever it does, the auth extension will return context, which we will put in the context of the request.
And that context will then contain tenant tokens, is what we're calling them.
that will identify the tenant in the request. It will have come from the auth extension, which we can trust. So we're trying to get to the point where we can receive a request, that we can call the auth extension, get the auth, as well as context about the auth.
and then use that as the tenant token, and then use that to route. So this is the sort of first extractor I want to implement.
is the extension an auth extension? Gokhan, please.
Gokhan Uslu 00:42:33 So, my thoughts and my questioning has been around so first of all.
there's a distinguisher of, you know, the tenant. There's going to be a way to distinguish tenant.
And a multi-tenancy probably could be done without any authentication, so there is going to be a distinguisher somewhat.
the visa without authentication, this is what I'm thinking.
And afterwards, the auth model should support a more trusted distinguisher, meaning that the distinguisher should be coming from authentication evaluation.
And how we should connect with the tenant distinguisher is… well, how I'm, like, is the thing that I'm questioning. So, how are we going to distinguish a tenant At the multi-tenancy level, and how authentication can provide it In the secure format, or secure version of that identification?
And the other is probably how we can make it so that the authorization… so authentication will identify the tenant.
But the authorization would also probably need to be configured at per tenant level or not, so how that authorization decision, maybe, is resulting, and how, like, that the resulting identity or context or whatever.
information, like, claim the sitter, we put there. Is there… how we can standardize, maybe, like, some tenant information being there? You know, I'm just trying to understand, the multi-tenancy part of it.
Because I'm not able to fully answer how authentication could, you know, connect to it, basically.
Laurent Querel 00:44:22 I can provide some feedback on my side, probably incomplete, but, So first, I really like the idea of separating authentication and, retinency identification, even if the… the multi-tenancy identification could come from authentication sometimes. It will not be always the case.
We have a… Classic scenarios, let's say you have, An observability SaaS solution.
Obviously, in that case, They will have customers.
And, they… they could, I mean, they could use such system to… For each of their customers.
make that a tenant, and coming with different, policies pertinent. And that's what we want to authorize. In that case, authorization and tenancy are connected together.
No… You have, a big enterprise.
They are not accepting external telemetry, it's more for internal usage.
In that case, the Nancy could… could come from different… I mean, so first, maybe they don't have maintenance in that case, or if they have, maybe they are related to project or team.
So it's not necessarily… it could be also attached to authorization, but not necessarily. Maybe they just have an header into the… HTTP header, either in the GFC or the… whatever is the… the protocol, and in that case, the tenant ID can come from a different place. Or it could be the combination of a service name and maybe something else.
And that's why, also, we have this tenant token mechanism that Joshua introduced, because that gives you a way to basically define what is a tenant ID, or what is a tenant token. It's not necessarily just one entry, it could be a combination of multiple.
So, long answer, but for me, I think, yeah, we could have multiple providers of tenant token, and the authentication could be one.
Now, how we articulate that? Do we use the capability system?
that, could be supported by, by the extensions. I could be a good… a good idea to do that. So we could have extensions that are bus… authentication provider and tenant token provider, and we could have other extensions that are only The non-token provided.
I think the… the extension mechanism you put in place, again, support that.
So I will, I think, I think it could be a good idea to, to follow this pattern, that, Is it, clear enough?
Joshua MacDonald 00:47:24 I believe so.
Gokhan Uslu 00:47:26 that I was thinking is that… I mean, before without authentication, a tenant will be identified by an identity, whatever that moniker, something like that. So, I'm guessing… authentication can extract… during the time of authentication, you can extract that moniker and then be able to put it into the request context, because it's attached to the request, and I don't know, like, how those things tie to each other, but… That, whatever that moniker is, it is orthogonal to authentication or authorization.
And that process can supply that… extract and supply that moniker, and then that moniker could be used in the rest of the pipeline.
Or it could be applied without authentication, could be just come from a header value. But I'm guessing, like, maybe we should just figure out how to extract it, and then how to then provide it to the request context.
and then the rest is, I guess, up to what multi-tenancy wants to address, because we just try to find who the tenant is, and then put it into that Request context created.
Joshua MacDonald 00:48:39 Well, everything you both are saying sounds right to me. I think we're on the same page, basically. I was using, in my latest draft, the word extractor, so to take… some context and produce one key value of tenant information is the… is called an extraction or extractor. So I could imagine an extractor capability, basically saying this is for a protocol that, like, is very specialized. You may not… it may not work in every receiver, but this is how you do an extractor for something specific. And it's… it's, like, the extension mechanism can handle that.
the… the… and I think this is what I'm saying, I plan to just begin implementing it, because I think I need to show all of the stakeholders here that the approach is flexible enough.
Just to be clear about the… there seems to be two topics that I see coming up again and again with this multi-tenancy topic… tenant token idea, is that we… we know… we talk about extracting tenant tokens from headers, or from auth context, or from connection state, or from… lots of different other locations, I think.
And then there's going to be some sort of standardization that we… that we have, where most of the receivers deal with it the same way through… policies. And, what we're saying is that… that for one thing you can do… one thing you can do with these tenant tokens is Describe… one thing you can do with these extractors is describe tenant tokens.
The other thing you can do is use the tenant tokens as a conditional in your configuration somehow. And that's where I had proposed a framework for using rate limiters and semaphores, basically, or resource limiters, that could be, like, fine-grained.
Those were applications of the tenant token that we can install as, like, a processor, just like, here's a rate limiter processor, or here's a memory limiter processor, or something like that.
But what Gokhan's also stated, and I think I heard echoed by Laurent, is that when you have these tenant tokens, and you have a component, like, say, batch processor to keep it simple, you also may want to say, okay, given the tenant token that arrives, I would like to find specific configuration for this tenant.
which is not a limiter, it's any other application. So it's like, because I am batching, I want to find tenant-specific batching. And in Gokhan's case, it's because I am authenticating, I need tenant-specific authentication instructions. So you might use a first level of extractor from the header to get a raw tenant.
Claim, saying this tenant claims they are this… this request claims it is this tenant from an unauthenticated header.
Now, I'm going to take that unauthenticated header, look it up, use it to extract the first tenant token, which is find my next configuration. So using my first untrusted token, I will then look up the authentication configuration for the claimed tenant. Now I have specific configuration. So it's like tenant tokens are also used to look up Specific configuration anywhere, really.
And I see those as two applications that both contribute to multi-tenancy.
Laurent Querel 00:52:03 Yeah, this is the concept of tenant-driven policies.
So, yeah, we could be… let me summarize what I understood, We… in a scenario where we discover the tenant token from authorization. So we have first We… we… we asked the extension to validate due to… Yeah, the, the user, huh?
And, and we gate some kind of, From there, when it's validated, we get a way to get a tenant token. And from this tenant token, we can get, for example, the policies It's not… obviously, it's… in some specific case, sometimes it's easier than that, but we can get the policies that are attached to this specific tenant, and those policies will Will be used to determine What are, what is authorized for this specific, tenant?
And that will traverse the system.
And will be enforced along the way, right? That's what you got in mind?
Wicked.
Joshua MacDonald 00:53:12 That's pretty close, that sounds about right, yeah. And I think that… I don't believe I can get much clearer than that without actually implementing it and showing it to you, so that's what I plan to do.
Laurent Querel 00:53:22 That makes sense for me.
Joshua MacDonald 00:53:25 Or first round, at least, and we'll all reconvene and take a look.
Laurent Querel 00:53:29 Yeah, but I guess this kind of… advanced approach will be, will… yeah, that's not the first thing that we will achieve first.
Joshua MacDonald 00:53:40 Right.
Laurent Querel 00:53:41 macro, the macro approach that you, you described.
We'll be, most likely the first, initial.
Joshua MacDonald 00:53:50 Yeah, I think we want to do… I think I want a minimum, like, proof of concept that takes, like, a header and puts it into… we already have transport headers in the request context, but I mean to say, that there is a… the framework that I've described has a level of compilation, where you're saying, I'm going to have a condition which is routing by tenant, and I'm going to compute my tenant token so that I can do the computation once, and then not have to evaluate it in my… my router, for example. So, this first proof of concept is I take some context, I extract a token, I can use… I put that token in the context, and I can use it to do some routing. That's, like, first deliverable, and if we like that, we'll keep moving. Otherwise, we'll refine.
Laurent Querel 00:54:40 Okay, great.
We have 7 minutes left. I think I can, very briefly talk about the… The processor exporter… so, let's see, I can share my screen… And then go to… yeah, so… the original idea I think I talked about that briefly last week.
It was about introducing an active formative exporter.
First, to basically replicate what we have with the admin endpoint, the slash metric endpoint.
That currently, so that we have this metric registry.
Connected to this internal telemetry system that now is able to process metrics and logs, and we can export all the internal telemetry now with the firm protocol, except with the primitives, the pull, primitives endpoint.
the pool bed for the primary centers. So right now, we are still… Using, like, A secondary pass, that duplicate the matrix and expose that independently of the internal telemetry system.
So the goal here is to… create a first version of a promise exporter that will be, limited First to single instance pipelines.
Because there is a concept of state, obviously, into the… this kind of pool-based Prometheus exporter. So, let's start with something simple. We… we, we introduce, a limit to this Prometheus exporter. It could not be deployed on multiple cores, just a single core.
But that could be good enough, anyway, for the internal telemetry system.
And, the… the second idea is… we could decompose even more the Prometris Exporter, and that's what I'd like to introduce.
We could, basically make the Prometus exporter dumped, and… and dumped in, and this, permitous exporter will just expect cumulative metrics.
everything that is not cumulative is not trying to be smart. It's just keeping track of the cumulative, keep them in a state with some garbage collecting mechanism, just to to get rid of the old cumulative metrics that have not been updated recently. And when there is an external request, we just get this, Internal state, and we expose, basically, the corresponding matrix.
The transformation delta to… to cumulative, instead of making it into the previous exporter.
I think it could be a good idea to introduce a temporality processor very close to what exists, I think it's… I put that somewhere… There is a delta to cumulative processor that exists in control.
And so what I'm suggesting is to generalize that.
to have a temporality processor that gives a user And that could be, Ultimately done, not only for the internal telemetry system, but in general.
But we'll start with, again, a first version that will be limited to one One instance of that per pipeline.
And, and we'll basically, offer a way to… So it will be… it will act like a pass-through for any signal that are not metric.
And also as a pass-through for any, matrix that are not the target of this, temporal processor. So, let's say you are configured in a… You want to get cumulative, so everything that is, data will be We will be, we'll participate to the state.
And we will expose cumulative. Everything that was already cumulative will just, traverse the… The processor without any, transformation.
So, having, that… that being… let's say we have that, it means that we will be able to have a Prometheus exporter that will be the combination of historicity processor and, the Prometus exporter.
So that's the proposal. I could provide more detail, but I just provided here the… so we have this concept of flow memory matrix.
So it's, something I discovered, via Joshua recently.
And you don't know that, that was, that this thing had a name inside, open telemetry, so it's something that exists for client SDK.
In order to minimize the… the amount of state, to keep for metrics.
And, and that's more or less what we have in our own system.
And then, like I said, exposing Prometus Endpoint will be the culmination of these two.
So it's, again, a composed approach where we combine this Prometus exporter with the processor comparability, and we end up with something that is doing what we want.
Excuse me.
Joshua MacDonald 01:00:36 Very good.
We're out of time, so not much time left, but I would comment that I'm in discussions with a sub-team here that is interested in similar stuff.
There are probably a few subparts here, but as you mentioned, doing this for an out-of-process stream of metrics would be also useful, although that can expand into a very hard problem. But in a slightly more general case, we have a definite user base where We want to collect metric events from on the host, and then aggregate them And also load balance them, so shuffling is in scope here.
But being able to, shuffle, load balance, and then do temporality correction, or adjustments in a… scalable pipeline, and then push the data would actually be useful. So I'm bringing some people in that will probably take up this, at least be interested in that.
A Prometheus person would probably say, hey, I want my Prometheus Remote Right protocol, which is a separate matter, and I don't have a feeling about.
Whether anyone's gonna ask for that.
Laurent Querel 01:01:49 Yeah, we could imagine that the Prometrus exporter at some point is… is, That's a good question. Do we have to define two exporter, one for the pool-based Prometheus exporter, and another one for the push-based?
Joshua MacDonald 01:02:05 That's sort of the way it goes.
Laurent Querel 01:02:08 Okay, so that maybe that means that we need to… To, think about a better name,
Joshua MacDonald 01:02:15 the Go Collector calls it Prometheus for what you've got in front of us. The pull-based exporter is called Prometheus, and the push-based is called Prometheus Remote, right?
Laurent Querel 01:02:24 Oh, okay, okay. We can follow maybe the same pattern, I don't know.
Yeah.
Joshua MacDonald 01:02:29 It does round trip with OTAP, or OTLP, although, and this is another note that you may care about. I've mentioned it in the, Slack recently, how, we have this metric metadata type in OpenTelemetry that was recently added, recent being the last 18 months, and it… we do not have it in OTAP, and If you try to do Prometheus Remote Write, you will eventually notice this feature.
Laurent Querel 01:02:55 Okay.
Joshua MacDonald 01:02:56 Andres has his hand. I don't know, I think we're out of time, but if, Andres, if you'd like to speak, I'm glad to hear.
Andres Borja 01:03:01 Oh, I was just trying to remember, I think the Prometheus push is OTLP recently, right?
Joshua MacDonald 01:03:09 Yes, Prometheus services have begun to accept OTLP, that is true. Prometheus itself has, that is also true. I don't know that that means Prometheus Remote doesn't matter.
I think the Prometheus would still prefer to export its own format to backends that are Prometheus-friendly. What they mean to do is accept OpenTelemetry SDKs pushing them data.
Andres Borja 01:03:35 Yeah, I think that the bull one is just easy, you know? That's why it's so useful.
Joshua MacDonald 01:03:41 It's treating the data flow engine like a Prometheus client, which was the first stated use here, is to do ITS, which is totally making sense. It's really… usually when someone.
Laurent Querel 01:03:51 Yes.
Joshua MacDonald 01:03:52 Methos, right, what they mean is we don't want open telemetry, and I don't think we should go that far.
Andres Borja 01:03:57 And the question is, once this is in place, Are we planning to remove the admin console?
Laurent Querel 01:04:08 Yeah, for sure, yes. Bmsr, yes.
Joshua MacDonald 01:04:12 Prometheus page, I think you mean.
Laurent Querel 01:04:15 Yes, the…
Andres Borja 01:04:16 Yeah, for example, you… Endpoint that we have there that is kind of, like, not in the best place to be.
Laurent Querel 01:04:24 I agree. Yeah, definitely, the goal is to be in a position where everything that is related to internal telemetry is handled by the ITS system.
And and then we can get rid of the… this slash metric endpoint, it will be still there, the slash metric endpoint could be exposed by the export… the… the Prometheus exporter.
But it will not be served by the admin. I think the admin needs to be only the… the… the admin API, To reconfigure the… the pipelines.
And I even think that the slash status could be something, that the ITS could expose also at some point.
That's not, part of the promoter use effort, but, we… If we start to have, To maintain states based on internal telemetry, we… I think that's the… for me, the beauty of reusing the… our own pipeline system to also expose the internal telemetry. That forced us to think about This kind of processors and exporters that, can accumulate states, that makes sense in some scenarios, like, like internal telemetry, and where you can describe, oh, we have a set of Let's say, event, Talking about the slash statues, for example.
The slash status is based on the observation of internal event, or internal system event.
And then we maintain a state to describe the status of every pipeline, every group, and so on.
And sometimes we need some rules to determine, if something is, readily or the readily and, like, the, endpoints are based on this, state that we we maintain. If we are able to create a pipeline to describe those configurations, I think that will be nice.
And that's my ultimate goal, to also migrate the… slash status, and potentially the slash, LiveZ release, also there.
Joshua MacDonald 01:06:48 Yes.
Andres Borja 01:06:49 I, I know you…
Joshua MacDonald 01:06:50 I know.
Andres Borja 01:06:51 I know it's a little late, but I'm just curious. So, the exporter, you know, the push, that is the one that I get, or the pool, that is the one that I guess we are talking.
it still requires some state, so I like the idea of having the processor, I think that is super clever, but the exporter will need some sort of anyway, so…
Laurent Querel 01:07:15 Yeah, not basic ones. It will be just the… that's why I was, qualifying this Prometus Exporter dump, because it will… it will not try to do any kind of computation. It will just keep Track of the cumulative metrics.
Ignore all the rest.
And, so, yes, there is a state.
But, nothing complex to maintain. And the split is there to… make, To be able to use this temporality computation in other places.
And, so if we imagine you have an exporter that is not exposing That need also, cumulative information.
Then this thing will be already there, they can just combine their exporter with this processor, temporality processor, and that will also simplify their, their work, and maybe this specific exporter will not need to To keep the site, because maybe they will just send the community outside.
Because it's not a pool-based approach.
Let's say a push.
In that case, the top IBT processor will be good enough.
Andres Borja 01:08:38 Got it. So the exporter, in summary, the Prometes exporter will just keep the state of the latest Metric values that they.
Laurent Querel 01:08:47 Yes, yeah.
Andres Borja 01:08:48 That's cool.
Laurent Querel 01:08:49 Yes.
Andres Borja 01:08:49 Yup.
Joshua MacDonald 01:08:51 And that's very much like what the Go Collector's Prometheus Exporter does as well. Sounds good to me.
Put them on disk and serve them from another exporter, anyway. Very good.
Well…
Laurent Querel 01:09:03 rates.
Joshua MacDonald 01:09:03 you all.
Laurent Querel 01:09:05 Okay, thank you, have a good, rick…
Andres Borja 01:09:08 Thank you.
Gokhan Uslu 01:09:10 Bye.

SIG: OpenTelemetry .Net Auto Instrumentation SIG
Date: 2026-11-18
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

**eftiquar** 00:42 Yeah, let's see…
**Alexey Pukhov** 00:49 Ashed cars.
**eftiquar** 00:50 Hey, how are you?
**Alexey Pukhov** 00:51 I'm good, how about you?
**eftiquar** 00:54 All good, all good.
The weather.
**Alexey Pukhov** 01:02 Oh yeah, the weather here in Bay Area is… He's not dry.
**eftiquar** 01:09 Yeah, same here. It's, wet, windy.
Rhynier?
**Rhynier Myburgh** 01:22 Good morning.
**eftiquar** 01:24 Hi.
Morning, how's the weather treating you Rhynier today? Over here, it's wet, windy.
**Rhynier Myburgh** 01:32 Yes, I mean, the wet's fine, though. The windy is the big thing, making sure that, Nothing goes wrong.
**eftiquar** 01:40 Yeah, hopefully.
**Rhynier Myburgh** 01:41 And you guys? A lot of wind there?
**eftiquar** 01:44 Yes, it's a steady wind. It's not too much, but…
**Rhynier Myburgh** 01:48 Dope.
**eftiquar** 01:49 I haven't seen any.
Trees falling, or such disruptions?
**Rhynier Myburgh** 01:55 Okay.
**Alexey Pukhov** 01:56 Yeah, I don't… see any wind here in San Francisco, but the rain is pretty heavy.
**eftiquar** 02:02 Oh, yeah, yeah.
San Francisco beginning.
**Rhynier Myburgh** 02:05 We have a wind advisory for Sacramento, which means it's… The kind of wind that'll blow over trees, so…
**Alexey Pukhov** 02:13 Oh, yeah, that's bad.
**eftiquar** 02:19 This is just a start, right? This year's El Nino is predicted to be one of the stronger El Ninos we have had.
Inc.
**Alexey Pukhov** 02:28 Hmm.
You know, last time in 2022, when there was heavy rains in San Francisco, people were… Surfboarding on the streets.
**eftiquar** 02:41 They say that the Pacific is also getting very violent. Oh, yeah. Tall waves crashing.
**Alexey Pukhov** 02:49 The king turt.
Yeah.
The pictures and videos are wild.
**eftiquar** 02:56 Yeah.
**Alexey Pukhov** 02:58 I'm glad I don't live on the coast.
**eftiquar** 03:02 Where are you from, though?
**Alexey Pukhov** 03:04 I'm in, well, kind of pretty far. It's Civic Center in San Francisco, so it's, like…
**eftiquar** 03:13 pretty good.
**Alexey Pukhov** 03:14 It's… it's not a… it's not a heel.
But, I don't think we will ever be… impacted by the king ties, or anything.
**eftiquar** 03:27 Yeah, I will.
They said that 40 feet tall waves were crashing in.
It's San Francisco Bay.
**Alexey Pukhov** 03:38 Oh, yeah.
Now, if you go to the bay, like, in Berkadero, where the bay is.
You can see the tides are actually entering the road.
**eftiquar** 03:50 Oh, really?
**Alexey Pukhov** 03:51 Yeah, there it is.
**eftiquar** 03:52 Ferry Plaza? Is it all washed up?
**Alexey Pukhov** 03:56 I mean, not entirely, but, like, it's kind of coming.
**eftiquar** 04:00 Hmm.
**Alexey Pukhov** 04:01 But, I mean, again, San Francisco is not that usually impacted, like, the area surrounded.
Like, the south… the north part, The roads can be flooded.
**eftiquar** 04:15 Okay.
**Alexey Pukhov** 04:21 Matthew.
**Matthew Hensley (Raintank, Inc. – Grafana Labs)** 04:24 Hello.
**eftiquar** 04:33 Is it…
**Zach Montoya** 04:35 Hey folks!
Sorry for, I had a meeting to go over.
**Alexey Pukhov** 04:39 Oh, no worries.
How are you doing?
**Zach Montoya** 04:45 Pretty good. How about you guys?
**Alexey Pukhov** 04:47 Good.
**Zach Montoya** 04:50 November is, we're already halfway through November, which is actually crazy.
**Alexey Pukhov** 04:56 Yeah.
Time flies.
**Zach Montoya** 05:01 And then the holidays are coming up, so… Let's see what all we can ship before then.
**Alexey Pukhov** 05:07 Okay.
Alright.
**Zach Montoya** 05:13 Let me… let me share, and then we can, get started.
I know that Pietra had a couple of items that he wanted to address,
**Alexey Pukhov** 05:24 Yeah, unfortunately, he cannot join.
**Zach Montoya** 05:27 Yeah.
**Alexey Pukhov** 05:27 So he left them in the… Note.
**Zach Montoya** 05:31 Yeah.
Yeah.
So let's get started with those, and then if any other topics you guys want to discuss, we can… follow up with that. So the first thing is we have, so for .NET 11, that, shipped, and so we want to publish a new release, I'm not sure if our CI is already updated to the GA release of the SDK, but We want to make sure we publish, a new package for that.
Any blockers? I'm not sure if we have any blockers. We already got in the runtime async support… this one… yeah, this would be nice to have, for sure.
I suppose we have time to… to include that.
from your all… all your perspective, is there any other work that you see as blocking us from publishing a release for .NET 11 support?
**eftiquar** 06:40 No, I think I'm just… Unbelievable.
**Alexey Pukhov** 06:43 Yeah, I think we should be good. We fixed the assembly resolution, we fixed the native.
Rewrite… And the tests are passing.
**Zach Montoya** 07:10 Okay, yeah, I also don't… I'm not aware of any other, anything blocking there.
So, yeah, I think we're in shape for… to cut a release. We'll see if we can merge this first. I'll give this review after the meeting, but should be able to take that pretty easily.
Okay, cool. And then for maintainers, yeah, just a little announcement that there's a new channel. So we now have, like, a good contact with a GC liaison, so, we have a kind of direct line to… to hotel leadership, so we can raise any issues, if there's anything that you guys, feel that we need to address or need support with, then… You can feel free to let us know, and then we can… Reach out to the GC liaison that we have.
Yeah.
Cool. Any other topics before we go through the regular agenda?
**eftiquar** 08:06 No, all good.
**Zach Montoya** 08:07 Okay, let's do it.
So, open pull requests… So we've got a couple of bumps… dependencies… There's the Validate the Profiler, that was follow-up from previous PR.
There's one about skipping some instrumentation.
Not sure if anyone has taken a look at this yet or not.
But, hey, first-time contributor, that's nice.
Okay.
Catcher's left some comments, okay, alright.
Not sure if there's anything else at the moment to kind of dive into there.
And then we just have a couple more that have been open for a bit. None of these are really critical, as far as I know.
So, unless you guys want to dive into any… are there any that you guys want to, Dive into while we're all on the call?
Oh, Matt, I also noticed that you had your PR here. Is that… is there any issues, or do you need any support from us?
**Matthew Hensley (Raintank, Inc. – Grafana Labs)** 09:28 No, I, a little bit ago, pushed the, What might be the last set of changes?
**Zach Montoya** 09:35 Okay.
**Matthew Hensley (Raintank, Inc. – Grafana Labs)** 09:36 Addressing the feedback. I was at KubeCon unexpectedly last week, so…
**Zach Montoya** 09:40 Oh, that's nice.
That's cool. Did you meet any other, of the SIG members, either here or .NET?
**Matthew Hensley (Raintank, Inc. – Grafana Labs)** 09:49 Not really. I spent most of the week working the booth, so…
**Zach Montoya** 09:54 Nice.
Cool. Alright, well, let us know if you… Need further review or anything here. Looks like we have a couple of… Approvals, some comments, so yeah, let us know if there's anything blocking.
**Matthew Hensley (Raintank, Inc. – Grafana Labs)** 10:10 I think… All the feedback should be accounted for, minus the two comments that said they need to be done in a follow-up.
**Zach Montoya** 10:19 Sure.
**Matthew Hensley (Raintank, Inc. – Grafana Labs)** 10:20 So… Okay.
**Zach Montoya** 10:21 Great.
Sounds good.
Alright, any other PRs?
That you guys want to discuss right now?
Alright, I'll take that as a no.
**eftiquar** 10:41 Nope.
**Zach Montoya** 10:42 Cool.
Let's see… new issues… drop supports… That framework 462, oh, I see, okay.
Yeah, there's some .NET Framework supports… Let's just update this.
The general policy, though, is that we are, Just making sure we update and, publish our packages to support, supported runtimes, so that's what this is about.
Keep an eye on that.
And I think this one… This Adonet one is the one from the, the first-time contributor.
Creating a bug report, and then trying to resolve it with… this, the PR.
I haven't taken a look at this, yet, so, If we need to, we can follow up here to make sure that the PR is solving a problem that we want to solve.
**eftiquar** 11:46 Right.
**Zach Montoya** 11:47 But I've had not… I've not had time to take a look at this yet.
So, we got the… .NET Framework, the ADONET one… And then we have a couple of these ones that Piotr opened.
These ones seem just like some small bug fixes.
And then we have the support for, for runtime async methods.
I'm not sure if you guys were aware of this, but we have one limitation right now, which is… in our on method end… the handler that we add to the end of methods in order to, like, close out the activities, we can, if we want to.
Write an async handler so that we can run, an async code path, like, if we wanted to await some sort of, like, dispose async, or we needed to… Do, like, a… some sort of, like, send async.
So, we have the capability to do this with our rewriting, we don't actually use it anywhere yet, but the problem is that capability does not work with runtime async, so that's what this.
**eftiquar** 13:01 The smoke.
**Zach Montoya** 13:01 she was addressing.
**eftiquar** 13:04 So, pre-runtime async, is that working?
**Zach Montoya** 13:08 Yes.
**eftiquar** 13:09 Okay.
**Zach Montoya** 13:09 Yeah, so we can basically, instead of writing asynchronous, method end, if we describe it with an async, or we describe the… the callback or the handler with, you know, a task and write async code. That would work, previously, but it doesn't work on runtime async methods. Or, sorry, it doesn't work when we, our library.
It's compiled as runtime async.
**eftiquar** 13:37 Oh…
**Zach Montoya** 13:39 So, there's no issue at the moment, because we're not doing this.
**Alexey Pukhov** 13:45 Is it related to how the runtime async methods are implemented in latest .NET runtimes?
Like, especially the engine of those methods, and how they decided to move everything to native.
**eftiquar** 13:57 Yeah, the return value, generally.
**Alexey Pukhov** 13:59 value, and…
**Zach Montoya** 14:01 Yeah, because I think it's more an issue of, like, we… just like we had to update our bytecode, the code that we emit, in order to satisfy.
**Alexey Pukhov** 14:10 Satisfied.
**Zach Montoya** 14:11 That, the way that we Either set up our handler, or we have a, like, a continuation class that handles, sort of, like, invoking these handlers. Part of that on our side is, just not… not compatible yet.
Cause we have, like… Continuation…
**Alexey Pukhov** 14:35 Oh yeah, the previous async methods, like an older… I mean, not older runtime, but pre-11 runtime worked just differently.
**Zach Montoya** 14:45 Yeah, so, like, this one, if we have a… We run the handler as a continuation when we handle async… when we're instrumenting an async method. And then, so we set a continuation For… to call back our, like, end handler.
So we execute this, and I think that some machinery here just isn't compatible yet.
So, there's a whole thing describing that, but currently, this isn't blocking us, because we don't actually author any of our end method handlers with async await, and we also don't, compile our library with runtime async.
But eventually, this…
**Alexey Pukhov** 15:32 It'll happen.
Hmm.
**Zach Montoya** 15:34 Yeah.
So… Not urgent, but if you guys have any ideas, or feel like tackling this, by all means.
**eftiquar** 15:45 We will have to do it eventually.
**Alexey Pukhov** 15:47 Yeah.
**Zach Montoya** 15:48 Yeah. I mean, we… to this point, we actually still don't have any instrumentations that we are writing any async, handlers there, so… It's still, like, yeah, eventually we will… we will compile this as a runtime async library.
But, yeah, we still don't actually have any async code, so it still wouldn't bite us until we introduce something like that.
In the, like, Datadog repo, there's only a handful of them where it's, like, awaiting Like, flushing some buffers.
And so, like, that's where it would blow up.
**eftiquar** 16:26 Right.
**Zach Montoya** 16:31 So yeah, and so these are all just hardening things, so… I don't think we have any particular milestones at all, but, these are some… Some good, hardening issues for us to address.
For now…
**eftiquar** 16:53 Yeah, I reviewed that the profile capture WorkVenta for, yeah, that one, because, It's okay for now, but we need to create a follow-up request. So, I posted my review feedback on this one.
**Zach Montoya** 17:06 Okay.
Okay, cool.
See?
I think we're good on that. I haven't moved any of these to any milestones yet, the Met's immediate thing will be for the .NET 11 support, and publishing something new, publish a new, release, but for these ones, they're kind of open-ended, and so I haven't put anything here.
Moving on to discussions… none.
Issues that should be assigned a project.
What milestones are we even at? This seems to be updated.
Okay.
Oh, we have… I didn't realize this, we have one for polyfill, argument, null.
Throw if null for .NET Framework.
Oh, okay, this seems like follow-up then.
Okay.
Let… I'm actually gonna move this one to the next milestone.
Oh.
Cool.
So, once we support .NET 11, we'll just drop these, and then we should be able to implement this.
And… So I don't see anything else.
For the next one, just this one right now.
So I guess we're good on tracking that. The project board, I don't really think there's any updates at the moment. I love support in progress.
Let's see if there's anything… This might already be completed.
Okay. Yeah, we can just, close this once we publish the new release.
The Kafka and the IBMQ, those ones have been sitting.
Haven't had time to look into this.
**eftiquar** 19:31 We did give them feedback on that IBM M-Cube thing, I'm not sure if the… contributor… Wants to follow up on the suggestions?
**Zach Montoya** 19:45 Okay, is it this one that was closed, or… So this one was closed.
Maybe this isn't the most recent one.
Oh, close is stale…
**eftiquar** 19:58 Feel free to… oh, okay. Yeah, this is the feedback that I had given September 29th.
**Zach Montoya** 20:05 Okay.
**eftiquar** 20:06 There are some items on this that will benefit us.
**Zach Montoya** 20:12 Was it changes to, like, the… did it update our, like, how we do some instrumentation?
**eftiquar** 20:18 Yeah, so there is some gap, especially on the inherited methods, how we parse the.
**Zach Montoya** 20:25 Oh, I see.
**eftiquar** 20:26 RTMS chair, which is… missing infrastructure in our machine. I mean, that's what My Carmen pointed out. So, one PR, that is generic, and then build the IBM-specific feature on top of that.
**Zach Montoya** 20:39 I see.
Yeah, because here, this is where we actually start looking at the hierarchy.
**eftiquar** 20:45 Yes.
**Zach Montoya** 20:47 Okay.
**eftiquar** 20:49 So this PR is doing more than just support IBM. It is building some common infrastructure, and on the back of that, it is doing the IBM work.
The comment was to split that.
**Zach Montoya** 21:01 Got it, okay.
**eftiquar** 21:01 Oops.
**Zach Montoya** 21:06 I… let's do this.
**eftiquar** 21:23 Exactly, that's what was the suggestion.
**Zach Montoya** 21:25 Yeah, and then I'm just going to reference a new issue… Okay.
Alright.
So now we have a new issue there, and we can just track that separately.
This one, let's put this back in the backlog for now.
And then, yeah, the Kafka stuff, I think, is, I think the… we were waiting for semantic, conventions changes, and I think those got implemented, so… So we're good on this, it's just, haven't had time to look into that. So… Nothing blocking there, just needs some… some time.
Cool, am I missing anything for in progress?
I think this… sorry, football, it's just not exhaustive.
This is in progress, this is the CLS ID.
Process name matching… oh.
We could probably do this.
Okay, well, it's done backlog for now. We haven't spent any time on it.
Okay, cool. So it's looking good. We'll, publish… a new release with .NET 11 support, soon, and… get to close this one out.
And, declare that we… Support the latest.net.
And that is all we got today.
Is there anything else you guys wanted to discuss? Or we can, just wrap up early?
**eftiquar** 23:28 Yeah, all good on my side.
**Zach Montoya** 23:32 Cool. Alright, well, thanks everyone for your time.
Thanks. See you later.
**Alexey Pukhov** 23:36 Thank you.

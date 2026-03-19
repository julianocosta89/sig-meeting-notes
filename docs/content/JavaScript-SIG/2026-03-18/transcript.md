SIG: JavaScript SIG
Date: 2026-03-18
Duration: 58 minutes
============================================================

## Zoom Recording Transcript

**Marc Pichler (Dynatrace)** 00:41 Hello?
**Marylia Gutierrez** 00:43 Hello.
**Hector Hernandez** 00:47 Hello.
**Jan Peer** 00:48 Bye.
**Marc Pichler (Dynatrace)** 00:50 Blue.
Jan, are you in the Dynatrace office?
**Jan Peer** 00:55 Maybe.
**Marc Pichler (Dynatrace)** 00:57 That's the wrong office, no?
**Jan Peer** 01:00 It is, it is, it is, depends on who you ask.
I mean, it's a good office to be.
But there are two floors above you, no one floor above you.
**Marc Pichler (Dynatrace)** 01:13 I'll stop by afterwards to say hi.
**Jan Peer** 01:16 Perfect.
By the way, I, replaced, Andre, for two and a half months, because he's on vacation.
Let's see, maybe longer, less, who knows?
**Marc Pichler (Dynatrace)** 01:32 Awesome.
Right, glad to have you. Welcome, everybody.
I'll… I will share my screen.
And then we can get started.
Bent.
So, the first topic here is, Nimrod asking for… Profiling support.
**Nimrod Avni** 02:13 Yes, hello.
Hello?
Nice meeting you, I'm the first time here in the JS SIG.
Thank you. I'm actually not part, like, a contributing part of the profiling thing. I'm using the profiling product, and I started, implementing some more stuff there, and coming from the OBI, SIG.
this request, I linked another issue I've opened in the eBPF… I don't know if, like, how much the profile… the new profiling signal is, like, familiar to everyone, because it's kind of, right now, been promoted to alpha.
To basically, basically, a new signal and counting the main… X photo of it with the OpenTermity repair profiler.
And there is, like, work in progress, to have other ways of exporting it. The main one now is having, like, PPROF, and those are, like, in the collector, there's a converter between PPROF and the OpenTelemetry, profiling signal.
And there's also some work on the Java space with, like, asking profiler support for the new profanic signal. I had specifically a thing I wanted to a proposal of basically having wall clock profiling for Node.js applications, because right now the AVP profile only does CPU profiling and off CPU, and the off-CPU is not really accurate, because it mainly samples, like, the event loop, idle time, and not the actual, like.
Asking tasks that are waiting, so there's no real way to know how much time your task is taking.
In… but there are, like, other profilers, I know the thing, there's a Dakota woman, there's a… There's Pioscope, there's, I think, a Google one, they do stuff similar to it.
And I wanted to… so there's also different, there's also, like, other stuff, like CPU and memory profiling that… I think was already supported in, like, the inspect, like, the Node.js Inspect API.
But as a… as, like, a starting point for all those stuff, I think maybe we can have initial support for the profiling signal in the… JavaScript SDK, stuff like, you know, how to… basically create and export profiles directly from the SDK, and then… maybe, let's say, in a Contrib repo, or even other repos that are consuming the JS SDK, have actual, like, profilers that can emit the new, signal.
So that was, like, that was the, why I kinda… that's, like, the host of how we got to, like, proposing it into the JSFig.
And I wanted to, like, hear your thoughts, if… do you think it's relevant? It's a place, like, it makes sense for it to live, though?
And I… I can also, walk on… on it, I don't know if there's, like, I don't know how often we add new signals to the SDK, I guess it's not a lot, but… Want to do with folks.
**Marc Pichler (Dynatrace)** 05:20 Yeah, so for, the whole profiling stuff, I have to say, I am not very deep into that. I haven't, looked into what the spec has been doing on that front at all. So I'm not sure if anybody else is on the call who has more insight.
than I do.
Looks like.
Breaking cats?
**Nimrod Avni** 05:47 anyone here from the profiling see? I can just say that, it's just been, promoted to alpha.
And I think it should, like, from what, the profounding fig is saying, it should be a lot more stable, and maybe only get, button changes that say it only hits, like, a different utility level, like, beta or stable.
But, yeah, I think it's kind of very a recent, like, it's been in work only, like, for about a year, and it's, like, a recent promotion to being more stable.
**Marc Pichler (Dynatrace)** 06:21 Yeah, I think… We'd probably be… interested in it, adding profiling, at some point. We are currently working on getting the logs signal stable, so that obviously is a priority first for us, but once we, actually have or the signers, stabil that we have been working on, this would be the logical next step, I think. So, from a priority standpoint, I think nothing speaks against, Starting to… to look into that.
As for where the best place for it to live is, I would have to Look into it a bit more, and see, like, how these things are usually done, and then, basically working my way backwards from, like, which technology stack we're using to, figure out if the JS repos are a good place, or if there should be maybe another repo, or, should live somewhere. So these are kind of the concerns that I, that are floating around in my mind right now, but I don't have any… good initial answer to your question, I think, yet.
**So… Nimrod Avni** 07:46 Like, I… I at least thought that the… like, the SDK, at least, for, like, how to, create and produce this, like, profiling telemetry. In my mind, it makes sense to leave.
in the, OpenTernalty.js, repo, because it's, like, kind of similar to all other signals of, like, how you produce it. And as far as, like, the profilers themselves, or, like, the equivalent of, like, instrumentations, maybe can live either in the JS contributory, or even other repos, But, like, I wanted to try to push it because I don't want to… like, if I say I want to start to implement, something that export these profiles.
I would like to lean on, like, the official, implementation of the… of the signal instead of, like, kind of implementing something of my own.
And as far as priority, I don't mind, like, taking it and working on it, but I guess you still need some, like, reviewing and priorities, but whatever you feel… makes sense if it's something that you say might not be the correct time, or you might need some more time to look at it, I'll… Fair enough.
**Marc Pichler (Dynatrace)** 09:01 Yeah, so… I think for, So, timeline-wise, we would be aiming to promote the logs stuff soonish, so, we'd be looking at I would hope not more than a two-month time frame on that, whereas, like, when… once we have finished that up, we would be able to, take on new topics, and that would probably be one of the topics that we'd be also looking at. Hasn't come up a lot in the past, but, Since it is specified, and there's… Bye.
good ca- good… Sid, there's a good reason to have it. I think we would definitely want to take it on. One of the things that I'm not, I haven't really looked into how profiling works on a technical level, and one of the things that I… probably would need to know is, is it gonna be, like, native, implementation of a profiler, or is that going to be, something else. So… these are the things that I'm… not sure about, and I also don't know how to approach them, because I've never looked into, like, how to… properly do it. So… Based on that, we would probably have to introduce some additional tooling and stuff like that, and that's something that we would have to figure out.
Possibly before getting started, what, like, the general architecture of the whole thing is going to be.
So, if you have any, initial ideas or anything like that. It would be really good to have some sort of a prototype or something.
Which we can then have a look at and iterate on to, figure out where it would fit best, I guess.
So if you are keen on working, on that, and interested in driving that forward, I think a small prototype is something that, would definitely help also convince the community to, Take it on, and yeah, find the correct place for it.
**Nimrod Avni** 11:42 Okay, so I'll… I guess I can start off on, like, a prototype, I'd like to prototype at least, like, the… generic signal pipeline, and then also maybe, like, an implementation that does, I don't know, some type of profiling, if it's CPU, workload, memory, whatever.
And if I have something, I'll, like, I'll continue to update the issue with more resources, I guess, both on… Like, general stuff, like, how profiling works in Autel, and the current implementation, which is this system eBPF profiler one, and also some stuff of my own, so I'll try to update it.
**Marc Pichler (Dynatrace)** 12:23 Yeah, that would be very helpful, because then everybody can go in and have a look, possibly run some stuff themselves. That always, also helps in like, getting a grasp of what the moving parts are and, how things fit together, so I think that would be definitely helpful. We probably wouldn't merge, the… Prototype directly, but it would be something that gives us a base to start looking at, and then we can move on from there.
**Nimrod Avni** 12:56 Okay, sounds good. Thank you very much.
**Marc Pichler (Dynatrace)** 12:59 Alright, thank you.
Does anybody have, any questions around profiling?
Guess now would be a good time to… That's coolie.
If not, then, yeah, if you have any, questions, Peace.
Just put them on the, on the issue there, and we can… discuss further.
Alright.
**If there's no more comments, then we can move on to Marilla's topic, which is asking… Marylia Gutierrez** 13:43 I'll just ask you for a review on the… Marc Pichler (Dynatrace) 13:45 Oh.
**Marylia Gutierrez** 13:46 Oh, wait, I guess you… Marc Pichler (Dynatrace) 13:49 I think she had the same idea there.
I was just going through reviewing PRs earlier, so, looks like that is already done.
**Marylia Gutierrez** 14:01 My job here is done. Next.
What is this?
**Marc Pichler (Dynatrace)** 14:08 And… Jan Peer 14:10 Yes.
**Marc Pichler (Dynatrace)** 14:10 one topic from Jan.
**Jan Peer** 14:13 Yeah, it's more of, information now spreading, since we are keen on adopting the tracing channels, because they're out since, I don't know, version 14, I think, of Node.js.
And there's… a lot of interest in different runtimes where the import module on the ESM doesn't work, like Cluster.
We try to adopt the tracing channels in the libraries directly. So, for example, of MySQL, we already have a PR merged.
Which means, once this is released, we could theoretically update the… the contrib channels, or the contribo.
Adopting this one, which means we don't need to monkey patch anything anymore.
And this way, we basically try to, you know, make Cloudflare runtimes more possible with OpenTelemetry. Also making it more aware for library maintainers, because I don't think that they know what this is about.
So this is actually something we've tried to adopt a little bit more.
**But I don't know if this is actually… I think these channels are here for exactly that thing, right? So… Marc Pichler (Dynatrace)** 15:22 Yeah, so, actually, there was an issue that was opened a while ago by, I think also somebody from Sentry.
**Jan Peer** 15:34 Okay.
**Marc Pichler (Dynatrace)** 15:35 Who… so, because one of the issues that we were having was that, I don't know if you did die.
Where is it? This one here. One of the issues that we were having is, that, we cannot… with the current context API, I just activate the context for that whole operation, because the tracing channel emits these events.
And we would actually want to, Have the context active.
not only just for the event, but also for the underlying operation, so that spans can be properly nested. So, that is essentially the one thing that we still need to take care of and figure out how to do.
And I have this proposal here.
Which is just PR.
has stored for a bit, because I haven't had much time to work on it recently. Yeah, that's alright.
But it is this, context, attach, detach thing. And what that essentially does is, it allows us to have a simple wrapper around Tracing channel, which is also very similar to what the person that opened the issue initially has proposed.
And… See if I can find something here.
Essentially, it just wraps it and then uses this context attachdetach to activate the context properly.
And that would then allow us to instrument tracing channels as well.
**Jan Peer** 17:14 Okay, okay, got it. Which means, first, this has to land in OpenTelemetry at some point?
And then we can adapt the… the country, you know, ice cream editions, right?
Is there any way… is there any way on how we can help on this one? The prototype Context Attach, Detach?
**It's just… Marc Pichler (Dynatrace)** 17:35 So… Jan Peer 17:35 Or no.
**Marc Pichler (Dynatrace)** 17:36 This is… this is a draft, the underlying functionality is actually very simple, so there's not a lot of work to be done. One of the things that we still need to figure out is how the shape of the API looks like, and how to move forward with that. I was actually planning to, Continue working on this soon, because it also kind of factors into the proposal on, the Node.js repo, where they were, thinking about adding an Oter module directly to Node.js.
So having something like that, to show that, tracing channels can be used directly to generate spans, could also maybe influenced the discussion there a little bit, because it simplifies stuff a lot, as you said. Having tracing channels used everywhere, and then us just consuming that is way, way simpler than the monkey patching, and way less error-prone, so… I think there's definitely an appetite for this.
**Jan Peer** 18:49 I mean, if you want, we can also brainstorm together at some point, if you want.
**So… Marc Pichler (Dynatrace)** 18:56 Yeah.
So, to answer your question, is there anything you can help with? One of the things that are still open is, implementing this context attach and detach for the other context managers.
We have two of them right now, that we haven't implemented that yet. This is the Stack Context Manager, and the Zone.js Context Manager. The Zone.js one will be Probably a lot more difficult to get right.
But, yeah, if… There's, sometime… to look into that, that would be already very helpful.
**Jan Peer** 19:42 Okay.
**Marc Pichler (Dynatrace)** 19:43 Because once we have prototypes for all three of these, we can… open the PR on the API, and then just merge these.
things in.
And then, it would be supported for all the context managers, and, we can easily then implement the proposed layoff here for the tracing channels.
**And that will then unblock the whole chain of, things to… Jan Peer** 20:13 of awesomeness.
**Marc Pichler (Dynatrace)** 20:14 Yeah, exactly.
**Jan Peer** 20:18 Okay.
That sounds like a good, first step.
Amazing.
**Marc Pichler (Dynatrace)** 20:26 Yeah, I think we would be all very hap… Happy to, Use less monkey patching and do more tracing channel subscribing.
**Jan Peer** 20:38 Yep.
Okay, then I'll just have a quick look on this one. I don't know if I know the best, but… Damn.
iteration.
**Marc Pichler (Dynatrace)** 20:50 Yes, thanks for bringing that up, too. It has been stored for a bit, over the past few weeks, but hoping to get back.
**Jan Peer** 20:57 Oh, that's right.
**Marc Pichler (Dynatrace)** 21:02 Alright.
Any questions about… Tracing… General sort of approach, maybe.
If not, then thank you for bringing that up, and… There's no more.
No more topics here, then we can move on to bug triage. As always, if you have a topic that you would like to discuss where we're doing bug triage.
Please just let me know, and then we can interrupt backtriage and go back to discussing topics.
**Marylia Gutierrez** 21:44 Yeah, I was gonna say, there's no bugs on both of them. The other has one that we are just waiting for a feedback on.
So you can go to PRs.
**Marc Pichler (Dynatrace)** 21:54 Alright, awesome, thank you.
**Marylia Gutierrez** 21:56 Or has more.
**Marc Pichler (Dynatrace)** 21:59 Core repo has more than we go for the core repo. So, Let's get started here. We talked about this recently, this is related to the… logs SDK milestone, so we'll skip this one, because we need first to… complete all the tasks in the logs SDK milestone, the stabilization… the stabilization milestone.
That you can find here.
So there's… Quite a few of these, that are waiting for… PR reviews as well, so if anybody has some time to Have a look into these, that would be very much appreciated.
So… That's this here. Then the second one… I assigned myself to, Open Issue to discuss having API extension packages, to facilitate these sorts of, features for the API that, We still want to have, but, we're not sure of the exact shape yet, so we don't want to commit to it in the API.
**Then, this one right here… Marylia Gutierrez** 23:39 So this one, I was thinking if we actually… if we should close it, because Mike picked up, and he has a PR… Yeah, continue, with that.
So I don't know if you want to just close that one.
**Marc Pichler (Dynatrace)** 23:55 I will just close this one, closing in favor of… 6, 4, 9, 8… So, that's… one down?
And, this one hasn't had any activity.
Oh, - I'm wondering if we should just close this one, and then, Let's have somebody else pick up.
the work.
On the ticket, it should be fairly simple.
Oh, this is actually good.
Close the stale, sorry, let's reopen this one.
This is actually for Cloudflare workers, the confusion on this PR was mainly because it tried to do two different things. It tried to, one, make it compatible with Cloudflare workers, and two, make it compatible with the GenAI SEMConf And… Discussion kind of derailed a bit, and Would be best to address these two things separately, because they are… Different… Enough that it warrants two PRs.
So I actually put a comment here to say, Closing this as the better approach would be to open… Two peers… Pressing the cloud… Issue… addressing gen AI StemConf.
And… If somebody has time, they can, still work on that.
PR's appreciated for both of these things.
Alright, then we have two… Renovate updates, we'll skip these for now.
the create instrumentation factory function, I guess it's also on hold right now.
So we'll skip that.
This one, we keep talking about every… week, but I haven't gotten into yet. Looks like Dan has had some time to review this one.
So… One is well on its way.
And we have this CLO monitor exemption. I always assigned this to me.
Because I need to figure out what the CLO monetize actually is, before adding an exemption for it.
And this one is actually approved, so we can probably merge this one in. I… Approved this one, but didn't merge it, so let's do that now.
This is a thing about the fetch later transport.
But the… ends on the… Processing seems to be that… We don't want to do this right now, so, And this, closing this as… Funnel.
You may Change… Oh, Position ones.
Faculator has been… Or roughly… And… Of course, people can always still implement their own exporters if this is needed. So… There's community interest, having another package for it is… And super… Then we have this PR here.
I asked 3 weeks ago if they're still working on this, but there seems to be.
no movement, so I will close this PR.
And we have… Another stale PR here… I'll put the comment here… If they're still planning to work on this… Almost accidentally closed this one.
Let's see, are there any new topics? No. If not, then let's continue.
with PR triage.
This one is related to the, ultery exporter… base… specifically, in the way that we handle our, retries.
Essentially, the way that it works now is, We had, like, an upper limit of around 15 seconds, and… This one, changes it so that there's better use of the, Of the timeout that's being configured.
But there is a problem with that, which is that… we have… a little bit of a difficult situation right now with the fourth flush.
So, essentially what's happening is, if we… shut down the SDK, we don't… call force flush before… we do call fast flush before shutdown, but force flush really just doesn't speed up anything, it just awaits the export. And if it's failing, then it will block, the shutdown for a while, so that what you're currently seeing when you shut down the SDK is, it will… wait for a bit, if there's no… no OTRPX, no OTRP endpoint there, and then, terminate later, after some seconds, and before We had a change that preceded That one, we actually terminated a bit quicker, which is a behavior that we want to get back.
So, I have this PR in flat right now.
Which is… essentially restoring spec-compliant behavior in the logs SDK.
So if anybody has time to look into that.
Then, that would also unblock.
this PR, because while it does improve things, it just makes the other situation worse.
Which we probably don't want to do right now, because it would just bump, I think, the current… the current blocking time that we have when shutting down is around 8 seconds. I would bump that by a few more seconds, which, would, not improve things. So I will put a comment there, just letting the person know that, this is the case.
Currently blocked on… And… Similar changes in the… Auto SDKs… Recurrencity C.
issues where… After it's no… opener.
Rick, App shutdowns, tick.
Significantly longer.
So… Just a heads up on what's happening here.
It would be a shame if this one… Went stale and then got closed, Because of that, because I still think we should… Align that somehow, so that we actually retry for the whole duration of what the user has configured.
Alright, so this is a performance improvement, looks like, there was a review here… What's going on?
**David Luna Bistuer** 36:32 this one.
**Marc Pichler (Dynatrace)** 36:37 Sorry, I, think I didn't hear you.
**David Luna Bistuer** 36:39 Yeah, sorry, Mark, maybe I'm kind of blocked at PR?
Because, we need to work on the, trade-state. I think that we have both implementation, we have implementation in the API and on the SDK. Let's say the two, duplicate the one on the API and… And review the one on the SDK. So, yeah. Well, if I have time, I'll try to work this week on it.
And hopefully include something about this. So, I, I tell Abhi, just to wait a little bit to… to get that tier first, and then, check the performance of that.
Okay, so I guess we can exit this one for now.
**Marc Pichler (Dynatrace)** 37:21 Alright, then, let's skip this one for now, and, yeah. If there's, a PR for the change that you mentioned, then, feel free to let me know, and I will… Have a look at it on as well, to unblock.
**David Luna Bistuer** 37:37 Love it.
**Marc Pichler (Dynatrace)** 37:39 Right?
So… This was trace state serialized, and then there's another one, which is… the… trace ID ratio-based sampler.
Looks like some more conflicts here.
Let's move this… And then I think this one, Should also be… good to merge soon. I haven't looked into this one before, so… Can't merge it immediately, but… I'm sure this one is… are so reasonable. So, if anybody has time, please feel free to have a look at this.
This one, I still need to reach out to the people mentioned there.
Set some time aside.
Soon, too.
Tech to death. This one is… quite a large PR.
So… I guess now is a good time, anyway, to talk about what it's doing, and maybe some of your thoughts on it.
It's… the… essentially introduce tiers down, and then, make all the packages have, And that's not the one that I was trying to look at, this one here. Have all the packages have these, dual, CommonJS and ESM, exports?
While doing that, it also migrates from, comma, which is deprecated to, by test.
Which I think is a change that… We probably want.
Oh, there's a lot of stuff going on here. I don't know, maybe, David, do you have… Opinions on it.
I think you did an experiment on the Undichi instrumentation a while ago, right?
**David Luna Bistuer** 40:39 This, yeah, this one, with a couple of tools, but, is TS Down is using another, another tool, which is to roll down.
Which is a Rust-based, bundler.
Need to check this one. So, one of the questions that I had when I was doing my test is, like, usually these boundaries are fast because they're not doing any type check.
And in my previous version, you still have some kind of type checking, because we were using TSNote.
**Marc Pichler (Dynatrace)** 41:09 Absolutely.
**David Luna Bistuer** 41:09 pilot test on the fly, and then you get the same. So usually you get the compilation issues while testing. That was kind of a safety net for us. I need to check if this actually is doing the same, and we are not… if TSTOM is not actually doing the type checking or not, so… Yeah, that's the only concern I have right now, so it's like, if we actually have kind of a type checking properly in place, so we don't… Generate the wrong types, and then we have breaking changes for consumers.
On the testing, I think it's a matter of… of tests. So, the browser's seek, they like PTEST, and they like the… this… This tool for testing.
And it goes with sync with the packages they already have in the process repository, so yeah, we think that the guise of the processing, they will be happy, and they will support and maintain it, so… That's a good thing.
But yeah, I'll put it on my list to review as soon as possible.
**Marc Pichler (Dynatrace)** 42:17 Yeah, thanks.
I'm wondering if we should suggest, splitting out the change for, B-Test, into a separate PR, and merging that first, because that would Could possibly be a bit simpler and align tooling first, and then we can iterate a bit more on it.
**David Luna Bistuer** 42:42 Okay, I'll answer it tomorrow while we have the Sikh meeting, so I can ask about this, if it's possible.
**Marc Pichler (Dynatrace)** 42:49 Yeah, that would be great. Then we can, figure out what we're gonna do, with this, PR, and hopefully cut down a little bit on its size as well, which should make subsequent changes a bit easier.
Alright, thank you.
Then, moving on, Is this PR up? But first, does anybody have any additional thoughts on… The proposed change here.
Or proposed change to test… tooling.
If not, then, Let's move on to this PR here. This is also, OTRP expert PR, This is intended to recover from an error state that, gRPC event Or the library that we use sometimes runs into, where, It gets stuck in this deadline exceeded mode, and recreating the… Client helps, essentially just… recover from that.
Actually… haven't had a look at this PR in a while, but I think the strategy here is sound, and once we merge that in, we can still iterate on, like, how quickly we Want to recreate it. I'm not sure… I think we have talked about this during a SIG meeting before, and somebody had an opinion.
But I don't recall anymore what the opinion was, or… Who it was.
But I think this makes sense, so I'll approve this for now. If anybody has… Any objections or anything, please feel free to, comment on the PR, and… Let me know, and then… I just leave this for a bit before merging, so that everyone has some time to… Boise their thoughts there.
many exporter PRs today. We have… GRPC… Export, Having the general options as config parameters.
I think this one is a larger one, I can't… prove that more quickly, so I'll assign myself, because this has also been sitting for a bit here.
Anyone else wants to have a look at this one, please feel free to do so.
for this one, I think the general options, or giving the general options Your parameter is probably fine.
One of the issues that we have had with, passing in gRPC config options is that… we encourage the user to instantiate, or to import gRPC before it can be patched, and that breaks gRPC.
instrumentations.
But… This specific one should be fine and free from that issue, since it's just the general options.
This is the PR I was talking about earlier, this just shows how everything works together.
Once we actually can cancel the retries on shutdown, and speed up the shutdown there.
Right.
Then we have… this PR, which I actually pushed a commit to earlier, but I messed up something, so now the lint is broken.
I'll also assign this to myself to have another look, because… I'm actually working on an issue that needs that to be merged first.
Next one is a PR that we talked about already. This is the one.
spawned off of the draft PR. It's also in the… blocks… milestone… We have Dan's entity resource prototype, just open for comments if anybody has one. And… We have… this PR to let… to add the logger-enabled method.
I did approve this.
a trend will be out for a few weeks, right? .
**David Luna Bistuer** 48:49 Yep.
**Marc Pichler (Dynatrace)** 48:51 I think you, addressed… yeah, I think you addressed all his comments, right?
Yeah.
**David Luna Bistuer** 48:58 I think maybe… and also, there was a PR that actually included the, the LinkedIn role for the import type.
So, make… go away all the… most of these, comments from… from 10.
So, yeah.
**Marc Pichler (Dynatrace)** 49:15 So, I guess this would be… Good to merge, but… trends to the US.
It's weekly.
**David Luna Bistuer** 49:25 Aaron, we… miro.
**Marc Pichler (Dynatrace)** 49:29 Yeah, we for sure can wait.
**David Luna Bistuer** 49:32 No.
**Marc Pichler (Dynatrace)** 49:33 I guess there's not a lot of change to the export pipeline or anything like that, so we shouldn't get any… David Luna Bistuer 49:41 No.
**Marc Pichler (Dynatrace)** 49:42 Any conflicts on it, so… David Luna Bistuer 49:44 One thing that I… my… I don't know, maybe one question that the club's app is, it is much of the… more similar… it's a bit similar.
quite similar to the emit method, so I think most of the logic… at the end, I finally implemented most of the logic following the same as the emit method, so I wonder if that's… Maybe it's better to have to kind of have a shared logic.
And in the mid… and… and… And so we can keep it as is, but it seems like the code is being duplicated. So we have to say for… At least, to discard everything along record, or to return false in enabled.
So I wonder if that… it makes sense to just have some, maybe, calling enabled first, or… You know, this shared logic.
See if the logger is enabled for that specific option, certain specific context, and log record.
And then, admitting or not. Just thinking out loud.
**Marc Pichler (Dynatrace)** 50:49 So it would be… These things right here.
I mean, right?
**David Luna Bistuer** 50:55 Yeah, I think that the only part that is not… it's the iteration of the processors, but the first part of checking the disabled configuration.
**Marc Pichler (Dynatrace)** 51:02 That's ready.
**David Luna Bistuer** 51:03 number, and then the context.
That's… it's… Exactly. Well, it's not exactly the same, but yeah, I would say the time. 90% is the same… it's the same code.
So I was wondering maybe to extract that code somewhere else, and then use it in both the meat and, you know.
**Marc Pichler (Dynatrace)** 51:20 Yeah, so would probably live somewhere in the blocks SDK, right?
Oh, no.
Yeah.
I think that's a… That's a good idea. We could probably keep it internal, too, because most of the usages are… in the logs SDK, right? So that's the multi-dog record processor, and… That's actually not that one.
But yeah, I think, I think that… Probably makes sense. If we make some changes, I will ever have another look to re-approve.
Oh, me.
**David Luna Bistuer** 52:00 Okay, sheds.
**Marc Pichler (Dynatrace)** 52:00 Yep.
**David Luna Bistuer** 52:01 I'll let you know.
**Marc Pichler (Dynatrace)** 52:02 also looks good as is, I think. So… whatever you prefer, I think… is… is good.
Alright, then we have this… Looks like there's a changes requested review from… errant… So… I think this is, still valid, so let's keep this open for now and see if the person… response, and if not, then I will, Ask again if they still intend to work on it.
this is, again, one of my PRs, Looks like I need to resolve some conflicts there, but the overall approach should still, be valid, is adding a custom logs protobuf serializer. Instead of using Protopuff.js, it, essentially hand-draws the serialization logic, which is a bit more efficient, both memory-wise and And in terms of compute, so if anybody has some time to have a look at that, would be very much appreciated.
It… Essentially moves us towards a place where, the OTRP exporters don't violate content security policies anymore.
Once we have that for all the signers, you can then export protopuff from the browser, which… some people might want. It at least improves compatibility with a few things.
Regardless of… That being, the best way to do it or not, it… Gets us into compliance with the spec as well.
Which says that, if we only support one, we should support Protopuff.
Which we currently don't do.
Alright, Then there's another one, which is tagged with browser.
is actually instrumentation fetch, so… Difficult to figure that out from the… I do.
Looks like there's this Copilot review and chart editor browser.
Label on it.
not deep enough into instrumentation fetch code that I would be able to… figure out what it's doing. That looks like there's one.
Issue linked.
Looks like there's… Some stuff that's being ignored.
So this is actually a… bug report, then. And that's not a refactor, but a bug fix.
And that's B1, because… It actually breaks.
End users.
Expectations of what's gonna happen.
And they use it like that.
I'm also gonna put the pack label on this one here, so that it actually sticks out.
When we look at the PRs.
Can review this one.
right here, because I… I have to admit, I don't know my way around the fetch.
instrumentation.
Too much.
And this one, I think Trent and, this person have been working on that.
Some time ago, project this one is also fairly large, but it follows a similar pattern that was already introduced in the Trace SDK. So, if anybody has time to review this one, please also feel free to go ahead, It… It's metrics that can be exported from… the logs SDK, which just described what the logs SDK is doing, so that you have some… some self-monitoring for hotel there.
But it looks like we are out of time for today anyway, so, that's it for yard triage.
Looks like we covered quite a bit of ground today.
If there's no more questions or comments… And thank you, everybody, for joining.
Have a nice week, and see you next week.
**Hector Hernandez** 58:40 Thank you very much.
**Jan Peer** 58:41 Hey guys.
**Marc Pichler (Dynatrace)** 58:43 Sweet.

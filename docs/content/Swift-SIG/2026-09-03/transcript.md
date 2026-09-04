SIG: Swift SIG
Date: 2026-09-03
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

**Bryce** 00:55 Nacho.
**Vishwan aranha** 00:59 Nice.
**Nacho Bonafonte** 01:05 Hey, nice. How are you?
**Bryce** 01:07 I'm doing good. How are you doing?
**Nacho Bonafonte** 01:10 Fine, fine, yeah, everything.
Lots of work, really happy.
**Bryce** 01:18 Very good.
I can, I can run the meeting, since I haven't been doing anything else.
Meeting notes… Okie dokie.
Okay, I think we've got a good turnout, why don't we just get started? Vishwan, last meeting. OTEL SWIFT extension points for mobile session context and delay metric diagnostics.
**Nacho Bonafonte** 02:27 Also, I think there are some other topics that… In previous week, yeah, I have not created this document today.
**Bryce** 02:35 Oh, okay, okay, okay.
**Nacho Bonafonte** 02:36 I don't know who it was Vishwan.
Understood. And yeah, we were… and these other topics, so… We are aware of some of them.
**Bryce** 02:50 Do we need to bring any of these ones forward? Swift Observability APIs Integration Document?
**Nacho Bonafonte** 02:56 Yeah, but basically, just maybe talking about it. We are waiting… about this topic, we are still waiting for Apple to… Peer and talked about their proposals, once we have talked a bit about it.
They were gonna… Yeah, last week, so we don't know.
More, yeah, we decided to try to do Clean up of all the issues.
at the end of the meeting, if there is time, so we can track some of them and remove those. That doesn't make sense anymore.
**Bryce** 03:35 Sounds good.
**Nacho Bonafonte** 03:36 And also… The other topic there… yeah, we were talking about That, that I think, yeah.
About creating a release?
During September, so… Let's try to do that. And it's in the first half of September for the latest CocoaPods theme, so let's try to merge all we can without creating any issues or problems, so… We don't have to release anything more about Cocoa Pozi. And after that, Yeah, we talked about moving the… Moving the streetcore.
again, into Swift.
Into the main repository, and continue from there.
Right, right. And also talk… after that, that also Apple will have landed the newest versions of all the tools, and… and… and iOS, and then think about the minimum versions that we plan to support, because we can probably… increase that and update some of the things, but let's wait after CocoaPulse for that.
I don't know. That was what we have talked so far. I don't know if you have any… and comment to us, or any idea around that price?
**Bryce** 04:57 No? Yeah, I think that's a good idea, next Wednesday. So, next week, we should, be able to make some, I don't know, decisions about the minimum supported versions? Are they gonna actually release the new, tools by then, or is it… that's just the announcement of their tools? Oh, where'd my camera go?
**Nacho Bonafonte** 05:20 Yeah, they will probably release them I think that they release, usually, the tools.
the same day.
**Bryce** 05:29 Thanks, Jamie.
**Nacho Bonafonte** 05:30 announced, or the final version, probably, or at least a golden… a golden, one version. So yeah, we can talk about that, but… as we will have probably released.
the latest OpenTelemetry version for CocoPost, we can then Aye.
Wait for that flow.
Yeah, addressing those, those other things.
**Bryce** 05:54 Okay, cool.
Alright, Vishwan is here. So, is there anything to say about, this topic from last week, the hotel swift extension points for mobile session context?
**Vishwan aranha** 06:07 Nothing that I… I think that was a week before, not, like, last week's discussion, but yeah, it's all sorted.
**Bryce** 06:17 Okay, so no update on that.
Is there a PO order?
**Nacho Bonafonte** 06:21 Yeah, Billy was gonna take a look, if he had… Time, he said?
I don't know if he… If you really were able to take a look.
**Billy** 06:33 For which one?
**Nacho Bonafonte** 06:35 to the…
**Bryce** 06:37 This one here, hold on, let me…
**Nacho Bonafonte** 06:39 context?
Or, or it's not that one?
**Bryce** 06:46 Or are you talking about the one in the topics list?
**Nacho Bonafonte** 06:49 Yeah, I think I'm missing… yeah, sorry, I think that I was talking about that one already, yeah, sorry.
**Bryce** 06:55 Oh, okay. Well, it doesn't sound like there's anything to say about this one, so we can't just jump to the current topics.
**Nacho Bonafonte** 07:01 Okay.
**Vishwan aranha** 07:04 Sounds good, and this was my first quick follow-up on mobile sessions for this topic. I split the remaining work into three smaller PRs, so we can review one problem at a time. So, the first PR is, like, I think one on A3, where I separated the automatic telemetry from real activity, and, like, it covers the expiry and, like, manual reset.
since chains are basically not allowed, so I created another PR, 1084, which goes off of that, which has, like, versioning storage and, like, defines which process owns the saved session, and the final PR, which is, like, the only PR we probably can merge once all three reviews are done, is, like, it keeps the same sampling choice across traces, logs, and metrics.
And, today I just wanted to… mainly wanted to confirm, like, that split is good, and it, the order makes sense. If so, we can, like, if we can begin reviewing by 1183, I can, like, Yeah, answering questions or anything you have, or we can do it async, that's perfectly fine.
**Bryce** 08:08 I see.
**Billy** 08:09 Yeah, I didn't see this, so yeah, I'll take a look. Thank you.
**Bryce** 08:18 Yeah, maybe it's a little too dense to go through right now.
Let me look at that. Yeah, but I can… I have some time this morning, so I'll take a look at this as well. My camera keeps turning off, it's annoying.
But yeah, thank you for… for all the effort. That looks good.
**Vishwan aranha** 08:38 Thank you for taking a look, because that's kind of unblocking me on a lot of the session tasks that I'm working on for Grafana, so it would be perfect whenever you guys get a chance.
**Bryce** 08:47 Cool, alright. Let's take a look at that offline. Alright, so the next topic, log and metric exporter bug fix.
**Yasura Dodo** 08:56 So, this is, kind of, like, auto PR, but, Nacho… Pointed out some concern that, Basically, like, it logs and metrics and traces using a different dispatch process, and… That's why we cannot use this fix for metrics. But actually, we can use… I think we can use this fix for… logs, if I understand correctly. And I was trying to fix it with async await solution, but, it takes a lot of time, takes a lot of effort to fix everywhere, so, instead, fixing them properly, I want to fix it log first.
Which is the, the quick fix for log.
**Bryce** 09:49 Okay.
**Yasura Dodo** 09:53 Cheap.
**Bryce** 09:54 And it just is the, yeah, the, the initial changes that you made, but just for logs. Yes.
**Yasura Dodo** 10:04 And for metrics, maybe, like, I… I… I don't know if I want to fix with a single-way solution, or maybe we can also fix the, the processor.
To be able to… Not blocking the, the… As a thread.
I will, I will, I will check it and provide some, solution that, it works with metrics as well.
But for now, I want to fix the logs first.
Keep fixing the, metrics.
**Bryce** 10:46 Yeah, I think that's reasonable. We can take a look at the logs fix.
Nacho, do you have any issues with… with that approach? Since you were the one who initially commented on the… with the concerns on the, VR.
**Nacho Bonafonte** 11:05 I, I have not taken a look at that, yeah,
**Bryce** 11:11 this.
**Nacho Bonafonte** 11:12 Which, which one is him?
**Bryce** 11:14 The initial one was the return upload failures for logs and metrics.
**Nacho Bonafonte** 11:20 Yeah, yeah, basically the problem was.
Having a SEMA for blocking the export.
It's safe.
Yeah.
That was the main program. If that's not using that, if it… I mean, if the… Thread calendar export is not being blocked, then that's okay for me.
But there is a semaphor there, I don't know… Yeah, so it's waiting for the res… Yeah, that…
**Yasura Dodo** 11:49 So, so, like, for traces, we have the batch spam processor, right?
**Nacho Bonafonte** 11:56 Yes.
**Yasura Dodo** 11:57 We have a similar one for logs, but metrics have a completely different, process.
**Nacho Bonafonte** 12:03 Oh, okay, no.
**Yasura Dodo** 12:04 I…
**Nacho Bonafonte** 12:05 So, logs really… I don't, so logs.
**Yasura Dodo** 12:08 Yeah, yeah, it's very complicated. You can take a look.
I can, I can have some, like, a helpful comment in the product list, so, like, you can have a look easily.
I would do it.
**Nacho Bonafonte** 12:21 Yeah, yeah, that, that, I mean, if, if logs… Are being exported in a different thread, or in a different process.
So if the export happens in a big firm.
Or task, or whatever, I mean, just…
**Yasura Dodo** 12:34 Yeah.
**Nacho Bonafonte** 12:35 other execution context that doesn't get blocked, then I am totally okay with blocking, because that's just the export.
Right.
what's been blocked, not the whole process, or the process, or the metrics process of being blocked by exporting. That will be what I think will happen with the metrics, at least how it's currently designed.
So, yeah, if… That's… If that's like that, yeah, I don't have problems with having a semi-4 block in there.
Export execution itself.
**Yasura Dodo** 13:12 Okay.
Sounds good.
**Bryce** 13:20 Alright, and I guess that covers all the topics for today. Does anybody else have anything they would like to discuss, or should we move on to cleaning up issues?
**Billy** 13:34 Just one more thing, I'm almost done with the, concurrency races thing. I found, like, tons of additional issues from, like.
when I last saw it, yeah, definitely, like, need some, extra review on it, but, yeah, it's, like, I almost have it, I think last week, Nacho also mentioned that, like, we promised, like, some deadline for this work as well.
Could I have some details on that?
**Nacho Bonafonte** 14:06 Yeah, I mean… there is no, like, hard, you know, deadlines. Basically, it's that I think it would be… Great, if we could land that for this release now that we plan to do with Cocoa Pots.
But, I mean, if that's not possible, we can drop it. I mean, it has been there for a long time already. We… if this CocoaPods version doesn't support that item.
They don't have a problem. They're just… Thought that maybe it would be great if we could add it, but… no hard deadlines for anything, I mean… Okay.
**Billy** 14:48 Oh yeah, sounds good.
**Nacho Bonafonte** 14:50 Yeah, what do you think, Bryce?
I mean, I think it's really interesting, but… If we cannot get that, we are not gonna stop everything just for… For this, because we are already releasing like this, so…
**Bryce** 15:02 Yeah, I don't quite have the context for what you're talking about, but, yeah, it sounds like it's one of those things where it would be nice if we could get it into the final CocoaPods release, but if not, then it's not a big deal.
Alright, let's take a look at our issue cleanups.
So, I think probably the easiest way… oh, I'm not even signed in.
Alright, hold on a sec.
**Nacho Bonafonte** 15:36 Yeah, I mean… Yeah, we can also review if there are any new issues, or any new PRs, or something blocked, maybe.
Before?
**Bryce** 15:45 Oh yeah, sure, let's do that. Yep.
**Nacho Bonafonte** 15:48 I don't know, I think there are… just some that… We're approved, but tried to merge, but, like… Getting conflicting each other.
When I, merge, so… but I think that those are…
**Bryce** 16:06 Sorry.
I need to get my authenticator app, and there is a video queued up.
**Nacho Bonafonte** 16:12 Yeah.
**Yasura Dodo** 16:19 So this is my DPR, right?
**Bryce** 16:26 Yeah, sorry, I, we, I wasn't pulling that up specifically, I just was logging in on a different screen. Oh, yeah.
Alright, so, let's look at our PRs first.
Alright, here's Yasura's… Pr?
This is the, yeah, the log exporter fix.
So we can take a look at that offline.
Ignore class prefix. Have you had a chance to look at this one yet?
Okay, yeah, this is part of the swizzling.
**Nacho Bonafonte** 17:11 Yes, yeah, there are many URL session fixes that comes from, This user summary?
That, yeah, approved many of them, but yeah, they've… most of them have… I mean, once you merge one, it conflicts with the other, something like that, because it's touching the same files.
So it's been a bit slow. I reviewed… not this, but I reviewed others.
Yeah, I think this is…
**Bryce** 17:42 The option is accepting the initializer and stored, but then never read, so setting it excludes nothing.
Well, that's unfortunate.
**Nacho Bonafonte** 17:52 Yeah, they definitely… it broke some… some…
**Bryce** 17:57 somehow…
**Nacho Bonafonte** 17:57 I don't know, because that was… Yeah, I mean, we wouldn't have an option, if it hadn't worked in the past.
**Bryce** 18:08 Interesting.
Well, it looks like that one's ongoing.
**Nacho Bonafonte** 18:14 Those are the…
**Bryce** 18:15 Alright.
Persist cross-signal sample decisions. Okay, so this is…
**Vishwan aranha** 18:22 This is the one I brought up before, yeah.
**Bryce** 18:25 Okay, yep, yep, yep, yep, okay. Oh, wait, that's your, that's your GitHub handle?
**Vishwan aranha** 18:29 Yes.
**Bryce** 18:30 Which one? Okay, alright. To know. Oh yeah, aranha, okay.
It's always hard to, you know, like, which way are we mashing… mashing names together on these things?
**Vishwan aranha** 18:41 My last name is, like, Spider in Portuguese.
**Bryce** 18:43 Yeah.
Yeah, okay. Nice, that's cool.
Alright, there we go, and then there's that one, too. Yasura's a refactor here. We already discussed this one, I believe, right?
**Yasura Dodo** 18:59 I just wanted to point out there is a breaking change, I already have a comment.
So, basically… The auto HTTP… Base?
X. Auto HTTP exporter base.
Can I go to the… yeah.
I… changed to the, just, the internal from the public. Right here.
And then that can screw up a little bit.
The type itself.
is now, can I scroll up? Yeah.
**Bryce** 19:43 Final, okay, yeah, so it's not public anymore.
**Yasura Dodo** 19:45 But, like, I don't see, like, people are using the base. I mean, like, it's misused, no? Like, people are using the base.
**Nacho Bonafonte** 19:53 Yeah, no, no, it was not thought to be used.
by… by… by… I mean, it was just a base class for the others to export.
For the other, You know, for trace metrics and logs to just, have some common…
**Yasura Dodo** 20:10 Yo.
**Nacho Bonafonte** 20:11 So, some common code for them, yeah.
So we… yeah, I… By the way, I mean…
**Bryce** 20:20 Well, this thing…
**Nacho Bonafonte** 20:20 It doesn't need to be an API itself.
**Bryce** 20:23 Yeah.
But is this… this is used by, the, exporters as an… okay, yep, yep, yep, yep. Okay, yeah,
**Nacho Bonafonte** 20:39 So, the thing is.
**Bryce** 20:40 from this as well, and then using.
**Nacho Bonafonte** 20:44 So you are making each exporter Half of the code itself?
Instead of.
I mean…
**Yasura Dodo** 20:51 Yeah.
**Nacho Bonafonte** 20:53 Why that? I mean, the thing was, the base class was thought to Add support for, you know, common things like headers.
**Yasura Dodo** 21:02 Yes.
**Nacho Bonafonte** 21:03 And things like that.
**Yasura Dodo** 21:05 Just, like, when I'm working on the, like, having, like, new async functionality, like, it's, a little bit easier to… separate the class, like, not, like, inheriting, but, like, composing is easier to, The stability functionality, like, stipulating concerns.
And… The… my original idea was, like, a lot of changes, so… I wanted to explain the PROs.
If… we don't want to have this breaking change, then, I mean… I can keep using the inheritance.
But, I've heard this is a simpler and cleaner solution. That's why I… I brought this, PR if… Did people like it?
**Nacho Bonafonte** 22:05 Okay, yeah.
Yeah, I think we will have to, yeah, review it.
**Bryce** 22:11 Yeah, I mean.
a positive change, yeah. The only concern I have is, like, if somebody wants to use that base class to implement their own exporters for OTLP, but I guess that's probably kind of far-fetched.
And unnecessary, so…
**Nacho Bonafonte** 22:28 Yeah, I mean, this base class was not thought to be inherited by anyone but their own exporters here. It's not part of the API or the SDK itself, just… it was just functional.
So, yeah, if compositing makes it usable, and also makes it, you know, reduce the code duplication also, that, that, that's perfect. So yeah, let's review that with more.
**Yasura Dodo** 22:59 Cute.
**Nacho Bonafonte** 23:00 motivated.
**Bryce** 23:02 Add shared security scan workflow, that's a bot. Okay.
So that just needs to get reviewed.
And then we have chores, chores, chores, Docs.
Lots of stuff to catch up on. So I'll spend some time this morning to review.
**Nacho Bonafonte** 23:25 Yeah, many of those, URL sessions, I reviewed them and approved.
**Bryce** 23:31 Okay.
Yeah, I see.
**Nacho Bonafonte** 23:33 Yeah, but the problem is that I have merged some, but the others are now conflict.
**Bryce** 23:39 Oh.
**Nacho Bonafonte** 23:40 So, yeah, so I asked… Many of them to be,
**Bryce** 23:46 solved. Yeah. Okay.
**Nacho Bonafonte** 23:48 So, yeah, I asked the user to fix them. He fixed all of them, but once I have merged the first one, all of the rest conflicted again.
So yeah, that…
**Bryce** 24:00 I'll… I'll… I'll go through it.
**Nacho Bonafonte** 24:02 But yeah, take a look if you, if you want. They are quite, you know, limited in the scope, and… important issue to understand, and I think that All of them look good.
But maybe, yeah, I'm missing something, so, yeah.
**Bryce** 24:20 Cool. Alright, that's great. More docs is always better. Alright, let's look at the issues.
**Vishwan aranha** 24:26 Also, I've been reviewing some PRs. My question was, like, open telemetry bot, is that a real person or a bot?
**Bryce** 24:33 That is a… I believe it's a bot, yeah.
**Vishwan aranha** 24:37 Is it safe to review or approve the PRs?
**Bryce** 24:41 I think the only… Well, yeah, actually, that's a good question, you know?
So the Trask is a, he's a reputable, individual, so if he says that this is legitimate, then I believe him.
Yeah, because you never know, you know, somebody could be, like, pretending to be the OpenTelemetry bot and opening PRs and stuff, but…
**Nacho Bonafonte** 25:09 Yeah, the trust… trust… I think.
**Bryce** 25:11 It is in the organization, so… Yeah.
**Vishwan aranha** 25:14 Sounds good.
**Bryce** 25:16 Damn.
But it's good to bring that to question, for sure. Alright, so, these are issues that, yep, we've already discussed.
Drop force flush and shutdown instead of delegate to next processor.
Okay, this is Ben's, okay.
And we have a… Mentioned here… Okay, so what happens? Session log record wraps another log record processor forwards on emit, but then force flush and shutdown returns success without calling the wrapper processor.
session log, yep, okay.
Which is true of the session processor's own state, holding nothing to flush.
But it is only… the only thing the loan provider can see… Anything it wraps becomes unreachable for both operations.
you know, start to create a chain.
I think that sounds reasonable. I don't know if you follow that show.
Yeah, so essentially the… the wrapping processor… doesn't… Pass the, forced flush and shutdowns to the… To the next processor that's in the chain, so… Yeah, kind of setting it up to be a chain of processors rather than… Yeah, I think that's reasonable.
I can reply to that after.
After the meeting, and then there's my last issue. Okay, let's, pop over to core now.
So, some renovate changes, bump minimum version… Okay.
And yeah, that's kind of the state of things. Also, I think we want to prevent any changes going into core at the moment, while we are in the process of switching over, or back into the single repo.
And… Okay, so nothing really to do in here.
Alright, let's take a look at… Our open issues, and… Here, I wonder if we can, use the agent to… Let's see… can we… I'm not really familiar with this, I haven't played around with it at all.
**Nacho Bonafonte** 28:21 Never use it.
**Bryce** 28:32 Hmm…
**Nacho Bonafonte** 28:40 Yeah, probably you have to interact in a different way, and it just tracks your living items, it looks, right?
**Bryce** 28:49 Yeah, yeah, so I was thinking that maybe we could use an agent to review the issues and find, out-of-date ones.
Let's just start at the very back.
**Nacho Bonafonte** 29:01 Yeah, we reviewed some of them.
Last week…
**Bryce** 29:06 Through our session metric instrumentation.
Okay, so… Oh, I see, like, the breakdown of, The breakdown of, like, the… the… points in the, in the URL session requests.
I think that's still relevant, so probably shouldn't remove that one.
**Nacho Bonafonte** 29:40 Last week, I think we cleaned some of them already.
**Bryce** 29:50 Do you know where you stopped?
**Nacho Bonafonte** 29:51 Do anyone know where we stopped?
Yeah, there are, like, a… Handful of promethers exported there.
They are probably… all of them. We didn't reach them.
And the thing is, do we want to… Truck them, still?
**Bryce** 30:19 These are pretty old.
**Nacho Bonafonte** 30:21 Yeah, no one has… Asked about it, so…
**Bryce** 30:26 Yeah, maybe at this point, if anybody wanted the Prometheus Exporter to be, improved, they would have opened a PR on it, or asked, yeah.
And so I think, yeah, it's probably… Fine to close these ones.
Just… Close those ones up.
And there's another one back, oops.
Lost that page, and…
**Nacho Bonafonte** 31:00 Huh, thanks.
Yeah, I think we… probably we ended in the… OTLP export services, that's basically what we are now tracking with.
Like, what Yasura is doing.
**Bryce** 31:15 Yeah.
**Nacho Bonafonte** 31:17 if… Neon.
**Bryce** 31:27 I think that we can close this one. This… nobody seems too interested in actually following up on that.
Thank you.
Create a default gRPC channel for easy… easier configuration.
**Nacho Bonafonte** 31:48 I don't know if anyone is using gRPC export.
anymore.
**Bryce** 31:53 Oh, I thought… I thought that maybe… we've… we've kind of updated the APIs already. I wonder if that's being…
**Nacho Bonafonte** 32:02 Oh, yeah.
**Bryce** 32:03 Yeah, that might already be, like, implemented, you know?
Yeah, so you can actually pass a channel in there.
**Nacho Bonafonte** 32:15 Okay.
**Bryce** 32:16 So, I think that that… that's closed as complete.
So we can…
**Nacho Bonafonte** 32:24 I think it was about creating a default one, instead of…
**Bryce** 32:27 Oh, yeah.
**Nacho Bonafonte** 32:28 They usually are adding one, but yeah, probably… He is not.
We need it anymore.
**Bryce** 32:36 Alright, decode values for OTLP resources.
So, baggage values… didn't we do something with baggage recently?
**Nacho Bonafonte** 32:51 Yes, I think, I think it was addressed in API.
With the baggage format being updated.
Yeah, that was addressed, I think.
Yes, totally.
**Bryce** 33:08 Yeah, there's been a couple…
**Nacho Bonafonte** 33:11 Yeah, I think that one is the one.
Let's address the format.
**Bryce** 33:25 Yeah.
Alright, I'll close that one as well.
Handle partial success responses in OTLP export services.
Okay, so the specification changed to add partial success responses. Each OTLP, or OTL's SDK is encouraged to handle the results.
I mean, this seems still relevant.
Yeah, so this is… this, I think, might be something that got added to the… The, specifications, so we need to… we'll need to adopt that.
Still relevant.
Complete unit tests, batch log, test max limit… Oopsie.
That's not what I wanted to do. Come on, come back.
That's weird.
Is it not there anymore?
Hmm.
Oh, it's probably… it's because it's in… it's in CORE.
Is that why? No.
Visiting?
**Nacho Bonafonte** 35:30 No.
Record processor?
**Bryce** 35:44 Yeah, this must be in, Yeah, that's why.
Batch, test max limit.
Oh yeah, see, this test doesn't do anything.
Yeah, that's still…
**Nacho Bonafonte** 36:17 Yeah, I mean, it tests that it doesn't crash, right? That's… Also, some kind of test.
**Bryce** 36:24 That's… yeah, that's fair.
**Nacho Bonafonte** 36:27 But, yeah, I don't know,
**Bryce** 36:31 But, yeah, like, I think it's the max… queue size that it's trying to test, or maybe it's not possible to test it, I'm not sure.
But, I think the idea is, is that it needs to be, The behavior needs to be tested on whether it actually maxes the cube size or not.
I think that that can be left. The thing is, though… Should we leave it here, because we're gonna merge Core back into Swift, or should I move it into Core, and then we can move it back when we merge Core?
**Nacho Bonafonte** 37:10 I think we can leave it here, yeah.
**Bryce** 37:13 Yeah. Alright, measure, metric keeps sending data. Oh, okay, I think… oh, this is a won't fix, okay.
Yeah, this is, Okay, so… Okay… Yeah, this… I think that we can close this one. It's a documentation issue, is the problem.
**Nacho Bonafonte** 37:44 And probably it was superseded by the new metrics.
**Bryce** 37:49 Oh, yeah, that's a good point. Well, wasn't this… this is, part of the stable metrics.
I think the problem is, the… the…
**Nacho Bonafonte** 37:59 Okay.
**Bryce** 38:00 Reporting configuration was incorrect, and that's… that's why… Or maybe… oh, yeah, I see. Actually, it is, Yeah, I… this… that's an old… Yeah.
Yeah, this is… this is about the old, The old metric stuff, so that, yeah, that's not relevant anymore.
Project doesn't build with Swift 5.2.
**Nacho Bonafonte** 38:39 Yeah, I think that's not… Closed.
**Bryce** 38:45 Minimum supported version… how many minimum supported version issues do we have?
**Nacho Bonafonte** 38:58 Yeah, I think we can't remove them.
**Bryce** 39:01 We'll just close all those.
We know about that.
Discuss, man, yup, did that. Swift Neo, inhibiting library evolution.
**Nacho Bonafonte** 39:28 Yeah, that, that could be known, That could be superseded when we update to a new fruit.
Yeah. But I think it's… Yeah, we update it, we… that will probably be fixed. And also.
Now there is the… Bam.
There is the import only.
Option in the language.
Which, I don't know, might fix this.
But at the same time, I don't know if… ZRPC is still being used by many users to explore OTL. Oh yeah, that'.
**Bryce** 40:10 Okay.
I'm remembering. Now, this is like building a, yeah. Evolution.
**Nacho Bonafonte** 40:17 framework.
**Bryce** 40:17 Yeah. Yeah.
**Nacho Bonafonte** 40:19 For an XC framework, probably it's a limitation. Yeah. If we build everything to an XC framework.
**Bryce** 40:25 Yup.
So, I think… This is good to remember, but I don't think it needs to be opened.
open to remember that this is a problem, and one of the reasons why we can't make an XC framework?
Should we just close it?
Or do you want to keep.
**Nacho Bonafonte** 40:47 Yeah, I think so. I think that also… It will be an issue for us if we try to create a new XC framework again.
And the version of the ZRPC library is still limiting us, because I can expect Apple will have fixed By now, but that's only 2 years ago. Who knows?
**Bryce** 41:11 Yeah.
Vladimir, you have a question?
**Vladimir Kukushkin** 41:18 A question, a comment about Swift Neo and Library Evolution Sport, Swift Neo doesn't officially support this mode of building.
**Nacho Bonafonte** 41:29 Okay.
**Vladimir Kukushkin** 41:29 plan, and, and it's general for, generic for all the… Packages we have in the open source.
So it most probably won't be solved by updating to a new GRPC.
**Nacho Bonafonte** 41:43 Okay.
**Bryce** 41:44 Good to know. Yeah, I mean, it seems like the whole XC framework, support is kind of on the wayside anyway, so…
**Vladimir Kukushkin** 41:54 Yeah, the idea behind this is a Swift Neo, he is distributed as the Swift package, which is the source distribution, so it is expected to be source stable, not ABI stable, and library evolution is on the ABI stability.
**Nacho Bonafonte** 42:12 Okay.
**Bryce** 42:13 Cool. Alright.
There you go. There you have it.
Okay, so, slow freeze render detection. I think this is still relevant, Well, hmm, so… this is kind of, A part of the metric kit, instrumentation, isn't it?
I don't know if we want, like, a more… robust… instrumentation.
**Nacho Bonafonte** 42:43 Yeah, I think… metric, it shows that, precinct, right, in the organizer in Xcode for their apps.
So probably it's reaching also the app.
preview.
If you… yeah, if you… ask… But yeah, definitely it's… it's… it's a feature to… to have, because it's interesting for observability of farmers.
Yeah, let me…
**Bryce** 43:15 So, I think we can review if that's actually solved by MetricKit or not.
Alright, backtrace support, always a thing. VisionOS support, hey, we got that, don't we?
Closed.
Swift metric to Swift Metric Stable Schum and RE2 and GA MER.
**Nacho Bonafonte** 43:35 That's… Yeah, I think we can close that also.
**Bryce** 43:43 Yeah.
Add an Apple distributed tracing importer.
**Nacho Bonafonte** 43:50 We'll trade that now.
**Bryce** 43:51 We have that now.
Add an importer for Swift Logs. That… do we have that? We have that.
**Nacho Bonafonte** 44:00 We have that now, right?
**Bryce** 44:04 I think so.
**Nacho Bonafonte** 44:05 Yeah.
**Vladimir Kukushkin** 44:08 Yes.
**Bryce** 44:11 I'll take your word for it.
mobile conventions… where are Android and iOS conventions being defined?
**Nacho Bonafonte** 44:35 Yeah, I think it's on clear insight to me.
**Bryce** 44:41 What's that?
**Nacho Bonafonte** 44:43 Yeah, I, I, yeah, that, that… That's in the semantic conventions and the client side, right?
**Bryce** 44:48 You know…
**Nacho Bonafonte** 44:49 So, it's not about… explicitly us.
**Bryce** 44:54 Alright. Well, I'm gonna close this then.
We'll go back to issues… Swift 5.9 doesn't support iOS 12, and blah blah blah.
**Nacho Bonafonte** 45:07 And probably we won't support either sooner.
**Bryce** 45:13 Alright, Okay.
Interesting.
**Nacho Bonafonte** 46:01 Yeah, basically, I think we can close that. Yeah, basically it's the same about the version we want to support.
**Bryce** 46:07 Yeah.
**Nacho Bonafonte** 46:08 Yeah, and the minimum version, because we can probably take a cut with the version that App Store.
At the minimum versus what type.
And take the version from there.
Because… I think only… Xcode.
Sixth.
It was 18, before the Xcode 26.
Or 16, I don't know, but basically, that's the… not the current, but the previous one is the latest one, supported.
That really makes the cut, except for Mac OS, that you don't need to go through the App Store.
That has always been our adapt, but… I don't think we currently have so many users on Mac.
that… are using all tools for support, I don't know. But yeah, probably we can go that route.
**Bryce** 47:04 Yeah. Well, I mean, the thing is, is that older versions of the SDK will still support those versions, they just won't get any updates.
I can still use it.
explicit static library types cause duplication of library. I don't know if there's a lot that we can do about this, right?
**Nacho Bonafonte** 47:33 Yeah, this is another of these teams with… We, we, we, at the beginning of the library, we had many problems having dynamically libraries defined.
**Bryce** 47:42 Yep.
**Nacho Bonafonte** 47:43 Because users were having lots of issues building something.
So we moved to Estati.
And everyone was happy with Dennis.
Who was also unhappy with many other things, in that period.
**Bryce** 48:02 Right, right.
**Nacho Bonafonte** 48:05 So, yeah, I don't know how we are… Not currently doing, but…
**Bryce** 48:10 Well, the alternative is, what if they're used, like, okay, so you've got duplicate libraries, package A, package B, both using OpenTelemetry API, but what if they're running different versions, right?
**Nacho Bonafonte** 48:24 Yep.
**Bryce** 48:24 And so we avoid duplication, but then if there… there's going to be a version mismatch if we try to avoid duplication, so I don't know if this is… this is, like, an intractable problem with SPM.
**Nacho Bonafonte** 48:36 Yeah, yeah, especially if there are several libraries linked in the same app at the end, which have different versions of third parties that end up being the same, yeah.
I think we can close it. It's working with how we have it now.
And we have had no… Users reporting problems with our current setup for a long time now.
**Bryce** 49:07 Well, we're at time, so we can probably call it here.
**Nacho Bonafonte** 49:13 Okay, yeah.
**Bryce** 49:13 I was very productive. I'm gonna try to fiddle with the agent thing and see if I can't get it to actually do more in-depth reviews of the issues, and see if there's any issues that are open that have been resolved.
And see what comes out of that. Maybe I'll have it make an issue that marks all of the issues that it thinks are… you know, fixed already, or… or, no longer applicable.
**Nacho Bonafonte** 49:42 Yes.
**Bryce** 49:44 Alright, thanks everybody for… coming to the meeting today, I hope you all have a nice rest of your week.
**Vishwan aranha** 49:53 Thank you, you too.
**Nacho Bonafonte** 49:54 Yep.
**Yasura Dodo** 49:54 They're cute.
**Nacho Bonafonte** 49:55 Nice weekend.
**Yasura Dodo** 49:56 Bye.

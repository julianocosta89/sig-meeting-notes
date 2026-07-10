SIG: Swift SIG
Date: 2026-07-09
Duration: 25 minutes
============================================================

## Zoom Recording Transcript

**Zoom user** 00:35 Oh, hey, Vinod.
**Vinod Vydier** 00:38 Hey, hey, good price.
Yeah, you look different with the… I think you're on a bigger monitor or something right before. Now you come close to the with camera.
**Robert Magnusson** 01:42 Hello, sorry for being late.
**Zoom user** 01:57 Hi there.
I'm just waiting for some people to join.
Hmm, okay.
Hey, Vinod, can you hear me?
**Vinod Vydier** 03:16 Yeah, I can hear you.
**Zoom user** 03:17 Okay, alright.
I wasn't sure if, if my audio was working or not.
Okay.
**Vinod Vydier** 04:22 Did we do the depreciation, note?
**Zoom user** 04:27 Yeah.
**Vinod Vydier** 04:33 I think maybe we should put it on the… The hotel community blog or something like that.
That's a good.
**Zoom user** 04:41 Yeah, there's a… there's a PR out for that right.
**Vinod Vydier** 04:43 Okay.
**Zoom user** 04:46 Let me just do.
So let's bring this forward.
And… Bring this forward.
Okay.
Alright. Concurrency issue, that's been fixed. That's good, so… Builds have resumed, and PRs are… it looks like they're all building correctly now… And… I think CORE is also looking good as well.
Yep.
**Vinod Vydier** 05:39 This is a concurrency issue.
Migration, right? 53. Issue 53.
**Zoom user** 05:45 Yeah, I haven't had a chance to actually, like, dig into what caused the sudden build failures, but… Yeah, it was… it did have to do with, Swift six concurrency, and the, like.
You know, tagging stuff as, As, not actors, but the, I can't remember off the top of my head.
But yeah, so that's all, that's all been taken care of, so that's good This is still to do.
I need to make an issue, or I think there's an issue, but I just haven't had time to work on this.
But, yeah, this is… Oh.
This is on my to do list.
Alright, let me pull up this… PR for the blog site, I think that… There's some… Issues that need to get handled By the… by the… whoever works on the blog stuff, like, apparently there's not an iOS… like, an iOS section that they need to create. I saw there was a… Issue opened.
But maybe, actually, maybe this can just be merged if we can approve it.
Oh.
Ch-ch Oh, oops, that's not There we go.
Oops.
- Oh, that's the issue.
That's the issue.
**Robert Magnusson** 07:56 Where do they end up? These blog posts on, like, the official OpenTelemetry.
**Zoom user** 08:00 Okay.
**Robert Magnusson** 08:00 It's.
**Zoom user** 08:01 Yeah, that's where… that's where it'll Let me actually get the blog. I grabbed the issue on accident.
**Vinod Vydier** 08:16 And there's an example like the they have the zipkin export as our.
They had a blog, right?
We can make an entry like that.
**Zoom user** 08:35 Okay, there we go. Alright, so there's the blog there. It's Ari wrote it. I made some edits to it, but it's mostly unchanged.
And I think we're just waiting for… oh, there's some issues setting to… The markdown linter is mad, so I'll need to take a look at that and make sure let's figure out what's going on Alright, CodeQL, that's breaking everything. That was part of the… part of the concurrency issue, so that that was fixed, I'll just remove that.
This is still to do.
All right, come on.
Does anybody have any topics they'd like to discuss today?
**Robert Magnusson** 09:44 Nothing in particular. My PR that I opened, I think it's green, I think you approved it,
**Zoom user** 09:49 Yeah, I just want…
**Robert Magnusson** 09:50 Hey, boss.
Yeah, sorry.
**Zoom user** 09:52 No, yeah, I was just waiting for… because I think… I looked through it briefly, and it looks good to me, and it looks like it's already been reviewed by Will, and I was just… Letting the, other maintainers to have a chance to look at it, But, I guess, yeah, since nobody else has really said anything, I think that we can… I can merge that after the meeting.
No problem.
We got a couple of other things stacked up as well.
And so, I think we'll get those all merged. I think I got them all approved.
And I was just letting them settle a little bit and let the other maintainers look at them all. But we'll get a release ruled after all that gets merged.
**Robert Magnusson** 10:41 Cool, thanks.
**Zoom user** 10:42 If…
**Robert Magnusson** 10:43 there's no, like, active topics. Like, my goal is to try to get a bit more involved in this community. Are there, like, good first topics to tackle? I saw you have these good first issues to…
**Zoom user** 10:54 Yeah, we can take a look at it.
**Robert Magnusson** 10:56 Yeah, that'.
**Zoom user** 10:57 We can take a look at them.
There was one thing I just wanted to discuss, Maybe for anybody who is gonna be watching this recording. But, I took a look at that, URL session instrumentation PR that… That was opened a little bit ago, and there was we had some discussion about it yesterday or last week.
and we weren't really sure what the intention was, but, I took a deeper look at it and pulled it and did some testing with it, and, The main contention was with this block here where the completion handler is being called in the instrumentation. And now I realize the cause of this was because what's happening is the poster.
wants the, this instrumentation to occur, whether or not the delegate actually implements this method. And, I think that… I made a note on the PR, down here that kind of just briefly… describes my concerns, but the, the TLDR is, the… instrumentation, the URL session, library changes depending on — its behavior changes depending on which methods are implemented. And I think that the main reason, if I recall correctly, the main reason why we didn't want to — Force, methods on the delegates is because there's also the non-delegate callbacks on the methods, or on the, on the, download, or on the tasks.
And if those methods on the delegate exist, then those callbacks won't get called, so we don't really know what a implementer is going to be using at the time of instrumentation, so we need to avoid You know, adding stuff to delegates that aren't there, whether intentional or not.
So, I think… What we might want to do is add a little more, documentation to the instrumentation as to why we made that decision, because I think the main issue was that Simon was just confused about this behavior and didn't understand why that was.
**Robert Magnusson** 13:28 That…
**Zoom user** 13:29 is that topic. All right.
But yeah, let's look at some new first issues for you to… to dig into.
Oops.
Bring this over here. There we go.
Oh.
That's a new one. 2 weeks ago, I didn't Okay.
I don't think that we've been very good at keeping up what a good new first issue might be.
And some of these might even be…
**Vinod Vydier** 14:15 I think a lot of it has been, you're tag some of them.
you know.
**Robert Magnusson** 14:21 I mean, in general, it's tough to keep a good shape of your issues.
**Zoom user** 14:25 Yeah, that's.
**Robert Magnusson** 14:25 thesis thing.
**Zoom user** 14:26 It's true. Yeah. Especially when it's like, not your day job.
**Robert Magnusson** 14:30 Yeah. Okay.
**Zoom user** 14:31 Okay.
Oh, boy. Okay, so… let's just… let's just take a look. So, Swift packages for OTEL exporters for traces, metrics, and logs. What is this? I don't even remember.
**Vinod Vydier** 14:48 Alolita has been actually.
**Zoom user** 14:51 Yeah. She's been pretty pretty helpful.
The package should be evaluated for spec compatibility. Okay.
You know, one… okay, so… this actually reminds me, and this might be a good… like, if you want to really kind of wrap your head around OpenTelemetry as a whole.
**Robert Magnusson** 15:12 Yeah, I.
**Zoom user** 15:12 Something like this might be really good to look at. I know that one thing specifically that we need to, really review is the tracing implementation that we have. Because it was one of the very first things that we implemented.
**Robert Magnusson** 15:33 It'.
**Zoom user** 15:33 It's been quite a while since we've actually reviewed, because the spec's been kind of been changed a little bit. And so things like trace events, I know, are getting deprecated, and we haven't really removed those yet.
**Vinod Vydier** 15:46 Final events.
**Zoom user** 15:47 Yeah, so doing, like, an audit of the OpenTelemetry spec.
against our implementation, I think that would be a really good place for you to… if you, like, if you really wanted to become, like, you know, locked into the… to how it… how it works and what the spec is.
That would be a really great place to look into, and you don't have to necessarily do any code changes.
But just creating issues based off of the difference between the spec and our implementation would be really helpful.
And then from there, you can start implementing that.
**Vinod Vydier** 16:24 And I should do that too, so… Maybe we can do that in parallel.
**Robert Magnusson** 16:30 But that's specifically maybe the tracing, because I just recently built some tracing also support for Dart. So it might be a good… It's a good area to cover them. That's a good tip.
**Zoom user** 16:51 Dependency dashboard. Hmm, that's interesting. I thought we had an issue for it somewhere, but apparently not.
**Robert Magnusson** 17:01 Can… Can non-maintenance create issues? Yes. Yeah. Okay. So I could also just take that on me and explore and… And create an issue for them.
**Zoom user** 17:13 Oh, here. I think that we might — here. Yeah, tracing spec review. Here you go.
**Robert Magnusson** 17:17 Okay.
**Zoom user** 17:18 Yeah, so I've already kind of broken down all the different, Aspects that need to get, kind of, reviewed. And, yeah, so follow-up, I've created a follow-up issue here.
And so… Yeah, so even there was this one here.
Somebody's actually already done a little something. Yeah, so there's this one.
Here, let me add this to the notes here.
And that, I mean, that's a pretty big… A pretty big task, in and of itself.
**Robert Magnusson** 17:58 Mmh.
**Zoom user** 17:59 Let's just take a look at good first issues here.
again.
Oh, interesting.
Log errors went… yeah, so another… yeah, these ones are, are also good ones.
Yeah, there's a lot of spots in… both core and… the main repo, where we just have, like, errors stubbed out.
**Robert Magnusson** 18:42 Is this the thing where you talked about last time with this error handler or something?
**Zoom user** 18:47 Yeah, yeah, yeah, so, in, In core, we don't — to reduce the size of the package, which is why core exists in the first place, is because a bunch of people just wanted the API and SDK and nothing — no instrumentation or anything on top because they wanted to do their own implementations.
To reduce the size, we did not want to include the Swift, logs.
And so… we were just gonna use OSLog, but that's not supported on Linux, so we had to stub out, like, a log handler, basically.
**Robert Magnusson** 19:26 And the Swift log, that's the one from Apple, so visual.
**Zoom user** 19:29 Yeah, that's Apple's official one, which is only supported in, I think we support an older version of.
**Robert Magnusson** 19:37 Okay.
**Zoom user** 19:38 Watch OS.
than Swift Log supports, so even if we wanted to, we'd have to bump that up, and I think people are hesitant to do that, because there's a lot of people on old stuff that want to keep using it, so… Let me see.
Yeah, and so there's actually — that's this.
Where is it?
Yeah, create an issue to add feedback handler to stubbed error message locations. Yeah, so that's in Swift Core.
Yeah, Swift port to do. So, yeah, that's… that would be.
Issue as well, you'd have to make it.
Let's see.
Yeah, and so this kind of falls into that as well. Add gRPC with TLS example.
Pretty straightforward.
Just, yeah, right, right out, yeah.
That's a good, like, acquaint yourself with how to boilerplate yourself OpenTelemetry Swift.
Ch, ch, ch.
Interesting. That's really old.
**Robert Magnusson** 20:55 I think doc C, that's this auto documentation. What is that again?
**Zoom user** 21:02 Oh, I don't know.
This was… I think this was just something that sounded interesting, and then… Introduce a WWDC.
**Robert Magnusson** 21:10 There you go.
**Zoom user** 21:11 2021, so that's a little old. We can probably just close that one.
Da-dum-dum Is that a good first issue? I don't know about that.
Create an Objective-C-friendly library. That doesn't seem very —.
**Vinod Vydier** 21:34 Okay.
**Zoom user** 21:35 It's.
**Vinod Vydier** 21:36 It's, yeah.
The small tutorial would be a good one, actually. We don't still have a good iOS app in the repo, right, in the example.
**Zoom user** 21:47 Yeah. It's true. Yeah. That would be useful as well.
**Vinod Vydier** 21:50 There are some examples on the swift docs and the open telemetry, which is like mostly server side.
**Zoom user** 21:56 Yeah, yeah.
**Vinod Vydier** 21:58 And most people are not really using it for server side, so.
It's not really useful.
**Zoom user** 22:05 Yeah, it might actually be better just to look at issues in general.
That one can probably be closed. That was just a question.
This is a weird one, that's probably not a good first issue.
These metric ones might be… might be good ones, because they're just, like, small little snippets of, implementation.
Oh.
**Robert Magnusson** 22:55 Right.
**Zoom user** 22:56 But if you're not familiar with, like, the metric system is kind of… The, the spec is pretty.
**Robert Magnusson** 23:01 Yeah, I mean, it might be a good way to learn it also. I'm actually… I didn't work with metrics, just logs and traces, so it might be a good way to…
**Zoom user** 23:10 Yep, so any of these metrics.
**Robert Magnusson** 23:12 Okay.
**Zoom user** 23:12 Good one. Just to get your get get acquainted with it.
Thread safety in the metrics. I thought this one.
**Robert Magnusson** 23:20 you tend to work with this, then you assign yourself as working on it, or you just basically work on it and open a PR then?
**Zoom user** 23:27 Say again.
**Robert Magnusson** 23:27 This is not, how do you work with these issues?
**Zoom user** 23:30 Oh, you.
**Robert Magnusson** 23:30 Assign yourself to it.
**Zoom user** 23:31 Yeah, yeah.
**Robert Magnusson** 23:32 You work on it, and then…
**Zoom user** 23:33 Yeah, if you want to assign yourself to it, yeah, yeah, that's a great way to do it. Just to let, yeah, let other people know that you're working on it.
**Robert Magnusson** 23:46 Yeah, I think they have enough.
Neat to start with.
**Zoom user** 23:50 Damn.
**Robert Magnusson** 23:51 Okay.
And I will try to join these meetings, it's a bit late for me, I'm Germany-based, so whenever my wife says okay, I can join.
**Zoom user** 24:00 Yeah, it's like 6:00 PM.
**Robert Magnusson** 24:02 Yeah, exactly. So she's out now with the kids down at work.
**Zoom user** 24:05 Yes.
**Robert Magnusson** 24:06 But I will try to join as much as I can these meetings.
**Zoom user** 24:09 Cool, yeah. Yeah, if you want to just do updates in the, in the Slack.
**Robert Magnusson** 24:13 I am Sl.
**Zoom user** 24:14 Yeah, cool.
Cool, yeah. So those are all, all good first issues. If you have any questions about anything, yeah, feel free to ask in the Slack, and we'll try to help you.
**Robert Magnusson** 24:26 Cool, thanks. You're all based in.
**Zoom user** 24:28 Actually, no, so I think, Well, I know that Nacho's in Madrid, and I think Ari is in,
**Vinod Vydier** 24:38 He's in the service. Yeah, he's in the service, yeah.
**Robert Magnusson** 24:42 Okay.
**Zoom user** 24:45 And Vinod, you're in Atlant.
**Vinod Vydier** 24:47 No, no, I am in St. Louis.
**Zoom user** 24:49 Oh, okay, okay, very good.
**Vinod Vydier** 24:51 Central, yeah.
**Zoom user** 24:54 All right.
Anything else?
Cool. I'll take this, the rest of this time, then, to go through and, get some of those PRs merged.
Alright.
**Vinod Vydier** 25:08 Yes.
**Robert Magnusson** 25:08 Cool, thanks.
**Zoom user** 25:09 Bye, everybody. Have a nice day.

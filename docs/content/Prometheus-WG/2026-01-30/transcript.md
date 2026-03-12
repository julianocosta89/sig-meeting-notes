SIG: Prometheus WG
Date: 2026-01-30
Duration: 65 minutes
============================================================

## Zoom Recording Transcript

krajo Krajcsovits 00:03:37 Hey.
Arve Knudsen 00:03:38 Hello!
krajo Krajcsovits 00:03:41 Hello.
Arve Knudsen 00:03:43 I thought this meeting wasn't going to happen.
Yeah, but I think also David Ashbel is, joining.
krajo Krajcsovits 00:03:51 Oh, okay, okay, cool.
Arve Knudsen 00:03:53 Hello, David.
krajo Krajcsovits 00:03:54 That's a bit.
David Ashpole (dashpole) 00:03:55 I hate it.
krajo Krajcsovits 00:03:56 Long time noisy.
David Ashpole (dashpole) 00:04:01 One sec, the Kubernetes instrumentation sig is finishing up.
krajo Krajcsovits 00:04:10 It's doing what? Sorry, pushing up?
David Ashpole (dashpole) 00:04:16 The instrumentation stage is finishing up.
krajo Krajcsovits 00:04:27 Okay, I'm probably out of the loop on… I don't understand what… what are…
David Ashpole (dashpole) 00:04:56 Alright, cool, sorry.
Okay, looks like… Got two agenda items.
Should we get started? Looks like Arthur's not gonna make it.
A penderv2.
It shouldn't have much of an impact, right?
krajo Krajcsovits 00:05:52 Yeah, I'm surprised by this text here, because Bartak said that it was actually going well.
David Ashpole (dashpole) 00:06:03 Well, V2.
Arve Knudsen 00:06:18 So his author specifically means the OPPO collector, Prometheus receiver, right?
Just searching from his PR.
David Ashpole (dashpole) 00:06:30 Dude.
Looks like he copied everything instead of trying to… or he rewrote it.
I don't.
What's… what's he looking for? Doesn't seem to be an easy transition.
krajo Krajcsovits 00:07:05 If anything, it should be handling less state.
Or, I mean, it… we are… Providing the exact same data in Opender V2.
So, yeah, this is a little bit strange. Maybe we can help out one… We do… when we're done with the Prometus side, meaning Bartak and myself.
I mean, I wrote code into… the point is this server as well, and touch this part of the code, actually, because of net histogram, so… I got some.
-Oh.
Knowledge about it.
David Ashpole (dashpole) 00:07:45 I was wondering, for the transition, is there a way for us to, like.
do the refactor in small pieces, like, implement the append V2 with all of our V1 functions, and then slowly unwrap them or something? Do you know what I mean?
krajo Krajcsovits 00:08:00 Yeah.
I… think so.
David Ashpole (dashpole) 00:08:06 it's just hard, always, with these, like, 2009… we've rewritten the whole thing for a new interface, so I don't know if… that's my only feedback, is… like, I love the prototype, but it's great. It should be a great performance win, right? In theory?
krajo Krajcsovits 00:08:23 That's what I heard, I haven't seen, but that's what I heard, yeah.
David Ashpole (dashpole) 00:08:28 There's some benchmarks on this. Did he post some more?
Well, I'll leave a comment with… that feedback.
krajo Krajcsovits 00:09:00 Sounds good.
David Ashpole (dashpole) 00:09:01 And then he wants us… He wants someone to review the other timing change PR, speed… the speed up test PR, which I will do.
I have no issues with it.
krajo Krajcsovits 00:09:22 Speed up.
PR?
David Ashpole (dashpole) 00:09:26 Where do you see this?
krajo Krajcsovits 00:09:28 Oh, the alternative, oh, okay, okay, I didn't.
Oh yeah, I think we talked about this… Ignore.
Skip soft setting… Oh yeah, I might have done the same in Prometus already, or maybe I just used it, I don't remember. But that's probably okay, yeah.
Not that I read the whole thing.
Arve Knudsen 00:09:59 It's an alternative to switch those tests over to sync tests instead.
krajo Krajcsovits 00:10:05 It's… I would consider it a workaround, not an alternative, but…
Arve Knudsen 00:10:12 Don't…
krajo Krajcsovits 00:10:12 Got it.
Arve Knudsen 00:10:13 is using SyncTest a workaround, really?
krajo Krajcsovits 00:10:16 No, using this skip off setting to just lower the timeouts is a workaround.
Arve Knudsen 00:10:22 Yeah, yeah, exactly, that sounds more like it.
So… so… So it… we're just thinking it takes too long to migrate to sync tests?
David Ashpole (dashpole) 00:10:38 Nobody's… nobody's been able to get even a very small test working properly. Something about… I haven't tried, so I can't speak to, like, the actual issues, but basically, it has something to do with, like, or what is it called, like, a bubble or something? Basically, like, we can't figure out what to put in or outside the bubble so that it stops at the right places and doesn't just block on, like, network I.O.
Arve Knudsen 00:11:02 Yeah, I don't think you can have network I.O. in the bubble. Like, I know this because I ported several Prometheus tests, two sync tests.
And I'm not gonna lie, I let Claude do it for me. But it needed a bit of, let's say, curation in retrospect to get the details right.
David Ashpole (dashpole) 00:11:25 Yep.
Arve Knudsen 00:11:25 But I think it's much speedier if you just let the, if you just let Claude kind of do the basics, and then you kind of arrive at something that works. So I ported things.
David Ashpole (dashpole) 00:11:36 I think it's arriving at anything that works that we're currently blocked on.
Arve Knudsen 00:11:39 Yeah, so, in the case of those tests, I… I had to fake, each of the vehicles, basically. And that was okay, because… because you kind of want to test the handling of a certain sequence. It's not really interesting to test the integration you can test in other tests, if you see what I mean.
David Ashpole (dashpole) 00:12:02 So, when you say fake the HTTP calls, I think the question is, from the perspective of the OpenTelemetry collector, where we can't, like.
like, as far as I know, we have to actually… we can't, like, modify the scrape code or anything, right? Or inject any fake handlers or request makers or anything like that, right? We would need upstream changes, I guess, to support that. Do you think that it's possible for us in the OpenTelemetry Collector.
Prometheus receiver to actually… somehow test.
That are trans… that, like… There's an endpoint, or, like.
I start with a file, it has some data that I want to be scraped.
And I want to somehow configure the Prometheus receiver.
to get that, right? And it uses the Prometheus scrape library, and then I want to see the results of the translation and validate it against some OTLP, right? That's… that's what, like, all of our tests are doing. And right now, they just literally bring up a Prometheus server, or, like, inside the receiver, right?
tell it to scrape, wait for the scrape to happen, wait for the data to come, and then look at it and do some tests against it, right?
Arve Knudsen 00:13:18 I'm unfortunately unfamiliar with these tests. I can only speak to my experience from the Prometheus… these Prometheus tests. I think the particular tests I fixed were maybe for the alert manager, I think.
David Ashpole (dashpole) 00:13:30 I see. Okay.
All I would… all we would want is, like.
Yeah, I think the… the thing that we would need to unblock us is, like, an MVP of… Here's, like, A text file with a counter.
And here's how you can tell the Prometheus Like, even just executing the scrape Manager. Like, can you… And test just for the scrape Manager that, you know, like, pretends to scrape.
an endpoint, right, that serves a thing, and then validate what we get out of it, right? Because that… then we can add on and add on, and add on, and… Get it in, but, like, even just the simple case of, like.
Test that you scrape an endpoint and get the up metric back isn't something we could do today.
Arve Knudsen 00:14:18 Yeah, I see what you mean, like, I think I would need to look at, a concrete test, and then as a use… as a case, you know, and then see if… See what can be done about that one, as a… Proof of concept.
David Ashpole (dashpole) 00:14:35 You want me… Do you want a… OpenTelemetry Collector Prometheus receiver test that is simple enough that you can Like, throw some agent at it and see if you.
Arve Knudsen 00:14:46 Sure, that sounds good, because that… because I'm just looking at Arthur's issue, and that's exactly what… what issue's for, right? Like, Prometheus receiver tests.
David Ashpole (dashpole) 00:14:56 Yes, yes.
Arve Knudsen 00:14:57 So I think I would just need an example, because I couldn't really see it in the issue. Maybe I'm missing something.
David Ashpole (dashpole) 00:15:04 Find.
Matrix Receiver Test.
Arve Knudsen 00:15:07 Hotel repositories are, in general, much less, understandable to me, like, they're a bit, to me, it's a bit of a bit chaos, chaotic, I mean, still.
Oh, dear.
David Ashpole (dashpole) 00:15:25 Okay.
Arve Knudsen 00:15:33 So, no, I'd be happy to take, like, an example test, and then I can see… If I can do something about that.
Like, I've been doing a lot of, fixing your tests lately, lately in Prometheus to get rid of lakiness, because I was going crazy, because… There was so much flaking, I think after fixing 4 tests or something, there are still more flaky tests.
Where's the…
David Ashpole (dashpole) 00:16:05 Where's the issue?
Here.
Okay, I'm gonna post some stuff then in the…
Arve Knudsen 00:16:19 So, I kind of… I was kind of left with the impression that this is, like, an endemic problem in the Prometheus, test suite.
That you have a lot of tests which are timing-dependent.
And they are typically flakier under CI, because of constrained, resource, constrained resources, probably.
krajo Krajcsovits 00:18:50 Are you looking for those tests?
David Ashpole (dashpole) 00:18:53 I'm… sorry, I'm copying a whole bunch of links.
krajo Krajcsovits 00:18:55 Oh, okay, okay, okay.
Because there's no… There's a file that has protobuf In the name, that's… those are very simple, they're just as you know, if you can…
David Ashpole (dashpole) 00:19:06 Oh, yeah.
krajo Krajcsovits 00:19:08 For… that's… One of them.
Aww.
I can't…
David Ashpole (dashpole) 00:19:17 You can also paste.
krajo Krajcsovits 00:19:18 Yeah, yeah, I'll do that as well.
David Ashpole (dashpole) 00:19:21 Yeah.
krajo Krajcsovits 00:19:24 I can just click fast enough.
Receiver… What does it say, huh?
Yeah, for example, this… Yeah, so there's a link.
David Ashpole (dashpole) 00:20:39 road.
krajo Krajcsovits 00:21:25 Okay, anyway.
David Ashpole (dashpole) 00:21:28 Good.
I pasted a comment there as well. Hopefully, maybe that's helpful.
Great.
Crap, you have two topics.
krajo Krajcsovits 00:21:46 Yeah, yeah, one is, I asked, What's our expectations on the stabilization?
This is for planning purposes.
And, I was hoping that Arthur would be here, but then I saw that he wasn't going to be, so I asked him on chat, and he said, it's kind of undefined, so that's what I… Convey to my manager.
And, Yeah, so unless you have another opinion, or you have an idea, then don't hesitate to tell me, but we can.
David Ashpole (dashpole) 00:22:20 I mean, do we know if the collector SIG?
Has… Has stated any… The orchery Collector.
I'm sure they'd love to have it by KubeCon EU, but… Hmm… Everyone, on track.
On track for when.
It's on track.
As of last August.
krajo Krajcsovits 00:22:58 Nice.
It doesn't matter, my managers are, like, Fine with it.
David Ashpole (dashpole) 00:23:10 Okay.
krajo Krajcsovits 00:23:12 Yeah, and the other… topic I have is just… just a note, just to notify you that I'll be… More active next quarter.
David Ashpole (dashpole) 00:23:23 Okay.
krajo Krajcsovits 00:23:25 So we have a reorg, and my team is being folded into Mimir.
But, like, memory is split into more teams, so our team is… like, not responsible for a lot of things, so… well, responsible for just a few things in the mirror.
So… And the idea is that we will have time for Especially OpenTeametry, stuff that is related to Promitus and Vimir.
So… and my personal OKRs have it that I've… I've tried to… step up from being a member on Pantamata to maybe approver.
You know, ideally, maintainer.
So, that would be the goal.
David Ashpole (dashpole) 00:24:13 Yeah, that'd be awesome. Even… Yeah, I feel like this group has a lot of people who know a lot of things, and are… would be… generally good.
good leaders in the OpenTelemetry broader community. So, that's good to hear.
krajo Krajcsovits 00:24:31 Yep, okay.
Other than that, I don't know, if we don't have other topics, we could do some triage, because that's… first step for me would be to get back into Reviewing stuff, and maybe working on things, so we could… Assigned me some review or something?
David Ashpole (dashpole) 00:24:54 Yep, yep. Let's find the project board.
Where is our project board?
It's probably linked from the SIGNotes.
Like, when I went to the black mode screen, your face got darker.
Yeah. I turned off the lights in the room. Okay.
This is good. Eliminate time dependency and tests.
documentation. Let's look at some of these… So these are workable.
Oh, and we have a PR.
We have many PRs.
deprecate it. So this is just about graduating the feature gate, I think?
Right? So we have… We promoted the feature gate to beta, and then it'll presumably go stable.
Great, yeah.
When was that? Last week, yeah. So, we'll probably need to… let's see what release this one went out with. I guess we'll give it one release. I can't imagine that, like, this is gonna be super breaking for people, so I'm happy to.
krajo Krajcsovits 00:26:22 Yeah.
David Ashpole (dashpole) 00:26:24 Boom, boom, boom.
Let's see where…
krajo Krajcsovits 00:26:27 Although, you never know how people use things.
David Ashpole (dashpole) 00:26:32 You do.
Why is this?
Oh, because I have to look at the merge.
Okay, so it hasn't been released yet.
And the latest tag is… 144.
So, this will be released in 1.45, so we can… Zero dollar.
True.
just change this. Can I… can you drag and drop here?
Yeah, cool.
This needs someone to work on.
But I think Arthur… Help wanted. Okay, so this… I think this is workable, it just is a big task.
So it… Yeah, same with the eliminate time dependency, honestly. Like, these are both significant, stuff.
Significant projects.
Okay, we do definitely need a bunch of docs, but… It's like… Classic. We have a week until… stability. Let's publish some… Better dogs.
Community support. I feel like it's workable, though.
Like, we just need to add a bunch of stuff to the README.
krajo Krajcsovits 00:28:36 Hmm.
David Ashpole (dashpole) 00:28:37 I think it needs maybe to be scoped out, like.
Someone could write a, here are the things we're gonna improve.
me support.
krajo Krajcsovits 00:28:51 Yeah, we talked about that last time, I don't, what did we say?
Well, yeah, that's why I remembered the triage.
David Ashpole (dashpole) 00:29:19 Is everyone here okay with closing it? I feel like we're not… I feel like we are gonna keep… Doing what we're doing, and it's like… Mostly good.
krajo Krajcsovits 00:29:30 Yeah.
David Ashpole (dashpole) 00:29:31 We have the most popular component, so, like, we're never gonna be… Perfect, but we're mostly on top of things, I think.
Arve Knudsen 00:29:38 I don't have a lot of context, so I'll leave.
David Ashpole (dashpole) 00:29:40 This is just, like… How can we do a better job of… what's the bar that we need to meet in terms of providing support on issues people report?
in the collector.
Are we doing good enough? Do we need to make process improvements to do better?
I… I sort of… I feel like we're probably doing good enough.
And then the spec, Arthur opened a PR, and I think we can start having more PRs to discuss next time.
But I feel like there should be some easy initial wins, just in terms of… Like, marking the counter.
you know.
Mapping a staple, things like that. So… Hopefully we can start making progress on that soon.
So, okay, if we hop over to the collector contribib and start looking at our stuff there?
krajo Krajcsovits 00:30:30 Yeah, yeah, yeah.
David Ashpole (dashpole) 00:30:32 I'm gonna mark this as can be worked on.
Would we have a triage link somewhere?
krajo Krajcsovits 00:30:47 I don't know, I usually just.
David Ashpole (dashpole) 00:30:48 Yes, we do, we do.
krajo Krajcsovits 00:30:49 Oh, wow, okay.
Nice.
David Ashpole (dashpole) 00:30:53 So, in the meeting doc.
Can you see the meeting, doc?
krajo Krajcsovits 00:30:59 not on your screen, but I can see it.
David Ashpole (dashpole) 00:31:04 The screen.
Yep. Okay, cool. So we've got 4 issues.
Maybe we'll… Oh, yeah, yeah, so this is one that I asked to be open. So, for context.
The Prometheus code has support for the underscore created series in the parser, but that, at least at one point in the past, had some performance issues.
This person would like to… And so we… we've put it behind a feature gate.
So we don't… we, I think, turn it off in Prometheus, unless… You turn on our feature gate.
And there have been some performance improvements in Prometheus, but I guess it's not enough.
Or…
krajo Krajcsovits 00:32:02 Yeah, it's another thing, yeah.
David Ashpole (dashpole) 00:32:05 So, the question is, like.
I allowed this person to merge a PR that added the parsing support in the Prometheus receiver itself.
The question is, because we're already doing a bunch of matching and stuff, right, and And so the question is, like.
basically, can we fix this upstream, or are we gonna be, I'll say, stuck with having our own understore created time series parsing in the receiver forever? Which isn't the end of the world, but… so that's all this is covering.
krajo Krajcsovits 00:32:43 Well, the problem with the created timestamp in OpenMetrix 1 is that It's very hard to efficiently, bars.
So I don't think that's ever going to… really work.
David Ashpole (dashpole) 00:33:00 Here's the issue, that… It's blocked on.
krajo Krajcsovits 00:33:11 Yeah, nobody's working on this.
David Ashpole (dashpole) 00:33:13 So… Yeah.
This is due to deep copying of parser on every created timestamp, so technically every series.
This was a known, naive implementation that they accepted when iterating on the feature.
krajo Krajcsovits 00:33:32 Yep.
David Ashpole (dashpole) 00:33:36 So…
krajo Krajcsovits 00:33:38 Like, the problem is that if you have a classic histogram, you know, you have… 20 lines.
And… The created timestamp is after the historium on the 21st line.
Because… because the way the… Parsaw works, you need to know on the first line, like, what?
What the created timestamp is going to be.
And… Yeah, so this… I feel like it's very hard… this would be very hard to actually… Fixing and efficiently.
in implementers.
David Ashpole (dashpole) 00:34:21 Is the idea, because ideally, you are… Each line, you get the full series, and then you… Send it onwards?
Is that… Or no, no.
krajo Krajcsovits 00:34:34 So, currently the… Sorry, yep?
David Ashpole (dashpole) 00:34:38 When you're parsing the created timestamp, don't you just, like, literally read the line, and then see the created suffix?
And then just call the… like, append… Zero…
krajo Krajcsovits 00:34:49 Nope. Function.
David Ashpole (dashpole) 00:34:50 No, nope, why not?
krajo Krajcsovits 00:34:51 at all. That's not how the script works.
David Ashpole (dashpole) 00:34:54 I know.
Or…
krajo Krajcsovits 00:34:58 I mean, first of all, the created line is after the sample, so it would be kind of weird to always put in out-of-order things, and that would slow everything down.
David Ashpole (dashpole) 00:35:10 What do you mean by out of order?
krajo Krajcsovits 00:35:12 Well, if you first, ingest, sample, and… Then add… append the zero.
Then it's out of order, because it comes before.
David Ashpole (dashpole) 00:35:27 But that's… I mean, but the start timestamp will always come before all of the points anyways, right?
krajo Krajcsovits 00:35:34 Yeah, but, like…
David Ashpole (dashpole) 00:35:35 Like, your start timestamp is probably 6 hours ago, right?
krajo Krajcsovits 00:35:41 Yeah, that's true. Like, most of… yeah. But, like, at least currently.
For the first sample, after the created timestamp, we don't… Put the created timestamp as out of order.
David Ashpole (dashpole) 00:35:54 I see. You get one.
One efficient scrape.
krajo Krajcsovits 00:35:58 And then you're out of luck.
David Ashpole (dashpole) 00:36:00 Kidding. Yeah.
krajo Krajcsovits 00:36:02 I mean, yeah, I don't know how much it would matter, you're right.
Hmm.
That's actually something that we could try out.
Although, another… Weirdness is that because it's separate lines.
the spec says in OpenMetrics that You can have something… That's called underscore created, which is not a created timestamp, but, like, a series that's called something underscore created.
And to distinguish the two bits.
Between the two cases where it is a created timestamp, and between the case where it is just a series.
You kind of have to keep track of what came before it, and that's… that's where the problems start.
Oh.
David Ashpole (dashpole) 00:36:53 you, in theory, just need to know the last comment, right? Or, like, the… basically the base metric name?
krajo Krajcsovits 00:37:01 Yeah, but… Not just a mat… well, metric, man.
Oh, yeah.
I guess so.
David Ashpole (dashpole) 00:37:16 But I guess it feels like you kind of want to know that for other series as well? Like, if I get a bucket.
and I'm trying to parse it to NHCB or something. I also… Need to know that it's not a gauge called underscore bucket, right?
krajo Krajcsovits 00:37:32 Yeah, exactly, and that's…
David Ashpole (dashpole) 00:37:33 So that's different from other…
krajo Krajcsovits 00:37:35 That's the exact same problem, that's the exact same problem, yes. And HCB parsing is the exact same problem, yes.
David Ashpole (dashpole) 00:37:41 Okay.
krajo Krajcsovits 00:37:42 But I… I guess you have what you said about… Just injecting the zero… I mean… We are trying to get away from injecting zero and actually storing the start time.
David Ashpole (dashpole) 00:37:59 Yep.
krajo Krajcsovits 00:38:00 So, that would be completely against the… Direction that the appender is taking.
David Ashpole (dashpole) 00:38:08 Well, I guess, from my point of view, it's… like, today, we're… Calling all of them in, like, seemingly random order, like, here's a bucket, and here's a sum, and here's a count, and… And here's your start timestamp, right?
krajo Krajcsovits 00:38:23 Yep.
David Ashpole (dashpole) 00:38:24 And, like, in the NHCB case, it's more like… We construct the full thing.
Which hopefully will include, like, we'll get the created timestamp at some point as part of it.
And then, once we have all of them, we ship it, right? Or is that not… I see a head shake again. No.
krajo Krajcsovits 00:38:44 I mean, yeah, I guess maybe it could work differently, but currently, the way it works is that When the parser goes through the lines, the… Scrip… So it returns the first… Wait, let me, let me think. So… When it sees the first line for a histogram, it will look ahead, parse the next bunch of lines to get the created timestamp.
David Ashpole (dashpole) 00:39:16 And then…
krajo Krajcsovits 00:39:18 it will… process again, line by line, and build up NHCB, or just return the… the… the separate… Series, one by one, with the same created timestamp.
David Ashpole (dashpole) 00:39:33 So we… we look ahead for the created timestamp.
krajo Krajcsovits 00:39:36 Yes.
Yeah, that's why it's slow.
David Ashpole (dashpole) 00:39:38 And we backtrack and go find all the points associated with it.
krajo Krajcsovits 00:39:44 Yeah.
David Ashpole (dashpole) 00:39:44 Is that neces… so, is that necessary because we're doing the append zero, or is that necessary to construct the NHCB properly?
Like, if we were… if we just went in order.
I feel like we could still construct the NHCB.
krajo Krajcsovits 00:40:03 Yeah, yeah, that's true, yeah. NSCB does… I mean, NSCB works with that, with the timestamp for, yeah.
I guess if you… if you use the old appenda interface and don't care that the Zero sample is out of order.
I mean, on the first… Oh, wait, So, currently, if we have an out-of-order error on the Created on the zero sample, we ignore it.
David Ashpole (dashpole) 00:40:46 Because we assumed that the first one succeeded. So basically, you'll never get it. I see, I see. So it's… it's not that… I see. It's not that, like, we were previously handling the out-of-order.
timestamps. It's that, like, we would just try every time. We're like, yep. Yeah, yeah.
krajo Krajcsovits 00:41:04 So, I guess in that sense, it wouldn't matter if we tried on the… I mean, the problem is that out-of-order is… slower from… from a query perspective for that area, so it would be… I don't know how much overhead it would be.
To always have that.
David Ashpole (dashpole) 00:41:27 Okay.
krajo Krajcsovits 00:41:28 I guess it's something that you could try out, basically, but it's hard to… .
David Ashpole (dashpole) 00:41:35 But…
krajo Krajcsovits 00:41:36 It's hard to actually simulate…
David Ashpole (dashpole) 00:41:39 are they considered… or no, the start timestamp is reported by the client, right? So it… Yeah, it's always going to be, like.
30 seconds ahead of the first scrape, right?
krajo Krajcsovits 00:41:51 Yeah, sometime before the first script, yes.
Oh, you mean to just…
David Ashpole (dashpole) 00:42:00 If there was a way for us to know that it was the first scrape.
Then we could do the look-ahead then, or something like that.
If it's a series, we… But… Maybe that's…
krajo Krajcsovits 00:42:20 I don't know. Maybe.
I kind of resigned myself to the fact that this is just too slow, but maybe somebody needs to give this another go.
You know… I mean, but it doesn't… Change the fact that if we do change to the new interface, you need the start time.
with the sample.
Meaning that… You do have to look ahead.
Because in the… in the new chunk format for… for start time.
We write the start time before the sample, like, in the same chunk.
David Ashpole (dashpole) 00:43:10 But they're not… but they're all appended together, though, right? Like…
krajo Krajcsovits 00:43:15 Yeah, but…
David Ashpole (dashpole) 00:43:17 The thing that we shove into our append function has… like, if you think about the text format getting smushed and then, like, shoved into an append function, right? It's like, it's one block of stuff.
Sum, and count, and buckets, and…
krajo Krajcsovits 00:43:36 Yup.
David Ashpole (dashpole) 00:43:36 created series, right? So, if we parse them in order, like, presumably we can't just parse the sum and then send it, right? Like, we're parsing and we're holding stuff, we're parsing and we're holding stuff.
And then we parse the created line at some point during that. I guess it's last, is what you're saying?
Then, like, we just wait until after we've parsed all the lines, and created will be included in that.
And then we send it, right? We can do them all in order if we're doing NHCBs, right?
krajo Krajcsovits 00:44:13 Yeah, there is buffering, obviously, because the… we are not… So… So when we are… appending to… storage, basically, from script.
It's not being added.
To the series right away, it goes into the wall.
And the wall… is in sequence, and when we read that sequence back, that's what we write into CSDB.
So… Either you would have to make sure to I mean, on readout, you don't want to reorder the wall.
Because that's just crazy, I think.
So how do you… I don't know how you would do it.
David Ashpole (dashpole) 00:45:02 all I'm trying to say is that, like, I think… Buffering all of the series.
for an NHCB?
is, like, sort of already doing the look-ahead for us. It's just that instead of Looking ahead, finding the… Created series, and then going back and doing each individual series.
We're instead just, like, Doing the whole thing and buffering it.
And then, like, if we buffered, let's say that we weren't using NHCBs. If we buffered.
And then… sent the things in the order we wanted them, like, created timestamp first, and then the.
Right? Like, we could achieve that same behavior, it's just now you're paying the cost of buffering for… Yes. Yeah, yeah, yeah. That's my only point, is like, once we're buffering, then you're already… In theory, you have access to all the data at once, and you can decide exactly how you want to.
krajo Krajcsovits 00:45:59 Yes, that would mean that we can… reimplement an HCB.
on top of that logic. If we had generic puffering.
we would reimplement the state logic. The only problem you have is that or buffering.
You want to always know when you are switching to a new series.
When do you empty the buffer, right?
David Ashpole (dashpole) 00:46:32 I guess, like, it feels like combining the bucket series with the sum and count series is basically the same problem as combining the created series with it.
In my, like…
krajo Krajcsovits 00:46:42 Yeah, but not everybody wants that, like, not everybody changed to an HCB, so not everybody is doing that.
David Ashpole (dashpole) 00:46:48 Yeah, yeah, I'm… right.
So, all I'm trying to say is, like.
if we are buffering, then this isn't an issue, right? So if we are using an HTVs, this isn't a.
krajo Krajcsovits 00:46:59 Yes. Well, it is useful for summaries and state sets, but yeah, gone, yeah.
David Ashpole (dashpole) 00:47:04 Yup.
Yeah, which… Anyways, I… like, maybe the long-term solution is that… but if you're using a different scrape format, then it doesn't matter anyways. This is just for open metrics, where everything is… Yeah, it's like, we've talked about doing native summaries, or NH summary.
Or, I don't know how we want to call it.
krajo Krajcsovits 00:47:32 It's not too van about that, it's about the exposition format, like, it's not… It's more about… Is it one line, you know?
David Ashpole (dashpole) 00:47:40 If the appender interface has a structured summary.
krajo Krajcsovits 00:47:45 Yep.
David Ashpole (dashpole) 00:47:46 And that's what ends up being shipped to the appender.
Then there's no, like… but then you're paying the… yeah. Sorry, go ahead.
krajo Krajcsovits 00:47:56 No, we are not talking about the appender side now, we are talking about the exposition and the parsing.
what I'm trying to get at is that Sure, you can buffer, and it seems to be the same efficiency with some additional memory, but it's not, because if you want to buffer.
Eventually, you want to empty that buffer.
And, like, Eve, like, I guess you could… No.
So you need to be able to tell When you can start releasing from the buffer, or just load the whole buffer.
Which would double your memory, basically.
So you probably don't want to double your memory, but then… To know when to really start from the buffer, you need to recognize that A summary or a histogram is over, right?
And that's the problem, because… In OpenMetrix 1, there's no requirements for the labels to be in the same order.
And there's these weird, you know, suffixes, so what you end up having to do is what the NHCB parsing does, is to Calculate the hash.
Of the labels to compare.
David Ashpole (dashpole) 00:49:18 Let me see.
krajo Krajcsovits 00:49:18 Without the magic suffix, because count and sum and bucket are, you know, doesn't matter, so you have to take off the magic suffix and calculate a hash of the labels.
without the LE label for the bucket, also, so that's even more complicated, and that's the bit that takes long. I don't think… it's not really the buffering.
David Ashpole (dashpole) 00:49:40 Okay.
Yeah.
I don't know if we're agreeing or disagreeing, but I… my… my, like, 10,000-foot assumption is that if we can do it for NHCBs, we could do something similar for Created.
But… But that only makes sense if the appender interface is, like, a complex type. It doesn't make sense if we need to append them.
In separate lines.
krajo Krajcsovits 00:50:08 Yeah, pretty much, because what you save on… like, the reason why NHCB works reasonably well, even from text.
is that, sure, it costs a lot to do an HCB conversion, but then you don't… you are not writing 5 series, or 10 series, just one, and that's much… cheaper.
David Ashpole (dashpole) 00:50:30 Yep.
krajo Krajcsovits 00:50:31 So I agree on that, yeah.
Yeah, and for your first point.
As soon as we have that.
new chunk formats, and we are moving away from the zero sample injection, it gets even more… Important to have the graded, or the start time.
But I think, yeah, it's a bit… Hopefully, we are not taking this as final, what we are saying today, because we are just…
David Ashpole (dashpole) 00:51:16 Spitballing. Spinstorming, yeah, yeah, so I think…
krajo Krajcsovits 00:51:20 I remember that Bartek had some… For the one that tried to, You know, improve the… the parsing? I don't know what happened to that one, probably their time ran out, and it's not a trivial problem.
I'd be shocked if they solved that.
Performance issue, for the reason that we just discussed.
David Ashpole (dashpole) 00:52:02 Okay, I asked the author to Try running with and without the upstream parser enabled, so that hopefully we can know, like.
At least how much worse it is.
krajo Krajcsovits 00:52:13 Nope.
David Ashpole (dashpole) 00:52:15 I don't know, what do we need to… I'm gonna put this as waiting on author.
Update map structure dependencies.
Cape.
Oh, this is old.
November.
Anyone want to pick this up? It's probably pretty simple.
krajo Krajcsovits 00:52:46 Is that PR already, or just not…
David Ashpole (dashpole) 00:52:48 Let's see…
krajo Krajcsovits 00:52:53 I see a lot of people just trying AI on everything now, so there might be already a PR.
David Ashpole (dashpole) 00:53:20 Focus.
krajo Krajcsovits 00:53:36 Isn't the path is just receiver slash premises receiver?
David Ashpole (dashpole) 00:53:44 The other slash, maybe? Seems like it wants to be skated.
So terrible.
Alright.
Okay.
This is probably fixed, honestly.
So it's an indirect dependency.
We depend on 1.5 and… 2.5.
Okay, so… Anyone interested in taking this, or should we just…
Arve Knudsen 00:55:23 I can try to take hands, I can…
David Ashpole (dashpole) 00:55:27 It should be pretty simple, it's just like…
Arve Knudsen 00:55:29 If you…
David Ashpole (dashpole) 00:55:29 into…
Arve Knudsen 00:55:30 Yeah, would you mind sending me the link? Unless it's… or is it in the meeting notes?
David Ashpole (dashpole) 00:55:38 I can put it in the meeting notes.
Arve Knudsen 00:55:39 Yeah.
I can try.
David Ashpole (dashpole) 00:55:42 R-A-O-A-K, N.
Arve Knudsen 00:55:46 What does me.
David Ashpole (dashpole) 00:55:50 I can't sign up yet. Are you not a member yet?
Arve Knudsen 00:55:54 Of the auto org, no?
David Ashpole (dashpole) 00:55:56 Yeah. Okay.
Arve Knudsen 00:55:57 I also… I mean, I had… I was going to ask to become one. I mean, I have submitted some PRs and such.
I have some contributions.
David Ashpole (dashpole) 00:56:08 if you have, like, almost anything, you can just open something and put… I think Arthur and I are both Approvers.
So, it should be pretty simple.
That way I can assign you to things.
Arve Knudsen 00:56:21 Yeah, yeah, I, I guess I could ask Kirio when I'm back, next week, because I talked with him before about the process for becoming a member.
krajo Krajcsovits 00:56:31 Yeah, yeah, you just open a PR in the, I think, automatic committee or something. Right. Repo, I… I think I sent you the links, but I can.
Arve Knudsen 00:56:40 Oh, yes.
Yeah, I understand. So, yeah, I probably have the links in, in our conversation history.
krajo Krajcsovits 00:56:49 Yep.
Arve Knudsen 00:56:49 I have already my… Another reminder to check it, I just didn't have the time last week.
krajo Krajcsovits 00:56:55 Okay.
Back to care about the point is not done.
David Ashpole (dashpole) 00:57:10 Can you update your Go.mod?
You will see some type check errors.
krajo Krajcsovits 00:57:15 I can take this one. Why not?
David Ashpole (dashpole) 00:57:18 I mean… There's nothing wrong with the receiver. I don't agree that it's a bug.
But if you want it, you can…
krajo Krajcsovits 00:57:31 Yeah.
David Ashpole (dashpole) 00:57:32 Like, someone's got a downstream project, and they're, like… But, yeah.
I won't.
The market is stale, then.
krajo Krajcsovits 00:57:41 Nope.
David Ashpole (dashpole) 00:57:45 They'll test. No.
Okay, I'm just… I might just say some of these are blocked on… the timing?
krajo Krajcsovits 00:57:56 Yeah, for… I mean, pretty sure. That was, conclusion, and… there's… that's kind of why I'm saying that the… reducing the timeouts is just a workaround, because Maybe… .
David Ashpole (dashpole) 00:58:13 What's the new package called? The Go One? Sync? I thought it was SyncTest.
Arve Knudsen 00:58:18 Signitas, yeah.
David Ashpole (dashpole) 00:58:23 Why did nothing come up?
Arve Knudsen 00:58:24 Are we talking about affiliate, play King Tests again.
krajo Krajcsovits 00:58:28 Yep.
Arve Knudsen 00:58:29 It's true.
I have Claude on the case right now. It's actually taking more than 16 minutes already, trying to come up with a solution. It thinks… think, test is not… it's not a fit for this, this type, these tests.
Like, it thinks they should remain integration tests, and if they were rewritten to use sync tests, they would no longer be integration tests.
So it kind of came up with a plan to, make the tests faster and more deterministic, so I'm kind of, like, waiting to see what it ends up, producing.
krajo Krajcsovits 00:59:11 Do you think it's… I mean… As we discussed, they shouldn't be integration tests, after all, because they…
Arve Knudsen 00:59:22 Okay, huh?
David Ashpole (dashpole) 00:59:23 Because, like, there's a text input and an OTLP output, and that's what we want, but because of the way everything's structured, there's an HTTP request in the middle. Like, so we either need to, like… maybe we could put in a fake scraper.
I don't know.
Arve Knudsen 00:59:38 Okay, maybe I missed…
David Ashpole (dashpole) 00:59:39 It's great for me.
Arve Knudsen 00:59:40 I mean, yeah, maybe I didn't quite understand this then, so…
David Ashpole (dashpole) 00:59:44 So the, the, the, so the, okay, so the, the…
Arve Knudsen 00:59:47 the test… the test function you linked me to, which calls test component.
It should actually really, not be an integration test.
krajo Krajcsovits 00:59:57 Yep.
David Ashpole (dashpole) 00:59:58 I mean, the problem is we have, like, 700 of them, right? Yeah. And that's why the… you're like, let's test… our component.
And the odds that one of the 700, like, times out, or whatever is…
Arve Knudsen 01:00:12 So, you're saying we would be fine to kind of fake the scraper, David?
David Ashpole (dashpole) 01:00:17 I mean, I…
Arve Knudsen 01:00:18 Yeah.
David Ashpole (dashpole) 01:00:18 That's an idea I just came up with on the.
Arve Knudsen 01:00:20 Because I, I think that's one thing… Claude thought we could not do, because he thought it should be an integration test, you know? So maybe it… maybe both… I mean, maybe I and the bot didn't understand the intention here, that we actually… we don't want for it to be an integration test, after all.
krajo Krajcsovits 01:00:38 Yeah. I mean, ideally.
there is some script, because script has a certain order, it calls the collector component, but it shouldn't reach out on HTTP as an integration test to read the input.
It should just… use some… you know, a byte slice or a file as input. It shouldn't reach out on the network, because that makes the sync test not work, basically.
Arve Knudsen 01:01:07 So, Kryo, you think, like, a radical rewrite, the sync test, you know, conceptually might be correct here?
krajo Krajcsovits 01:01:15 I don't know how much radical… sorry, go ahead.
Arve Knudsen 01:01:19 Norma, go ahead.
krajo Krajcsovits 01:01:21 So, I don't know how much… how radical it needs to be, like… Also, we are all maintainers in Prometus, so if we need an interface to make this simpler, make writing this test simpler, we can do that.
Arve Knudsen 01:01:38 Yes, I saw that could be, a necessity for our rewrite, to kind of upstream, some sort of change.
M…
krajo Krajcsovits 01:01:50 Yeah.
Arve Knudsen 01:01:50 Also, I guess, like, if you're okay to kind of change the nature of the test, so it's no longer integration test, then I can… I can just propose, like, a radical change, which is based on SyncTest, and then I can kind of ask you just for, you know, quick feedback on whether this may make sense directionally.
krajo Krajcsovits 01:02:11 Yeah, yeah. As David said.
Arve Knudsen 01:02:13 my thinking?
krajo Krajcsovits 01:02:14 Yeah, as David says, we don't need all of these to be integration tests, because we are not interested in the networking and the… things. We are interested in the logic vendor… script code calls the open telemetry storage, basically.
Arve Knudsen 01:02:40 load is taking insanely long, with this, rewrite without sync tests, so I'm… I'm wondering, you know, if rewriting to sync tests would actually be faster.
Maybe it's, like, maybe keeping the integration matrix is a difficult problem to solve.
David Ashpole (dashpole) 01:03:05 Okay, we're over time.
krajo Krajcsovits 01:03:06 Yep.
David Ashpole (dashpole) 01:03:08 I think we had some, maybe, useful discussions.
Thanks for joining.
I'll see you guys next week.
krajo Krajcsovits 01:03:15 Or two weeks from now, no?
David Ashpole (dashpole) 01:03:18 Two weeks, yep, yep.
Arve Knudsen 01:03:18 Alright, cheers, bye-bye. Bye-bye.

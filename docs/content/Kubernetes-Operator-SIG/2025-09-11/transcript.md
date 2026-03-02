SIG: Kubernetes Operator SIG
Date: 2025-09-11
Duration: 37 minutes
============================================================

## Zoom Recording Transcript

**PL Pavol Loffay** 00:32 Hi guys, I'm Ecloi. Hey, Jacob.
**Jacob Aronoff** 00:34 Hello.
**Mikołaj Świątek** 00:37 I just… I… I am… why? Why doesn't my camera want to… okay. I am… I'm reading… I'm reading the… the thing you posted in Leeds right now, Jacob, and this is, like…
If only, if only we could only run Kubernetes 130, 134.
**Jacob Aronoff** 00:54 I know, life would be a lot easier. Oh, where did Pavel go?
**Mikołaj Świątek** 01:01 I said Kubernetes 134, and he is, he got a.
**Jacob Aronoff** 01:04 He said, I'm out.
**Mikołaj Świątek** 01:06 This is not a conversation I want to participate.
Alright, let's see, do we need… do we actually have anything, anything interesting to talk about?
**Jacob Aronoff** 01:20 I think we should probably talk about some of the releases that are happening.
**Mikołaj Świątek** 01:26 What's going on with 144, right? Why are the internal tests failing?
**Jacob Aronoff** 01:32 Yeah, I wanted to get some more clarity on that. I wasn't really sure. I was trying to read the,
I was trying to read some of the errors that Benny was running into.
Oh, I don't know if we… did we merge the…
One second… Nerves now.
**PL Pavol Loffay** 01:52 Yeah, I think the PR is still there.
**Jacob Aronoff** 01:54 Yeah, I was checking that, Tyler merged the operator version… Oh, what?
**Mikołaj Świątek** 02:03 I'm unfortunately, unfortunately kind of busy right now with some urgent stuff.
**Jacob Aronoff** 02:09 Yeah, I'm also 25, yeah.
**Mikołaj Świątek** 02:12 So, I don't have that much time to do anything other than code review.
But I can take a look, maybe tomorrow morning.
See if it's… if it's still trouble.
**PL Pavol Loffay** 02:27 Yeah, I think Bennett will be the way for… two weeks.
**Jacob Aronoff** 02:32 Yeah, you don't…
**PL Pavol Loffay** 02:33 We'll be able to finish.
**Jacob Aronoff** 02:36 Yeah.
**Mikołaj Świątek** 02:38 Okay, so in that case, Jacob, can you… can you take it? Because it's, like, technically your turn, I think.
**Jacob Aronoff** 02:42 Yeah, no, I can take it.
**Mikołaj Świątek** 02:46 I could help you out.
**Jacob Aronoff** 02:47 Paul, do you know any of the problems that he was running into?
**PL Pavol Loffay** 02:52 No, I… didn't investigate. I can look now what's… what's there, but it's like so many tests are failing.
**Jacob Aronoff** 03:00 Yeah.
To take this over, given,
Maybe I'll just, start it from scratch.
And see if there's, like, a thing with… Some bad version change.
**Mikołaj Świątek** 03:18 This almost… this almost looks like there's some…
**PL Pavol Loffay** 03:22 Some weirdness.
**Mikołaj Świątek** 03:24 I don't know, the container, the image is messed up somehow? Something like that?
**Jacob Aronoff** 03:31 Yeah, let me just… I'm gonna try to do it right now, and see where we can get. Sure.
**PL Pavol Loffay** 03:39 Can I merge some PRs? Probably, like, the update to Python?
**Jacob Aronoff** 03:43 Yeah, yeah, go for it.
**Mikołaj Świątek** 03:46 And again, I don't know how… what causes this, but we have another flaky test in the target allocator, and I know what causes that flaky test, even, but I have no idea why it, like, sometimes comes up, and it comes up for… comes up… comes… comes up for… comes up for a while.
in basically every run, and then suddenly it stops. Like, is it… is that some, like, internal GitHub Actions, scheduling thing?
**Jacob Aronoff** 04:17 That I don't know.
**Mikołaj Świątek** 04:19 Well, I know how to fix that test. That test is the problem. It's an old, funny problem related to the fact that if you use a fake Kubernetes client when testing informers, then that fake Kubernetes client doesn't support resource versions, and you can get… if you're unlucky, you can get a race conditional.
**Jacob Aronoff** 04:39 Oh, why didn't I merge this?
I have, like, a PR that I thought I had opened up and merged, but I guess I didn't?
**Mikołaj Świątek** 04:50 I will say that I have one item in the agenda for today.
I added it yesterday during the collector's sake, because I went to the collector's egg.
meeting, and I was asked point-blank, hey, what does the operator think about this?
So, what's going on is that there's an RFC,
describing how to do configuration merging, and I think the current state of it is to use YAML tags.
Alright.
**Jacob Aronoff** 05:30 Oh, I did merge this. Sorry.
Yeah, I did see that, I don't like YAML tags. Maybe it's personal preference, but I don't like YAML tags at all.
**Mikołaj Świątek** 05:44 I don't really have preference about this… preferences about this at all.
I…
**Jacob Aronoff** 05:49 I mean… I'm kind of frustrated about this, because I, like, a year or two ago, was like.
Remember when they started doing the multiple config files?
We basically were like, we shouldn't do this, because that's what other environments are for, and like, we shouldn't bake in this logic, because it's just gonna get super complicated, essentially.
And this is just another scope creep to me.
**Mikołaj Świątek** 06:19 I mean, I, for the record, think this is a perfectly fine thing to have in the collector for environments where it is useful, because not everyone's running in Kubernetes, and not everyone's just orchestrating and building their whole YAML config using some external tool.
**Jacob Aronoff** 06:39 So, yes and no, like, I agree that not everybody's running in Kubernetes, but there are other tools that do config merging. Like, that's what, like, there are full languages that are built out for this, is, I guess, my point. Like, and ultimately what this… what it feels like is going to happen is that we're gonna build our own YAML merging language, and…
like, I don't want us to have to support YAML merging.
In addition to hell merging, and in addition to Kubernetes merging.
**Mikołaj Świątek** 07:06 When you say us, do you mean the hotel… open telemetry in total, or do you mean the operator specifically?
**Jacob Aronoff** 07:13 Operator specifically. Like, I don't want to… Yeah, so…
I, I think it's fi- like…
But that's really annoying, because someone's going to come to us and be like, why don't you support this, you know, specific, emerging strategy, or whatever?
**Mikołaj Świątek** 07:29 I think our answer is very simple. Our answer for the collector CRD
Is that we rely on being able to know what your configuration is, or final configuration.
And if you're going to do, say, things like, here is my file that I mount from some config map, and I want to use that.
Then we have no idea, and we can't do most of the things that the operator is useful for.
**Jacob Aronoff** 07:55 So, no.
**PL Pavol Loffay** 07:57 But at the same time, in the past, we had many requests to split out the config of the collector, so that multiple teams can, you know, supply their additions and distribute the config, essentially. And maybe this opportunity how we can
Look at that use case and think.
Or we could support it in the… the operator.
**Mikołaj Świątek** 08:24 I think that use case requires… the answer to that use case is,
having more high-level constructs, and having, like, more flexibility, the answer is not to let someone just mount a config map with the.
**PL Pavol Loffay** 08:43 No, I think… I think mounting the config map is sort of… explicitly…
Disabled in the operator, and we kind of make it clear that the config should go into the config field.
Which…
Again, like, makes it explicit that there is only a single configuration for the collector, so we are safe on that front, but…
But we should be thinking about…
How we could then solve the use case of…
supplying multiple configs to the collector, but you're right, it's probably a different approach than just using a bunch of config maps mounted on the collector CR.
**Mikołaj Świątek** 09:29 If somebody came to… if somebody came up and said.
Hey, my idea is that I want to have a collector config CRD, and I want to potentially link multiple of these into my auto collector to assemble the config that way. That would be something I would consider.
Because…
**PL Pavol Loffay** 09:55 that is something explicit that still lives in CRDs.
**Mikołaj Świątek** 10:00 Even if the actual merging Behavior might be.
**PL Pavol Loffay** 10:07 But is the merging behavior implemented by…
the collector, or is it, like, standard Go YAML package?
**Mikołaj Świątek** 10:18 It is… It is not the standard YAML package, it's core on F.
And this RFC is actually… actually wants to do something more elaborate with it.
**PL Pavol Loffay** 10:36 I think there… It's gonna be like…
**Mikołaj Świątek** 10:38 Open thermality Collector specific.
**PL Pavol Loffay** 10:40 implement.
**Mikołaj Świątek** 10:41 Something like that. I think the… most of the basic idea of this RFC is something like…
Like, for example, we… the problem… the problem generally with merging maps is that you don't know how to merge lists.
**PL Pavol Loffay** 10:59 Good.
**Mikołaj Świątek** 11:00 That's, like, 90% of the problem of this, I think, is to specify how do we merge lists. And part of… a large part of this RFC is basically saying.
In the auto collector, we know that for certain lists, the order doesn't matter.
So let's just, you know, merge those by appending and removing duplicates, is something like that.
Which is not unreasonable and covers a lot of use cases, because, like, the main use case for these kinds of things, and I know this also from internally from Elastic, is something like…
You want to make…
Like, you want to supply some kind of base configuration that defines something like, you know, two or three extensions that do something specific that you always want to be able to rely on, and then let the user write everything else themselves.
It's that kind of thing. The use case is not actually to do anything exceptionally complicated.
with the merging. It's about adding things which happen to appear in lists.
In a way that's, like, largely independent.
But, like, the main question that we need to answer about this RFC, and I promise that we would give our opinion, is that
Does this upset us?
And Jacob, I think it upsets you slightly, so you can… you can go there and say… I mean.
questions, like, does it upset us personally? And the other question is, is it a problem for the operator project? I don't think it's a problem for the operator project, mostly, because I think we're just going to say no. But if you disagree, you know, you have an opportunity to voice that here.
**Jacob Aronoff** 12:56 Yeah, I… I mean, I definitely have a problem with this, but I also don't, like…
I don't like the idea that I get to hold it up, so I don't think I should hold it up. Like, if this is what people want, this is what people want. There was enough time for me to have commented on an RFC to make it heard that this is, like, not a thing that we should do, but…
I, you know…
decisions have been made, and that's fine. I think for us, I don't want to support this,
behavior, because I think that it's going to really, really confuse a lot of what we have.
And so I think…
**Mikołaj Świątek** 13:33 There's no way to support it right now, because our config is an app. It's not a text, so there's no place to put the tags.
**Jacob Aronoff** 13:44 Yeah, it would just be a mess to try and support this.
**Mikołaj Świątek** 13:50 Yeah, so it's like, if you want to answer for speaking for us, then I'm personally fine with the answer. We don't object to it, but we are not going to support it in the operator.
**Jacob Aronoff** 14:03 Yeah.
I think that's fine.
**Mikołaj Świątek** 14:06 Alright, cool.
Okay, cool. Do we need to talk about anything else?
**Jacob Aronoff** 14:18 I'm doing the release right now, if we want to stay on until that's…
**Mikołaj Świątek** 14:22 Let's say, no concern.
You should start up the tests locally and see what happens. If so many of them are failing, then…
you should… it should be obvious. Last time, we had something failing that had to do specifically with the .slept image.
And not the one that we had at default, the newly released one, so figuring out locally what was going on was a little bit difficult, but here…
Should do not simplify.
**Jacob Aronoff** 14:58 Yeah, let's… we'll see. I'm going through the steps right now, just before I do that.
Okay. Should I just swap Benny? Because he moved me to 135?
And him to 134?
What should this be?
**Mikołaj Świątek** 15:22 I think… I think Bene already did one Freddy too, so… so you should just, like, put him at the bottom for the one.
**Jacob Aronoff** 15:29 Yeah, well, that's what I was thinking, so that… but then I move everybody up one, essentially.
**Mikołaj Świątek** 15:34 No.
**Jacob Aronoff** 15:35 No, no, no, let me show you. Hold on.
I don't know about that.
So this is what it was before. There's been A134, me 135.
Because he had swapped me and him, like, what he did, I was like, don't you just, you know, move yourself to the bottom. He's like, no, no, I'll do both. And I'm like, you don't have to do that.
So now, now we're in this weird one.
I mean, I think you should go to the bottom, because he's done enough at this point.
**Mikołaj Świątek** 16:10 Yes.
**Jacob Aronoff** 16:11 I mean, I guess I could do the next one as well, if… just to make life easier.
I don't really care.
**Mikołaj Świątek** 16:20 Alright.
**Jacob Aronoff** 16:22 Okay.
So, that's that, that's that.
Let's go through… okay, make changelog update.
Okay…
I don't think they had any breaking changes in here.
But let me check.
No, no breaking changes.
Okay… And that'll be after. Cool.
Even when it does this.
They're, like, search… they're, like, fuzzy search is not good. 4329.
Okay, let's see if everything just crashes here.
And then I'm also seeing a problem in the Helm chart for the release here.
Oh, this exists, so what was the problem?
Oh, interesting. So it failed the GHCR part of this? That's super annoying.
Let's see what failed this time.
Did the test just slow, or is, like…
I don't know what's going on.
**Mikołaj Świątek** 22:36 Give me a second, I'm gonna…
I'm just going to bump some stuff and run it as slowly and see what happens.
**Jacob Aronoff** 22:47 Okay.
**Mikołaj Świątek** 22:48 We'll just check out your flow of those.
Let's see…
**Jacob Aronoff** 24:28 Yeah, and unit tests are failing already.
**Mikołaj Świątek** 24:32 The failure is really weird.
Soon.
**Jacob Aronoff** 24:41 Yeah, so what is this failure? Fail internal controllers reconcile Test 1457?
Is this one intermittent or persistent?
**Mikołaj Świątek** 25:31 Good question.
I think I already saw it once.
Do the unit tests pass locally?
**Jacob Aronoff** 25:47 That's what I'm testing right now.
What do I want to do, I want to do make test, right, as the command.
**PL Pavol Loffay** 27:03 I have to drop, it was nice seeing you.
**Jacob Aronoff** 27:06 Yeah, you too. Have a good day.
**PL Pavol Loffay** 27:08 You too. Bye.
**Jacob Aronoff** 27:10 Yeah, bye.
Okay, I'm trying to run tests locally right now.
**Mikołaj Świątek** 27:21 Both human tests and internal tests.
What's going on?
What is this?
**Jacob Aronoff** 27:47 Hmm.
Hmm.
**Mikołaj Świątek** 28:31 The answer is that this collector image does not exist.
**Jacob Aronoff** 28:36 Which one? 134?
That's hot.
**Mikołaj Świątek** 28:42 Phew.
**Jacob Aronoff** 28:45 Is it because we're using the, the wrong one?
Like, the wrong repository. Are we using the, Docker one?
**Mikołaj Świątek** 28:54 We're using JHCR.
It doesn't exist.
**Jacob Aronoff** 29:05 Is it Contrip, or is it bass?
**Mikołaj Świątek** 29:08 It's OpenTelemetry Collector, under Open Telemetry Collector Releases. Manifest under.
Let's see what collector releases has to say first.
**Jacob Aronoff** 29:23 Yeah, that's what I'm looking at now.
**Mikołaj Świątek** 29:34 Yeah, it doesn't exist. Should be 1, not 0.
**Jacob Aronoff** 29:41 One second.
I'm seeing the nightly, where's the non-nightly?
**Mikołaj Świątek** 29:49 It doesn't exist, not with… not with.
**Jacob Aronoff** 29:54 How do we look at just the, like, major versions? Like, why does it give me all of these extra shaws?
**Mikołaj Świątek** 30:13 Perfect.
canceled.
**Jacob Aronoff** 30:17 Oh, yeah, it looks like it doesn't… it's… it's… they have 134.1, they don't have 134.
**Mikołaj Świątek** 30:23 Yep.
**Jacob Aronoff** 30:24 I guess they must have retracted it, okay.
I mean, that's an easy fix.
**Mikołaj Świątek** 30:28 That seems easy fix to me.
Where are we gonna… how did some of the tests pass, then?
**Jacob Aronoff** 30:43 That's a great question. Which one's passed?
It looks like all.
**Mikołaj Świątek** 30:47 Some of them… some of them passed, I think, didn't?
**Jacob Aronoff** 30:51 Maybe ones that are just target allocator ones?
**Mikołaj Świątek** 30:55 There isn't really anything like that, I don't think.
**Jacob Aronoff** 30:59 No, we have a target allocator one here. I mean, this is…
This goes to that problem that, you know, we've both mentioned before of, like, our end-to-end tests aren't very good. Like, some of them are useless, and they should just be unit tests.
**Mikołaj Świątek** 31:14 Well, not exactly unit tests, they should be something…
**Jacob Aronoff** 31:19 Or, like, integration tests, but, like, they shouldn't be end-to-end tests. Like, we don't need to run a whole harness to check some of the stuff, you know?
**Mikołaj Świątek** 31:28 We have this fixed distance.
**Jacob Aronoff** 31:31 Well, I'm not getting that same error, the one that, the unit test error that we got, so…
**Mikołaj Świątek** 31:41 Yeah, unit tests succeeded for me a lot.
**Jacob Aronoff** 31:44 Yeah, I got one Prometheus problem, but it seemed like that was.
**Mikołaj Świątek** 31:50 It's flaky.
**Jacob Aronoff** 31:52 Yeah, thank you.
**Mikołaj Świątek** 31:53 It's called, like, namespace Label Update is what it's called, right? Yeah.
That's something I'm aware of, like this.
**Jacob Aronoff** 32:03 you know, Okay, I just pushed the new one.
**Mikołaj Świątek** 32:07 Okay.
Running these tests will go into…
Since we're, like, both yawning you, because it's morning, and because it's, like, it's the afternoon.
**Jacob Aronoff** 32:23 Yeah.
Wait, what time is it for you? Like…
**Mikołaj Świątek** 32:32 It's, like, 6 Freddy, yeah.
**Jacob Aronoff** 32:40 Bing.
**Mikołaj Świątek** 32:47 This… this enable operator network policy test is really slow for some of them.
**Jacob Aronoff** 32:54 Is it because it requires OpenShift?
**Mikołaj Świątek** 32:58 I mean, it runs on… in the… in kind as well, just takes a long time.
Okay, that seems, seems fun.
Do you understand why… why the… why… why Pavel wants to fix security issues in our end-to-end tests?
**Jacob Aronoff** 34:20 Say that again?
**Mikołaj Świątek** 34:22 There's a PR by Pavel, which is, like, disable auto-mounting service account tokens, because it's.
**Jacob Aronoff** 34:30 Oh, yeah, there was, like, a problem that we were having in the Helm Cart release that was related to it, I think.
**Mikołaj Świątek** 34:36 Really?
**Jacob Aronoff** 34:38 Yeah, there's,
At least I think so.
Let me see… there's something in the,
Was it the Helm charts thread?
No…
Bing.
Yeah, I think this might be what that was for.
I might be misremembering, though. I sent it in the chat.
Oh, no, this is unrelated. Unrelated.
I don't know if…
**Mikołaj Świątek** 35:57 God, this network policy test takes a long time.
I don't really know what it's doing.
**Jacob Aronoff** 37:08 I think we're looking okay.
We can probably call it…
Anything else you want to go over?
**Mikołaj Świątek** 37:19 Not a particular one.
**Jacob Aronoff** 37:20 Okay. Eager to… to end my day.
Yeah, well, I hope you have a good night. Thanks for helping out.
**Mikołaj Świątek** 37:28 Much appreciated.
**Jacob Aronoff** 37:30 Have a good rest of your day as well, Jacob. Thank you.
**Mikołaj Świątek** 37:34 See ya.
**Jacob Aronoff** 37:35 Bye.

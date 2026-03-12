SIG: eBPF instrumentation
Date: 2025-08-27
Duration: 45 minutes
============================================================

## Zoom Recording Transcript

**Tyler Yahn** 00:36 Hey, Steven. Hey, Mike.
**Stephen Lang** 00:39 Hey.
**Tyler Yahn** 00:41 How's it going?
**Mike Dame** 00:42 8.
Pretty good. How about you?
**Tyler Yahn** 00:45 Good. Yeah, just getting started with the day.
Hey, Raphael.
**Rafael Roquetto** 01:13 Hey guys, hey.
**Tyler Yahn** 01:15 How's it going?
**Rafael Roquetto** 01:15 Good, good.
**Tyler Yahn** 01:17 Yeah?
**Rafael Roquetto** 01:21 How are you?
**Tyler Yahn** 01:22 Yeah, doing good, as starting the day. … Little… little, not as hot today, so I'm pretty excited about that. It's been, like, the upper 90s over here, so yeah.
**Rafael Roquetto** 01:34 Oh, enjoy… enjoy it while it lasts, because it's only getting chiller now, I guess?
**Tyler Yahn** 01:41 We'll take it. I… I don't mind.
I'm all about that. Although I guess I don't have to deal with, like, the bitter cold up north like you do.
**Rafael Roquetto** 01:52 Yeah, but honestly, I'll take the coat over the, scorching hot weather, so… Yeah. You know… I don't have AC anyways.
**Tyler Yahn** 02:02 Oh, what? Really?
How far north are you?
Hey, Mattia. Hey, Mario.
**MM Mario Macias** 02:14 Hello.
**Tyler Yahn** 02:15 Good to see ya.
**MM Mario Macias** 02:18 Yeah.
**Tyler Yahn** 02:19 How's the… how's the vacation?
**MM Mario Macias** 02:21 Pretty good, pretty good.
As always.
**Tyler Yahn** 02:26 Nice. Yeah.
**Rafael Roquetto** 02:27 Everyone is happy that Mario is back, maybe him not so much, but….
**MM Mario Macias** 02:34 Oh, yeah, I got a very fun comeback, yeah, lots of, lots of activities, and many, many things to catch up. That means that you, you work hard during August.
**Tyler Yahn** 02:51 Yeah, Rafael's been after it.
**Rafael Roquetto** 02:56 I'm glad you're back, Marty.
**Tyler Yahn** 03:00 Cool, so we can probably get started here in just a second. If you haven't yet, go ahead and add your name to the attendees list. If you have, agenda items you want to talk about.
Go ahead and add them as well.
And I'll start sharing my screen here.
Cool. Alright, so first up, Mario, you wanted to talk about removing the third-party licenses, .cs.
**MM Mario Macias** 03:35 Yes, this… this file is not actually any kind of legal requirement. It was just when we moved the Vela code to… to OpenTelemetry.
I just thought it would be fine just keeping the generation of that file, but … I think it's hindering, Havid, some pull requests. For example, those pull requests That are automatically, … that automatically updates some dependencies, might need to get… or might fail because this third-party licenses is… is failing.
that you need to manually fix that. Also, for… for some contributions, for some new contributors that are not aware of this, they often… their pull requests fail. So, as long as it is not something legal requirement.
I… I will vote for removing it.
And maybe if later we need to add something similar, we can use some OpenTelemetry standards, or, I mean, some standard tool from the hotel… the hotel organization.
**Tyler Yahn** 04:48 Yeah, so that's a good point, … I agree, I think this can get removed. This actually doesn't satisfy any sort of, like, legal requirements. I think this is good for just, like, a… Oh, that's cool, I didn't realize it formatted like this. Sorry, it's good for just, like, understanding, like, what's included in here?
**MM Mario Macias** 05:08 ….
**Tyler Yahn** 05:10 I definitely am in favor of that. I do also, like, I thought we also copied in the licenses themselves, but I actually don't see that. I think that was because it was in the vendor directory?
was where it was. I think that actually might be more of a problem than I realized. So, in, like, the, Go Auto, projects.
We do this. So, if you're gonna make a distribution, and you have dependencies on, source code, there are definitely some licenses that actually require, you to redistribute the license as well. Not all licenses, obviously, but, like, some. And so what we do here is we just copy any dependencies license, and we, will… Put… include that in the distribution.
… So… this, I think, is actually, like, Apache 2, I don't think, actually has this requirement, but I do think that, like, this is kind of important, for making a distribution, that, like, we do need to be sure that we are actually including in this. So I… I was looking at this just right before the meeting. I definitely think we should remove this, but I also think we need to add, like, a licenses directory to copy in all of the, … Specific licenses that we actually do depend on.
I can… I can take that as an action item, Mario, unless you wanted to pick that up.
**MM Mario Macias** 06:30 No, I'm fine with you, if you take it, yeah.
**Tyler Yahn** 06:34 Yeah, … Yeah, good call on finding us, though. I think it… It's just annoying having that file, and it's actually not serving the purpose that it needs to, so, yeah.
Okay.
Okay, cool.
Yeah, any other comments on that one?
**MM Mario Macias** 07:31 No.
**Tyler Yahn** 07:33 If not, then I was going to just do a review of OpenPRs, but it looks like, Steven, you've actually got a question that maybe we can touch on before that. You wanted to ask about parallelizing the CI?
**Stephen Lang** 07:48 Sure, yeah, so I noticed that the… CI in general, we have a whole bunch of workflows.
A bunch of them do run in parallel with each other.
But the slowest one, takes over 45 minutes to run, which is the integration tests.
… And the Kubernetes tests take about 30 minutes as well. So I was generally thinking about speeding up, CI, just to kind of improve the contribution process, turnaround times.
When I thought about parallelizing the integration tests, I had a look at the GitHub limits, and it seems that the free account allows you to have about 20 executors at any point in time. That seems to be per org.
So, one thing that I just wanted to ask, and I don't know if anybody's aware, are there any general guidelines for the, sort of.
Level of parallelization, or number of jobs, so that we can be you know, a, not a noisy neighbor in the, in the hotel, organization, because I could, you know, try and max this out, and really speed up the, the CI, by having the maximum number of executors, but maybe I shouldn't do that, maybe I should only go for 5. … I tried to look at the hotel org, I didn't see any… Guidelines or recommendations around… you know, the usage of the number of GitHub executors.
So, I was just gonna try and… you know.
We can get an, … speed up as much as I can whilst, you know, not really maxing out the number of executors.
Just to… you know, as a guess, we probably don't want to use them all, because if we get a lot of PRs, you know, then Maybe we could make other repos.
Have longer, you know, queue times, wait times.
**Tyler Yahn** 09:46 So I don't think that we are limited to 20 per org.
So we must be paying.
Cause, like, I think they go… UpstreamGo one alone, I think, uses I don't know about 20, but it's pretty close to 20, … this is the one that kind of stands out. Like, the collector, I think, has… I mean, there's just… way more than 20 here. And so, like, this one also, it was approached in the same way that you're talking about, trying to, like, split things off to try to make things faster.
So, … I don't see why we wouldn't want to try to do this. Obviously, you're right, like, you know, if we had, like, a few hundred of them, like, that's just not gonna probably work, … just, I think that it's gonna take a long time for it to get through, let alone, like.
Yeah, like, there's diminishing returns eventually, you're just wasting more of your time spinning things up than actually running things. And so, yeah, like, I definitely think it's worth just investigating or just trying, through experiment to split things up a little bit, is what my suggestion there would be. I don't… there isn't, specifically any hotel-related guidelines here.
Yeah, so I, I don't, I don't know of any, it definitely hasn't been told to any maintainers in the past.
I definitely don't think that, … It's something that's been highly considered.
I… I do… I kind of wonder what the… the organization… defaults are. It's a CNCF project, so I would be surprised if they didn't get some sort of, like, comps amount, or if we aren't paying for something as well, so it's above the minimum. But yeah, I would say go for it.
45 minutes is just… out of all of the… out of all the Go repositories that I've worked for, or worked with in, hotel is long, is very long. So, yeah, I think that, like, if we want… if we can split… speed that up by splitting this up a little bit, I definitely think we should try to do that.
So yeah.
**Stephen Lang** 11:44 True.
Well, I'll go for, like, a loose target of around, sort of, 15 minutes, and just, shard things appropriately, so it's probably going to be… Around about 4 shards for maybe several of the jobs.
**Tyler Yahn** 11:58 Yeah, I think that seems reasonable.
I think also, like, once you… once you start sharding, then you can look at individual, like, workflows and see if we can optimize, you know, the… the build, or some processes as well in there, like… I haven't looked too close, but I'm pretty sure that, like, a lot of our building stuff could get cached, just based on, like, Docker images and things like that, and so we could try to… we could try to look at optimizations along those lines as well, which would then pay dividends across the parallelization. So, yeah, I think that makes a lot of sense to me.
**Stephen Lang** 12:28 Sure, okay, great.
Thank you.
**Tyler Yahn** 12:32 Yeah, … Mario or Rafael, I know that, like, coming from the Belo world, like, is this something that you guys considered, looking at?
**MM Mario Macias** 12:43 You, you mean regarding to this… … parallelization?
**Tyler Yahn** 12:50 Yeah. So, yeah.
**MM Mario Macias** 12:51 Yeah, I was thinking… I was looking or working last month on trying to, instead of parallelizing, consolidating the different tests.
Because most of the time, the tests are just spinning up a cluster, running the tests, destroying the Docker Compose cluster, create… recreate it, so I was trying to create a big Docker Compose cluster that will run multiple test suites.
But it was not as straightforward as I would have expected initially.
So, it… the task remained unfinished.
Yeah.
No, I run out of ideas rather than just, okay, let's try to travel, like….
**Tyler Yahn** 13:42 Yeah, I think that makes a lot of sense. I've looked at that in the past as well for, like, a Kubernetes cluster, a lot of the time is spent just creating it.
**MM Mario Macias** 13:49 Yeah, so if you can, like, reuse it, it's kind of, like, the best thing, but….
**Tyler Yahn** 13:54 then you have, like, issues of side effects of, like, what test ran before, like, are you causing other issues because of this? Like, how do you isolate things, appropriately? So, like, yeah, I think there's a lot of… ….
**MM Mario Macias** 14:05 Yeah, some tests are part of consolidated, we will need to rewrite some of them to… Do not make assumptions.
**Tyler Yahn** 14:13 Right, right, exactly.
So yeah, I think… I think just starting out by… I mean, we could always pull things back together, that's not a hard thing to do.
**MM Mario Macias** 14:22 Yeah.
**Tyler Yahn** 14:23 Splitting it up, I think, is the harder thing. So, yeah, I think if we just go there, and then, … like, yeah, in, like, a Phase 2, if we wanted to get it down, like… Even 15 minutes is really long to me, but, 45 is much longer, so, yeah.
**MM Mario Macias** 14:36 yeah.
**Tyler Yahn** 14:37 Yeah, yeah.
Well, cool. Yeah, Steven, that sounds good. I'm excited to see the work on that one. Thanks for helping on that.
Okay, … Oh, wow, there's 11. Okay, so next up, just wanted to go through the open PRs and see if we can, move things along.
So, first up, Mattia, you have this PR for, … Kafka adding 2.8 and 4.8… or 4.0 integration tests to increase API version coverage. I know this was something I had taken a brief look at. It looks like Rafael has reviewed it.
It looks like there's been updates to it, though.
**Mattia Meleleo** 15:20 Yes, I think it meets another possibility.
**Tyler Yahn** 15:24 Okay, this is just looking for a review, then, is what we're waiting on them.
Okay.
Yeah, okay, cool. Alright.
trace export internal metrics plus, BPF internal metrics. So, Nimran, this is something I think we talked about as well last week.
Looks like Mark has, provided a review.
**Nimrod Avni** 15:46 Yeah, and then I… I fixed, I think, both of those, like, all the stuff that he… mentioned, … I think… I'll check why. I think some of the tests are flaky, but I think maybe, I'll check if it's, … Actual failures, but it should be just ready for… Another review.
**Marc** 16:07 I think if you're seeing with main, probably… we fixed some of the flakiness, or… Yeah, it helps.
But, yeah, I'm sorry I couldn't take another review, but I will do soon.
**Nimrod Avni** 16:21 Okay.
I'll make sure it's, … I'll see if it's, run the tests locally to see if it's, flakiness or… They break something.
**Tyler Yahn** 16:31 Yeah, and like Mark was saying, also maybe just sync with main if it isn't, already based on domain, yeah.
**Nimrod Avni** 16:38 Okay, I'll do that.
**Tyler Yahn** 16:40 Okay.
Fixed Prometheus metrics export, is missing the SDK version target info.
**MM Mario Macias** 16:47 Yeah, I reviewed that. It's… it's incomplete. The… the tests, all the tests are failing.
Because the author missed some… some other, properties they… they should modify. I asked for a modification, but I… still, there are… there… there are… there isn't any….
**Tyler Yahn** 17:10 Any addition?
**MM Mario Macias** 17:12 Yeah, let's see.
**Rafael Roquetto** 17:14 I think… I think he will eventually get to it. This guy is, active in the C++ SIG as well, and the SDK, and he wants to contribute more and more to… to all be so… yeah, I think you'll… you'll change it.
**Tyler Yahn** 17:33 Okay.
then we'll wait, I think next week, if we don't see any update, we can comment and try to get this moved. But yeah, we'll just… we'll wait for feedback on that.
Okay, fix possible memory leak. Mario, this is something we should take a look at, or is this all a work in progress?
**MM Mario Macias** 17:52 No, this is still a draft. Yes, there… it seems there is a memory leak in the hotel exporter. I was trying to reproduce and fix it, but… It's just, some experiments, yeah.
**Tyler Yahn** 18:05 Okay.
Right, well, we'll keep an eye on that one then.
Next up, Mark, added option to remove IP from metrics to reduce cardinality.
Looks like Mario's taking a look at this.
It looks like we're just looking for a review on this one, Mark.
**MM Mario Macias** 18:25 Yeah, Marky is actively working on that. He has submitted some commits today, but still, it seems that the integration tests are failing, so we will need to check.
What?
What's going on?
**Marc** 18:42 I'm looking right now, but ….
**Tyler Yahn** 18:45 Okay. Yeah, alright, that sounds good. We'll keep an eye on it then.
This can get closed, this is kind of annoying. This is getting resolved, we're trying to get an hotel, ….
**MM Mario Macias** 18:56 tagged release out this week, so this should go away. … Yeah, I… I've… I've tried to… to fix it, but this update is breaking… is breaking some unit tests consistently. I don't know why, because the unit tests are… don't make use of the EC2 detector, but they… they consistently fail, and I don't know why, so I need to… to dig a bit more to see, … What's going on, or how can we fix it?
**Tyler Yahn** 19:36 Oh, interesting, okay. ….
**Marc** 19:39 And now that I see this, we probably should remove this lock, because it makes the… Impossible to view this page sometimes, because.
now it's 20,000, but they were like… I tried to open one, and it has 60,000 lines, and the UI was….
**MM Mario Macias** 19:58 Okay. Yeah. Yeah.
**Tyler Yahn** 20:02 Yeah, it's probably, yeah, maybe a debug, level then, if that's the case.
**MM Mario Macias** 20:08 Yeah.
**Tyler Yahn** 20:08 I guess debug's in here as well, so, yeah, okay. … That's weird, I didn't realize it was breaking the tests in this update.
… Man, yeah, I don't know why that would be the case.
**MM Mario Macias** 20:22 Yeah.
Maybe they are using some… global, or they are initializing some global value, some init function with some side effect. Yeah, I don't know what could be the reason. The only thing it's doing differently is this, ….
**Tyler Yahn** 20:42 is… uses the V2 AWS SDK.
And, like, it literally is, like, the same API as the other one, It's just, … huh.
**Stephen Lang** 20:56 Testify got bumped as well.
**Tyler Yahn** 21:00 Yeah, that's true.
Yeah, I mean, that could definitely… that could be something, I guess. Okay, yeah, I mean, we can… We could take another look at this. I was just closing these because, like, they aren't really that, like, consequential, until we get to a tagged release, and then that upgrade is kind of important, but if they're failing, the upgrade's gonna fail as well, so maybe I should take a little closer look.
But, okay.
**MM Mario Macias** 21:21 Huh.
**Tyler Yahn** 21:22 Yeah, I'll try to put this on my list as well, Mario, and work on this in parallel.
Okay, back to non-update ones. The feature improved, Kafka parsing. Let's see, this is from Dimbrod.
**Nimrod Avni** 21:38 Yeah, … it's kind of… I actually have kind of merged into Mattia's previous PR, so maybe when it's merged domain, we can, like, move from all this stuff. Basically, it, like, improves, kind of refactor the Kafka parsing code to be more… like, resilient and make sure it works with, like, all versions, plus having it support… I think we talked about it previously, that from some Kafka version, Basically, we can get the topic name. When we, like, fetch, we do, like, a star.
So I added some, like, caching way to, like, when we get… like, when the consumer starts, we keep, like, a mapping between the UID and the name, and then whenever we see the fetch, we kind of link it.
I forgot to mention, also, like, adding some more attributes, like the… Partition and offset, like, if… in the cases where we, consume from one partition and one offset?
Kind of a big PR, but if anyone has time… I'm looking for a room.
**Tyler Yahn** 22:41 Yeah, I… so this is based off of, Mattia's PR, right?
**Nimrod Avni** 22:45 Yeah, so, like, I wanted to make sure that, I'm all… like, I… the test coverage that Mattia added, I'm, you know, the… because I kind of refactored most of the code there, so I wanted to make sure that… all the tests of Mattia are passing.
And, yeah.
But that's mainly, like, more of a factor of, like, the actual logic of the Kafka parting.
**Tyler Yahn** 23:08 So, if his PR is merged, is this, is this number gonna go down?
**Nimrod Avni** 23:14 Yeah, I'm guessing it's kind of of a combination of both the… it's still a bit more code, like, all the Kafka parser package there is new.
**Tyler Yahn** 23:24 And, some, like, minor changes, like adding more….
**Nimrod Avni** 23:28 attributes and stuff, … yeah, but as soon as Matthias' PR will be merged, a lot of the other stuff will go down.
**Tyler Yahn** 23:36 So this is… I would just say that, like, this is… this is getting to the point where, like, I… for me, personally, like, I can't review Over 4,000 lines of code. Like, that's, … That's such a commitment of ours, to try to work on this. It sounds like you have a few different things in here you're talking about, though, like, is there any way you can split this up into smaller PRs?
**Nimrod Avni** 23:58 Mia, I think I can maybe… Maybe, first of all, I'll wait till my TSPR will be merged, and I'll see how many changes there, and then maybe I can do, like.
you know, just start off with the, like, the Kafka parser direct, like, those 8 files there.
Which is, like, I think most of the meat of the code, and then after that, like, all the integrating part. So I'll see after Matia PR will be merged, I'll try to split it up.
**Mattia Meleleo** 24:22 So I wanted to add a note on this. There is a bunch of test coverage, unit tests, so that number is not really, … Like, you shouldn't fear it.
**Tyler Yahn** 24:35 Well, I mean, we want to review tests just as much as regular code, right? Because that's….
**Mattia Meleleo** 24:39 Yeah, yeah.
**Tyler Yahn** 24:39 So, like, I think that, like, especially if the tests are just additive tests, those are great, those are great, candidates for just being split off, right? Like, if they're a testing feature that's being introduced in this PR, then yeah, I think that that makes a lot of sense to include them. But, like, if they're just one-off tests.
that are additionally being added, I think that's a… that's a really good candidate, to split off, yeah.
**Nimrod Avni** 25:01 I think the additional tests are, like, Matthias PR.
**Tyler Yahn** 25:04 Oh, okay.
**Nimrod Avni** 25:05 I understand.
**Tyler Yahn** 25:06 So there are, like….
**Nimrod Avni** 25:07 Yeah, after that'll be merged, I'll see… we can view and see if that's, like, too much, and then I'll try to split it up. Okay.
**Tyler Yahn** 25:14 Yeah, that sounds… that sounds like a plan. Let's do that.
**Nimrod Avni** 25:17 Cool.
**Tyler Yahn** 25:18 Okay.
Next up, make use of the OTEL OB generator image for proto-seed generation. Mario, this is something I saw you open yesterday.
**MM Mario Macias** 25:28 Yes, I… I… it cannot still be merged. I… I got a suggestion from Rafael, because I… I did a change I had in context that would break some… some behavior, so I have just updated this prototy image. If you observe, this prototy image was a personal image from Docker. So, basically, I just moved all the protocol buffer generation to the OB generator image.
Now that I have updated it and installing wget, I… I will… I will implement the comment from Raphael, and… and then we are ready to merge.
**Tyler Yahn** 26:09 Yeah, that sounds great. I think that looks good. So, what was the comment? Sorry? It's just, ….
**Rafael Roquetto** 26:17 The, … Yeah.
**Tyler Yahn** 26:21 Okay, alright, … Alright, so we're just waiting on, … the WGit being installed, I thought… oh yeah, here it is.
**MM Mario Macias** 26:31 Yeah, I think the image should be ready in… if it is not already available, it should be available in few minutes. I just triggered the… the action to build a new image. Then I will update, coordinate, and… And remove this… this change.
**Tyler Yahn** 26:50 Yeah, okay, perfect. Cool, alright, that sounds good.
Okay. Upgrade the hotel collector to 133.
**MM Mario Macias** 27:04 This is… just an update.
Y-yeah… Yeah, we're waiting for… for tests. I… I… This comment, I didn't see it.
Avoid this dependency wasn't proposed to renovate.
**Tyler Yahn** 27:22 It might have been.
I think that… … hmm.
Let me see… Yeah, there's a good chance that it could have been, or it could just have been held up. Let's see… No… Right, let's not renovate. ….
**MM Mario Macias** 27:52 Yeah, these are issues, I mean, maybe you want to search in the pull request.
**Tyler Yahn** 27:58 Yeah, thank you.
Collector… Yeah, huh, I guess that's not there.
I think it might be… let's see… Yeah, there you go, that's why.
It's sitting in a backlog. Yeah.
**MM Mario Macias** 28:33 Okay.
**Tyler Yahn** 28:34 Yeah.
So, yeah, that just looks like it was coming up. This is just… Gonna close a lot of those dependencies.
But, okay, yeah, otherwise, I think this looks good. Yeah, Marty, you've already approved this. It looks like the tests are passing.
One of the things that this did do is that it upgraded the minimum version of Go, but I don't think that that's a problem for us. I think we're using 124, so, that looks good.
But yeah, otherwise, … yeah, I think this looks ready to go. Okay.
**MM Mario Macias** 29:25 Cool.
**Tyler Yahn** 29:26 Then last up, Docker RM requires at least one argument. Yeah, I've seen this before.
**Stephen Lang** 29:33 That's me.
I just started looking at the integration tests, and… Had issues running this locally.
**Tyler Yahn** 29:41 Yeah.
**Stephen Lang** 29:42 So, just… I think it's to do with the makeval, eval.
behavior on my machine. Maybe different to how it works in CI.
So, I took effectively the same logic, but did it in, shell instead of make.
I did find a bug as well.
Can you see how it checks, line?
260 on the red.
It checks containers twice. It should have been containers and then images, so that was fixed as well, but you can't really tell in the DIM.
**Tyler Yahn** 30:16 Yeah, it's this… I see.
**Stephen Lang** 30:22 So, it should have checked. On 260, it should have checked images.
**Tyler Yahn** 30:26 And not containers, yeah, okay.
**Stephen Lang** 30:28 Yeah.
… That wasn't the issue, but… That was fixed as well, so this effectively behaves in exactly the same way.
Oh, the other thing is I added, the or true.
On the end of the grip.
And this is just if, if there's no results, it prevents … grep from returning a non-zero exit code, so it's just a bit more… Error handling and safety around, … Around this.
**Tyler Yahn** 30:59 Yeah, I'm trying to remember. I feel like I… I had seen this before as well for that exact same grep issue, but I think it must have just been this, is what… what I was addressing. So, okay, yeah, cool. Alright, yeah, this looks… Looks good. Yeah, I think that all makes sense.
I'm kind of surprised that Make… What system are you running on?
**Stephen Lang** 31:22 macOS.
**Tyler Yahn** 31:24 Oh, okay.
**Stephen Lang** 31:25 So I don't know if it's maybe a….
**Tyler Yahn** 31:28 Sometimes that, the….
**Stephen Lang** 31:29 you know, GNU tools are not GNU tools, and they're something else.
**Tyler Yahn** 31:33 Right, right.
**Stephen Lang** 31:34 Okay.
**Tyler Yahn** 31:35 Yeah.
But this works, the shell script works for you.
**Stephen Lang** 31:39 Yeah, yeah, I don't know why the old one didn't… I couldn't quite work it out, because the, … The variable was populating.
like, well, at least I was getting results. There were containers to remove.
Oh, for whatever reason, containers was seen as as empty, because when… the error I was getting was docker RM requires an argument. Right. And the command is docker RM containers.
So, for whatever reason, containers.
Was apparently empty, even though… There were… there were results.
So I… that's why I kind of thought, well, the only thing that's happening on that line… Because the shell command must be working.
Or maybe it wasn't. It's either shell or eval or something along that line that was, ….
**Tyler Yahn** 32:30 Yeah, it may be these, double, signs here. Like, I can't remember specifically, but I think macOS has something unique about that, and, … Yeah, I do remember this kind of thing before.
**MM Mario Macias** 32:45 maybe we can remove all of this just by a Docker system prune.
Basically, the aim of this was on one side, removing the… any… I mean, if something failed, remove any dangling image or dangling cluster. So maybe with a Docker system prune, and say… to remove all the dangling images and stop at containers, we'll suffice.
**Stephen Lang** 33:13 Yeah, but the….
**Tyler Yahn** 33:14 the… that's… that's gonna affect everything on the system, right? So if you have other Docker images running.
**MM Mario Macias** 33:19 Yeah, yeah, yeah.
**Tyler Yahn** 33:24 Yeah, I mean, I'm with you.
… But, yeah, I think it….
**Stephen Lang** 33:30 I could… I could dig a bit deeper, maybe.
Have a look more into exactly what's going on with the eval or the… or the shell.
**Tyler Yahn** 33:38 So I'm not opposed, the only problem is if, like, another author Doesn't have a shell.
or these shell commands are specific… I actually don't know. I mean, it looks like it's just shell. It's not actually, like, bash or, … Other, like, shells, specifically. But, like.
I would want to try to test this on something more than just Mac, to make sure this is… this is running, because it's… yeah, we want to find a solution for everybody, I guess is kind of the only concern I have, if that makes sense.
**Stephen Lang** 34:08 Yeah, this does run every time in CI, as part of the integration test step.
**Tyler Yahn** 34:13 Okay, that's confidence building. Okay, then, yeah, then that makes sense.
… Yeah, I mean, I don't know, this looks fine to me. I don't know if there's much more… outside of, like, what Mario said, something more, like, Docker-specific, which would be great. I wish you could just, like, pass, like.
these, like, patterns to Docker prune.
But….
**Stephen Lang** 34:33 I mean, are the, … Mario, the container names, are they always the same? Are they always known?
**MM Mario Macias** 34:39 they should start by this, yeah, by those patterns, this integration, test. I don't know if… Later, we added new patterns for the integration test containers, but in principle, those are the container patterns.
**Stephen Lang** 35:05 I was just wondering if we literally had a list of, you know, Docker RM Explicit list of containers to remove, and… Whether that command fails or not, it doesn't really matter.
But then you'd have to maintain it, because, you know, the new container's added.
**MM Mario Macias** 35:21 Yeah.
To be honest, I created this task, and I don't really remember the context.
of that, because… this… this integration test task usually runs on CI, and after CI runs.
all the files… I mean, if they run in a virtual machine, I guess all the containers, or the dangling containers, should be removed.
It's wooden sweaty.
**Stephen Lang** 35:52 when you run it locally, the containers are, like, running, so it's nice.
**Tyler Yahn** 35:58 I've also seen it where the CI actually… this step was failing the same way, saying that, like, it had the same error message that Steven's talking about, and it, like… didn't care. You know, like, kind of like what you were just saying, like, it….
**MM Mario Macias** 36:09 Yes.
**Tyler Yahn** 36:09 whatever, it's gonna just delete it anyways. But it's just, yeah, just, it's more about locally, I think, is kind of, like, the key thing.
**MM Mario Macias** 36:16 Okay.
**Tyler Yahn** 36:17 So, yeah, I mean, I'm in favor of this, this looks good to me, … I can… probably review this once we get off the call. But yeah, I don't see any opposition.
So yeah, let's, let's, let's just hope for, let's get some reviews on that, then.
**MM Mario Macias** 36:35 Okay.
**Tyler Yahn** 36:39 Okay. I'll stop sharing my screen here. Actually, I'll double check. Yeah, it doesn't look like we don't have anything else on the agenda.
Any other topics people want to talk about?
**Mattia Meleleo** 36:54 Do we keep track of the flaky tests?
Do we have an issue to…?
instruct them.
**Tyler Yahn** 37:01 We haven't, no. It's a little bit hard. So yeah, we have, in the past, we have had issues to track some of the flaky tests.
Yeah, so we should continue to do this. The problem, though, is that, like, the cause in the CI system, in the logs is very opaque. Essentially, it just says that, like, you know, you should have one successful test, and you have had zero successful tests, so you don't really actually know what the errors are. … And you need to download the actual logs to find the errors, is the thing? So… Yeah, we should probably do a better job at, like, tracking what is actually causing these flakes. … But no, like, I… so the answer is yes, there have been. Those have all been resolved, so if there are still flaky tests, then we should open up new ones, Mattia?
**Mattia Meleleo** 37:52 Yeah, I will open a generic issue for that. For me, it's failing mostly the JSON RPC one and the Elixir one.
I don't know if, for other guys, she's… do we have others, or…?
But yeah, … yeah.
**Tyler Yahn** 38:10 Yeah, I mean, there's a lot. So, yeah, if you found out that specifically those two things, I think, like, just including the test failure lines would be really helpful in an issue, and just… yeah.
That'd be great, so… Please, please do that, yep.
**Stephen Lang** 38:28 Is it… is it worth… Tyler, you mentioned having to download that file, because I've seen that as well. Is it worth keying to that file so that we get the standard out as well?
**Tyler Yahn** 38:37 Yeah, it is. It's something I had asked Nikola about doing in the past, and he was all on board for it, so I just… it's sitting in my backlog. Yeah, if you can… if you can make a change to see it, that'd be great. I would really appreciate that, so then we can just see it in the logs.
And just copy from there.
**Stephen Lang** 38:54 I could take a look, because I'm gonna be in that area anyway.
**Tyler Yahn** 38:57 Yeah, I would definitely appreciate that. I think that'd be really helpful, because, like I said, like, otherwise the errors are, like, super opaque, so, yeah.
**Stephen Lang** 39:05 Sure.
**Tyler Yahn** 39:11 Yeah, cool. Alright, any other, topics, things that people are working on? Obviously, we got some Kafka stuff coming in, so looking at that, anything else?
**Mattia Meleleo** 39:23 I have a question.
which is unrelated to Kafka.
… So, since, for context propagation, there is the requirement of having a BPF loop, the helper?
Have you guys tried in the past to re-implement that without the use of BPF loop? Like, maybe a best effort thing?
**Rafael Roquetto** 39:50 Yes, I think so.
But it got… it got diff… I don't… I don't remember the details, it was a long time ago.
But, I need to look in the code.
It might… might be possible, but it wasn't easy. Sorry, this is not very helpful.
**Mattia Meleleo** 40:05 Because I'm giving it a shot, to… in order to be able to support kernel 5.10.
So yeah, I wanted to know if anyone has tried this, and if there were some, like, major, major pain or major issues.
**Rafael Roquetto** 40:22 It was a major pain, but I don't… I don't remember what kind of, I guess, got paged out of my brain. … yeah.
I have to see where… where is the eBPF loop, again, being used?
**Mattia Meleleo** 40:35 It's used in, three parts, … and three, parts of code. One is the HTTP… I think, the header parsing, I'm not… I'm not remembering. One is the gRPC one.
And I don't remember the third one. Right. But the important one is the HTTP, I think.
**Rafael Roquetto** 41:00 I see, yeah.
**Nimrod Avni** 41:02 Yeah, I'm guessing we can do something, like, without doing something like… iterating, like, X headers or something, like, something that's, like, bound.
You know, in case we can't, we can't load with BPF loop, and I don't know. You can guess, like, in most… I don't know if it's, like, a fair assumption.
**Rafael Roquetto** 41:21 They can… Oh, I think it's a first assumption.
I don't know if it helps, but when we had this other HTTP tracer, which got removed.
Which also did trace parent injection. That did not use BPF loop, I guess, and … There was just a regular loop, but… It had to… … it was bounded to some upper value, like, constant value. The other thing that we did, so I have to look in the code to point out, I'll do this later to you.
is… it's not optimal, but if you're prototyping might be worth a shot. Somewhere in the code, we removed the BPF loop, and replaced with a tail call to… to ourselves. So… The… kind of the program became recursive.
And we keep, like, a… it was like a… some global variable where we check the number of iterations, and we do some tail calls. That was something that just… I will have to look in the code, and then I'll send you the references, and maybe that helps you.
**Mattia Meleleo** 42:27 Yeah, thank you. Because one thing that is worrying me is that we explode with the number of instructions.
And, yeah, because I saw that, BPF loop is being used, in some other loop, and if I start putting bounded loops everywhere, it will explode pretty soon.
**Rafael Roquetto** 42:45 Yeah.
**Mattia Meleleo** 42:48 Okay, thank you very much.
**Rafael Roquetto** 42:50 Norris.
**Tyler Yahn** 42:53 Okay.
Any other topics? Otherwise, you could probably end it a little bit early here today.
Got a lot of things to review, so that sounds probably good.
Awesome. Well, thanks everyone for joining. Good to see everyone. Looking forward to making this, strong push towards the end of the year, so yeah. Yeah, happy to see y'all. See y'all in a week's time.
**MM Mario Macias** 43:17 Bye-bye!

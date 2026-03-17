SIG: SIG Injector
Date: 2026-03-16
Duration: 70 minutes
============================================================

## Zoom Recording Transcript

Michele Mancioppi 00:11:03 Hello.
Jack Berg 00:11:08 What's going on?
Michele Mancioppi 00:11:11 Wait, what's stuff.
Jack Berg 00:11:13 Is anyone else coming to you? Do you know?
Michele Mancioppi 00:11:15 preparations with KubeCon and, everything else. It's a lot.
As always. Are you going to transfer them?
Jack Berg 00:11:25 No, I'm not. Are you? I assume you are.
Are you giving a talk, or just attending?
Michele Mancioppi 00:11:32 I have a sponsored vendor talk, but it's going to be about, sampling in OpenTelemetry, nothing, there's no specific.
Jack Berg 00:11:43 A lot of prep, or is it pretty lightweight?
Michele Mancioppi 00:11:47 I don't know, I mean, preparing it is not difficult, right? I've written articles about it, I have examples, I just need to bang it together somehow.
Yeah. It's not difficult.
I still have gotten no answer from the TC about the packaging slick.
Jack Berg 00:12:09 Yeah, sorry about that, there's, There's a lot of conversations happening in the background right now, about… About how to bootstrap projects, when to… what types of criteria we need to meet to accept them.
And, yeah, the GC and TC are actively talking and arguing.
Michele Mancioppi 00:12:37 the… Which would be perfectly fine with me, as long as I knew that there was still a discussion ongoing.
Jack Berg 00:12:45 Yep, and… Michele Mancioppi 00:12:46 Absolutely, I mean, I honestly, I stopped checking after a bit.
But I have not seen anybody… not received a notification about anybody commenting on that PR since a bit.
Jack Berg 00:13:01 Yep.
that's one of the action items we talked about in last week's GCTC meeting, was, Just to be, more upfront and better and more communicative with, with, you know, what the process is, you know, what to expect, and, timelines, you know, for both the contributors for these proposals, and also for any GC or TC people that might be involved, like, what their expectations are, so… Michele Mancioppi 00:13:35 So, say, if I wanted to ping the TC from, from, the issue, what is the hand, the handle for, Hi, Group.
Jack Berg 00:13:44 It's just OpenTelemetry slash technical committee.
Michele Mancioppi 00:13:48 Technical.
Jack Berg 00:13:49 DASH committee.
Yeah, it's a team in the OpenTelemetry organization.
Michele Mancioppi 00:14:00 Alright.
atoulme 00:14:02 I think… I think we should just get started on this work.
Just make it happen.
Okay, what do you think? Just open up… Michele Mancioppi 00:14:09 I have… I did.
atoulme 00:14:11 You open the report is good.
Michele Mancioppi 00:14:12 entire POC, so now it's, it's whether we get serious and do it on infrastructure or not.
atoulme 00:14:19 I mean, that's… I needed two, so… Let's do it. It's just a matter of… Yeah.
Resources.
Michele Mancioppi 00:14:27 There is already the PR. You can test… you can literally test PR number… in the OpenTelemetry injector.
atoulme 00:14:34 But, like, even if it doesn't really work the right way, it's better than what I have.
Right?
Michele Mancioppi 00:14:40 I believe so.
atoulme 00:14:42 Then let's just go.
You know?
Michele Mancioppi 00:14:46 I don't.
atoulme 00:14:47 Would you like me to approve it?
Michele Mancioppi 00:14:49 No, I want you to test it.
atoulme 00:14:51 Oh, come on, there's more work.
Michele Mancioppi 00:14:53 I know.
atoulme 00:14:55 Ugh.
Michele Mancioppi 00:14:59 Fair.
atoulme 00:15:01 Yeah, yeah, yeah.
Michele Mancioppi 00:15:05 Cry it out. I need people to test it.
atoulme 00:15:09 Got some conflicts, but… Alright.
I'll take a look.
I said that before.
Jack Berg 00:15:17 My topic is actually related to this. So, at Grafana, we've been, we've been trying to integrate the injector into the operator.
And so we have this branch that a bunch of us have been contributing to.
In our, you know, Grafana fork of the operator. And, you know, it tries to do the things that the injector unlocks, like, you know, avoid the requirement for the annotations, on individual pods or workloads.
you know, the classic, you know, thing where you don't need to know whether your application's Musil or glibc.
And, so, like, you know, part of that, is, you know, a centralized instrumentation CR definition, saying.
what versions of the instrumentation you want to install, like Java Agent 2.1, 2.2, etc, what, which workloads you want to instrument, and what you want the configuration to be for each of those, those workloads that you want instrumented, so there's, like, a rules-based approach for that, where it's, like.
You have this array of rules where each rule is a combination of a predicate and a config.
And it's, like, first match wins, so, you know, as we go to instrument… Michele Mancioppi 00:16:33 We're gonna use labels and letters for that.
Jack Berg 00:16:35 What's up?
Michele Mancioppi 00:16:36 I thought you would have used label selectors.
Jack Berg 00:16:39 That's what you use. So the predicate is, like, you know, expressed in forms of labels, so, or in namespaces. I think there's a couple of options on how you can select things.
Michele Mancioppi 00:16:52 Oh, you make it centrally, and once you're de in the, yes. Oh.
Oh, that's unwieldy.
Jack Berg 00:16:59 It's very powerful if you can have a single rule that instruments everything.
Michele Mancioppi 00:17:06 Yeah.
atoulme 00:17:06 Yeah.
So, guys, we're doing something a little different. We are moving to remove CRDs entirely.
Sorry.
Michele Mancioppi 00:17:17 Say what?
atoulme 00:17:20 For taking it into a completely different direction, because we don't think CRDs are actually, like, worth it in most of the cases, like, for vanilla Kubernetes, and certainly for Helm, they're creating a lot of tension. So I have an open PR, where the config file of the operator should be able to take configuration.
That is going to allow you to just bypass all this CR business and all that stuff.
Still not solving anything that Jack wants, and this is why I'm sorry, I took you into a completely different direction.
I feel like this configuration discussion should be separate from the use case, but this, yeah, this is happening. We… Michele Mancioppi 00:17:57 Helma has huge problems with CRDs.
atoulme 00:18:00 Exactly.
Michele Mancioppi 00:18:00 As long as you don't want them to have the same lifecycle as the operator.
For example, I'm having infinite pain with the desktop operator wanting to install the Prometheus CRDs and the Percy CRDs, and what if the customer already has them?
atoulme 00:18:15 You can, you can disable that.
in… there's a config flag to not care for CLDs.
Michele Mancioppi 00:18:24 No, I know, but the problem is, I want home to care, and he cannot deal with it.
atoulme 00:18:29 on that.
Michele Mancioppi 00:18:29 of non-atomic things, and the same CRD definition comes, potentially, from different operators.
atoulme 00:18:36 Yeah, we've had even issues with HUM4 upgrades. So in general, like, I find that defining configuration, especially the instrumentation information, through custom resources is not great.
There's also an open bug in the operator where the operator on each mutating webhook calls is going to list and get CRs.
Without using a cache.
It's crazy.
Michele Mancioppi 00:19:00 That's all right.
atoulme 00:19:02 yeah, it's actually been known to break stuff at large scale. We have 2,000 pods at once. So, just FYI, like, there's, in my opinion, a lot of work put into these operators, it stops having so many damned opinions. And, I'm trying to take slices of the operator and move them to Helm charts, one by one.
I've done it with the target allocator, I want to do that with this instrumentation stuff, because I find that the value of this is a use case, not really how it's done.
And then we force people into very uncomfortable compromises of running a whole bunch of CRDs for no good reason.
So, whatever you do, just try to help me here, just don't bring more complexity or CRD-only stuff. Don't bring new CRDs, or make it possible to do it via config first, because that's cheaper.
Jack Berg 00:19:49 I don't understand what the alternative is. Maybe, if you could elaborate that more.
atoulme 00:19:54 up.
I just drop down all the stuff that you put in the CR in a config map, it gets loaded when the operator starts, and it just works.
Michele Mancioppi 00:20:02 So, effectively, what Antoine is saying, that… screw Kube API for enforcing the schema. The operator will enforce the schema by cropping its pants.
Jack Berg 00:20:11 email I'd read.
Michele Mancioppi 00:20:12 Don't write it.
atoulme 00:20:14 just… just load your static config file on startup, like, you know, intended by communities. Just do declarative config maps. Don't try… Michele Mancioppi 00:20:22 Yeah, but the reason why CRDs exist is because The values here, these are config maps with an enforced schema.
atoulme 00:20:31 Just apply validation of your configuration when you start your program.
Michele Mancioppi 00:20:35 Yeah, exactly, and then the operator, instead of the QBPR rejecting your invalid thing, the operator will enter a broken mode, which is very hard for people to notice that it is in that state.
atoulme 00:20:49 Yeah.
Michele Mancioppi 00:20:50 I think the studies are difficult. Wait until you go and find out staff, principal SREs that do not know that resources can have states and conditions.
atoulme 00:21:02 Yes, yes, exactly. So, you define, like, 2 years of support tickets right there, right? It's just not fun. I don't want to support this. I need things to be repeatable, easy, reproducible, and I've been fighting… Michele Mancioppi 00:21:15 What I'm trying to say is that I do not believe that sidestepping CRDs and pushing more into the opaque and entirely misunderstood resource status is a better solution.
atoulme 00:21:28 Well, it at least is better to reproduce, because you don't even start the operator if your config is bad.
Michele Mancioppi 00:21:35 So, Father, you're leaving the operator in a crash, loop back.
atoulme 00:21:39 How can it start? This config is bad.
Michele Mancioppi 00:21:45 I have.
I don't know, my first thing is that our chance.
atoulme 00:21:49 Do you think it's better to be able to break your operator deployment at any point by sending some bad configuration, like, 5 months in?
I don't like it either.
But at least it's clear.
Anyway, and.
Michele Mancioppi 00:22:03 That's a take. That's a take.
atoulme 00:22:06 And Helm doesn't like CRDs anyway, so you cannot upgrade, and most of the issues we're having are Helm-related with CRDs updates.
Okay, so… Michele Mancioppi 00:22:16 Interesting. Sorry.
So anyhow, Jack, back to us.
Jack Berg 00:22:22 So… so going back, yeah, so whether… whether that, like, you know, I guess it's done via a config map or a CRD, the, like, one of the concepts is, like, a centralized definition of what should be… what should be instrumented and what the configuration is of that, rather than decentralizing it to all of your workloads.
And so, like, so, when, part of this config definition is which versions of your instrumentation you want. I think they need to be, that needs to be, like, decoupled from the operator's version. You need to be able to use, like, operator version 1.1 and select your version of the Java agent independently of that, so that you're not tied to the operator's You know, versioning lifecycle and versioning cadence when you are trying to make decisions about which instrumentation makes sense for your Your ecosystem, your environment.
Michele Mancioppi 00:23:15 But, I mean, you keep saying, the agent version, and I keep thinking instrumentation image version.
Jack Berg 00:23:22 Same thing, yeah, yeah. So I'll try to update my vocabulary, but yeah, so, like, the way that you indicate your agent version is by selecting your instrumentation image version, which, like, you know, right now, the operator it publishes images for the instrumentations, but it doesn't publish a version, an image version, for every version of the instrumentation that's published, right? So, like.
or if it does now, there was a big gap, because it was, like, you know, only publishing version 1.x of the Java agent for the longest time.
And, so, you know, I would be very surprised if they caught up and published all the interim versions of 2.x up till now. So, like, you know, I think the relation to this packaging conversation that we're having is, like, it would be great if there was an independent project That was publishing images that… include, you know, the versions of these instrumentation, these auto-instrumentation resources, and that those images were published with a versioning scheme that was, like, in lockstep with each of these respective instrumentations. So every time a Java agent version was published, there's a corresponding image published. Every time there's a Python you know, instrumentation published, there's a Python image published.
Okay.
Michele Mancioppi 00:24:43 Legally, it's a bit more… I mean, yes.
But the Java agent is the happy use case here. It's a federally monolithic single file.
Based on one single project.
when we talk about any other language, then there is potentially different versions of Contribut SDK that can work with each other.
Or even single instrumentations, where it's… Much less monolithic.
So I guess what you would say is, Following on trip, Materiality contrib… for example, for Python or Node, does it have one version.
Each of the packages is versioned atomically.
Jack Berg 00:25:28 But they still probably have a release cadence.
Right? Where, like, those versions… or do they… or do they not? Do they just, like, publish versions for each of those individual artifacts, like, as needed, ad hoc? Like, when there's corresponding updates?
Michele Mancioppi 00:25:44 I am not sure, to be honest. I mean, what I ended up doing in those packages is, Just to grab the latest.
But… I'm not aware that there is a natural release strategy for these things.
Jack Berg 00:26:01 So, yeah, somebody has to do some kind of, like, curation, so that, like, we can take these kind of fractured ecosystems of Contrib and kind of, like, coalesce all the changes into, you know, a single version of whatever scheme. Maybe it's time-based or month-based or something like that.
Michele Mancioppi 00:26:20 like… Jack Berg 00:26:21 Let, like, you can… you can… You can have an image published with, and that you can select as, like, a user.
Michele Mancioppi 00:26:27 Yeah. There is… So that would be a second work stream, the way I imagine the packaging sake? Yeah.
In-system packages, you need strictly more stuff.
So, for these packages that you're talking about, well, one could make a distro-less image, and then schlop them on top of it, and you just have the files.
But there's a whole bunch of stuff that, you know, good system package, like DEB or RPM.
experience for virtual hosts that, you know, they need to play nice together, configuration files that go in particular places, the way that, for example, you need to modify the HTCLD.SO something files.
So that is not, it's much more stateful. That's why, in the OTEP, I was talking about a system of packages.
Jack Berg 00:27:21 Yeah, no, yeah, I got that, and this is definitely different. You know, we… different types of packaging for different environments, right? So the… what you need out of your package, your instrumentation package, which is like an image in the case of Kubernetes, is different than when you're dealing with bare Linux. But they share some things in common, right?
Michele Mancioppi 00:27:44 Yeah.
Jack Berg 00:27:44 you know, we need to kind of do this, this curation activity, this coalescing activity that we were talking about, which is, like, making sense of the, you know, this disjoint versioning schemes of these different languages, and coming together with something sensible. Some shared parts, some different parts, right?
Michele Mancioppi 00:28:03 Yeah, I agree. The, yep.
Jack Berg 00:28:09 And, you know, I guess the issue that I have linked in the meeting notes is about just, like, the first, I guess, incompatibility I came across. So, like, when I was trying to include the injector and the operator, and allow you to specify your image version for Java, and your image version for Python, and your image version for Node.js. I came across this discrepancy of the, The layout, the directory layout of the injector versus the operator's images that it publishes today.
Okay.
And so, you know, this issue is all about just, like, resolving that, that specific thing. And, you know, I guess it has some things that might interact with this future packaging SIG work that we've been talking about, but, like, you know, also we should just, like, solve it independently of that.
Michele Mancioppi 00:29:02 Yeah, I'm very wary of solving this.
in, the OpenTimes Injector project and SIG, because the next thing is going to happen.
Is that people switch over to using the packages to build images, and then we're fucked.
Jack Berg 00:29:21 Use the… which packages?
Michele Mancioppi 00:29:23 the packages that we use, so we publish DBM packages in the interactor.
Jack Berg 00:29:28 Yeah.
Michele Mancioppi 00:29:29 And that, technically, could be used the way it is now, not the PR that is linked in the chat, but what is now, it could… kind of work.
To make a monolithic instrumentation image.
And I dread the idea That the potential operator could just say, oh yeah, we do that instead.
And then it's a problem of the injector to sort out the versioning of the images with the language 6, because that is obviously not happening yet.
Jack Berg 00:29:57 Yeah, right, that just, like, that just shifts the responsibility to the injector SIG, which made a decision. Yeah, that would not be good.
Michele Mancioppi 00:30:05 That'll be… Catastrophic, because then there is even less incentive the moment that the pain is no longer felt in the operator to go and fix the packages of those images, right?
atoulme 00:30:17 I mean, they'll tell you, I don't understand Zieg.
And then they're like, okay, cool, help you, it's in Zieg. Anyway, no, that's… That's not related.
Jack Berg 00:30:28 So the couple of approaches that I came up with was, like, we could adjust the injector's expectations to match the directory layout that the operator already encodes into its images.
So they have a certain, like, directory naming convention that they, that they rely on, and, you know, the injector could just match that. And it's just… it's a really subtle change, but it's different enough that it matters.
Michele Mancioppi 00:30:52 That screws up the layout. So the current layout, is, You know what?
Let's ask a different question.
What is the expected layout for an LSF-compliant image?
Jack Berg 00:31:15 LSF, I don't know what that.
Michele Mancioppi 00:31:16 Linux file system. It's a set of conventions about where to put which file.
Jack Berg 00:31:23 I'm not sure what they would say about this, because the specific discrepancy between what the injector does and the operator does is just about, like, the naming convention of the directory for, like, the libc variant and the mucil. So you think there might be an LFS, like, convention for how to lay this stuff out?
Michele Mancioppi 00:31:40 Yeah, I'm thinking, thinking yes, the same way that you have System 64 and System 32 on Windows.
Jack Berg 00:31:46 Okay, yeah.
Michele Mancioppi 00:31:46 It looks nothing of this.
Let me, let me ask Claude, just a sec.
That could be it.
Jack Berg 00:32:47 What's that?
Michele Mancioppi 00:32:49 So, I'm thinking, it's usually the correct thing to do in packaging, just to follow LSF.
And, when I look at those names.
They both look wrong to me.
Both of them look wrong.
Jack Berg 00:33:04 Which both? Like, the operator and the injector? They neither match what LFS expects?
Michele Mancioppi 00:33:10 Yeah. It's a long time since I squinted LSF.
But, yeah, they don't look kosher.
Jack Berg 00:33:20 Well, so the other option, besides, like, aligning the injector to what the operator's layout is, it would be to add additional environment variables or config options for you to configure where the mucil versus glibc version is of the Python and .NET instrumentations.
Yeah. And, like, it gets kind of complicated, because .NET has, has, like, 3 sort of directories that matter. There's, like, the Musil, glibc, and also the shared resources directory, and so, like.
like, you know, it's like, it kind of becomes this interplay between environment variables or config options that are… that are competing with each other. Like, if you only specify the shared resource directory, do you assume a convention for where glibc and mucil lay with respect to that, that shared directory, and then only look for the glibc and mucil actual, binaries if those additional environment variables are that. Like, it quickly gets kind of, like, unintuitive. But… Michele Mancioppi 00:34:21 It would stop.
Jack Berg 00:34:21 It'll work.
Michele Mancioppi 00:34:22 Have you tried what happens if you install auto with the .NET installation scripts?
on, a, AMD64 and the ARM64 image after that.
Jack Berg 00:34:35 No.
Michele Mancioppi 00:34:39 Because I would take that as the canonical expectation where files are.
Jack Berg 00:34:44 Is there, like, their installation instructions from, from, you know.NET Auto Instrumentation?
Michele Mancioppi 00:34:51 Business cryptos.
Jack Berg 00:34:54 So just try to, like… But so, let's say we have this, like, this canonical expectations, this source of authority for how the layout ought to be. You know, it still would be convenient to be able to leverage the operator's existing images, at least in, like, the short term, until the packaging SIG provides separate images.
Michele Mancioppi 00:35:21 The funny thing is, I cannot promise you that What the operator does currently is not correct.
I just do not know.
Jack Berg 00:35:31 Yeah.
Michele Mancioppi 00:35:31 Correctly how it is.
So, if it turns out that what the operator does.
is the same way that would happen in .NET.
then I, I could see us migrating to that.
Jack Berg 00:35:46 Yeah, like, let's say… let's say the .NET advice is exactly what the operator does today, then that's, like, a very strong argument to just, like, align on the operator's convention, and then this whole issue goes away.
Michele Mancioppi 00:35:57 Hmm, review the line on the DOSNAT conventions.
Jack Berg 00:36:00 Yeah, right.
Michele Mancioppi 00:36:01 Operator happens to follow.
Jack Berg 00:36:02 Yeah, right.
So I'll add a note to the issue, to do some additional research on what .NET Auto Instrumentation says, and also LFS, and just, like, add details to that thread.
Michele Mancioppi 00:36:14 Yeah, sounds good.
The, when I was, when I was doing the, last summer, when, I did all the, the Libsy shenanigans.
I don't remember I checked how the .NET images used in the operator looked like.
It was… it was so far away from my brains at the time that… It was just for Tarcido. We're… we had… we didn't care. We hadn't shipped .NET images yet.
Jack Berg 00:36:45 Right.
Alright, that's enough of my topic.
Thanks for that.
There's nothing else on the agenda. Does anyone else have things they want to talk about?
atoulme 00:37:17 Who's going to keep condo?
Deep.
Alright, I'll see you then, okay.
Michele Mancioppi 00:37:26 Oh, you're coming. Yeah, no.
Make sure that.
atoulme 00:37:31 I'll try him. I'll try to be around.
Michele Mancioppi 00:37:34 Make sure that during Cube Crawl, you pass by the Durser booth.
I have Jurassi and Cyber in, doing a Hot Ones live with me.
atoulme 00:37:46 Oh, that's cool.
Michele Mancioppi 00:37:47 Yeah, there Don't worry. Jackie, do you know that the Hot Ones show?
Jack Berg 00:37:51 Yeah.
Michele Mancioppi 00:37:52 Yeah, that.
Live.
Jack Berg 00:37:54 Who's gonna be the host?
Michele Mancioppi 00:37:56 Me.
Jack Berg 00:37:57 You're the host?
atoulme 00:37:58 That's cool. That's pretty cool.
Michele Mancioppi 00:38:01 Yeah, and I go through two entire rotations during one key crop. I don't know in which state I'm going… getting out of it.
atoulme 00:38:09 Yes, indeed.
Jack Berg 00:38:10 Gotta keep some beer to wash it down with.
Cool off your mouth.
Michele Mancioppi 00:38:15 More, like, lassy.
atoulme 00:38:19 Well, that's… that's a lot. Yeah, no, otherwise, I think I have one talk where I'm gonna talk about the Collector SIG, and That's it. We… we have a lot of activity around the community space, so there was a bit of an issue with getting the tables for the project, but apparently it's not a big deal.
So we could have an injector SIG meeting next week, if we wanted to.
Is there an interest for that?
Michele Mancioppi 00:38:47 Ladmilla was, was, planning to do some, open, open hours.
For, for a weaver.
atoulme 00:39:00 Oh, yeah.
Michele Mancioppi 00:39:02 I don't know if… The current amount of adoption users is pretty transparent.
So I don't know if there would be enough demand.
atoulme 00:39:15 You could be surprised, I mean, if there's one place you're gonna have questions about Weaver, it could be there, right? So… Michele Mancioppi 00:39:20 No, I'm not talking about Weaver, I'm talking about Inter.
atoulme 00:39:23 The injector for… the injector right now, yeah, this is a little early, but… Yeah.
I don't know, we can play it by ear and see how the week shakes out.
Jack Berg 00:39:38 Nicola's gonna be there, too. I won't be there, but Nicola will from Grafana.
atoulme 00:39:43 I'd like us to use the time. I am overbooked and oversubscribed, but I'd like it if we were able to start the packaging seeks sometime soon, and I would like it if we were by… And 6 months from now, we have a working version of that working.
Michele Mancioppi 00:40:00 Try those PR, because maybe we have a working version of that working today.
atoulme 00:40:05 Yes, exactly.
Michele Mancioppi 00:40:06 Or 3 months ago, also, would have been a good time.
atoulme 00:40:10 But… thank you. Yeah, let's do that. And then on top of it, so the discussion with all the… I think the discussion with the SDKs is just never going to really come to fruition.
if we ask for the TC and the GC to push on them, they won't pay.
Michele Mancioppi 00:40:26 And there is the Open Teleentry Maintainer Summit on Sunday.
Yep.
atoulme 00:40:31 I'm not holding much hope that it will… Michele Mancioppi 00:40:34 I will bring it up, I will be there, and I'll bring it up. Do I hope that something's going to shake?
No. Will I try? Yes.
atoulme 00:40:43 diff.
That's fair enough.
Michele Mancioppi 00:40:46 Because where else are you going to get this rolling if it's not at the Maintainer Summit?
atoulme 00:40:59 Sure.
Michele Mancioppi 00:41:02 I mean, there is no other.
atoulme 00:41:04 there's… there is a body of people that we elect every year who manage the project, right? So… they have a job.
Their job is to make sure we deliver, and one of the big things that came out of KubeCon of America from the maintenance summit, mind you, the discussion that happened during that time was, how do we make OpenTerritory more like a product? Then we wrote a very fancy backpost.
And I have yet to see a single thing that we did with this.
No, I'm not trying to pay attention too much, because, you know, again, busy. But… I… I would like it if we were able to turn this into more of an actionable item that would actually fulfill some of the reasons we're trying to fill here.
And there is no point in having a project if no one can install it.
Michele Mancioppi 00:41:52 Yeah, you're preaching to the choir, yes.
atoulme 00:41:54 I know, I know.
Otherwise, we're gonna all build our own packaging systems, and then we'll just be in deep, deep trouble 5 years in.
Well, I look like… Michele Mancioppi 00:42:05 It's going to be insanity, because without the language Sikhs collaborating, they can break shit without any remorse.
atoulme 00:42:14 So, I mean, the only way that I've seen it done before is the really strange from Eclipse, where some old, crusty, 50-some-year-old I was in charge of going from project to project and just telling them, you did not meet the deadline, you did not do the work, your acceptance tests don't pass, you cannot be in the release train.
And people just scramble, like, what!
The train's leaving the station? Like, yeah.
You had his dreaded at that time.
Michele Mancioppi 00:42:41 Antoine, there is no release train.
atoulme 00:42:43 No, no, but we have to make one.
Otherwise, how do you ship stuff?
Michele Mancioppi 00:42:51 I mean… atoulme 00:42:51 Okay, alright, serepancy. We just wait to the bottom of the mountain, and things will just come down.
Jack Berg 00:42:57 I have a different perspective here. I don't think you try to get everybody aligned. I think you just… you work around, the… what happens when everybody has their own release cadences, and your project, which is like a confederation, a federation of, like, a bunch of individual projects, and You know, you decouple the two, and you don't try to have one product that has one version. You have a product with a configuration scheme that is where you specify all the subproducts that you want to configure, and you explicitly say what the version of collector you want. You explicitly say what version of the injector you want, you explicitly say what version of Java instrumentation you want.
atoulme 00:43:33 So you build a manifest of what it is that you're going to install, and it's a set of conversions which are known to work well together, because you have some integration testing there.
Michele Mancioppi 00:43:44 Wait a second. So, when you look at the different components, right, OTLP is effectively written in stone.
For a whole bunch of things, I mean, that is one of the interfaces.
The other interface we need is the activation of the SDK.
that is what the language SIGs are going to break, like, the same way that when going from the JS SDK 1.x to the 2.x.
You needed to install it in a different way.
That technically broke the contract, because no contract was done to be forward extensible, right?
atoulme 00:44:20 Yeah, your config file change is… is the most breakable thing, right? So declarative config is helpful to get there.
Michele Mancioppi 00:44:29 No, I'm not talking about you in the declarative config, because that is short.
But the way that the injector is supposed to activate an SDK, That is a contract, which, at the moment, has only one signatory.
atoulme 00:44:43 That's true.
But you could, you could create… so, this is what the restraint was for, is that you said, here is the set of integration tests you need to fill.
and make pass, so that the interface is filled, and then you can be part of the next version of the overall. So when you update in your manifest the version of the JS SDK, it goes through the testing, and then if for any reason you broke something, then you need to fix the test, document the breaking change.
Michele Mancioppi 00:45:13 No, I don't know if, so I like the… for example, with Jack, we had spoken somewhere, I don't remember where, in which form, about contributing integration tests to the language 6, or something like this. The contrary here with Injector, if you break it, you don't break it.
The, there is there, of course, the question of… who mandates these tests? Is it the technical committee that goes and says, hey, these are the tests for Python. These are not going to fail. Otherwise, you don't ship.
Jack Berg 00:45:43 Well, so, like, one concrete way that we can achieve this is, like, so there's… there's gotta be a repo somewhere where, that is publishing these packages, that is publishing these images that correspond to the instrumentation. And, yeah, so, you know, Mikel, you've, you've proposed putting it in the injector for now, for lack of a better place.
And, you know, there should be some sort of build action that automatically runs an update and publish sequence when Java agent publishes a new version, when Python agent publishes a new version. And so, like, that automation could include running of an integration suite, and if that integration suite fails, automatically opening an issue on the respective repository. So, like, we can… Michele Mancioppi 00:46:34 Yeah, it's plus, but the integration test, you put in the… if you want the Java agent not to break it, you put it in the open-telemetry slash java dash instrumentation.
Jack Berg 00:46:46 Yeah.
Yeah, yeah, yeah, yeah, yeah, right.
Michele Mancioppi 00:46:48 Excellent.
Jack Berg 00:46:49 like, it's got to be in both places, right? So, like, you know, you need to… it's like a belts and suspenders thing. Like, ideally, they have it in their repository so that any change that they make, a break is detected. But also, we need to run our own tests to verify, like, you know.
Trim me that.
Michele Mancioppi 00:47:05 Yeah, but those are more acceptance tests. I mean, of course, I mean, we have an entire suite of testing that the thing actually works.
The, at the moment, we are not publishing, really, those images based on… so the system package that we have today is published when the injector updates, although we have now a release schedule for the injector, but, for example, we are not using Dependabot.
To follow the versions, right?
atoulme 00:47:33 What should… Michele Mancioppi 00:47:34 That's something we do in, in, Interstateo, but not in… I think it's.
atoulme 00:47:38 We need to do that. The renov thing is just broken, because I don't know how to do this properly. So, blame it on me not being good at RenovoBot.
renovate boat. So… Yeah, we should do all of the above anyway, right? So… One thing that could be interesting is to also it starts to dream up of stuff that is just completely weird, but right now, we don't have any checks on which metrics are being emitted by those SDKs, for example, even the metadata metrics. We've had surprises in the past where SDK was starting to get really chatty with some integration.
Michele Mancioppi 00:48:19 What's… atoulme 00:48:20 And then all of a sudden, you have cardinality issues because someone just sensed 33 million data points with, like… I mean, it's just this type of.
Michele Mancioppi 00:48:26 Or stable instrumentations that are meeting OpenTelemetry HCP semantic conventions from where I was in kindergarten.
atoulme 00:48:33 Alright, yes.
Michele Mancioppi 00:48:35 I'm just… Node.js.
atoulme 00:48:37 That's yes.
Yeah, so we can, we can, we could expand on this type of, like, just codifying the behavior.
And that would probably help with stabilization of those SDKs anyway.
Anyway, this is plain-the-sky stuff at this point. Let me review your PR, make sure we get there. Let's talk next week about how we can make this so it's a reality. And I do not want to spend our engineer's time in maintaining our own packaging, distribution, and testing of those agents. It should be done upstream.
Where we have maximum capability to affect it.
Not, you know, our stupid vendor stuff.
Michele Mancioppi 00:49:14 Ask was saying that to host the dev and RPM repositories, there's a bunch of credits from Oracle Cloud.
atoulme 00:49:23 Oh, wow. Okay.
Michele Mancioppi 00:49:25 Right? Fine.
atoulme 00:49:27 I did.
Michele Mancioppi 00:49:27 Better than… better than not?
But… atoulme 00:49:31 Okay.
Michele Mancioppi 00:49:32 Every other question's still open.
atoulme 00:49:35 Yeah.
I mean, okay. No, that's actually pretty exciting, right? We didn't have a solution before, so at least that's a way. We just need to set the GPT keys, and… I don't even know how to use Oracle Cloud. Is it, like, a 3-like thing for… Michele Mancioppi 00:49:52 I have no idea, and honestly, I'm not looking into that until… We have a Pakistan sake.
atoulme 00:50:00 How about we, we do the horrible thing and we just ship everything into GitHub pages until we count anymore?
Michele Mancioppi 00:50:09 I thought about it.
I think also, if I remember correctly, the PR, it actually does that.
atoulme 00:50:14 Okay, great.
Michele Mancioppi 00:50:16 But don't quote me on it, it was, like, 2 months ago, which… In many years, like, 10 years.
atoulme 00:50:24 That good… yeah, that game was… Young and Spy, yes.
All right, I'll.
Michele Mancioppi 00:50:30 I don't think it's a great idea, and I don't think it's a great idea to actually change the location of the, of the, the packages afterwards?
atoulme 00:50:42 Oh, you're gonna have to do some… you know, good old DNS work, right?
Michele Mancioppi 00:50:48 DNS on what?
And do we have a DNS entry that goes packages.opentry.io that we can change?
atoulme 00:50:57 I certainly don't, but, you know, this is also why having the TC and GC involved here would help a lot, because they know how to do that. I don't.
Michele Mancioppi 00:51:06 Yeah, no, but at the moment, the reason why this is stuck is because the GC and TC are not, in point of fact, working on it yet. They're talking about working on it.
That's my understanding.
atoulme 00:51:17 I'm glad we're here, too.
Michele Mancioppi 00:51:20 There is no… that PR, the community PR, is stuck on not having a GC sponsor, because we have a GC sponsor.
Is it a C-sponsor that is missing, to my understanding?
Whether that is the only blocker, I cannot begin to say.
But that is the one I'm aware of.
atoulme 00:51:42 Okay.
Alright.
Michele Mancioppi 00:51:51 It's a pity, because, I mean, we could have done this For this year.
And it's still waiting for… Some red tape to get started, honestly.
atoulme 00:52:07 Yeah, I'm guessing this is just a symptom of the malaise there?
Why is that happening? What is it doing instead? What is the TC working on that is higher priority?
Michele Mancioppi 00:52:17 I'm sure they're working on a lot of stuff, and it's not easy to be on ATC, but right now, it's a hell of a bottleneck.
atoulme 00:52:24 Okay.
Because they said no to the MCP server as well.
There was another initiative in the queue.
And they said no.
Like, I… okay.
Jack Berg 00:52:37 Like, what are the big things that are being worked on right now?
atoulme 00:52:40 I mean, if you're not doing this, what are you doing instead? Where's the effort being?
Perfect, Tom.
Jack Berg 00:52:45 Profiling?
Oh, cool. Entities.
atoulme 00:52:49 Okay.
Jack Berg 00:52:50 Semantic conventions.
Until a week ago, declarative config.
atoulme 00:53:02 Oh, look at you, you got time!
Jack Berg 00:53:05 I got time, yeah, and the last time I signed up to sponsor a project, it was a 3-year commitment of, like, 20-plus hours a week.
Michele Mancioppi 00:53:15 I cannot tell you that this is going to be less than 3 years, but it is going to be less than 20 hours a week.
Jack Berg 00:53:22 Yeah, I'm just… I'm waiting for the dust to settle a little bit, personally.
what are the other projects that are going on?
I'm sponsoring, like, the Ecosystem Explorer, but that's kind of hands-off, but just reworking the Ecosystem Explorer on the dock site.
And then… ba-buh-buh… Maybe there's a spreadsheet somewhere, like, I think it's, like… Should we look at it synchronously, or no?
atoulme 00:53:58 Okay, don't worry, do we not… do we need to have a window with the whole TC or whole GC to kind of make our call?
Is that how we would move things forward?
Jack Berg 00:54:20 So, I've advertised this to… oh, the other things that are going on is, is Prometheus stabilization. That's taken up effort.
Michele Mancioppi 00:54:28 That's a big one.
atoulme 00:54:30 Okay.
Jack Berg 00:54:31 But, Yeah, like, so I've tried to pitch this to the TC and in the maintainers call and be like, hey, like, somebody should really sponsor this. And, you know, I talked to Mikael and said that, like, you know, I would consider being, like, a sponsor of last resort, but, like, I really do want somebody else to pick this up.
And… Yeah, it just hasn't happened. So.
Michele Mancioppi 00:54:58 Notice, I didn't share any of this, you did, right?
Jack Berg 00:55:01 Yeah.
atoulme 00:55:06 Let me ask Tigrant, because that's free.
I mean, he's similar to me, but… Sponsor… sponsoring this… Yeah.
Let's see if that works.
Jack Berg 00:55:21 See if you all can see this.
This link I'm gonna send in the chat. Do you have access to that? Is that private?
Oh, it's restricted.
atoulme 00:55:29 not… Jack Berg 00:55:31 It's a list of all the SIGs, and and all the TC people who are sponsoring their respective SIGs, and at what sponsorship level. And there's, like, a little pivot table where it shows you know.
how many sponsorships each TC member is performing, and at what level, so therefore you can, like, quickly calculate capacity.
atoulme 00:55:54 Do you… okay. Do you think there would be, Is there a TC member who's free? Do you need more TC members?
Jack Berg 00:56:03 We can't add more TC members, we set a cap of 10.
atoulme 00:56:06 Okay.
Jack Berg 00:56:07 We can have, So, one thing that I talked about doing in the last GCTC call was, like, I volunteered to do… add some tooling to the community repo, so we could, so we could have a auto-generated report that showed a list of all the work streams in progress, and so that's SIGs, and projects, and OTEPs, and who the people are that are, like, you know, engaged in them. So you can kind of see at a glance, like, where time is being spent, and identify, like, who might be candidates to work on other projects.
And also, like, get a feel for, like, what the project capacity is. Like, how spread thin are we right now?
atoulme 00:56:54 Yeah.
who's working on… let me take it the other way. Who from the TC is actually tasked or volunteering their time towards the productization of OpenTelemetry?
Jack Berg 00:57:07 the productization, nobody on the TC has… is taking that as, like, their… atoulme 00:57:14 Alright, so let me take it the other way, right? So, let me be more clear. There is work that was done by the GC to say that the direction of a project is to be more like a product, right?
Stability blog, where is that? Evolving upon destabilization and release practices.
November 7th, 2025. There it is.
Who is working on that?
Jack Berg 00:57:46 Austin Parker is working on an OTEP.
atoulme 00:57:49 Oh my god, he's still on that?
Jack Berg 00:57:52 Yeah, that's, like, yeah, he made a very controversial, big, expansive OTEP.
Yeah, and like… and it's so big that everybody can take issue with a thousand parts of it.
atoulme 00:58:02 Yeah, that's… I asked him if I could help him, he said, sure, the OTIP's coming out, and then you'll be able to help.
I think that was January.
Jack Berg 00:58:10 That's the issue with trying to, like, make such, like, a broad, sweeping proclamation, is that it's hard to get everybody aligned.
atoulme 00:58:17 Yeah, never do that. Just do the smallest possible step to move forward, right?
Jack Berg 00:58:23 So… That one feels stuck.
There's, like, 100 plus comments on it, and I don't… I think it has one or two approvals, but… atoulme 00:58:34 I know that also, like, Austin Parker was impacted because Honeycomb changed up a little bit things, and there was a… Late hour? Like, my day off.
Michele Mancioppi 00:58:42 Austin got, got promoted, to head to… atoulme 00:58:46 Yes.
Michele Mancioppi 00:58:46 Director.
atoulme 00:58:48 It's no longer just open telemetry, and… he's got, like, a lot more in terms of responsibilities at Honeycomb.
So… the TC is not going to pick up any work until the OTEP is adopted?
Jack Berg 00:59:02 No, like, it's not… atoulme 00:59:04 She's not even that, right?
Jack Berg 00:59:05 It's not… it's not even that. Yeah, like, the issue is that the GC wants to do a thing, and thinks it's important, and wrote a blog post about it, but we're… we don't have a hierarchical arrangement. You can't… nobody has authority over anybody. Everybody has to volunteer for things.
atoulme 00:59:20 Yeah.
Jack Berg 00:59:22 It's open source.
atoulme 00:59:24 Yeah, you're supposed to build consensus in, you know.
working codes works best. So I'm gonna go back to Michael and apply his patch, and then we're gonna go from there.
Jack Berg 00:59:35 Yeah, I mean, like, is… If you can get stuff done without having to depend on other people, without having to get red tape, but also, like, you know, preserve the ability to adjust or publish things in different names if you need to, or relocate things, once, sort of, the red tape and bureaucracy catches up.
Michele Mancioppi 00:59:54 This feels like a defeat of the project.
atoulme 00:59:58 To be clear, like, this is bad leadership, because leadership's not supposed to write OTEPs. Leadership's supposed to tell people to go write OTEPs.
And we messed up.
We should… we should really just empower people to go do stuff, not… Not bees, weird.
entity where we try to, like, have the GC write the roadmap.
Okay, well, it was great feedback. I'm sure someone will care about it when I say that to them, but… I agree with Mikuli, that's a… that's a famine.
It's not great.
Michele Mancioppi 01:00:33 I am seriously concerned. The moment you go ahead and republish packages, From an official segue.
We are stuck with it.
atoulme 01:00:44 It will very quickly turn into that, or just move the clock up the side.
Michele Mancioppi 01:00:48 And one that, I mean, has the PR, but I am not deploying packages. I'm not getting involved in deploying those packages anywhere public.
Until there is, there is some consensus on the fact that Langer Sigs are not just gonna give me the candle over.
He is.
The kind of bot that came up with that?
atoulme 01:01:08 That's fair, that's fair. But I think that that requires an intense amount of lobbying and joining every SIG meeting for, like, 3-4 weeks, and starting.
Michele Mancioppi 01:01:18 This is what I was expecting the TC to be on. Hi, I'm from the TC, I am saying you're getting these integration tests.
atoulme 01:01:27 Yes, I'm here because we decided to stabilize the project, and therefore, we will be working together to make it so that you have this level of competence shown through your packaging, so we can get you over the hump and really get you to the masses, because right now.
there's 5 guys who know how to install your stuff, like, and you have these weird dependencies, and going back to the qualms you've had with Python, like, you know, look at all the things that you have to install just to get Python working, and… Having a C++ dependency is terrible, like, etc.
Michele Mancioppi 01:01:59 Honestly, I mean, the… I don't think there is, like, massive amounts of improvement That one can make on the proposal for the packages, not without using it at scale first.
So I don't expect involvement of the TC.
to find glaring bugs, at least I hope not. But we need the authority of the TC to go to a language6 and say, hello, now you have a new requirement.
Because without that, it's not working.
Beslanguage CX have made it very clear over time that they don't care about packaging.
atoulme 01:02:34 suddenly they don't know what to do. I mean, they play… they… they… they go Betty up. The second I push, I'm like, oh no, I… Consist in the discussion.
Okay, alright.
Let's see if we can do… no promises, because… busy.
Michele Mancioppi 01:02:59 Well, let's see what happens in Amsterdam.
Maybe we'll get lucky. Stuff happens.
atoulme 01:03:05 I don't… I think that will depend entirely on whether the Wi-Fi works well or not.
Given how London was, I would not hope for much, and .
Michele Mancioppi 01:03:18 We brought… we always bring along a dedicated access point.
Because that thing never fucking works.
atoulme 01:03:25 We, we also bring along a lot of those, and then, everybody's just jamming everybody else's.
Michele Mancioppi 01:03:31 Great.
atoulme 01:03:32 That's how it works.
We'll try to see what I can do. Is… do you know if Austin Parker's coming to KubeCon? You?
Michele Mancioppi 01:03:44 Go?
atoulme 01:03:45 Austin Parker.
Michele Mancioppi 01:03:48 Who… atoulme 01:03:49 Maybe a different question. Do you know who from the GCNTC is going to Kipkon? I know Morgan's going.
Michele Mancioppi 01:03:55 I know that that is not. Ludmila will. Josh is not.
Trask is not.
atoulme 01:04:03 Whoa.
Michele Mancioppi 01:04:04 Pablo… Don't know.
atoulme 01:04:07 Auto Biants is coming, I think.
Yes, I can tell you. He's also pretty local, he's, like, Madrid to Netherlands.
Okay.
Yeah, so, that's the point, is like, even if we were all there, if they don't show up to that committee meeting, I'll try to be at the Maintenance Summit, My flight is overnight.
And I show up in the Sunday morning.
So I'm gonna be pretty smashed, but… Michele Mancioppi 01:04:41 They're gonna be freshly grows.
atoulme 01:04:43 I'll smell… I'll smell like an Erbus.
Yay.
Michele Mancioppi 01:04:50 Folks?
be in the Netherlands.
atoulme 01:04:52 Susan?
Michele Mancioppi 01:04:54 My… atoulme 01:04:54 But the.

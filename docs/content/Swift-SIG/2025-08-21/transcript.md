SIG: Swift SIG
Date: 2025-08-21
Duration: 72 minutes
============================================================

## Zoom Recording Transcript

Vinod Vydier 00:00:41 Moving on.
Hey, hey, how are you?
Bryce Buchanan 00:00:48 Good, how are you doing?
Vinod Vydier 00:00:49 Good, good.
A lot of meetings.
Bryce Buchanan 00:00:54 Oh, yeah.
Vinod Vydier 00:00:55 speak.
nacho 00:01:36 Lo….
Bryce Buchanan 00:01:38 In a nutshell.
nacho 00:02:08 Yeah, Bryce, I had created… that was a copy of the previous.
Bryce Buchanan 00:02:14 Oh, oh, okay.
nacho 00:02:16 I had not changed the date, but yeah, I had already cut it and moved.
Bryce Buchanan 00:02:19 on the date at the top.
nacho 00:02:23 Yeah, I forgot the name.
Bryce Buchanan 00:02:24 There we go, okay.
Thank you.
nacho 00:02:29 I have not cleaned up anything, just copied and moved from new topics to topics from last weekend.
Bryce Buchanan 00:02:34 I gotcha, okay.
True, true.
Let me share my screen.
There we go.
Looks like the right one.
Okie dokie, shall we get started? I'm not sure if Ari's gonna show up or not.
Okay. Alright, so topics from last week. Let's look at this data compression issue.
Looks like this is still open.
On the data compression, …
And just know, maybe we can, ….
nacho 00:04:35 Yeah.
We can ping again.
Bryce Buchanan 00:04:38 Yeah.
nacho 00:04:45 But that's only for CocoaPort support, right?
Bryce Buchanan 00:04:48 Yeah, this is only for CocoaPods support.
nacho 00:04:50 Ambition Pro.
Bryce Buchanan 00:05:17 Okay, alright, repository division follow-up, so I'm still working on getting this repo set up. It does exist, but, …
the way that OOTEL does this stuff, is pretty complicated, so, like, I need to push
an initial commit to get the main branch created, but I can't do that right now because I don't have the permissions, and I've followed all the instructions, so I've reached out to, like.
One of the, …
one of the fellows that, like, manages this stuff and hosts, like, the repo that holds all, like, the Terraforms for the OpenTelemetry repositories, so…
Hopefully he can help me out get this, get this set up.
So, …
I've got all of the teams and collaborators set up. Oh, I can't look at that right now. …
And, everything looks like it should, but I can't push to it, so…
I don't know. We'll… we'll try to figure that out.
nacho 00:06:36 Yeah… Yeah, just for… I don't know if you followed the last meeting.
Bryce, just to… for you to know, there were some… Concerns from some people.
… Especially, I think it was Martin Fallman and Adriana that were saying that
at the end, having this separation with IPSDK and the
in the country with all the rest of the things would mean that
It will end up downloading everything again.
Well, I mean, it's gonna happen no matter what.
Bryce Buchanan 00:07:14 Yeah.
nacho 00:07:16 So yeah, there were all sorts… they, they… Yeah, they weren't…
Also, saying about keeping some basic stuff.
In the…
in the base repository that does not have dependencies, things like that. That was also something, like, Alex.
Started doing, just keeping in that
Ripple, whatever, didn't have dependencies and things like that. So yeah, yes, yes, food for thought.
But that, that, that was something that happened that week.
Bryce Buchanan 00:07:51 Okay.
nacho 00:07:52 Around, around this issue, or, or around this, new change.
Bryce Buchanan 00:07:57 Love you.
Turtles all the way down, as they say.
Okay, decision on view, I guess, did we talk about this? Yeah, so we're not gonna, ….
nacho 00:08:12 Yeah, I, I explained the reasons that that was, …
the decision was taken, after the meeting, by, by the….
Bryce Buchanan 00:08:23 Okay, alright.
nacho 00:08:24 Ball de… Maintainers.
Yes. Yeah.
Bryce Buchanan 00:08:30 Yeah, yeah. Yep, okay, very good. So I'll just remove that off of the thing then there. Added test to new upload task instrumentation…
All merge, very good.
And, issue with the metric builder 2.0. Yeah, so this is, this is by design, so the, the, spec has this
as a no-op until there's a view, and then it switches from a no-op meter provider builder to an actual meter provider builder SDK, so…
…
it just looks weird the way that it needs to be handled, due to the way Swift, like, has those, you know, associated type resolutions.
Okay, are there any new topics?
Bee Klimt 00:09:26 On the issue of the meter builder, I might suggest, some additional documentation might be helpful, because I found that pretty confusing, too.
Bryce Buchanan 00:09:34 Oh, yeah, certainly, yeah. Let's add some notes to there.
Okay.
If I can follow up on that.
… let's see here…
I guess, shall we, … shall we look at open issues?
Oh, interesting.
gRPC version 1.15.0 is not working for metrics.
nacho 00:10:34 Yeah, there was a… we read about it, and we… Ask about the versions? Yeah.
So, he was talking about the library?
It was talking about our library in progression 15, which is not the latest one.
Bryce Buchanan 00:10:52 Oh, yeah, okay. Mmm.
nacho 00:10:55 Yeah, we had that last meeting about what that pressure referred to.
Vinod Vydier 00:11:02 Yeah, we should ask them to try with the new version.
Bryce Buchanan 00:11:05 I see, okay.
nacho 00:11:06 I don't know if there are changes there.
…
And that's the collector version that, yeah.
Bryce Buchanan 00:11:16 Okay, alright. Yeah. This… this version is the… no, that's the collector version down there. Yeah.
nacho 00:11:22 Yeah, that's our… This is the S. That's the OpenTelematist version, yes.
Bryce Buchanan 00:11:27 Yeah, okay.
… let's take a look here.
Vinod Vydier 00:11:33 Yeah, it's not… it's not that old, yeah, it's only, yeah, 1.15 is April 8th, so…
I don't know if we updated any of the protobufs after that.
Bryce Buchanan 00:11:46 Hell yeah.
Alolita Sharma 00:11:48 Hey, good morning, good morning.
nacho 00:11:50 Right?
Bryce Buchanan 00:11:55 I'll take a look at this. …
And just to kind of verify if it's still a thing.
In the later versions of the SDK. there's one thing I wanted to share, just to bump back out to the new topic. So, I've been working on an OPAMP implementation for, …
…
the Elastic agent, and since that is a potential… I mean, it's part of Hotel, so it's probably… I'm probably gonna contribute that up to, this project, so if you guys want to take a look at it and let me know what you think.
Alolita Sharma 00:12:36 Oh, very cool. That's very cool.
Bryce Buchanan 00:12:38 … I'll add the PR.
Vinod Vydier 00:12:52 So does it also use the, like, a common…
like a protobuf for the OPEB?
Bryce Buchanan 00:12:57 Yeah, it uses the protobuf for the OPAMP.
So, …
So, any feedback on that would be helpful. I know it's in, like, the Elastic repo, but, …
Oh, it's already been approved by…
But it's not building. I should probably figure that out. …
This might be, this issue that we had in our repo, too, so I'll need to bring that up to date.
Or in the Swift repo, rather, with the, with the macOS builders.
Okay, so back to, back to the issues.
Jaeger Package Propagator Field Center. Hmm…
Oh, yeah, okay.
Okay, so I was wondering if this is a, background session.
Prop… or it's, executing outside of the context.
….
nacho 00:14:30 Yeah, he says that.
He's getting across in the Jagger baggage propaganda?
But he's not setting up the baggage propagator, which doesn't make sense at all.
Bryce Buchanan 00:14:41 Yeah, yeah. Okay, so….
nacho 00:14:44 Or, or the symbols are totally…
broken, or is something strange there. So I asked how… I mean.
How he was setting the baggage propagator?
Bryce Buchanan 00:14:56 If he was doing it himself, if not, if not.
nacho 00:14:59 Maybe it's the Datadog SDK.
Bryce Buchanan 00:15:02 Yeah, Datadog at CK.
nacho 00:15:03 Initializing things on their own.
I'm not doing that properly.
Bryce Buchanan 00:15:08 Well, and we… we don't… Do we instrument background?
tasks? Like, are we actually… is our instrumentation actually capturing background tasks?
I don't think it does.
It avoids them.
nacho 00:15:25 if he… Yeah, we are… the auto instrumentation is…
It's not instrument in background tasks.
Bryce Buchanan 00:15:36 Yeah.
nacho 00:15:36 We… we are not… keeping that. But the… but the…
Yeah, but the strange thing here is that
in the line on top of the one you have selected, it shows JaggerPro propagator.
the agar baggage propagator, and…
I mean, that's not initialized by default in the pen telemetry library, but it's not in any baggage propagator, and…
On the other side, In the thread that it has in the Datadog SDK, it also says that …
He's not, he's not using the….
Bryce Buchanan 00:16:19 Jagger, that's… he's only using the Datadog SDK, so I don't know where that… Yeah, that's….
nacho 00:16:25 Where that call comes from, so….
I was asking how he was…
setting that, because I don't know if that's… that…
Yeah. Where'd that line coming from?
Bryce Buchanan 00:16:38 Yeah, yeah. Or the symbols are bad, definitely, so in….
nacho 00:16:42 But… it must be there. If it shows the name, at least, of the module, that means that
Some call is being added there.
I don't know.
Bryce Buchanan 00:16:54 Yeah, what is… what the heck is this? Like, why is that…
Why is that in the stack trace? Why is there a URL in the stack trace?
That's really weird. Okay, I'll… I see that he responded to my query, so I'll reply with that and make a note that, we don't…
there's, like, this is something that's set up manually. And yeah, I'm skeptical about its… how it will perform when the device is not, initialized, or when the app is not initialized, so that, like.
like, we're not instrumenting the, background tasks, I don't believe, so….
nacho 00:17:41 Yeah, probably Datadog is doing that.
Bryce Buchanan 00:17:43 Yeah.
nacho 00:17:43 It's… it's crazy, it's crashing there, and the symbols are… Wrong?
Somehow, and it shows something random in the, … In their memory.
It shows a random address in a library that is sour, but….
Bryce Buchanan 00:18:00 Yam.
nacho 00:18:01 It doesn't have… relation to us.
Alolita Sharma 00:18:05 Yeah, maybe, maybe we should just state that on that issue, that it's just… they need to do more debugging.
Bryce Buchanan 00:18:11 Yeah, yeah.
Alolita Sharma 00:18:12 SDK.
Bryce Buchanan 00:18:13 Yep, yep.
Okay, mute, we're still following up on that.
What should… I don't know what our, policy is for, like.
you know, abandoned issues, like, how long should we leave them open? Like, what… what is the stale issue definition?
Alolita Sharma 00:19:05 I think, I think, Hotel doesn't have any…
clear, time period, but I think…
That typically, in the collector, for example, …
Issues that are, like, 2 years old, you know, or so, have definitely been retired, like, just closed, and then, if somebody comes back, then they get reopened.
Bryce Buchanan 00:19:29 Yeah, they can reopen it, I think.
Alolita Sharma 00:19:31 Yes, exactly.
Bryce Buchanan 00:19:32 There's no… yeah, it's not really a big… it's like, oh, it's not a big bunch of hoops you have to jump through to….
Alolita Sharma 00:19:36 No, no, no. You can just take a call and say, hey, you know, we'll retire the issues after a year or two years. I mean, the collector typically is very active, so therefore, you know, for… there's just too many issues.
Bryce Buchanan 00:19:51 sorts of… with these sorts of issues, like, these… I mean, like, when you're building on iOS, like, the… it'll just get, like, hung up and run into this problem, like, and then you, like, restart your computer, and then it works.
Alolita Sharma 00:20:05 And it goes away, yeah.
Bryce Buchanan 00:20:06 Yeah, so…
So, like, I mean, I wouldn't be surprised if, like, it just started working, and then they just forgot about this issue. So, you know, after… I feel like something like this, like, if… give it another two weeks if they don't say anything, and then we can probably close this.
nacho 00:20:21 Yeah, yeah, for this one, I think that he just selected, probably Mac, …
with Catalyst or something like that?
Bryce Buchanan 00:20:30 Yeah, yeah.
nacho 00:20:31 NEO doesn't have symbols for. Yeah, yeah. Because it's…
Yeah, it's looking for a simulator on… an Intel simulator.
Bryce Buchanan 00:20:41 Yeah, Apple.
nacho 00:20:43 Apparently, that doesn't have Apple support for that. Yeah, I mean, blaming Apple is always the easiest.
Alolita Sharma 00:20:50 Yeah.
nacho 00:20:50 I mean….
Alolita Sharma 00:20:51 True. Go look at the axes.
Bryce Buchanan 00:20:54 Easy.
Alolita Sharma 00:20:54 issues on the sift. Depose first.
nacho 00:21:01 Yeah, I think that that user simply selected the wrong target architecture, and it didn't work because of that.
Yeah, this one is about the URL system instrumentation.
in, in an…
That method doesn't work for a synchronous network task. It doesn't return the data because we don't have access to it.
As you know, we cannot…
instrumental delegates, we can only instrument one of them, and we…
And we cannot… in that callback, we cannot provide the data that has come with the response.
Because we don't have access to it in the legit data can improve it.
Bryce Buchanan 00:21:46 Is the… the issue…
Okay, so you're on… there's a… there's a parameter called receiveResponse, it takes response… it seems like in my testing that doesn't… oh, okay, so, like, our… our callback for the configuration isn't working?
nacho 00:22:04 Yeah, it fails to return that data. Yeah. Because when it's in a synchronous network call that doesn't have a delivery, yes.
Bryce Buchanan 00:22:15 Yeah.
Could we add this to, like, a README in the…
Instrumentation, or the instrumentation, network instrumentation library.
nacho 00:22:28 Yeah, we could probably document that in the method, that it's not gonna work.
Bryce Buchanan 00:22:34 Okay.
nacho 00:22:35 I'll create… That parameter is gonna be always for asynchronous.
Bryce Buchanan 00:22:39 Yeah.
nacho 00:22:39 Network request, yeah.
Bryce Buchanan 00:24:02 Okay.
Hopefully that's enough information to… Go off of to add that.
…
Instrumentation, uses the same request twice, overwriting the context propagation as… this looks like I'm not sure why.
So, a recent… this is not related to the header issue.
But this….
nacho 00:24:32 Yay.
Bryce Buchanan 00:24:33 Yeah.
nacho 00:24:33 Yeah, it says that it's not related to the header, but that the network request is processed… is processed twice.
Yeah, so I have it… … Yeah, I explained that.
that…
it shows like a bug, but not sure why. So I asked him to put the call stack, so we could see how it gets there. Because we really have to
Recreate a new request, because there is no way to change the headers of an existing.
Bryce Buchanan 00:25:08 Right, right, right, yeah.
nacho 00:25:09 So we had to recreate the request with the headers?
We… so… I would have to do that before, … Before resume.
Bryce Buchanan 00:25:23 Yeah, right, right, right. So, the issue, but, ….
nacho 00:25:29 So it… but it looks like… like it's calling that process and log request twice.
But we don't know from where.
Bryce Buchanan 00:25:38 yeah, so I wonder, yeah, I wonder… so this is his example.
I… okay, yeah, I have this assigned to me, and I looked at it a little bit, and was able to… to… you know, …
reproduce it, but I haven't had a chance to, dig into it any further than that. But I can, I can look into this, in a… in a clean environment and try to figure out where that…
Like, where the duplication call is of that.
nacho 00:26:13 Yeah, I think it must be calling process and log request twice.
Yeah. From several… from different places in the code.
But don't know what, maybe….
Bryce Buchanan 00:26:37 Yeah, interesting.
I have it linked there, but I'm not seeing… oh, here it is.
So this is in… yeah, so, …
Yeah, maybe we just need to have…
A different header injection, …
Because we don't want to start a trace, we just want to inject headers, right?
nacho 00:27:09 But….
Bryce Buchanan 00:27:11 Yeah, so I'll take a look at that. I think that maybe we just overloaded that method.
And it shouldn't be starting a trace at that point, it just needs to create a new request.
Okie dokie.
Okay, and so now we're back at… okay, so those are all kind of the new ones. I received an issue, …
… at Elastic, related to…
the instrumentation, and there's a crash in there, but I haven't had a chance to… where did my screen go?
I haven't had a chance to really dig into it yet.
So, I'll… I'll keep you posted if I come up with anything out here.
There we go.
Alright, any other topics?
nacho 00:28:18 Yep, … Release 2.0.
Bryce Buchanan 00:28:21 Oh, yeah.
nacho 00:28:22 Final one. We still are in pre-release.
….
Bryce Buchanan 00:28:26 I thought that, I thought that we took care of that already while I was away.
nacho 00:28:31 Yeah, no, I mean, we had the doubt about the meta builder in 2.0.
Bryce Buchanan 00:28:38 Oh, right, right, right.
nacho 00:28:39 If that was… I mean, if that was an issue, it looked like something that had to be fixed before?
So, yeah, I think we, we should….
Bryce Buchanan 00:28:48 Can we just… Will we fix some things….
nacho 00:28:50 But… but we fixed some things from here, right?
Bryce Buchanan 00:28:53 Oh, did we?
nacho 00:28:55 I think we merged some.
A pair of issues, at least.
Bryce Buchanan 00:28:59 I mean.
nacho 00:28:59 I'm not sure.
Bryce Buchanan 00:29:00 I'm not sure if we can re-release Under 2.0.0 is a thing.
Maybe we can… I mean, like, I don't think it's possible to, like, update a tag.
to a later….
nacho 00:29:23 I mean, but then maybe we can remove it from the tax?
I don't know, because I, I'm…
I think that there were a pair of fixes.
That will be….
Bryce Buchanan 00:29:38 Here, let's take a look.
nacho 00:29:40 Oh, we have 999 comments, which is nice.
Bryce Buchanan 00:29:46 999 comments, or commits.
nacho 00:29:48 Yep.
Yes.
Pretty cool.
Yeah, almost… so, so, so release 2.0, if we recreate it, will be…
Commit 1,000, or something like that?
Bryce Buchanan 00:30:02 Oh, right, yeah.
nacho 00:30:03 So….
Bryce Buchanan 00:30:05 Not true.
Alolita Sharma 00:30:06 You, you should do the thousandth one.
Bryce Buchanan 00:30:09 Oh yeah, it's true.
Alolita Sharma 00:30:12 What happens if I just do that?
Bryce Buchanan 00:30:16 It probably won't work.
I'm just curious what it'll spit out in terms of the diff.
nacho 00:30:33 Yeah, we… we… from the… from the… there are several, there is a…
Prevent Cross during class swizzling, commit that happened after the… Please release?
also added the client protocol for customizable HTTP behavior.
And also another class for a amplified upload task.
Bryce Buchanan 00:31:00 Mmm, I wonder if that's what I'm running into in my… in my, … Project.
nacho 00:31:06 So, maybe we can… remove the tasks, or the… I don't know if that will work.
Bryce Buchanan 00:31:17 Maybe we need to remove.
nacho 00:31:20 the….
Bryce Buchanan 00:31:21 have, succeeded.
That's interesting.
nacho 00:31:36 Yeah, also….
Bryce Buchanan 00:31:37 I think if you….
nacho 00:31:40 Eiff.
I'm not sorry if SPM just also gets angry when you… Change that's happening.
Bryce Buchanan 00:31:46 Yeah.
nacho 00:31:47 Or you, delete one and keep the same?
That could also be a….
Bryce Buchanan 00:31:52 Let's do this.
Maybe we should just do a 2.0.1.
nacho 00:31:58 Okay, yeah, that makes sense, and make that….
Bryce Buchanan 00:32:01 That'll be a, it won't be a pre-release, it'll be the official release.
nacho 00:32:06 Okay, yeah, that, that works.
Bryce Buchanan 00:32:18 Cool. Alright, well, we'll get that going.
Alright, well… I think….
nacho 00:32:28 Yeah, Adi, you joined?
Oh, honey.
Bryce Buchanan 00:32:31 There you are.
Ariel Demarco 00:32:32 Hey guys, sorry, hot summer.
nacho 00:32:34 I don't know what we're….
Ariel Demarco 00:32:35 interruptions. We're just in the city.
nacho 00:32:39 Okay, yeah, just to know if you had any issue, any topic, anything you had… you wanted to add?
Ariel Demarco 00:32:45 No, I was going to talk about, like, the PR, Alex PR, and also mostly around, automation and the new repository, but…
I don't know if you've.
Alolita Sharma 00:32:58 Yeah, Ari, I also had the same question. Bryce, you'd mentioned,
Now that the new repo exists, you know, again, do we need to have, like, a…
list of, components related to GRPC that we want to move? What else? What else do we want to kind of… yeah….
Bryce Buchanan 00:33:18 How do we do that? Everything besides the OpenTelemetry Swift, or, I mean, the SDK and the API, but maybe we can keep some other components in there.
Alolita Sharma 00:33:29 Yeah.
Bryce Buchanan 00:33:29 That are….
Alolita Sharma 00:33:30 Typically, anything related to OTLP stays in core, you know.
Bryce Buchanan 00:33:35 Oh, no.
But that's the whole reason why we wanted to make a new repository, was because of how big OTL or the gRPC stuff is.
nacho 00:33:45 Yeah, the gRPC stuff is the one that really.
Alolita Sharma 00:33:49 Yes, inflates our packages. Well, yeah.
Bryce Buchanan 00:33:52 So….
Ariel Demarco 00:33:54 And also, that's why one of the things that maybe we discussed in the past week was maybe it's not the right name to call it country, because…
maybe it's not the same concept as in the other repositories or technologies, because in our case, it's mostly something regarding our limitations with SPM, and how the SPM works.
Alolita Sharma 00:34:16 Yeah.
Ariel Demarco 00:34:17 I… and I don't see, like, a change coming in the way it works, at least.
Alolita Sharma 00:34:22 Yeah, we, we located, Ari, the, the issue with on the Swift repos, which, you know, has flagged the SPM issues, but, and I was, I was mentioning to Bryce that we'll, we'll,
I'll try to follow up with the CoreSwift team to see if they have some ideas about where SPM is going, if they have some internal, you know, external documentation that they can share, right? So that'll at least give us some insight there. But I…
Again, I have a question here on the GRPC, you know, why, …
Component and… and the related, dependencies.
I guess we'd have to separate it into contribib, or is it something that we can say… …
is another folder. That still doesn't help us, right, in the core.
Ariel Demarco 00:35:23 No, the main problem… The main problem is SBM will….
Alolita Sharma 00:35:27 Yeah.
Include everything.
Ariel Demarco 00:35:30 will download the tree of dependencies before even selecting the actual product that you are going to use. So, imagine you just select OpenSeridometry API, which has no dependencies at all.
Alolita Sharma 00:35:40 Yeah.
Ariel Demarco 00:35:40 And you basically download 300MB of dependencies.
Alolita Sharma 00:35:44 Yeah, but I mean, the question is, is it contrib, right? Because again, the definition of contribib really is, integrations that are, being done with the SDK or the API, right? So…
It's… it's fundamentally all the components that are typically, maintained by other
you know, by vendor integrations or, other project integrations, say tomorrow you have FoundationDB, coming in as a, you know, integration into the API.
So, I mean, should we…
name this repo to be something different, is my question. Maybe SwiftGRPC, or something like that.
Ariel Demarco 00:36:35 I think one fair question Bryce had when we asked… we mentioned this is, is there any other technology doing something similar?
Like, we're having an intermediate repo that is not contributed, but is not the core.
Alolita Sharma 00:36:49 Yeah, you can have… I mean, again, for any of the libraries, you can have as many, repos as you need, right? So there's no restriction on having repos of named
named and representing different components. It's more that contrib typically has had that definition attached to it.
Where there are integrations which are being managed, and this is, again, more of a naming convention, not… nothing beyond that. For example, like, Collector has a builder.
repo, it has a operator repo, you know, there are all these different repos, HumCharts, so you can…
You know, even have something
Such as Swift GRPC kind of thing, right? Which is totally okay, because fundamentally, you know, how the packages are built is…
your call.
nacho 00:37:47 Yep. Okay.
Bryce Buchanan 00:37:49 Yes.
nacho 00:37:50 Yeah, on the other side.
Bryce Buchanan 00:37:51 I think that's more appropriate, is to create a separate GRPC repo.
Alolita Sharma 00:37:55 Yeah, yeah, yeah. Because, you know, it's very clearly then indicative of, the related, files and components that are in there.
And you could even, in the future, say HTTP is another, you know.
repo if you need to, right? I mean, it totally depends on how you build.
Bryce Buchanan 00:38:19 Yeah, the issue is, is it becomes kind of a nightmare maintaining all of these different repos.
Alolita Sharma 00:38:24 Absolutely. Agreed, agreed.
Bryce Buchanan 00:38:26 Yum.
Ariel Demarco 00:38:28 Yeah, I think that… it'll be…
good to have no dependent… non-dependent in the reboot, and other with dependencies, like the gRPC and all… all the ones that have plenty of other dependencies to be on the other one.
Alolita Sharma 00:38:44 Yeah.
Ariel Demarco 00:38:45 I have to say something.
Alolita Sharma 00:38:47 I mean, it's also, you know, thinking forward in terms of understanding, you know, what other …
mechanisms under the hood, whether those are protocols or, you know, any other components that we would like to trim down in the future. Because this is just a current issue, say.
magically, SPM actually fixes or upgrades its way of doing packaging, then, you know, how would you
How would you structure other parts also?
It's maintainability, as Bryce, you said. Yeah.
Bryce Buchanan 00:39:30 …
I, you know, perfect as the enemy of good, why don't we just continue with the original plan for now, see how that goes?
I don't know what to name the repo other than Contrib at this point.
But let's just put all of the additional components on top of the SDK into there for now, and then…
You know, maybe in the future we can try breaking it out further if necessary.
What do you… what do you think about that?
Alolita Sharma 00:40:06 Yeah, I mean, again, to Vinod's point, gRPC is typically never in Contrib, so, in hotel.
Bryce Buchanan 00:40:13 Okay. So maybe, should we just create a, … Yeah, so here's… ugh…
So, with this change, I mean, now we're looking at potentially 4 separate repos?
You know, so we'll have, like, the contrib repo.
for the instrumentation, we'll have a OTLP repo for the OTLP stuff, and then a separate GRPC one for the OTLP GRPC.
Alolita Sharma 00:40:42 Yeah.
nacho 00:40:43 We could keep the RTLP.
the non-GRPC part of OTLP in the main repo.
Alolita Sharma 00:40:49 Yeah, that's HTTP, right?
nacho 00:40:51 HTTP, yeah, we have that implemented ourselves. We don't have dependencies there, I think.
Bryce Buchanan 00:40:58 Yeah, I think that it's pretty….
nacho 00:41:00 bath.
Bryce Buchanan 00:41:00 Before we're in….
nacho 00:41:01 Guys that we must create.
Alolita Sharma 00:41:02 Yeah, the product must, ….
nacho 00:41:05 And also, they have definition for some of the objects, so maybe…
We could keep that in the… In the main repo?
Sure. That it might make it a bit easier to keep seeing, maybe? I don't know, at least for the definition of the types, I don't know.
Alolita Sharma 00:41:25 I have a question for you, though, that, you know, in the… in the long run, as you have run, as you have built the Swift releases, the library releases, and also the, …
the current, you know, labels that are there in the… in the build process, do you see more…
Sophistication coming in there, in terms of more additional types of, variations of packages that are done in the future?
say, you have different versions, for example, of, you know, different OSes, right, which are… Related to Swift.
Such as… and this has come up in some of the issues in the past, where, like, there is an iOS build versus an…
iPadOS build, OSS, you know, other, ….
nacho 00:42:25 Yeah, we have to explain that.
Yeah, sometimes some of the…
The dependencies have also limitations on the versions that we support, so we have had to keep some of them.
Alolita Sharma 00:42:39 So, would you….
nacho 00:42:40 Don't have releases.
Alolita Sharma 00:42:41 Have build variations?
Or would you like to have built variations? Again, you don't necessarily have to implement it right now, but it's more that, you know, are we thinking through all the different….
nacho 00:42:55 Yeah, it's true that SPM doesn't support having several versions of Swift or iOS. Right.
Bryce Buchanan 00:43:02 Yeah.
nacho 00:43:03 So yeah, that… having… Some of those in different repos can maybe.
Alolita Sharma 00:43:11 I mean, does it make your life easier, is my question, because then you're working with the current, you know….
nacho 00:43:17 that is more than one repo, makes things more complex. I understood.
Alolita Sharma 00:43:24 And maybe, does it make sense to, like, for example, what the collector has done, have a builder, for example?
Which is, you know, …
a more sophisticated toolchain for doing different types of, … again, the objective there was make your… build your own collector, kind of thing, right? So, being able to collect, or take a subset of, components and build your own package.
Kind of thing.
I mean, would… would we ever envision doing something like that for instrumentation or any other…
Variations of the library in the future.
Bryce Buchanan 00:44:06 I… I don't really know if that's possible.
with… SPM at this point.
Alolita Sharma 00:44:13 It's all or nothing, right?
Bryce Buchanan 00:44:14 Yeah, yeah, I mean, like, you can, you can… you can…
Define, like, what components you want to bring in to your project.
Alolita Sharma 00:44:24 Hmm.
Bryce Buchanan 00:44:24 But, you know, it still has the underlying problem of, you know, it just downloads the entire dependency chain regardless of
What you are actually using in your project.
So, yeah, no, no.
Alolita Sharma 00:44:39 I mean, I can… you can, … actually, Bryce, if you're sharing your screen, okay, if you can go back up to OpenTeleventry and look at the collector, just, you know, repos, you can see how…
If you just search on collector, and you will see that, there is a contribib, there's a collector, which is the collector core, right? All that has is all the dependencies only on…
the core OTLP spec, if you will, right? In terms of the basic support. And then you have collector releases, you have operator, then you have build tools. You also have a fork of the collector, which is
Arrow, which is written in Rust, you know, which is, again, an experimental version, but it really is for high performance.
So you can see that over time, you know, we started with only the core collector repo, but over time, it has kind of branched and advanced into
multiple… Things, right?
And contrib is massive in the collector, as you know, but … it's just that….
Bryce Buchanan 00:45:56 It's like….
Alolita Sharma 00:45:57 It's just way too many things. But, you know, you potentially could have exporters, Swift exporters, Swift receivers, you know, different components which are.
Vinod Vydier 00:46:09 I think it's best to compare it with another language, because….
Alolita Sharma 00:46:14 Yeah, we could look at Java, which is also relatively sophisticated.
Vinod Vydier 00:46:19 Neutral.
Alolita Sharma 00:46:19 … And if you go back to looking at Java, for example.
You can see that there is the, EBPF implementation, which is being done on the side.
It'll get merged into the primary, you know, implementation at some point, or built together. There are examples, there is the protobuf, that actually, I guess, Java bindings, that could be maybe similar to what we are doing with the gRPC.
….
Bryce Buchanan 00:46:52 Java bindings.
Alolita Sharma 00:46:54 this… this proto-Java.
Bryce Buchanan 00:46:56 Oh, the proto one, okay.
Alolita Sharma 00:46:57 Yeah.
And, so…
again, you can name whatever you need it to be, is my point. You don't have to necessarily name it contrib.
Bryce Buchanan 00:47:09 Okay.
Alolita Sharma 00:47:11 I mean, we can always go and request another repo, right, Bryce? Yeah. I've spent all week….
Bryce Buchanan 00:47:16 trying to get this, … I know, I'm sorry. I… I was under the impression this would be low overhead.
Alolita Sharma 00:47:27 And it is, I mean, you can just use it for whatever.
Bryce Buchanan 00:47:30 Oh, yeah.
Alolita Sharma 00:47:31 You know, you want them to be wet.
Yeah, Neera, we might hear back again that, that we are not, ….
Bryce Buchanan 00:47:44 we're not using good driven the way it should be. Yeah, okay.
….
Alolita Sharma 00:47:50 Random things like that.
Bryce Buchanan 00:47:52 Yeah, so, yeah, maybe what we can do… well, I don't know, ….
Ariel Demarco 00:47:59 I think that's.
Bryce Buchanan 00:47:59 There's no big offender is… Nope.
Ariel Demarco 00:48:02 No, I think that the first thing to define is what's going to be on the core one.
Alolita Sharma 00:48:08 Yes.
Ariel Demarco 00:48:09 Find what's going to be on the core one.
Then we can….
Alolita Sharma 00:48:12 Pick the right name. Yeah, yeah, exactly.
Bryce Buchanan 00:48:16 I was actually gonna say go the opposite route, because, like, what are we trying to do here? We're trying to solve this issue with…
….
Alolita Sharma 00:48:24 tendency sites.
Bryce Buchanan 00:48:25 dependencies, right? And the real culprit in terms of the size of the dependency chain, is gRPC. And so, should we just break out gRPC right now, and just call this OpenTelemetry Swift-GRPC? Yeah. Leave everything else in the main repo?
Alolita Sharma 00:48:43 Yeah, I would do that if, you know, that's the first step.
Bryce Buchanan 00:48:49 And then, you know, if that…
It works… maybe it's like an interim solution, and then eventually, when we get a little bit more confident, or whatever, feel like it's time, we can break things out into other repos.
Alolita Sharma 00:49:02 Yeah, and we can even do a build repo if that's useful, because what that does is then enables the packages to be built
with gRPC, without gRPC, you know, and that is easy to write, change if…
If you have different repos, right?
nacho 00:49:24 But if we do that with SPM, for example, that will automatically download everything from both repos, and all the dependencies, or the dependencies are
Yeah, so that's, that's one bill, right?
Alolita Sharma 00:49:37 I mean, naturally, that's one package, but another package could be only the core.
nacho 00:49:42 Sift.
Yeah, I mean, but if you want to build the others, you have to, yeah, include… if we create a project that includes them automatically.
It will download everything. Yes.
Bryce Buchanan 00:49:57 Yeah, even if it's in, like, the test chain.
Alolita Sharma 00:50:00 That's right. Yeah, yeah, and that's understood.
So….
nacho 00:50:03 So, yeah, we must provide a way for the users to include
the repositories themselves are not in their solution. We… we cannot include… how to include them.
Alolita Sharma 00:50:15 I mean, maybe what we can do is we can provide, build, you know, scripts, that is, the makefiles, and then people can run that themselves.
nacho 00:50:29 Yeah, that's something that we talked in the past, and we… there was even one contributor that wanted to create one for iOS.
And we asked him to update that to other platforms in order to add.
Alolita Sharma 00:50:43 Yeah.
nacho 00:50:43 And we, and he never connected again.
Alolita Sharma 00:50:48 I see. But we could… we could… if that's a project that we want to kind of encourage in the future, maybe we could have an issue and get one of these….
nacho 00:50:57 Something really useful for deploying OpenTelemetry Swift is using an XC framework, an intermediate XC framework.
that builds everything into a package, and you can distribute that with your app, or link with your app. So you don't have to keep all the code downloaded every time, and building every time gRPC, or Swift Neo, or even the SDK itself, because you can…
We cannot distribute that because we have many libraries, so you never know which is the package that will work for you.
Alolita Sharma 00:51:31 And that's, I think, where Natural, your idea of build your own kind of thing, then, you know, makes more sense.
nacho 00:51:39 Yeah, having a make file or having a script that built what they wanted will be… will be great, yeah.
Alolita Sharma 00:51:46 I mean, we can go after getting…
intern contributors or others to actually build that out, and then get other maintainers also to support it, even from Apple.
Bryce Buchanan 00:52:01 That'd be cool.
nacho 00:52:03 Yeah.
Alolita Sharma 00:52:04 So, I mean, maybe defining just an issue for that, and then having, you know, working on it once.
We have an engineer attached to it.
nacho 00:52:16 Yeah, not thinking about that, maybe.
Would it be possible to… distribute…
all the depend… all the libraries as XC frameworks, and link them into a…
another XC framework, so we distribute the binaries for the users.
Do you know if that's possible?
So instead of….
Ariel Demarco 00:52:40 make an XE framework out of XC frameworks.
nacho 00:52:44 You can.
Ariel Demarco 00:52:45 you got. You have to.
nacho 00:52:46 Okay.
Ariel Demarco 00:52:47 Like, ship all the XE frameworks all together.
Okay, yeah, then now possible. That said, if you have… let's say you have two, and that complicates things. Imagine that you have two SDKs using OpenTelemetry.
all of them.
nacho 00:53:03 Yep.
Ariel Demarco 00:53:04 their own version.
they will have conflicts in terms of the module generated. The module name will be exactly the same, so you have conflicts that are unsolvable from the SPM side.
Yeah, that's true. And I probably think that…
And I think that cocoa pots will also have the same problem.
nacho 00:53:22 Okay, yeah, then discard my mind.
Alolita Sharma 00:53:25 It really is.
Primitive, right, Ari? Because it seems like there's only one level of, … … You cannot have multi-level….
nacho 00:53:37 Yep.
Alolita Sharma 00:53:38 Dependencies.
Ariel Demarco 00:53:39 Exactly, yeah. You… you cannot do the… solve the different… the… the reverses.
Alolita Sharma 00:53:44 Have we… have we filed a issue on Swift for this? We should. I mean, because again, these are things that are, areas that should be part of any sophisticated package manager.
Ariel Demarco 00:54:00 It's… I think that the good idea would be to be able to type alias in some way.
Prior to do the linking, and when downloading, because this… this will crash on download, the dependencies.
Because it will recognize that two modules have the exact same name. Someone said… some problem similar happened to us with one module called data compression.
Alolita Sharma 00:54:25 Because it was being used in two different contexts.
Ariel Demarco 00:54:28 We basically had a target ourselves that was being exposed called data compression, and there was an SDK using a data compression library, but it's a dependency, a well-known dependency.
And there's no way to type Alessa.
on… That's maybe the good idea to… to have in…
In SVM, being able to type values, a dependency.
So, under the hood, when it's linked, it's linked with…
Even though it's the same binary, you have one of them with a Thai values, or something like that.
Alolita Sharma 00:55:10 Yeah, that would be something worthy of… Adding an issue to Swift.
SVM.
Well, brilliant.
Bryce Buchanan 00:55:19 Alright, so do we have a, a follow-up, like, action item to…
Like, do we want to open an issue?
Alolita Sharma 00:55:27 Upstream? Yeah, we should, for SPM, for sure.
Bryce Buchanan 00:55:30 We can draft one up, and then….
Alolita Sharma 00:55:33 Review it next time, and then we can file it.
Bryce Buchanan 00:55:36 … Let's see, okay, so….
Alolita Sharma 00:55:41 Ari, I can work with you on drafting up an issue, and then we can figure out, you know, we can review it next time, and then…
… violent….
nacho 00:55:52 Yeah, if Alolita pings it internally, maybe.
Alolita Sharma 00:55:55 Yeah, yeah, I will definitely do that. You'll be coming there. I will be coming there.
nacho 00:56:00 Sunday.
Alolita Sharma 00:56:00 one of their favorite people here. It's like, oh no, hotel is here again?
nacho 00:56:08 Yeah, I…
it was such a basic thing that I didn't price it… I mean, that I thought it will… yeah, it didn't come with version 1.0, but that will come with the next one. I mean, it's like…
Do you know? Something….
Bryce Buchanan 00:56:26 We all… we are all on the same page here. Yeah.
nacho 00:56:30 I can imagine many people opening the scene.
Alolita Sharma 00:56:32 Oh, absolutely. And I'm sure any third-party team is… has the same issue and concern.
Ariel Demarco 00:56:39 Yeah, I think that also what Alex proposes in chat, it would be also good, like, having multiple package definitions in the same repository, and being able to link that, because you could create a package that is compatible with iOS.
Alolita Sharma 00:56:54 Yep. 12.
Ariel Demarco 00:56:55 And one of them with the definition to iOS 15, and that one with IFC 15 uses different sources, different stuff, so….
Alolita Sharma 00:57:03 Yeah, and different dependencies, right? Because there can be different versions.
nacho 00:57:07 You can have… You can have different packets for the different compilers where it seems.
Yeah.
We've had that in the past with…
with OpenTremity, we had 3 different packages.
Ariel Demarco 00:57:23 Yeah.
nacho 00:57:23 Fine Nine.
Alolita Sharma 00:57:26 How did you maintain that, Naja? How did you, I mean….
nacho 00:57:29 We only maintain the latest one. I mean.
Alolita Sharma 00:57:31 I see.
nacho 00:57:32 I mean, just building, because it was… usually only the package had to be included in the proper way.
Alolita Sharma 00:57:39 I see.
nacho 00:57:39 I'm not including what?
Alolita Sharma 00:57:41 Even if you… so, let me ask you, even if you have explicit, definitions, it still doesn't work to have the same name for the dependencies? Like, if you were to string the entire, …
You know, which version, which, package, and… Everything in the same…
path. It still doesn't work for the dependency, resolution.
nacho 00:58:10 You can… you can change the version, but that's not tied to the name. I see.
Alolita Sharma 00:58:17 I see, I see, I see, got it.
nacho 00:58:18 So you can, yeah, and also having different packages, select, say, in the same repo.
Alolita Sharma 00:58:25 Yeah.
nacho 00:58:25 I… I think that's so inerrant to SPM that they…
identify a repository with a package itself that I don't think that will be easy, get… to get from, from SPM.
having different packages. I mean, it would be great if you can have the package for the exporter that is in a soup.
Alolita Sharma 00:58:50 Yes.
nacho 00:58:51 And you have all the libraries in different packages inside the folders, or the directories, it would be great, but…
I think all the security that Apple has, and all the resolution is based on having the root
Being at the root of the Git, itself.
But yeah, definitely that would be great, for this kind of projects, having all yeah, coming….
Alolita Sharma 00:59:18 We can, we can, we should ask, for sure.
To find out, you know, what….
nacho 00:59:23 Yeah.
Alolita Sharma 00:59:24 what can be done there? Because, again, I'm sure it is a common issue.
Ariel Demarco 00:59:31 One last question regarding the renaming and this new repo.
Emm…
there are other things that depends on other stuff. I don't know which one is the biggest. I really think that gRPC, it's a big repository, but I don't know, for example, the protobuf one.
there's a, I don't know, like this.
Alolita Sharma 00:59:54 I mean….
Ariel Demarco 00:59:54 change depends on Swift metrics, all of those, …
Do we know if they are actually big dependencies?
Bryce Buchanan 01:00:04 I… I don't….
nacho 01:00:05 Yeah, maybe….
Bryce Buchanan 01:00:06 I think so, but, I haven't really looked closely at it. We just know that the gRPC and the atomic stuff is what is really killing us.
Ariel Demarco 01:00:17 Yeah.
nacho 01:00:17 Yeah, that's true.
the truth is that as ERPC is so big, we don't know if it's hiding the dependencies on other libraries, so it could be true.
we can remove gRPC, and maybe we still download 80% of the dependencies of, gRPC, just because, yeah.
the Swift metrics.
Loads it.
Ariel Demarco 01:00:38 the algorithm.
nacho 01:00:40 Yeah.
Ariel Demarco 01:00:41 The log is downloading Swift log, the metric stream is downloading Swift Metrics, the Prometheus, I think, or some of the exporter.
Alolita Sharma 01:00:51 Very huge dependency chain, because, …
We kind of import all of Prometheus under the hood.
You know, so… ….
Ariel Demarco 01:01:02 In our case, the exporter is importing Swift NIO and NIO… yeah, NIO.
Alolita Sharma 01:01:10 Yeah.
Ariel Demarco 01:01:11 We can just take… we can just take a look at all these.
Oh.
Bryce Buchanan 01:01:15 So….
Alolita Sharma 01:01:17 And maybe next time, Bryce, we can actually go through each one of these.
Bryce Buchanan 01:01:22 Yeah, that's.
Ariel Demarco 01:01:23 So GRP Swift, we'll just take a look at that one. So this one is, I guess you can't see it, 33 megabytes there.
Bryce Buchanan 01:01:32 So that's… so that's the, …
like, I guess people are complaining total is, like, 100 megabytes.
Alolita Sharma 01:01:39 Yes.
Bryce Buchanan 01:01:40 So that's a third of it.
Oh, interesting, that's only 1.8 megabytes on the….
Alolita Sharma 01:01:47 Atomics.
Bryce Buchanan 01:01:48 on the atomics, and let's look at all the NEO….
Ariel Demarco 01:01:53 100 megabits.
Bryce Buchanan 01:01:54 Yeah, so, oh my gosh, yeah, Swift Neo is, 83 megabytes.
On its own.
And the next highest is the SSL, which is 24 megabytes, and then the HTTP2 is 13. Yeah, so it's all, like, I think that's all part of the gRPC one, right?
Alolita Sharma 01:02:18 Hmm.
Ariel Demarco 01:02:18 These are all depend… from GRPC.
Yeah, and at the same time, the Prometheus exporter uses that one.
Safe night out.
Bryce Buchanan 01:02:29 Oh, okay, so we might….
Alolita Sharma 01:02:31 But Prometheus you can add to contribib, right? Like, if you are providing a Prometheus exporter, Or, ….
Bryce Buchanan 01:02:38 Yep.
Alolita Sharma 01:02:39 Or a Jaeger, ….
nacho 01:02:41 Yeah, but it wasn't Prometheus Exporter… it was, mandatory for….
Alolita Sharma 01:02:46 Yes, it is, but, you know….
nacho 01:02:48 It can be in country, okay.
Alolita Sharma 01:02:50 Yes, it can be in Contrib because it's a, you know, again, an integration with another project.
Right? So that's why, the foundational promise that Core makes is OTLP, native OTLP support, right? So Prometheus, again, or Jaeger, can be in Kintrib.
nacho 01:03:14 Oh, nice.
Bryce Buchanan 01:03:16 Alright, so if we remove those things… Protobuff is pretty big, too.
that adds….
Ariel Demarco 01:03:23 Yeah, that's a Because it's… it's part of the OpenTelemetry….
Alolita Sharma 01:03:27 Protocol but export are common.
nacho 01:03:30 Yeah, that's part of the basic OTLP. Even for HTTP OTLP, we need….
Ariel Demarco 01:03:35 Yeah.
Bryce Buchanan 01:03:39 So what are we even doing here?
Alolita Sharma 01:03:42 Because, again, what are the interdependencies, as Ari pointed out?
I think we'll find out as we… as we change the builds, right? Yeah, we also….
nacho 01:03:59 We also talked last week about Swift Atomics that we are only currently in for 1.
Ariel Demarco 01:04:06 Yeah.
Yeah, I like… I like to see that change.
Bryce Buchanan 01:04:09 Atomics is actually really tiny, so it's not really a big….
nacho 01:04:13 Okay, yeah, but we are only using for one variable. Yeah.
Alolita Sharma 01:04:17 Maybe we can just start with gRPC and then….
nacho 01:04:21 Yeah, I think we should start with ERPC.
Alolita Sharma 01:04:25 Yeah, just with one.
nacho 01:04:26 Move that out, and just evaluate how it works.
Alolita Sharma 01:04:30 Yeah.
Bryce Buchanan 01:04:30 Damn.
Okay, alright. I'll con- I'll continue with that, process then.
Alex Cohen 01:04:37 Okay, sounds good.
Alolita Sharma 01:04:39 I did.
Alex Cohen 01:04:40 I just had one thing that I was thinking about, and I'm trying it out, and it seems to work. I don't know if you guys noticed what I wrote there, but what if we have an environment variable for core only, or all the extra stuff?
And for people that actually want all the extra stuff for now, they can just set it.
Whether that load up their product, or the other way around.
That would basically do the same thing. I'm not exactly sure how you set the environment variable from the outside without just passing it to Xcode, but could definitely be in build commands or whatever.
But that would sort of fix the problem for… at least… at least for Embrace, for now, for sure.
Bryce Buchanan 01:05:27 Yeah, that's actually a really good idea, yeah.
Ariel Demarco 01:05:31 That's an interesting idea, yeah.
Alolita Sharma 01:05:32 Definitely worth trying.
Alex Cohen 01:05:34 Yeah, well, I'm trying it now, I know, I know it works.
Bryce Buchanan 01:05:37 Yeah, we have some environment variables for other components as well.
Alex Cohen 01:05:43 Like, ….
Bryce Buchanan 01:05:45 The, SwiftLint stuff is under an environment variable.
Ariel Demarco 01:05:50 Yeah.
Alolita Sharma 01:05:51 Hmm.
Ariel Demarco 01:05:53 The plugin is only added wherever you pass that in.
Alolita Sharma 01:05:58 Alex, would that mean we don't have to separate out the code?
Alex Cohen 01:06:02 It would mean… I think so. Like, it would… it would mean we could keep everything as is, and the package would be… would be created based on… on whatever the… whatever the user wants.
So… and most people, I… like, I don't know how people use the package, really, that much. I just know that,
Well, I don't know. I don't know if we would get environmental, and that's something that we definitely need help with. It sounds like we've done it before.
Bryce Buchanan 01:06:32 you have to either do it through, the kind line when you launch the project or launch Xcode,
there might be a way to inject it through the Xcode…
interface? I'm not sure, so we may need to explore that.
Alex Cohen 01:06:51 I wonder if the… The environment variables in the… in the… in the schemes.
To… would… would have an effect on… on that.
nacho 01:07:01 I think it's worth trying, I'm not sure. Yeah, there is a….
Bryce Buchanan 01:07:04 Chris or not.
nacho 01:07:05 in Xcode to read the system environment by ourselves.
Bryce Buchanan 01:07:09 I think.
nacho 01:07:10 And you have to manually go and change that in the second cycle.
Bryce Buchanan 01:07:14 I think the problem that I ran in with, ran into with using this for the SwiftLint stuff was it wouldn't… like, like, the package, like, analysis occurs when, like, the project is launched.
in Xcode, and so you can't apply… like, the environment variables that you add to the project while it's open don't get applied to… and it doesn't, like, refresh the.
Alolita Sharma 01:07:42 It's not runtime.
Bryce Buchanan 01:07:44 Yeah.
Alolita Sharma 01:07:44 innate thing.
Bryce Buchanan 01:07:45 We've got launch time, so….
Alolita Sharma 01:07:46 Yeah, yeah, it's.
Bryce Buchanan 01:07:47 Maybe we can play around with it a little more, Alex, if you want to look into that, but I recall that it really… the only way I could get it to work was if I, like, you know, through a command line, you know, said export my variable true and launch Xcode with the project.
So, I'm not sure if…
Like, maybe, maybe we can do it the reverse way, where the environment variables, turn it off.
Ariel Demarco 01:08:17 table.
Bryce Buchanan 01:08:18 We'll disable it.
Alex Cohen 01:08:20 Yeah, that's… I actually… well, what do you mean, disable it? Because the way I was testing, I first started trying it out by being like, I want the core only. Yeah.
But then, after that, I tried basically having an environment variable that said we want everything. So, if you don't specify you want everything, you only get the core. And then if you do spec… if you do pass some environment variable, then you get
everything else.
Bryce Buchanan 01:08:47 Yeah, so what I was thinking is if we do it the other way around, where everything is available, initial, like, by default.
And, … the hoops are for the people who…
need it pared down for their special case. Whereas, like, the majority of people want to use it, like, just normal, pulls everything down, running it locally, I don't have a big CI thing, I'm just fiddling around with it.
Alex Cohen 01:09:14 Yeah. So… I guess my question is, well, two things. First of all.
if you… if you have a dependency, if you're working on an app and you have a dependency on OpenTelemetry, if you set the environment variable in your package, does it trickle down to the packages that are… that are loaded as dependencies? Which means that that would be easy for anyone that doesn't want it. You just put it in your package, or your package file, and say, I'm setting this environment variable.
So.
Bryce Buchanan 01:09:44 Can you… can you do that? Can you set….
Alex Cohen 01:09:46 Oh, I don't know, but I'm gonna try it.
Bryce Buchanan 01:09:48 I think that that is not part… like, you cannot set environmental variables, in the package itself, like, in the… in the Swift package. You can…
depend on them in the SWIFT package,
Alolita Sharma 01:10:04 Yeah, but you shouldn't… agreed, agreed. I don't think you….
Alex Cohen 01:10:07 I wonder, then, if you can pass…
something… pass a variable to a package when you depend on it. Like, … Or pass.
Bryce Buchanan 01:10:20 Yeah, yeah, if you can set an invar in the package itself, that would be interesting. That could solve the problem. Like, if we can provide, like, add this to your package for the dependencies….
…
I think that would be great. But, yeah, the way that I have it set up for the SwiftLint stuff is the only way I could get it to actually enable is if I pass it… if I open the project in the command line with the environmental variable set in the command line environment.
I'll try a couple of things out and see if it works, because this would simplify things, like, so much. Yeah, that would be…
Yes, for sure.
problems, it sounds like. It didn't work properly.
Alolita Sharma 01:10:57 If it works, actually.
nacho 01:11:00 That's true. If that works, it will be great. We should think also on the beginners, who just
Doesn't have experience or don't know anything, so…
it should, if possible, make that work with everything by default. A bit like Bryce said, and just limit what things you want to remove, and probably
what you really need is that the CI doesn't do that, and in the CI, you have a command line interface, so.
Bryce Buchanan 01:11:28 Yeah, it's more….
Alex Cohen 01:11:29 We're in two cultures like today.
Bryce Buchanan 01:11:31 Yeah.
nacho 01:11:31 More easy, yeah, to add an environment variable there and make things just don't build or don't.
Bryce Buchanan 01:11:37 on the road.
nacho 01:11:38 Or don't exist themselves.
Alex Cohen 01:11:41 I'm gonna give that a try, this is very exciting.
nacho 01:11:43 Yeah, that's a really great idea.
Alolita Sharma 01:11:45 find a hack for it. Yeah, good thinking, Alex. We'll see how far it can go down.
Alex Cohen 01:11:52 Yeah.
Bryce Buchanan 01:11:55 Cool.
Alolita Sharma 01:11:55 Alright, we'll regroup. Thank you again, Bryce.
Bryce Buchanan 01:11:58 That'.
Alolita Sharma 01:11:58 Are we helping you on Slack. All right, thank you.
Bryce Buchanan 01:12:03 Have a good weekend, everybody.
Ariel Demarco 01:12:04 Take care. Bye-bye.
Vinod Vydier 01:12:05 Can we get Mike.

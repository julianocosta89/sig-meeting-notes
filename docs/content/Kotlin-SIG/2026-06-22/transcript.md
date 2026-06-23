SIG: Kotlin SIG
Date: 2026-06-22
Duration: 24 minutes
============================================================

## Zoom Recording Transcript

**Leonid Stashevskii** 00:39 Egg.
**Jason Plumb** 04:16 Hello, hello.
**Leonid Stashevskii** 04:21 Dame!
**Jason Plumb** 04:24 Nice to see you, Leonid.
**Leonid Stashevskii** 04:26 Yeah, nice to see you again.
How are you? How are you? How are you? How are you in two weeks?
**Jason Plumb** 04:36 Sorry, say again?
**Leonid Stashevskii** 04:37 How are you? How was two weeks?
**Jason Plumb** 04:40 It was alright, spread pretty thin. I don't know… But there was a ton of progress made on… the Kotlin project, but we will take a look here today.
**Leonid Stashevskii** 04:59 Nice. Nice. It's good to hear.
**Jason Plumb** 05:04 The agenda is pretty light. Hanson, I have a question for you. Do you know when Jamie is coming back?
**Hanson Ho** 05:10 Middle of July, so probably, actually, in, like, 2-3 weeks.
**Jason Plumb** 05:16 Okay.
Cool, that's good info. I'm gonna… I'm gonna miss next week, so, Hanson, I think you offered to run it.
**Hanson Ho** 05:25 Yep, I thought you were missing this week, so… but good.
**Jason Plumb** 05:28 Well, you know, I should be, but I'm definitely missing next week.
**Hanson Ho** 05:33 Got it.
**Jason Plumb** 05:42 Alright, feel free to add agenda items, add yourself to the itinerary, or to the agenda, and then, I will take a look at some PRs, and we can talk about them, since there's no other agenda yet.
Honestly, I'm going on vacation for a week, so I'm basically checked out at this point, but I'm here to help facilitate what I can.
Jas, if I'm using that abbreviation correctly or shortening, have you joined us before?
**Jaskeerat Sethi** 06:13 Hey, no, I have not. I'm just…
**Jason Plumb** 06:18 Thanks for joining, yeah. Have you checked out the… have you cloned the repo? Have you checked out the project?
**Jaskeerat Sethi** 06:22 Yeah, I get… yeah, basically, we're actually… so I'm from Amazon Music, I work there. We effectively built… hotel Kotlin internally, not completely, obviously. But it's just, we needed to launch something, and we needed to be in Kotlin, so we kinda… did a lot of the work already, and I wanted to just contribute back upstream, so I…
**Jason Plumb** 06:51 Yeah, yeah.
**Jaskeerat Sethi** 06:52 I was just waiting for, like, our OSS approval internally, like, legal approval.
So, I'm here… I'm here now. My plan Start looking at, like.
just really touch base here to understand where you guys are at, see how I could be most effective, and really, I was just gonna start knocking off some… PRs.
**Jason Plumb** 07:14 Killer.
**Hanson Ho** 07:15 That's grace.
**Jason Plumb** 07:16 Yeah, yeah, and we can always use help on reviews, like, that's the biggest thing right now, just because we're down on maintainer for a few more weeks, and everyone's pretty busy, so any additional reviews or clicking on PRs is, like… pretty helpful. But yeah, so kind of the state of things is that Embrace, like, donated the bulk of what exists today, and has been just absolutely instrumental in driving this project forward and contributing. We are currently working on API stability, and that means getting the API surface kind of dialed into how we like it before we focus too much on building the backend implementations of the SDK. But a lot of that has already happened in parallel, but we're kind of going piecemeal through the API and making sure that various areas Are to our liking, and that we won't expect them to change once we declare them stable, at least not for a while.
Yeah. And so that's a lot of what the discussion in this group has been about, is, like, what areas we go after, and where the gaps to the spec might be. So a lot of comparing it to Java, because that's a well-established, you know, API surface, but, like, making sure that we're paying attention to try and drive stuff.
to be more, Kotlin idiomatic, and not fall back into the same trappings of Java. So that's kind of… That's kind of where we're at.
**Jaskeerat Sethi** 08:38 Okay, I can… yeah, I'll sift through to see what open PRs there are for APIs, and then I can actually just… I think maybe what I'll do is… Spend, some time this week familiarizing myself with what you guys have already implemented.
And, open some discussions if I'm like, hey… if I have some questions or something, I'll maybe manage the Kotlin channel.
**Jason Plumb** 09:05 Nice.
**Hanson Ho** 09:06 Yeah, perfect.
There was a book…
**Jason Plumb** 09:08 A bunch of stuff that landed last week. Go ahead, Hanson.
**Hanson Ho** 09:10 Oh, I was saying, most of the API, so, so, things are done, but, we wanted… right now, the stabilization API is more… like, getting consensus with the hotel folks about what the API surface, ought to be, you know, shapes, and so the nitty-gritty of discussions of, like, you know, not functionality, but, like, how the functionality is exposed, things like that.
In terms of the implementation, the tracing and logging is, you know, fairly good and well used… well, fairly good, and comprehensive, with, you know, some, you know, I think, missing parts. The biggest part that we, haven't really explored very much on is the metrics, because our use case mostly is mobile and Android, and hotel metrics as they are right now isn't, you know, super suited, for that purpose. So, I don't know what your use case is. Are you primarily using it on mobile, or using it on, like, a KMP app, or, or backend?
**Jaskeerat Sethi** 10:12 It's, it's mobile, yeah. We have a, like, a common KMP… library that sort of builds into both iOS and Android.
So that's kind of why we built it.
**Jason Plumb** 10:30 And do you do both Android and iOS?
**Jaskeerat Sethi** 10:33 Android and iOS, yeah. We're, like, about, I would say… 2 months?
Less than 2 months from production launch from our end.
we have, yeah, like, our focus actually has been tracing and metrics. I'd be curious to hear what about the metrics doesn't… drive with mobile?
**Hanson Ho** 11:00 Mostly, mostly it's cardinality, and, and the fact that, we can't really distinguish, you know, readings, from different mobile devices, just because of the cardinality issue with the collector. So, hotel collectors don't handle high cardinality.
Well, and so if we want to put anything in the resource, that identifies, like, a device, or a session, or anything that, you know, goes above your typical, you know, low cardinality dimensions, things just get bad. And, you know, certainly we could strip those things from the resource, but then we basically get data that cannot be pinned back, not only to the, specific session, but, you're like, oh, P50, network requests, 6.5, cool.
What do you do with that? So you can do some…
**Jason Plumb** 11:56 I'm gonna limit the time on this discussion, because we've had this discussion so many times, and I think there is some writing now on the website, but if you're interested in metrics on mobile, I would encourage you to join either the Android SIG or the client-side SIG.
where this discussion is still discussed at length, but let's be clear, for this Kotlin implementation, we will absolutely have metrics as a first-class API, because there will be back-end users, there will be other use cases where it's…
**Jaskeerat Sethi** 12:25 with me.
**Jason Plumb** 12:26 It's just, historically, it's just been, like, less of a priority for this group.
**Jaskeerat Sethi** 12:30 Got it.
**Jason Plumb** 12:31 them over, yeah.
**Jaskeerat Sethi** 12:32 Well, I can start taking a look at that, and I'll look through the other channels to see what the discussion has been.
**Hanson Ho** 12:39 That would be great. Metrics is one area that's a bit light.
Also coverage on, non-Android platforms. Like, there are tests and things theoretically work, but I don't think there's anything in production, at all that uses, you know, the iOS and web, bindings. So, if, if you have something like that, it would be good to just, you know, see what holes there are.
**Jaskeerat Sethi** 13:03 Sounds good.
**Jason Plumb** 13:04 You know, I pulled this up earlier, because we've talked about this quite a bit in recent times. You know, there's these kind of component areas of the API, and they're not published as a separate module. We want to publish that as one.
coherent API, and so there's no way to mark individual ones, kind of stable or ready for production, outside of this matrix. And then, once we've got this stable, we'll declare the API stable, is basically what that looks like. And then if you're looking for stuff to work on, kind of the main areas right now… are attributes, resources, logging, and tracing. Those are, like, the first four. In fact, Does Tracy even have… It's weird that we don't have a milestone for a trade.
**Hanson Ho** 13:50 Do you want to scroll down one, I think.
**Jason Plumb** 13:52 Oh, there's a scroll… Okay, that's cool. Well, I could've just put that on screen. I had plenty of real estate. That's fine.
9 o'clock in the morning, very much awake. Anyway, you can see that there's also nothing left in… I need a tickle this.
There we go.
So they're… Oh, gross, what?
Feel like this. Yes, no.
Let's start over, shall we, from the top.
Okay, so here's what's left in the milestone that we think needs to happen before tracing is considered stable.
Before we stop changing it, and then the other ones that we're very close on, we think attributes, is probably… Probably ready to go.
And we just have to kind of do that work, and I think we want to do it before the next release, we haven't done a release in a little while, we're probably due for one, but I'm not gonna do it until I come back.
**Jaskeerat Sethi** 14:55 Okay.
**Jason Plumb** 14:56 And even then, it's gonna be a cramped week, but we, you know, we're due for one. We were… we have been trying to do, like, a two-week release cadence, but right now, it's just… I think it's… for me, as the only maintainer right now, it's two… it's two… two bananas. But we should get one out. And maybe we can… maybe we can include… This, and then have attributes as, like, a… a milestone.
In that… in that next release.
Alright.
So, without much more being added to the agenda, I'm just gonna pick through the more recent issues, and I will also… actually, before I even do that, Leonid has generously offered to, like, lend… some assistance from the Kotlin JetBrains side of things, which is really appreciated, and I think that we just don't have a good, like, concrete, hey.
Kotlin folks, like, Kotlin language folks, this is where we really could need your help. I don't think we have a nice bulleted list of that, so if anyone on the call thinks of things.
Let's please add them to the agenda, just, like, write them down. I will say right now, Hanson and I chatted a little bit about this, and the biggest thing that I think we could benefit from is just some additional eyes verifying that there aren't more naturally Kotlin-y ways of doing things, right? So I know that, like, at least for me, and probably for everyone else, we do fall back to our Java trappings, like, from time to time, and so having language expertise to, like, make sure that we're aligned with what the language direction is… the current state of the language and where it's going is the biggest thing that I can think of, but I know that's also vague, so I appreciate that, that you're offering to help, and I wish I had more concrete, specific things that I could ask for, but yeah, guidance around language use would be great.
**Hanson Ho** 16:51 Projects.
**Leonid Stashevskii** 16:51 Yeah, in terms of this stuff, let me know. We have experts in the API design and the library, the surface design.
I can bring them to the table.
So, let me know, you can tag me by emailing the document, and assign, for instance, we need this kind of API to be reviewed, and I will bring the expert on this from JetBrains, and we'll take a look at this.
**Hanson Ho** 17:20 Yep.
Project structure, I think, as well. I think… I think recently you guys announced a new structure of KMP projects, and I'm pretty sure… I know we're not, you know, you know, using that, because this has been in there for several months. So I think… I think the basics, like, is this good Kotlin, and KMP is… is the main answer, the main question I want to answer.
**Leonid Stashevskii** 17:41 Yup, good, definitely, no problem.
**Jason Plumb** 17:44 Cool.
**Hanson Ho** 17:44 Thanks.
**Jason Plumb** 17:48 Well, as far as new issues go, I think that there are not a ton of them. I… did this… so, Hanson, I saw this come up, like, last week, and then I… Oh, it did land, so it looks like… Was there more… was there more than just doing this?
**Hanson Ho** 18:04 I think the OpenTellencia picks it from here. So, I would… I would look at the… I would get this merge, have it released, and see if anywhere else it shows up, or anywhere else it doesn't show up, and then we could fix it. But I'm hoping this is it.
**Jason Plumb** 18:21 Okay, and where… when you say where it shows up, you mean, like, over, on the main… Like, in here somewhere?
**Hanson Ho** 18:28 Yeah, if you, if you, if you look for, like, that specific attribute, like, yeah, telemetry.attribute.language.
**Jason Plumb** 18:37 Oh, look at that. Yeah. Okay.
**Hanson Ho** 18:39 Oh.
**Jason Plumb** 18:41 Is this not the same thing?
**Hanson Ho** 18:42 No, this is not the same thing. I think this is… this is… this is different. I think it, under semantic conventions, there's a place where, it basically points to all the semantic conventions, and I want to say it takes in the release of the, of the semantic conventions and builds a website, like a web page, that's…
**Jason Plumb** 19:00 Like, in here?
**Hanson Ho** 19:01 Yeah, yeah, yeah, yeah, perfect, yeah.
**Jason Plumb** 19:04 And components?
**Hanson Ho** 19:06 I don't remember, it's… it's… If you do search for that actual literal, televentry.sdk.language, I think it'll show up.
**Jason Plumb** 19:17 I remember seeing some table… Oh, is it this one?
**Hanson Ho** 19:24 Nope.
**Jason Plumb** 19:26 Right.
**Hanson Ho** 19:27 I'll find it, I'll find it.
**Jason Plumb** 19:28 Okay.
**Hanson Ho** 19:29 on one of my 12 tabs, or…
**Jason Plumb** 19:31 I bet you it's one… I bet you this is also generated from that table.
**Hanson Ho** 19:34 That would be nice! I don't think it's released yet, but okay, cool.
**Jason Plumb** 19:41 Yeah, because this is all development, and then, you know, API stuff that we're not even listed in here.
Oh wait, there it was.
**Hanson Ho** 19:50 Yeah, I think this is the stuff that Jamie added a while ago.
**Jason Plumb** 19:54 Yeah.
**Hanson Ho** 19:55 Yeah, resource, yeah, there you go.
**Jason Plumb** 19:57 Okay.
That's right. Oh, now… now I'm remembering. Okay, so it was one of the valid values of.
**Hanson Ho** 20:02 Yes.
**Jason Plumb** 20:03 this.
Which is now… Probably hasn't been released yet.
**Hanson Ho** 20:09 No, yeah.
**Jason Plumb** 20:09 Caught up with what you were saying, like, 3 minutes ago, sorry.
Yeah, so nothing really new on issues. There are some pull requests that I have not yet seen, and that need to be reviewed.
Frankly, I'm not gonna touch any of this today. As soon as I get off this call, I'm closing my laptop.
**Hanson Ho** 20:30 Thanks for dialing in for this.
**Francisco Prieto** 20:33 I think I.
review today, so I hope to… Excellent.
**Jason Plumb** 20:37 Cool.
**Francisco Prieto** 20:38 Something like that.
**Jason Plumb** 20:38 Yeah, that'd be great.
**Hanson Ho** 20:39 Do it in the house.
**Francisco Prieto** 20:40 nutrition.
**Hanson Ho** 20:41 breaks.
**Francisco Prieto** 20:43 My god.
About the renovate VRs, we have a better… suit of tests that… what I expected, thanks to Shami. Okay. He actually added some minimum version tests, last month, so… I think, I will have a look and see what's failing, and close the ones that are failing, and maybe create a PR with the ones that are safe to bump.
**Hanson Ho** 21:15 Perfect. We, we should definitely close… we can't do min version AP, AGP9, that's… Oh, no, yeah.
**Francisco Prieto** 21:23 But the good thing is that Tesla are failing, so…
**Jason Plumb** 21:27 Yeah, exactly.
**Hanson Ho** 21:35 Maybe by the next World Cup we can do that, but… Not now.
**Jason Plumb** 21:39 It looks like this… oh, this is a minor, probably.
**Hanson Ho** 21:42 Yeah, and this should be fine.
**Jason Plumb** 21:44 Yeah. So, like, I… I… okay, I will spend a few minutes going through, just some of the renovate PRs, because I won't.
**Francisco Prieto** 21:52 So, if you wanted to go ahead and merge whatever it passes, then that's pretty much it.
**Jason Plumb** 21:57 Okay.
But yeah, apologies in advance for this backing up even more while I'm out for the next week, but don't let that discourage, you know, submitting PRs and reviewing them.
**Hanson Ho** 22:07 I should… yeah, I got sidetracked again, but, you know…
**Jason Plumb** 22:13 Cool, yeah, there's a lot of good stuff, but I think also, you know.
We had a bunch get merged last week.
Like, it's not… it hasn't been super slow. There's… there has been a bunch of stuff that's gone in that wasn't, I'll just renovate, so… Making progress.
**Hanson Ho** 22:28 Yeah, I think there's a lot of contributions. It's actually a good thing that we're not keeping up. Well, it's a bad thing we're not keeping up with it, but it's a good problem to have, so…
**Jason Plumb** 22:38 I think it's still manageable, I don't think it's that… yeah, yes, but… Ask me again in a week.
Okay, is there anything else specifically that people want to look at or talk about? I think… I… I don't have anything right now.
**Hanson Ho** 23:05 we can call early if, if we don't have anything. I think last week has been… I only made progress on a few reviews and stuff, so it… there isn't a ton. And… Yeah.
David, you were gonna look at, something that I'm seeing a PR for that's not under your name, so… Wonder what's going on here.
the B3.
Anyway, I'll take a look at the reuse, and I'll find out.
**Jason Plumb** 23:44 Okay, cool.
Well, I think we can probably stop with that, and… Yep.
Right, we'll save everyone.
**Leonid Stashevskii** 23:53 Thanks, folks.
**Jason Plumb** 23:54 I won't see you next week, I'll see you in two weeks, technically, but I'll see some of you in Android a week from tomorrow.
**Hanson Ho** 23:59 Thanks for that, I'll tag you in the doc, once I find it.
**Leonid Stashevskii** 24:03 We'll spring in two weeks.
If you need any help, just mention, and I will bring you folks.
**Hanson Ho** 24:10 Excellent, thank you.
**Francisco Prieto** 24:11 Thanks.
**Leonid Stashevskii** 24:13 Right.
Damn.

SIG: .NET SIG
Date: 2026-06-30
Duration: 26 minutes
============================================================

## Zoom Recording Transcript

**Alan West** 02:29 Hey, Martin.
**Martin Costello** 02:31 Hey, how's it going?
**Alan West** 02:33 Not too shabby.
How's things with you?
**Martin Costello** 02:38 Not bad. I'm glad the hot weather's… Temporarily gone away.
It's been far too hot here recently.
**Alan West** 02:49 Oh.
**Martin Costello** 02:50 The spread of cold weather.
**Alan West** 02:53 Yeah, I've read about that.
I've read about that. I've heard that… well, I've heard that people are dying. I mean, it's bad.
**Martin Costello** 03:01 I think in the UK, the dyeing is more… You know, increased mortality than… you know, like… specific… It's killing people, kinds of things, but yeah, it has not been fun.
**Alan West** 03:18 I mean, yeah, it definitely affects people that are older, you know.
**Martin Costello** 03:22 Yeah.
**Alan West** 03:23 And… Otherwise, stuck in there.
Stuck in their apartments, or can't move, or whatever.
**Martin Costello** 03:32 Yeah, there's been a… there's been a lot of stuff in the local news… national news here, about people living in, like, new apartment buildings built in, like, the last 10 years that are all glass.
And they're basically just in, air-conditioned greenhouses.
**Alan West** 03:50 That's nuts. That's nuts.
Yeah, bad planning.
**Martin Costello** 03:58 Yeah.
**Alan West** 03:59 lease.
Yeah, and I also, I guess I heard that AC is just not very common?
**Martin Costello** 04:08 No. We have an air conditioner unit, but it's one we bought about 4 years ago that's, you know, it's about 3 feet tall.
On wheels, sort of thing, and you just have to put a big, tube out of the window, and it tries its best.
**Alan West** 04:29 Yeah, I've had one of those before. They're kind of heavy, but I would move it around our house, depending on what room we were in.
**Martin Costello** 04:39 Oh, yeah, we don't do that. It's, We live in a three-story house, so… we just… it just lives in the bedroom.
**Alan West** 04:50 Gotcha, yeah, yeah, yeah.
So, you're working in the bedroom, if that makes sense.
**Martin Costello** 04:58 I go up there sometimes, but, it's… it's sort of a, like, put up with it during the day, and then at night.
it's sleepable.
**Alan West** 05:07 Yeah, yeah, yeah.
**Martin Costello** 05:12 Yeah, none of that.
**Alan West** 05:13 Let me get it going?
**Martin Costello** 05:15 No, it's okay. I was, I was doing the, the customary, how's the weather been on your end? But.
**Alan West** 05:22 The weather has been cold. I mean, not cold, it's cold, but, like, it's definitely chillier than normal.
and it… we had some torrential rain, which we very rarely get here.
At least where I am.
On the West Coast.
So that was interesting. We got that a couple days ago.
So, yeah, weird weather all around, but… I guess.
For us, not uncomfortable, because we can just, you know…
**Martin Costello** 05:55 Yeah, at least that's one thing about the UK. 99% of the time, if there's a lot of rain, we're prepared for that.
**Alan West** 06:03 Huh,
**Martin Costello** 06:06 It's the heat we can't deal with.
**Alan West** 06:10 I hear ya.
**Martin Costello** 06:14 So, the only item I've got for the agenda is… There was a bunch of… there's been a few bug fixes in recently, but also there's now also been some new public APIs that have gone in related to Prometheus stuff, plus I've got some PRs open today, unrelated to Prometheus that also had public APIs, so I was just wondering what the critical mass of pending changes.
Should be before we think about doing another minor version.
**Alan West** 06:53 I'm always a fan of releasing, you know, more regularly, so I… I don't… I've never been of the opinion that there's, like, a particular critical mass of, you know, items.
I mean, not too frequently, but, you know.
**Martin Costello** 07:08 Yeah.
**Alan West** 07:10 Once a month, I don't think, is a bad… a bad… a bad cadence, you know, if we were to ever hit that.
**Martin Costello** 07:17 Where did we do that?
forgotten.
Three weeks ago, so…
**Alan West** 07:23 Three weeks ago. So, you know.
Coming up on… A month.
But yeah, new public API, I guess, you know.
As you know, I've kind of been a little bit… Not paying attention, so… I guess… Normally, when there's new public API, we… take a pause and just kind of look over them. I don't think I'd be… the Prometheus stuff is, not… it's still, like, in beta or whatever, not, like, stable, right? Yeah.
So that…
**Martin Costello** 08:00 There is a… there is a P… there is a PR I opened today that is not Prometheus-specific, though, but I opened that, like, after I'd written this item, so… There's a… I found… I was going through the backlog, looking at old issues to see if there was stuff to pick up, and there was one about schema URLs for resource attributes.
And that… public API to make that work.
But, other than that, yeah, I think everything I've added is Prometheus-specific, so it would still be under the, the unstable tag.
**Alan West** 08:38 Yeah.
So, yeah, with respect to, like, any kind of a thorough public API review, I wouldn't be too concerned about the Prometheus stuff. I mean, we'll probably want to do that as you get close to wanting to declare it stable, just kind of, like, as a last sanity check, but… So the schema URL one that you're talking about, that's a currently open PR?
**Martin Costello** 09:06 Yeah, that's the… I think it's the most recent at OpenPR, it's 7472?
Let me share my screen.
That's what we have.
**Alan West** 09:16 Oh yeah, sure, let me hear you.
And you'd like to get that into… if we're gonna do another release, you're… you're in.
**Martin Costello** 09:23 Yeah, I figured it would make sense to sort of get as many things in Before doing a release, rather than just putting one and then going, oh, can we have an 18 the week after?
**Alan West** 09:35 So…
**Martin Costello** 09:35 So, for the schema URL stuff.
Where's the public API? Yeah, so… There's, a few changes on, resource and the resource builder.
Just to get it so that people can actually configure it.
So it's not, it's not a major addition, but it is in the SDK.
Compared to…
**Alan West** 10:01 Look, I'.
**Martin Costello** 10:01 Here's stuff that's all separate.
**Alan West** 10:04 I forget, did that schema URL get added to, like, the activity API and the metrics API? Yes. It did, okay.
**Martin Costello** 10:13 So that's in the runtime now, since 10.
But this one is independent of the runtime, so I think it sort of… slightly fell in the cracks when I was doing the .NET 10 work.
And so I just sort of came back round to the issue today, and I was like, oh, I should probably pick that up and fill the cap in.
**Alan West** 10:35 Okay, yeah, makes sense.
**Martin Costello** 10:37 Yeah, but we don't need to review it now, but yeah, it would be good to get, some opinions on that one.
And then also, just while I've got this open… There is a Prometheus one.
But Pyoto is approved.
But he asked that it would be good if someone else could have a look at it.
Cheers.
**Alan West** 11:01 7.448? Okay.
**Martin Costello** 11:03 Yeah, so this one, essentially, is part of the Prometheus stabilization.
we removed a property for, like, configuring URL prefixes, because it was tidy bound to the HTTP listener options.
And it wasn't something in the spec.
And then in the course of removing it, once after it had been obsoleted, I, found that I now needed it in the integration test, so I just sort of made an internal property to use for the test to solve that problem.
And then a user opened an issue going, hey, we wanted to, like, do wildcard host listening, and now we can't do it, because we can't configure it.
And the use case for the HTTP listener package is that it's kind of non-production-ish usage.
So, my suggestion was that we basically added, like, a delegate property on the options that just gave you the whole HTTP listener.
And you do whatever you want. It's sort of like… sort of like an escape hatch API.
And you can use it to do the use case that you can't do anymore, but without having to have first-class support for it. So that also means if they added new properties to the type in the future, we wouldn't have to change anything.
**Alan West** 12:26 Gotcha.
This… this package still, even though HTTP Listener is not… really considered a production thing. This package, you always used it behind the scenes or something, or…
**Martin Costello** 12:47 So Yeah, so HTTPS, like, the internal implementation. It basically gives you, like, a lightweight HTTP server.
to do Prometheus scraping from.
And the user… let me get open the issue. The user… Basically, their use case was they didn't want to use the ASP NetCore one because they had some hyper-optimized AOT And they didn't want to bring in all of ASPNetCore just to scrape Prometheus for their… Raspberry Pi stuff, so they've been using the HTTP listener.
And… for whatever reason on their Raspberry Pi thing, they needed to make it listen on any address.
And they can't do that anymore, since we removed the URI.
URL prefixes property.
**Alan West** 13:41 Gotcha, here we come.
**Martin Costello** 13:50 And the user seemed amenable to the idea of, if we gave them a way to do it, that that's fine with them, rather than having to bring it back.
**Alan West** 14:07 Okay.
And I think it seems reasonable. If we use HTV Listener behind the scenes, it's not like we're reintroducing a complete dependency that we removed.
**Martin Costello** 14:21 Yeah.
**Alan West** 14:22 No.
**Martin Costello** 14:22 Because, for users, like, with a full-on web app with ASP.NET Core, there's a different package they can use for that anyway, and there, if they need to do the same equivalent functionality, that's configuring ASP.NET Core, it's not configuring the Prometheus listener.
the HTTP listeners, like, they're sort of a weird hybrid that it basically gives you a whole server.
**Alan West** 14:47 Yeah.
**Martin Costello** 14:48 Just so you can do scraping, rather than plugging into the framework itself.
**Alan West** 14:57 Okay.
**Martin Costello** 15:01 But yeah, if, you could just give that a quick skin read today, and just leave a comment to… so Piotr knows you've seen it, and then I'll just merge the change if you're happy with it.
**Alan West** 15:13 Sounds good. Yep, I can do that.
**Martin Costello** 15:17 That was all from me, so… Judeus?
**Julius Koval** 15:23 Hi, I wanted to talk about the PR related to key-value lists.
But it looks like Rush isn't here, so I guess we'll wait until the next week again.
**Martin Costello** 15:34 So, Raj won't be back until the first week of August.
**Julius Koval** 15:39 Okay, well, fair enough.
**Martin Costello** 15:42 He's on extended PTO at the moment.
**Julius Koval** 15:44 Okay, okay.
Sure.
**Alan West** 15:48 He tends to take… I think July is kind of the month that he usually is out. He did… he was out last July, too.
**Julius Koval** 15:57 Yeah.
Yeah, I remember that.
Anyway, one more thing I wanted to mention was the… was persistent storage.
I was wondering if there's some kind of roadmap for it, because it's been experimenting for a while?
**Martin Costello** 16:16 I don't know the answer to that one, do you, Alan?
**Alan West** 16:19 Mmm… I've… never really followed the story on persistent storage very closely. It was originally something that… the team that Raj works with They had a… they had a need for it, and it was… They kept it internal because it was never anything that, was… spec'd. It wasn't in the specification.
And I thought that there was some… there was going to be some effort to try to drive it through the spec, though I don't think that ever Happened, to my knowledge.
So… Unfortunately, that's another one that I think I'd… I'd need to touch base with Raj on, because it was his team that originally introduced it for… For their own needs.
But, I'm curious, like, what, what does, what's your use case?
**Julius Koval** 17:35 So we have, a collector running on each of our servers.
And a few weeks ago, on a few of them, the collector was down for, like, a day or two, and I didn't notice that.
So all the data was lost, basically, and… Yeah, that's it.
**Martin Costello** 17:58 The two packages we have in contract for it say they're stable.
Just to check a… Are you specifically referring to the OTLP Retry storage stuff.
**Julius Koval** 18:11 Yes, yeah, that's what I meant.
**Alan West** 18:17 Yeah, it's the… I actually hadn't even realized that those packages were stable, but that's cool. But yeah, as it applies to OTLP retry.
that's… that was my memory. So, the specification for OTLP retry is… Pretty vague and wishy-washy.
And… the… your kind of use case, like, my collector went down for days, and I didn't notice, right, is just simply not something that the retry specification has… Really taken into account.
If you go… if you go read, like, the specification, the retry is… the framing of OTLP retry is mostly around, like, the transient kind of network issue, or errors.
That are usually resolved.
Within, you know, Just a few seconds or so, right?
But your use case, right, like, down for multiple days, I don't want to lose data, is exactly the use case that, Raj and team had. And so that's why they introduced this persistent storage. And then… I guess the hope was that they were going to take this to the spec and say, like, hey, you know, let's… let's talk about retry more broadly. Let's talk about, like, the different use cases beyond just, you know, transient network issues.
However, I don't think there's been any movement on that at the spec level, and so that's why we have not… We've kept it as experimental. I see all these experimental, configuration that, is on Martin's screen.
**Martin Costello** 20:15 It looks like… I vaguely remember this now, it looks like it's got, like, a fork of the code inside it as well, because, yeah, otherwise we'd have a sort of cyclic, depending on contribib.
**Alan West** 20:28 Hmm, sure.
**Martin Costello** 20:35 Gosh.
Yeah, I guess to answer your question, Julius, no, there isn't currently a plan to unexperimentalify it.
**Julius Koval** 20:48 Okay, sure.
**Alan West** 20:50 Yeah, I mean, the… The loose plan would be, you know, take this up with the spec and see if we can drive.
Drive it at the spec, but nobody's… Nobody, to my knowledge, is doing that at this point in time.
**Martin Costello** 21:12 And this might be one of those things, Julius, where it's sort of… no one does any further work until there's, like, known customer need for it. So if… maybe if you take this… if you open an issue in the spec.
about the need?
then maybe that will sort of kick… re-kickstart the conversation. Because also, typically.
for stuff to be stabilized, it needs to be implemented. I think it's at least 2, maybe 3 SDKs?
to, like, prove that it really solves the problem and get all to, like, the nitty-gritty detail out. So, if it isn't implemented in any of the SDKs.
We would also sort of need that.
Polarity and consensus.
**Julius Koval** 22:03 Sure.
And, what SDKs do you mean?
**Martin Costello** 22:08 any.
Typically, when something in the spec goes towards stability, it's… two or three SDKs of any language have to implement it, because that gives enough coverage that it's a solvable problem in a consistent way.
**Julius Koval** 22:27 Thanks.
**Martin Costello** 22:28 For example, we recently… there's, the environment variable context propagators currently in RC.
and .NET, Go, and Java, I think, were the three implementations.
There were, like, the quorum to get it over the line. I think .NET was, like, the third one.
Cause, yeah.
Because, yeah, typically, the individual SDKs, including us, push back on… per SDK-specific functionality, when it's something that should be common.
Or would make sense to be common, at least.
Because it stops us accidentally… creating a spec and, like, backing other people… other SDKs into, like, a specific design that hasn't been designed.
**Julius Koval** 23:30 Okay, so I'll try to create the issue.
**Alan West** 23:36 Yeah, if you, if you, are keen on… seeing if you can move that forward with the spec. You might search old issues, too. There's… there's been a number of issues, I think, opened with the spec with respect to… retry over the years.
And so, you might familiarize yourselves with those first, because there might be some issue that Touches on this, on… Like, persistent storage.
I just can't recall offhand. I don't have any to, like, point you to, but I know that there have been some retry issues open against the spec.
**Julius Koval** 24:17 Okay, sure.
**Martin Costello** 24:26 Anything else from anyone?
**Harsimar Kaur (Simar)** 24:30 I wanted to introduce myself real quick.
So, hey, yeah, I'm Simmer, and I work on Raj's team.
And so, I wasn't aware of the persistent file storage topic that you guys were talking about until now. And so I think it would be useful to open up that issue, and then we can see whether it makes sense for us to look into that or not. Like, my sense is that we probably won't be able to work on that until Raj gets back.
But, just for our awareness and the use case, I think it's good to understand further.
For us.
To open that issue.
**Martin Costello** 25:15 Cool.
**Alan West** 25:17 For sure. Yeah, and you know, I mean, since you're on Raj's team.
Right? Utkarsh and, CJO are kind of on your team, or at least a sister team, right?
**Harsimar Kaur (Simar)** 25:27 Yeah, yeah.
**Alan West** 25:29 Yeah, they have… they… If you're curious, you know, they would have some context of, like, your internal use case at Microsoft.
And, why?
why it was developed in the first place. Udkarsh, I think, worked on it quite a bit, and then, someone prior to that's not actually at Microsoft anymore, Vishwash.
The two of them were… The primary people that were involved in designing that.
**Harsimar Kaur (Simar)** 25:59 Yeah, I'll probably reach out to them as well, just to understand the historical context. Like, as far as I'm aware, we just haven't been working on the persistent fall storage for quite a long time.
And so, yeah.
But yeah, just in case, like, I have set up, like, my Slack, so if you need to contact me about anything, related to, like, PRs or stuff like that.
You can ping me as well.
**Martin Costello** 26:27 Okay, cool, great.
**Harsimar Kaur (Simar)** 26:29 Yeah.
**Alan West** 26:30 Sounds good, yeah, thank you.
**Harsimar Kaur (Simar)** 26:31 Nope.
**Martin Costello** 26:32 Always happy for more people to be involved.
**Alan West** 26:41 Alright, y'all.
Next week?
**Julius Koval** 26:46 Yeah, bye.
**Alan West** 26:47 See you.

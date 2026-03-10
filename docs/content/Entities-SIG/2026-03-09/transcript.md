SIG: Entities SIG
Date: 2026-03-09
Duration: 41 minutes
Zoom Recording URL: https://zoom.us/rec/share/L6BLTTpZiayQNjh_l-Ommu41x_BBh7kWuiVgTiILv_96BLPzmnWAKUad3k92EIXj.J1kNTPxidCVbckDk
============================================================

## Zoom Recording Transcript

**Josh Suereth** 00:01 is being recorded.
Hey, how's it going?
You… you're muted.
**Arve Knudsen** 00:50 Ha, sorry. I was just about to say, there are just the two of us, but, here is, here is Ted joining us, too. Hello, Ted.
**Ted Young** 01:01 Man, how do we fuck time up this much? This is the week that I'm always reminded of, like, how humans took a simple spec of time equals 1 second per second, and turned it into, like, non-overlapping daylight savings time nonsense.
**Josh Suereth** 01:18 Maybe half the reason why people are not here today.
Yeah…
You think, oh, is it… it's… do you think it's a Europe versus, North America thing, or you think it's people didn't…
They were sleeping in.
**Ted Young** 01:33 This is the week where we discover which meetings were, marked in, like, Pacific time versus, like, Central European time, because in North America, we go on daylight savings yesterday, and in Europe, they go on daylight savings, like, 3 weeks from now or something.
**Josh Suereth** 01:51 Yep.
**Ted Young** 01:52 So there's this, like, gap in here where the Grafana schedule and the OpenTelemetry schedule go, like.
For, like, 3 weeks, and then they, like, come back together.
**Josh Suereth** 02:01 Yeah.
Yep.
It's… yeah…
**Ted Young** 02:08 It's like, what do you do, you know?
**Josh Suereth** 02:13 Well, you can't… you can't do fun things, like, say, we're gonna meet when the sun's high.
You know.
**Ted Young** 02:20 We're not really there, but yeah, the daylight savings is weird.
Yeah, it's just… I mean, if it all lined up, it would be fine, but it's the fact that we do daylight savings staggered in different countries means there's this couple weeks where.
**Josh Suereth** 02:32 We do, we do it staggered within the U.S. by county some places.
I don't know if you knew that, but, like, there's, like, a county in Ohio that just doesn't do daylight savings the way the rest of everyone does, just because they can, you know?
It might not be Ohio, but it's somewhere near that. What? I said, how does your cell phone deal with that?
**Ted Young** 02:54 Just, like, constantly switching times when you drive over the county line.
**Josh Suereth** 02:59 Well, you ever see the drop-down for what time zone you're in, where there's, like.
For any particular time zone, there's still, like, 5 options within a time zone, because you have to figure out which daylight savings part you're in.
Yeah.
**Ted Young** 03:11 Anyways, I would guess if we're… if we are seeing light hotel stuff, it's for this reason, this week.
**Josh Suereth** 03:18 That would make sense, that would make sense. I think if that's the case, I want to do a quick review on progress, and maybe we'll call it early here, just because, I've been a bit focused on the stability by default stuff, which means I've let entities take a backburner.
I do have an update from a TC discussion, so I will add that as well.
Shit.
**Ted Young** 03:44 Oh, we got a Daniel, that's great.
**Josh Suereth** 03:47 On the.
**Daniel Dyla (Dynatrace)** 03:50 Yes, I am back from vacation.
**Ted Young** 03:53 Welcome.
**Josh Suereth** 03:55 Okay?
Cool. So, let's see… Let's do some reviews here.
I think, in progress, we have,
I think Dimitri's working on MDataGen, And fun things there, still.
But he's not here, so we'll skip the entity prototype for SDK specification. That is, so we can actually start finishing the merge logic.
Did the PR get merged yet? Oh, I don't have the PR listed there.
Here it is.
Is this it?
Yeah.
We still don't have anyone approving from the SIG, though.
No one knows.
**Ted Young** 04:54 approving from this SIG, or from…
**Josh Suereth** 04:55 From this thing, yeah, no one…
**Daniel Dyla (Dynatrace)** 04:57 Well, from anywhere, really, but from this SIG, I think, is what it's…
**Josh Suereth** 05:00 Oh, this thing to worry about first, that's step one, yeah.
**Daniel Dyla (Dynatrace)** 05:04 Yeah, I had meant to approve it, I think we were waiting… the reason that I wasn't was because we were waiting on the browser prototype that,
I forget who was working on…
**Ted Young** 05:16 Mark Kuba?
**Daniel Dyla (Dynatrace)** 05:17 Martin. Yeah, Martin was working on…
**Josh Suereth** 05:19 This is unrelated to the browser stuff, this is just our merge algorithm for our previous work. Or, like, this is from the previous OTEB.
**Daniel Dyla (Dynatrace)** 05:29 Oh, yeah, yeah, sorry, I… I thought we were talking about something else.
**Josh Suereth** 05:34 No, we're gonna talk about that in a minute, don't worry.
That's the TC feedback. We talked about that OTEP a bunch. I'll… we'll go through that. No, this is just the merge algorithm itself.
So, yeah, I haven't seen any updates to this. I believe I added everything and resolved all comments. It just needs to be approved. I also need to update it to latest, because they changed out the tooling used.
Now?
And this has been open so long that all of the tooling the spec uses has changed from underneath it, so none of these checks are actually called the same thing anymore. That's pretty, pretty beautiful.
Anyway…
Yep, so I'll update it to latest, and update it with some of the data model changes that happened.
Okay. Anyway, if, if no one, if…
I don't have anything that I think is contentious in here, and we've talked about it a lot in this meeting, so it just needs people to click the… that they approve, or, like, literally, I don't know how to make progress on this at this point.
**Daniel Dyla (Dynatrace)** 06:40 Yeah, we've talked about it a lot, it's been implemented in all the prototypes, I think, at this point.
we just haven't clicked the buttons, so I'll approve it, and I think we should just merge it.
**Josh Suereth** 06:52 Okay.
Cool. The TC asked me to make sure that people from the SIG have approved it before I push it there, so,
Alright.
So that's the status of that one.
SDK startup specification, you had this in, like, you added this, I think we could move this to…
I don't know if we can move it to done, because I don't know if we want it in the spec, but this was the notion of… we wanted to have it more clear.
how SDK components find resource?
And how that can be shared across the SDK. I think the OTEP around multi-resource actually calls this out pretty well, but I think it'd be nice to get it in the spec.
So I might leave this open for now, if that's okay?
**Daniel Dyla (Dynatrace)** 07:38 Yep, that works.
**Josh Suereth** 07:40 Cool.
And then, develop strategy for asynchronous resource and entities, and I know you were working on this, Daniel. I don't know,
Yeah, it's in the JS prototype, we just need to write it down, right?
**Daniel Dyla (Dynatrace)** 07:53 Yeah, and I think that this was on hold because we were doing the multi-resource stuff
And it was just a… A question of bandwidth.
**Josh Suereth** 08:03 Yep. Who…
**Daniel Dyla (Dynatrace)** 08:04 Who has time to do what first?
**Josh Suereth** 08:07 Okay.
Cool.
**Daniel Dyla (Dynatrace)** 08:09 Now that I'm back from vacation, I should have more time, so…
**Josh Suereth** 08:13 Yeah.
This, this thing, I… this is blocked right now. This is about tracking, communicating that we're going to have some breaking changes around resource, where,
attribute… this notice that attributes are no longer considered immutable. I don't know if we need to do that just yet.
But the, Prometheus compatibility specification, to notify that you can use identity, and to notify that the identity of resource is now,
actually uses the identifying part of the entity when it exists. I think this is, does need to get communicated, but we're nowhere near at the point where we can communicate that. We're still in, like, let's get the early part of the spec out, let's get our prototypes to the point where you can opt into them with a flag, and then let's
Right, so I feel like this is still blocked on that work.
**Daniel Dyla (Dynatrace)** 09:10 I agree.
**Josh Suereth** 09:12 Cool.
What else do we have?
Finish the SDK specification. So this is the next thing we need to do, is, actually working on the SDK specification from the prototypes, getting all the specs written from the prototypes that we wrote.
And then, getting, like, feature flags and stuff, and getting, sorry, getting it in the spec, and then actually getting the prototypes kind of merged with, like, an opt-in flag, so people can try it out.
Okay.
I'm gonna… so, Daniel, I don't know if you were here last week, but we had a discussion, a really good discussion on, the entity manager slash multi-resource thing. Effectively, what we built and what browser needs are different.
I still think the multi-resource thing is actually useful for a class of problem that we know we have, but I don't think it's going to be used for the browser's sake, and so we don't think it's a high priority right now to push that through.
**Ted Young** 10:11 Well, it's more, like, we discovered it's a broader problem. That's the way I would…
like, I feel… like, I don't know how the TC discussion, but I feel like we left that discussion being like, we designed the wrong thing, and I'm like, no, we've just discovered there's, like, more to this problem, right? There's… how do you deal with resources in, like, batch exporters and, like, things like that? And, like, how do you deal with a metrics SDK where the labels might change?
And then we discovered that we actually need all of this. I'm a little worried that if we keep being piecemeal and being like, the client needs this, and maybe the collector needs this other piece, it's a little bit like logging doesn't need an API or something, like…
like, I started to think about how, like.
we do need to, at least in one language, maybe it's Go, ship a complete SDK that can actually handle, like, all of entities. Otherwise, we're making an observability model and, like, not shipping people anything
To… to be able to, like, construct the data with.
**Daniel Dyla (Dynatrace)** 11:15 I think the prototypes, you know, when you say all of entities, the prototypes in JavaScript, Go, and Java all…
like, fully support everything that we've talked about. I don't think there's anything that's, you know, behind from that regard.
**Josh Suereth** 11:29 Right. So I think the TLDR from the… the…
TC was, first of all, there was some confusion about what this is and what it's for.
And so, once we walked through that, and I think there's just some language and terms I need to change in the OTEP to be less confusing for people, once we walked through what it actually is, and actually, Jack and David Ashpole were the biggest defenders here, which was nice. It wasn't necessarily me.
we're like, this is still a useful OTEP, and this is just one of the set of problems we need to solve.
not all the problems we need to solve, and we still need to solve more for browser. So that was basically the outcome of it. And so, what I asked them was, look, can we view this OTEP as a directional design that we might not implement yet, because we're going to keep looking at the rest of the problem?
But at least we agree, when we need to solve
an SDK reporting against multi-resources, where there's a limited set of things that you're doing, not necessarily a browser's problem.
that this would be a way we can do that, and then we listed some use cases where that could fit in, and they're like, yeah, okay. So, the tentative plan is, if we get all the approvals, we'll merge this, and it'll be a directional OTEP of, like, if we need to do multi-resource of the nature described in the OTEP,
This is a path forward, and we can move on to other problems.
**Ted Young** 12:53 Isn't that what Dimitri… wasn't that Dimitri's feedback last week? That, like, in the collector, they have to do this kind of stuff, and as a result, they're not using the Go Metrics SDK, because it doesn't actually work efficiently.
**Josh Suereth** 13:06 Yep. So I just feel like what you were pointing out, Daniel, in this is, like, when you want to deal with, like, entities changing and resources, it's like, we don't…
**Ted Young** 13:14 Like, you're pointing out an inefficiency that we're already, like, experiencing in the collector.
Yeah.
And I don't know how that relates to the latest work on entities in the Go SDK, but that was the feedback. It's like, the collector's definitely a place where this…
This proposal could be useful, because they're thinking about this problem over there.
**Josh Suereth** 13:36 Yeah, there was some, some expressed skepticism as to whether the, the collector would actually use,
the SDK ever, but…
**Ted Young** 13:45 But that's the smell I want to propose, though. If we create something like entities, and then we're like, there's no real way for you, the end user, to, like… we don't… there's no, like, hey, I want to go deal with entities, give me the, like, SDK for dealing with that. And we're like, there's a bit over here, there's a bit over there.
**Josh Suereth** 14:03 Yeah, yeah, yeah.
**Ted Young** 14:04 Just about that.
**Josh Suereth** 14:05 Well, it's also… I think the fact the collector could never use the SDK is a problem.
**Ted Young** 14:11 Like, there's a little bit of, like, that's just, like…
And I get it, like, things work more effectively when they're specialized, right? But there's also a little bit of, like.
What does it mean that we can't use our own stuff?
**Josh Suereth** 14:27 Yeah. Yeah.
Cool. So…
But basically, yeah, there's some discussion on this. I don't know… I didn't check the status of approvals on it. I think we might be…
If we look at it, I think we actually have enough approvals to merge.
Yeah.
So if anyone has concerns with this, like, still… actually, ironically, we… I don't think we got anyone from this SIG to approve it yet.
**Daniel Dyla (Dynatrace)** 14:57 Well, we were waiting… this is the one that I… that we were waiting on, the JS prototype. I was not here last week for that discussion, but I did…
Have a call, with… Martin the Thursday before I left for vacation to try to help him
to, like, to merge his prototype with my prototype. He was doing the session manager. So I'm aware of the problems that I believe you probably talked about, unless new problems came up in the meeting.
But the… the outcome that I…
remember, from my discussion with Martin is that they needed it to be more, like, global, right? Rather than instrumentation scoped the way that we kind of have it defined.
**Josh Suereth** 15:43 Yep.
**Ted Young** 15:44 The, the way.
**Daniel Dyla (Dynatrace)** 15:45 And they needed to…
**Ted Young** 15:46 expert metrics, right? If you're dealing with metrics labels, which is, like, the one problem we don't have on the browser.
So we could skip solving that problem for now, because we just aren't using the Metrics SDK in the browser.
**Daniel Dyla (Dynatrace)** 15:58 Yeah, but I don't think… I don't know if it's fair to say that nobody is using… like, people definitely use the Metrics SDK in the browser today, and I don't know if it's fair to say we'll never use it, so it should at least be considered. It may not be a major blocker.
But…
**Ted Young** 16:14 But in terms of, like, merging this OTEP right now, I feel…
I mean, there's, like, approvals for it, but I feel like we haven't quite figured out
where we're gonna use it, or how we're gonna use it. I'd feel a little weird merging this without, like…
**Daniel Dyla (Dynatrace)** 16:31 That's what I was just gonna say, is if it doesn't work for the browser, and the collector is already not using our SDK, then… is merging this OTEP bringing value? Do we have motivating use cases for it?
**Josh Suereth** 16:44 Yeah, that's… we talked about this in the TC a bit, so I'll just briefly share. I have internal use cases for this as well.
So, like, this is… this is how effectively we use OpenTelemetry internally. But today, we can't do this, so we instantiate a thousand SDKs, and people complain it's too inefficient, and they're, you know, threatening not to use it. So, it's,
Kinda, kind of important for us.
**Ted Young** 17:14 Do you do this in every language, or, like…
**Josh Suereth** 17:16 Yeah, well, so, we have our own implementation of, like, all the things in C++ that is hard to change, so that one is… no, but, like, we are, we are using this in, like, Go and Python and, Java and that sort of thing, yeah.
**Ted Young** 17:35 So you're saying, like, like, there's a use case for having the metrics SDK updated everywhere, potentially, for…
**Josh Suereth** 17:42 Yes. Yeah, yeah, yeah. And not only that, like.
let me see if I can describe the use case effectively. It's kind of a bit of a sassy use case, where I am reporting a resource for myself.
But I'm also reporting a resource for you, the user of me.
**Ted Young** 18:01 Yeah.
**Josh Suereth** 18:02 And so, I have a set of data which goes to you, my user.
to, like, give you observability, and I have a set of data that goes to me. And the resource for me has private things, and the resource for you has public things.
**Ted Young** 18:15 So you're dealing…
**Josh Suereth** 18:16 And then, like…
**Ted Young** 18:16 didn't see… okay.
**Josh Suereth** 18:18 Yeah.
And when I tried to describe this multi-tenancy use case, it really confused the crap out of the TC, because they're like, where's the tenant ID? I'm like.
No!
**Ted Young** 18:28 No, I understand, I understand this problem. I've had to work with a bunch of people, and it's hard.
**Josh Suereth** 18:33 Exactly.
**Ted Young** 18:33 It's not just multi-tenancy, it's also, like, two layers of observability, and all the… it's… yeah, it's a way trickier thing than…
**Josh Suereth** 18:41 Exactly. And so, I actually… I told the TC that probably, Google will be providing a set of proposals around solving all kinds of multi-tenancy problems in the future.
This is one of them.
However, this doesn't help the browser, SIG. It does help solve that problem, which I think is still a worthwhile problem to solve, but I'm okay… like, what I want to do is basically say, do we think that the shape of this is okay? If so, great. Let's put it on hold.
And let's move on and try to figure out how to solve the browser problem, knowing that this is a solution to a problem, but it's not the problem browser has right now.
**Ted Young** 19:20 I think that's fine. On the browser side, we're just gonna try to move forward with the… the prior proposal that was focused.
on this part of the problem, and and just deliver… we're gonna… what we're gonna try to do, what we feel like, in general, on the browser sigs, we had a discussion, and we feel like the time has passed to just be talking in specs in English.
Right? Like, we've just hit one of those moments where what we need is, like, a working end-to-end demo of, like, the browser, you know, clicking through multiple pages, and you have a session, and it's all… and we're like, this! This is the model.
That everyone can kind of play with and be like, okay, I get…
how all the pieces fit together, and it'll probably be hard to make, like, final design decisions about this stuff without being able to see it working together. So that's what we're focused on right now.
**Josh Suereth** 20:11 Yep.
Yep.
**Ted Young** 20:14 Cool.
**Josh Suereth** 20:17 All right, so I think I can respond to this comment, and I think this is high enough priority to act on right now, as everyone says. I spoke to direct this OTEP, left several comments, now I'm blocking, right. Okay, so that's the stats at OTEP. Go ahead.
**Daniel Dyla (Dynatrace)** 20:32 It looks like you got a bunch of TC approvals 5 days ago. I assume that that meeting must have gone well then. Like, they had some initial concerns, but you were able to address them?
**Josh Suereth** 20:45 All the people who defended the OTEP and said it made sense, including David Ashpel, who, like, wrote a whole implementation of it without me talking to him.
**Daniel Dyla (Dynatrace)** 20:52 And yeah.
**Josh Suereth** 20:53 Yeah.
**Daniel Dyla (Dynatrace)** 20:54 Okay.
**Ted Young** 20:54 That's great.
You know, the only other thing I might mention here is, like, I think this is a great proposal for, like, how do we retrofit the existing Metrics SDK?
There is, like, more of a stretch goal at some point in the future of, like, Metrics 2.0, right? Like, have we learned a lot about this? Have we updated our relationship with the Prometheus community? Is there, like, collectively enough stuff?
That we would want to take another shot at that architecture at some point.
But I think it's great to have this proposal in our pocket to be like, if we don't want to do it, we don't have to, you can do it this way. But I did wonder, based on Daniel, some of your comments about, like, how…
it made me wonder if we could, like, rework the internals of that SDK. Does that present a better experience to the end user?
But… but that's a whole can of worms, so…
**Josh Suereth** 21:52 Oh, yeah. I don't know if you saw, I've been doing crazy experiments with that, by the way, but I can… I can put on my chaser at… yeah. I'll send you a ping in a different channel, but I've been doing weird SDK reimplementation things,
But for context, if you re-implement the Python SDK in Rust, it's, like, 100 times faster.
**Ted Young** 22:12 Yeah, yeah, I mean, there's also foreign function calls, you know, that approach, but…
**Josh Suereth** 22:17 Yeah, anyway.
No, it's, it's, I'm using a slow architecture, and it's still 100 times faster. That was what would impressed me.
**Ted Young** 22:24 Shit.
**Daniel Dyla (Dynatrace)** 22:25 So, are we going to go to a previous proposal for the browser stuff, or is there a new proposal, or are we stuck with a problem without a proposal at the moment?
**Ted Young** 22:35 The previous proposal, like, but we're…
**Daniel Dyla (Dynatrace)** 22:38 Which previous proposal?
**Ted Young** 22:40 The one that I made last.
Okay. Because that's the one focused on this. This is what we discovered, right? It's like, we were looking at just, like, two parts of the elephant.
**Daniel Dyla (Dynatrace)** 22:50 Yeah, so I have to go back and look at your proposal, but if I remember it correctly, it required instrumentation to interact with the SDK directly, rather than going through the API.
**Ted Young** 23:02 No, that's… that's not true.
**Daniel Dyla (Dynatrace)** 23:04 Okay. I have to go back and look at it.
**Ted Young** 23:06 It's entirely abstracted, it's just the idea that, like, you have, like, an entity provider, and just what the thing you need for the exporter, the batch exporter, to know something changed, so I need to just segment this batch.
and then start a new batch. Not even necessarily flush it, but it's just the idea that, like, oh, it's time to start a new batch, because I've got a new set of resources.
And so it's literally just having that entity provider in there, and the…
the parts of the SDK that have to respond to those changes. And they don't really care… they don't want to know anything about sessions or any of the details. They just want to generically be like.
Stuff changed in the bag, so you get a new bag with the new stuff.
That's… that's kind of what we've seen we've needed.
to make entities work for logs and traces. It seems like the only places those things really care about this is resources. So, it's a simpler problem than… than with metrics.
**Josh Suereth** 24:11 Yeah, the argument I had, Daniel, was I think browser actually…
I think it needs a different API SDK shape.
Like… to Ted's point, I think the…
way that you bundle data together and fire it out is slightly different. Like, there's different places where it's safe to do so.
And so, like, batch span processor.
with the configuration control it has, maybe that doesn't make sense. Maybe there's something where we have a, like, you know, report when request is over processor, or something.
Right? Maybe, we don't provide a metrics API at all, because we can't do so efficiently, and if we have a metrics API, it's something different that basically fires events out, and then, as Ted was saying, you aggregate downstream.
Right? Like, I think that when it comes to browser, that's why I… we want to push on a prototype, but let's get something out to look at this, and look at the shape of it, and figure out what we need at various places, because I… yeah, I would be… the way that we designed our metric API and what browser needs.
**Ted Young** 25:15 Yeah. I think they're completely at odds with each other.
**Josh Suereth** 25:17 Right now.
**Ted Young** 25:18 In order to, like, like, just not try to eat the whole elephant in one bite, like, the approach we decided is, step one, make it complete
you know, with the existing SDK, right? Like, have a completeness first, efficiency second.
Basically. And all these SDK problems you're talking about are more like efficiency and… and hard edges and grinding all those things off, and if we need to, like, under the hood, totally redesign it, that makes a lot of sense. But we really don't want to have, like, a separate API, because that… we get worried about…
brine zone, node browser stuff and things, and…
**Josh Suereth** 25:57 That's fine. The metrics part, though, I do think, like…
The way the metrics is designed today, it's not an efficiency problem, it's a, you would never get data problem, potentially.
**Ted Young** 26:09 Yeah, yeah, yeah. I mean, I think it's fine. I totally agree that we need a different approach to metrics on the browser, but, like, everything else you're saying… Anyways, we're all in violent agreement. We're saying, like, we would much prefer to just make this work with the existing SDK and be like, this is how it works, and then later…
Once the model's working, be like.
how do we black box this SDK into something that's
actually browser-specific, because we all agree that it's, like, such a weird, gnarly environment, it would probably benefit from having its own…
implementation. And the trade-offs people want are different, you know? People don't want the same kind of optionality in the browsers that they want on the server and everything else.
**Josh Suereth** 26:56 Yeah, I had a friend who did Internet of Things as well, and I think you're in a similar space.
**Ted Young** 27:01 They want something that's much less flexible and much more built to spec, right? Whereas, like, our generic framework is much more about being flexible to deal with all the crazy situations that might come up.
But it's kind of like the opposite in the browser. Like, it just needs.
**Josh Suereth** 27:17 Just for confirmation, you're gonna tackle spans and traces with the current APIs, but you're not planning to throw metrics, or are you?
**Ted Young** 27:24 So the current… we're plan… the current instrumentation we're creating will just be… will be mostly logs.
**Josh Suereth** 27:31 Or spins and logs, sorry, logs, gotcha.
**Ted Young** 27:33 Right? So it'll be mostly logs, and where we're using spans is just when we're connecting to the server, right?
Right, so we're kicking off those spans, but where the advantage might be is it's not just, like, one network call. Potentially, you want to expand out that top-level span to represent the latency the user perceives.
But everything else is just events, because that's just the way the browser works. Right.
**Josh Suereth** 28:02 Okay.
**Ted Young** 28:03 And then we want to design those events very specifically with their attributes so that they can be turned into metrics later. But turning them into metrics and exporting from the browser, like you're saying, the mechanics of all of that don't make any sense.
**Daniel Dyla (Dynatrace)** 28:17 Well, the thing about metrics…
The thing about metrics is metrics only exists to aggregate a bunch of events together and save on bandwidth, and the browser is just only sending so much stuff. Like, it doesn't make sense to aggregate it on the browser.
**Ted Young** 28:32 Yeah, yeah, because it's the opposite. It's like, it's as fast as you can get it out the door is what you want to do, and you want to aggregate it and do all that stuff in a gateway or just somewhere else, right? So, it's like, yes, people could do metrics in the browser, but yeah, it's just, it doesn't…
The whole chain of stuff doesn't really make sense.
So it's like, it's never gonna… it's like, you would… the metrics implementation would be spitting events out, effectively, right? It would be spitting out measurements, not…
What we normally spit out.
So, yeah, we're fine just punting on that.
And just being like, don't, don't touch the Metrics SDK if you're in the browser, just… just don't, don't touch that plate, it's hot.
**Daniel Dyla (Dynatrace)** 29:22 Okay, I put into the chat what I believe is your previous proposal. There were a couple, but I found the one that I think you're referencing. It's closed as stale, so it should be reopened and brought up to date.
**Ted Young** 29:35 We, we want to implement…
I think what we decide is we just want to build a damn thing first, have everyone look at what we built, and then retrofit a proposal out of that.
It was just feeling a little bit like trying to, like, hold the pencil with chopsticks to, like, at this point, build the prototype via spec, and it would be easier to just show people a working end-to-end demo of, like, what we think the browser should look like.
again, without digging into the SDK in a crazy way other than this, and be like, this is what we're trying to do, and then…
Get that critiqued, basically, and extract a spec from that.
Rather than through a new spec, try to implement that and be like, oh, funny thing happened when we tried to implement this, let's change the spec on you guys yet one more time.
So…
**Daniel Dyla (Dynatrace)** 30:28 Okay.
**Ted Young** 30:29 Yeah.
**Josh Suereth** 30:35 I think, like, I'll be honest, I don't think that the OTEP you made Tep will get merged unless we find a way to scope it to browser.
Just because I don't think we can implement the metrics part.
**Ted Young** 30:49 I just think it's…
**Daniel Dyla (Dynatrace)** 30:50 We may not need the metrics part.
**Josh Suereth** 30:52 That's what I mean, like, I think we need to figure out a way to phrase it so it's like, hey, this is a feature, and we don't need it to work for metrics.
**Ted Young** 31:01 Right, right. It's not scope… I think we should think about it less like browser versus…
somewhere else. It's just more like, if you're… this is dealing with resources, and the others…
OTEP is dealing with metrics, right? These are the two places where entities show up in our data model, and they are handled by different subsystems in different ways at different times.
Like, and that's just, like, if you need to be updating resources on your batches, like your resource scope, you need something, I believe, like my proposal, because Daniel's proposal doesn't really…
Cover how that works, outside of, like, talking about statements.
**Josh Suereth** 31:42 The resource proposal, I'm just saying, I implemented it, and implementing it in an SDK today, where you have to interact with metrics.
**Ted Young** 31:50 I see.
**Josh Suereth** 31:50 what's problematic?
**Ted Young** 31:52 I see, I see.
**Josh Suereth** 31:53 That's the thing, that's why we put a pause on that OTEP, and we're like, this is really complicated.
So, that's what I'm saying, if you could find a way to de-scope it so you don't have to address the metrics problem at all.
**Ted Young** 32:05 I mean… it wouldn't solve your metrics labels problem, but I don't…
Yeah, maybe I don't quite understand how that interacts with resources.
**Josh Suereth** 32:14 So, when a resource changes, like, when you actually fundamentally change the resource and advertise a new one.
Do you kill the existing state of metrics? Do you keep the existing state of metrics? Do you try to make a double state of metrics, where you report what the previous values were against the previous resource and that? That problem was a pain in the ass to deal with, and if we can just not solve it.
I would be happier.
**Ted Young** 32:38 Yeah, that's what I… yeah, I think we're in agreement again. I… it's not… it's like… the question I have is, like.
Does doing… adding this to update the resources actually actively interfere with adding the second part that Daniel would want to add to solve the metrics part? Like, can we add one, and then add the other, and then you have a complete system?
Or are these things, like, actually incompatible with each other in some…
some weird way, and if we add an entity provider that does this, it will somehow… I don't see how that's possible, so it seems…
**Josh Suereth** 33:12 Oh, I… in code, it would be possible, because we're really lazy about resource right now. Everything is, like, a static reference and all that, so I… I think it's possible that we can resolve it. Like, that's fair. We'll just have to make the prototypes, yeah.
And if you need, I mean, I have a prototype of your previous OTEP, feel free to take it.
Is it in JavaScript? No, in Java.
**Ted Young** 33:34 Okay.
**Josh Suereth** 33:35 I think… did you make one in JavaScript, Daniel, or did we have one? I can't remember.
**Daniel Dyla (Dynatrace)** 33:40 I was trying… made one that worked for,
traces and logs, and then the… the metrics, SDK was fighting me, and we dropped it, so I never finished that one.
**Josh Suereth** 33:55 Yeah.
**Ted Young** 33:56 Look at those.
I kind of want the browser SIG to build their… they need to also internalize all of this stuff themselves, you know, so I think it's fine for that SIG to just…
**Josh Suereth** 34:06 That's good, yeah. And when it comes to metrics, if we're gonna talk… so, I think if your proposal is, when you mutate a resource in the way that you're suggesting, the metrics just carry along with the new thing, the way we're doing for, kind of, traces… well, so traces and logs we grab ahead of time. Like, we grab the resource when we make them.
That was what we were doing before.
If metrics, you say, cool, at report time, we just use whatever the latest resource is.
I honestly think that's 100% reasonable, and I don't see a problem. And we invented that problem and then tried to solve it, and it's, like, really hard and frustrating. But let's just say it's out of scope and not do it, and then I think that's fine.
**Ted Young** 34:48 The way I imagine it would happen, and I think we can actually spike this, like, on the browser, we can implement our part, and then we can take Daniel's prototype, right, of… of the metrics part, and we can just try to spike that in and be like.
can all of this play together, or… or do bad things happen? Like, we could certainly explore that, just to make sure
We aren't being cray-cray.
**Daniel Dyla (Dynatrace)** 35:11 I mean, the fact that the browser is not using metrics makes it more of a thought exercise than anything, and maybe that's… we should just get past that. But the problem that I had envisioned is something like, you know, you're measuring the memory use of a page, you switch pages, and then you report the memory use, and you report it
it's the memory that was used by the previous page that's now reported against the new one, and your data is lying. Like, it needs to be flushed.
Or reset somehow.
**Ted Young** 35:41 Right, right, exactly. If you were using metrics, and we implemented just the resource half, what I would expect the situation on the other side of that is you… everything would be working, it would just be, like, you would see the resources updated on that batch of metrics, but you would not see the labels updated on the metrics themselves, right? And so that would be the bit…
That would be out of sync.
Like you're saying, the metrics. But then if we added your piece, then the metrics would be able to update themselves.
I think it would be worthwhile to… to prove that… that these things are… are, like, parallel things.
and that they don't interact gnarly, I think it would be worth it to at least spike on that.
Even if it is just a thought exercise. Because I do feel like somewhere… something somewhere is gonna have to do all of this, and it's probably the collector.
But…
**Daniel Dyla (Dynatrace)** 36:36 Yeah, that's what I was just thinking, is I think it'll be the collector. Like, I can envision a future where the browser metrics SDK
doesn't do any metrics at all, it just delegates measurements to events… to the events API, and that fires to the collector, and then you use the, like, an event-to-metric processor to… to extract whatever metrics you need.
**Ted Young** 36:59 Yes. If we added an API, it would almost be like some sugar over the event API around…
Things people need to not have a…
you know, you can see events turning into a metrics footgun if you aren't thinking properly around certain things, but I don't know how much API saves you from that.
**Josh Suereth** 37:19 I also know from practical experience, it could be that you, architecturally, you're gonna have layers of turning into metrics, so that the collector might actually take things and turn them into one set of metrics where it compresses?
and report something down, and then your database might compress further into the actual metric you want, because you don't want to funnel everything through the same collector, for example. But yeah, like, that's why I think your system's going to be very complicated, and involve things outside of OTEL that our data model has to support.
Which is why end-to-end examples are winning here, yeah.
**Ted Young** 37:51 Yeah, it's really just kind of like a switch. There's a gateway that, if you turn it on, it knows how to make metrics out of events, and it's loaded with the schema for all of the browser
event metrics translation, so there's just something in the collector that can do that. But the reality is we expect probably for most people, depending on where people are sending this, you would only turn that on if you're sending it to a generic backend.
Right? If you're actually being like, I'm doing mobile observability in the mobile observability backend, you're not turning anything into metrics in the telemetry pipeline.
the backend is gonna deal with all that stuff, right? You just want to send it all of the events. So, it's like, what we kind of expect is, like, at least half the time, you're not even bothering to turn these into metrics, because that's all happening at the database layer.
**Josh Suereth** 38:46 Cool.
I think that's… I'm gonna call that discussion there, and say, I don't know about you, but I'm still tired from losing an hour of sleep.
And it's lunchtime here, so I'm hungry, too. Are we, I don't think we have anything else to talk about besides, like, let's review that merge PR, and try to get that in, and then I wanna… I wanna start…
with an SDK specification for defining entities and resource detection.
Right? That was… because that's part of our OTEP that was merged oh so long ago. I want to actually start getting that specification rolled out, so we can start getting, opt-in features of SDKs with entities out.
**Daniel Dyla (Dynatrace)** 39:32 Okay.
**Josh Suereth** 39:33 Okay.
Cool.
**Ted Young** 39:34 Sounds good.
**Josh Suereth** 39:35 Alright, thanks everybody!
**Ted Young** 39:37 by…
**Josh Suereth** 39:38 Be y'all next week?

SIG: eBPF Instrumentation
Date: 2026-08-26
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

**Tyler Yahn (Splunk)** 00:29 Hey, Mike.
**Mike Dame (Odigos)** 00:32 Oh, hey Tyler, how's it going?
**Tyler Yahn (Splunk)** 00:34 Doing well. How you doing?
**Mike Dame (Odigos)** 00:36 Good. Bye.
Haven't had a chance to get back to my PR that I've been working on, but…
**Tyler Yahn (Splunk)** 00:43 Oh, oh, yeah, yeah, I gotcha.
Yeah, how are… how are things these days over there? Are you busy?
**Mike Dame (Odigos)** 00:50 It's good. Oh, yeah, it's busy. We're, we're doing a lot. Got the… I really want… so, I really want to try to get that PR by, like, KubeCon, because we've got, kind of, a talk about that sort of stuff, about, like, dynamic and rendering in general.
**Tyler Yahn (Splunk)** 01:04 also kind of.
**Mike Dame (Odigos)** 01:04 open to talk about, like, the generated Go.
object files and how that works, and since we tried to do a whole talk on that before, I think this is a good spot to at least kind of bring it in and say, hey, if you're trying to develop or vendor this.
here's, like, the whole discussion that we've had, but this is, you know, I'd also like to have a little bit more there to show for rendering and building off of it, so that's kind of my goal.
**Tyler Yahn (Splunk)** 01:29 Yeah, yeah, I gotcha. Yeah.
**Nikola Grcevski @ Grafana / OpenTelemetry** 01:33 Hi, everyone.
**Tyler Yahn (Splunk)** 01:38 Steven, are you in a camper van?
**Stephen Lang (Raintank, Inc. – Grafana Labs)** 01:41 Oh, we're having some work done on the house, so I'm just, in the caravan on my drive.
**Tyler Yahn (Splunk)** 01:45 Yeah, nice, huh.
Oh, that's right, you're in, you're in England, it's a caravan, it's not a… it's not a campervan.
**Stephen Lang (Raintank, Inc. – Grafana Labs)** 01:51 Yeah.
Well, we have camper vans as well.
**Tyler Yahn (Splunk)** 01:55 Oh, really?
**Stephen Lang (Raintank, Inc. – Grafana Labs)** 01:56 They… so the camper vans, they have, motors.
So that…
**Tyler Yahn (Splunk)** 02:01 Oh, I see. Like a… what we would call, like, a Winnebago or something like that? Yeah.
**Stephen Lang (Raintank, Inc. – Grafana Labs)** 02:05 Yeah.
**Tyler Yahn (Splunk)** 02:05 Okay.
**Stephen Lang (Raintank, Inc. – Grafana Labs)** 02:06 Yeah. But a caravan is just a trailer.
**Tyler Yahn (Splunk)** 02:08 Cool. Oh, nice.
Yeah, I'm pretty jealous. Those things are pretty sweet.
I know that, like, certain people… there's strong opinions in England on those. I don't know why, but… Maybe it's because you all have, like, very tight space, here in the US, it's just, like, it's not even a big deal, but yeah.
**Stephen Lang (Raintank, Inc. – Grafana Labs)** 02:28 Yeah, yeah.
But, no, it makes, makes going away cheaper.
**Tyler Yahn (Splunk)** 02:33 Yeah, exactly, and instantaneous. You just get in the car, and you're already packed, like, it's already there, yeah.
Well, cool. Looks like we're coming up on 3 minutes in. There's a lot of people on the call, so we could probably get started here in just a second. If you have agenda items you want to talk about, go ahead and make sure you add them to the agenda.
If you have not yet, also, please go ahead and add your name to the attendees list, and yeah, we'll jump in here.
Cool, alright.
Awesome, so I wanted to start off, actually, is Mattia on the call? Maybe I could restructure this. Oh yeah, there's Mattia.
**Matt** 03:24 Okay.
**Tyler Yahn (Splunk)** 03:25 So I wanted to point this blog post out to folks that haven't seen it. I totally missed it two weeks ago. So yeah, like, this is happening.
Just a heads up, so if you haven't taken a look, please take a look as well. I wanted to ask you about this, I don't know if you saw my feedback on this, but I was wondering if we could maybe look at restructuring it?
**Matt** 03:46 Yes.
Maybe? I'm, I'm not sure what's the, what's the, like, the usual, tone in which these blog posts are written. So I was thinking, maybe it needs to be more technical, maybe it doesn't need to be, like, Like, a substitution for documentation?
That's… that's why I initially brought it like that. I wanted to understand what's the direction we want to go.
**Tyler Yahn (Splunk)** 04:17 Yeah, so, usually, my read on… almost all the blog posts that I've read on the OTEL website are that they're for the end users. They're… they're not particularly for developers. They're for people that are interested in OpenTelemetry, or interested in, like, the updates on OpenTelemetry, or what's going on, or are new to the project. So, The details of, like, how it's actually running, and how it's actually operating, the technical stuff.
Is usually not… included, but it's also, I don't think, the target audience, I don't think we're gonna have a lot of developers for OB.
reading the blog post. And if we are, I mean, I think that's great. I think it's great.
But I think that that's a really small audience, right? And so I wanted to try to see if we can repurpose this to try to hit a broader audience, because you are going to get a lot of the industry to look at this, and when they start reading things about, like, you know, the internal eBPF dynamics and the kernel, like, internals.
I imagine that's where they're gonna stop reading, which is kind of a shame, because it's, like, a really phenomenal feature, and I want to make sure that they, like, try it out. I think is kind of, like, the goal I would love to get to. So yeah, that's why I was suggesting maybe we try to take back the, you know, the internals of, like, the maps and stuff.
And more so position it as something that, like.
you know, as a… as a SRE, or as a DevOps, or something like that, like.
how can this help them? Like, you know, obviously, like, you start off really, really well, like, pointing out that, like, you know, this has a lot of value, but then showing, like.
Real use cases like you're doing, highlighting that really… pointing out then, like, operational things, like how can you get started, what can you do today to, like, start working on this, I think it's really helpful for, like, those end users, and I think we're gonna have a little bit more of an impact if we go in that direction. But I did want to bring it up to the broader audience, though, to see what others' opinions on this are.
**Nikola Grcevski @ Grafana / OpenTelemetry** 06:17 Yeah, I think you bring a valid point. I also, like, mentioned in my comments that, I mean, I think it's important to say that this actually works on OTEL instrumented applications as well.
And it sort of completes the story, because… I mean, the span IDs won't match, but the trace ID will, and I think that's really useful to somebody who doesn't have anything. So even if you have, like, a hotel Instrumented app, and you have no ability to do Law correlation… oh, we can finish that.
And it sort of is perfect that we have this separate section in which we declare What services we want to instrument with, the law correlation.
So, it could be, like… a really nice addition. I could say, hey, if you didn't have this before, and that's for the end user's perspective, you didn't have this before, you wanted to have correlated logs with your hotel Python tracing or whatever, this is what you do. You can easily get this going.
And, maybe describe some of the gotchas. I think, I'm not mistaken, for Python, you need an environment variable or something to make it work. Some of those.
Pacific?
**Matt** 07:32 Python and Buffer, that's in case.
**Nikola Grcevski @ Grafana / OpenTelemetry** 07:35 Yeah.
Yeah.
Which is, I think, common for a lot of people, because I think otherwise you miss a bunch of messages if you do Python on Buffer. If you don't have it, even, like, the SDKs, like, some of the messages will not come out.
Unless you have this Python and buffer.
Yeah, describing some of those gotchas, what are important. I think for some… like, if… I think Tyler's right. Focusing on somebody, how would they use this, rather than what we build? But I think what how we build this, I think it's a falls down talk.
how to abuse the Linux kernel, with eBPF.
Yeah, that would be, like, a great following talk for 2027, February.
**Tyler Yahn (Splunk)** 08:22 I also think that, like, you could take a lot of the technical details and put them in our dev docs, and then link them, from the blog post. You know, I think, like, yeah, to Nikola's point, like, that could turn into, like, a Fosden talk, it could also turn into, like, a, hey, like.
you… how… like, you're wondering, like, you just read all this, how do we do this? I think you do a really good job describing it. Like, that, I think, is actually great. It's just that, like, I think that maybe we could put that in a different place, and then we can link to it or something like that. I think it's maybe a better, approach.
**Matt** 08:52 Yep, makes sense.
**Tyler Yahn (Splunk)** 08:54 Okay.
**Nikola Grcevski @ Grafana / OpenTelemetry** 08:55 I thought it was cool, I mean, I thought it was, like, good to ship, to be honest.
But I think Tyler makes a really good point. If it's for more for the end users that will be reading this, then we'll probably lose them by… what the hell? Like, why do I care about slow-level stuff?
I mean, there's a certain number of people that do care about this stuff, obviously. I mean… Those would… those would definitely be a positive.
**Tyler Yahn (Splunk)** 09:26 Yeah, but I mean, I definitely want to reiterate, I mean, I think it's, like, a really cool feature. To Nikola's point, like, it's… It's one of those things where I think that, like, Obi's doing things that people kind of… forget how, like, cool some of the stuff we're doing is, and this is one of them. Like, it's like, yeah, like, even regular hotel services, like, can benefit from this. It's not just this niche thing, so making sure we, like, capture that and telling people what we're doing, I think, is a great idea.
That being said.
I'm happy if we wanted to, you know, convert this to a draft and start, like, working async in, like, a Google Doc or something like that, Macias, I'm happy to help, drafting and working on this with you as well. Also happy to just keep reviewing if you want to just iterate on it.
**Nikola Grcevski @ Grafana / OpenTelemetry** 10:09 Yeah. And on the… on the not just eBPF Instrumented applications?
I wanted to… like, the reason… I actually didn't realize how big of a deal was this to kind of complement the story for the regular SDKs until KubeCon… EU this year, I spoke to Lyudmila.
And when I mentioned that we have this capability, she was like, what? How come I don't know about this? This is like… It's been a missing piece for such a long time, like, there's so many… People that are struggling with this.
You need to talk about this.
And that's when I realized, what? Not all SDKs have… law correlation? I… it was news to me, but apparently, in many cases, they cannot.
Can someone else supported, yeah.
**Tyler Yahn (Splunk)** 10:58 Very few, actually, have… Very few, yeah. Yeah.
Yeah.
So yeah, yeah, I think this is great. Yeah, let me know, Macias, if you need some help on this, okay?
Okay, cool.
Okay.
Next up, I wanted to, jump in and ask, about the next milestone. Actually, I wanted to pause. Just a heads up, thanks again, Macias, for getting the, V… what are we at, V0122, out.
Yeah, that was definitely a lot of iterations on these next releases, so yeah, it's been a little bit of a whirlwind. Yeah, so thanks, thanks for doing that.
The V013 is still slated.
there's definitely some more blog post… I'm sorry, some more, bugs and other, fixes and enhancements coming out in this one, so… Yeah, pretty excited about all these things. I did want to jump in here, though. We've got a lot of it assigned, a lot of it scoped. I had originally thought something like October… I don't think I've updated this yet, but yeah, something around, I'm guessing at the end of September, but… Obviously, if we can get this out earlier, that's all the faster we can get to an RC, all the faster we can start to, get to that 1.0. So, yeah, I just wanted to double-check, make sure that this is scoped properly.
If there are things that are missing from this, I'd love if we can talk about those, maybe add those, now, or in the near future so we can understand it. And then, for the things that aren't assigned, obviously, like, they need owners, Definitely a few that I'd love to pick up, but I didn't want to, like, jump in in case other folks are looking to do something.
Yeah, I mean, in that said, I can talk a little bit about, maybe the work that I'm looking at doing. Obviously, the stabilized opening release artifact stuff is just a documentation task.
For those that are looking to pick something up, it's more about saying, like, project-wise, what we're actually trying to accomplish, and, like, what we guarantee going forward. It's not too hard, given what we're already doing. It's probably just… just needs to be documented, essentially, what's going on there. So yeah.
I think the GoTracer PreventDuplicate trace parent injection, I started taking a look at this one. I had built this nice, big ol' PR that was, like, 6,000 lines, which just is not gonna get reviewed. So I'm looking at breaking it up. I've got a proposal here to try to change a little bit of this. It has a lot to do with, like, this thing that we just addressed, where… There's offsets from two different libraries, and they were both producing, transparent injections. So, wanting to resolve that is kind of the goal. I've got a little bit of a plan going here.
There's definitely, you know, a little bit of a rollout. Obviously, like, we wanted to provide backwards compatible support for what already exists when things are working, so that's the goal here. You can read the details here if you're interested, yeah, but it's also probably not worth going too deep in just this meeting.
The config v2 migration end-to-end coverage, this is, again, also something we had asked for. I'm starting to work on this. I'm not exactly sure this is a blocker for V1, but we have it in the milestone. This is a follow-up from an ask that Mario had made. It's one of the PRs, so I've split this out.
I could probably get this done, I estimated it in 3… well, I didn't estimate… AI estimated it in 3 PRs, so, yeah, I think that we can probably get this done, so I'm… Working on this, as well.
I think… other than that, the big ones I did see in this one are the semantic convention stuff, I see Nimrod's out of the call.
Do you want to give us a little bit of an overview where we're at on this stuff, and progress towards this?
**Nimrod Avni** 14:47 Yeah, so… regarding coverage, we have coverage in all the main three integration suites, which is, like, the normal integration, OATS, and Kubernetes.
regarding the publishing of the schema, I have a draft for it. I think I can… I just looked at it before the call. I'm gonna make sure it's ready, and then I'm gonna… open it up for PR, and basically publishing the schema to our GitHub pages. Might need some, like, requirements on the REPA, I need to check if we can do it ourselves, so we need… Someone from the maintainers.
Regarding the telemetry schema, Basically, there's… Yeah, I have a couple stuff that are kind of additive, they're not blockers, but I have something that, I have a… a PR that's not on one of my forks, so I can open.
Which will supersede the one, like, the 3004?
Which is, like, kinda old now, and that PR just became… Really big, because when we need to redefine a lot.
So I'm gonna… I think I can… I can already open it now, but it might be, like, a… I don't know if there's a real way to split it, because it's just… Taking… basically rewriting the whole, schema.
That we're exporting, plus some, like, tests to make sure that we don't drift, and a lot of stuff that, like, you can't really ship it without it.
So it might be a kind of a big PR, but I'll try to give, like, a very detailed description to have, you know, the reviewer's life easier, but I think we can get it done.
**Tyler Yahn (Splunk)** 16:38 Okay, yeah, that sounds good.
So you're saying this published OB telemetry schema is pretty close as well, and then this one is… needs to take another look, maybe break it up, but maybe it also just needs to go?
**Nimrod Avni** 16:50 Yeah, I think that one will… I'll probably close it and open a new one instead of it. Okay. And yeah, I'll… once I'm done, I'll probably… I'll send it so we… you can have a look.
**Tyler Yahn (Splunk)** 17:03 Cool. Alright, yeah, that sounds good.
Is there anything… issue-wise, or other PRs that we need to include in the milestone, probably want to include this in the milestone.
**Nimrod Avni** 17:15 I think the, the one with the span metric sizes is probably… I'm hoping to get it done before the… the schema one, because it will affect the schema.
And we can even do the, like, the internal queue stuff, but that's not, really critical.
**Tyler Yahn (Splunk)** 17:36 So you're saying this one… add this to the milestone as well?
**Nimrod Avni** 17:38 Yeah, I knew that.
**Tyler Yahn (Splunk)** 17:40 Yeah.
Cool. Alright.
Yeah, these look like bugs as well, but… okay.
Okay, yeah, we'll keep an eye on it, updated that…
**Nimrod Avni** 18:05 I think after the schema, I want to have, like, another… Basically, coverage test that will, like, say how much of the… how much of the schema we actually cover with integration tests. It will only work on Metrics and resource… and resource objects, because spans are not an official, like, schema, like, object, like, you can define, like, what is an HTTP span and what attribute… you can define the attributes, and you say, like, you know, this attribute should have these values.
But there's no, like, entity that is, like, an HTTP span has attribute A, B, C, whatever. I think there's a Notep open for it, I can link it.
So the coverage won't work on spans, but it can work on attributes, on metrics with their attributes, and on resources.
So I… but I want to get the schema first before doing that.
**Tyler Yahn (Splunk)** 19:01 Okay, yeah, that sounds cool. That's definitely interesting to know.
Okay, yeah, I'd be interested in seeing that. Have you looked at, tasks like, Auto Discovery, like, God, what's it called? Like, semantic conventions Validation, project… yet?
**Nimrod Avni** 19:20 The one that, Steven linked, like, a couple…
**Tyler Yahn (Splunk)** 19:24 Yeah, it's just, like, it's been evolving, and so, like, there's a bunch of, like, test cases, essentially, where he's got these runners, essentially, like, examples that will generate, semantic conventions, and then… And then it uses Weaver very similar to what you're doing, but I just didn't know if, like, you've been following that, I guess. Maybe not seen it, but following it, yeah.
**Nimrod Avni** 19:45 I actually, actually, since we saw one of the previous SIG meetings, I haven't… Go ahead and get a look at it, so I'll try to see if there's anything relevant there for us.
**Tyler Yahn (Splunk)** 19:55 Yeah, it may be, like, relevant, but it also may be, like, we could just, ship them our stuff as well, like, sending, like, some… because I think that there's, like, he's trying to, like, essentially add this whole database for all this support.
And saying, like, add a column instead of, like, you know.
for, for Go, or for Obi. It'd be pretty cool, so…
**Nimrod Avni** 20:16 Maybe once we get, like, the full… schema, and we publish it.
**Tyler Yahn (Splunk)** 20:21 Yeah, yeah, exactly.
**Nimrod Avni** 20:23 Zoomed.
**Tyler Yahn (Splunk)** 20:24 Yeah, something like that'd be cool, so… Yeah, just a thought. I don't know if you were following, but, yeah, I'm getting pinged on a few PRs, and so I just… that's why it's top of mind, yeah.
**Nimrod Avni** 20:32 Yeah, that sounds cool. I'll have it. Yeah.
**Tyler Yahn (Splunk)** 20:36 Okay, cool.
Alright, I think that that's probably a good overview, if folks… would like, over the next week, please try to solidify what you're going to be doing for this next release, because I think we want to try to get that work done. So, making sure we have the scope, correct is pretty appropriate.
Okay, last up, I just wanted to stop in again on the OpenPRs. We had done this last week, we didn't get through all of them, and there's a lot.
So I wanted to maybe just step back. I did see Mario's back. Welcome back, Mario. It was a good break.
**Mario Macias** 21:15 Thank you.
**Tyler Yahn (Splunk)** 21:16 Yeah.
I know there's a few PRs we saw of yours that we were kind of pausing on, so maybe we can jump in as well into those, Yeah, I think, this we definitely talked about. I think there's definitely some changes requested here. I can't remember if our decision was to close this, actually.
**Matt** 21:38 I think this one is almost good, but the changes keep breaking the… The verifier for some kernels.
**Tyler Yahn (Splunk)** 21:47 Hmm.
Okay, so it's more just about getting the test suite running, yeah.
**Matt** 21:53 Yeah.
**Tyler Yahn (Splunk)** 22:03 Okay.
These two still drafts, add support for generic Python async Server. Marc's on the call. I think that there's been some review on this one, right?
**Marc Tudurí** 22:17 Yeah, it's on your… your plate, I can, so… Okay.
**Tyler Yahn (Splunk)** 22:21 So it's just coming back to me? Okay, I will take this on.
Okay. Mario, Dino, Instrumentation Library, obviously you've been out for a little while, so maybe this isn't top of mind. There was, overlap here. I did have, another PR that went in, and it fixed, the SIG User 1. Yeah, Trying to remember…
**Mario Macias** 22:46 Oh… Yeah, I didn't have time to look at that, since I come from holidays, but yeah, we'll have a look and… And…
**Tyler Yahn (Splunk)** 22:56 Yeah, yeah, no, I figured.
**Mario Macias** 22:57 libraries.
**Tyler Yahn (Splunk)** 22:58 Yeah, just a heads up on this one. Yeah, I do think you had, like.
**Mario Macias** 23:01 Okay.
**Tyler Yahn (Splunk)** 23:01 Similar, like, a different fit.
But it just, like, there was a very similar, like, pattern for the Instrumentation stuff, so…
**Mario Macias** 23:08 Who's.
**Tyler Yahn (Splunk)** 23:09 copied into this PR, and then… so then the idea is, just should be able to rebaste.
**Mario Macias** 23:12 Okay, okay, okay.
**Nikola Grcevski @ Grafana / OpenTelemetry** 23:15 Recently, I think I checked, we do have a Dino Instrumentable type in main now.
Yeah.
You can find it, yeah.
**Tyler Yahn (Splunk)** 23:25 Right, yeah.
**Mario Macias** 23:26 Yes, this is, I think, this is internal.
**Nikola Grcevski @ Grafana / OpenTelemetry** 23:31 Okay.
**Mario Macias** 23:32 This is how we internal consider the… the Dino, unless someone else has added the, the… I did. Okay, okay, okay, then… then I will… I will see, maybe we need to remove this, or… Yeah, close it. Okay, well… Close it, or… or…
**Tyler Yahn (Splunk)** 23:50 Yeah.
**Mario Macias** 23:50 Okay.
**Tyler Yahn (Splunk)** 23:51 like I said, I think that's… I definitely added the internal, or sorry, the interpretation type for Dino, but I was using it for a different thing. I think you're trying to do some different parsing of, like, what is actually.
**Mario Macias** 24:00 Okay.
**Tyler Yahn (Splunk)** 24:00 So it may just be, like, using that internal type and then achieving those things, but yeah. Yeah, Nikola, to your point, yeah.
**Mario Macias** 24:07 Okay.
**Tyler Yahn (Splunk)** 24:08 there, so… Nikola Grcevski @ Grafana / OpenTelemetry 24:08 There is even a test thing Dina specifically does.
Yeah. Integration test, yeah.
**Tyler Yahn (Splunk)** 24:14 Yeah, just a heads up, yep.
**Mario Macias** 24:17 Okay.
**Tyler Yahn (Splunk)** 24:17 Okay. Then, mario, you also… this is, I think, a… yep, design doc for the DINA stuff, yep.
Plan on working on that one, I'm.
**Mario Macias** 24:28 Yeah.
**Tyler Yahn (Splunk)** 24:30 Mike, we were just talking about this at the beginning, something you're still looking at, haven't gotten back to, though, right?
**Mike Dame (Odigos)** 24:36 Yeah, and I might, try to sync up with… I know, Nikola, we talked about this last time, about… I think we kind of… just to rehash, we decided that it would be acceptable to do a, like, a different map for, I guess, Bear host.
processes that is keyed on kind of the old tuple-based approach, socket and PID, so that we can just grab that info. So that's what I still need to do.
It's just… you know how slow I am with getting back to stuff, but I do have some questions, if there's any, like, references that I can point to, or, you know, I'm kind of digging through the history a little bit, but… I might pin you later. Yeah, still working on this. It's not tied to any milestone or anything, it's, just something we'd like to support for some users.
**Tyler Yahn (Splunk)** 25:29 Yep, yeah, absolutely.
Sounds good.
Okay, This, I think, is a really cool proof of concept, but it doesn't need to remain open.
So, yeah, exactly. Let's just close this.
I can still reference a closed PR.
Cool. Alright, had always omitted telemetry schema, this is something also we just talked about. Add support for Python runtime metrics. Mark, where are we at on this one?
**Marc Tudurí** 26:04 Yeah, giuseppe added a review, and I addressed your comments, and I'm still waiting for Nikola.
Yeah.
**Nikola Grcevski @ Grafana / OpenTelemetry** 26:15 Yeah, I'm declaring review bankruptcy, so I'm trying to catch up with everything.
I've been, like, this last two days a little bit under the weather, so… Trying to shake that off, and… Get everything going. But today's my review day. I've decided to spend the whole day on reviews to catch up with these 45 PRs we have opened.
**Marc Tudurí** 26:38 Oh, nice.
**Nikola Grcevski @ Grafana / OpenTelemetry** 26:39 I will get to it today.
Oh, I can promise, yeah.
**Tyler Yahn (Splunk)** 26:45 Okay.
Published telemetry schemas, talk about that one.
**Close Admago… Connection host and logging, Nikola Grcevski @ Grafana / OpenTelemetry** 26:58 Yeah, that's… that's a… that's the one that we discussed at length.
**Tyler Yahn (Splunk)** 27:03 Oh, that's not… Nikola Grcevski @ Grafana / OpenTelemetry 27:04 Last time, but… I think it's just,
**Tyler Yahn (Splunk)** 27:07 It doesn't have a CLA, like, it's not… Nikola Grcevski @ Grafana / OpenTelemetry 27:10 Yeah…
**Tyler Yahn (Splunk)** 27:10 And this is exactly what you talked about, where you're like.
Yeah, 2 days ago, 2 days ago.
**Nikola Grcevski @ Grafana / OpenTelemetry** 27:17 I think, I think it's a good idea, to be honest, I don't know why it's not working, I haven't looked into detail, because there's no CLA, but I think it's, It's doing the same thing that Mark did for finding in Go the actual host name for remote SQL database. Marc did that for Postgres and MySQL. I think this is trying to do the same thing for MongoDB.
**Marc Tudurí** 27:45 Good.
**But… Nikola Grcevski @ Grafana / OpenTelemetry** 27:48 I mean… BOA, and… Maybe we… maybe if this doesn't have any movement, some of us can take over and just implement this.
**Matt** 28:00 I'm not sure what this PR is doing, to be honest, because there is an added field in the C struct, but it's not getting filled anywhere.
**Nikola Grcevski @ Grafana / OpenTelemetry** 28:10 Yeah, it's probably, like, an AI-generated stuff, but I think the idea is probably… Valid.
I think it's trying to, you know, when you have… Go servers.
And you… Call into, like a remote database, let's say this MongoDB.
We don't know what the name of the server is.
We don't export that anywhere. We will put an IP address. And now, because it's just an IP address, unless it's on the same cluster, you have no idea, and it's Kubernetes, you have no idea what that is.
Unless you can reverse DNS it somehow, and so on.
But the… the data, what the database is, is in one of those Mongol structures.
So, it would be nice to extract it and pass it along with the payload that we ship through the ring buffer.
Which is what we did… what Marc did for Python, MySQL… Sorry, Postgres, MySQL.
So you extract from the driver what the actual database is, so then you're… Metrics and traces look much better, right? You know what the remote is.
**Matt** 29:27 Yup.
**Nikola Grcevski @ Grafana / OpenTelemetry** 29:29 It's useful.
Right.
**Tyler Yahn (Splunk)** 29:32 Yeah, okay, let's give it another, I guess it's only open a week, but, yes, things are moving fast. If there's no movement on the CLA, let's close this, and then, if it's of value, we can have somebody else open up a PR for it.
Yeah. That sounds good.
**Nikola Grcevski @ Grafana / OpenTelemetry** 29:44 I know.
**Tyler Yahn (Splunk)** 29:47 Okay.
Update Docker. This should be cleared, we just added support for Go 1.27, which was blocking this, so just waiting on CI on that one, so, yeah.
Generic trace to report an unobserved response, as unknown.
**Nikola Grcevski @ Grafana / OpenTelemetry** 30:06 Yeah, I think he addressed your last comment. I haven't actually had time to review this one more time.
We'll see if tests passed. I think mostly it was okay, but some… Tests keep on failing, so he's trying to get it right, I think.
**Tyler Yahn (Splunk)** 30:23 Yeah.
Yeah… It's, it's morning on the US time, so this is always when CI is… Problematic.
Okay, yeah, I'll definitely take another look at this one now.
Fix, keep conditional parent sub, settlement coherent. This is another one, that I was working on, I guess, a week old now? Yeah, I'm trying to remember, Yeah, this just needs review.
Maybe.
I need to look into this failing test.
**Nikola Grcevski @ Grafana / OpenTelemetry** 30:59 2 minutes, it probably failed because it couldn't pull an image. I would just bounce it.
**Tyler Yahn (Splunk)** 31:04 Yeah, I think I might be on, like.
**Nikola Grcevski @ Grafana / OpenTelemetry** 31:06 Yeah.
**Tyler Yahn (Splunk)** 31:07 Definitely right.
**Nikola Grcevski @ Grafana / OpenTelemetry** 31:08 Actually, this will… you won't be able to resolve this. You know what?
I think you probably need to push. This happened to the same user And he messaged me and asked me what the hell is going on with our CI.
somehow, the CA gets stuck on this… Problem.
**Stephen Lang (Raintank, Inc. – Grafana Labs)** 31:28 It's the… the generateBPF. The artifact only stays.
**Tyler Yahn (Splunk)** 31:33 Yeah.
**Nikola Grcevski @ Grafana / OpenTelemetry** 31:34 Yeah, this cash.
**Tyler Yahn (Splunk)** 31:34 I think it's actually 24 hours, or something like that.
**Stephen Lang (Raintank, Inc. – Grafana Labs)** 31:36 Right.
**Tyler Yahn (Splunk)** 31:37 Like, it's… yeah, so… Nikola Grcevski @ Grafana / OpenTelemetry 31:38 Restart the whole thing, I see.
**Tyler Yahn (Splunk)** 31:41 Yeah.
**Marc Tudurí** 31:42 Yeah.
**Nikola Grcevski @ Grafana / OpenTelemetry** 31:43 I asked him to push, force push.
**Tyler Yahn (Splunk)** 31:46 Yeah, that'll do it.
**Nikola Grcevski @ Grafana / OpenTelemetry** 31:49 I had never seen it, okay. Yeah.
**Tyler Yahn (Splunk)** 31:52 Yeah.
**Marc Tudurí** 31:52 Well…
**Tyler Yahn (Splunk)** 31:53 Found the solution anyways, yeah.
**Stephen Lang (Raintank, Inc. – Grafana Labs)** 31:55 Yeah, do what Tyler did and do rerun all jobs instead of just failed, and it will regenerate the artifact.
**Nikola Grcevski @ Grafana / OpenTelemetry** 32:02 I see.
**Tyler Yahn (Splunk)** 32:03 Yeah, but of course, then you get put back in this queue, so… Nikola Grcevski @ Grafana / OpenTelemetry 32:06 Yah, yeah.
**Tyler Yahn (Splunk)** 32:07 We'll see you next week.
Yeah. Okay. Well, I'll keep an eye on that one, see if I need to actually address anything, but it should be ready for review, though.
Nimrod, these other two I don't think are ready for review yet.
**Nimrod Avni** 32:24 They're probably soon ready for review, but I'll open up the writing.
**Tyler Yahn (Splunk)** 32:30 Right.
We'll pause on that, then.
Nikola, Python extracts service metadata from known frameworks.
**Nikola Grcevski @ Grafana / OpenTelemetry** 32:38 Yeah, so… Yeah, I moved it up to review just this morning. I was fighting with all the edge cases yesterday that I could possibly find, because maybe I think I tried to chew too much.
In one, go, because I tried to support all this weird… Python frameworks, and they all have their own Nuances around the options and whatnot, but… I think it's there now, so… Yeah.
**Tyler Yahn (Splunk)** 33:06 Okay.
**Nikola Grcevski @ Grafana / OpenTelemetry** 33:07 And it's… I've got, like, 3 more that are in work in progress, but not moving. They're all dependent on one another, and, like, here I realize I have duplicate bunch of code, so I restructure some of it, reuse.
Between no Java and now Python, so…
**Tyler Yahn (Splunk)** 33:22 Hmm.
**Nikola Grcevski @ Grafana / OpenTelemetry** 33:22 I can't… like, the rest of them, they're in draft, they should stay in draft.
Yeah, that's Merge Maps, so… Yep.
**Tyler Yahn (Splunk)** 33:30 Yeah, yeah, okay. Cool.
Alright, so yeah, then this is just looking for reviews at this point. We've got one, so really… Probably good, unless, I'd like to look at this, so… Yeah.
**Nikola Grcevski @ Grafana / OpenTelemetry** 33:42 Take a walk.
**Tyler Yahn (Splunk)** 33:44 Okay, then yeah, I'll definitely do that.
**Okay, moving on, yeah, here's the other two, and then… Nikola Grcevski @ Grafana / OpenTelemetry** 33:51 those, yeah.
**Tyler Yahn (Splunk)** 33:52 Yep.
Got another… I think a newer contributor?
**Nikola Grcevski @ Grafana / OpenTelemetry** 33:58 Oh, yeah, I have to look into this one, yeah.
**Tyler Yahn (Splunk)** 34:00 Oh yeah, yeah, yeah, it seems, like, just a fix.
Definitely a little bit of a bug. Looks like CI's failing out as well. But, yeah, I'll add you as an assignee, Nikola.
**Nikola Grcevski @ Grafana / OpenTelemetry** 34:12 I will take a look at this, this, yeah.
I think it was one of the issues that we had opened, that we should sign a check for incompatibilities, and I think he did it.
**Tyler Yahn (Splunk)** 34:21 Yeah, I think so. Oh yeah, there it is, yeah.
Perfect, okay.
Alright.
Back to the first page.
Rubik's, again, another work in progress, yep. Yep. This is for, the integration test, for moving the configuration integration test to the V2. One of the things I realized at the start was that it's, kind of shimming in this migration stuff for the config.
So this just makes all the tests, like, repeatable, and uses… uses, like, standard config, for the migration, so it doesn't plum in things, essentially, saying things like this, where… yeah, you're missing gRPC protocol by default, so, yeah.
This is just a cleanup of the config. It looks kind of like this, nothing… nothing too hard to… review. But essentially, without this, then the next PR… can't work, and the next PR is much larger, so, yeah.
Just needs a review.
Okay.
Keep OTCLP export compression default to make it configurable? Yeah, I took a look at this one. I don't… I think this is right, I think it's partly right. For those, I guess, who haven't taken a look at it, this is looking at, trying to fix the default compression. This, adds this option for the OT… essentially, it's a sophistication-defined configuration that we don't actually support here, which probably should. It also then goes… Actually, maybe it's been updated, before I say anything. No, it doesn't look like it. It also adds a bunch of, compression formats that are, like, not… Guaranteed to be supported by downstream. So, like, the OpenTelemetry Collector supports a bunch of, like, LZ2 and a bunch of other different compression formats.
Which is great, but there's no guarantee that a client can send those, and then there's no negotiation.
Between the client and the server. So, like, if we add a lot of these things, we're essentially adding a foot gun, saying that clients should be able to start sending compression types that It's not guaranteed the downstream… collector is able to support, so… I think there's parts of this PR that are worth including. I definitely think the compression stuff, needs to get pulled back. But, yeah.
Yeah, that's where that is. I haven't seen any response on this, though, so… Yeah.
Oh, there's… please take a look, though. I think there is some fixes here that we want to include, it's just we gotta detangle them.
**Nikola Grcevski @ Grafana / OpenTelemetry** 37:02 Interesting, yeah.
**Tyler Yahn (Splunk)** 37:04 Yeah.
**Nikola Grcevski @ Grafana / OpenTelemetry** 37:04 So, you mean, even if… So, I guess what you're saying is that a customer can… Can enable compression, but then… It's not supported by the collector, and they'll get a failure.
**Tyler Yahn (Splunk)** 37:17 Yeah, exactly. So, yeah, the specification specifically calls out Gzip and then none.
**Nikola Grcevski @ Grafana / OpenTelemetry** 37:23 Those are the two.
**Tyler Yahn (Splunk)** 37:23 supported compression types, but, like, yeah, say you use Snappy, and then, you know, you're gonna get a 400 from the, the gRPC server going, like, what is this? And then that's, like, a non-recoverable error, so then it's never gonna retry, and it's like, yeah, it's so… Okay.
**Nikola Grcevski @ Grafana / OpenTelemetry** 37:40 Maybe we should just do Giuseppe and none, right?
**Tyler Yahn (Splunk)** 37:43 I think that's the way to do it. Yeah, from the client side, we want to be conservative with what we're sending. I know the server side, like, the hotel collector itself supports all of these compression formats, which is probably where that list came from.
But there's no guarantee that, like, any third-party collectors, any, other OTLP endpoints in general are gonna support these formats. So, yeah, that's, I think, where we're gonna get into trouble if we do that, so yeah.
**Nikola Grcevski @ Grafana / OpenTelemetry** 38:06 Let's see.
**Tyler Yahn (Splunk)** 38:08 Yeah, if other folks think that that's wrong, I'm fine.
rethinking it, but I do… I want to be very cautious on this one, yeah.
**Nikola Grcevski @ Grafana / OpenTelemetry** 38:21 But if it's not the default, I guess you enable it, then it fails, and you're like, okay, well… maybe it's not the end of the world, I guess?
**Tyler Yahn (Splunk)** 38:28 Yeah, it's just that it… it… like, you turn it on, and then you just… the user's experience is they just don't get any telemetry coming out anymore, and they gotta go investigate, why? I guess it starts dropping?
**Nikola Grcevski @ Grafana / OpenTelemetry** 38:43 It's like…
**Tyler Yahn (Splunk)** 38:44 don't give that option. And, like, there's not really a big reason, like, I've heard LZ4 compression has definitely helped some folks, in reducing, like, network size and that kind of thing, but, like.
**Nikola Grcevski @ Grafana / OpenTelemetry** 38:55 Yeah.
I know that from… That's fair enough, yeah.
**Tyler Yahn (Splunk)** 38:58 Yeah, exactly, yeah, we're talking, like, you know, less than 10% at that point. And so… Yeah, it was… Nikola Grcevski @ Grafana / OpenTelemetry 39:05 Let's use Giuseppe and not… as a… It's an option, so… Yeah. And we can actually tell them if they try one or the other, says, no, we don't support any of those.
**Tyler Yahn (Splunk)** 39:16 Yeah.
**Nikola Grcevski @ Grafana / OpenTelemetry** 39:16 maybe they can just build… like, if you start saying, I want to use the compression.
but it's not GiZip, then we say, sorry, that's not supported by OB, because we consider the other ones not… broadly supported.
**Tyler Yahn (Splunk)** 39:30 Yeah, agreed. And I honestly, if we start getting those kinds of requests, we can maybe look into, you know, allowing this to be extended easily, or something like that, like, so they can do custom… yeah, but like… Yeah, and when that bridge comes, let's cross it, kind of thing, yeah.
Okay.
Cool. Clean up a little bit here. Where are we at?
Yes, here, preserve application transparency in HT, go HTTP2.
Yeah, I think this is the start of… I can't remember. There's a bunch of cleanup tasks as well, I'm sorry, I'm, like, a few PR is in the run.
Yeah.
**Nikola Grcevski @ Grafana / OpenTelemetry** 40:19 Yeah, easier to do, okay.
**Tyler Yahn (Splunk)** 40:20 Yeah, yeah, it needs a review. It definitely is a little bit of a larger one, it's kind of complex, but I think it's definitely worthwhile. Definitely, yeah.
It's helpful. So… Yeah, these are view.
**Nikola Grcevski @ Grafana / OpenTelemetry** 40:35 Hey, I mean, I guess you and Matt, I wanted to ask… If we… what's the status of the HTTP2 generic? We don't support dynamic tables, right?
Or an HVAC? Or do we know?
**Matt** 40:50 Dynamic tables, you mean, UFMAN-encoded headers?
**Nikola Grcevski @ Grafana / OpenTelemetry** 40:55 Yeah, so… so when the… when the transparent It's not obvious.
I guess.
When there's no… I guess what I'm trying to say is that there's no key, transparent. We don't do any sort of… Matching…
**Matt** 41:14 And the values right now, so… Nikola Grcevski @ Grafana / OpenTelemetry 41:15 Oh my goodness.
**Matt** 41:16 when we see… Oh, okay. Yeah.
and also UFMAN encoded values, but there are some, Some limitations also there on the length of something, I don't remember well.
But I won the two PRs, I guess, like, 2 or 3 weeks ago.
**Nikola Grcevski @ Grafana / OpenTelemetry** 41:34 Nice. I guess, so you're actually doing the… the pattern matching of a Huffman-encoded value that looks like a trace parent, and then try to decode it. Oh, man, that's awesome. Yeah. Okay, I… I think I saw some PR supply, and I just, didn't review, or wasn't… I didn't know if it was that, but that's awesome.
**Tyler Yahn (Splunk)** 41:57 No, it's… it's… it is pretty awesome.
**Nikola Grcevski @ Grafana / OpenTelemetry** 41:59 Mmm.
**Tyler Yahn (Splunk)** 42:01 I don't… there's… Yeah, Macias, I can't remember what the edge cases are, but, like.
It was… it was pretty well covered, actually. Like, it was… yeah, I'm trying to.
**Nikola Grcevski @ Grafana / OpenTelemetry** 42:10 No.
**Tyler Yahn (Splunk)** 42:10 But, Nikola Grcevski @ Grafana / OpenTelemetry 42:11 That is pretty… yeah, that covers a lot of cases. So that means that we can probably run the hotel demo and figure out if it's working.
**Tyler Yahn (Splunk)** 42:20 It… yeah, I think it does, yeah.
**Nikola Grcevski @ Grafana / OpenTelemetry** 42:23 Yeah? Okay. So I'll tell demo is all gRPCs, huh?
**Tyler Yahn (Splunk)** 42:27 Yep, yeah, exactly.
**Nikola Grcevski @ Grafana / OpenTelemetry** 42:28 and persistent connections.
Yeah.
Nice.
**Tyler Yahn (Splunk)** 42:34 Yeah, it should be really cool.
Similarly, I think, oh, no, this is the one I was thinking of. Yeah, this is actually the stacked, propagation for immediate writers. Yeah, this is the first in that, duplicate trace parent stuff, so essentially this is reducing… yeah, that's what it was.
Yeah, this is just… Should be straightforward, I think the tests are passing… yeah, Nikola is self-assigned. Okay, so, yeah.
Looks like it just needs reviews as well.
**Nikola Grcevski @ Grafana / OpenTelemetry** 43:05 Yep.
**Tyler Yahn (Splunk)** 43:08 Cool. Similar here, definitely needs the review on this. This is, again, having a save rollback on the SK message stuff, so I think this is another cleanup. I think it's a little bit more of a hardening PR, rather than, getting us towards the duplicate, trace resolution, but, like, yeah, this is… But I think worthwhile. It's not, I think, as much of a priority, but yeah.
Yeah, similar for this, also another cleanup, frame injection failsafe. Essentially, if you're not able to parse this, it pulls back to what it's already doing, and it doesn't try to guess, essentially, at that point, so… Yeah, I think that's, again, also just looking for reviews, looks like CS passing.
This one… yeah, Nikola, I did want to ask you about this one, so… This is the cleanup, that I had mentioned before. It looks like… I've pushed some fixes, but, like, it looks like you just opened another PR that was.
**Nikola Grcevski @ Grafana / OpenTelemetry** 44:11 Oh, okay, I missed it, okay, alright.
Cool.
**Tyler Yahn (Splunk)** 44:14 But yeah, I was just… I pushed this really quick right after. I'm guessing.
**Nikola Grcevski @ Grafana / OpenTelemetry** 44:18 Hi, yeah, okay, so let's go over yours. I'm gonna close mine,
**Tyler Yahn (Splunk)** 44:23 Well… Okay. Okay, yeah. We'll see if we can.
**Nikola Grcevski @ Grafana / OpenTelemetry** 44:27 I think I may have added just one more test.
**Tyler Yahn (Splunk)** 44:31 Okay, then if… actually, let's double check.
He added more, much more.
**Nikola Grcevski @ Grafana / OpenTelemetry** 44:42 And a little bit more tests. I mean, it's the same fix, but I just added more tests in two places, because even when the.
**Tyler Yahn (Splunk)** 44:49 Yeah, why don't we just go with this, then?
**Nikola Grcevski @ Grafana / OpenTelemetry** 44:51 Okay.
**Tyler Yahn (Splunk)** 44:52 It looks… yeah, like a super… okay.
**Nikola Grcevski @ Grafana / OpenTelemetry** 44:55 It's the same thing. I mean, it's just… yeah, but some unit tests are failing. Oh, that's yours, okay.
**Tyler Yahn (Splunk)** 45:00 Yeah.
**Nikola Grcevski @ Grafana / OpenTelemetry** 45:05 It's basically what you had there. I just needed that option there, I just added more tests. Okay.
**Tyler Yahn (Splunk)** 45:10 Yeah, exactly, yeah.
Okay, well then I will review yours.
**Nikola Grcevski @ Grafana / OpenTelemetry** 45:14 Sounds good.
**Tyler Yahn (Splunk)** 45:19 Cool. Add Aerospike server spans, this one, I think… Where are we at on this?
**Nikola Grcevski @ Grafana / OpenTelemetry** 45:28 And I think I asked for that one.
And a review of the service band DVs. So this is a follow-up.
**Tyler Yahn (Splunk)** 45:35 Yeah, correct.
**Giuseppe Ognibene (Coralogix)** 45:36 Yeah, you can approve it. I trust the guy.
**Tyler Yahn (Splunk)** 45:45 Cool, yeah, so, giuseppe, this is just looking for more reviews then, right?
**Giuseppe Ognibene (Coralogix)** 45:51 Yep.
**Tyler Yahn (Splunk)** 45:53 Okay.
Yeah.
**Giuseppe Ognibene (Coralogix)** 45:56 Okay.
**Tyler Yahn (Splunk)** 45:58 Declare span size metrics, we talked a little bit about this earlier.
This is now in the milestone. This looks like it just needs, more review.
No, no. I did review this, Yeah.
This looks like it needs to get updated with main, was what I was looking at yesterday. Nimrod, I don't know if you've taken a look at this?
**Nimrod Avni** 46:24 Probably not.
**Tyler Yahn (Splunk)** 46:27 Okay.
**Nimrod Avni** 46:29 I'll have a look soon.
**Tyler Yahn (Splunk)** 46:31 Okay, yeah, It looked good, I think it just needed some cleanup from what I saw that did land on main, but yeah, I think this looks great, yeah.
Okay.
Shoot, I'll get lost. Reject inverted ranges… yeah, I think this is where we're at next.
Yeah, this looked good. This is a newer contributor, I don't know if, Emmanuel's on the call, but yeah, I think this is just one of those things where we weren't checking the fact that, like, end is less than start, so we could have some pretty awkward ranges, that would pass through.
The only ask that I had was that this error is still, ignored, meaning that these values may be garbage, so I wanted to get that checked as well. But otherwise, yeah, this looked like it's good, ready for review as well.
**Nikola Grcevski @ Grafana / OpenTelemetry** 47:25 Nice.
**Tyler Yahn (Splunk)** 47:28 Okay, cool.
Emit… This is your queue, yeah, key metric, right?
This looks like it's just looking for review.
**Nikola Grcevski @ Grafana / OpenTelemetry** 47:43 Very.
**Nimrod Avni** 47:44 Yeah, it was… there's apparently some internal metric that's declared everywhere, but we just don't… like, we never wired it up to actually ports.
**Nikola Grcevski @ Grafana / OpenTelemetry** 47:54 populated.
**Nimrod Avni** 47:55 Yeah, so nothing actually populated.
**Tyler Yahn (Splunk)** 48:00 Yeah, alright, let's turn.
**Nikola Grcevski @ Grafana / OpenTelemetry** 48:01 Fair enough, yeah.
**Tyler Yahn (Splunk)** 48:05 Okay.
behind Java injections of stable process identities? Yeah, this is a follow-up to a PR that was, merged, yeah, 2949, where essentially, like, It was great, like, that, yeah, it added some validation process, in making sure that, like, what we're attaching to is the right Process, but it was using… the PID for the credential lookup. The problem is, is that, like, there's that edge case where, like, PIDs aren't necessarily going to be unique. If you have really quick churn, it's very much of an edge But it also is, like, one of those things where This is using the start timestamp as essentially a second check to make sure that, like, what we're actually injecting, is the correct thing, but it also has, like, a clean rollback.
was kind of the idea, so it makes the whole process atomic, and it won't, like, try to attach to a process, or a Java agent-like process. If it… if it has, like, these sort of failures, or it realizes that, like, afterwards the process has died. So, yeah, it does a lot of interesting locking, to try to get this, but it also is, like, just trying to make it atomic from, like, a programmatic standpoint as well, so… It's a cleanup, not a higher priority, but yeah, Nikola, I'm guessing you might be interested in looking at.
**Nikola Grcevski @ Grafana / OpenTelemetry** 49:21 Yeah, I'll take a lot, yeah.
**Tyler Yahn (Splunk)** 49:22 Yeah.
Cool.
Fixed config mapped code for YAML sequences for unmarshable types, I think this is good to go… no?
Hmm.
Actually, don't know if I saw this issue.
They opened it as well 13 hours ago.
**Nikola Grcevski @ Grafana / OpenTelemetry** 49:51 Collector receiver.
Interesting.
**Tyler Yahn (Splunk)** 49:56 Okay. Huh.
**Nikola Grcevski @ Grafana / OpenTelemetry** 49:58 Bye.
**Tyler Yahn (Splunk)** 50:00 Yeah… That's interesting.
Yeah, okay, well… Looks like it needs reviews. I'll try to take a look at this one. I don't know exactly.
Yeah, news to me, so… Cool.
Don't need to talk about it too much here.
fixed route K-Log output through S-Log. I think this is Steven. I saw this one come through my notifications this morning.
Just looks like it's needing a review then, I'm guessing, right, Steven?
**Stephen Lang (Raintank, Inc. – Grafana Labs)** 50:29 Yeah, yeah, it should be good to go. It's a fairly small change, it's just, we had blogs going in different formats to different streams, and this is to try and just bring them all into one place.
**Tyler Yahn (Splunk)** 50:40 Yeah, right. That's… I was super excited when I saw that title, so I was hoping that's exactly what it did. Yeah, sounds great.
Okay, I will take a look. Others, too.
At DB namespace, db client, and DB Server Operation Metrics.
**Nikola Grcevski @ Grafana / OpenTelemetry** 51:01 That's a good idea.
**Tyler Yahn (Splunk)** 51:02 Yeah.
Okay, yeah, just looking for a review, I'm guessing, on this one. Anything specific, Giuseppe?
**Giuseppe Ognibene (Coralogix)** 51:10 No, there will be some follow-ups, because we have some attributes that are conditional required, and we are not adding it.
So I'm just doing small PRs.
**Tyler Yahn (Splunk)** 51:26 Okay.
I gotcha.
Well, cool, yeah, alright.
This is definitely a good size PR, so yeah, take a look.
These are the other draft ones from Nimrod.
Talked a little bit about those.
**Nimrod Avni** 51:40 open pretty soon, just when CI finishes, and you should be ready to go.
**Tyler Yahn (Splunk)** 51:47 Yeah, I'm right there with ya.
**Nimrod Avni** 51:49 Loosely.
Yeah, same vein as, as, Giuseppe's, like.
Enhancing, compliance and, like, covering more stuff that we can kind of easily.
**Tyler Yahn (Splunk)** 52:00 Okay, yeah, perfect.
That looks good.
Okay, keep an eye out for those.
Macias, gotchaser support, nested spans, and shared contacts.
**Matt** 52:12 Yeah, this is the continuation of three previous PRs that were open.
I hope this, this will fix them all. So basically, this is the support for… since in Indigo Tracer, we set the shared context for every protocol, and not just HTTP, if it happens that more protocols are, are called… are set in a nested way.
when any of them exits, the… as of now, the whole context gets deleted. So this one, just, supports this nesting for all protocols.
there are a bunch of edge cases with… specifically with Go, with Go routines, so you start a Go routine, and then you start a context, and then you exit from there, and it's a bit of a mess, but this one should support most, most patterns. The only one that is not supported yet is the Panic Recover case, but that one needs different hooks.
it would increase the complexity a lot, so I prefer to have it as a follow-up.
**Nikola Grcevski @ Grafana / OpenTelemetry** 53:26 That's great.
**Tyler Yahn (Splunk)** 53:29 Yeah, this is really great.
Okay.
Yeah, cool, I'm already starting to review it, I should stop.
**Nikola Grcevski @ Grafana / OpenTelemetry** 53:35 Cool.
**Tyler Yahn (Splunk)** 53:36 Need some eyes on it.
Cool, we just talked about this one, this is… needs to review as well, just a follow-up fix.
For this new testing, giuseppe replaced disabled Kafka Fetch… Looks like there's an error here.
**Giuseppe Ognibene (Coralogix)** 53:56 Oh, I didn't see it.
It's probably lit up.
**Nikola Grcevski @ Grafana / OpenTelemetry** 54:00 I've failed, aren't you? Yeah.
**Tyler Yahn (Splunk)** 54:02 Oh, no, no, I'm sorry, the… I… oh, yeah, see, I probably failed, but I just meant you're addressing, oh, it's a to-do, yeah.
**Giuseppe Ognibene (Coralogix)** 54:11 Wow. I will, I will check the list.
**Tyler Yahn (Splunk)** 54:13 Yeah, yeah, I'm guessing it's probably just… Flakiness, but… Yeah. Sure. Yeah.
Okay, but, more of you, please take a look at this one.
Hotelbot… Yeah, that looks like it's… I don't know why that's a draft, but interesting. Take a look at that when it comes out. And add JVM class thread, CPU, runtime metrics, mark, this is something just opened as well.
**Marc Tudurí** 54:43 Yeah, this is just to add, like, the rest of runtime metrics for… well, not the rest, but almost the rest of runtime metrics for JVN that cannot be obtained with USDT.
**So it works similar to the… Node.js, runtime metrics that Giuseppe added. It has… This tiny agent, and then… Nikola Grcevski @ Grafana / OpenTelemetry** 55:06 Oh, nice.
**Marc Tudurí** 55:06 Yeah. Yeah.
**Tyler Yahn (Splunk)** 55:07 Yeah, yeah.
Cool.
**Marc Tudurí** 55:09 And then it… and then it fetches in BPM.
**Nikola Grcevski @ Grafana / OpenTelemetry** 55:14 That's awesome, alright?
**Marc Tudurí** 55:16 Yep.
**Tyler Yahn (Splunk)** 55:19 Yeah, that is awesome. Okay, looks like in his review.
**Marc Tudurí** 55:22 Also, like, a benchmark there, because, with Nikola, we discussed about this, that it could be… Very expensive, to enable, so just… Nikola Grcevski @ Grafana / OpenTelemetry 55:32 Oh, nice, okay.
**Marc Tudurí** 55:34 I don't know.
**Nikola Grcevski @ Grafana / OpenTelemetry** 55:35 That sounds pretty small.
**Marc Tudurí** 55:37 Yeah, yeah, yeah.
**Nikola Grcevski @ Grafana / OpenTelemetry** 55:41 Cool. What's the default sampling interval?
Oh, one second, yeah, so it's nothing, yeah.
**Marc Tudurí** 55:46 We can't change it, but, since we are sharing… Nikola Grcevski @ Grafana / OpenTelemetry 55:50 Yeah, true.
**Marc Tudurí** 55:50 Same parameter with the other one, but… Nikola Grcevski @ Grafana / OpenTelemetry 55:52 Yeah, that's good.
**Marc Tudurí** 55:54 And Giuseppe added also one second for… OJS, so… Nikola Grcevski @ Grafana / OpenTelemetry 55:58 Yeah, that makes sense. Yeah, one second is pretty good.
Yeah.
**Tyler Yahn (Splunk)** 56:05 Okay, cool.
Oh… Take a look at this.
Double-check the agenda. Doesn't look like there's anything else added. So, that's the end of the agenda. We're coming up right on time, about 5 minutes left. Any other announcements or things that people wanted to bring up?
Before we end it.
Well, cool, yeah, a lot in progress. Thanks all for the hard work, definitely a lot that's gone into the past week or two, so yeah, definitely worth, calling out. Definitely appreciated.
**Well, cool, awesome. Well, if that's the case, let's send the meeting here. Thanks all for joining, and Nikola Grcevski @ Grafana / OpenTelemetry** 56:47 I just wanted to bring up, most Grafanistas will not be… being here next week. We have a company-wide event, so we're not here.
**Tyler Yahn (Splunk)** 56:55 Let's make some really important decisions next week, then.
**Nikola Grcevski @ Grafana / OpenTelemetry** 56:59 Rewrite the… rewrite the code in Rust.
**Tyler Yahn (Splunk)** 57:02 Yeah, yeah, obviously.
**Stephen Lang (Raintank, Inc. – Grafana Labs)** 57:04 Yeah, Nikola.
**Nikola Grcevski @ Grafana / OpenTelemetry** 57:05 Oh, yes, yes, Steven is… Steven is not joining us.
**Tyler Yahn (Splunk)** 57:09 Okay, cool. Alright, yeah, thanks for the heads up. So, yeah.
We'll… we'll understand that one.
Well, cool, alright. Well then, we'll see most of you all next week, the others, in two weeks. But yeah, until then.

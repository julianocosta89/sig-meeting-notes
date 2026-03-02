SIG: Client Instrumentation SIG
Date: 2025-09-16
Duration: 31 minutes
Zoom Recording URL: https://zoom.us/rec/share/0AFpw_edFhRBV8ANpAxOzByfZSPg4xATlE9xKgk41lBV6memIc3_DmGYCEuCG3lE.2-bApwVLedfkHgFn
============================================================

## Zoom Recording Transcript

**Hanson Ho** 01:27 Hello.
**Leonardo Serrano** 01:32 Hello?
**Jason Plumb** 01:33 Why is there a huge warning at the top of the dock? Who did that?
**Hanson Ho** 01:41 It should be editable, because…
**Jason Plumb** 01:44 Do we know who added that?
**Hanson Ho** 01:50 I have no idea. We could probably check the history and stuff, but it could be anonymous.
**Jason Plumb** 01:56 say anonymous bozo, yeah. I wonder if somebody was, like, thinking that maybe the top of the document shouldn't be editable or something, but…
**Hanson Ho** 02:05 I don't care.
**Jason Plumb** 02:07 Delete it. Delete it. Get rid of it.
**Hanson Ho** 02:11 It should be editable, and .
**Jason Plumb** 02:13 Yeah, the community projects.
**Hanson Ho** 02:14 Yeah.
If someone wants to come here and vandalize it, then…
**Jason Plumb** 02:18 Going to, yeah.
**Hanson Ho** 02:19 Yeah.
**Jason Plumb** 02:21 And then we'll go back to the history, or make a new doc, or whatever, like, yeah, okay. But I mean, I… I mean, the concept, if someone's trying to be helpful, that's fine, but… No, no, it… What I don't think should be up here is just a random date. There we go, okay.
**Hanson Ho** 02:35 Let's see… okay. So, Martin can't attend. I will, I will present, I guess.
**Jason Plumb** 02:51 I appreciate that, Hanson.
**Hanson Ho** 02:53 Yeah, we did it for an hour, so that's only fair.
Alright.
**Jason Plumb** 03:03 Hi, Dan.
**Hanson Ho** 03:04 Yeah.
**Dan Gomez Blanco** 03:06 Hololo.
**Hanson Ho** 03:09 Who's here?
You asking?
Jason's here twice.
**Jason Plumb** 03:16 Damn.
**Hanson Ho** 03:17 Please add your names.
What the heck?
**Jason Plumb** 03:28 Did you copy the agenda from last time?
**Hanson Ho** 03:29 I did, I'm just… I was just trying to…
**Jason Plumb** 03:31 That's why I was confused. I was like, how's our agenda this morning?
**Hanson Ho** 03:33 It's so full,
I guess I'm gonna put Jamie on the spot.
And he can talk about… Kotlin API SDK donation proposal.
If you want me to talk to JV, just let me know.
**Jamie Lynch** 04:02 You want me to spot now?
**Hanson Ho** 04:05 Yeah, yeah, as Leonardo and others fill in the rest of the topic, yeah, why don't you kick us off, Jamie? We're already 4 minutes in, so…
**Jamie Lynch** 04:13 Cool. Yeah, so for folks who don't know, Embassa's been working on a Kotlin API and implementation of the OpenTelemetry spec.
We've submitted a proposal to donate that now. So…
Yeah, Hanson, did you have, like, anything specific you wanted to…
**Hanson Ho** 04:37 I think, go and check it out. If you have, if you work on Android, you have colleagues who work on Android, especially multiplatform, please check it out. We're looking for contributors, reviewers, anybody who can kind of give feedback, as we go through this process,
before and after donation as well, kind of just want to, you know, put it in the agenda, kind of spread it up a little bit for those who are not, like, on the Slack or, you know. But yeah, an FYI that this has got to a place that is ready for further review.
**Dan Gomez Blanco** 05:19 Cute.
**Hanson Ho** 05:20 Alright.
Next is… Leonardo, Performance SLAs.
**Leonardo Serrano** 05:29 Yeah, yeah, so,
Something I wanted to get some thoughts on… I don't know if, the community here has any thoughts on, like, SLAs for app startup, additional latency, memory utilization, and I think a big one is,
actually one I didn't list here, network bandwidth for the SDKs, in terms of, like, the…
Android and iOS clients.
It's kind of a broad question, but… I guess, do folks have…
Okay, I'll start with, are there any SLAs? I think the answer's no. Second question will be, should there be, and how can we actually, you know.
Make the decision on what is, like.
I don't know, for app startup, like, you know, any additional app startup latency that the clients introduce.
What should be the magic number that we decide upon?
**Jason Plumb** 06:29 Oh, you're referring to SLAs for instrumentation itself?
**Leonardo Serrano** 06:34 Yeah, yeah, yeah.
**Jason Plumb** 06:35 Okay, I think we should call that out.
**Leonardo Serrano** 06:37 Oh, yeah, good point, good point.
**Jason Plumb** 06:40 Because startup time is different than startup time…
Delays caused by instrumentation or whatever.
**Hanson Ho** 06:48 So… Typically, it's hard to benchmark this kind of stuff, because the runtime environment is so diverse.
In terms of devices, in terms of use cases. So, like, the word SLA implies that, you know, violations are bad.
I think it would be good if we have some sort of benchmark published in terms of additional, latency and things like that that gets introduced for the various packages, on some benchmark device.
**Jason Plumb** 07:20 Bye.
I might respectfully disagree with that.
Because I think benchmarks… I mean, I agree with your first point, I think the benchmark can give people a false sense of security, or send the wrong message, set up expectations around certain numbers, or performance numbers, or overhead numbers that, I think are unrealistic.
**Hanson Ho** 07:40 Yeah, well, yes. So, I mean, if we ever do this, it would be very much as, these are unrealistic, don't expect this in production. I think that's almost implied. But it would be, like, if someone comes in here and says, hey, if I drop this in.
roughly how much, should I expect overhead to be? And, you know, 10 milliseconds is very different than 1 second. I think giving them, like, a range, not even a range, just like, given this device, it takes this much with these features, it would be something nice to have, kind of thing. But, I would say it…
You know, many things are nice to have that, you know, are unlikely to be, you know.
done, unless someone's really passionate about it. But things like memory and CPU is also difficult to calculate, because different devices,
provision resources differently under different conditions. So, I would say you may be able to do something like that with, like, additional start latency, given some sample app, but memory and CPU is going to be all over the place. So, I wouldn't even… I would even consider benchmarks, you know, for that.
**Dan Gomez Blanco** 08:46 That's interesting.
**Hanson Ho** 08:47 Yeah, TLDR, the mobile space, especially when we're dealing with a library, these things are going to be very much, in flux.
**Dan Gomez Blanco** 08:58 That's interesting, there was a discussion on the browser sig as well, about…
Well, not benchmarks on performance, but on bundle size, and then basically have, you know.
you can, you know, you can integrate that into your CI, right, to ensure that, you know, you don't go over a specific
So a change doesn't introduce, you know.
Massive change in bundle size.
I know close to nothing about mobile, development. If, you know, if these would be…
things. If there is something that one can look at to say, well, you know, we've got this as a…
As a benchmark, and are we deviating a lot from it?
Maybe not automated, but something… Tune in.
**Jason Plumb** 09:42 I think that's the only real benefit of having these kinds of numbers, is to look for regressions. Like, on a given platform with a given configuration.
version to version, are you regressing or making things considerably worse? Like, that's the… kind of the only benefit to having these numbers, because they are so dependent on
all of the variables, right? Like, what device you're on, what operating system, what version, what configuration, what features you're using, like, it's really hard to dial in this stuff.
I'm curious to hear where the question comes from, Leonardo. Are you having other people, like users, ask about this stuff?
**Leonardo Serrano** 10:17 Yes, yes. So, specifically,
you know, we've been trying to get some users to try to use, like, our bundle for the, Android client, Android implementation, and they have a… so…
This is the first time we've heard, but they have, like, a very tight SLA on,
additional application startup latencies. So, you know, whenever they want to evaluate whether or not they are able to pull in this dependency on their application, they…
judge it based on whether or not it will increase their app start latency by X milliseconds, or X percent, given this, like, test environment. Like, they have their own dedicated, like.
device, they run this test, and if it's greater than their, you know, SLA or their tolerable increase in latency, then they just don't use the library. So…
you know, we ran into this case and kind of don't really have a good answer for these people.
**Jason Plumb** 11:20 Yeah.
**Hanson Ho** 11:21 So, folks who have those types of requirements kind of have to do the test themselves, because their environment is very bespoke.
in terms of the sample app, or the app that they have, in terms of the device that they're testing on, in terms of the environment, and how much load it's, you know, preset. So even if we have numbers for our kind of bespoke environment, it just gives a rough
idea, and it seems like they want something more precise than a rough idea would, would give them. So, what I would encourage, them to do is just drop it in and see, because we could never tell. I mean, the best we could do is add some macro benchmark tests.
That folks could run. But of course, they also have to know
like, to lock their environment appropriately to get results that are appropriate. So, you know, I think I'm flip-flopping a little bit, you know, and agreeing with what Jason's saying, that there may be so many qualifiers to this that it may not be worth doing.
But if… but for sure, if your customer's restrictions are so tight, and their SLA is very specific for their app, then there's only one thing they could do, which is test it themselves, because…
what you run on an Android Go phone from, you know, 2017, running Android 9 Go, is very different than, you know, a Pixel 9 Pro.
So, what are you benchmarking for? Well, it depends what your customer base is, right? If everybody uses crap phones, then you care about those people more. If everybody uses good phones, you care about those people more, so…
**Jason Plumb** 13:00 Yeah, what I think might be helpful for the community, Leonardo, is to hear what these numbers are. So if you have teams that are like, if it increases startup latency by more than 3% on this phone in this configuration, then we can't use it. I think for the community to know what those numbers are for your user base would be, like, super helpful.
**Leonardo Serrano** 13:21 Yeah, yeah, I'll get back to you if I'm able to share those numbers.
**Jason Plumb** 13:23 school.
**Leonardo Serrano** 13:24 It's something, honestly, it's something that sounds super, super arbitrary, like, you know.
**Jason Plumb** 13:30 Yeah.
**Leonardo Serrano** 13:31 Don't increase it by 3% for any of our devices, which seems a bit…
**Jason Plumb** 13:35 Oh, percent.
**Leonardo Serrano** 13:36 Yeah.
**Jason Plumb** 13:36 Okay, that's cool. Yeah, percentage. I have a talk on this topic, by the way, like, it really…
It's been a… it's been a hot… a hot button for me for a long time, so I'm trying not to go… if you haven't seen it, I can… I can share it with you.
**Leonardo Serrano** 13:50 Yeah, please, by all means.
**Jason Plumb** 13:51 Okay.
**Hanson Ho** 13:53 Having done this as well, and been part of the evaluation team, it's really about how much value you think it brings versus how much cost… it's always a cost-benefit analysis, so having very strict numbers-based things is…
You know, good try, but you're gonna have exceptions all the time, so…
But they need to test it at the end of the day, is kind of…
**Leonardo Serrano** 14:16 Makes sense. I think all we could do is just get some figures for maybe, like, the most common top-end devices.
Per plat… per platform, and… But yeah, that also seems kind of, like, not super helpful.
**Hanson Ho** 14:30 like, if I can, like, snap a finger and get this done, because the problem with this is, it's not like I write some code and it's there. There's a lot of meticulous, kind of, tuning and making sure things get updated and things like that.
If I were, you know, magically snap my fingers to get this to work, I think a mid-tier, a high-end, and a low-end phone with some
features that we expect, to be on by default, on a relatively non,
relatively non, testy kind of app, like a real, real application. That would be nice, to be able to, have that as, like, you know, a gauge. But, you know, the qualifications we have to say is don't take these as real numbers.
Because these, you know, these are synthetic, and blah blah blah, and… but again, it'll take…
a decent amount of work to get this automated and spun up and done for each release, or require manual work, both of which is work, so…
**Leonardo Serrano** 15:29 Makes sense. Got it. Okay, cool. I think I have my answers.
**Hanson Ho** 15:34 I read Jason's paper, which I should do myself.
**Leonardo Serrano** 15:37 Oh, yes.
Thank you, Jason.
**Jason Plumb** 15:41 Yeah, I put a link to the… to the YouTube video as well from KubeCon. Yeah.
This meeting is so short now, and we're not gonna get to Dan's topic.
**Hanson Ho** 15:55 Well, let's, let's try. Leonardo has a third one. Client tracing. Tracing and expansion sessions, okay.
**Leonardo Serrano** 16:02 Yeah, yeah, so I know we've been harping about this for a while,
I have a different idea to propose, and I'd just like to quickly get some temperature on this. So, the whole issue, for those who haven't been around when I've been repeatedly talking about this in previous things,
TLDR here is that, you want some way, in either, like, you know.
I don't know, the current default ways we can visualize traces,
we want some way to kind of group all our traces, or spans, by sessions, you know, without needing a totally different, like, way of doing that aggregation. So right now, you can view
We have different, like, programs that let you view, traces, you know, blanking on some names, but you guys know them, you guys use them.
**Jason Plumb** 16:59 Jaeger.
**Leonardo Serrano** 17:00 Jaeger, yeah, that's the big one. And certainly, you can build something, that can do some grouping and visualization on sessions, but that kind of… it starts to deviate from, like, the conventional OpenTelemetry,
behavior, I suppose, that's the right way to explain it. So, one proposal that I have, actually, I've had several in the past, but…
Trace linking, so…
Trace linking is a way that we could use to organize spans in a session without having to create a single long-running parent span. I don't know if anyone's evaluated this before, but I just wanted to get some temperature to…
there are some open questions, like, trace linking is, I believe, I haven't, like, experimented with this just yet,
But I believe it is specifically a span-to-trace linking, not a trace-to-trace linking. So the open… there's an open question of, like, how do you know, you know, what span to link to what trace, how much, like, you know, for our, instrumentation.
How much overhead is there going to be in, you know, keeping Stateful track of, like.
previous traces, or trace IDs, or span IDs that pertain to X session ID,
But yeah, that's… that's my proposal, in a nutshell. I wish I had a more formal doc to, like, share, but that's all I have right now.
**Hanson Ho** 18:40 So a span link links to a span, actually, not to a trace, so it could be part of the same trace, it could be, it could be another trace, it could be just an ID that doesn't really exist.
So that's definitely a way of doing it. But if the goal is to get a visualization, happening, I don't know how well
and I'm sure others will be able to comment better than me, how well span links are supported in generic visualization of a distributed trace, which is what all those UIs are for. It's for a distributed trace.
Versus the way we're using spans on the client is very much not like a distributed trace. So, I'm worried there's a bit of a trying to cram this and annotate this with metadata so we can reuse existing
tooling, to visualize this, rather than
you know, advocate for generic tooling that actually looks at this for what it is. I know which is, you know, not what you probably want to do to spin something up from the ground and get this going, but rather to use existing tooling for this. But.
**Dan Gomez Blanco** 19:53 Damn.
**Hanson Ho** 19:54 Yeah, I'd like to hear what… how well span links are supported in generic, visualization tools.
**Dan Gomez Blanco** 20:00 I agree. I think, at least the, you know, what I've seen in terms of supporting span links tends to be a… so, like, a cause relationship of, like, from two, rather than, like, all these things are linked together. Like, you… you have, like, span, you know, when…
It relies on that fact that…
It's not all these traces are part of a common session, but rather, you know, you're looking at a trace, and there's a span in that, and you're linking to another span, maybe in another trace.
But, like, there is a causal relationship there between one and the other.
So I agree with Hanson in terms of, like, and this is probably what the discussion about…
session, right? How do we represent sessions, and the concept of…
I guess what the entity SEG is working on to allow for…
resource attributes to be… or non-identifiable resource attributes to be modifiable, and so on. I guess, yeah, I would probably argue the same. That it's more about, like.
It's a higher level.
Constructs and a trace that can be represented via some type of, like.
Modifiable resource attribute in the future, but right now, it would be… Part of the attributes of… of.
Over span, right?
Not sure if…
That answers the question, but I think, you know, there's probably something that is worth exploring with the session.
Recession stabilization, right?
**Hanson Ho** 21:37 No, no, no.
I think, Leonardo, if you want to just, like, code this out and see what it looks like in the existing tooling, that's a fine experiment, because I think what I'm proposing is… is not… probably not very satisfactory. You know, build something from scratch that interprets this data in a slightly different way. So if the idea is just to get something that's slightly better than what it is right now, it…
Oh, Jason?
**Jason Plumb** 22:01 Oh, sorry, I was just gonna wait for you to finish your thought, Bill.
The one thing that span links also don't account for is being able to have logs and events in the same…
In the same view… viewport, like, to see those alongside of, or on top of.
Other operations, like, that… that solution doesn't account for that.
**Leonardo Serrano** 22:21 Yeah, it doesn't. Yeah, this so far is just solving for spans, which… So far?
It's good enough, but yeah, that's a totally separate thing.
**Hanson Ho** 22:34 So I think there's probably two steps here. One is try this out yourself, see if it actually solves your problem. If it does, then maybe there's something you can propose, even if it's just, like, a recommendation of usage. Hey, if you want to use generic open source visualization tooling.
annotate this way. It may not be official semantic convention, but, you know, it is… it is a usable way to get around existing issues until, you know, this is better supported. Because I do feel that, session-based,
telemetry visualization, in a generic way, is extremely useful, and someone should be building it. That is not, like, a vendor. Like, you know, I think vendors have it, but, you know,
But…
you know, nothing… you just, you know, get off the open source world and deploy on your own. So I think that's a big miss, but until we actually codify what sessions mean and things like that, there's nothing to build against. So I do understand the hesitation of folks spending time on that, but…
Hopefully we'll get there soon.
**Leonardo Serrano** 23:44 Makes sense. Okay, thanks.
**Hanson Ho** 23:49 Dan?
**Dan Gomez Blanco** 23:50 Right, can I share my screen? So I think I wanted to talk about the work-in-progress OpenTelemetry roadmap.
And also, basically, start the topic of
the client instrumentation project that's still there, basically, in the list of projects. So what you see here is, like, something that I've been working on to represent the OpenTelemetry roadmap as a roadmap of
Who doesn't love Gantt charts, right?
**Jason Plumb** 24:21 I don't. I know.
**Dan Gomez Blanco** 24:25 But it's like, you know, basically what we had in the community. These… these projects are the projects that are currently active in the community. That means those projects are approved by the GC, that have been… have a TC sponsors. It's a long process, let's say, to come up with… with that, with the logistics for that. Well, hopefully we're trying to stream… streamline it, but still.
You know, a bit of,
Bit of a longer process for some of the…
tight… tighter scope projects that we'd like to do. So, at the moment, and this only represents that, some of them, as you can see here.
the client instrumentation one. So these, by the way, these are issues in the roadmap.
repo. There's roadmap repo, those issues basically are synced from… they're basically not meant to be used as something to… to…
to actively… This was created by me, but, but now there's a bot that does it.
Or that syncs, all this. So all these issues are just basically automatically synced to whatever is in the project itself. So if you open a project.
And this is what we've got in the board of the Client Instrumentation project.
Mmm…
this basically was off track, and then this is how… this is part of the reason why the browser SIG was created, and now basically we've got another project for browser that will have, basically a list of… basically all this… all those issues that are in that roadmap.
repo. They're just there, too, so you can put them in a…
in a Gantt view, basically. There's nothing… if GitHub comes up with a way of showing a list of projects.
of GitHub projects like this one, in a same way, without us having to create issues and sync them, then that's great. But for now, that's what we've got. So…
And in terms of this one.
I just wanted to get a feel for, you know, Do we want to…
Close that project, and start a new one, that client side.
Mmm…
with, you know, some of the, for example, I know that this is something that page view event instrumentation, this is something that's now being handled by the browser sig, page navigation timing, all these things are here, and basically start to put together
Some of the things that we want to tackle, perhaps in a… in another…
like, shorter scope. Now, on that, and I know I'm conscious of time.
If there is a new… there's some new guidance as well.
for how do SIGs, GitHub projects, and the OpenTelemetry roadmap relate to each other. Recommend you have a read of this if you want.
what we want to do is we want to create an easier way for any SIG to…
let's say, bubble up things to the roadmap, right? So you've got something that is important to you, that you want to say, hey, as a SIG, we're going to be doing this, we're ready and established SIG, we don't need, sort of like TC sponsor, you know, we've already got a sponsor, GC liaison and all that, we just want to…
advertised that we're doing something else. So if you go into 6.yaml, anyone could create a project and add it here, as a, you know, this SIG, for example.
Sampling sake, this… they're focusing on this project, you can have a list of them, right?
So it doesn't require… a full-on… projects.
like these ones, if there is a smaller scope that a particular SIG wants to… or two or three SIGs that are currently existing want to focus on, as long as they're currently staffed, and basically, they just have a… something that they want to focus on. However, we do require a project
Proposal for the things that are called out
here, which is non-trivial changes to the specification, non-trivial changes to semantic conventions, a new SIG being formed, or an existing sync taking more work that will affect the project as a whole. So, I guess, what I wanted to find out is, one, would people be okay if we
Let's say, archive that client-side repo, call it, you know, close it, that particular project, and then we think about…
what… What next to focus on.
Which could be…
Focusing on session, focusing on, you know, something like that, and then try to get a few
Tasks on the… on a… on a project that are very, you know, scoped to that thing.
M…
**Jason Plumb** 28:59 I support closing that board.
**Hanson Ho** 29:01 Me too. I mean, anything that we would… we would be doing aren't… isn't going to be instrumentation, per se. It's more going to be, like, some… a bit more cross-client platform. So, yeah, the name is… is wrong, and I don't think we should backdoor our stuff into… to what was meant to be that, so…
**Dan Gomez Blanco** 29:20 Yeah. Cool, awesome. Because there is a, there is a, something that's been happening in the project as well as,
These projects never being closed.
And then, sort of like, you know, basically just continuing as a sync. We don't need a, you know, a project there for that. Right, so we'll close that, and then we… we can then maybe async, decide, you know.
If it is a…
a project board that we can put together. That's all, that's all that's needed, basically. A project board.
**Jason Plumb** 29:46 Yep.
**Dan Gomez Blanco** 29:46 With some tasks, and then…
**Jason Plumb** 29:48 Dan, sorry to jump in, are you the… are you kind of acting as liaison between the WebSig, the BrowserSig, rather, and this meeting, or are we just… do we have any representation for BrowserSig here today?
**Dan Gomez Blanco** 29:59 not today. I mean, I'm the liaison for both, for the purposes.
**Jason Plumb** 30:04 Okay.
**Dan Gomez Blanco** 30:04 Yes, yeah, like, that would be…
**Jason Plumb** 30:06 So it's you, but that, yeah, that would be cool to, like, make sure that we have that. That it's not… I mean, they're off doing their important thing, but I don't want us to feel isolated, and this is also very Android-heavy now, so I want to keep that.
**Dan Gomez Blanco** 30:16 I will join… I always normally join, I'll join on Thursday and say the same thing, so…
**Jason Plumb** 30:21 Hansen's been joining over there too, right?
In… in…
**Hanson Ho** 30:24 The browser? No.
**Jason Plumb** 30:26 Okay, okay.
**Hanson Ho** 30:27 Martin should be here. Martin's just sick today, so Martin couldn't come, but Martin should be here.
**Jason Plumb** 30:31 Okay.
**Dan Gomez Blanco** 30:32 I'm happy to, you know, that's what liaison means, right? Happy to, like, be between both, yeah.
**Hanson Ho** 30:39 You know…
**Jason Plumb** 30:40 speak French?
**Hanson Ho** 30:41 Oh, yeah.
**Jason Plumb** 30:42 you know.
**Hanson Ho** 30:43 You're American. We are over time, Grace. Sorry, we don't have time to… So, something you want to quickly, 30 seconds, talk about, and then we can take it up on Slack, or do it in two weeks?
**Grace Lim** 30:56 No, let me do it offline on Slack, and I also plan on joining BrowserSig anyway, so it should be good.
**Hanson Ho** 31:03 Okay. Thank you. Thanks, everyone.
**Dan Gomez Blanco** 31:06 Let's talk.
**Leonardo Serrano** 31:08 Thank you.

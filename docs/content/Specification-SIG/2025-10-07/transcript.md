SIG: Specification SIG
Date: 2025-10-07
Duration: 37 minutes
Zoom Recording URL: https://zoom.us/rec/share/FW_dO9fV-0OtekUTjHB4R0mspCMX03PuQkzkW5YjtL9uwRHVqUhXIh4f2xx_hc7H.2ig_htN8wKT13wxy
============================================================

## Zoom Recording Transcript

**Austin Parker** 01:16 Lo, low…
**Antoine Toulme** 01:22 Justin.
**Tigran Najaryan** 01:23 Hey, everyone.
**Antoine Toulme** 01:25 I do.
**Tigran Najaryan** 02:20 Am I sharing the right talk, guys?
**Austin Parker** 02:23 Yeah.
**Tigran Najaryan** 02:24 The meeting notes? Yeah. Okay.
I'll just give everyone a minute to join, and we can start.
Let me open this first item.
I'm not sure I recognize the GitHub handle.
-Oh.
**Mladjan Gadzic** 03:58 Is the person who submitted this here, I'm not sure who that is. That's me, I can just say a few words about myself. So, I'm Lajan, I am working for Gree Research company based in the UK, and I'm part of their open source department.
G-research is having a lot of troubles with visibility.
for traces, specifically spans, for long-lasting jobs. We have jobs that last for a few days, and at some point, we don't know if job crashed or something happened, so we need to check into that and see what is going on.
And, we had a proposal for SDKs for this before, but it seems that community is not interested in that, and is more interesting in long-term solution and spec change, which, of course, makes sense, and I'm here with, proposal for, or solution for this kind of issue, where visibility is not really great, and you don't know when process died, and no span is exported because of that. So, the idea that we came to is to have something called partial trace connector.
Basically, the idea is that SDK… SDKs would periodically export spans at some defined intervals.
where exactly that could be, defined, that's up to the implementation or specification detail at this point, but the idea is that SDK would export span, that are, still running, so not only when it's completed, and then if the end time is specified or not specified, that's when the connector takes place and does its magic. So, if no time is specified, connector would store this Spans, or traces locally.
And, that would not, affect Other part of the pipeline, but if the end time is specified, it will just forward the span through the rest of the pipeline.
I would just like to hear your opinion, if you have any, or, Give me some kind of an idea what would be next steps for this?
Because we want to have this, you know, long.
Therm done, not only just as a workaround for something, because so far we had a lot of workarounds for these things.
That's it.
**Austin Parker** 06:57 Hi, yeah, thanks for the proposal. So, I see on the discussion, someone Pointed you towards the semantic events for span lifecycle?
Did you review those?
**Mladjan Gadzic** 07:18 Yeah, I… I have, it's just that there… an idea was to actually join this meeting as well, and, see what people from the community thinks as well, so, yeah.
**Austin Parker** 07:31 Did… does the solution… does… does this seem like it would work for you?
**Mladjan Gadzic** 07:38 In… In our use case, it would both, for the greatest good, for the whole community, I'm not sure, so that's why I wanted to check a few more opinions on this.
**Austin Parker** 07:54 Yeah, one just general challenge with the… the thing you specified here is, and correct me if I'm wrong.
But I'm gonna summarize what I'm reading. You have a… Something running, a stateful collector that is receiving these, partial events, and… Is holding them in… Memory until either… you get a timeout, or until this fan finishes? Is that…
**Mladjan Gadzic** 08:36 Yeah, more or less, yeah, yeah.
**Austin Parker** 08:39 Yeah.
So, the problem I see is this periodic export of in-process spans, because no database… most all databases that I'm aware of, for spans especially, don't support updates. And, nobody, as far as I know, has deduplication logic for what happens if I receive a colliding Trace ID span ID.
I think that's probably too baked into consumer assumptions for us to, ever… Have something that… to ever have an upstream component that says, like, oh, this is gonna re-export the same span again?
Just because I have very little confidence that consumers would actually make the necessary updates, at least now. Like, maybe in the future.
But the idea with the semantic events for spans is supposed to address this by… giving people… by giving consumers a side-channel way to get the same information, since events don't have durations and are kind of instant like that. So… I see Josh has his hand up, so I'll… I'll let Josh… Continue.
**Josh Suereth** 10:05 Yeah, can you hear me? I… unfortunately, my microphone isn't working, so I'm using my phone. Is this audible?
**Reiley** 10:11 Thank you.
**Josh Suereth** 10:12 Great. So I think… I just want to say generally, like, one of the challenges that… that I personally have been looking at, because we've been running into the issue, is what happens when we crash?
Right? When a process is failing.
What does observability look like then? I think you're running into this, where, you know, is the data getting off the process as quickly as it possibly can? Are we able to observe what happened during the crash? And what happens to all the things that were in a queue waiting to be sent via OCLP?
Right. I have a project I've been toying with. You can see this OTLP MMAP thing, where we actually have a file that has a ring buffer where you fling events onto.
I've recently been experimenting with throwing span start, span end in there. So the idea would be that this is a file that gets things off the SDK as quickly as possible.
And then some collector can reconstruct the span model, as is, in OTLP, and fire it off.
I… I want to call out, I think your… the problem you have is real, and something we should start looking into. The ability to see, like, in-flight spans, I'm totally a fan of. If you need something right now, I do think this semantic event thing is a good way to go. Have a span processor that will fire out events, so you can see what's happening live.
I do think we have a longer-term play that we want to do here around, like, what would be the healthiest thing to do for OpenTelemetry? You know, how do we make sure During the crash of a process, we are getting the observability we need.
Right? So this is, techniques we've had in the past about, you know, pre-allocating things, making sure things are off process as quickly as possible, all kinds of fun. That is a big, broad discussion.
Hopefully… so, so, but I think it's one that we should continue to have.
It's just, it's not, like, top priority in OpenTelemetry right now, which I think is what you're seeing.
Anyway, to re-emphasize what I was just saying and recap it quickly, I agree with you, this is a problem that needs to be addressed.
I think you see and you've heard that this is not a top priority in OpenTelemetry at the moment, and something that if you want to make progress on, I think there are ways that you can make progress now.
And I think you need a solution today for your users, and I think having events and a span processor that fires events out quickly is probably your best bet in today's OpenTelemetry world.
And I think we could actually greenlight these things going forward.
But also, if we want to actually start thinking about how to architect these things, in the long run.
To have alternative solutions that might not be friendly to all languages, but at least give us better, you know, crash style observability in some languages, I'm personally more than amenable in kind of driving that direction. I see it's on a hand, so I don't want to monopolize the microphone, but I think Josh was next.
**jmacdonald** 13:18 I just wanted to agree that I think this is real. I sort of… I sort of disagree maybe with Austin, though. Like, you know, we need a way to support late-arriving data across the signal space, especially in metrics, but spans don't make this field very different to me. I have a span that's living forever. I don't see why we shouldn't just re-report it.
And when it comes to metrics, we see this problem where, you know, I'm receiving data pushed to me, I want to look at its real timestamp.
And there's gonna be data that keeps arriving. I can't output that metric data without waiting forever.
And I don't want to do that. I'd like to be able to put out 99% of my metric data, push it again when I get to 100%, And have that be part of the data model. And actually, the data model supports that fairly well, we just have no semantic conventions about how to do it. I could push a new metric update with some sort of revision number that says, this is version 2 of my metric update. I'm going to come up with version 3 of my metric update in a little while as well, when more later data comes in.
So I just think that, there's space in OpenTelemetry for later having data, and I think re-reporting spans makes sense. However, it doesn't go against what Josh and Austin said, that this is going to be hard to fit in right now.
**Austin Parker** 14:30 Two things. First, to your late-arriving metric data, I mean.
It's a different problem, because they'll have different timestamps. The secondary… Every… I mean… Right.
you know, when you get Rev 2 or 3 or whatever, that's gonna be later… The reporting time will be later.
So, it's not a collision.
I can't hear you.
**jmacdonald** 14:59 If I'm aggregating one minute of data, you know, minutes from 0 to second 0 to 2nd 60, that timestamp range is not going to change. I'm aggregating my metrics. Now some late-arriving data comes in.
still the same minute I'm aggregating, I just have more information. I need a version 2 on my minute of aggregation, and I think OTEL could benefit from a way to say that. That's what I'm trying to propose.
**Austin Parker** 15:22 Okay, yeah.
That makes sense.
I think we definitely have an easy… I think since reporting time and, recording time are different, that… that's slightly easier in metrics.
But either way, like… Yeah, I also want to suggest, like, it does kind of sound… like, when I talk to people about this, because I do want to agree with you, right? Like, I don't want this to sound like we're being dismissive, or I'm being dismissive, because I'm not. Like, this is a problem.
And if we had infinite time, money, and people, then we could solve it today.
But… I do want to say there's, like, two… when I talk to people that are having this problem, there's two very similar problems that are actually, like, kind of different, and Josh got to one of them, which is When you have a process that crashes and you have, buffered or in-flight data on the process.
Like, you want the ability to kind of see what is the stuff that is in memory, or that's waiting, or pending, or whatever? Like, you want that sort of, like, TraceZ sort of real-time, let me see what's in here and get a dump of it, and then, you know, yeet it out, right?
But then there's another problem, which is very similar to that, which is sort of the very long-running job problem, of, I have a process that takes several days, and… it might succeed, it might fail, I don't know, but I have no… but, like, the trace is fundamentally broken until the job completes.
Right? Because there's no root span, because the root span is… whatever.
And I think there's a open question still about… I think two things. One.
there's an open question of, are these the same solutions? I would say no, like, the… if you have a… I don't think everyone would agree with me here, but I would say if you have a job that is taking multiple days, or weeks, or months, like.
That's something where you're blending telemetry together, and you're not… Turning the entire thing into a trace, you're using a combination of events and traces.
But the solutioning for these is different, right? Because you don't really want, like… you want something where you're able to remotely see, oh, I have my job that takes a week to run, or multiple hours. Like, I think a good example of this is stuff like, I see this a lot with, like, AI people, or ML people, where they're doing training runs that can take days, weeks, whatever, and… need to be able to kind of see, you know, to be able to introspect the behavior of that run as it goes. And… that looks like a combination of different things. So… I just want to be precise that, like, yes, it's a problem. Yes, we're interested in solving and working on it. No, we don't really have the bandwidth to work on it, I think, to solve it big picture.
There's a lot of different things, you know, there's actually multiple specific questions that kind of come up, and the solutions for one aren't necessarily solving the other, even if there is overlap, and in the immediate term.
using events and helping to get the event stuff done, and semantic events for span metadata or span lifecycle is probably the most immediate way to solve your pain point today. Because that's something that works with everything that's out there, and it's something that we can sup… that, you know, we support in the SDK, the API, da-da-da-da-da-da.
Is that helpful?
**Mladjan Gadzic** 19:01 Yes, it was, yeah, really helpful. Thank you very much.
**Austin Parker** 19:06 Thanks for coming to the, thanks for coming, and thanks for using Hotel.
**Tigran Najaryan** 19:13 Okay, cool. I think you guys can take this offline and continue discussing. We should move to the next item.
Robert?
**Austin Parker** 19:26 I don't… know if Robert's… Not here.
**Tigran Najaryan** 19:29 Okay, he's not here. So this is… I think he calls for reviews, he wants it merged.
This is the… the extending of the attribute value types. This has been…
**Austin Parker** 19:40 Discussed.
**Tigran Najaryan** 19:40 to… to death, I think.
For the lost.
Multiple months, I think.
**Austin Parker** 19:48 Yeah, I can talk to it a little bit, because it's part of… it's coming out of, like, the log event stuff, but, we would… Appreciate being able to… have all of this stuff, spec stuff done by KubeCon North America, so, you know, that's coming up pretty soon, so it would be great if we could…
**Carlos Alberto Cortez** 20:13 I think there are some more results.
Sorry, yeah, there are some original comments. I don't know whether, actually, Robert paid, you know, attention to those ones.
Because I was reviewing that, yeah.
**Austin Parker** 20:26 Okay, I don't know, he's not here, but I can bring it up at the next, log sig.
If he's there.
And if he's not, then… Yeah.
DMM.
**Tigran Najaryan** 20:40 Okay, yeah, please take a look.
I think we need approvals.
I did a review, probably need to do another round myself.
Okay.
Let's see, what's this next one?
**Austin Parker** 21:02 Yeah, this is just for maintainers, or anyone in the sound of my voice, but, if you remember last year, we did community awards.
These are meant to recognize contributors that maybe don't… wouldn't get recognized otherwise, so… People… you can nominate people for this, anyone in the community can.
And it can be… For people that are contributing code, or docs, or CI fixes, or writing blogs, or tutorials, or whatever, right? This is literally… we want to cast the net very wide here, so please feel free to share this, into your SIGs, if you have… Observability, or open source teams, or whatever at your employers, point them towards this.
Nominations will run until November 6th, and we will announce the winners at KubeCon.
That is all. Thank you.
**Tigran Najaryan** 22:00 Right.
Thanks, Austin.
Antoine?
**Antoine Toulme** 22:07 So, if you are coming to KubeCon North America, there will be an observatory booth. You will be able to take time with your SIGs to have different meetings there. So, I just put up a little form here if you'd like to register interest, if you want to have a particular discussion or something like that, I would love to hear about what you want to present.
And, for now, it's just a forum for interest. We'll, consolidate that, and… Work together on the final schedule a little closer to date.
please pass it on, pass it on to your sigs. I'll start to make noise about it on the Slack as well, and make sure people get a chance to… Talk about what they want to talk about.
That's it.
**Tigran Najaryan** 22:58 Thanks, Antong.
David, you here?
**David Ashpole (dashpole)** 23:01 Yep.
So I was working on the Go histogram reservoir, and noticed that it just always keeps the last value for each bucket.
And, I wanted to propose changing that so that it's more like the… fixed-size reservoir. Initially, I thought it would be a… Have a performance cost associated with it, but… it turns out, at least in Go, it's actually much more expensive to record lots of exemplars than it is to, do this math for… calculating whether or not we should be recording them. So, I actually think this is just overall a good change for the reservoir. It means that the exemplars will be spread out over time instead of being All concentrated at the end, close to the… The collect… Point in time. Josh?
**Tigran Najaryan** 23:52 Isn't this a stable document? Sorry.
**David Ashpole (dashpole)** 23:54 Yes, I've written it in such a way that it still allows the existing implementations, I've just changed the recommendation.
**Josh Suereth** 24:01 Yeah.
**David Ashpole (dashpole)** 24:02 There's still concerns, that's fine.
**Josh Suereth** 24:05 I… I'm a… like, from an observability standpoint, David, I'm a huge fan of this. I think this is much better.
The reason it's the way it was, was to exactly match Prometheus behavior. I think that what you're proposing is actually better behavior, so as long as we don't have concerns with that, then I think we should totally change. In fact, like, with, With the exponential histogram, when we were doing experimentation with different reservoir sampling methods.
The fixed-sized sampling is actually pretty frickin' good, relatively. It's just, it doesn't necessarily grab your tails.
But it… it was better than a line bucket, in my opinion, in terms of, like, what you could capture.
So anyway, I'm a fan of starting to make some improvements here. I think this is a good improvement. I'm on board with this. The only concern is, if we deviate from Prometheus behavior, do we think that's a risk?
If it's not a big enough risk, and I think you'd be the person to tell us if it is, then we should go forward with it.
**Tigran Najaryan** 25:12 Okay, and my concern is this is a breaking change, guys. Even if this is just changing the default, I don't think we should do that, right? We should make this an option.
Exemption.
**Josh Suereth** 25:21 These bars are always opportunistic. There is no breaking change for changing the sampling method.
Like, because of the way exemplars work.
**Tigran Najaryan** 25:32 Yeah. Okay.
**Josh Suereth** 25:33 Alright.
Yeah.
**Tigran Najaryan** 25:37 This is not a break.
Oh.
in an observable change, essentially, if you update the SDK, right?
**David Ashpole (dashpole)** 25:47 Yes. Instead of seeing all of your exemplars.
clustered close to when the collection point happened, you'll see them spread out over time.
That's the change.
**Tigran Najaryan** 26:01 Okay.
It's a behavior… I guess let's…
**David Ashpole (dashpole)** 26:06 But… I've written the spec in such a way that if an SDK decided they couldn't do it without a breaking change, that they wouldn't be required to make this.
But if we don't think that any SDKs could actually make this change, then yeah, we should reject it, if that makes sense.
**Tigran Najaryan** 26:23 I don't mean breaking in the… in the public API, right? But this is… this changes the output.
Essentially, right? You see something different as a result of this change in the emitted data.
**David Ashpole (dashpole)** 26:37 Yes.
**Tigran Najaryan** 26:37 Don't we consider that to be a breaking change?
**Josh Suereth** 26:43 It… not… like, with the guarantees that are made with exemplars, no.
**Tigran Najaryan** 26:51 Okay, I… okay. I'm not sure I agree with that, but maybe you can point me to where in the spec we have Or don't have wording, which makes that… The actual wastewater.
**Josh Suereth** 27:05 it to you, but yeah.
**Tigran Najaryan** 27:06 Okay, okay.
**Josh Suereth** 27:07 Because by nature… by nature of how exemplars work and how most systems interact with them, this is… this is not a breaking change. Like, if we were to ask if somebody has an observability system set up that they're relying on exemplars to aid them, would this break their observability? The answer is no.
This might actually improve their observability or give them better coverage.
**Tigran Najaryan** 27:29 Okay, let's, I think we need to make it clear about…
**jmacdonald** 27:34 And it seems… I wonder, just to ask Tigran's question another way, why not have a new mode that's just, like, the time-weighted version? Because the first implementation is trivial, so leaving it doesn't seem like a lot of work.
**Austin Parker** 27:53 I… not to make this more or less complicated, but I do think that We do need to be very, cognizant of changing defaults.
Given some of the feedback that we've, been getting.
So, I would… I think it's a good change, and I think it is useful?
And I agree that it makes it better.
But I do think we need to… you know, carefully consider how we expose this to users, after the change. Should, you know.
I think we should probably treat it like anything else, where… existing systems can keep… existing things keep the old behavior, and then new things get the new behavior, and then after some time, you know, and then we publish a deprecation notice, whatever it is, like, I don't want to solutionize. I just think we need to be very considerate towards, like, when we change the defaults for things.
**Tigran Najaryan** 29:07 I agree with you in general, Austin.
**Josh Suereth** 29:10 when we designed… when we designed exemplars, though, and Tyler, thank you for the link, this is part of the data model of exemplars, is that the statistical sampling that we chose is something we should be able to change over time.
**Austin Parker** 29:24 I… I agree with that. And, again, if we…
**Josh Suereth** 29:26 if we… yeah. So, I… to your point, I think what you're saying is just, let's do a minor version bump. So this is not a major version bump breaking change, but we should be careful in doing a minor version bump. If that's the case, I'm on board.
**Austin Parker** 29:42 Yes, I think it, I mean… We wrote it, yes, good. I'm just saying that we write a lot of things, and you know, people… choose the buttons they press in life. So, like, as long as we're, you know, as long as we're commun… I think the… my point, I think, is mostly we just need to be sure that when we do stuff like this, we need to be communicative about what we're doing, why we're doing it, da-da-da-da-da. I think nobody here is wrong.
We shouldn't, you know, we did leave ourselves the ability to evolve this, and I agree that This is a much… this is a… this makes this just flat out better, and so we need to be able to do it.
We just need to make sure that we are clearly communicating these changes.
And, if possible, Letting people have a opt-in way that… Isn't just don't take the update.
Because a lot of people do blindly take updates, too.
**Tigran Najaryan** 30:45 Okay.
**Carlos Alberto Cortez** 30:46 But I guess that I have only a small request, which is that we leave this PR open so maintainers can take a look, check, and I like the notes that you left.
**Austin Parker** 30:57 Yeah, baby, could you please add the changelog label to this?
**David Ashpole (dashpole)** 31:06 With, like, needs changelog?
**Austin Parker** 31:08 It's just, if you go to labels and type changelog, it should.
Yeah, changelogs at OpenTillary, yeah.
**David Ashpole (dashpole)** 31:16 Okay. Yep. Just…
**Austin Parker** 31:17 And just for people, we do get traffic through this, like, people do pay attention to it, but yeah, if you have any, like, user-facing Maintainer-facing changes, please make sure you hit them with that changelog label so that it gets published to the feed.
**David Ashpole (dashpole)** 31:32 Yep.
**Austin Parker** 31:33 GC is supposed to do this for you, it's part of triage, but I, I don't know if we've been doing it, and I've been… Very busy with non-hotel stuff for a few months, so…
**Tigran Najaryan** 31:49 Okay, I think this explicitly answers the objection I had, so I'm cool.
**David Ashpole (dashpole)** 31:56 Alright, thank you. But any feedback, please leave it on the issue. I'll leave it open for a while.
Make sure people have time. And I only have a prototype in Go, so if anyone is interested in prototyping this in other languages, please let me know.
Thanks.
**Tigran Najaryan** 32:16 Okay.
That's all we have in the agenda. Anything else, anyone?
**Austin Parker** 32:23 Is this the first, spec meeting since the new TC members joined?
**David Ashpole (dashpole)** 32:32 Yep.
**Tigran Najaryan** 32:32 Yes, I think so.
**Austin Parker** 32:33 Hey, welcome! Just in case people didn't read, welcome back, Josh McDonald to the TC, and welcome, David Ashfold to the TC.
**David Ashpole (dashpole)** 32:43 Thank you.
**Reiley** 32:45 Welcome.
**Tigran Najaryan** 32:46 Come guys, good to have you.
**Austin Parker** 32:48 Hope to see y'all in person at KubeCon.
Alright.
**Tigran Najaryan** 33:03 Right? That's it, looks like.
**Reiley** 33:05 Bruh.
**Tigran Najaryan** 33:06 And Carol?
**Austin Parker** 33:07 Bye, Zoe.

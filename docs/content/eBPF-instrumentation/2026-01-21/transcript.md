SIG: eBPF instrumentation
Date: 2026-01-21
Duration: 64 minutes
Zoom Recording URL: https://zoom.us/rec/share/mN0PTGC8K4P9XQex0eHCS2SNiGSn3rVWkBTBScKaoL80KzVbnVUqr1dnuS0DQzTt.WQQGg0xaSgMpsfTX
============================================================

## Zoom Recording Transcript

Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:00:47 Hey, folks.
Mike Dame 00:00:50 Hey, guys.
Giuseppe Ognibene | Coralogix 00:00:51 removed.
Mike Dame 00:00:52 How's it going?
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:00:55 Hmm.
Giuseppe Ognibene | Coralogix 00:00:55 Pioneem.
Mike Dame 00:00:57 Good.
Tyler 00:01:00 Hey, how y'all doing?
Mike Dame 00:01:03 Hello?
Giuseppe Ognibene | Coralogix 00:01:04 Hi, Dalit.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:01:05 I'm recovering a little bit, I was so sick.
Tyler 00:01:08 -Oh.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:01:09 Yeah.
Tyler 00:01:10 That's not great.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:01:12 It's not.
Mario Macias 00:01:13 Afternoon.
Tyler 00:01:16 Hey.
Yeah, look, we can probably jump in here in just a second. If you haven't yet, go ahead and add your name to the attendees list. If you have, topics you want to talk about, please go ahead and add them there as well, and then, yeah, I'll start.
Sharing my screen, and we can jump in here.
Okay, awesome. Welcome, everyone.
So…
First thing on the agenda is I wanted to talk about these 2026 goals in the OB, roadmap, so…
Last time, we went through a lot to get all this stuff done. I've gone through, and I think for most of the things.
There's either an issue or an epic. I think that the only thing that I didn't…
get in here was, performance and log correlation works really well.
I didn't put issues for these today, I didn't… I… log correlation stuff, I think, might actually already… it's already there, so I'm not exactly sure what this topic was, and then the performance, I think, was captured in other areas with the specifics here, so…
There should be issues, all around these sort of things.
So they were captured here. I kind of wanted to walk through, what this was done, and one of the things that, like, I did do was I realized that there's, like, some bigger, like.
topics that we wanted to accomplish, and I captured those in what I called here, like, epics.
not married to any of these names, either. But, yeah, so, I've come through this, and this is kind of, like, the big highlights here. Each one of these epics has a bunch of sub-issues included in it, so…
This is, like, the 1.0 stabilization epic. A little bit of a breakdown here, and you can do a little bit of a, you know, deeper dive into that.
But this is all of the issues, outside of… this doesn't include any of the sub-issues here. So this is at, like, a high level, like, you know.
All of the issues, plus
Those that are not in EPICs here.
So, I wanted to kind of go through this, and if we could maybe, I guess if folks haven't already seen it, take a look at it, and maybe go through and…
ask ourself if this is still, like, our goals for 2026, because I think this is… today I wanted to, like, finalize this so we could start advertising this. This looked like a lot to me,
So, that's why I'm asking, I think, for a little bit more eyes on this. There's a lot of stuff here. Obviously, there's a bigger group here than, than just, you know, a few people, so I think we should be able to get a lot done, but I did want to go through this and ask about people's…
Thoughts if we are going to be able to accomplish all this?
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:04:46 My personal opinion is yes. If we continue with the effort, or the amount of effort we're putting in.
as… Before today, I guess?
And I know from, at least from Grafana's side, we don't want to slow down at all.
I think it's doable. I think it's a stretch, but I think it's… Not out of it.
of possibility.
Mario Macias 00:05:13 I agree with you, Nicura.
Tyler 00:05:15 Okay.
Yeah, sounds good.
Okay, then I guess, let's maybe go through some of this stuff. So I wanted to look at assignees, and more just, like, people we can ask about…
Not necessarily accomplishing the task, but make sure that the task is on hand, and that we're prioritizing it over the upcoming year.
So, for this 1.0 stabilization, I started this off by saying that, you know, I was willing to take on the task of making sure that we keep this going, and prioritize this going forward.
I wanted to also ask, like, size-wise, what people thought this was. I was considering this more of a large task, and, I'd also say this is kind of a higher priority, and so I just kind of wanted to go through this and see what people thought. So, like, does that seem reasonable to people?
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:06:03 Yeah, sounds good.
Tyler 00:06:04 Okay, cool. So, this other, Epic Additional Protocol Support, this is one where maybe we can kind of just jump through this one really quick.
There's, support for what I've got right now, gRPC context for application, MongoDB, compression payload stuff, instrument collection, for MQTT, AMQP, NATs.
Redis PubSub, and then Google Cloud Services as well. These are all the things that we had listed as well here. I was wondering, there's a few people that, like, brought up a lot of these things. Is there multiple people or one person that would like to take on the task of trying to work on this one?
Nimrod Avni 00:06:40 I think I can be assigned,
like, the Mongo stuff, and the gRPC.
It looks exactly like I'll do it, or someone in CoreLogix, but… I think we're doing.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:06:55 It doesn't have to be you doing all that, just kind of responsible to chase people down.
Nimrod Avni 00:07:00 I think that…
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:07:00 That's what we're looking for, if you want to be kind of the owner of the Epic, and obviously, like, I want to help out.
Absolutely.
Tyler 00:07:09 Yeah. Yeah, and at least Steven as well, I think, was looking at the.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:07:12 Yeah, and I, I mean, it's been on my list, the gRPC thing, for such a long time, so definitely want to help out.
Just kind of like an owner of the other.
Tyler 00:07:25 Yeah.
Marc 00:07:26 So, volunteered to work on all these… some of these topics.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:07:30 Exactly. Yeah, awesome.
Tyler 00:07:33 So, okay, Nimrod, I'm gonna put you down as the point person for all this. Folks that are interested in each one of these specific things, there are issues here, go ahead and, if you can't, I think you should be able to assign yourself. If you can't, put your name down and just, like, in a comment saying, I'd like to work on this, and then we can make these assigns.
But yeah, Nimrod, I'm gonna ask this, we'll have you be the point person on this one.
The size-wise here, I would also say this is quite a large, task, maybe even an extra large, but we'll just start there, and…
Priority, I'm also guessing a high one.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:08:07 Yeah, some of the items are high. I think gRPC's come up a couple of times.
Tyler 00:08:12 Yeah, I agree. I agree.
Okay.
Cool. Keeping it going, this is great. So, the .NET, work here, this one is just a… it's a little bit smaller, I think. I would definitely say that this one is less than what we would just look at. So, I'd probably say size-wise, this is probably closer to a medium. Priority-wise.
I'd also say this is a high one. This is, like, we've talked about this before, this is one of the more popular languages, right, Nicola?
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:08:40 Yep, yep.
Tyler 00:08:41 Yeah, okay.
As for an owner here, are there folks…
That are really interested in looking into this?
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:08:51 I'm gonna put… you can put me down, or I think, one item that I spoke about this with, Raphael, as well.
I don't know if he wants to own it, but essentially, if we have the capability of adding a trace ID on incoming requests, this will solve .NET.
So, that's a major blocker. Once we do that,
Supporting the older versions, we can decide if we want to do that.
Because… My understanding is that before .NET, they used request-ID, or something like that?
And still do the propagation if we inject that for them.
So… Yeah, but one critical item is injecting an incoming request.
Rafael Roquetto 00:09:36 I can… I can take care of it.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:09:39 Yeah, so do you… so the question is, do you want to own the Epic, or do you want to just do the work? Yeah? Okay.
Rafael Roquetto 00:09:44 No, no, I can only Epic, yeah.
Tyler 00:09:47 Okay.
Awesome.
I saw Robert was on the call as well, so yeah, this is something I think I've talked with him a lot about as well. By the way, Robert, is here. Nikola, we've talked about it before, so… Yeah. But yeah, maybe we can talk a little more later in the meeting, but this is great. Thanks, Raphael, for taking up the epic, and then…
That looks, looks good.
Then the last one, this one is a little bit harder.
I haven't finished the details on this one, so there's actually no sub-issues here. But this is a lot of really great ideas, and I just wanted to, like, capture it, so there's still a lot, I think, work here to do.
This is around the integration of the API SDK and the integration here.
So, if you haven't read through it, like, this is stuff we talked about last week. We could talk about it again if people have some questions.
As for ownership… Think about that.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:10:41 I'll take the… I'll take this one.
Tyler 00:10:43 Okay.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:10:43 Yeah. Unless somebody else wants to, I'm willing to, you know, push…
Tyler 00:10:48 No, that looks good.
I think, for…
strategic, like, sizing on this. I think this, again, is quite a large task. Yeah, and then,
I'd say, priority-wise, maybe not as high, or… okay, so maybe, like, a medium?
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:11:06 Yeah.
Tyler 00:11:07 Okay.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:11:08 Yeah.
Tyler 00:11:09 Cool.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:11:09 I mean…
Tyler 00:11:10 Awesome.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:11:12 Yeah, if we're able to do this, I mean, we're providing a value…
to open telemetry broad in general, right? Especially if we solve
the request time versus service time problem for all SDKs. We have the… we sort of…
That would be a great, I think, addition to open telemetry Community in total.
Tyler 00:11:31 I think, yeah, I 100% agree. I just think.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:11:36 Priority-wise, looking at these other epics, I would think we would probably try to prioritize those higher, but, like.
Tyler 00:11:42 I, like, if maybe you looked at a 2-year time span, I'd say this is maybe a very high priority.
So, yeah, I agree. I think that the integration with, just the hotel SDKs and, like, I have the agents as well as the API here as well, because, like, that interaction, it should just work seamlessly, and I think if it does, like, what we were talking about last time, it'd be…
phenomenal. I think we would just have, like, a really great reason to tell people just, you should always be running this, yeah.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:12:09 Yeah.
Tyler 00:12:11 Okay.
Next one, now we're out of the epics, so these are kind of, like, the bigger tasks, so definitely, I think, smaller tasks coming forward. Published binary executable files. This is something that's been on the roadmap for a long time. This is something I opened. I'm happy to take on this actual issue. This is something I need to work on, unless there's somebody else really chomping at the bit to get this done.
I think we can…
accomplish this pretty easily. There's a lot of thought already put into this, and I don't think there's too much. We already have a very, you know, some references. I do think it's a pretty small task by comparison, and I'll say probably a higher priority, so I'm just gonna rate it that way, if there's any…
Any objections?
He should…
Mario Macias 00:12:57 Charles.
Tyler 00:12:58 Okay, perfect.
Http header and body extraction. This is a newer one, that was opened by, Nimrod. I… if there's… this one seems pretty…
Pretty well documented. Thanks again, Nimrod, for opening this. This looks great. There's a lot of… a lot of thought on this one.
And so, yeah, I didn't know if we had an assignee. I think, size-wise, though, this one definitely looks a little smaller as well. Priority-wise, I didn't know what people thought on this one, if this is a low, medium, or high.
Nimrod Avni 00:13:29 I think I can take it. I think it's, like, a low or a medium, because there's no, like, real, like, semantic conventions, or I don't think there's a lot of instrumentation doing it. So it's not, like, something we need to catch up with.
Other, like, instrumentations, but it's, like, a… just a great feature to have.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:13:49 Yeah.
Tyler 00:13:51 Okay, I'm gonna… I'm gonna start at low. We can always bump it up as we… as we see fit. And then, Imrat, I'm gonna add you as the assignee here.
Perfect.
Okay, proposal, adopt OpenTelemetry submitted conventions for network flow attributes. This is one of the things that was opened last time. Sven, I think this is one of yours. Yep.
Sven Cowart 00:14:09 Yeah, happy to own it.
Tyler 00:14:11 Okay, perfect. Yep, there you are.
Mario Macias 00:14:14 Yeah, could you add me as a co-assigned?
Tyler 00:14:17 Yep.
Yeah, good point also, Mario, like, if there's anything people have seen that somebody's already been assigned to that they want to work on, that doesn't, like, doesn't exclude you, we've already said, but you can also just dual assign, we can always do that.
Mario Macias 00:14:31 So, yeah.
Tyler 00:14:32 Yeah, thanks for that.
And then, size-wise,
This one definitely looks smaller by comparison to some of the other tasks. Maybe a little bit larger…
It's maybe…
Mario Macias 00:14:43 Yeah, it's… it's not big… it's not big, but requires some coordination with many people.
Tyler 00:14:50 Right.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:14:51 We meet them.
Tyler 00:14:52 Yeah, maybe.
Sven Cowart 00:14:53 take a long time based on what Lyudmila said.
Yeah.
Tyler 00:14:59 Okay, then I will bump it up to a medium. Priority-wise, what are we thinking in this one?
Sven Cowart 00:15:07 had let.
Mario Macias 00:15:07 It's not… it's not super urgent in the sense that it won't block the… it won't block the release of OBI, but it will be nice to have it eat as soon as possible.
Sven Cowart 00:15:22 I'd say it's a low, just because of that reason.
Tyler 00:15:25 Okay.
I'll put it as low.
Sven Cowart 00:15:27 Until the semantic convention exists, there's no reason to make it a high priority, so we gotta make sure that first exists.
Tyler 00:15:35 Good point. Yep.
Okay.
Okay, and then align OB, network attributes with OpenTelemetry semantic conventions. I think this is, again, also one of yours, Sven, right?
Sven Cowart 00:15:47 Again, happy to own it.
Tyler 00:15:48 Okay.
Mario is this one you were interested.
Mario Macias 00:15:51 Please. Yes, please.
Sven Cowart 00:15:56 As far as size.
Tyler 00:15:58 Small, okay. And then, priority-wise, similar.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:16:02 Probably not.
Sven Cowart 00:16:03 I don't know how you guys feel about this, but I feel like this is a high if we're pushing for a 1.0 release, because after 1.0,
Making schema changes like this should… He avoided, possibly.
Mario Macias 00:16:15 This… but this one, yeah, so this is restrict… just to clarify, this is restricted to the current existing semantic conventions, right?
Sven Cowart 00:16:26 Yes.
I added a little extra in there, but yeah, my goal is… and I almost have this PR ready, actually, it's… I just… I want to make sure I have,
I just want to verify everything perfectly, because I'm new to the codebase, so I'm just making sure I understand everything that's going on, I don't miss anything before I make a PR, but, it's about 90% there. But it's just making sure that, like, like in this just top description here, we're actually using the
The actual semantic conversion attributes that
Relate back to some of these attributes we have here.
Tyler 00:17:04 Yeah, okay.
Perfect. Then we'll look forward to the PR, that looks great. And then, yeah, I think this looks, like, properly, categorized, yeah.
Okay, continuing on, Rust Tokyo context propagation. This is another one where I was close to building out an epic for a lot of the Rust stuff, but I don't think it was quite that size. So I…
I think this is definitely something that's extremely relevant. I think outside of .NET, this is one of, like, the last major, like, language hurdles that we have.
So, I was just wondering what people think on this one, for assignee size and priority.
Nimrod Avni 00:17:40 I… I can take it. And…
size, I think it might be a bit, like, I don't know, might have some complication with, like, all the stuff with, like, missing debug symbols and whatever,
And the priority, I don't know, it depends how many, how we… big we think, like, Rust usage and…
you know, adopting Tokyo and stuff can be, like, a medium as well.
Tyler 00:18:08 Okay.
Yeah, I think if, like, you had a direct comparison.NET would probably win out, but I don't think it's, like, that much further behind, is my…
Nimrod Avni 00:18:19 really gut impression. I don't have, like, much more to say. I'm also, like…
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:18:23 Nice.
Tyler 00:18:24 biased, because I like Russ more, but anyways, like.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:18:27 Well, also, I mean, mine, like.NET has an auto-instrumentation support from .NET is.
Robert Pająk (pellared) 00:18:34 Yeah, for us, there's no…
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:18:37 Yeah.
Rust, there's no auto instrumentation support, so…
Tyler 00:18:41 Yeah, good point.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:18:42 A bigger win for the community.
Tyler 00:18:44 Right, right.
So, yeah, okay, I think this is… this looks correct.
Sven Cowart 00:18:48 other EVPF agents as well.
Is that what you're getting at?
Zed.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:18:53 No, there's no other agents as well. So, for example.NET, you have… the SDK has a way to auto-inject on restart, given, right? If a new .NET service was starting, you can kind of…
set some environment variables, and it will automatically instrument .NET.
But there's no such thing for Rust.
Sven Cowart 00:19:16 Right, right.
I'm more speaking in the larger landscape of eBPF agents that export traces and so on. There's not a lot of them that support Rust, so if you could support Rust, that's really useful.
Tyler 00:19:30 Okay.
Good points for this. I think this is correctly structured. If people want to bump up the priority, we can always do that. But yeah, let's… let's start here.
Okay, next up, optimize switching to tracing, using tracing programs using K-probes. This is another one we had talked about last time, is captured here.
Mario Macias 00:19:51 this is somewhat related to a task I'm doing now, so… unless Nimrod, who proposed it, is interested, I can… I can… you can add me as a Sydney.
Or is anyone else is interested.
Nimrod Avni 00:20:07 I think there was originally, Matthias…
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:20:09 to you.
Nimrod Avni 00:20:10 Proposal.
Mattia Meleleo 00:20:11 Yeah, yeah, sure, feel free to take it if you're ready.
Started some work.
Mario Macias 00:20:17 Okay, if you'll be…
Rafael Roquetto 00:20:19 Sorry, Mario.
Mario Macias 00:20:20 No, I mean, if you are interested, I mean, I'm a signee, but that doesn't mean I'm doing it. If you are anyway interested… if you are anyway interested on doing or implementing the implementation, just feel free also to take it.
Mattia Meleleo 00:20:35 Yeah, sure, but I think this one will be priority low, so…
Mario Macias 00:20:40 Okay, okay.
Okay.
Rafael Roquetto 00:20:44 I was just curious if anyone ever tried it.
Like, as a prototype or anything?
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:20:51 I mean, this is part of the…
the task, right? To try it, see if it gets anywhere.
Rafael Roquetto 00:20:56 Yes. Well, yeah, I'm just wondering if anyone has already tried it, because I… I mean, I'm not discouraging, on the contrary. I'm all for it. It's just that I had a…
with something in the past, something to the correlation, that required me to kind of do that.
And I… I… I run into some issues, like, the kernel wasn't really accepting tracing programs, and as soon as VPF was.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:21:22 It's an.
Rafael Roquetto 00:21:22 Giving me a headache, so I was just wondering… I don't remember what it was, I was just wondering if someone else had tried it and it could refresh my mind.
Mattia Meleleo 00:21:30 Were you trying it on, ARM64?
Rafael Roquetto 00:21:34 No, just, Intel.
Mattia Meleleo 00:21:38 I don't know, I guess we have to try it, because it also depends, yeah.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:21:44 Yeah, especially the F, whatever those F trace or F things, they're supposed to be really fast.
Probe-wise. But they're not available in all kernel versions that we currently support, so something we discussed last sick call was that this would have to be part of the work.
Mattia Meleleo 00:22:00 Yeah, we also have to fall back if it's not supported.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:22:03 Yeah.
Rafael Roquetto 00:22:06 Cool.
Tyler 00:22:09 Yeah, raphael, if you want, there, like, please put down…
I guess you have vague recollections, but if you have more concrete recollections into this, what you've done before, like, please go ahead and add them to the, like, as a comment there, that'd be great.
Rafael Roquetto 00:22:22 Yeah, I'll see if we still have the branch where I… because I don't think we have infrastructure for that in our code, and I edit something, but I probably did it wrong. So, but I'll see if I can find out, and I'll add it there. Okay.
Awesome. Thanks.
Tyler 00:22:36 Okay, another one, update all semantic conventions to use the latest. This is something that we have,
Alex Bowen actually has opened a PR for this already, so this is pretty close, just needs to go through and get it over the line. So, I definitely think this is a smaller task, relatively. I'll put that down. I'm happy to take this on. I've worked a lot with the semantic conventions and that kind of stuff, so I can jump in here if there's nobody else that wants to…
Shepherd this one.
Sven Cowart 00:23:05 How much does this overlap with the other one, about, adopting the network semantic conventions?
Tyler 00:23:11 Probably a f- a little bit, yeah. I imagine it does just because, like,
there's probably no replacement for the things that we're currently using, and if we try to upgrade the semantic conventions, we're gonna need to be doing that, so… that's a… that's a good point. Actually, let me see, I got it right here…
Never float.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:23:35 I think it was more about existing other attributes related to application observability rather than network.
Tyler 00:23:42 Yeah, so I think, I think this one is more where it would overlap, just because…
I think if we try to do an upgrade here…
the new semantic convention might… it might actually be not a problem, from what I'm seeing.
What I'm thinking is there might actually not be versions of what we're currently using that exist, we need to migrate to a new one, but…
It might not as well. I definitely think that there's more included in this task than just that part, though, so…
Yeah.
But I'm just gonna put this down here.
Just for reference. But yeah, I don't… I don't know exactly. You can take a look at what Alex has already done, and you can see that there's failures in the CI, so there's… that might be one of the things he's looking at, too, so…
Okay, and I can assign this to myself on this one.
Okay, next up was integrate with the, EVPF… Profiler, which is… Real easy to say.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:24:53 Yeah.
I can own this.
Tyler 00:24:58 Okay, this is one of those ones where I was wondering if we actually want to have this as a goal for 2026?
Or if this one may actually not make the line.
But, Nicola, that's… if you wanted to take on this task, then I'm happy to let you make that determination as well.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:25:14 Yeah, that was good.
Mattia Meleleo 00:25:14 I put, I put a link in the chat, there have been some discussion in the first, OTEP.
So, basically, the consensus was that, we should make an OTEP, which is… which extends that one.
And it, basically should be based on the BPF map, which will contain the context.
Which, I'm starting to work on, started to work on, this week.
So, this is somewhat related to the improvement of the trace law correlation. That map will firstly be used internally.
And once it's good enough to share with the profiler, we can…
We can write that, OTEP, and go forward from there.
Tyler 00:26:09 Okay. I do have the OTEP links here. I also have, from our previous discussion, there is a document that was shared around this, that was created by the Datadog team in the profiler space, so I've linked those both here.
Batia, did you want me to add you as one of the owners of this here?
Mattia Meleleo 00:26:27 Yeah, sure.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:26:28 That's great.
That's awesome.
That's… that's great.
Tyler 00:26:35 Yeah.
Size-wise, I would say this is, like, on a medium or large.
What order?
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:26:40 people's.
Tyler 00:26:41 Thoughts?
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:26:42 I mean, technically, why is this medium, like, for us to add a map?
put it on a BPF file system, it's nothing, but…
Working with, OTEP and creating all those changes, probably.
Tyler 00:26:54 The OTEP, yeah, I think Robert can attest to, getting things through the specification, it's pretty hard.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:27:01 think otherwise. Do you think you should make it large?
Mattia Meleleo 00:27:04 No, I think the size… I mean, for us, the size is medium. There will be some work needed in the profiler as well, so I can't… I can't say what's…
What's the size.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:27:17 Like, I wanted to hack it up, and I had this map, and it was quite easy. It's just one place where they look at the Java current implementation, and if you just return that from a map there, just don't find it.
It seemed pretty easy to me, but I'm… but I didn't… I didn't actually attempt it.
Mattia Meleleo 00:27:35 Yeah, let's leave medium for now. This size is still, subject to…
Tyler 00:27:40 Right. Interpretation, so it's fine.
They're completely arbitrary anyway, so… that's what we agree on.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:27:46 Yeah, like I said, like, the good news is they actually do support something like this for the elastic way of the Java elastic agent pushing this a little bit of information for them to pick it up. So…
This was prior, this was at the time of the donation of the Oto Profiler, so…
Since they have that, I think majority of the difficult work of correlating the trace ID, making sure it's part of the profiler metadata and everything, it's already there. It's just providing a different means of giving back that.
Nimrod Avni 00:28:18 I think they also have, integration with PProf labels, where you can add some, so I guess, also some similar.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:28:29 Constance, yeah.
Tyler 00:28:32 Okay.
Yeah, so it looks like there's some… definitely some possibility here. Priority-wise, are we thinking lower-medium on this one?
Nimrod Avni 00:28:42 I think… I think medium. Okay. Yeah.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:28:45 Yeah, I think so, too. Sounds good.
Tyler 00:28:50 Okay. Keeping the momentum going, improving service metadata when not running in Kubernetes. This is another one, Nicola, you had posted.
Mario Macias 00:28:59 I can take it. Okay. It's also related with… What time do it.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:29:06 Yeah. Cool.
Giuseppe Ognibene | Coralogix 00:29:06 It's kind of.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:29:07 it's kind of really cool if you look what the Java agent does. You know, you throw it at some…
unknown, like, completely no labels, it figures everything out. It has some really good.
Mario Macias 00:29:17 Gotcha, but…
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:29:18 you try, like, the Node.js SDK, and it just says unknown service, right?
And if we could do an OBI, in a sort of generic way for all languages, it would be really good if we could…
be like Java.
Tyler 00:29:35 Be more like Java, but…
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:29:37 I think he's.
Tyler 00:29:37 Stickers for that, yeah.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:29:39 Giuseppe has his hand up.
Giuseppe Ognibene | Coralogix 00:29:42 Yeah. Is this something related to, like, the instrumentation of the container runtime? Because I was looking the semantic convention for the container.
And, we, we have something similar for Kubernetes, and I was thinking to, like.
If it's a good idea to instrument the container runtime or the container runtime interface, And, get,
information from directly the container instead of the API server, when actually you are not on a Kubernetes environment.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:30:16 That'd be great. Yeah, that helps with Docker, for sure, that's awesome. And, but also, like, we want to handle the cases where it's just a host. People deploy on a VM,
And… They should get a little bit better than just… Like… We, we use the…
I think the program name?
Which is great for Go, I think mostly is the right call, but…
But not if you're, like, Node.js, right? You just get Node, and all you have is Node.
Mario Macias 00:30:49 Do these include cloud metadata?
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:30:54 I think, it's probably good to add, yeah.
Mario Macias 00:30:58 Okay.
Nimrod Avni 00:30:58 That's, that's a question, because that's handled, I think that's mostly handled by the collector.
So it's a question of do we want… in Kubernetes, like, we do it because we want to implement, like, you know, connections with other containers. And maybe in cloud, we also want to have, like, connections with other, like, AWS components and get their name by their IP or something.
Yeah. But I think, like, I'm hoping for most of the stuff that the collector can handle.
We don't need to re-implement.
Mario Macias 00:31:33 Yes. Even maybe we can use the collector as libraries, some of the… part of the collector code as libraries, if we… if we need, for example, to assign a service name, or…
Things like that.
Nimrod Avni 00:31:49 Yeah, that sounds… the container runtime sounds good for…
Mario Macias 00:31:53 Yeah. Like.
Nimrod Avni 00:31:55 you know, containerized whether or not Kubernetes.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:32:00 Yeah, that's… that's gonna be great.
Tyler 00:32:02 Okay, yeah, I want to keep this moving, so these are all great ideas. If you have more, please go ahead and add them as comments here. I think this is great, just more thoughts that you have, or ideas.
Size-wise on this, we've got Mario assigned. Let me know if other people want to be assigned. Size-wise, this looks like a… I'd say a medium. There's a lot of surface area here, is that reasonable?
Mario Macias 00:32:22 Yeah.
Tyler 00:32:23 I would say that even it's large, or even it's an epic.
Yeah, yeah, that's actually a good point. If you would like, feel free, if you wanted to put more details here, we can always switch.
Mario Macias 00:32:35 Just too.
Tyler 00:32:36 Epic. Like, that is totally reasonable. Yeah, that's definitely fine.
Mario Macias 00:32:40 Priority-wise, I'm guessing it's probably, say, like, a medium?
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:32:48 Sounds good.
Mario Macias 00:32:48 Yeah, sounds good.
Tyler 00:32:50 Okay.
Cool. Alright, yeah, there's definitely a lot here, so, it's pretty thin right now, yeah.
Okay, next up, provide metrics about OBI, the self-observability metrics. This is something that was talked about in a few different places. I tried to capture, it in a single place here.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:33:13 Cool.
Mario Macias 00:33:14 We already have metrics about OB, OB, so it's…
Create… modify the… them for the semantic conventions, or adding more metrics will be.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:33:28 I think it's boats.
Tyler 00:33:30 Yeah, so this was about, like, it's runtime, right? So, if I remember correctly, so, like, the GC metrics, number of threads, number of goverages…
Mario Macias 00:33:37 Okay, okay.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:33:39 Okay, okay, to the rock.
Mario Macias 00:33:40 Platforms, yeah, okay, runtime matrix, okay, okay.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:33:44 No, I… I… sorry, it's… it's misunderstanding there. I think it will be, provide runtime metrics with OB. Should be… should be that, sorry. Okay, so not…
Yeah, so this would be, like, if you're running a Java application, but you're not instrumenting with the Java SDK,
we should try to get you GC metrics.
Or if you're running Node, we should probably get you some information about how big is the event loop.
Or things like that, which typically…
Mario Macias 00:34:17 Okay.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:34:18 Application developers on those platforms care about that.
Tyler 00:34:21 Okay.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:34:24 And they use that to tell them, like, why is my service not performing well enough? Oh, they…
the event queue is massive, or GC's taking too much time, so I need to resize my…
Mario Macias 00:34:35 Right.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:34:36 bogged.
Mario Macias 00:34:37 Is… is this targeting, is GO for GO, or generate?
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:34:44 Go, yeah, Go is one other example, like, go… number of Go routines is important, I think, to Go… to Go developers, that you…
They use it as a… sort of a metric to kind of know, am I doing something silly, right?
But…
Go GC is sort of important as well, maybe not as much, because it's a more like a…
But I know for Java, like, GC metrics are…
key to most people, and you'll find in the… in out there people doing crazy tunings on garbage collection with command line options for Java.
Yeah, if you submit an application with a Go SDK, you get all this stuff, right?
Correct me if I'm wrong.
Mario Macias 00:35:34 Yes.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:35:36 If you…
Tyler 00:35:37 If you submit… sorry, say that one more time?
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:35:40 If you kind of install the Go SDK, not user OB, you will get runtime metrics.
Tyler 00:35:47 No.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:35:48 No.
Tyler 00:35:48 To specifically install the runtime metric instrumentation.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:35:52 Okay, alright. But if you did install it, then you would get it, right? Yeah, yeah.
Stephen Lang 00:35:56 They… Nicola, the ones you're thinking of, they might be coming from the Prometheus library.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:36:01 Oh, okay.
Stephen Lang 00:36:02 No, David's shaking his head.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:36:05 No?
David Ashpole (dashpole) 00:36:05 I mean, there is a version that uses OTEL, or, like.
you could use the Prometheus Library and the Prometheus Bridge. Oh, you're saying, like.
if there's some that are already there on an endpoint today, where did they come from? Yeah, probably.
Stephen Lang 00:36:21 I mean, like, the Go GC metrics that you see on every Go process tend to come from the Meetius SDK, I think.
David Ashpole (dashpole) 00:36:29 Yeah, when you set up the Prometheus, like, default handle or whatever, it comes with runtime metrics.
Tyler 00:36:38 Okay.
I want to make sure we keep this going. Anybody wanted to take this on?
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:36:45 I can own it.
Tyler 00:36:47 Okay.
Obviously, it doesn't mean you have to do the work, but yeah,
Definitely wanted to keep track of it. And then, priority, or size-wise, this is, what would you say, Nikola?
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:36:57 I think it's a medium. It will be a long tail of languages we need to kind of add for, and some will not be possible.
Priority-wise, I would choose medium. I mean, some… some of these metrics are very important to… to developers, right? Like I mentioned, like, for Java people, they just religiously look at the GC metrics and try to optimize them.
Maybe not so much for other languages, but…
I'll stop prioritizing right there, and then add a couple more that are important to Go developers, Node.js, and I don't know, like, maybe.
Tyler 00:37:31 Yeah, and there are semantic conventions around this one, so, like, I think starting for that is probably where we want to go, yeah.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:37:37 Yeah.
Tyler 00:37:38 Okay, cool. Alright, thanks.
Next up is extend the network metrics. This is something that was, mentioned by Nikola, but also, was brought up extensively by, Nimrod in a previous, meeting, yeah, down here. So this is around, like, essentially, like, how are we going to merge this OpenTelemetry Networks project, into, Obi, is the idea.
And so, this is capturing that. I think with that in mind, there's probably, size-wise, I'd say, again, probably a medium on this one.
Correct. Nimrod and Nicola, I think you guys have looked at this most. Does that seem reasonable?
Nimrod Avni 00:38:15 I don't know.
Jessica.
Giuseppe Ognibene | Coralogix 00:38:18 Sure, I'm working on that. I have some, something to… to ask to you later, after we assign that, but…
I, really start to work on that.
Okay. If you want to assign me, or if anyone wants to…
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:38:35 It's great.
Tyler 00:38:37 No, that's great. Yeah, thanks, Giuseppe. Then, that's definitely perfect. I don't… are you a member of OTEL yet?
I don't know. You can search P&O.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:38:49 Beautiful.
Giuseppe Ognibene | Coralogix 00:38:50 Pinopinot instead of Giuseppe.
Tyler 00:38:51 Yeah…
Giuseppe Ognibene | Coralogix 00:38:52 I'm not part of.
Okay, you should…
Tyler 00:38:57 contact me, like, or message us in Slack afterwards, we should… I think you're at a point you can get added to the org.
You're well beyond that, so, yeah, happy to sponsor you. But, but if you want, could you just leave a comment here? If you leave a comment with your name, then I should be able to assign you to this, so that, that would work great.
And priority-wise, Giuseppe, it looks like you're already working on this one, and so I'm guessing it's something you can… we can put it, like, a medium?
Giuseppe Ognibene | Coralogix 00:39:26 Yeah.
Sven Cowart 00:39:28 I'm curious where this is coming from, or, some of these… like, who's working on that, because this…
Likely overlaps with the other larger, networks and anti-convention work.
That we talked about earlier.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:39:42 Yeah, it's mostly around adding missing functionality, such as, for example, TCP resets and things like that, that are part of the OpenTelemetry Network project.
that we want to re-enable, by using OB as a backend.
Sven Cowart 00:39:58 Okay.
Tyler 00:40:00 Yeah, these were just… these were the existing manifest of what's being exported by the networking metrics. So this is essentially, like, what we would try to be moving over. So, you are right, like, there's… I would be surprised if there is an overlap here.
So, yeah, like, it definitely is something to keep consolidate work on and keep an eye there.
I guess what?
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:40:21 involved.
Sven Cowart 00:40:21 what is this open tele… that open… and I can look at it myself, it just…
I'll just look… I'll just research it myself, and read up about it, and then come back.
Tyler 00:40:33 No, it's fair.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:40:33 Cold.
Tyler 00:40:34 It's just that it was, a project that existed prior to, this OB project. It's a very different
it's eBPF-based for networking metrics, and so it's very similar, it's just that, like, it does things in a very old way, and we have a lot of modern tooling that we're actually using now. And so the idea is, essentially, it's not…
It's not dead, I think people use it, but I think it is abandoned. I don't think there's a lot of development work on it there anymore, and so the idea was to try to, like, modernize it and bring that forward, and provide an offering there so we could, you know, in theory, give a recommendation to OTEL to say, like, let's archive this at this point.
Sven Cowart 00:41:11 Okay.
Tyler 00:41:12 Yeah, and so it's more about, I think, like, having a path forward for users of that existing thing. And so…
You know, providing…
comparable or overlapping, metrics here is the goal. And so what those names are, maybe there's a migration path for users, that, I think, is not as, as clear in this task as what you've already aligned here, with the networking. Okay. Yeah.
Sven Cowart 00:41:36 Yeah, that makes sense. I'll do a deep dive into it.
Tyler 00:41:41 Okay, yeah, yeah, definitely. And then, obviously, comment here, with any questions, something like that, like, have a conversation in this issue. It'd be perfect. So, yeah. Thanks again, Sam.
Sven Cowart 00:41:50 Yep, thank you.
Tyler 00:41:51 Okay, two more. We're almost there. Improved trace and log correlation?
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:41:59 That might be complete, I mean.
Tyler 00:42:01 I was wondering about this.
Nimrod Avni 00:42:03 Yeah, I just written a couple of stuff that we discussed internally, because the first draft is kind of complete, but we have a lot of…
Is there stuff you want to work on?
Including, like, supporting all… it's kind of what Mattia's already working on with, like, correlating all the runtimes, not pipelines, runtimes, and then maybe in the future also,
finding some other way that, does not include the BPF ProBrite.
But that's, seems like an umbrella issue for all that.
Tyler 00:42:40 Matthias Shea, saying.
Mattia Meleleo 00:42:41 I can take this one.
Tyler 00:42:42 Okay.
And then, Mattia, what size would you say this is?
Mattia Meleleo 00:42:51 Probably medium, and for priority…
I'm not sure here, maybe medium as well.
Tyler 00:43:00 Okay.
Yeah, that sounds good.
Okay. And then…
Another one, that I think we gotta start on, so build an hotel collector distribution with Obi as a receiver. This, again, opened by Nimrod.
Nimrod Avni 00:43:19 I can take it, yeah, just have some minor thing blocking, but I think it's…
overall, it's, like, a low effort, it's… I think it's mostly done, and I guess it's,
Medium or high priority, just to be part of the collector and,
I don't know, enjoy stuff like the op amp and all that stuff.
Tyler 00:43:44 Yeah, absolutely. Medium… Okay, yeah, I was… this might be larger than that, but…
You think you have a better understanding of it at this point? I think we already merged the initial receiver PR, so this actually might not be as big as I think it is, but…
Nimrod Avni 00:43:57 Yes, I think the main stuff, it's not a lot left.
Tyler 00:44:01 Okay.
Is the priority a medium we're talking here?
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:44:05 or high.
Tyler 00:44:06 Hi, sorry. Thanks.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:44:10 So… I mean, do you wanna try this?
approach that we've been using. We went back and forth what to do with the eBPF binaries on the Bela project, and we tried all these things and eventually settled back to the simplest
Or, which is just… Add the binaries on every release.
Rafael is here now. Rafael, does this happen automatically now? I… maybe other people know. I didn't know.
when we… I think we… we had this done in Vela, that when you make a release, the VPN binary gets built and committed.
Rafael Roquetto 00:44:49 Yes, I mean, we have a… there's something we need to discuss.
But yeah, basically, when we make a release, it gets committed. There's one problem that I realized,
late last year, which is, it's committing the binaries after the fact of the release, so after the tag, so it's always one minor version, behind.
So I'm… we're kind of working around that manually for the time being, but yes, that's the idea. So for every release, we ship in the binaries.
Tyler 00:45:22 Oh, you have an issue. Yeah, it's a… Is that nice?
Nimrod Avni 00:45:28 I, so I just wanted to first, like, consult with… there was a thread in the Slack, and that was also my fear of, like, how… I'm not sure how… I think, Tyler, you're doing most of the releases, I'm not sure what's the process of you just, like…
creating a new version, and then, like, everything runs, but if you want to, like, commit the BPF files, I guess you need, like, the release should be, after it's committed.
So I'm not sure what's the process there. If there's any way to automate it, I'm fine with, like… I think that's a good solution, but I think if it's gonna be manual, it's gonna be, like, well, I don't know.
It's not gonna be nice to manually, like, run docker generate and commit.
Tyler 00:46:13 Yeah, that's a good question. So, one of the things we're looking at is, like, committing them to a release branch, so people on the main branch won't have to deal with this.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:46:21 But…
Tyler 00:46:22 I think… I think that we could… we could make that happen.
from the automation side, the automation starts whenever I push a tag. This is how Steven has it set up, and it works great. I really like this.
But essentially, like, what I tag essentially gets included there. So if we… you know, in those pre-release PRs that we've been doing, instead of merging those back into main, if we merge them into some sort of release branch, and then if in that release PR we include the binary files that we want to include, like, the object files into that… into that PR.
It seems like that would do what we're trying to accomplish, and then the tagging would just pick that release branch, and it should include everything.
There's a lot of shits there, but yeah.
Rafael Roquetto 00:47:06 I think what we do at the moment at Grafana, basically, we run a workflow that runs Docker generate, and then it creates a commit on top of the last commit.
And with the updated binaries. So, if we did that for a release branch, that would work, and then once you do the release, you're gonna have the most up-to-date binaries. The only downside of that is, obviously, you're gonna be doing
that for every commit. I'm not sure… I mean, since we're already committing binaries, maybe, you know, we just…
suck it up, because it may blow up the repo size, may not, I don't know. But yeah, that would work, unless there is a way of really, as you were saying.
When you… before tagging, it does, like, one last step of… Running those actions, and…
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:47:58 But, hold on, like, if… if we're able to kind of, like, fork a release branch.
Whoever forks the release branch runs the… Where does the Docker generate?
And once that's ready, that's when we make the tag on top of that release branch.
Rafael Roquetto 00:48:14 Cheers.
Nimrod Avni 00:48:16 Yeah, I'm not sure exactly what's the process of, like, these, pre-release PRs.
Like, what do we actually change? Or is it something that happens automatically?
Tyler 00:48:26 Yeah, those are, those are manually done, those pre-release PRs. But, like, so yeah, there's a human in the loop there. So we could… we could do the step there, of manually creating it all in one.
I kinda like that cult, too, because, like.
and have somebody review it, essentially. Like, I'm not expecting people to review binary, but more just to say, like, it's there, right? Like, they got committed, yeah.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:48:51 People can still review it, like, what they can do is, they can download your branch if you really want, if you're worried about maintainer doing something funny. Yeah. You can download a branch, run Docker Generator yourself, and do a diff to see if it generates anything different. Then you say, hey, why did this…
Nimrod Avni 00:49:07 We can… we can even… I think I… I tried to do something, you can just do some, do it even in some GitHub hack action that, like, try to… like, only on release branches, or release PRs, kind of validate that it's the same binaries.
Tyler 00:49:22 Yeah, we could do that, absolutely, yeah.
One thing, I just want to make sure that we are talking about only doing this for releases, so things like commits to main won't have the binaries, and you, like, if you wanted to take, like, a point snapshot, you'd still have to do this funny thing where you generate it on your side, right?
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:49:38 Or generate your own branch, push it, like, if you want to test it with main, you can… you can make your own branch, push it to yours, and…
Tyler 00:49:44 Yeah, oh, yeah.
Nimrod Avni 00:49:45 Just as, because I tried to test it, apparently there's… because I need… when you build a collector, there's, like, the vanity URL that you, like, go to…
OpenTelemetry, I.O, blah blah blah, then you can't push it to, like, a fork. You need to push it to the actual, like, main… to, like, to our repository, and there's some branch rules of, like, you can't push…
like, you push only, like, like, Dependabot, and, like, reverts and stuff, so there's, like, some limitations on that. So either we need some other way to do it, if we want to test it, like, against some, like, collector, or…
Like, I think as soon as we have one release, I think it's gonna be easier for me to try to build it.
Tyler 00:50:29 Another thing you can do in the collector side is, in your go.mod file, you can add a replace statement there. That'll pull from a different location, which can be local or an external URL, yeah.
Nimrod Avni 00:50:40 Yeah, I think that… but the… some of the collector distributions, they don't actually use the go.mod, they use some, like, manifest file, which I don't… like, somehow, I guess, translates to, the go.mod.
Maybe I can check if there's some way to do it with that.
Rafael Roquetto 00:50:59 Yeah, I know that for Bela and Aloy.
which we have the same problem, we do exactly that, we do a replace on the go-out mod. But yeah, as you said, Nimrod, I'm not sure about the manifest.
We still would worry.
Nimrod Avni 00:51:12 When I built it, like, locally, like, I just did some replace, but if we want to build, like, our official release, I think we might.
Mike Dame 00:51:21 those… those builder configs support, like, GoMod replaces in there now. I think that the builder config manifest structure has a way to send, like.
Specific, modules.
Nimrod Avni 00:51:33 I… I can try.
Cool.
Tyler 00:51:38 But yeah, let me, jump back into that issue.
I can take on… The task of looking at, this more…
around the releasing, I think that would solve your problem, right? Looking at that, right, Nimrod?
Nimrod Avni 00:51:54 Yeah, as soon as we have, like, a release branch with, like, committed object files, then I can continue.
Tyler 00:52:03 I'm just gonna put some notes in here.
Okay,
I can start sharing my screen here in just a second. We only have, 8 minutes left, but we only have a few more topics. Giuseppe, I think the rest is coming from you,
You… we talked a little bit already about these network metrics,
Going back here, application network metrics. Is there more you wanted to discuss on this one?
Giuseppe Ognibene | Coralogix 00:52:44 Yeah, I hope this is related to the issue. Basically, let's start to create,
I call it an app network tracer, which is a tracer inside the, Upholi.
And this will create, like, network matrix, but related to one application, which is, like, separated with respect to the Anatoly, because that one is for, like, flows and so on.
So, if I can share my screen, maybe, I can show what I have in mind, maybe, you can give me…
I can share my screen.
Okay, yes.
So… Right now, we have this, let's see, what's my last name?
Can you… can you see it?
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:53:54 Yep.
Tyler 00:53:55 Yep, looking good.
Nimrod Avni 00:53:55 Okay.
Giuseppe Ognibene | Coralogix 00:53:57 So, on the left, right now we have this architecture. You know it very well. I had two ideas, actually three, but let's say that the first one is to create a completely separated network tracer.
which is, like, not like the usual tracers, like, GPU tracers and so on.
that reads from its own maps and sends to another pipeline here, where you just have everything that already has not only, like decorator, some metrics that we do on matrix, then aggregator, and then we send the metrics here.
And we don't pass, so we don't use the request spawn.
Or, another possi… another solution, and I already did some… some tests, like, with that one.
Another solution is to create a tracer inside the genetic tracer, like we already did for the GPU tracer.
But, again, we can read from our custom maps, so instead of reading from the events ring buffer, which can be, like, the performance can be slower, depends on how many network metrics we add.
We can just feed from our maps, and then, send, to the already created pipeline.
Instead of creating a new one.
This is something that you… you think is a good path, or do you have something else in mind?
Mario Macias 00:55:39 If we are not the correct… I mean, what's the… what's the… what's going to be in those metrics that are not already in the network metrics? We have the flows?
Giuseppe Ognibene | Coralogix 00:55:53 So, for example, I already did a test with the RTT, so it's a metric related.
Mario Macias 00:55:59 Oh, God.
Giuseppe Ognibene | Coralogix 00:56:00 osis.
So, we need to have in mind the relationship between PID, service, and so on. So we need to correlate that metric to that process. And in Natalie, we are not doing that, because we use traffic control.
Mario Macias 00:56:17 So…
Giuseppe Ognibene | Coralogix 00:56:19 this is why I just… actually, I just did a test with that. The only… the only thing is that, as we had a discussion internally, I need to replicate, like.
more or less the similar pipeline that we have in Etoli, but plus the knowledge of the… of the PID, so of what we… we already have in the other pipeline.
So the idea was actually on the one on the right.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:56:50 Yeah, the ride seems simpler, in my opinion, if you want to especially.
Mario Macias 00:56:53 Yes.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:56:53 It's… if you later want to correlate stuff by service and all that stuff, The application metrics is…
more suitable, in my opinion, the application pipeline?
Mario Macias 00:57:06 Yeah.
Giuseppe Ognibene | Coralogix 00:57:06 Actually, this one on the right is more or less what, Nicola, what you did on the DNS stuff, but it's a separated tracer, so you can enable it or not. But another thing is that we read from custom apps instead of the events.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:57:28 I see.
Yeah, yeah, I think…
I like that approach. The only downside is you have to fit it in the span format, but…
Probably can find enough fields, too.
Giuseppe Ognibene | Coralogix 00:57:40 Yeah, another thing that we were discussing internally is that
when we will change the name of the spawn, because from my point of view, it's not the spawn.
Mario Macias 00:57:50 Yeah.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:57:51 Yeah, yeah, go ahead. I don't, I don't mind.
Mario Macias 00:57:57 Rename it to…
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:57:59 Whatever. I think. Eddie.
Any, catch all.
Giuseppe Ognibene | Coralogix 00:58:08 Oh, okay.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:58:09 Probably need some… some love there, too.
to be, yeah.
Tyler 00:58:17 Okay, so, Giuseppe, sorry to cut you off, we're also coming up on the last minute here, so I just wanted to touch base. That looks great. If there are more, I think, things to say on that one, can we get in, in an issue, maybe continue the discussion if you have any more questions? Does that make sense, Giuseppe?
Giuseppe Ognibene | Coralogix 00:58:35 Yeah, yeah, well, actually, I'm on the… I'm in progress, so I can do some… something, and then I can push it.
Tyler 00:58:43 Yeah, okay. That sounds great.
Giuseppe Ognibene | Coralogix 00:58:46 Thank you.
Tyler 00:58:46 Last thing was this FOSTEM thing you had. We have 10, 15 seconds, is that something you can get done, then?
Giuseppe Ognibene | Coralogix 00:58:53 It's just, just a question. Does any one of you go to force them? Because me and Mattia, we will go to Brooks Hell at the end of January, if anyone…
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:59:02 hotel unplugged as well?
Giuseppe Ognibene | Coralogix 00:59:04 No, because it's on Monday, and I didn't know that. I will go on Saturday and Sunday.
Mario Macias 00:59:12 I'm going to… I'm going to be in both, force them and hotel unplugged.
Giuseppe Ognibene | Coralogix 00:59:19 Okay, we can, we can see that.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:59:22 Not sure yet, I said no, but, the appointment that I had that was blocking me from going got moved, so…
But it's last minute, so I may not be able to find a good flight.
Giuseppe Ognibene | Coralogix 00:59:34 Oh.
If, if you, if you come out here, we'll offer us a beer. You say that.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:59:40 That's… that's the deal? Okay.
Mario Macias 00:59:42 That's right.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:59:43 game completely now.
Tyler 00:59:44 I didn't know this, maybe I'll come now.
Okay, alright, we are at time. I want to be respectful, so thanks everyone for their time. I will see you all in a week, otherwise I'll see you asynchronously. Alright, bye.
Mattia Meleleo 00:59:58 You inform them. Bye, guys.
Mario Macias 01:00:00 Bye-bye.

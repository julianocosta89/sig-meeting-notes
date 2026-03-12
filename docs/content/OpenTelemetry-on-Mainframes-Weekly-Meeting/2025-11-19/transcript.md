SIG: OpenTelemetry on Mainframes Weekly Meeting
Date: 2025-11-19
Duration: 14 minutes
============================================================

## Zoom Recording Transcript

**Ruediger Schulze (IBM)** 00:13 Hey, Craig, good to see you.
**Greg Shriver** 00:20 Hey, Rudica!
**Ruediger Schulze (IBM)** 00:24 Boom.
Can be that it's only the two of us today, and… I don't know.
Wow.
Let's see if somebody else is joining, but That's maybe… that's maybe a chance to consolidate on things.
**Greg Shriver** 00:41 Yeah.
**Ruediger Schulze (IBM)** 00:42 Seth has been very busy times, obviously.
**Greg Shriver** 00:45 Yeah.
Yeah, I wasn't able to make it last week.
**Ruediger Schulze (IBM)** 00:51 Okay, yeah, I think last week.
Did we? They actually had it? I think last week we skipped, isn't it?
**Greg Shriver** 01:01 Oh, did we skip last week?
**Ruediger Schulze (IBM)** 01:02 Yeah, I was good last year.
**Greg Shriver** 01:05 Okay.
**Ruediger Schulze (IBM)** 01:07 The guy also couldn't do it, so…
**Greg Shriver** 01:10 Okay, yeah, 5th, that would have been the 12th, yeah, we didn't have it there. Okay.
**Ruediger Schulze (IBM)** 01:30 I'll be…
**Anand Somasundaram** 01:33 Hello, good afternoon, good evening.
**Ruediger Schulze (IBM)** 01:36 Hang on.
It's a small group today.
Let me pick on, on a couple of topics. So, G-Top Action Runner.
So… Actually, an ongoing odyssey.
So, I was able to install the application.
And from my perspective, this all also looks good.
But, checking this with the… of resource office.
It looks like that the installation process did not completely go through.
**atoulme** 02:20 Yeah, approve, right?
**Ruediger Schulze (IBM)** 02:22 Yeah, they, they, they did it. Hey, hey, Antoine.
They don't see the request cleanly going through in terms of the association with the IBM ID.
**atoulme** 02:34 Yep.
**Ruediger Schulze (IBM)** 02:34 And, this is more probably a suspect, but it might be that I have not sufficient authority on the… This was for the OpenTelemetry Collector repository.
That I might actually have to have administrative authorization on the repository.
**atoulme** 02:56 That's pretty exciting.
**Ruediger Schulze (IBM)** 02:58 That puts me to this point we had earlier, this idea of having a call once together.
Maybe this is really what we need to do once to get this moving.
**atoulme** 03:13 Yeah, so we're now in a Plan B, where things didn't work, and we need to get you in the same room as Trask to do something really in the open source office.
Folks to do something in simultaneously where Yeah. Everybody lined up and agreeing on the permissions, and maybe even elevating your permissions during the time of install.
**Ruediger Schulze (IBM)** 03:34 That might be required. I mean, first step is probably to really reconfirm that that's the cause of the issue, and I think I also need to go back to our folks on this one.
But then, sounds like we… we probably need to do this in a coordinated way to, you know, like I say, potentially elevating access, doing the installation.
Verifying… You know, decreasing access again.
**atoulme** 04:05 Yeah, no, no, that's going to work all the way.
So, anywho, can't really help with that in this meeting. I can ping Trask on it if he hasn't.
**Ruediger Schulze (IBM)** 04:17 I saw that you discussed that with me, but Trask was in the thread, so I was hoping it would… Yeah.
**atoulme** 04:22 But he did not.
Right.
**Ruediger Schulze (IBM)** 04:27 Yeah, I think not, that's correct.
But yeah, this was also hidden in this, and this was just replying to you.
**atoulme** 04:36 No, he did not… he did not pick that up. Yeah, I can't do much for you, because the only person who can actually do anything is.
**Ruediger Schulze (IBM)** 04:42 Sure.
**atoulme** 04:42 Let's go, Osteen Parker.
**Ruediger Schulze (IBM)** 04:55 Let me just put a brief slack here.
**atoulme** 05:19 Okay.
**Ruediger Schulze (IBM)** 05:21 It's not gonna Put this also here on the Slack.
**atoulme** 05:31 Yeah, I wouldn't hold my breath too much on this one. I don't know if it's going to be able to get back to us.
Anytime soon.
**Ruediger Schulze (IBM)** 05:38 Anyway.
Okay.
Okay, that's this topic.
Right, so, Craig, don't want to put you on the spot, but I think at some point, we discussed about pulling together The different documents that we had.
**Greg Shriver** 06:15 We did. We did discuss that, yeah.
I have not made any progress on that, and I will try and make that more of a priority.
**Ruediger Schulze (IBM)** 06:26 Mmm.
Right, so…
**Greg Shriver** 06:31 Yep.
**Ruediger Schulze (IBM)** 06:33 I'm just looking at, you know… Right.
Yeah, and then, you know, I think we could also, also in blog posts or anything.
Oops, I'm sorry, wrong line here.
Yeah, this was from the fifths.
**Greg Shriver** 07:01 Yeah, 5th, yeah.
**Ruediger Schulze (IBM)** 07:02 Yeah.
Okay, good.
Right.
So I know, also, somewhat, Delaying activities here.
But it's not off my agenda, not the PRs for the CUS subsystems and the related spans, it's just that they're… There were very busy times recently.
And the same for… for the… all the metric discussion. I mean, this relates to this, right, Craig? So, there's a related topic is the… get… topic is the… get the metric discussion going.
Yeah. I'll continue this.
And, enable us, or enable folks to get, get related PRs out there.
Whoa.
initial metrics.
Right.
Yeah, so in this sense, there's not much update, Morgan and Antoine, but, you know, it's… You know, Anyway, the… as we discussed last time, actually, the hotel train for the mainframe is… is… is going.
I think we need to put a couple of contributions back to the community with respect to semantic conventions at ATC, but you know, the… the, you know, implementations by the ISVs is actually happening.
**Morgan McLean** 08:53 Where are we right now in terms of capabilities? Like, one of the Wells Fargo people who's joined about a month or two ago had asked me privately, like.
what works right now? Like, what sort of mainframe data can they get?
Like, at this moment, using this. I think the answer is the collector runs on most mainframe systems and can capture a variety of host metrics, even though the semantics aren't finished yet. Is that accurate?
**Ruediger Schulze (IBM)** 09:18 No, this is, so the… okay, first of all, you need to distinguish between Do you look at Linux on C, or do you look at COS?
**Morgan McLean** 09:29 Yes.
Both.
**Ruediger Schulze (IBM)** 09:32 There are… there are two different… Of course. You know, operating systems, and COS obviously is, you know, from historically a complete different architecture than Linux.
Yep. The collector, as we said, is ported over to Linux on C. There's also this effort around the Digitub action runner to now elevate the support, to Tier 2, so that would be part of the CI pipeline. Yep. Once we get over this hurdle, that should also be straightforward, and… Then… from a mainframe point of view, so what is available from the CUS subsystem, so there are these transaction processing systems, think of KICS, IMS, DB2, MQ.
If you look at, current documentation, latest releases of those, They support native distributed tracing.
through telemetry, so you can get spans… Oh, wow, okay. …in a non-code… So, no code…
**Morgan McLean** 10:35 Right out of the system, through kicks and everything else, yeah.
**Ruediger Schulze (IBM)** 10:37 Right, not, requiring changes to your application, or to your program.
Having said that, when it comes to metrics and logs, there are different vendor implementations out there.
So, the, obviously, metric data, gathered in the system measurement facility, as it's being called SMF, And then, you know, these different ISV vendors have solutions on top of this. Building on existing products, obviously, but enabling them, having them enabled to support the OpenTelemetry protocol.
Des.
not specifically semantic conventions for this data that is being exported. Yeah. And this is what we are aiming for here from a metric point of view, to… what we always say, kind of like to have the base set of metrics being part of the semantic conventions. At some point, this obviously, you know, will then go into vendor-specific metrics, because everybody has its own mechanism to aggregate to process the data that you get from the system, which I think is a fair way still. The data is being sent over OpenTelemetry.
And if there is a, you know, a core set of these metrics, portable.
**Morgan McLean** 11:56 semantic conventions, all this, what we discussed. All of that'll come through OTEL, yeah.
**Ruediger Schulze (IBM)** 12:00 Yeah, that, that's, that's all very good, and… If then, you know, it goes into, let's say, ISV-specific metrics, as long as they come via OpenTelemetry, you know, this is still good, because you can then have your custom dashboards or custom analytics built on top of this.
**Morgan McLean** 12:18 Sure. Okay.
**Ruediger Schulze (IBM)** 12:19 That's actually more progress than I realized we'd made. That's actually quite impressive.
So, there is functionality there, it's more now about to retrofit span attributes, like I said, right? It's, something… That needs to be done.
**Morgan McLean** 12:34 Okay This is a great river.
**Ruediger Schulze (IBM)** 12:37 Yeah.
Okay, I don't have much else to share today, maybe, Craig, the next thing is maybe, really, let's work on a block there, and let's really focus on maybe building some small PRs for the metric discussion.
Before I get this spent, topic being dissolved.
**Greg Shriver** 13:00 Yeah, agreed.
Any, any mainframe-related nuggets from KubeCon?
**Morgan McLean** 13:10 The… I mean, some press and analysts asked about it. I don't know how… I mean, they're clearly asking about it because they've been asked by others.
most of the sort of mainframe-related conversations I've had recently have been with Wells Fargo, who's a customer of ours, and I think a customer, actually, many of the people contributing to this. But the present analysts that I've had raised it, which I always find interesting.
I also find it interesting, because, like, KubeCon is kind of, like, the last place in the world people would typically talk about mainframes.
Yeah, so the fact that.
**Greg Shriver** 13:42 That's true.
**Morgan McLean** 13:42 Up frequently enough.
I mean, we mentioned I did… I was part of the governance committee present and TC presentation. We brought it up as one of the major roadmap items for OTEL. But, like, it's… the fact that mainframe stuff comes up enough with the audiences at KubeCon is very telling.
Because if the Kubernetes people are talking about it, obviously it's probably even more important than everyone else.
**Ruediger Schulze (IBM)** 14:04 Right, yeah, so the… I mean, this is what you see with the clients, you know, this is all this aspect of end-to-end observability that plays into this.
And, yeah, so it makes perfect sense.
Right.
**Morgan McLean** 14:19 Cool.
**Ruediger Schulze (IBM)** 14:20 Okay, yeah, and yeah, let's… let's… let me work internally to understand this GitHub action challenge a little bit better, and then we need to reconvene on this one, and… Yeah, let's… let's check next week.
**Morgan McLean** 14:35 Okay.
**Greg Shriver** 14:36 Okay.
**Morgan McLean** 14:37 Thanks, folks. Okay, thank you. Catch you later!
**Greg Shriver** 14:39 Thanks, everybody.
**Ruediger Schulze (IBM)** 14:40 See ya. Bye.
**Greg Shriver** 14:41 Bye-bye.
**Anand Somasundaram** 14:42 Why?

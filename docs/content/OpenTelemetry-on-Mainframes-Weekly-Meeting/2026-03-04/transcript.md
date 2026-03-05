SIG: OpenTelemetry on Mainframes Weekly Meeting
Date: 2026-03-04
Duration: 22 minutes
============================================================

## Zoom Recording Transcript

**Jim Porell** 00:24 Okay, who solved the problem?
**Richard Nikula** 00:34 I just figured somebody had it.
Running, I don't know.
**Jim Porell** 00:39 Yeah, I don't know, but who would it be?
**Richard Nikula** 00:43 That I didn't know.
Man, who owns this meeting?
**Jim Porell** 00:47 I was thinking it was Morgan, but then he's not here, so…
**Richard Nikula** 00:51 Maybe he's in.
**Jim Porell** 00:59 Let me try and ping root again.
**Greg Shriver** 01:14 Hello? Check.
**Jim Porell** 01:18 We are here.
**Greg Shriver** 01:22 Alrighty.
**Jim Porell** 01:25 Hmm, we're just showing off the line, but… Hmm…
**Greg Shriver** 01:45 I'm sh…
**Ruediger Schulze (IBM)** 02:27 Hi, Lance.
**Jim Porell** 02:30 There he is.
**Ruediger Schulze (IBM)** 02:32 Jim, is this just you and me today?
**Jim Porell** 02:34 No, it's Richard, Kai, Greg, and… Not here.
**Ruediger Schulze (IBM)** 02:39 Oh.
**Jim Porell** 02:40 Aaron Richards.
**Ruediger Schulze (IBM)** 02:41 Now I can see you. Okay, so, sorry, I'm a little bit on the road with my kids.
**Jim Porell** 02:46 Yeah, you're driving again?
**Ruediger Schulze (IBM)** 02:47 But anyway, wanted to dial in.
Okay, okay, good.
Maybe we start, Craig? I think you have been on share. Any… anything about open telemetry, open mainframe project?
**Greg Shriver** 03:07 Sure, yeah, I mean, I can… I can certainly,
So, I wasn't able to attend all the sessions, but I know that, I mean, I was able to attend the MQ session, and… oh, I do have a quote to share, and I don't remember the gentleman's name, but it was,
It was an MQ session, and they were highlighting the, the MQ, support that they added.
And the quote was.
We actually… the MQ development team used OpenTelemetry as the main debugging tool when developing the support within the MQ component.
So, I thought… I mean, that's not a direct quote, I'm sure I'm paraphrasing, but I felt that that was pretty high praise, so…
**Ruediger Schulze (IBM)** 04:01 Yeah, and I can say there have been similar statements from the Kix development team as well, when they did their work. So, yeah, I think it's…
It's… it's… it's a functionality that actually helps in different ways, right? So, that's good. Okay.
**Greg Shriver** 04:18 Sure. We also had another session… there were several sessions that touched on OpenTelemetry.
We did talk about the mainframe SIG in… in the session that I had, and there were…
There were about…
maybe 30 people in that one? I don't know. The rooms of the chair were really, really small.
Or at least most of them. And most… and for many of the sessions, they were just packed.
I mean, anything that had to do with AI, of course. There were, you know, several OpenTelemetry-related sessions. Those seemed to be pretty well attended.
And… and of course, post-quantum crypto, that was a hot topic as well.
But that's about it. That's really all I have to share in terms of feedback or impressions from Cher.
**Ruediger Schulze (IBM)** 05:18 Yeah, no, that's great. So, thanks for…
For, for sharing that. Okay.
I can't see the agenda today, apologies for this, and I think we want to follow up on a couple of things, but what I wanted to say is… so, the TPS PR, as you know, we had that open, I actually updated it, then for… maybe there have been holidays or whatever, it went again into stale, I let it open again, reopened the PR again.
My plan is to go…
to the… I was on the semantic convention SICK meeting this week, but next week, I want to go there as well. Actually, I want to put us on the agenda.
It's probably good just to talk about the TPS PR again, but also…
I think it would be good to share a little bit about our plans, and as you remember, the Semantic Convention Center also, they asked us for input, what we want to do at the… during the course of this year. So, I would like to discuss this a little bit, and if you have any input or anything that you would like to
you know, have discussed there in this context. Please add this to the…
To the meeting notes, and I will take this forward on… on Monday.
**Greg Shriver** 06:38 for… on Monday… Alright, actually, I should share my screen while I'm taking notes. Hold on a minute.
Sorry, not that folks want to watch me type, but I just want to make sure I get the… So, Ruduga, you're gonna attend the Semantic Convention's, Semantic Convention's meeting Monday?
**Ruediger Schulze (IBM)** 06:59 Yes, yeah.
**Greg Shriver** 07:01 And the ask is that…
**Ruediger Schulze (IBM)** 07:05 Yeah.
**Greg Shriver** 07:06 Spokes comment.
**Ruediger Schulze (IBM)** 07:08 Right, and… or just input what, you know… I think it's probably good if we…
I have a couple of questions to them, which is probably the best to discuss with them, just on the call. So things like, okay, where are we now with virtualization? Where are we with entity relationships?
what do you expect us how to do this? I mean, I know the semantic conventions, they also rely, in the meantime, pretty much on prototypes being available.
Now, with the work that we are doing.
Maybe also with some of the attributes.
That's an interesting scenario. Some of this obviously made it into the product of the different vendors that we have here on this call.
And,
So, yeah, I think I will have a couple of questions to them, and if you have, kind of, like, also similar type of questions, it would be… would be good if we consolidate them, and then I would try to…
To, to walk through them on the next semantic conventions sequels.
**Greg Shriver** 08:10 Okay.
And… and Rutica, do you want folks to comment… add their comments in… directly in the PR, or do you want it to do… do you want them to add them in the… in the Slack channel, or directly?
**Ruediger Schulze (IBM)** 08:23 If it's to the TPS, then, please feel free to comment on the PR. Yeah, if it's more generic, general topics, then either Slack or on the… yeah, probably on the Slack channel is probably the best.
**Greg Shriver** 08:39 Okay.
**Ruediger Schulze (IBM)** 08:40 And…
then I really would want to go forward, as we discussed, right? We said small PRs that we want to create.
So, essentially, what I want to do is, you know, bring us again into awareness at the semantic convention stick, and then I think we need to bring forward a couple of PRs to really work with them to
Get content in.
**Greg Shriver** 09:16 Okay.
Alrighty.
So…
and sort of in line with that, I threw… I hope… Rude, you probably can't see this, because you're in
in communicato, but…
I added a section in the OpenTelemetry on Mainframe notes, having the… it has the open PRs and their current status kind of at the top of the document before the meeting notes.
And I have your TPS PR as the first one, and the general documentation PR as the second one. I can go over the document… the documentation PR,
that… that one has… that's still in the same state. It's still open and pending, and I still have the next action, and I have not been able to take that yet. I've been away.
I guess the question that I have is, are those currently the only open PRs
That this group is focusing on that we know of, and are there any that we should add to that list?
**Ruediger Schulze (IBM)** 10:24 I think that's… and by the way, I can't see the screen now. I think that's the current list.
**Greg Shriver** 10:30 Okay.
**Ruediger Schulze (IBM)** 10:31 And, just FYI, this is not really a PR. There isn't…
there was an issue opened, and I can put the number later on on the…
on the… on the notes here. There was an issue opened by somebody for the OpenTelemetry collector on Linux on S390X.
seeing high CPU consumption rates for some scenarios, and somebody from my colleagues is looking into this, but also
The way how the collector is used, it might be actually not a S390-specific issue, it might be actually…
let's say, an issue that you would also see on x86?
But it's… it's interesting, so obviously there are some, you know.
organizations or some people who, you know, work with the port to Linux S390X.
**Greg Shriver** 11:32 Okay, so there was an issue against the collector for high CPU running on… on S390?
**Ruediger Schulze (IBM)** 11:38 Yes, Linux, Linux S390.
**Greg Shriver** 11:41 Okay.
**Jim Porell** 11:42 See, I wonder…
**Ruediger Schulze (IBM)** 11:44 when you…
**Jim Porell** 11:47 I think that's always gonna be true.
**Ruediger Schulze (IBM)** 11:49 And I, I think it's…
**Jim Porell** 11:51 I don't… I don't know if it's…
I would be interested to see how does it compare the S390 to a non-S390, because I just think the volume coming out of a mainframe could be huge in a development environment, and that's why I was interested in the comment that Greg said.
For, MQ. Development environment, there's probably not a lot of queues. When you get this thing fully loaded.
That scares the hell out of me. You know, you think about how tight a KICS transaction is.
And now, if you're trying to add in a communication path.
per transaction, you're gonna double, triple the MIPS, possibly, so… I, I… Yeah.
**Ruediger Schulze (IBM)** 12:36 I, I could see…
**Jim Porell** 12:37 Performance being several different ways.
**Ruediger Schulze (IBM)** 12:40 Yeah, and I think we… from the perspective of our company, I think we have been… some of this discussing also at some conferences and other places. So, in fact, in case of MQ, the overhead is… if you just take it relatively to the message.
It's… it's significant, so you can… and this is something which we generally have been observing, if you think about how the approach works there.
So the… the gathering of the span attributes and then injection to the in-memory SMF, this is, like, 5 microseconds, and this is more or less consistent across the different subsystems.
But that's what you need to… to account for if you turn on… The distributed tracing functionality.
And then with the way, or with the emitter that is part of CUS, it's another 3 microseconds, for formatting, then, the data.
Which obviously is then, you know, separate to your transaction processing.
However, and this is then really dependent on your workload.
And the complexity, obviously, of your business logic and what your transaction does. The…
we, in the end, didn't go forward to kind of, like, publish relative overhead numbers, because this will vary very much. What we have been sharing is just the numbers that I just mentioned, so…
And then it's really up to the workloads that clients would be running.
**Jim Porell** 14:19 Yeah, I just… I don't know, personal opinion, it seems like…
Customers are going to decide, based on that overhead.
who's actually eligible for OpenTelemetry, because I don't know if they can afford to turn it on for everybody.
**Ruediger Schulze (IBM)** 14:34 Yes, and I think that's probably the reality that we will see in maybe 2-3 years timeframe. We had different
Customers… You know, talking to us about this topic in the sense of.
They would be pricing in this overhead, because they… they would like to have this visibility. Obviously, not for all, but maybe for some of the transactions.
Whereas,
okay, maybe for others, you know, maybe also smaller size customers, this overhead is maybe already very significant, right? And, then it's maybe more something that they would be using to
discover the application landscape, maybe more from a test perspective. So I think there are different use cases to it at the end.
**Jim Porell** 15:25 Like I said, development environment makes a ton of sense, because.
**Ruediger Schulze (IBM)** 15:29 Yeah.
**Jim Porell** 15:30 getting a topology. You just mentioned it, you know, you're getting the topology of the environment. That's huge.
And automagically getting that. That's pretty beneficial to everybody.
But then, turning on the metering while you're running in production, you are…
**Ruediger Schulze (IBM)** 15:47 Yep.
**Richard Nikula** 15:50 Yeah, I think there's different use cases, and I think one of the things that I noticed is if you look at
what Kix did… Kicks did a very…
brief, terse set of data, right? It's just… just enough, right?
MQ, on the other hand, is kind of decided a different way, where it's really almost more of a tracing scenario, where you want to know as much as you can about transaction.
which I'm not sure is a good fit for the open telemetry, right? So I think that's part of also what has to get figured out, is what are the use cases
that people are going to be doing, right? Do they simply want to know it went to the mainframe and went here, here, here, or do they… oh, it went to the mainframe and it did X and Y? Well, I mean, that's… you have to know a lot more. I mean, it's… it may be a combination of tools, ultimately.
**Jim Porell** 16:45 Yep.
**Ruediger Schulze (IBM)** 16:47 And I think, Richard, that's what you just said as last. I think that's really the reality, that, you know, it's a combination of tools, and we would…
anyway, assume this is more for the SRE type of persona.
And the… the SME type of persona would… they would have their own tours.
to… So, I think it's really about rou…
problem identification, where the problem sits, but it's not about root cause identification as such, right? This would be with, you know, the other two as.
**Richard Nikula** 17:17 Right. That everybody is using.
**Greg Shriver** 17:21 I'm personally very happy that this conversation is coming up, because in my view, that this is a very high-quality problem to have.
I mean, yeah, we can address this 16 different ways, right? With sampling, with…
you know, cutting stuff down in the collector, cutting it be… you know, cutting data down before it ever gets emitted. I mean, there's… there's…
The fact that the data is available
for those different use cases. I also agree with the comment that, you know, it really depends on the use case, and it would probably be helpful to, you know, have sort of a list of those use cases.
**Jim Porell** 18:08 I'm feeling… I'm feeling it for the S390 side, because, you know, maybe that first customer only had an S390 collector. It would be really interesting to do a benchmark with a non-S390 collector.
only because…
one, their common code, and two, I don't… I really don't think it's a collector issue, it's a volume issue.
And… or potentially, it might be more of a volume issue, and the volume would be the same on either side.
**Ruediger Schulze (IBM)** 18:39 Yeah, and just to this specific scenario, Jim, that was actually a lock gathering on Linux scenario, so this was not related to the tracing.
**Jim Porell** 18:49 Okay, okay.
**Ruediger Schulze (IBM)** 18:50 When I'm home, I will add the issue number. There's not too much information, unfortunately, on the issue itself, and my colleague has been asking for more details on the config and things like this. But,
it's anyway interesting to see that also the OpenTelemetry Collector is being used.
**Jim Porell** 19:14 But as Greg said, this is a good thing. You know, you want people trying this stuff, you know, it's not… you're trying to… nobody's trying to create vaporware.
**Ruediger Schulze (IBM)** 19:22 Right, right, right, right.
Okay, what else? If you zoom in on the agenda…
**Greg Shriver** 19:40 I didn't have anything else on the agenda. I don't have any other topics to add to the agenda.
I'm not sure if, Kai or Richard Selak have anything to add.
**Ruediger Schulze (IBM)** 19:55 Snow?
**Richard Salac** 19:56 I have a question. I have a question regarding the Java agent that was offered to the community, the one from Madeframe.
Yeah.
**Ruediger Schulze (IBM)** 20:08 Unfortunately, I didn't… you know, they were supposed to…
to join the SICK meeting, I think 2 weeks ago.
And I… they didn't join, and I haven't heard back from them. I may write an email as well to them and ask if this interest is still there, and maybe it's just a timing issue that they couldn't make it to the sick call, or if they
We'd like to handle this differently.
Let me, let me write to them and see if I can get a response.
**Richard Salac** 20:44 Okay, great. The reason why I'm asking is that we had a talk with the ZOE, and even though it is not exactly to the ZOE, the open mainframe project could be interested.
But we wanted to sync with, with you first, Rodrigo, because… because you were the one.
Who was, in contact with them.
**Ruediger Schulze (IBM)** 21:14 Yeah, let me check with Sam if… if this is still current.
And then, you know, let's look at next steps. We can also do this, you know, they have been on the Slack channel, and we can also
You know, if they are willing to continue, we can also coordinate via the Slack channel, obviously.
**Richard Salac** 21:37 Okay, thanks.
**Greg Shriver** 21:51 Okay.
All right, thanks, Richard. Kai, anything from you?
**Kai Kirsch** 21:57 No, I'm good. Thank you, Greg.
**Greg Shriver** 21:59 Thanks, Kai.
**Ruediger Schulze (IBM)** 22:02 Good. Yeah, then let's meet next Wednesday again, hopefully with some feedback from the Somatic Convention SICK.
**Greg Shriver** 22:12 Sounds great.
**Jim Porell** 22:13 Right, yeah, thanks.
**Richard Salac** 22:14 Okay.
**Ruediger Schulze (IBM)** 22:15 Okay, good, have a good one.
**Greg Shriver** 22:17 Like…
**Ruediger Schulze (IBM)** 22:18 Thank you, bye.
**Jim Porell** 22:19 Bye.
**Kai Kirsch** 22:20 Bye.

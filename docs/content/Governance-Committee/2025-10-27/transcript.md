SIG: GC Project Management (EU)
Date: 2025-10-27
Duration: 64 minutes
============================================================

## Zoom Recording Transcript

Kushal 00:08:09 Hey Dan, what's up?
Can you hear me?
Dan Gomez Blanco 00:08:15 Hello? Yeah, I can hear you, yep.
Kushal 00:08:17 Yo.
Juraci Paixão Kröhling 00:08:18 Oh…
Kushal 00:08:19 Whoa.
Actually, I just, started to… looking into OpenTelemetry.
And, previously I was contributing to Prometheus.
So can you guys just guide me, like, where I can start? Like, there are so many… repository in OpenTelemetry organization.
Like, how I can start learning about it and get into this thing.
Dan Gomez Blanco 00:08:46 Yep, So, thanks for joining, I want to say, first of all. Do you know more or less what this, you know, we can go through that. Do you know, what this, meeting is about?
I think you joined the…
Kushal 00:09:01 Yeah, so, I think this is related to… project, right? I think it's more related to, like, some of the open issues.
In OpenTelemetry, yeah.
Dan Gomez Blanco 00:09:15 Yeah, so we'll be doing more of a… the OpenTelemetry specification tri- triage.
So, in terms of, like, if you wanted to start to contribute to OpenTelemetry, you've got multiple avenues there. I think, you know, depending on what area you would be more interested in contributing. Is there a specific area, or are you looking to…
Kushal 00:09:39 Yeah, so there's a collective contra repository I was looking.
Dan Gomez Blanco 00:09:44 Okay, and are you familiar with the, community… let me just share it.
Kushal 00:09:50 Yeah, yeah, Ubernetes, Prometheus.
Dan Gomez Blanco 00:09:52 No, the community repo, there is, like, all the meetings that one can join, so I think, you know, we normally recommend Either joining the Slack channel, joining the meeting, seeing, you know, hey, I'm here.
Here, I want to start contributing.
Kushal 00:10:06 Yeah.
Yep.
Dan Gomez Blanco 00:10:09 So, if it is the collector contrib, that you, you know, that you would like to start contributing to. They… yeah, I would put the… probably the best way to get started is to go to that, To that meeting?
I am.
Or join the Slack channel, as well.
One second, I'm trying to find the… The meeting times.
There you go. So, and if you scroll down in that page, Actually, we do have a… a specific…
Kushal 00:10:51 No.
Dan Gomez Blanco 00:10:51 For the collector. So yeah, so I think, you know, they do… the collector do have alternating… alternating meetings, so if you wanted to start contributing to the collector, I would recommend either joining the… the Slack channel, CNCF. Are you on the CNCF, Slack already? Have you got one again?
Kushal 00:11:09 Oh, yeah, yeah.
Dan Gomez Blanco 00:11:11 Cool. Yeah, so I think what I would propose is, you know, that you start by joining the channel, joining the meeting, seeing how you, you know, basically say, hey, you know, I just want to start contributing, what is the best way to start?
I don't know if the collector… Specifically, have, Like a starter guide.
I'm not… Too sure, but I know that some… SIGs may do have a… Yeah.
If you're a, if you're a, you know, if your first contribution, where should you start?
Kushal 00:11:46 Got it, yeah. Basically… There's no… documentation, like, starting documentation for collector.
So yeah, I will go through this.
Dan Gomez Blanco 00:11:57 It might, there might be, there might be, I'm not, I'm not too sure. But I, yeah, I think, you know.
If you join the meeting, any of the meetings.
It would be more than happy to, to… To get you started.
Kushal 00:12:11 Got it, yeah. Actually, this is my first meeting.
Dan Gomez Blanco 00:12:14 Oh, thanks for joining. I mean, you're welcome to stay, if you want.
Kushal 00:12:18 Yeah, yeah.
Dan Gomez Blanco 00:12:18 You know, would probably be talking about more about the specification and other areas, rather than the collector.
Kushal 00:12:24 Got it, yeah, I will try to grab as much as I can.
Dan Gomez Blanco 00:12:33 Hello, Robert.
RP Robert Pająk (Pellared) 00:12:35 Hello, nice to see you.
Dan Gomez Blanco 00:12:39 How was your tourism in Edinburgh after KCD?
RP Robert Pająk (Pellared) 00:12:43 Yeah, it was awesome.
Dan Gomez Blanco 00:12:44 I, used the advice I was in Steering.
RP Robert Pająk (Pellared) 00:12:48 And it was a good, actually good advice. It was perfect. You've been there already?
Dan Gomez Blanco 00:12:53 To what? To a…
RP Robert Pająk (Pellared) 00:12:54 dealing…
Dan Gomez Blanco 00:12:56 Yeah, I mean, I've been there a long time ago, Sterling, yeah, it does, Yeah, it's a good… day trip.
RP Robert Pająk (Pellared) 00:13:04 Yeah. Like, I also had a chance, because the weather was perfect.
Dan Gomez Blanco 00:13:09 So, I had seen all the mountains to the north.
RP Robert Pająk (Pellared) 00:13:13 Which is amazing. There was no wind.
Dan Gomez Blanco 00:13:17 Yeah. Good luck.
Hi, Severin.
RP Robert Pająk (Pellared) 00:13:24 I'm gonna mute myself, because someone is renovating some apartment nearby, and… I almost did not hear even your husband.
Severin Neumann 00:13:37 Awesome.
I think Yorasi sent his… Getting some coffee, and we'll be back in a minute.
Juraci Paixão Kröhling 00:13:43 And I'm back.
I'm back, I'm here. Hello, hello.
Severin Neumann 00:13:47 Awesome.
Do we want to get started with the triage, then?
Juraci Paixão Kröhling 00:13:53 Yeah, but before we do that, what… what… I mean, I cannot parse the message that you have behind you. Sharks love sugar?
Severin Neumann 00:14:01 Yeah. What is that?
That's, like, part of what we do at work, right? It's not about correlation, it's about causation.
So…
Juraci Paixão Kröhling 00:14:10 You know?
Severin Neumann 00:14:12 You noted… you noted thing about, like, in… in… In summer, when people go to the beach, they eat more ice cream, and also there's more shock attacks, so the… the correlation.
Juraci Paixão Kröhling 00:14:25 That's a pleasure.
Severin Neumann 00:14:26 They're like, shark sugar, right?
Juraci Paixão Kröhling 00:14:30 Oh, my, okay, okay.
Dan Gomez Blanco 00:14:32 one related to…
Juraci Paixão Kröhling 00:14:33 That's good.
Dan Gomez Blanco 00:14:34 Like, oh, what's his name?
Forgot this famous actor's, like… His films, and, like, something like, you know, correlation to some other thing that was, like…
Severin Neumann 00:14:47 There's a whole website, I think it's called Spurious Correlations or something like that, I think they definitely have that with the… That's, that's really fun, it's like, let me send you the link in the chat.
That's it.
Tyler Wiegan, or something like that, but he's, like, all those, like, hey, here's a correlate, like, like, here's two metrics, and they correlate with each other, so obviously there's… there's something into that, and I think there's also a bunch of actors Let me see… Discover… But yeah, you can have a lot of fun with that. Anyways, that's not what we wanted to talk about, right?
Dan Gomez Blanco 00:15:33 Yeah, okay, let me get the… I can get the spec issues… Up.
Right, okay. Got it. Let me share my screen.
Okay.
We can make this a bit bigger.
Should we start from the bottom?
What is this? This… define what metrics.
As a signal type means.
Severin Neumann 00:16:06 Oh, that's a really old one, and then someone commented, like.
Dan Gomez Blanco 00:16:09 Yeah, someone added this.
Severin Neumann 00:16:13 Signal…
RP Robert Pająk (Pellared) 00:16:17 I think we can just assign…
Severin Neumann 00:16:22 But maybe this is solved already, right? So maybe we can, like, I would be surprised that we… That we don't have a… yeah, I think we do have it in the spec. Can you click into the… Into the spec glossary, so maybe…
Dan Gomez Blanco 00:16:38 Okay.
Oh, and signals… Logs?
I guess we have logs, but we don't have metrics or traces in this… in the…
RP Robert Pająk (Pellared) 00:17:04 I think the issue is also that we have two glossaries. I think we have a different glossary in the spec, and different in OpExter material, am I right, Severin?
Severin Neumann 00:17:12 Yeah, there always also has been, like, issue.
RP Robert Pająk (Pellared) 00:17:18 I think the other one in the open room.io is the more important, I guess.
Severin Neumann 00:17:24 Yeah, we… I think at some point we even had a debate about, like, hey, how do we merge the two, or should there be only one, or whatever, and that always got lost.
Dan Gomez Blanco 00:17:33 I mean… What I'm thinking is, like… sorry, I'm just copying the link from…
Severin Neumann 00:17:37 having it, like, in the official, like, in the spec glossary, I think it's, like, is, like, worthwhile to have, so, yeah, why not?
Dan Gomez Blanco 00:17:45 So we have this, right?
And then here we've got, like.
all of them defined all the signals, so…
RP Robert Pająk (Pellared) 00:17:54 There's also glossary in the concepts here.
But I'm not.
Dan Gomez Blanco 00:18:02 Alright, I see.
But I think… I don't know, I… I don't know how I feel about, like… Having… Well, we don't have metric.
Right, so that actually… and then see metric, and I'm assuming that points to the… yeah, cool.
RP Robert Pająk (Pellared) 00:18:25 And that's perfect.
Dan Gomez Blanco 00:18:28 So… I don't know.
Is there… is this an issue?
That is already solved, and the issue is a different one where, like, maybe there's already one open, where we've got the… The, you know, the fact that we've got two glossaries, or…
Severin Neumann 00:18:46 Let me see… I think we had one on the OpenTelemetry I.O.
repo… That could be really old as well.
Really?
Yep.
the… yeah, the question is, like, that you say, like, hey, thank you for offering your help, but yeah. And maybe let's remove the help wanted.
Dan Gomez Blanco 00:20:30 Do we have the issue, or do we want to search for that other issue, if there is one?
About having to…
Severin Neumann 00:20:37 I did not find one, but let me create one. Can you… can you send me that issue into our triage channel?
And then I can… Let me… would it make more sense to have that issue on SPAC, or would it make more sense to have it on… I.O.
Dan Gomez Blanco 00:20:58 Mmm, perhaps both.
Severin Neumann 00:21:00 Or is it a community issue? Should we have, like…
Dan Gomez Blanco 00:21:04 I would probably create it in the spec.
Severin Neumann 00:21:07 Yeah.
Dan Gomez Blanco 00:21:08 Yeah. Okay.
More.
Severin Neumann 00:21:13 Maybe we have one in the stack already, let me check that. But yeah, just send it to me and I can…
Dan Gomez Blanco 00:21:22 Right, so I'll just comment this, thanks for offering your help, this is fine.
In here, admittedly not in the spec glossary.
It is an issue that we have two glossaries, spec and docs, we should discuss that in a different… Issue.
Let us see… problem. Otherwise, I'm just using the word issue too many times.
It's a problem that we have the two glossaries of specs and dogs… spec and dogs. We should discuss that in a different issue.
And I'll close that.
This can be close, right?
Severin Neumann 00:21:53 I think this can be closed, too.
But same conf has not yet another glossary, right? Okay.
Dan Gomez Blanco 00:22:03 same comf as another glossary, right?
Severin Neumann 00:22:05 No, I said, like, hopefully they don't, but it looks like they don't, so.
Dan Gomez Blanco 00:22:10 Cool, alright, I'll do that Mmm… Having a look at this, it looks like the other glossary has more content in it.
So… Yeah.
Don't know if you wanted to mention that, but… It looks like this has more.
More content in it.
Okay.
If you can… yeah, if you can link that.
Okay, cool. That's one.
And there are a few… okay, no translation mode and Prometheus to OTLP.
conversion.
Severin Neumann 00:24:01 Is there not, like, a Prometheus, just like that we drop it into…
RP Robert Pająk (Pellared) 00:24:06 Yep, that's the issue.
Severin Neumann 00:24:08 Yeah.
Dan Gomez Blanco 00:24:11 Yeah… I, you know, I just borderline… yeah, I think it's probably a SIG issue.
I mean, it is definitely a sick issue. I'm just thinking, if we want to have a say about… If there's… from the perspective of… I guess… Spec.
if this is something that… because I'm seeing, like, Back-end being involved… being… mentioned… Let me… mirror me.
And it seemed the problem… I don't know.
The issue was open after discussion here.
So there's another issue here.
And then, yeah, so Arthur… Already moved it into the spec.
Or it moved it, like, asked them to… Created it here in the spec.
I mean, we could mark it as Seg issue, and I think it is already labeled as Seg issue, actually.
Severin Neumann 00:25:46 Yup.
Dan Gomez Blanco 00:25:46 Got that now? Alright, you're just…
Severin Neumann 00:25:48 If it's labels are sick, yeah.
Dan Gomez Blanco 00:25:52 Yeah, I mean… It is labeled a SIG issue, but I'm just trying to understand if, you know, we're trying to solve here for… the backend… that you're… Creating that data from?
And there's something that… It's not in the scope of OpenTelemetry, I'm assuming?
Juraci Paixão Kröhling 00:26:16 Yeah, I mean, taking my triager hat off, I… I think this is a bad idea.
Dan Gomez Blanco 00:26:24 But is that Norway?
Juraci Paixão Kröhling 00:26:24 night.
Dan Gomez Blanco 00:26:25 Doing triage a little bit, and say, you know, this does not align with the scope of OpenTelemetry, or… or are we taking that too far, if we do that?
Juraci Paixão Kröhling 00:26:35 I… huh, that's a good… I mean, I always assumed that we would, only leave things, well, make things find their way to the people doing… making the decision, making the call on that. Like, if something is really obvious that it's not… Hotel. Then we just close it.
But in this case here.
I think there might be an angle that we… that I'm not aware of, or not familiar, like, I don't know Prometheus that much. I would delegate that to the Prometheus SIG.
But, without further context, I think this is a really bad idea.
Perhaps the Prometheus folks think that this does make sense, I don't know.
Dan Gomez Blanco 00:27:21 Okay.
Should we just leave it there?
Juraci Paixão Kröhling 00:27:25 Yeah, I knew.
Yeah, I think so.
Dan Gomez Blanco 00:27:30 I'm going to…
Juraci Paixão Kröhling 00:27:30 I mean, yeah. I think I didn't… But you have a very good point, Tan. I think there are two… three places where a decision can be made here. One is the SIG itself, the second one is the TC, and then the GC.
Dan Gomez Blanco 00:27:46 Yeah. Yeah, okay, fair enough.
Juraci Paixão Kröhling 00:27:48 I think, yeah, I think, like, even if it passes the SIG, the TC can say this is a really bad idea.
And if… if the TC decides that it's a very good idea to focus on that, then the GC can say, well, you know what, we have other pressing issues right now.
Dan Gomez Blanco 00:28:06 Yep.
Okay, let's leave it at that.
Right, so that's done.
I was thinking of, so this is more of a sem column thing.
And it's not.
We'll put that trace in.
I don't think this is related to Trace.
RP Robert Pająk (Pellared) 00:28:44 First of all, I think it should be moved to semantic conventions.
Right?
Dan Gomez Blanco 00:28:52 It should be.
We can move it.
Mmm… Yeah.
I'll move it there.
Why'd you make a comment?
M… Where's Trump?
Just one… Is there not, like, a… do we not have a project that is… Just kicked off. Or was approved.
For this sort of thing.
Maybe worth mentioning it. Maybe just mention that.
If I can get that project.
Juraci Paixão Kröhling 00:30:01 Desktop?
Dan Gomez Blanco 00:30:02 No, there was one around… I will find it.
Juraci Paixão Kröhling 00:30:09 Okay, I thought you mentioned, desktop, so that's… that's why I was confused.
Dan Gomez Blanco 00:30:13 Service and deployment.
Senkov.
Juraci Paixão Kröhling 00:30:16 Yeah.
Yes.
Dan Gomez Blanco 00:30:21 this project.
Juraci Paixão Kröhling 00:30:23 Yes.
This, this was approved, this is, this is happening now.
Dan Gomez Blanco 00:30:28 It is already.
Juraci Paixão Kröhling 00:30:30 Yeah.
Dan Gomez Blanco 00:30:31 here.
Mmm… That's the same person that…
Juraci Paixão Kröhling 00:30:51 You know.
Dan Gomez Blanco 00:30:51 Nope.
Juraci Paixão Kröhling 00:30:52 But it is the same issue, yeah, but it's there now.
Right. So I think we can just close it.
Dan Gomez Blanco 00:30:58 But close it in the SenConf repo? I mean, maybe this is, like, part of their work, I'm not sure.
RP Robert Pająk (Pellared) 00:31:03 Logis…
Juraci Paixão Kröhling 00:31:04 This was opened last week.
RP Robert Pająk (Pellared) 00:31:07 I would just move it there and let semantic conventions decide if the job is done or not, just to make sure that…
Dan Gomez Blanco 00:31:15 Right.
Juraci Paixão Kröhling 00:31:15 I mean, I… yeah, I would even close and say, like, reopen if you think it's not… this is not done, or if there's anything that is still missing.
Because otherwise, it would just linger there, linger around there.
Well, hopefully people there will triage and close.
Dan Gomez Blanco 00:31:35 I think this will probably be triage… needs triage, so I think they'll… yeah, I'll leave the semantic conventions team to do it, I think.
Juraci Paixão Kröhling 00:31:43 Okay, good.
Dan Gomez Blanco 00:31:45 That's the… Close some of these.
Always process bands, always record sampler, and… There's a PR.
I'm not sure I understand the… So… do we know, I mean, there's a noise… There's an always-on sampler, is that not, like… Am I missing the point here?
If it's early, I have not… I just realized this morning that I don't have any coffee beans in the house, so… Maybe I'm…
Juraci Paixão Kröhling 00:34:00 No, I think it is somewhat confusing, so, A sampler that always returns a sampling decision that includes the recording span. Includes the recording span.
I don't know if it's not simple.org.
I mean, simply is recording, isn't it?
Dan Gomez Blanco 00:34:18 Yeah, so they always own, they always own span.
Juraci Paixão Kröhling 00:34:21 Yeah.
Dan Gomez Blanco 00:34:22 Already…
Juraci Paixão Kröhling 00:34:25 So I guess the only situation that I can think of that makes sense here is you have the parent span with a decision to not record, like.
Not simple, and then you want to sample the child spend anyway.
But it means you end up with a broken trace, because you have a… The parent service is not sampling the parent spend.
And the child span would be sampled, so it makes reference to a parent span that doesn't exist.
I, I mean, I would ask for a clarification, like, can you, can you draw that, like, Because there is the always-on sampler.
As you mentioned. So, there is this option already, unless they are talking about a child span of a span that was… Decided not to be recorded, not to be assembled.
Dan Gomez Blanco 00:35:20 But then, that's also possible at the moment, right? You can have an always-on sampler, and then not have the… respect… parent… I forgot the… what it was, but, like, the…
Juraci Paixão Kröhling 00:35:30 A decision made at the parent is always respected.
Except for something that is very, very new and hasn't been implemented on any… any SDKs yet, as far as I know. Perhaps only Go, and Hubbard would correct me here, but there's a new proposal for, It's actually one of the latest blog posts that we have on the blog right now, and that would allow you to sample, like, narrow down even more the sampling rate of a trace as it flows through the pipeline. So at another point of the pipeline, you can say, no, I'm not going to sample this one here, even though it was saved… said to be sampled. So you… Oh, I see what you mean.
Dan Gomez Blanco 00:36:15 It's not, like… Yep.
Juraci Paixão Kröhling 00:36:18 Yeah, so it is not about this one here. I mean, I would ask for a clarification there, like, oh, Given a trace, and given that the parent span.
Made a decision not to sample.
what do you do with the child's fan? If the child's fan has this always record.
the new sampler that you're talking about, like.
Dan Gomez Blanco 00:36:39 Is he talking about parents' bands here? I think, you know, it's just…
Juraci Paixão Kröhling 00:36:46 Yeah.
I mean… Apart from the parent spend scope, like, I… I don't… I don't… I don't understand this issue.
I would like to have all generated spans go through the spend processor, and I'm assuming the spend processor here is the SDK processor, not a collector, right? I mean…
Dan Gomez Blanco 00:37:09 Yeah.
I mean, but…
Juraci Paixão Kröhling 00:37:11 Regardless.
Dan Gomez Blanco 00:37:11 Yeah, I just… I didn't really understand what you said there, like, you've got… if you've got the always-on sampler, not the composable one, because you've got the composable.
Juraci Paixão Kröhling 00:37:19 Yeah, yeah.
Dan Gomez Blanco 00:37:19 Because the, you know, respect the parent decision, if you have the raw, always-horn sampler.
Juraci Paixão Kröhling 00:37:24 Yeah, always simple, yeah.
Dan Gomez Blanco 00:37:27 Yeah, so it doesn't match with the… If the pairing spam one sample or not, right? There's no… no context taken into consideration here, it's just like… Always on.
Which is not generally what people do, because they use a composite sampler to say, well, at least, you know.
Juraci Paixão Kröhling 00:37:43 Take into consideration.
I… let me reread the specter, but my understanding is… the first source of information is the parent. Like, if a span is part of a transaction already, the decision made at the parent takes precedence over anything. If you don't have a context, then the sampling from the sampler The decision from the sampler kicks in.
But always, and always simple.
Is in respect to the parent, like, the root span.
Dan Gomez Blanco 00:38:19 The decision of…
Juraci Paixão Kröhling 00:38:21 Yeah. The simplest decision is always taken at the root span.
Exactly, because you can propagate that decision down the… to the other services through the trace context specification. One of the flags in the trace context is the samples flag.
Dan Gomez Blanco 00:38:43 Yeah…
Juraci Paixão Kröhling 00:38:46 Let me look at this back, I mean, just to be 100% sure.
Dan Gomez Blanco 00:39:11 Maybe I'm… I mean, it really makes… I mean, I agree with you, but, like, I seem to remember there was a… Maybe that changed, actually.
Yeah, there's the pairing-based, right?
Juraci Paixão Kröhling 00:39:49 But the parent-based is when you have the ratio. Like, when you have a… parent.
That said, we are taking 20%, then you are taking the 20% of what the parent said, like.
This is confusing. Hold on a second, let me… So, okay, recording sample reaction table, so there's a table here. If the samples flag is true.
then it's true. If it's false, any spend processor receives SPAN, I… There we go.
Okay, so this is the link here to the… to how the behavior should actually be.
Dan Gomez Blanco 00:40:55 I think in the… I'm just looking at… So I remember in Java, like, the… The default sampler is the parent-based in Java.
If you configure the SDK… the agent, for example, right?
It's not the always-on.
Which… So they're different… different ones.
Sorry, you shared a link in the chat, okay, yeah.
Juraci Paixão Kröhling 00:41:36 But yeah, but it's not exactly that part.
It's a little bit before that.
Dan Gomez Blanco 00:41:49 Yeah, so in the built-in sampler, we've got the built-in samplers, we've got always on, Which is… You know, recording sample always.
And then we've got the pairing based.
Which is…
Juraci Paixão Kröhling 00:42:05 Right.
Sorry, go ahead.
Dan Gomez Blanco 00:42:08 It's… so the default is always on, if the remote… this is the table here, right? But this… and then Java, I'm not sure about other… I mean, I'm assuming that the default in other languages is the parent-based as well?
Which… Does that, you know, makes that decision that you mentioned there, but, like… This one is something that the always-on… I don't know if many people are using that, because that completely disregards the sampling decision that happened before. That was my understanding, maybe I'm… Maybe I'm wrong here.
And this is the decision… the reason why…
Juraci Paixão Kröhling 00:42:48 Yeah, you're right. I mean, I had the impression that always-on, with respecting the parent, would be the… like, that always-on means, the parent base.
Always on.
But this is just a default, right? So if I override… I mean, it doesn't make sense to me, but yeah, it is what this guy says.
Dan Gomez Blanco 00:43:10 It's… yeah, I think, at least, you know, I'm looking at the Java code as, yeah, it's basically that, like, always honest, always a yes, like… M…
Juraci Paixão Kröhling 00:43:19 Okay, so what they want is always on.
Dan Gomez Blanco 00:43:23 Yeah.
So maybe that's it, that's the question here, it's like, how is this not already implemented by the always-on.
Juraci Paixão Kröhling 00:43:30 No more.
Dan Gomez Blanco 00:43:51 Also, another thing that I… I can't remember exactly now in this bag.
If, at what point is the on start called? Is it after the… so on processors, on spam processors, is it after?
The sampler decision is made.
I don't… I don't… I've got my hand raised for some reason, and I don't know how to stop it while I'm sharing my screen.
Anyway, isn't that another one? Another sort of, like, issue here? That…
Juraci Paixão Kröhling 00:44:37 So, I have a… this pack here for that part, so it is, like, spend processor.
Basically, it is… it's fan.start, And then… the processors.
own star.
Dan Gomez Blanco 00:45:02 to es… Alright, so the spam processors are invoked only when edge recording is true. Okay, so it's after… the span is…
Juraci Paixão Kröhling 00:45:11 Yeah.
Dan Gomez Blanco 00:45:12 Yeah, okay.
Maybe that's what the… So they want to process bans before this happens.
Juraci Paixão Kröhling 00:45:21 Oh…
Dan Gomez Blanco 00:45:23 Maybe I'm starting to get it now.
Juraci Paixão Kröhling 00:45:26 Yeah.
Yeah, okay. Now, okay, yeah.
Dan Gomez Blanco 00:45:35 Right, so I think my comment here doesn't make a lot of sense, because the… I guess what they're trying to do.
Sampling is basically Having a processor.
I'll clarify that.
M.
Juraci Paixão Kröhling 00:46:00 Yeah, no, it makes sense.
Dan Gomez Blanco 00:46:26 Yeah, but then… So instead of a sampler that… so what do you expect to see? A sampler that always returns a sampling decision that includes the record… recording the span, okay?
Or, the ability for the spam processor to interact with spans regardless of the sampling decision. Okay.
So I think that ore doesn't really… that throws me off.
Mmm… Always recording something which replaces any drop decision will record and drop.
I see.
So is that record… Always record something.
Yeah, okay.
Recording drop.
Which basically means… You can… it still goes through the processor, but then it's dropped.
And we don't have something like that already.
K's not.
Did I record?
Severin Neumann 00:47:53 I mean, I mean, in respect of time, is it really, like.
Dan Gomez Blanco 00:47:56 Sorry, yeah.
Severin Neumann 00:47:57 required to… to spend that much time going on that. I mean, I totally understand, like, but…
Dan Gomez Blanco 00:48:03 Yeah, I understand the thing, the… yeah, so decision with record and drop, I think this is, SIG issue for sampling?
Or…
Severin Neumann 00:48:13 Yeah.
Dan Gomez Blanco 00:48:17 And we can put it into their… Project.
Do that? Do anything?
Right?
Okay.
In the interest of time.
That's done.
This is already… Creative for entities, it seems.
So, sick issue?
this label play.
Severin Neumann 00:49:22 Is this entity sig, then? Because it's, like, tagged with entities.
Dan Gomez Blanco 00:49:28 So it sounds like it.
Severin Neumann 00:49:29 There's been sick issue, and we should put it on their board.
Yeah, naming for entity attribute fields to issue a grenades from the… so… I think there's a board for… entities, so…
Dan Gomez Blanco 00:49:45 So entities phase one, but…
Severin Neumann 00:49:47 Yeah.
Dan Gomez Blanco 00:49:48 I'll just add it there, and then…
Severin Neumann 00:49:50 I mean, they can still, like, move it somewhere else, but… I suspect it's like… Where is this coming from?
Dan Gomez Blanco 00:49:57 I always wonder in these if there's… Wonder… if I wonder if we should… Tag them.
I'll type in.
Okay, yeah, but that makes sense.
Cool.
Okay, two more. Composable… Rules sampler.
Description is incomplete.
Guess.
Severin Neumann 00:51:10 Oh, drawer…
Dan Gomez Blanco 00:51:11 We assigned this to…
Severin Neumann 00:51:12 Sampling.
Dan Gomez Blanco 00:51:14 I'm blessed.
Severin Neumann 00:51:15 Oh.
Dan Gomez Blanco 00:51:31 you know, make another comment like that. So I don't know if people actively triage their port, you know.
Hmm.
We don't have a sampling… Maintainers, or something, or approvers.
Severin Neumann 00:51:55 No, I don't think so. Maybe they should have some.
Sometimes, also, they do, add sampling, like, sometimes it does not work that well, like, you know.
Dan Gomez Blanco 00:52:08 Nope.
And… if I do, like… Yeah.
It should be something… Yep, nope, doesn't appear.
I guess I'll just leave it there.
Let's take issue.
And this one is… The one that we just opened.
Give it a thumbs up.
So… Do we… 1, 2… Filter out editorial from… Triage.
Or… Or maybe this is accepted, or… Community feedback.
Severin Neumann 00:53:01 Yeah, put it on feedback, because, like, I still need also, like… I'm especially curious what people like Patrice think about it. I remember vaguely that we discussed that, like.
2 or 3 years ago, but I do not remember what we… what we tried to do, so…
Dan Gomez Blanco 00:53:21 Cool. Makes sense.
Okay, so that's all of them.
Is there anything else we want to… We'll have a look at the community.
I think.
And… there's a fine.
This should be a project proposal.
The label.
Can we merge this, by the way?
It's got a lot of approvals.
Severin Neumann 00:54:10 Yeah, I think that was the goal, right? I think, didn't we even, during the last GC meeting.
Better log, it should be fine to… good to go.
Dan Gomez Blanco 00:54:20 Right, and Dalton just said… I'm happy to… potentially create an approach to what Athena said to do.
That's the only comment that is left.
So they create a new board and they move stuff, but, happy to… Resolve this comment.
Are you happy with me, sort of, like, Marking this as resolved.
Severin Neumann 00:54:46 Yep.
Dan Gomez Blanco 00:54:59 And… Let's merge it.
Yeah, definitely have enough.
Who do it.
And the rest is fine.
Is this… GitHub membership? No.
What radius do we have?
Maintenance on GitHub.
So, see, I don't know exactly what can be done via the admin.
I know that…
Severin Neumann 00:56:11 No, I mean, the scripts, we just have to create them, right? I thought Trask can do it, I mean, technically I can do it as well, so… yeah, just tag it as area GitHub, and… so we cannot do yet…
Dan Gomez Blanco 00:56:24 Team. No, wait.
Severin Neumann 00:56:25 we have to… I think we have to add the group to the admin repo, and then once it is created by Terraform, we have to add the members manually, because that's not yet managed. I think that was the story. Yeah, exactly.
Dan Gomez Blanco 00:56:39 We don't create teams, or… yeah, okay.
Severin Neumann 00:56:42 We create them, but we don't populate them, so you can create… go over into the admin repo and And… and trade it, but I think that was the… that was how it goes.
Dan Gomez Blanco 00:56:53 Alright, I had no idea what this is. Feedback issue.
Pablo Baeyens 00:56:57 I think that's for the blog post that Boston is working on, but we can ignore it for now.
Dan Gomez Blanco 00:57:07 GKE Autopilot.
Do we label this? As, mrs. Sigemfra?
Project, non-GitHub project infra.
Sounds like it.
Severin Neumann 00:57:43 Yep.
Dan Gomez Blanco 00:57:53 These aren't old, but… open source, like, this is… That's not infra, is it?
We don't really have a label for this, do we?
I think.
Severin Neumann 00:58:30 I mean, it's kind of infra, right? I mean, at the end, the big question is, like.
I think Brad asked back then, like.
Dan Gomez Blanco 00:58:44 If we're using the open source offering from JetBrains.
Yeah.
I… Dunno…
Severin Neumann 00:58:59 I mean, it stalled, right? I mean, the thing is, like, I asked Brad back then, like, to race this, but, like.
Dan Gomez Blanco 00:59:13 So who's managing this? .
Severin Neumann 00:59:16 Yeah, it looks like the PHP SIG, they have, like, reached out to ChetBrains, and I have, like, the 3 licenses for the… Php thingy, and .
Dan Gomez Blanco 00:59:44 I mean…
Severin Neumann 00:59:47 Yeah, I mean, he even offered to help with that, right? I mean, maybe just to, like, yeah, please go ahead and do that, and expand it to the project, and then, like, people can… can reach out. So, yeah, why make it complicated? That's my question. I think we just forgot to… To handle that, so…
Dan Gomez Blanco 01:00:06 Yeah, I think we should just say, you know.
Juraci Paixão Kröhling 01:00:10 And then it should go to the assets that we have, right? So there's the assets.
Severin Neumann 01:00:16 I think that was the ask then to say, like, that Brad just texted that he… He kind of owns that, so…
Dan Gomez Blanco 01:00:26 Yep. So, assets… I say that, will you be willing to work with.
JetBrains to expand within this group.
Or this license.
To generate open telemetry and add the entry to the assets file.
Yep.
I'm just asking.
I guess.
Right, and I think that's all we had time for.
Severin Neumann 01:01:36 Yep.
Awesome.
Juraci Paixão Kröhling 01:01:40 Looks good.
Dan Gomez Blanco 01:01:41 Good triaging.
It's just now that I stopped sharing, I just go, like, you haven't spoken in a while, so we'll lower your hand, no way.
Juraci Paixão Kröhling 01:01:51 I never get this.
Dan Gomez Blanco 01:01:53 thing with Zoom. Anyway, yeah, thanks for coming. Krisha, thanks for joining.
Juraci Paixão Kröhling 01:01:59 See you, folks.
Dan Gomez Blanco 01:02:00 Yeah, if you find…
Juraci Paixão Kröhling 01:02:01 Training.
Dan Gomez Blanco 01:02:01 problems crucial, like, you know, joining meetings or anything like that.
Got it, yeah.
Kushal 01:02:07 Yeah, sure.
Dan Gomez Blanco 01:02:09 See ya, bye-bye.
Kushal 01:02:11 Bye-bye.

SIG: LLM Semantic Convention WG
Date: 2026-06-23
Duration: 35 minutes
============================================================

## Zoom Recording Transcript

**Steve Rao** 01:17 Yeah, hello.
**Trask Stalnaker** 01:18 Safety… Hey, Jack.
**Jack Gordley (Grafana)** 01:26 Hey, everyone.
Nice to meet you.
**Trask Stalnaker** 01:28 Yeah, welcome.
**Jack Gordley (Grafana)** 01:36 I was planning on doing a little intro, but I guess I can wait… wait a second.
**Trask Stalnaker** 01:41 Yeah, are you, also, are you able to join the meeting in an hour and a half?
Did you see that there's two meetings?
**Jack Gordley (Grafana)** 01:52 Yeah, I did see that. Yeah, I can join that one, too.
**Trask Stalnaker** 01:59 Good morning, Lindula.
**Liudmila Molkova** 02:02 Hello, everyone.
**Trask Stalnaker** 02:14 Yeah, let's… oh, let's see, we've got… Agenda, yeah, so, Jack, why don't you, introduce yourself. Welcome!
**Jack Gordley (Grafana)** 02:27 Cool, yeah, thank you.
Yeah, so I'm Jack, I'm a software engineer at Grafana, and we are, working on some AI observability, like, new AI observability products, and… interested in learning more about what we can do to contribute to the GenAI SIG for, like, for AI, so, we did a little bit of discussion, we have, like, an SDK that we've been, like, starting.
for this kind of thing, and realized that, like, why are we kind of… why are we going against the grain here on our own conventions when we should be, you know, helping to align the SIG? So, anyways, just looking for any ways we can get involved, and yeah.
**Trask Stalnaker** 03:11 Fantastic.
**Liudmila Molkova** 03:13 Welcome. I'm excited to see you.
And yay.
Sigil is awesome, but we should… Right, good stuff.
**Jack Gordley (Grafana)** 03:23 Yeah, exactly.
Yeah, we spoke to Ted Young at the… we had, like, an off-site, and he kind of ran us through where we're at and what we can do, so… yeah, looking forward to getting started.
**Trask Stalnaker** 03:38 Alright.
Jeremy, welcome!
Introductions are totally optional.
**Jeremy Eder (Red Hat)** 03:47 Hey! How's it going? My name is Jeremy Eater, I work for Red Hat, IBM, and we… We sell AI-related platform infrastructure products, and… We are in desperate need of standardization in the space that you guys are in. So… Great. We don't know what to do just yet.
**Trask Stalnaker** 04:11 Yeah, sounds like you're in the same place as all of us.
**Jeremy Eder (Red Hat)** 04:14 Well, this is the thing, dude, because I spent the last couple days finding you people, like, trying to find where the center of gravity is here.
**Trask Stalnaker** 04:21 Hmm.
**Jeremy Eder (Red Hat)** 04:21 And so it took me a while to come kind of stumble on this, so here I am, but… I don't know if there's other places we should be looking, but, you know, here I am. And by the way, Red Hat, as you can imagine, like, all our stuff is hotel, so it would be ideal if we had It's all sorted.
**Trask Stalnaker** 04:38 Yeah, there's some, related… there's some work going on Well, there's some working foundation… Related work. In Linux Foundation, there's the AAIF, Agentic AI Foundation.
And they're doing… they have an observability track.
I liaise with them from OpenTelemetry side, and their goal is to, work out, work through their use cases, but then contribute the conventions to the OpenTelemetry Gen AI semantic conventions.
So it does feel like… I think we have gravity here.
There's also the LLimetry and open inference, who have been far ahead, in this space.
With instrumentation support, and Open Inference also has some semantic conventions they've defined.
We've recently, worked with Open Inference. They've donated their code to us. They're continuing to work in their codebase, but they gave us, basically, permission to, use their code to kind of help accelerate our instrumentations.
With our semantic conventions.
But yes, there is… there's a lot of different things out there, and… worth…
**Jeremy Eder (Red Hat)** 06:17 Yeah, thanks for flagging the, the Linux Foundation one.
That had slipped my mind, but it's cool that… so y'all are working together, and they consider their landing zone for their decisions to be this codebase?
Is that fair to say?
**Trask Stalnaker** 06:34 Yeah, the… the semantic conventions.
**Jeremy Eder (Red Hat)** 06:37 Yeah. Yeah. Yeah. And then this code is actually delivered from these conventions.
Downstream.
**Trask Stalnaker** 06:46 Yeah, so generally with the conventions, we require prototypes, so we require some code, like, to prove out the conventions when we accept the conventions to begin with.
And then… We have in… OpenTelemetry, we have instrumentations, for different languages, mostly Python, but other languages, some other languages as well. A handful of the myriad of, Gen AI libraries out there, and that's where we're, leaning on the… going forward, going to start pulling in the open inference, or transforming some of the open inference work into open telemetry.
To try to cover more of that.
There's also, like, you know, obviously products and proprietary things that other people are building, cloud platforms, that use the Gen AI semantic conventions.
**Jeremy Eder (Red Hat)** 07:58 Got it. Okay, thanks a lot. I… Yeah, I have some… I'm gonna say I have to come up to speed here.
So I guess the last question is, just to make sure I'm in the right place, is I don't know if you've got, Personas or use cases written up that you're… that you're attempting to solve that we could… Maybe either contribute to, or at least become stakeholders for.
**Trask Stalnaker** 08:22 Yeah, so just checking, have you found this repository?
**Jeremy Eder (Red Hat)** 08:29 Yeah.
**Trask Stalnaker** 08:30 Great. So this is where all of our work Well, I shouldn't say all. This SIG is both a semantic convention SIG and an implementation SIG, kind of combined.
So all of the semantic convention work is happening here.
Most of the… Implementation work, instrumentation work.
At this point is happening in this repository.
And so, yeah, like, it's… My recommendation would be, you know, peek through you know, kind of come up to speed on what's there today, and peek through the PRs.
And issues for things that you, are, you know, have knowledge, like, have, are, have domain expertise about, or are problems that you're running into, in your org.
That you can kind of contribute, Your perspectives, or, like, just any kind of feedback on them. Yeah, it's great to have stakeholders, people who… If we make mistakes, it's gonna hurt them. If we do something good, it's gonna help them.
**Jeremy Eder (Red Hat)** 09:56 Okay, so I can just… maybe towards the end of the meeting, we can save some time, I can go through what we're trying to do, and why we think we need this stuff, and what parts of it would help.
Well, I don't want to hijack the meeting, I just got here.
**Trask Stalnaker** 10:09 Yeah, yeah. Sounds good.
So, let's jump off, steve.
**Steve Rao** 10:17 Yeah.
Yeah, firstly, I… I list, a PR. Yeah.
**Trask Stalnaker** 10:27 Cool, yeah, looks like this one is ready to go.
One variable.
**Liudmila Molkova** 10:37 It seems OpenAI is going to drop this feature.
By the end of the year.
Completely removed, it's already deprecated.
I don't think we need to change our plans, because there are other systems that would support it.
But, I'm… curious… I mean, the version, the prompt name and prompt version.
I'm curious if you folks… if it changes any of your plans.
**Steve Rao** 11:11 yeah, for us, designing a change?
Yeah, currently, we don't have any, change to… To do any, different things, yeah. But, yeah, I very appreciate the, maintainer to leave the comments, yeah, to remind us this point.
**Liudmila Molkova** 11:39 Oh, Alex already left the comment.
**Steve Rao** 11:44 Yeah.
Yeah, for this point, yeah, do you have any, suggestions, for me to, to adjust this PR or not?
Is there anything I need to do?
**Liudmila Molkova** 12:02 Oh, we usually have… go ahead, Jessica.
**Trask Stalnaker** 12:05 Is there any other support?
outside of OpenAI for these fields.
**Steve Rao** 12:11 Yeah, you can… you can go back to the comment, yeah.
**Liudmila Molkova** 12:18 The bedrock, right in front.
**Steve Rao** 12:21 The first one is OpenApp, the second one is AWS. And, yeah, for, For Alibaba, there is a team, they want to, support a similar, feature.
**Liudmila Molkova** 12:37 Well, you've never.
**Trask Stalnaker** 12:38 supported… oh, go ahead.
**Liudmila Molkova** 12:42 If OpenAI removes it, when OpenAI removes it, we still have to… Likely two different versions of it, implementations, so we still have the rule of two applying.
**Trask Stalnaker** 12:56 How is Alibaba team planning? Is… is that going to be exposed in your API?
Or would use… how would users provide the prompt name and version?
Do they have to manually tag things? Is this for a hosted service?
**Steve Rao** 13:15 Mmm, okay, yeah. They are going to launch this product, but, so far, I'm not sure, is there any documentation, to introduce this point.
Yeah, maybe I can discard with them, Tomorrow, and is there any, documentation, I will, Lisa.
On the PR.
**Trask Stalnaker** 13:49 Cool.
I'm also okay, I mean, if… We want to merge it.
Regardless.
Wouldnilla, if you have any reference.
**Liudmila Molkova** 14:01 Let's, let's merge it.
I can hit merge.
Or you can hit Merge, yeah.
**Trask Stalnaker** 14:12 Loved hitting that big green button.
**Liudmila Molkova** 14:14 Oh, yes.
**Trask Stalnaker** 14:18 Alright, how to find events… .
**Steve Rao** 14:24 Yeah, this is another, topic. There is a team in, our company. They want to, define the, semantic convention of logs.
So far, they, create, they send a PR to, our, Alibaba semantic convention, JNI semantic convention.
But, a… They also, they also hope to, bring this, topic to, Autel GNI's semantic convention, but so far, they don't propel it very well, so they, send a PR to our, a generalized manic convention, but there is a point I'm not very sure.
How to define the JNI log semantic convention? I found in JNI semantic convention, there is a concept called events.
or, Yeah, I'm… I'm not sure how to define this, content. Yeah, there is any suggestion or recommendation, yeah, I want to hear from you.
**Liudmila Molkova** 15:48 So what is the… Thing, like, what kind of event, what information does it carry?
**Trask Stalnaker** 16:00 Just to replace… is it, like, a back-end choice of some… you want to capture logs instead of spans, or is this additional information that can't be captured on spans?
**Steve Rao** 16:12 Yeah.
especially in some, scenarios such as, Cloud Code, for some, coding agent, like, Cloud Code, it's not so, so easy to, instrument the, the AI agent. So, another way to collect the, Observability data is to collect, logs, based on some hooks.
So they, use the logs to, collect the observability data.
Yeah, I think this is the one point why they want to define the JNI log semantic conventions.
**Liudmila Molkova** 17:12 So it sounds like something external that we don't control, that generates, like, cloud-cut logs on its own, and we want to document their… what they… Send.
**Steve Rao** 17:28 they, they provide, a collection, too, like, yeah, we can, we can, think, it's something like, gen, hotel Python agent, something like that.
And for users, 4 users, they use, Cloud Code, they just need to, install the, 2, and the two will, send some, logs.
According to the… JNI logs a semantic convention.
Instead of the, logs, Sent, sent by, application.
**Liudmila Molkova** 18:19 So we… it sounds like it's not the specific thing you want to describe. It's more like, our log.
And for those, we don't define conventions, Like, at all?
If you know what you want to… R… describe. Then there is, yeah, the concept of events, and this is essentially a log.
That has a certain format.
there is one event defined in GenAI conventions for, inference details or something. It's effectively a replacement, and we have a guidance in semantic conventions on how to define events In general.
If you just capture something external.
Well, you could document its structure, but it probably shouldn't be in hotel semantic conventions.
If you want to define your own conventions for it.
Awesome, no concerns. But the first question is, what does this thing represent? If it's anything, then probably there is no convention.
Or maybe your question is, when you… use something like a log bridge. Like, if you use a library that creates logs, how they are… Mapped to open telemetry.
**Steve Rao** 19:56 Yeah, maybe you can, yeah, Chaska, you can, click on the fire change. Yeah, there are some, events.
The guy, A fire changed. Changed.
You can scroll… scroll down.
you can, click on the, JNI logs.
dot empty.
You… Jni looks, Though MD.
**Trask Stalnaker** 20:36 Yeah, this one.
**Steve Rao** 20:39 Yeah.
Yeah, I, I think, he, used some attribute from, Hotel JNI semantic convention, but, he defined a lot of, events.
And, in the events, they defined some, JNI, related attributes. And, what he want to do, I think he wants to, use the logs to collect some observability data, replies, spam.
Something like that.
**Trask Stalnaker** 21:18 So the main question I have is, if this is… I mean, we probably aren't at the point here with GenAI where We want two different modelings.
Like, the thing of, like, HTTP… we have HTTP semantic conventions, but then there's also the idea that, like, HTTP logs are common, you know, and web servers emit HTTP logs, and what would a common HTTP log format be?
And we haven't even really… define that. Like, the semantic conventions is more like a pure modeling, like, what's our ideal modeling?
And if these are… these seem like… Things that can be derived from These semantic conventions?
Is that fair? Like, if you… if we are… if we omit the real semantic conventions.
Are these all derivable from that?
**Steve Rao** 22:32 Yeah, you mean…
**Tom** 22:37 On a yes.
Most of these events are on the start.
and the end of, span. But sometimes, the recording point is in a hook. Maybe it is not quite convenient to record a full span there.
And, as you see, the events, quite flexible, and they don't need to be closed on the end if the, agent crashed, yeah. And, also, there are some, events that the… span attributes, that… Don't cover.
Upload there.
the human review, that… that the hook asks you to, approve, an action. So… so such… events, I think they don't have… Hmm.
Enough?
meaning for, spend, because the time… the duration doesn't matter, actually, that it's just an event. So… So I think recording our event is proper here. However, there is, there's no semantic convention for For… for this… So… so I proposed the… the… issue, in this repoitory.
**Trask Stalnaker** 24:18 So, I would split the… split these into two different cases here. One is the things that are… and the point about spans emitting events on span start and span end.
That's actually a very common request, in OpenTelemetry, and if you look around the spec and semantic convention repos, you'll find, discussions about that.
And that's the direction I would pursue for that, is we don't need a new semantic invention for those… that kind of event. What we need is a common Way to… just a common mapping for all spans to emit a span start and a span end event, that people could opt into, say.
The… The other category is things that, like you said, the human evaluation, something that maybe… that we don't have already covered in semantic conventions, and which should be, you know… like, basically, I would raise that as an issue in the semantic convention.
And if it turns out to be modeled better as an event than a span, then great, we'll, you know, add it as an event.
But, you know, just kind of more proposed, hey, here's a gap in the semantic invention, and then, you know, discussion can happen over what's the best modeling for that.
**Tom** 25:55 Okay, so, What's up?
I have a question, is that… is… events are supplementary elements of SPAN, or The event itself can… can be an event stream to log everything.
What's its position in the, open telemetry model.
**Trask Stalnaker** 26:26 If something has a… we actually have some guidance here, but in essence… Or, let's just pull this up.
Even… Not docs… Non-normative… No.
**Liudmila Molkova** 26:52 It's in the Docs General Events MD.
**Trask Stalnaker** 26:57 Thank you.
When to define events. Here's what you want. I can drop this in the… When to define that event. Occurrence does not require a new trace context or child operation. It represents a checkpoint.
It's out when not to define events, operations that have duration, Use spans… Right, so… Check this out.
Should help. But in general, we, you know, if… if it… for… we would prefer… I mean, we're going to define… Span, like, that case of emitting an event on span start and span end.
We're… I don't think we're going to define events for span start and span end in Gen AI. I do think there's… if you find the discussions There's interest from some people in defining those more generically for all spans that some people find… might want to use.
**Tom** 28:15 Yeah, okay, thank you, I will check it out.
**Trask Stalnaker** 28:18 Great.
**Liudmila Molkova** 28:20 Thank you.
**Trask Stalnaker** 28:24 Looks like the next topic is, probably for the May… the, 9 a.m. Pacific time meeting.
Oh, and we only have 2 minutes left, Jeremy, you want to try in 2 minutes to…
**Jeremy Eder (Red Hat)** 28:45 Well, I can…
**Trask Stalnaker** 28:46 wherever you are.
**Jeremy Eder (Red Hat)** 28:46 Maybe. I don't know why there's a second meeting, actually. Maybe I should be going to the other one?
**Trask Stalnaker** 28:52 Yeah, yeah, so the other one is… has been our main meeting. This meeting we added to the calendar, to, meet with the… primarily to overlap with the Alibaba folks in China.
Because the next meeting time is too late for them.
**Jeremy Eder (Red Hat)** 29:14 Yeah.
Okay, I'll join the other one in a minute. Well… the TLDR is we want to find a… business practical way to expand our use of CodeGen.
And in order to do that, we need… Instrumentation throughout our entire SDLC, and… This… the agent trajectories are… An area we want to optimize.
It's just basically around costs, yeah, yeah. So I'll.
**Trask Stalnaker** 29:47 As an end user of the.
**Jeremy Eder (Red Hat)** 29:49 Yeah, exactly, exactly. I work for… I work in the AI business unit here, but my focus isn't on our products, it's on our infrastructure.
**Trask Stalnaker** 29:58 Fantastic.
**Liudmila Molkova** 30:00 We're excited to talk about deadline trajectories.
We're long overdue to have some stance around them in semantic conventions.
**Jeremy Eder (Red Hat)** 30:10 Well, I can tell you what we… what we need, and maybe we can figure out how to do it. So, I'll join the next meeting, though, instead of holding people here.
**Liudmila Molkova** 30:18 Yeah, it's just not in 1 minute, but in 1 hour.
**Jeremy Eder (Red Hat)** 30:21 Got you.
**Trask Stalnaker** 30:23 Thanks. Bye.
**Liudmila Molkova** 30:24 Thank you.
**Trask Stalnaker** 30:25 Bye.
**Steve Rao** 30:26 Yeah, bye, thank you.

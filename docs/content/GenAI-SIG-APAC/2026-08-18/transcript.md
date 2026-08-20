SIG: GenAI SIG (APAC)
Date: 2026-08-18
Duration: 30 minutes
============================================================

## Zoom Recording Transcript

**Trask Stalnaker (Microsoft Corporation)** 02:14 Hey folks! Sorry I'm late.
**Steve Rao (Alibaba Cloud (Singapore) Private LTD)** 02:18 Hey.
**Trask Stalnaker (Microsoft Corporation)** 02:19 How are you all… how are you all doing?
**Steve Rao (Alibaba Cloud (Singapore) Private LTD)** 02:24 Yeah, yeah, I'm good.
**Huxing Zhang (Alibaba Cloud (Singapore) Private LTD)** 03:05 Hello? Trask?
**Trask Stalnaker (Microsoft Corporation)** 03:06 Have you ever seen… Let's see, you've got the first topic here… Tracing plugin for Deep Sea Carness.
You'll have one.
**Already… Huxing Zhang (Alibaba Cloud (Singapore) Private LTD)** 03:28 Yeah, I just want to share that we work… that we work with have done a couple of days before.
this deep-seq harness has been published, like, last Friday, or last Thursday, and then we're working… we're working… being… we have been working on this… for the recent days, and then we have this, OpenTelemetry plugin for… Deep SIG harness, and I think I… that's one thing that I want to share with the community.
And, What I want to mention is that, the deep-seq harness has native OpenTelemetry exporter, but it only, It only generates the logs and the sessions, events.
And to… it's like reporting, like, a log to a backend… to the hotel backend, but it doesn't provide the… tracing and metrics, outputs, so we have been doing that. We have built that plugin.
And, an, an over… overview of, like, you have to… you can… see the… you can scroll down to… there's a screenshot where you can send the trace to, like, Landfuse or other… Open source backends, and you'll see that the LM calls the chat, and everything that we can do.
we can capture that with the GenAI GenAI conformant, spends.
Yes, that's one thing I want to share, but, I don't know if the… there's the… any interest in this… in OTL community, that this can be, like.
Part of that, you know, would be, good.
And we can, like, we can send a PR if there's a good place.
To, to, to, like, to… To have this plugin, but I don't… I'm not sure whether it's appropriate to, like, to… where should I put this, right? So, okay.
That's my questions.
**Trask Stalnaker (Microsoft Corporation)** 06:10 Yeah, so it's… JavaScript… I mean, it certainly seems like it would be… Interesting from… As we are modeling Semantic conventions to be able to validate against is… Agentic loops… There's… Example… oh, no, I did want GenAI… There's a… PR… here we go, the sort of agent delegation and handoff.
Would that be applicable?
I don't know.
Maybe not, but… Yeah, what, let me, I'll bring it up on the general, call in, you know, an hour and a half.
And see what, folks… Think.
**Huxing Zhang (Alibaba Cloud (Singapore) Private LTD)** 07:38 Yeah.
Yes, it's another… Wider topic is that for the coding agent, we have actually quite a lot of coding agents.
and codecs.
Cloud Code or OpenCode, we actually provide support for various kinds of that, so… I… actually, I want to… I'd like to, ask if the… there is a… kind of… SIG or other form of, Organizational other things to, like, to… talk about the… observability for coding agents, simply. That's what I'm thinking about, but I'm still not find out, a good, a good place to discuss this, but this, an idea that came out.
for me for a couple of days right now, so I would like to bring it up.
And see if there's anything that we can do in this community.
**Trask Stalnaker (Microsoft Corporation)** 08:57 Yeah, So, sort of taking… because I know, for example, like, Copilot has… you can emit open telemetry from it.
I imagine there's… The, sort of, there's some baseline telemetry that… Is already described by the semantic conventions?
And so, you're thinking, sort of, to go a little bit deeper into, Capturing things that are specific to coding agents, as opposed to generic agents?
**Huxing Zhang (Alibaba Cloud (Singapore) Private LTD)** 09:37 Right, for coding agent, and we have, like, we have, instrumentation for Java are written in Java, or Go, or Python. By the way.
don't have… I'm not sure if there's any instrumentation provided for specific coding agents, like Codex, OpenCode, or other… other coding agent.
**Trask Stalnaker (Microsoft Corporation)** 10:07 Oh, I see, building nodes, yeah.
That's a good question. I don't know… If there is… I think some of them have some open telemetry support, but I'm not sure.
**Like, I know that Copilot does… Huxing Zhang (Alibaba Cloud (Singapore) Private LTD)** 10:29 Yeah, some of them may have, we provide hooks that we can do things, like, we can capture them, but they… normally they don't provide native support, I think. So we actually have to hook them, and to transform these, like, events or sessions, logs, or this, kind of data to that OpenTelemetry compatible format. That's what we have been doing for recent days.
And, because of this coding agent, they are variant across different languages. Some of them build on JavaScript, TypeScript, some of them they be building on… maybe Rust, or Go, or other languages, so… they can't be, like, simply divided into… by languages, I think, so we… I think we can… I think these coding agents, like, can be a kind of form, group of, interest, maybe. Or… Just an unfamiliar, unmature idea that… came up that maybe we should have a SIG. But, yeah.
That's what I'm thinking about, yeah.
**Trask Stalnaker (Microsoft Corporation)** 11:54 Cool, yeah, like, I can see… I mean, we can definitely float the idea, I mean, you could… could always open a community issue to sort of… Get, see how many people would be interested in, dedicated conversations around coding agents.
Certainly, I think this SIG… it could fit in this SIG, So, I think it would be okay to have those discussions in the SIG, if there's not enough, like, dedicated interest to create a new SIG?
But it would probably be a… Kind of depends on interest and demand.
**Huxing Zhang (Alibaba Cloud (Singapore) Private LTD)** 12:46 Okay? I tried to bring up an issue on the community repo.
**Trask Stalnaker (Microsoft Corporation)** 12:55 Cool. You could also open one in the GenAI repo… Oh, okay.
I'm trying to think… that might get more… more of the right eyeballs, or maybe open one in both places, and cross-reference them.
**Huxing Zhang (Alibaba Cloud (Singapore) Private LTD)** 13:13 Sure, sure.
**Trask Stalnaker (Microsoft Corporation)** 13:24 Cool. Steve… Steve Rao (Alibaba Cloud (Singapore) Private LTD) 13:29 Yeah, high cost.
**Trask Stalnaker (Microsoft Corporation)** 13:30 I mean, hey!
**Steve Rao (Alibaba Cloud (Singapore) Private LTD)** 13:33 Yeah, I… yeah, you can scroll down.
I left a comment.
Below. And, yeah, this is a, previous, issue about to add adding a scale semantic convention to GenI.
And, yeah, I found, It's a long time, no people to discuss about this, but, yeah, we have, demand to, to, construct, related semantic conventions, so I… I want to… Yeah, ask the community, is there any, feedback or, idea, for, at this point, to construct a scale-related, semantic convention?
**Trask Stalnaker (Microsoft Corporation)** 14:38 Yeah, I'm wondering why this hasn't been… More active… Question, except… maybe, Maybe a lot of… maybe some harnesses already capture skills as tools?
to a cause… Yeah. Or maybe it's not… Well, no, it doesn't really matter if it's not, like, making remote calls, because we have a lot… we capture tools for local executions.
As well, just to see what's happening.
**It's a good question. I… I don't know the answer, but, I can… Definitely ask, With the larger group, probably some folks there will have ideas on what the current… Steve Rao (Alibaba Cloud (Singapore) Private LTD)** 15:44 Okay, yeah, I appreciate it.
And, yeah, if you have any, comment or feedback, yeah, please, left.
on the issue.
**Trask Stalnaker (Microsoft Corporation)** 15:59 Cool, yeah, yeah, I will, I will leave a… I will leave a comment there.
Based on what we… People say in the… other meeting.
For this one… Pushing… I can… DM you, With, kind of, what is discussed there.
If anybody has thoughts.
Or in the… Gen… in the GenAI Slack.
Maybe.
**Huxing Zhang (Alibaba Cloud (Singapore) Private LTD)** 16:59 Okay, I… I can share this link, and Maybe, raise a topic there, and, see if there's a… any interest in getting that? Yeah.
**Trask Stalnaker (Microsoft Corporation)** 17:13 Cool.
Will do.
Anything else to chat about, in this meeting.
**Huxing Zhang (Alibaba Cloud (Singapore) Private LTD)** 17:28 Yeah, another thing that I'm preparing for the… blog post, things, and, last… we discussed, last week.
I will create the issue this, this, this week.
And then send the PR… I think there's a need of some sponsors when we create a blog post, there, so I'll…
**Trask Stalnaker (Microsoft Corporation)** 17:52 Yeah.
**Huxing Zhang (Alibaba Cloud (Singapore) Private LTD)** 17:52 So, Dudmina, is that correct?
**Trask Stalnaker (Microsoft Corporation)** 17:56 Yeah.
Yeah, yeah, you can add both of us.
**Huxing Zhang (Alibaba Cloud (Singapore) Private LTD)** 18:00 Okay.
So… okay, I'll create that to maybe… today or tomorrow, and then, yeah, I hope I can get it done by this week.
**Trask Stalnaker (Microsoft Corporation)** 18:14 Cool, awesome.
Alright.
Well, I will, let y'all know how those discussions go later.
**Huxing Zhang (Alibaba Cloud (Singapore) Private LTD)** 18:31 Okay. And…
**Trask Stalnaker (Microsoft Corporation)** 18:32 Good to see you all.
**Steve Rao (Alibaba Cloud (Singapore) Private LTD)** 18:34 Thank you.
**Huxing Zhang (Alibaba Cloud (Singapore) Private LTD)** 18:34 U.
**Steve Rao (Alibaba Cloud (Singapore) Private LTD)** 18:35 Do you?
**Trask Stalnaker (Microsoft Corporation)** 18:37 by… Huxing Zhang (Alibaba Cloud (Singapore) Private LTD) 18:37 Bye, pal.

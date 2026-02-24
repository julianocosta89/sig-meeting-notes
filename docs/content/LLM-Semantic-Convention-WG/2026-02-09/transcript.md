SIG: LLM Semantic Convention WG
Date: 2026-02-09
Duration: 83 minutes
============================================================

## Zoom Recording Transcript

**Sergey Sergeev** 00:39 Air, then…
A solemn check.
Anybody is here?
**Keith Decker** 02:05 Yep, I can hear you.
**Surya Teja** 02:06 Hey, hi, I'm here.
**Sergey Sergeev** 02:08 Nice. Just wanted to… Double check.
Yeah, any… AI agent monitoring track.
Agenda items for today.
Unfortunately, I'm not, yet ready for anything on my side. Most probably, I will be presenting tomorrow…
We have, session, support for…
Open Celebrity Instrumentation Utility Library, scheduled for tomorrow.
But otherwise… I don't have anything on my site.
**Surya Teja** 03:00 I have a couple of, things which I wanted to bring to notice. So, I created a prototype for… not prototype, actually, the boilerplate stuff for,
Claude Agent SDK.
I want some reviews on that one.
So…
**Sergey Sergeev** 03:22 Same.
**Surya Teja** 03:23 Yeah, I'm… for some reason, Docs is not allowing me to paste the link of,
Yeah, I could paste the link of the PR that I raised.
**Sergey Sergeev** 03:36 Yeah, if you, if you press enter, so it will turn it into a link.
**Surya Teja** 03:40 Yeah, sure.
**Sergey Sergeev** 03:42 Yep.
**Surya Teja** 03:43 Yeah, I added the link for that. So, it's not containing any code or anything, but it is setting up the base repository and,
Tests and talks, related, stuff for, this.
The same thing has been done for Anthropic SDK instrumentation.
Since this is agent, SDK, I wanted to bring this to agent, call.
Once after this is approved and merged, the next steps are adding spans around create agent, invoke agent, and…
tool called, steps or functions inside, Cloud Agent SDK.
for Python.
That's the… first thing. And the second thing,
is, understanding more about create agent and,
differences between, create… sorry, more about understanding more on create age and stuff. So, the func… definition was not clear. I believe we… I spoke briefly, Sergey, last week, to understand
what are the boundaries or limitations of CreateAgent? So, I have an example that I want to add today so that I can get more intuition around it.
So…
**Sergey Sergeev** 05:06 Yeah.
Yeah, it will be the question to this group, especially.
**Surya Teja** 05:11 Yeah.
**Sergey Sergeev** 05:11 This blank, guys, you worked, on different instrumentation. Have you used CreateAgent at all, or…
What do you think is the best fit for Kate Agent?
**Surya Teja** 05:24 I have no clue with this, but I'm going to ask a question from Anthropic perspective. So, in Anthropic, you can create sub-agents, say, for example,
you want to create an agent which is… which can write code, and you want to create a sub-agent which can review the code. You are going to create a sub-agent for
with the predefined syntax for reviewing the code. So the calls that happen for spawning the sub-agent
Or the calls that happen, For, you know, initializing the agent framework.
Do they fall under… Create agent span, or…
How do we capture instrumentation error on those?
**Sergey Sergeev** 06:16 And, sorry to re… can you repeat, what are the use cases in Anthropic? So, you can create sub-agent? Is it, something you do in the code? Is it something,
an agent, like an orchestrator agent creates dynamically, or…
Is it something, you create in your program?
**Surya Teja** 06:42 It is something you create in our program, so let me send you the relevant docs, so it's going to make life, more…
**Sergey Sergeev** 06:50 You can put it right here in the doc lobby.
**Surya Teja** 06:53 Yeah.
**Sergey Sergeev** 06:54 easier for everybody. By the way, everybody, Mega, Victor… And Josh,
everybody on the call, if you can put your names here, just to understand who's attending, what's your interest, and etc. We should have started probably from a quick introduction.
But if you can do it asynchronously in… the OpenCeremity, group.
doc, let me share it to the chat, if I can.
Find it here…
**Anirudha Jadhav** 07:36 Hey, everyone.
**Sergey Sergeev** 07:36 Hehei.
**Anirudha Jadhav** 07:39 I put an agenda item above, I think it went into the.
**Sergey Sergeev** 07:43 Okay.
**Anirudha Jadhav** 07:44 So, like, the next topic, yeah, yeah.
Is it a tiny…
**Sergey Sergeev** 07:48 Gentecor General…
group, so this call is more trying to figure out, multi-agent, semantic intervention in this setting.
**Anirudha Jadhav** 07:59 Makes sense.
**Sergey Sergeev** 08:01 So, it's open search project, right? Yeah.
**Anirudha Jadhav** 08:09 And, Surya, thanks for the PRs. I…
If you need something else, let me know, I've been reviewing that.
**Surya Teja** 08:15 Yeah, yeah. Can I add you as a reviewer for, agent, yeah, sure. Yes, please. Yeah.
Cool. Sure, Ali. So, yeah, can I go ahead?
**Sergey Sergeev** 08:29 Yeah, go ahead.
**Surya Teja** 08:30 Yeah, so… I pasted a link.
Related to cloud documentation around how they define subagents. So, they are specific…
tasks that are, assigned to the agents that are created. To give you a raw example, it's like running things asynchronously, like on threads. So…
You have a major agent which is doing the main thing, but if you want to offload some parallel or concurrent thing to a agent.
or sub-agent. You just create a sub-agent and, offload that task to it.
And that, sub-agent is going to
Complete the task, and give back the result to the main agent.
They gave an example over here in… program…
**Sergey Sergeev** 09:25 Yes.
**Surya Teja** 09:26 Yeah, this is going to add a little bit more… Color to it.
from the look of it, it felt like, we are creating agents and create agent span. Makes sense for that, but…
when I dug deep into the code, it's not doing any remote agent instantiation, rather it's
Doing the local agent instantiation.
**Sergey Sergeev** 09:56 Yeah,
In general, I don't think V in Spoane district of OpenTelemator V, create any… create agent, spans.
And, yeah,
Anybody… anybody used to create agent spending? Because here, it's just when you initialize your agent, again,
cigarette?
two different patterns, how to run agents. One pattern, you run permanent agent process.
In this case, it makes sense to create,
When you initialize your program.
You probably want to create,
To create those pants with create agents to indicate.
**Surya Teja** 10:50 Yeah.
**Sergey Sergeev** 10:51 Those were my parameters, and then when you, serve every request to the agent, so you don't…
Create, create agent spends, you just, Create, invoke agent span.
**Surya Teja** 11:07 Okay Okay.
**Sergey Sergeev** 11:09 This, this would make sense to me. What if, for example, architecture dynamically create agents.
**Surya Teja** 11:17 Then probably you won't.
**Sergey Sergeev** 11:19 To create that create agent span, because the span should capture your agent parameters.
**Surya Teja** 11:27 Yeah.
**Sergey Sergeev** 11:27 But,
There is another pattern, which is, for example, AWS agent query runtime, where all the agents are Lambda function style. They are…
Transient. So, in this case.
every time you start, you will create that create agent span. I don't know if it's a good fit in this case, but again, maybe also create agents may be optional, because I think it will be quite noisy
Let's say you start an agent on every vacation.
**Surya Teja** 12:02 And then you…
**Sergey Sergeev** 12:03 define 10 different agents, which never changes. So, in this case, you will create create agent span.
**Surya Teja** 12:11 On every request, so to me, it's just too noisy, but maybe it's some optional parameter, like, do I want to capture my create agents?
**Sergey Sergeev** 12:21 Maybe it's…
**Surya Teja** 12:22 Yeah.
Yeah, that makes sense, Sergei. So…
**Sergey Sergeev** 12:26 This is my guesses. By the way, anybody on the call.
Wants to add anything to… to this?
We can double-check in tomorrow's meeting that this is the right assumption about the create agent spends.
Or if anybody is using it differently.
Yeah, let's… let's just use this assumption for now, and maybe double-check in tomorrow's call.
**Surya Teja** 13:02 Yeah, cool. Thanks, Sage.
**Anirudha Jadhav** 13:04 Okay, that's…
**Sergey Sergeev** 13:10 So, victor, do you want to go with your topic? I see it in the chat.
**Victor Lu** 13:17 Yeah, I'm a journalist, so you've probably heard of a cloud event, right? So that's the CNCF Cloud Event, and then there's, in the CD Foundation, there's a spec called CDEvent.
The idea is to, make the different CICD pipelines interoperable by creating standard events. So it's not matrix, telemetry matrix, but it's events.
So that the GitOffs, we don't know, the GitOffs workflow and the CICD workflow can, more, flow better, I guess, to describe it. So we are starting a new discussion about
how does it apply to data? Because,
There are so many ops nowadays, so, the one that we think is probably the first tier ops, these ones, MR DevStack Agent Ops, and there's a multiple.
So, ML, DevSecOps, as probably everybody knows. Agent is the new thing. There are many other ops, but we think that those are not the first tier. For example, you got FinOps for financial analysis, cost analysis, and AIOps for using AI for operation.
But this ops, I mean, our DevSec agent, that's more of a first tier, and… but they all work on data.
So that's why, yeah, we think it's probably necessary to create some standard events so that all the parties participating in the workflow can talk to each other in the same language. So it's kind of a different…
view from OpenTelemetry, but it's the same idea, standard, language. So, yeah, so this is… so I've just come here to listen and borrow some idea from the discussion here.
**Sergey Sergeev** 15:10 It's at the bottom. Yeah.
**Victor Lu** 15:12 if you look at the bottom, the top are all modeled against the CD events that already is a spec in CD Foundation. The one at the bottom, if you go to, yeah, the agent, so we think that this is all new, so this is all kind of a…
You know, very randomly generated at this point, on what's, when it comes to agent, what…
What kind of a related event can happen related to data?
Yeah, they're very primitive at this point. Yeah.
**Sergey Sergeev** 15:46 In… in general, yeah, anybody has any… Opinion on it?
Yeah, my first take would be, so, in general, we have all the tool invocation and et cetera, so I would expect, your agent workflow will look like, a bunch of
sub-agent invocation, each of them can call some tools, some LOM invocations, and so on, until it,
does something… Helpful, and then, be it,
Passes that context to the next agent, too, and so on, and then you finish the workflow.
And, let me ask the question about, the data ops event. So, is it kind of an input for your agent, or…
What others?
**Victor Lu** 16:48 The idea… so the first step, we… so there's already, if you look at the beginning, the top of the document, very top.
**Sergey Sergeev** 16:57 By the way, do you want to share, if you want?
**Victor Lu** 17:00 No, no, I don't have much to show. This is really just a very kind of scratch at this point. If you look at the reference, the CD events.
That's already a kind of a mature spec already. So those, so this is basically modeled after CD events.
So, for example, Jenkins, Tektong, you know, different workflows, they will speak the same event language, so that whenever something happens, they know, you know, what do they mean, right? So, same thing for… so the first step.
from this discussion really is to identify, you know, is there already a need for this kind of event? For example, data catalog
providers, you know, workflow providers, such as the, you know, Informatica being the old one, but there are many new ones, and who are the players that can… already kind of need to define those kind of events, and can benefit kind of unifying the definition, make it standard type of events?
That's the goal.
**Sergey Sergeev** 18:00 Yeah, I… I would be surprised if there is no something like CICD, a special interest group in OpenClimate.
Which tries to define it.
**Victor Lu** 18:13 Yeah, so the CD events, it's already… Oh, yeah. It's completely separate from the OpenTelemetry, effort, but it's, it's already a spec, so it's kind of already there, so,
Yeah, so this is just… yeah, this is part of a so-called CD Foundation. It's also part of Linux Foundation, but it's not part of CNCF.
**Sergey Sergeev** 18:36 Yeah, Lyudmilo will be the biased.
to chat about it, maybe in tomorrow's meeting. Again, how can we connect it, to generative AI? It's a good question.
I think,
I think it's basically the input to your agent, right? And you want to be able…
To see what your agent was doing by all those different types of events, right?
**Victor Lu** 19:10 Yeah, each group have their focus. For example, we don't…
plan to go into too much into ML events, right? Because everybody's doing things differently, so it's really… there's so many efforts already to defining, you know, the right workflow, you know, so it's pretty hard. Then for dev, it's basically the CD event is for dev. Security is, it's
yeah, there's more complexion there. So the reason I say focus on data is because everybody, no matter what you do, is for security, it's for CICD, it's for machine learning agent, everybody has to touch data, right? So, it's kind of…
foundation for everything else, so that's why we think it's probably good to just focus on the data-related events. And some of it may not be… you may not consider as daily events. For example, through the agent, I mean, if you scroll all the way down, down there, some of the events, such as, you know, called
tooling call… tool call, this may not be, you consider, a data event, right? So, but that's up to the discussion, you know, what kind of data events should be… can be standardized and make it part of the data ops event.
**Sergey Sergeev** 20:19 Yeah, so we have, those two codes, for example, memory and knowledge.
etc. So those are representable as, Gen AI spans.
So this is the telemet you produce. So now, what is the event? How do you represent those events in…
In, for example, continuous delivery of foundation. So, what is an event?
what type of telemetry? Is it… is it something like Kubernetes-specific?
**Victor Lu** 20:57 Oh, no, it's not, it's not really the… Well, okay, I guess it's also, it's not for monitoring, it's more for, you know, for example, Jenkins, did something, right, did one step.
I'm just giving the… I'm not…
**Sergey Sergeev** 21:13 Yeah, yeah, yeah.
**Victor Lu** 21:14 So, let's…
Yeah. Let's say Jenkins did a, commit, commit to repository event, for example, right? And then, and then, for the, for the same project, Kapton is also used, as part of CICD pipeline. So, for… but it's for a different, obviously, it's for a different, project in the… in the system.
So, when both system… both CICD pipeline is involved in building a system.
How do you make sure that they all
kind of say, okay, are you done yet? Did Jenkins, did you commit what you did in Jenkins? Yes. Did you commit what you did in Kapton? Yes. Now we can say, okay, now both are done, and in the GitOps workflow, I can say, okay, now both CIO CICD pipeline have done what they need, so we can now roll out the…
the Git, you know, that infrastructure.
So this is just kind of a… making sure different, projects, like Jenkins and Capital talk to each other. That's… so that's on the CICD side. So this is more on the data side.
**Sergey Sergeev** 22:19 Yeah, what is the protocol for them talking to each other?
**Victor Lu** 22:24 Exactly.
**Sergey Sergeev** 22:26 So you… right now, there's no kind of protocol, or message format, or whatever?
Yeah, I'm… I'm also wondering about,
this special interest group for CICD.
Again, yeah,
If we can define some kind of telemetry, if there is already defined some kind of telemetry, for…
All of those events, what…
If there is much representation in OpenTelem at the…
For those, I think, then we can try to define it as a subtype, for example, for tour and vacation and etc. So right now, we have, basically conversation messages
Represented, as a list of messages…
From user and setting, they have types.
So, if we want to define a special type, which is CICD event, I think it's possible.
So at least we can,
You will be able to search by those specific types, and probably predefined values.
Does that make sense, or…
**Victor Lu** 23:55 Yeah, yeah, yeah. The, the, the, yeah, that, that's, that's, yeah, I, I agree, yeah.
**Sergey Sergeev** 24:08 Yeah, and for… The metrics,
Yeah, for the metrics, it may be the same 2 on vacation metric, or LM on vacation metric, and so on.
Just, gives us additional.
attributes, so I assume they will be not super high cardinality, but, higher cardinality than some of the backends may want, so it may be opt-in
For this. But again, it's… I think, it's a good actionable
item just tried to find definitions in OpenTelemet for the CICD, events.
And if there is already the definition, maybe that a special interest group, so there is a CICD, group, I believe.
Which tries to define those events. If you can define them, probably we can… define it,
As a message type, if needed.
**Victor Lu** 25:17 Yeah, got it, yeah.
**Sergey Sergeev** 25:23 We have 5 more minutes.
**Anirudha Jadhav** 25:35 Oh.
From a roadmap standpoint, how do we cover agendas or roadmaps in G6? I'm just new to the structure.
**Sergey Sergeev** 25:47 Yeah, I think, on… at some point, so Tuesday meeting is a bigger group, with more time. I… I think in the past, Ludmi, put together
Some of the roadmap.
I don't know if we could, stick to it.
But in… General, yeah, annual…
any involvement, is highly appreciated, so my, participation in those groups, were… was very limited in the past, but now I hope to get more time, and.
**Anirudha Jadhav** 26:29 So, in summary, we have, like, this meeting for agents, then we have the Tuesday meeting for GenAI, and then there's a semantic conventions overall working group at 8 AM today morning.
**Sergey Sergeev** 26:40 Yeah, and this is Humantic Convention 2026 roadmap.
**Anirudha Jadhav** 26:49 Perfect.
**Sergey Sergeev** 26:50 Yeah, this document is deep, if you search for it.
**Anirudha Jadhav** 26:54 That was fine.
**Sergey Sergeev** 26:55 And you can find, roadmap, into 25, maybe.
**Anirudha Jadhav** 27:02 Okay, this helps. I'll just do the homework now. No worries, thanks.
**Sergey Sergeev** 27:06 Yeah, maybe even feeding it to GenAI and crunching it.
But yeah, I think everybody in the Sikh is so busy, so any active participation and help will be appreciated, for sure.
**Anirudha Jadhav** 27:25 Okay, thank you, sirs.
**Sergey Sergeev** 27:29 Okay, anything else?
My baby will take 3 minutes back.
Have a good start of the week. Hi, everybody.
Right.
**Surya Teja** 27:44 See you guys, have a good day.

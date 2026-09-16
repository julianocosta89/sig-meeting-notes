SIG: GenAI SIG (APAC)
Date: 2026-09-15
Duration: 30 minutes
============================================================

## Zoom Recording Transcript

**Steve Rao (Alibaba Cloud (Singapore) Private LTD)** 00:54 Hi, Liudmila.
**Liudmila Molkova** 00:57 Hello, hi Steve, how are you?
**Steve Rao (Alibaba Cloud (Singapore) Private LTD)** 01:00 Yeah, I'm fine.
Thank you.
**Liudmila Molkova** 01:09 And let's give people a few minutes to join.
**Steve Rao (Alibaba Cloud (Singapore) Private LTD)** 01:12 Okay.
**Liudmila Molkova** 02:35 I'm starting to doubt if we're in the right call.
Should be.
This is the The… the new LFX one.
**Steve Rao (Alibaba Cloud (Singapore) Private LTD)** 02:52 Hmm.
**Liudmila Molkova** 03:08 Did you add, an item about A2A?
**Steve Rao (Alibaba Cloud (Singapore) Private LTD)** 03:13 Yeah.
**Liudmila Molkova** 03:17 Yeah, so maybe I'd love to start.
Hi, Emil.
**Emil F** 03:24 Hello?
**Liudmila Molkova** 03:39 I think Ankit's topic is for later, and I don't see them here.
Let's talk about Daytree!
**Steve Rao (Alibaba Cloud (Singapore) Private LTD)** 03:50 Yeah.
Yeah, I have a true question about the HOA protocol.
In, Hotel GenI Cemantic Commission.
I found that there are some guys, they, created some issue on the PR.
To migrate the A2A protocol to, hotel GenAI semantic convention.
and, in our, In our company, we also have, some related scenarios, to want to define HOA, related semantic, semantic convention to, capture related data.
And my first question, just like a list on the documentation, what are the committee's future plan regarding the design of ATA-related semantic convention?
Well, we priority to, giving to directly, A2A protocol specification to hotel GenIi.
**Liudmila Molkova** 05:10 Yeah, so this is the… the pull request you're talking about, right?
**Steve Rao (Alibaba Cloud (Singapore) Private LTD)** 05:15 Yeah.
**Liudmila Molkova** 05:18 Yeah, I think it's pretty close. I've been reviewing it quite a while, and I think maybe there is one open comment about the… Duh… reference tests. Other than that, I'm ready to approve it.
And I think it's been looked at by a person who works on A2A, this person.
**Steve Rao (Alibaba Cloud (Singapore) Private LTD)** 05:45 the day.
**Liudmila Molkova** 05:45 at some point, I want to update. There is native instrumentation for A2A, and I think this person works on it, but it's kind of… noisy, and they, at some point, will probably update to the autosomatic conventions when they have some Capacity to work on this, and, libraries themselves.
So… are… besides my approval, we'll need a second one that's from some other company? Are you… are you approver on this report, Steve?
**Steve Rao (Alibaba Cloud (Singapore) Private LTD)** 06:20 No.
**Liudmila Molkova** 06:21 No. Okay. Oh, maybe mean quiz.
**Steve Rao (Alibaba Cloud (Singapore) Private LTD)** 06:24 Yeah.
**Liudmila Molkova** 06:26 So, like, if you're interested, give it a review, get… let's get another approval besides mine, but I intend to approve it once all the final details are published.
**Steve Rao (Alibaba Cloud (Singapore) Private LTD)** 06:39 Sure, yeah.
And the second question is, in GenAI, Old Testament convention, I also found some issue they, want to capture something like, task ID.
in… A2A protocol.
There is, a related, field called, A2A.Tasker.id.
And, if we merge the PR in the future, we will use the H2A.task.id to capture the task ID between multi-agents.
**Liudmila Molkova** 07:34 Yeah, is it, like, do you see a potential for, something broader, because… Task is something very generic, and I don't know what the task here means, what is it about?
And the person who sent this issue had never defined what the task is, and if you… if I… I tried to map it.
To… something generic across systems.
And… there is… nothing generic, so I think Crew EI has tasks.
and they might be related, but there is nothing, like, an entity we can record, it's something just internal to the query eye.
So… I… like… what do you think tasks are, and do you have an API that Takes tasks.
**Steve Rao (Alibaba Cloud (Singapore) Private LTD)** 08:40 Yeah, in our, internal scenarios, yeah, maybe in multi-agent scenarios, they defined, A task, something like, if a person asks an agent to finish something, and the agent will, define the task in its context.
And, assign the task to other agents and, something like this.
**Liudmila Molkova** 09:12 Is it a public API, or is it something internal to Alibaba?
**Steve Rao (Alibaba Cloud (Singapore) Private LTD)** 09:16 I think, there isn't a public API, just the inside, concept.
**Liudmila Molkova** 09:30 Yeah.
There is something similar at Google, but it's also… seems very similar to what you're describing, but I've been struggling to find, like, other companies that do it, and it seems everybody does it, but maybe… Nobody… Documented publicly.
**Steve Rao (Alibaba Cloud (Singapore) Private LTD)** 09:55 Okay.
Okay, that means, in hotel, GenAI semantic convention in the future, if we need to define something about, HOA, maybe we will, Specialization on the… On that PR.
**Liudmila Molkova** 10:19 I mean… here?
**Steve Rao (Alibaba Cloud (Singapore) Private LTD)** 10:20 Yeah, yeah, yeah.
**Liudmila Molkova** 10:23 And this one would… would do the A3 things, and…
**Emil F** 10:33 Give me a sec.
**Liudmila Molkova** 10:34 Yeah, go ahead.
**Emil F** 10:35 I'm trying… I'm not familiar with 8-way or the concept, but If Steve can explain, is it a task that a human gives to an agent, or is it a task where one agent Basically sends dust to other agents.
Rao 8 to 8.
**Steve Rao (Alibaba Cloud (Singapore) Private LTD)** 10:54 Hmm.
**Emil F** 10:54 that we're talking about.
**Steve Rao (Alibaba Cloud (Singapore) Private LTD)** 11:00 I mean, yeah, in our inside concept, maybe human will, send a tasker, send a, task to, to the agent, and the agent will, will define a task according to the description by human.
And, the agent maybe will, write a spec for MD to define the task, how to finish the task, and send the… the spec.md to other agent, something like a work agent, to, finish, the task.
**Emil F** 11:43 Yeah, okay, so… Essentially, task and fan out of a single agent, you know, multiple tasks and go to other sub-agents.
**Liudmila Molkova** 11:54 And A2A is different, though.
Okay. So you send a message request, which is, like, a start… call. There is a message.
And the agent gives you back a task. It's essentially a handle of what it is working on, so you can retrieve the state after. I see. So it's something completely different, and it kind of makes sense for it to be an A2A namespace.
**Emil F** 12:21 Yeah.
Sounds good.
**Steve Rao (Alibaba Cloud (Singapore) Private LTD)** 12:28 Okay, yeah, yeah, besides the A2A semantic convention, I also have a question in, Google or in other companies, you know.
For their multi-agent system, how do they choose, define the communication protocol.
for multi-agent, just use the HOA protocol or other… Protocol defined by themselves.
**Liudmila Molkova** 12:58 I think it's a Wild West.
So, there is in-process, agent communication, there are agent runtimes that I think use A2A underneath.
I think… Microsoft, from what I see, probably uses the… the… just… the HTTP communication, maybe MTP, I… I don't… I could… I don't know how to answer your question. Maybe Emil do you know?
**Emil F** 13:34 No, I don't have, experience with multi-agent systems.
**Steve Rao (Alibaba Cloud (Singapore) Private LTD)** 13:46 Okay, thank you.
**Liudmila Molkova** 13:55 Yeah.
I'm curious, Emil, you mentioned… yeah, you're for… at Langsmiths, right?
**Emil F** 14:07 Yeah, Lang can, yeah.
**Liudmila Molkova** 14:10 Nice.
**Emil F** 14:10 Yes.
**Liudmila Molkova** 14:11 Yeah.
Cool, I'm, like, what brings you here?
Can we work together? There's so much.
**Emil F** 14:18 Yeah, I mean, Trying to get a better idea of what is happening in the, hotel.
world, because Langsmith has its own sort of protocol, but it also supports OTEL, or a subset of the OTEL attributes. So, I'm trying to basically see where the specification evolves, and… how do we need to extend, Langsmith to a better support hotel, basically?
**Liudmila Molkova** 14:54 Okay.
Any findings so far? Would you like to talk about anything?
**Emil F** 14:59 I'm…
**Liudmila Molkova** 14:59 particular?
**Emil F** 15:00 I'm still ramping up, pretty much. I just, you know, over the past couple weeks, I started Looking into the autoimplementation Works series.
So, yeah.
I… I'm still not very current as to what is going on with, like, what kind of attributes are supported by, like, third party… well, third party… by, various auto-implementation.
for… for GenAI.
So, I don't know if there's a tracker… That is…
**Liudmila Molkova** 15:35 No, I dare.
**Emil F** 15:35 there.
**Liudmila Molkova** 15:36 There is…
**Emil F** 15:38 But…
**Liudmila Molkova** 15:39 Might not be perfect.
But, there is a raw data, and you… Can ask… your AI to make sense of it. So we have this confirmance repo.
And… it contains scenarios for different instrumentation libraries.
For example, let's take, langChain.
And there is an open inference implementation, up in telemetry, and up in telemetry 1.
And each of them has the file called DataJSON.
It's actually… it only includes here the things from OpenTelemetry semantic conventions. It does not yet include attributes that are unknown.
I'll probably, make it happen here, but you can see the spans that we were able to recognize.
And, these are the attributes that are… I stamped on this fence.
are no metrics from Open Inference, and… This is the open telemetry version, which is… A bit more broad, a little bit less populated, and this is the open telemetry.
implementation, And there are things called findings, these are the things that are, Some violations of conventions, sometimes they are serious, sometimes they are less serious.
So here, for example, we see some, Unknown attributes. OpenTelemetry does not recognize this friend.
**Emil F** 17:22 Yep.
**Liudmila Molkova** 17:23 Is this what you were looking for, or something?
**Emil F** 17:27 Yeah, I think that that would be very useful.
Though I see there is no… No conformance for the Langsmith, which is kind of the… The tracing portion, Of LinkedIn, which can be used, standalone.
Oh, man.
**Liudmila Molkova** 17:46 It emits OTLP, you… you… it would be awesome if you could contribute here.
**Emil F** 17:54 Yeah, I don't… I don't need to take a look. It definitely does. It emits OTLP4.
So it can be used to trace to other backends other than, than LineChain or Linesmith.
**Liudmila Molkova** 18:07 Yeah, I mean, what we do, like, for some instrumentations, there is a native one that the library meets itself.
And for length chain, it would probably be native, or you can call it lengthsmiths.
And…
**Emil F** 18:23 Yep.
**Liudmila Molkova** 18:24 It should be pretty straightforward how to add stuff here. You see, it's just a few, configuration files. The actual code is… Here, and feel free to contribute scenarios or update existing ones if you… think they are problematic. But they are shared across all the instrumentations, and it's just you contribute this… this portion And the toll shows up.
And it's very AI-driven repository, so there should be way too excessive instructions everywhere.
**Emil F** 19:03 Sounds good.
I think it's, so, you have… hmm… Yeah, I need to rub my head a little bit around the structure there.
So you have the different top level, top level, producers, basically, of Signal, and then in each you have a… you have the instrumentation library.
**Liudmila Molkova** 19:28 Yeah, so let's say we pick some… some scenario, right? It's just a Python code, it only runs long-chain.
And… If there is a… So you, you can potentially modify it. If you need, like, some programmatic configuration before, then you, you can… we can find ways to edit But if it's, like, zero-code monkey patching, then probably you don't, and there is this file that controls the flow.
This is just the configuration.
And then it runs a mock server, where it doesn't run against a specific, like, no, no API keys, and if you miss something, the mock server is right here in the same repo, and we can update that more stuff here.
And again, there is a bit of configuration. If you can enable, tracing with environment variable, it's awesome, and then it's just a bunch of commands that actually run the Python script. And here we use the OpenTelemetry zero code. It essentially applies all the monkey patching and, enables instrumentation.
But, and this is just to declare dependencies.
So, this is the only meaningful file, and the data JSON is produced by running this scenario.
**Emil F** 20:59 Okay, I'll take a look.
**Liudmila Molkova** 21:03 Cool, and if you, like, see any problems, or get stuck around something.
Ping me, I'm really happy to help.
**Emil F** 21:14 Alright, thank you.
**Liudmila Molkova** 21:17 Thank you.
Cool.
Oh, hi, Trask. We've been talking about conformance and link chain.
An ATE.
**Trask Stalnaker (Microsoft Corporation)** 21:29 Cool. Sorry, I'm extremely late.
**Liudmila Molkova** 21:33 It's okay.
Maybe.
**Emil F** 21:40 This meeting is titled APAC, and I don't think it's… at least in my calendar. I don't think it's an… not time suitable for APEC.
Not much.
**Trask Stalnaker (Microsoft Corporation)** 21:53 It's the best that we could do, and Steve here is from Alibaba.
**Emil F** 22:00 Yeah.
Well, I expect it's in the middle of the night, or close to.
**Steve Rao (Alibaba Cloud (Singapore) Private LTD)** 22:06 Yeah.
**Liudmila Molkova** 22:07 How late is it for you, Steve?
**Trask Stalnaker (Microsoft Corporation)** 22:10 11.30, I think? I remember? 10.30 right now? Maybe 11… 10.30… During daylight savings, and 11.30 when we flip, which will be problem.
**Liudmila Molkova** 22:23 Oh…
**Trask Stalnaker (Microsoft Corporation)** 22:25 Did I get that right, Steve?
**Steve Rao (Alibaba Cloud (Singapore) Private LTD)** 22:28 Yeah.
Yeah, maybe we, we… We can, negotiate.
Later.
**Liudmila Molkova** 22:43 Yeah, I'm sorry, Steve. Thank you for making it so far.
**Steve Rao (Alibaba Cloud (Singapore) Private LTD)** 22:47 Okay, thank you.
**Liudmila Molkova** 22:51 Anything we should talk about in the last 8 minutes?
And Nishin, we want to prepare for the… the main… Meeting later.
See, my brain didn't turn on yet, so I'll…
**Trask Stalnaker (Microsoft Corporation)** 23:21 My brain is all on the, the stabilization piece, so I'm like, oh, man, we still have other GenAI meetings, too.
**Liudmila Molkova** 23:32 A lot of GenAI meetings.
**Steve Rao (Alibaba Cloud (Singapore) Private LTD)** 23:34 Yeah.
**Liudmila Molkova** 23:37 Yeah, so, Steve, Emil, we… Emil, you've been in the stabilization effort, so maybe we'll give a quick update to Steve.
**Steve Rao (Alibaba Cloud (Singapore) Private LTD)** 23:47 Okay, thank you.
**Liudmila Molkova** 23:50 Oh, Emil, you wanted to say something?
**Emil F** 23:53 No, no, I was just agreeing with you.
**Liudmila Molkova** 23:58 Yeah, so, Steve, we started the stabilization, I'm not sure if you've seen so there is the… The meeting notes are essentially in the same doc.
**Steve Rao (Alibaba Cloud (Singapore) Private LTD)** 24:10 Yeah.
**Liudmila Molkova** 24:10 And it's like a kind of meeting… 3 short meetings during a week focused on the… just the stabilization, somewhat similar to our PC.
But they are… we wanna… Target… The… inference, yeah, so, inference… And, exactly what it means, it's… to be defined, I think. The details will figure it out. The Agentic stuff.
Probably not the identity itself, but the things around, like, the spans we have already defined… defined.
Oh, and Trask has an issue that lists… Yeah, I was just more…
**Trask Stalnaker (Microsoft Corporation)** 25:05 I mean that.
**Liudmila Molkova** 25:05 listed.
Yeah, thank you.
**Trask Stalnaker (Microsoft Corporation)** 25:07 In chat now.
**Steve Rao (Alibaba Cloud (Singapore) Private LTD)** 25:10 Okay, thank you. And I will take a look about the dashboard, and if there are anything, related to me, to my daily work, and I'm also interested in, working in…
**Trask Stalnaker (Microsoft Corporation)** 25:28 Great.
**Liudmila Molkova** 25:31 Yeah, so there is this, project board… It keeps disappearing.
Seriously.
**Trask Stalnaker (Microsoft Corporation)** 25:44 Show me?
**Liudmila Molkova** 25:45 the project, tab keeps disappearing from here.
**Trask Stalnaker (Microsoft Corporation)** 25:49 Whoa.
**Liudmila Molkova** 25:50 Should I enable it in the admin repo?
**Trask Stalnaker (Microsoft Corporation)** 25:52 Yeah.
**Liudmila Molkova** 25:53 I see, I see, okay.
**Trask Stalnaker (Microsoft Corporation)** 25:55 Terraform… Terraform rules.
Not rules in a good way, but rules in a… authoritarian way.
**Liudmila Molkova** 26:04 Oh, that's… that's fine, it's just I didn't know.
Yeah. Yeah, so there are… Like, some things that are in to-do here.
And maybe we should go through them, in the stability meeting and clean things up.
But this is what I think is non-controversial.
Oh, so maybe this is controversial, the… overlap between retrieval and memory records. We don't… know yet if we want to stabilize… Oh, I'm not sharing?
**Trask Stalnaker (Microsoft Corporation)** 26:43 Yeah.
**Liudmila Molkova** 26:45 Sorry.
Okay, so there is this project board.
Maybe we should put it in the… links here… And there is a to-do column here.
Which is… something that is probably… Within, stabilization?
It's either one of the spans you have in your issue, or, something that… that is very related to it.
And there are a lot of small things and some giant things. So, like, this is the… the giant Uber issue, this is the… something I would love us to… Polish, the details.
So, Steve, if you feel attached to any of these things, and you would be interested in working on them, it'd be awesome.
**Steve Rao (Alibaba Cloud (Singapore) Private LTD)** 28:07 Okay, thank you.
**Liudmila Molkova** 28:14 Great.
So… Anything else we need to talk about?
**Steve Rao (Alibaba Cloud (Singapore) Private LTD)** 28:23 No from me.
**Emil F** 28:28 book.
**Liudmila Molkova** 28:32 Then?
Have a good night, Steve, and if we see some of… if I see some of you in an hour.
See you there.
**Trask Stalnaker (Microsoft Corporation)** 28:41 Alright.
Bye.
**Emil F** 28:44 Bye-bye.

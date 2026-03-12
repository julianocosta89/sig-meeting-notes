SIG: LLM Semantic Convention WG
Date: 2026-03-02
Duration: 32 minutes
============================================================

## Zoom Recording Transcript

**Sergey Sergeev** 02:10 Oh, sorry, folks. Monday meeting, trying to get video call tools work.
How are you doing?
**Keith Decker** 02:28 Get everything up and running again on a Monday morning.
**Erdenesaikhan Tserendavga** 02:32 Hello, everyone.
**Sergey Sergeev** 02:35 Yehay.
Yeah, while I'm still brushing up, An agenda. Let's see how many people About to join on Monday.
So, do you have any open questions?
**Tao** 02:54 No, I'm from, Microsoft, the Agent Framework team. I was told to join this meeting to answer any multi-agent-related questions.
**Sergey Sergeev** 03:05 Nice, Agent Framework Team, what does it mean? What do you guys do?
**Tao** 03:12 Literally, the name is Adrian Famore. It's Microsoft Adrian Famore.
**Sergey Sergeev** 03:15 Oh, it's my Soft Agent Framework.
Is it semantic?
Is it semantic kernel, or…
**Tao** 03:24 Well, you can think of it's the, V2 of semantic kernel.
**Sergey Sergeev** 03:29 So basically, you are taking care of that framework, and using it, as a core framework for your foundation, or…
**Tao** 03:40 No, I'm not using the framework, I'm the, you know, I'm representing the team that's building the framework.
**Sergey Sergeev** 03:53 it.
**Tao** 03:53 And… and I'm responsible for, Absolutely, of that framework.
And I also work on the multi-agent aspects of the framework, and… There was… last week, I think… I wasn't in a meeting, in this meeting last week, but I think someone told me that last week you had a question about… Multi-agent systems, and… You know, so I'm told to join.
Yeah, my… See if you have any questions.
**Sergey Sergeev** 04:25 Thank you so much, yeah, you probably have a time just… bootstrapping my brain what was happening the last week, by basically looking at the notes, which we took, A3.
**Surya Teja** 04:44 Hey, hi, Sergei, how are you?
**Sergey Sergeev** 04:46 Good, getting up to speed, and just starting the document.
I'm… Looking at… The last Monday meeting.
And, what we had, on it. Oh, the last Monday…
**Tao** 05:10 It… maybe it's… hmm… We should last me.
**Sergey Sergeev** 05:18 So… Okay, we had, A few questions, About the frameworks, maybe we can, have them Repeat it, Yeah, put your names in the doc if you can.
Yeah, so Chao, since you are here, probably we can use… Some of your time, specifically for… I assume you… you have some customers of that framework, So, do you see, basically, any use cases? So, first of all, semantic kernel, do you extend semantic convention with some custom attributes and etc?
**Tao** 07:02 Yeah, both semantic kernel and, Microsoft Agent Framework has, well, they both use, hotels and many conventions.
the Gen AO ones.
**Sergey Sergeev** 07:19 But do you extend it?
I mean, something which is not, in semantic convention, you just implement it on your own.
**Tao** 07:32 For semantic kernel, no. For agent framework, we have something called the workflows.
Workflows can kind of… you can think of it kind of like a graph.
Right? So, to trace… The steps within a workflow, we have something proprietary.
So that you can kind of think… you can think of it as, like, the extension of the GenAI convention. Yeah, yeah. But we don't prefix it… prefix those spans with the Gen AI…
**Sergey Sergeev** 08:09 Oh, you don't.
**Tao** 08:11 Yeah, it's… yeah, but those are… if you… If you consider those as… GenAI-related spends, then yes.
But, you know, because it's a workflow, it doesn't necessarily need AI.
So… Yeah, it depends on how people interpret it.
**Sergey Sergeev** 08:36 Yeah, the… the team, at least the Splunk team, is working on… Proposing… into semantic conventions workflow, specifically GenA workflow.
And this is a spend level.
**Tao** 08:54 Oh, there's, oh, sorry to interrupt. So there's a new… SPACT, that's, focused on workflows.
**Sergey Sergeev** 09:05 Yeah, workforce pick. Workforce plans, right?
**Tao** 09:10 Oh, oh.
**Sergey Sergeev** 09:10 Okay. Yeah, and direct quotes, Span, represents, basically, some… grouping of different Gen AI spans, so when you execute the same steps, basically, it's valuable to track it.
**Tao** 09:31 Okay. Yeah, I see, I think I saw a PR that was, proposing the workflow invoke.
**Sergey Sergeev** 09:40 Spend.
Yeah. But…
**Tao** 09:42 I think that PR's still open.
**Sergey Sergeev** 09:45 Yeah.
Oily… It will be… fixed soon, Yeah, would be great to hear from you.
And your team.
If it's applicable.
**Tao** 10:21 Yeah, I will take a look at this PR, review it. But I think, you know, there… more than that, right? So… You know… how do I put this? So, invoke workflow is just kind of like invoke agent, right?
**Sergey Sergeev** 10:37 Yeah. Where…
**Tao** 10:39 it's the entry point of the agent, but then underneath, you still have the SEQ tool, spans, and everything.
for workflow, it's even more complex, right? So you have OneNote sending messages to a bunch of other notes, right? And then… You know, or, you know, so basically there are multiple… there are many message sending patterns.
that… I think that that student needs to.
**Sergey Sergeev** 11:10 Yeah, it feels like, there are different, types of grouping being discussed, so there is, that… GenAI session concept as well, which maybe is a workflow in your terms. So basically, when you execute, Distributed coordination, basically running a workflow, right?
In… This case, the question is when trace ID is not sufficient to track it.
**Tao** 11:50 when trace ID is not sufficient to track.
Which agent invoked?
Which agent is that to question?
**Sergey Sergeev** 12:01 So basically, if you have that invoke workflow.
Span, which indicates, basically, okay, we started a workflow.
And from this point, you… your agents execute the workflow, I'm not sure how it looks like in Microsoft Agentic Framework, but… I assume… it… maybe… some other operations.
So, for example, workflow, I assume, may include an agent on vacation, 2 on vacation, LM on vacation.
And so on, right?
**Tao** 12:44 Well, a workflow is composed of multiple agents, right?
And then an agent is… an LM with… tools.
Right.
So, invoke workflow.
The first thing it does is just… Invoke the first agent.
Right, and then depending on some… depending on the agent or some custom logic, you can invoke After the first agent, you know, you can invoke the… the workflow will invoke the next agent.
Right? Or… or… it can invoke multiple next agents, right? And then, you know, you can even create loops, and… and you can create conditions, right, depending on the output of the first agent.
You know, you can… Use some condition to decide what… Which, group of agents to invoke.
in the next round, right? Things like that. So there are many patterns, and… You can build within your workflow.
Right, and you can even have… An agent, you know, and the next… the next step is not agent, right?
So, it really… so it's… so it's very flexible, and… it's basically a graph, and each node can be an agent or non-agent, right? And each node can be Can't even… you know, because we don't define the node. You, as the user, defines the note. And you can put many agents in one note, too, if that's what you want. So we don't make that restriction.
But from a high-level concept, right, a workflow is composed of nodes. Most often, each node is a… it's an agent.
So we can abstract that concept away, right? When we invoke a node, it's actually invoking an agent.
But, I mean, but we don't make that restriction. But, I mean, for the purpose of Gen AI Convention, I think we can assume That inside a workflow, everything will be an agent.
So… You know, workflow invoked.
Underneath will be a bunch of invoke, well, invoke workflow. Underneath will be a bunch of invoke agent spans.
And then… I think the question is.
Because we… I think the purpose is to know which agent triggers which other agents.
Right.
I think that's the… that's… that concept… that concept needs to be formalized.
Right.
Right now, what we're doing in Adrian Framework is we're using links.
So… Say, Agent B, right, is triggered by Agent A, And inside the invoke agent span of agent B, we have a link that points to the span of Agent A.
And that's how we draw that relationship.
**Sergey Sergeev** 16:13 Sorry, can you… That's not necessary. Can you repeat that? Well, maybe…
**Tao** 16:16 So…
**Sergey Sergeev** 16:17 If you…
**Tao** 16:18 Yeah.
**Sergey Sergeev** 16:18 Any UI to show how it looks like?
**Tao** 16:23 Yeah, I can… I can show you.
**Sergey Sergeev** 16:25 Yeah, let me stop sharing.
**Tao** 16:38 Make sure I'm not throwing anything confidential So… Let me share.
Okay, can you see my screen?
**Sergey Sergeev** 16:57 Yes, we can.
**Tao** 16:58 Yeah, so this is a workflow, right?
And right now, we're not using the invoke workflow span name, we're using something proprietary, and the name is workflow.run, but it's the same concept as invoke workflow.
Right. Underneath, you see, two spans, right? You see the executor process? You can think of executor as a note.
Right? Executive processes to spend that encapsulates the invocation of that note.
Right? So it would capture the ID of… The… the node and the type.
And then, We're not capturing any input and output messages yet.
But you can see here this node executes. It's a demo program, so the processing is very fast. It's simply reversing a string and making a string uppercase, so you don't see the time. And here, once it finishes processing, it sends out a message.
Right, so this is… edge group is the edge connecting the nodes.
This is a single edge group. That means this edge group only has one edge. Only has a single edge.
where it processes messages and sends to the… to the next… to the next node, which is the… the other node that is reversing the text. And you can see here.
It has a link.
Right.
to the previous span, that is the, the send message, right? So we know which message triggered this node, right?
So here. And then here you can see the message, you can see this message, right? Yeah, so… Single edge group, this is the link.
And… message sent… So this is the outgoing link.
This is the link.
to itself. No way, actually.
Yeah, so this is the outgoing link, this is the incoming link. So, you can see here, Oh, wow, shall we? One sec.
Yeah, so this is the outgoing link. So this message… this message sent is from within the executor, right? So this executor sends the message, and then it goes to this group, this edge group, and then within this edge group.
So we can trace back, right? So here, we can trace back to which executor sends the message. Yes. Sorry, I messed up a little. So, this executor… Right, has a link.
Going back to which executor sends this message.
So that's how we link the two… Processing steps.
together. It's not nested, as you can see here, because these are not nested processes.
They're parallel, right? And the way we draw the connection is via links.
Right here, right, you can go back. So here, this span is the node processing span, but somehow, if you need to know which message, right? Which message triggered this note? You know, you trace back through the link. And here we see, okay, so it's actually this message sent, right? And we can, from this message, we can tell This message is nested below this executor span.
Right? So this is how we know how you draw the connection between the two executors, right? So this executor may send multiple messages, right? Say, for example, you have kind of, like, a fan-out kind of thing.
Right? So this… this executor, we send multiple messages. Each of those messages will link to a different executor, right? Say you have executor A, right? It sends a… it sends out to executor BCD.
Great.
And so, if you go into BCD, you can go back to the link, through the link, to that message that triggered the note. And you can go back to, using the message sent, you can see, oh, this is actually coming from this particular executor.
It's not ideal, but this is the way we're doing it at this moment.
**Sergey Sergeev** 21:46 Yeah, thank you for sharing it, it's, super cool.
I… So, basically, you… You don't have that direct, parent-child relationships, in the span.
**Tao** 22:01 Yeah, because… Because it's not… because, say, you have a long-running agency.
Right? Or long-running workflow. The agents will… You know, if you have, like, a… two agents, right? A simplified example, right? Say if you have two agents, and just… they just talk to each other.
**Sergey Sergeev** 22:20 Yeah.
**Tao** 22:20 Then you have some infinite nested span.
Right Then, that's not… probably not so good.
**Sergey Sergeev** 22:28 Well, you will see, basically, So they can be still parallel.
For that, if they… Don't have that parent-child relationships, yeah, it's…
**Tao** 22:46 And that's… yeah, and that also… and inside the system, right, there are not… if Agent A invokes Agent B, they're not, like, Agent A invoking Agent B in its own context, right? It's… it's via message.
sending, right? They send messages, right? So, once… Agent A sends the message, Agent A is considered finished, right? So… so I think the child… parent-child relationship doesn't make sense in this context, because Agent A is not the parent of Agent B.
Right? It just sends out a message, and then Agent B picks up, right?
And Agent B does its own processing. Agent B is not the trial of Agent A. So in… you can… in your workflow, you can kind of think of it, Agent B is the trial of Agent A, but in this… from the system's perspective, right, Agent A doesn't own Agent B.
**Sergey Sergeev** 23:52 Yeah.
No, this, this is interesting, I… I'm wondering how it will look like, in… Something like A2A… Protocol, when we have agents, basically, taking over, and etc.
I think this approach, still makes sense. Really cool to see that you have, spend links for Tracon, the regional… Message instead of parent-child, Still back to the workflow, I think, I think, our proposal for in-work workflow I think it should work for… What you do, so you have that, workflow run, but it doesn't have GenAI input and output.
Yep.
**Tao** 24:58 We, we do. In the trace.
that I showed, I just did not enable that, because those are… you need to, you know, enable a flag. Those were considered sensitive information, right, the input, so we need to specifically enable that. But in the sample I show, I just didn't enable that.
**Sergey Sergeev** 25:18 Yeah, maybe you can just look into it and fit, if the proposal works for you.
Maybe we can… you can join the proposal to… Because I think what we proposed on the spend level, that invoke workflow GenAI-specific type, it may work because, basically it's JAI-specific input and output, and it may help you also to visualize it on the backend.
Because, what basically… What user asked, or what was the request to do for the agent.
And the output is, what was the final output, if there is one.
**Tao** 26:07 Oh, yeah, the input, we can track, but then the output, it's more… tricky. Yeah. So I can, I can explain briefly, right? So for a workflow, you have one input, right? For… for a run, right? Yeah.
But then you may have multiple outputs, or no outputs at all, right?
**Sergey Sergeev** 26:32 You run, basically, parallel agents, and you… each of them Took some action.
**Tao** 26:42 Yeah, maybe no output at all.
Yeah.
**Sergey Sergeev** 26:46 Our output may be as an email.
**Tao** 26:49 Yeah, so maybe that will be… Yeah, I need to take a look at the PR and see if it's included in… Oh.
**Sergey Sergeev** 26:57 Yeah, any of your feedback on what you see from… From the customer base and real use cases will be really, really helpful.
Also, we are trying to simplify a little bit, Usage of, Creation of new instrumentations and etc. by introducing… And utility function with a different type, so Airdan added, an agent, also.
So we have, basically, as part of the OpenTelemet Python concept, we have, a bunch of tools.
Which we put, into… that U2Gen EA… Package.
Where you can simplify telemedication, but by using those APIs, so basically… you can use something like StartAgent, and… Fail agent, stop agent.
to import, open Telematismantic Convention.
Telemetry, such as spam, metrics, and etc.
Maybe, if you're using… open Telemati SDK directly.
So you will have that overhead of maintaining all the semantic invention. This way, may simplify Basically, your instrumentation and telemedication, so… Maybe worth looking for your team.
**Tao** 28:56 Are you talking about, suggesting us to use this, or are you just talking about this? Yeah. Oh, we have instrumentation built in directly in our code.
**Sergey Sergeev** 29:10 Yeah, yeah, yeah, we chat.
**Tao** 29:12 Yeah.
**Sergey Sergeev** 29:13 Yeah, right now, it's not part of instrumentation, it's part of OpenClemmata extension for Generator for AI.
So, basically.
**Tao** 29:22 Oh, okay.
**Sergey Sergeev** 29:22 One way you can, create Telematy, you can, basically call OpenTelematy SDK, like, Start Span, Startmatic, whatever the APIs are, or you can use higher-level APIs, from that, OpenTelemati Hotel Gen AI.
And just, instead of, trying to… To guess what are all the semantic conventions for everything, you can just use high-level APIs, Python APIs.
**Tao** 29:58 I see.
**Sergey Sergeev** 29:58 To start, stop, those things, and… You can also control which… Telemeting UAE meet, and so on.
**Tao** 30:10 I see. Yeah. So one question I have, about this is… So this Python package, what is the release cadence? Because we took an update last week, and then it contained breaking changes, but then it was… It was the first release for… Since… The last… it's been a couple of months since the last one, and then it included multiple Releases of the semantic conventions.
**Sergey Sergeev** 30:45 Yeah, I think this is, a problem for sure. First of all, making changes, yes, the mighty convention changed, ironically.
And, this package, if you use a particular version, and pinpoint to that version, so you will ensure You will ensure the same semantic conventions for this, and this is one way to control if you're just using SDK directly, you will have to pinpoint the whole SDK.
here, pinpointing, the version of OpenTelemetry Gen AI will guarantee Same semantic conventions, but… Yeah, breaking… we hope to merge more of the type support as we go. It will be agent workflow, embeddings, and etc.
once we merged it, so I think it will be no vacant changes.
From that point, once we release.
**Tao** 31:52 Hmm, okay.
Yeah, the last breaking change I saw was we remove.
**Sergey Sergeev** 31:56 the Gen AI system.
**Tao** 31:59 And… And that… Yeah, that, that broke, part of our code, but it's not a big, big deal.
It's just surprising.
**Sergey Sergeev** 32:12 Yeah.
Sorry, we are out of time for this particular meeting, so tomorrow will be a longer and bigger group.
Ciao, thank you so much for… for this. Please review the workflow… and work, workflow span.
I have it.
**Tao** 32:30 Right.
**Sergey Sergeev** 32:30 That it may work for you, but any feedback, if it doesn't work, or if you think it should be more generic, will help, for sure.
**Tao** 32:39 Yeah.
Sounds good.
**Sergey Sergeev** 32:44 Thank you, everybody.
**Tao** 32:46 Alright, thank you so much, Suki.
**Surya Teja** 32:47 I congrats.
**Erdenesaikhan Tserendavga** 32:50 Thank you.

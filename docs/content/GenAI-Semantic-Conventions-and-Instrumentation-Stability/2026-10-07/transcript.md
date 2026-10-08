SIG: GenAI Semantic Conventions and Instrumentation Stability
Date: 2026-10-07
Duration: 30 minutes
============================================================

## Zoom Recording Transcript

**Siri Varma Vegiraju** 00:57 Hello, Milo.
**Liudmila Molkova** 01:00 Hello, how are you?
**Siri Varma Vegiraju** 01:02 Good. You?
**Liudmila Molkova** 01:05 Also good, thank you.
Hi Emil.
**Emil F** 01:23 Hello.
**Liudmila Molkova** 01:39 Thanks.
**Trask Stalnaker (Microsoft Corporation)** 01:40 Hey, Fox.
**Liudmila Molkova** 01:43 Hello.
Yeah, let's see what they have to review… For the scope of the Stability… And.
And then now, if we have a good view on… Everything in progress.
And… The board or anything.
Oh, sorry?
**Trask Stalnaker (Microsoft Corporation)** 02:30 you.
**Liudmila Molkova** 02:30 Wrong one.
Okay, I'm going to just pretend that I know which ones are related to Stability.
I… Yes.
Maybe this one.
So I think… This is a good one.
The review… Oh, it's a usage histogram, sorry, yeah.
This is… Some small clarification… I don't even remember what is it about.
But I think it came up in the JavaScript.
Anyway, so we'll… we'll get there.
I don't think it's controversial or urgent.
What's this one about?
Yeah, some clarification for the tools.
Maybe we can keep it in the bucket of… Arch.
Okay, I'm leaving it here, so we don't forget to take a look. I don't know if we need to discuss each of them independently, or I don't think I'm ready to have any discussions on this one. I didn't take another look.
I'm curious…
**Trask Stalnaker (Microsoft Corporation)** 05:36 Probably one quick one. If the failed ops tokens can you open that?
0… Let's see, so, yeah, here, let's look. Should we record this metric for Opera with a non-zero token count?
I thought that we… I thought that it was gonna be also zero count?
why I didn't… I felt like I missed something.
Oh, it's different down here, maybe…
**Liudmila Molkova** 06:18 So it's counter. It makes no sense to record counter with zero value.
**Trask Stalnaker (Microsoft Corporation)** 06:23 Oh, okay.
**Liudmila Molkova** 06:26 And then let's see your histograms. That's what I missed.
And… This is the histogram.
**Trask Stalnaker (Microsoft Corporation)** 06:41 Yeah, okay, thank you. That's what I missed. The obvious thing I missed.
**Liudmila Molkova** 06:48 Very unobvious.
**Trask Stalnaker (Microsoft Corporation)** 06:52 I mean, it would be the same if we left it out, though, since it's a counter.
**Liudmila Molkova** 06:57 Right.
Yeah.
**Trask Stalnaker (Microsoft Corporation)** 07:02 But I'm fine with it being… it's… not relevant, then.
Cool, thank you, I will approve that one.
**Liudmila Molkova** 07:14 Arun, you said something?
**Aaron Abbott (Google LLC)** 07:15 Sorry, in terms of it being a counter, like, yeah, can you hear me?
**Trask Stalnaker (Microsoft Corporation)** 07:17 Yeah.
**Aaron Abbott (Google LLC)** 07:19 Sorry, I'm having some internet issues.
Anyway, sorry, I was saying, do we think that people might configure the counters to a different instrument, like histogram, potentially?
I think it wouldn't make sense based on what we've said, but then the zero counts would have a slightly different semantic…
**Liudmila Molkova** 07:42 I missed the first part.
**Trask Stalnaker (Microsoft Corporation)** 07:44 If you change the aggregation via a view.
**Liudmila Molkova** 07:47 Oh.
Oh.
Would it… would it make sense for Kant, or anybody, to add a zero?
**Aaron Abbott (Google LLC)** 08:01 I mean, it's possible you could include, like, an exemplar also?
**Liudmila Molkova** 08:07 Oh, in a counter?
**Aaron Abbott (Google LLC)** 08:09 Yeah.
**Liudmila Molkova** 08:13 Okay, so record for all.
**Aaron Abbott (Google LLC)** 08:18 I don't know, I mean, what have we done in other… Conventions.
**Liudmila Molkova** 08:24 It's pretty unique. We don't go into this level of details anywhere, I think.
**Aaron Abbott (Google LLC)** 08:29 Okay, I mean, maybe we can just leave it unspecified for now, and then… Treat it as a bug fix if people want.
**Liudmila Molkova** 08:36 And wait, what?
I mean, we can say included for all operations.
**Trask Stalnaker (Microsoft Corporation)** 08:42 Yeah, I would just remove that. Yeah, I would just remove the with a non-zero token count.
**Liudmila Molkova** 08:58 All operations… including… Failed operations.
Should we just make it the same?
Between histogram and counter.
**Trask Stalnaker (Microsoft Corporation)** 09:13 Yeah.
**Liudmila Molkova** 09:14 It's just not worth it, right? Yeah. To have any special logic.
Okay, sounds good.
Great.
Moving on, maybe… This one is a quick one. Oh, Dylan, you have another one, right? Or it's the same?
**Dylan Russell** 10:57 This is the one we've been working on, I think.
Yeah.
**Liudmila Molkova** 11:07 So this is both debug and… Oh, wait, this is the Python PR. Do you have the Semantic Conventions one as well, right?
**Dylan Russell** 11:18 Oh, yes, yes.
We have a one to just make it, like, recommended instead of… opt-in.
**Liudmila Molkova** 11:29 All right.
So we are just using the regular login mechanisms, then.
**Dylan Russell** 11:48 Yes.
If people want to opt out, they just use, like, the logging enabled What is it? It's like a filter-enabled thing.
And, yeah, they can opt out through declarative config, or… By, like, creating their own, like, processor to opt out.
**Liudmila Molkova** 12:18 Okay, and then I'm going to put… here…
**Dylan Russell** 12:25 I have one minor random question.
I was gonna go try and change the spec.
On, like, filter enabled?
To, like, add a, like, default parameter.
So you could have, like, opt-in events.
And when you check, like, logger.enabled.
Default equals false, for example.
Because right now, the default is to, like, return true.
Anyway, yeah, I opened a bug, and maybe it'll be more clear. I went to issue on this.
Yeah.
**Liudmila Molkova** 13:19 Oh, I see, so, like…
**Dylan Russell** 13:21 Yeah.
**Liudmila Molkova** 13:24 Oh, this… I think this… this is… This is coming… maybe coming in some other ways through declarative config and options we would define for GenAI instrumentation.
So the instrumentation wouldn't need to know.
I need to check if this event is enabled, so the declarative config option first.
**Dylan Russell** 14:01 I'm not following you exactly, but…
**Liudmila Molkova** 14:05 I guess, do we… Do we need, do we, are we blocked on this in the spec?
**Dylan Russell** 14:11 So.
**Liudmila Molkova** 14:11 We're changing to the default, to the recommended.
**Dylan Russell** 14:14 Not blocking at all for us.
I was just gonna ask, what meeting do I go to to discuss this?
**Liudmila Molkova** 14:21 SPAC call.
**Dylan Russell** 14:22 Okay, okay.
**Liudmila Molkova** 14:24 and check, there is a similar issue for metrics, I think, David.
Ashpole was pushing for a very similar thing for a metric sub.
Sydney Metric Advisory or something, so it would be… Very natural to do the same approach for both signals.
**Dylan Russell** 14:44 Oh, okay. I'll talk to David then.
**Liudmila Molkova** 14:50 Awesome.
Okay.
I kind of want to use this time to talk about the… Agent workflow stuff.
That we started last time.
But I don't think Max is… Here.
Yeah.
So… Can you put… This in the list of the PRs.
So Max did another round.
And I've tried to summarize, from The PR… And the discussions we had.
what it all… Bows down to… And I think this is the current proposal from Max.
We have… different pen names.
For different operations, but the same metric and the same spend type.
And.
And depending on who does it, it is… The meaning is slightly… different, but, give me a sec.
So what does it mean, the semantics?
Everybody calls it differently, but, let's call it full.
But essentially, every… everything has some notion that means Okay, I started doing stuff, like, Agentic thing.
Based on some input I've got, and once I have an output, or some final outcome.
This is the fool.
So the process of getting this food.
Sorry, the process of getting the final Output based on the input.
**Trask Stalnaker (Microsoft Corporation)** 17:08 If it helps, my confusion is between, is the semantic difference between the Turn, step… The turn and the agent.
Invoke agent and handle turn.
like, when… When do I pick one or the other?
**Liudmila Molkova** 17:39 So I would imagine if we look here, when… You don't know it's an agent, you run.
something?
**Trask Stalnaker (Microsoft Corporation)** 17:56 Oh, you don't know it's an agent at that point?
**Liudmila Molkova** 18:00 It's not… yeah, it's… it's something. It can be a graph, it can be a… An agent, it can be a workflow.
You can start with the planner, but then there are five other agents that could kick in.
**Trask Stalnaker (Microsoft Corporation)** 18:19 Okay, and so the overarching thing For that, while… Typically, people call it an agent, it's not really an agent, it's… It's a… component… And so that's… that's the distinction we're drawing, is.
Okay, and that kind of fits with preserving, then, workflow as something different, also, because Again, like, I was, like… colloquially.
People call everything an agent. It's a workflow, it's an agent, it's.
But we're drawing, kind of, that distinction of three things, kind of, more fine-grained, more accurate.
Terminology for those 3 things.
But at the same time, we're… because we're wrapping them all in the same span type and metric, we're also acknowledging that they're more or less all three the same thing, but with slight Semantic differences.
**Liudmila Molkova** 19:25 Yeah. Surya.
**Surya Teja** 19:30 Yeah, mostly from what I understand, every framework is using workflow to.
Demonstrate something that is deterministic.
Say, you know, the flow will be repeatable and everything is as per steps. That's the workflow. And agents are something that are non-deterministic in nature.
if you give the same task to the agent in two different settings, it's going to be doing things differently in the two different settings, and it is non… it is non-deterministic. So… That's what we are doing it.
**Liudmila Molkova** 20:09 I think we're getting at, we have multiple things that all represent some Agentic.
Scenario.
And they are pretty much.
**Surya Teja** 20:19 licenses.
**Liudmila Molkova** 20:19 Same, but they are… sometimes they are non-deterministic agents, sometimes they are called workflow, sometimes they are called runner, or loop, or whatever.
**Surya Teja** 20:31 Yeah, yeah.
**Liudmila Molkova** 20:32 Yeah.
I think Emil, you were next.
**Emil F** 20:40 Yes, thank you. So, first, like, yeah, thanks for setting up a vocabulary. I think it's sort of needed, and as Surya said, like, the clarification between what is a workflow, what is an agent makes a lot of sense, especially if it's in a common place somewhere in the conventions that everybody can refer to.
But I also really like the Trask question. Like, in what scenarios Would the handle turn, or whatever we call it?
Would it… Not.
Come before, like, a start agent, or invoke agent, or invoke workflow.
Like, do we put it in front of every invoke agent to turn?
Because it's a… it's a new Agentic system that starts up.
And the other kind of slightly related question that I have is in the multi-agent scenario, and, like, a deep tree. let's say, agents or turtles all the way down.
Do we put handle turns?
Before each… Each invocation that we consider to be some somewhat encapsulated agent system.
Or do we do a single handle turn at the entry of the Agentic systems?
**Trask Stalnaker (Microsoft Corporation)** 22:01 Let me try to, sort of, my understanding from.
See if that matches, is that handle turn, we would pick handle turn for… Any framework where we… it's not an agent.
And it's not a workflow.
Like, it's… it's a third category of things, and… Lamilla was earlier showing on the PR, kind of the list of things, like Google ADK Run.
Where… it's… a framework… Call that wraps stuff, but isn't an agent by itself, and doesn't fit workflow?
**Liudmila Molkova** 22:52 And then, if… Okay, and then for this thing… There's still a good question, if there is just one agent, and you know if there's just one.
Would there be a need to… I have… Handle churn at all.
So here, it's kind of clear.
**Trask Stalnaker (Microsoft Corporation)** 23:31 I mean, if you are invoking an agent.
it seems like handle turn isn't needed. It seems like handle turn is sort of this… New… thing… New third category of things that.
isn't an agent. Like, would you ask, Sam, would you have an agent name on Handle Turn?
I'm assuming no, because if you had an agent name on it, that means you know what the agent is, and then it feels like it would be an invoke agent.
**Liudmila Molkova** 24:04 Wait.
It can be, I'd say, in LangGraph, I think you can give a custom name to a graph.
**Trask Stalnaker (Microsoft Corporation)** 24:15 Oh, okay.
So, we're calling it an agent… Joe Moore, Colloquially, we're grouping it all still as an agent, an agent name, we're just differentiating slightly that it's a handle turn.
**Liudmila Molkova** 24:34 I feel like… I… I don't… It goes against my understanding that we give special meaning to the string. Maybe it's temporary, it has special meaning.
But it could be anything. It could be arbitrary strings.
It could be execute graph, and nobody would care, ideally.
**Trask Stalnaker (Microsoft Corporation)** 24:55 Oh, okay. So you're… Just… yeah.
So what's the def… okay, so it's just a span name, and frameworks can use whatever span name is.
Makes sense.
To their… to them.
But it's… everything is still on invoke agent, or whatever we're generic, or, Foo, whatever we're using as our generic term for all three.
**Liudmila Molkova** 25:27 Yeah. We'll live in a in a time where we need operation names to be somewhat fixed. So we kinda have to talk about it a little bit.
But I I hand this queries to demonstrate that Like, if you want to find all… Metrics.
Sorry, all, let's say… Invocation spans.
Today.
This is what you would do. You need to know a fixed list of things that represent agent invocation.
with Dan.
At some point, we want people to write this instead.
And for metrics, there is no such problem.
And maybe for metrics, it means… that the answer… To this question is that you report one if you know they are the same.
**Emil F** 26:48 I guess that sometimes you wouldn't know, like… The… the graph… Might short-circuit earlier, or if it's an agent with a, you know.
But can they decide to call other agents, or… And decide to not call other agents.
**Liudmila Molkova** 27:04 Based on the configuration, right? So if your graph is configured with just one node.
you… report one. If your graph is configured with multiple nodes, it doesn't matter if they're short-circuited, you report The the outer 2.
**Emil F** 27:25 Okay, I see.
**Trask Stalnaker (Microsoft Corporation)** 27:28 And I don't think it would… wouldn't necessarily be wrong if you reported the… the workflow node and the single agent there. I mean, it's… it's sort of… a… I see it as… It's just a grouping. It's sort of… Telling you a little bit more about.
the operation.
pieces were involved.
**Emil F** 28:07 So… If I understand correctly, this is basically the entry point of the agent graph.
Or the agent loop. That's what we want to mark with this.
With this, span type.
And spell names.
**Liudmila Molkova** 28:23 The span type means any.
Agent invocation, workflow invocation, or any such a thing.
Right?
**Emil F** 28:34 Yep.
**Liudmila Molkova** 28:35 All of them at once.
This guy, it's.
Almost meaningless, the, the thing we care about is we need some way to distinguish the outermost.
Thing.
From the nested one, and it's orthogonal.
**Dylan Russell** 28:52 I think in ADK, there's, like, this concept of, like, a… Like a runner.
which decides, like, which agent to… Invoke.
And you just call the runner.
And let the runner kind of, like, decide which agents to call.
Like, what to do.
So they're… yeah.
**Aaron Abbott (Google LLC)** 29:21 Yeah, I feel like this thing is… Before the workflow and before the graph, like it's the entry point to the harness. And if say it does some stuff before it runs the graph, say it like.
sets up an MCP connection, or it fetches, like, agent card for subagents or something like that. Like, we do need a parent for that stuff, and it might be… Before, I feel like… There's always going to be some code that runs as part of the harness before, like, the The agent workflow actually starts, right?
**Liudmila Molkova** 29:57 Okay, yeah.
**Emil F** 29:58 Yeah, that makes sense.
Rojaduno.
**Liudmila Molkova** 30:04 Yeah, I was just going to say that it's… the SDK Instrumentation choice to create this or not, and depending on which conditions.
We are at time, and we didn't even start.
**Trask Stalnaker (Microsoft Corporation)** 30:22 No, that was good. I… feel like I have, It makes sense to me, at least.
It's not that handle turn is, like, a special, like, a better, like, outermost that everybody should be emitting these, like, outermost turn… spans. It's more just… For some frameworks, there's this… Slight variation that doesn't quite fit Invoke Agent, doesn't quite fit Invoke Workflow, so we're just creating a third.
Sort of variant, but at the same time, because we're combining them all in the same span type, we're essentially saying.
They're all the same. Here's the structure across. They're just a structured… showing structure.
Yeah, Jeff.
Hey.
**Jeff Leva** 31:32 Oh, hi. Sorry to kind of pop in unannounced. Since we're at time, I wanted to check real quick before everybody broke. Somebody gave me this meeting invite. I work with COSI and OCSF, and specifically on the COSI, we're trying to Work on some, security, telemetry.
definitions and alignment. This kind of seemed like part of where I would need to be. Can somebody direct me if this is the right place for OTEL, or is there another meeting that I should be in?
**Trask Stalnaker (Microsoft Corporation)** 32:07 Yeah, you're super close. This is more or less the right group of people. The Monday… we have a lot of different meetings within this group. The Monday, Wednesday, Friday meetings are, focused on the stabilization effort, for, sort of, exist… For the kind of core, GenAI Semantic Conventions that have existed, or that we're trying to iron out.
And then the Tuesday 9 a.m. Pacific meeting, the one hour meeting, that's the kind of general topics meeting. And that would probably be the best place to.
**Jeff Leva** 32:44 Okay.
**Trask Stalnaker (Microsoft Corporation)** 32:45 Can, throw your topic on the agenda, and yeah, would love to…
**Jeff Leva** 32:49 Okay.
Cool.
**Trask Stalnaker (Microsoft Corporation)** 32:52 Hear more about it.
**Jeff Leva** 32:52 Thank you very much. Yeah, I figured that was a good one to go to. Tuesdays tend to be hard for me, but, and I missed this week, obviously, so yeah, I'll try to get to that one next week. Is there a repo or anything?
Well, not to get too far ahead that I can open issues on.
**Trask Stalnaker (Microsoft Corporation)** 33:09 Yeah, for sure.
**Liudmila Molkova** 33:11 Yeah, this one.
Pasting in the chat.
**Jeff Leva** 33:15 Okay, thank you.
Thank you. Awesome.
Okay, well, yep, thank you, sorry for barging in, so…
**Trask Stalnaker (Microsoft Corporation)** 33:24 No worries. Thanks.
**Liudmila Molkova** 33:26 Cool, then thank you all, see you around.
**Jeff Leva** 33:28 Okay, thank you. Bye.

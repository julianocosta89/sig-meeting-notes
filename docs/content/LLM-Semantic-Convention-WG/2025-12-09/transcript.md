SIG: LLM Semantic Convention WG
Date: 2025-12-09
Duration: 67 minutes
============================================================

## Zoom Recording Transcript

Liudmila Molkova 00:04:47 Hello, hi everyone. Sorry for being late.
And let's get started.
Let's… the… What we have on the agenda.
How's everybody doing?
Okay. Not bad.
That's great.
Okay, let's take a look at the new issues. Model parameters and object.
I haven't seen this…
So if anybody has thoughts, please take a look, share your thoughts. I think the question is…
There are important parameters that we promote to top-level attributes, and there is the Rust, and,
That's a good question.
I'll keep it in the triage and new issues, so if people have thoughts, you would pause them and we'll decide what to do.
Alex Hall 00:06:23 Maybe, maybe… implementation could just, like, record the entire request body… Minus the big parts.
Even… even if things like temperature get duplicated, just so that people can see the exact thing that was sent.
Without worrying about normalization.
It's just an idea.
Liudmila Molkova 00:06:48 Also, it would also include the messages.
Alex Hall 00:06:53 No, not the messages. I think, as in… minus the big parts, so specifically messages.
The tool definitions, whatever, would get left out, but…
I mean, I don't know exactly about how this would be defined, but…
Especially if the request happens to, like, bundle messages and stuff separately from I don't know, provinces.
Then it might be very doable, too.
Just record everything.
Smaller.
Liudmila Molkova 00:07:39 And if it… if we can have a logic, in theory, that says, okay, there is temperature, there is, I don't know, tokens, max tokens, there are messages, these are known.
maybe we should exclude not the big parts, but known parts, right? Because it's the safe, right?
And I think there was a…
PR for this one, for, GCP.
Ugh.
Sprint.
And one thing we can do, it kinda makes sense, right?
It's the common ask.
And it's a common thing people do.
So I can say it's to do, it's somewhere in the backlog.
I know.
Let's see… Let's take a look at another one.
Crush.
Reception raised.
Would anybody be able to take a look?
Aaron Abbott 00:10:05 Looks like they found the bug, maybe they'd be willing to send a PR.
Liudmila Molkova 00:10:10 Yeah.
Aaron Abbott 00:10:11 Oh, Ricardo.
Liudmila Molkova 00:10:21 Blank chain up in the eye.
Okay.
Aaron Abbott 00:10:39 Yeah, we… the only thing… we usually don't assign people, just because,
If people don't get back to it, It just kinda sits.
But yeah.
Liudmila Molkova 00:10:52 I, I would love if we could, if we get…
Like, straightforward bug, and we know how to fix it, we can just Go ahead and…
Fixed them, in days, not weeks.
So, I…
I hope somebody will come back. I'll keep an eye on this issue. If nobody comes, I'll send a fix.
Aaron Abbott 00:11:28 Thank you.
Liudmila Molkova 00:11:30 Okay, so this is definitely a to-do.
Cool, we are out of the time box for our triage session.
So if, anybody would like to introduce themselves, go ahead.
anksing 00:11:51 Hello, hi, this is Ankit, and I've been out for quite some time. I've been working on one of the PR for built-in tools, and I've got that in here, so I'll be happy to chat about that today, and get any feedback.
Thank you.
Liudmila Molkova 00:12:13 Anyone else?
Okay.
So then let's move on to the agenda. So, I…
I've addressed the feedback points we discussed on the MCPPR.
And that's a big one, there were a lot of discussions, and there are some trade-offs.
I… would appreciate if people are still interested in MCP, if they…
give it another round of review, and if you're happy with it, then approve. If you're not interested in MCP, then so be it.
Okay, that was just the announcement,
Tia, do we need to talk about it, or is it already merged? All good?
Surya Teja 00:13:11 No, it's… oh, it's merged. I'm sorry, I haven't seen that it's merged.
Aaron Abbott 00:13:17 Go ahead.
Surya Teja 00:13:18 Yeah.
Yeah, sorry, Aaron, I have been troubling you by reaching out to you directly, but
Just wanted to get this ahead and focus on the next things that I already have in pipeline.
Liudmila Molkova 00:13:29 Wonderful.
Thanks, Erin.
Surya Teja 00:13:32 Yeah, thanks to Aaron a lot.
Aaron Abbott 00:13:36 No, thank you.
Liudmila Molkova 00:13:39 Okay, it came out, the proposal for the… Edge and PRs?
Which one do you want to start with first?
Ridhima Satam 00:13:53 Yeah, so we can open the proposal here. Hi, I'm Radhima, so…
Liudmila Molkova 00:13:58 They want to present.
Ridhima Satam 00:14:00 Yeah, I can present, actually.
Liudmila Molkova 00:14:01 Yeah.
Ridhima Satam 00:14:13 Oh, here we are.
Okay, can you see?
Can everyone see?
Liudmila Molkova 00:14:19 Yep.
Ridhima Satam 00:14:20 So, I think this proposal was there earlier. I mean, we introduced it, some time ago, but most of it was, mostly it was about Langraph, and I think the feedback we got at that time was, like, most, we have to consider other agentic frameworks for this, so we went back and did, Creo AI and OpenAI agents research also in this.
So, this talks about mainly introducing two new spans, workflow and step.
And… so…
I'm not sure how much I should be going over this, or people want to review back, but I can briefly just pass over this. Like, a workflow is the beginning…
say, in Landgraph, it could be the… the main…
chain, which is in the beginning, so that starts with a workflow. Crewe AI is where a crew is there, and we kick off a crew that can be turned as a workflow. Or in OpenAI agents, like, it's the start of a trace. So that's the beginning of it. So everything under it, like the orchestrating of the agents.
through a predefined code path, right? That's what we define, like, a predefined path for the agents to work with each other. That's under a workflow. So that… that is what we have introduced in here.
Liudmila Molkova 00:15:41 A quick question, if, let's say, I use OpenAI agents, it's just because I'm mostly familiar with it,
The start of an operation, the agentic operation, would be invoke agent span.
And it also starts a workflow. What… how would…
the instrumentation know which is which, and would it be able to distinguish the workflow from just arbitrary invoke agent?
Ridhima Satam 00:16:08 I think, the start is always the start of a trace, right?
Liudmila Molkova 00:16:12 No. The trace starts wherever it starts. The…
instrumentation would start a span. It can be a root, it doesn't have to be, but essentially.
What… how would it create a workflow span or invoke agent span?
Ridhima Satam 00:16:31 Okay, so that differentiation we have to… we always, think… thought that, like, it's going to start the trace, but that's a good point to note, like, if… if just directly agent is starting. So, we were actually looking at when we are going to instrument and start the trace, that time we can create this workflow in that cases.
Alex Hall 00:16:56 A different way of putting this is, what is the difference between workflow and invoke agent?
Ridhima Satam 00:17:01 So, so here, like, if you see in here, like, I have other example mentioned in here, let me see.
So, an invoke agent comes in later, like, for example, if you're taking a land graph or a Creo AI, so I was going to come at this step where a task is actually getting executed.
Or, there is a fallback type. We have introduced this step span, where the agent is actually working on that task.
So that comes in later. So workflow… workflow is, like, the beginning, a very beginning of it, like, in the Creo, it's a kickoff, like, in the very beginning of it, and in line graph, it's the start of the first chain, and the intermediate chains could be this step.
And then the… then the agent invocation follows.
Alex Hall 00:17:53 Does that make sense when there's only one agent?
Ridhima Satam 00:17:56 Sorry, what?
Alex Hall 00:17:58 Does it make sense to use a workflow when there's only one agent?
Ridhima Satam 00:18:02 Could be,
But with the multiple, agents, it… you get a… you get all to… you get to see complete picture of all the agents working under the workflow. That's the addition that we have there.
Alex Hall 00:18:18 What does it mean in this example to have… the second ChatGPT4, the one that is under step research step, but not under an agent? What does it mean…
To have, like, a chat span that isn't part of an agent.
Ridhima Satam 00:18:33 In here.
Alex Hall 00:18:34 Yeah, I'm trying to imagine how this would happen, but you get one that is not part of an agent.
In the occasion.
Ridhima Satam 00:18:45 Yeah, maybe this is… this is just a typo, I think. Yeah, we haven't already… we always have tried it under that agent.
But I think, let me recollect. We have certain, like, in Landgraph, I remember that you don't have to use an agent, like, it could be, like, a chain.
And in that chain invocation, we have the LLM invocations. Like, there could be a tool or a chain. In that particular instance, we didn't use agent.
That's one example I can recollect.
Yep.
Liudmila Molkova 00:19:23 See, if I can summarize, then there is, if we think about, let's say, OpenAI Agent, there is actually no layer, like, workflow, because it's Invoke Agent all the time, but some frameworks
Creole AI, you mentioned, blank chain, blank gravity, would have some… some extra layer that can be broken down into steps.
Alex Hall 00:19:45 Doesn't it actually make sense to say that OpenAI Agents is not just InVogue Agent, because you actually hand over between
Agents.
Liudmila Molkova 00:19:57 Could you say that?
Alex Hall 00:19:59 Do they have a special.
Liudmila Molkova 00:20:00 API for this.
Alex Hall 00:20:02 There's a special concept of handoff.
Liudmila Molkova 00:20:05 Mmm.
Alex Hall 00:20:06 So you can have multiple agents.
within the city.
Liudmila Molkova 00:20:11 And off is the between invoke agents, right?
Alex Hall 00:20:15 Right, but it does… it does seem like it makes sense, too.
Wrap all of that into one workflow.
I don't know about the steps part, but…
anksing 00:20:24 Excellent.
Liudmila Molkova 00:20:25 That makes sense, maybe, but can you?
Alex Hall 00:20:28 Right?
Liudmila Molkova 00:20:29 Do you know? How much do you know? How complicated instrumentation could be?
Okay, also, Aaron is saying that there is a…
For Google ADK, there is always a retagent.
That wraps the orchestration.
Aaron Abbott 00:20:53 Yeah, I think, Ankit, you wanna jump in?
anksing 00:20:58 Yeah, so I think, workflow definitely sounds like a multi-agent orchestration?
You have to, like, have an analogy, and I know, like, with OpenAI agents as well, you can have, like, agents as too, like, you can have, like, an agent, have access to other agents, which also kind of forms a workflow, but it doesn't say that.
And I think that's what Alex also was mentioning about, like, one agent can hand off to another agent.
Which can hand off to another agent, right? But, OpenAI agents does not use that, like, term of being called a workflow, but in a way, it does form that, where multi-agents work together.
Liudmila Molkova 00:21:45 Okay, so should we think about workflow as the orchestration layer, essentially?
anksing 00:21:51 At least in my opinion, like, some sort of way to kind of work with multi-agencies.
Together, right? An agent calling another agent.
Having access to call multiple agents, right?
Something along those lines, definitely.
Ridhima Satam 00:22:11 Okay, so… Okay, so these are the attributes we have added for the workflow.
And… yeah, if people are okay with the workflow, I can just talk about the span, so…
Liudmila Molkova 00:22:26 Oh, sorry, can we talk about the terminology still? Like, the moment we decide on the terminology, the moment it will be clear which attributes to expose.
So, wha- what…
is workflow… is it the terminology that… what is the terminology that's actually used in different SDKs, do we know?
Ridhima Satam 00:22:48 So in Creo AI, it's the…
crew, which kickoffs… kicks off the crew, there's an API for crew.kickoff.
So that's when we are going to initiate a workflow.
For line graph, it's the first chain we get, that's the beginning.
That's the term as a workflow.
OpenA agents, when we did, like, we thought, like, the first trace it starts with, that we can,
add it as a workflow. So…
So there is, like, these multiple agents working together, and we are going to start something for them, like, every… all of the agents together. It's the beginning of it, that is the terminology here, to orchestrate the multiple agents.
Liudmila Molkova 00:23:39 So if we call it orchestration, wouldn't it be more specific?
Ridhima Satam 00:23:46 We want to be more specific, are you saying?
Liudmila Molkova 00:23:50 It's a question, so if we call it workflow… It happens,
Some interesting discussions, so it can be anything.
So if we can be more specific, we should be.
Ridhima Satam 00:24:05 It could be, okay, it could be, like, orchestrating agents and steps, through a predefined code path, like, where the agents are actually working in predefined. They are not autonomous agents, but they have a predefined path.
I was going through an article by, Anthropic, and it was presented in the, the Conference of Data Science.
Where they are… they have added this terminology, and I can tag that maybe in this, proposal as well, that they have termed it as workflow, where multiple agents
are orchestrating, where the multiple agents orchestration has been done under workflow for different kinds of predefined code parts, like a routing, or something like that, like a parallel way of doing that.
Liudmila Molkova 00:25:01 Okay.
Can, can you please tag it? It would be great.
Ridhima Satam 00:25:05 Yeah, I'll add that. Yeah, so that's where we got the idea, like, we can…
yeah, add this orchestrating for a predefined code path, not the autonomous agents. I've added this in the document somewhere, that…
Tom?
Aaron Abbott 00:25:23 Boop.
Adk also… I put a link in the… in the doc, but it… they also call it a workflow.
But they wrap it in, like, an agent, so it's a workflow agent, and then there's, like, some specialization, so there's sequential, loop.
Parallel, etc.
Ridhima Satam 00:25:42 Yes, yeah.
Aaron Abbott 00:25:44 Yeah, Don, do you wanna… go ahead.
Don B 00:25:49 Yeah, in terms of the terminology, this was reminding me about some of the recent stuff around durable execution that's become more mainstream. It's like, you have potential data from various sources.
that could be used to manage state in service. So, it's like, could be temporal, could be DBOS, could be prefect, and I did drop a link to what I knew about what Pydanik is doing in terms of bringing this together in terms of solutions in their libraries, but I was wondering if
People have started to look at how to do this with telemetry data.
Liudmila Molkova 00:26:28 Yeah, there is a lot of in-between of different…
Workflows and, durable execution event preventing frameworks, I…
Personally, I'm a bit scared of boiling the ocean and trying to define something very generic, not tied to GenAI, because
like, I mean, workflow, if we call it just workflow, not GenA workflow, It would be crazy.
But I'm open to, this discussion.
Don B 00:27:02 Is there a broader workflow standard within the OpenTelemetry umbrella?
Liudmila Molkova 00:27:07 No.
Don B 00:27:08 Okay.
Liudmila Molkova 00:27:10 There are discussions.
Aaron Abbott 00:27:11 Yeah, wasn't it the CICD?
group. There was some discussion there.
Liudmila Molkova 00:27:18 There is some discussion there. Well, there is some discussion around modeling some of the CI-CD stuff as workflow.
What is in common between CICD workflow and GenAI workflow?
like, how much benefit does it make to build an obstruction that supports both? I don't know, I don't think there is anything in common.
Don B 00:27:49 So, one of the examples I like related to, temporal that,
you know, Pydantic AI did, like Samuel Colvin, was a deep research-type workflow, and so some of the times where it provides value is if you have a scenario, and you can map, sort of, how between, you know, solving it using different
frameworks, how they would be captured and potentially compared. So I think that's maybe where there's value.
But yeah, it is… Not a simple problem to solve, so… Go forward.
anksing 00:28:34 Oh, hi, one quick question. So, what extra information would be captured if we, say, defined something called generate workflow?
In addition to, like, what could have been captured if it was just, like, a… different, like, invoke agent.
plans being put together, right? So, I mean, if that can help us kind of help answer where we can go with that?
Kind of probably help answer, like, why we need this.
And how does it really help?
Overall.
Ridhima Satam 00:29:10 So what we have done is here, we have added this name, description, that's a simple one, but the framework we have added, and we are not putting this as a workflow framework, because we kind of briefly tried to introduce this attribute in here for
other purposes also, like, when we are making… when other frameworks are used, for LLM calls.
In that also, we can use this. So this, and then in addition to this, for a workflow, we have… we are also introducing the metric for it.
Sorry.
Liudmila Molkova 00:29:48 Can we stop there for a sec? So,
If we return back, assuming it's invoke agent.
the… First, the workflow name becomes agent name, the workflow description becomes agent description.
The GenAI framework, you should already have it as instrumentation scope attribute on every span.
If we should not add it as an extra attribute, it's already there. It should be set.
Ridhima Satam 00:30:21 So you're saying this shouldn't be on the workflow?
But it's… Yeah, good.
Liudmila Molkova 00:30:27 It's already everywhere, because this is the instrumentation scope name. When you create a tracer, you put your instrumentation library… oh, the instrumentation library name.
Yeah.
So, we will figure… we'll need to figure out how to put it, but if we introduce something like this, it should be on all spans.
Not just workflow spans.
Ridhima Satam 00:30:47 Yeah.
it could be on other spans as well, right? That's where I said, like, that's why we are not putting this as a workflow framework, but we want to introduce this for, say, inference span as well, or other.
Liudmila Molkova 00:31:00 Yeah.
Yeah, so, yeah, but getting back to the invoke agent, this could be Invoke Agent Span. And also, in some places, the ADK, the OpenAI, it will be Invoke Span, Invoke Agent Span.
That's what you're saying, that there is an outer workflow span.
That you care… about… of the… because of the metric, because you want the portal time, right? End-to-end time.
Ridhima Satam 00:31:37 Yeah.
Liudmila Molkova 00:31:40 And it's a good question on how to differentiate, how do you differentiate the span or the instrumentation point? How would it know that it should measure
The total duration.
Ridhima Satam 00:31:58 So, how it's going to differentiate total duration?
So, we have… Two different,
Durations here, like, for the workflow, and then the agent as well.
So we know… How much time is spent at the agent?
And then the complete workflow.
Liudmila Molkova 00:32:22 let's say you're instrumenting OpenAI Agent, or ADK.
Ridhima Satam 00:32:26 Okay.
Liudmila Molkova 00:32:27 This, invoke agent is the instrumentation point for both.
Can you differentiate? Can you know this is the author?
Thing, and not the inner.
Do you know when to measure which of those durations?
Ridhima Satam 00:32:49 I haven't tried ADK myself for this example, but I can try that and get back.
Wow.
Liudmila Molkova 00:32:57 Have you tried OpenAI agents?
Ridhima Satam 00:33:01 Openai, not directly the Asian part, yeah.
Not invoking the agent.
But I have tried an example where you start a trace, and then a span an agent.
Liudmila Molkova 00:33:15 Yeah, the trace is unrelated to Gen AI, it can start anywhere.
Ridhima Satam 00:33:21 Okay.
Yeah, that differentiation factor, then I have to figure out then.
But for the other purposes, like, for at least LAN chain, we know Langgraph, that's the first chain we differentiate, and there is an invocation, a separate callback for that.
Similar for the PUAI, that… those two examples we have, but we have to look into the other one then.
Pradeep Nair 00:33:53 I haven't, really used ADK, but looking at the chat, wouldn't that be the workflow agent? That is the… the specialized workflow agent in work agent call, which would… which would be, the outer workflow in this case?
Aaron Abbott 00:34:10 Yep, that's what we do right now.
Liudmila Molkova 00:34:15 The differentiation would be possible in most cases, and just we would need to describe it in some way.
So maybe the way to describe it is that if you… if you know, like, you should know.
And if you don't know, you just don't create an AI workflow duration metric.
Pradeep Nair 00:34:38 Yeah, I mean, like you said, in most cases, we should know, and if it's not known, then probably the workflow span doesn't exist, or the duration metric is not recorded.
Liudmila Molkova 00:35:03 Sorry, I'm just taking some notes, in the doc.
Can we talk about STEP?
Like, why is it necessary? How is it different from Invoke Edit?
Ridhima Satam 00:35:42 Yeah, so step is, like, mostly, so in Creo AI, there is something called a task, where you define a task, and that is given to an agent.
And we have mapped two terminologies here. One is that, and the other in Langraph, we saw that there could be an intermediate
step before invoking an agent, like an intermediate chains. So, that could be mapped as a
step, so that's a fallback type. So, you can always see, the… the… the flow is like this. An agent, invoke agent is… if it's a Creo AI, it's…
Taken some task, and it's working on it.
Or there could be an intermediate chain between when it's the land graph.
That, that is what we have just,
Added as a step in between.
Liudmila Molkova 00:36:39 So when I look into the screenshots you shared, it's pretty much the same as the invoke agent in terms of duration.
And there are, like, I don't know, 4 layers, that are of the same duration.
And people usually complain about the…
Costs and, duplication of this.
So do we have a good reason to have… or… Whoa.
Suri spends on top of the… Chat.
1.
Ridhima Satam 00:37:17 Yeah, so we have this, steps in… so this is the land graph example, the first one.
Where you see these steps between, in between.
And then…
Liudmila Molkova 00:37:30 I mean, does the step coordinator, invoke agent coordinator, and step model, these three spans represent the same period of time?
And I have some, intuition that they have the same information, pretty much.
Ridhima Satam 00:37:46 Yes, but if there is a…
Yeah, that could be possible, but
If there's any bottleneck in between, like, if there is, time spent more, then we know that, where the time is spent.
Liudmila Molkova 00:38:00 Can we measure just this time spent instead of measuring, like, creating the outer span? If there is an HTTP request in between database execution, tool call, they would appear as a spanse under
I don't know, invoke agent.
So, what's the difference between step coordinator and Invoke Agent Coordinator?
Ridhima Satam 00:38:23 Yeah, it was just part of the same task, as you see.
It was the intermediate… for this line graph, it was the intermediate chain, happening, chaining happening. Yeah.
And, but, but in cases of, say, Creo AI, and when we have STEP, it has the information about, what is the task about, what exactly the task was given to an agent, so…
Liudmila Molkova 00:38:51 It would also be available on the Invoke Agent, right?
Ridhima Satam 00:38:56 It can be available. Yeah, we can make it available on the invocation.
Aaron Abbott 00:39:02 In LaneGraph, like, does somebody choose the step name, or is it just coming from the inner invoke agent coordinator, for example? So, like, step coordinator versus invoke agent coordinator. Does the person configuring LaneGraph put both of those.
Ridhima Satam 00:39:18 That was Landgraf putting in.
Aaron Abbott 00:39:21 Yeah.
Ridhima Satam 00:39:36 Yeah, so mostly, the step would have, in Creo AI,
The information about the objective and the description above the task, which can also be added for the agent, but we were just trying to add a fallback type where we can show the spans there, specific spans.
Liudmila Molkova 00:40:04 If…
Ridhima Satam 00:40:05 Is the duplication of the information is the concern here, is what you're saying?
Liudmila Molkova 00:40:10 Yeah, the cost. The duplication cost.
Related to it.
Ridhima Satam 00:40:17 Thank you.
Aaron Abbott 00:40:23 Yeah, I'm also feeling like if the user only, like, configures… they say that there's a coordinator agent, they, you know, they say that there's, like, a…
I don't know, like, the top-level thing is called Travel Workflow or something like that, like.
The other stuff seems kind of, like, internals to LaneGraph, which maybe should just be, like, a LaneGraph-specific convention.
That… That kind of make sense?
Ridhima Satam 00:41:12 Are we… are we just completely… Do the step, or…
Aaron Abbott 00:41:18 Tay it?
Ridhima Satam 00:41:19 Are we completely, saying to remove the step, It's just the duplication of…
Aaron Abbott 00:41:38 I mean, yeah, I heard… I heard Ludmila's concern. I think it makes the trace a little bit clunky to look at, just because you have some kind of nested stuff.
I don't know.
I haven't thought about this as much as you, though, and…
I feel like maybe the thing we're getting at is that
We're trying to capture, like, the control flow execution.
Like, the agent internals, the orchestration internals, right?
Ridhima Satam 00:42:06 Right.
I have one of these parameters again in here, like,
We can see that which,
To other assigned agents to that task.
Liudmila Molkova 00:42:25 Can you have more than one agent assigned to a specific step?
Ridhima Satam 00:42:29 I have seen that in Creo AI, where you have…
Where we are mapping that step as a concept of task, where that task can be assigned to multiple agents.
Liudmila Molkova 00:42:42 Oh, then what is the difference between step and workflow? I'm sorry.
Ridhima Satam 00:42:48 Workflow is just, like, so, so there could be, say, 5 tasks, right? But out of that, like…
each task is assigned to a single agent, but there could be one of the tasks which can be assigned to two agents, right? But the workflow is at the top.
Where it's actually giving the complete picture, very intact.
everything together.
That was…
Liudmila Molkova 00:43:13 Yeah, so, like, essentially, if you're…
think about it, like, you never know what is the top layer. You can use workflow inside workflow.
Right?
Nothing stops you from building a workflow agent that's used by another workflow agent, and you don't necessarily know about it if it crosses service boundaries or something.
Ridhima Satam 00:43:52 Yeah, I mean, there was this instance where the crew AI has certain sub-workflows, like, there is flows, and you can add workflows under that workflow.
But that always starts with a flow, and we term that as a mean.
Workflow, and then the rest crews will fall under those.
So there could… it's not just, yeah, I mean, when you want to begin, it's a workflow, but you can have scenarios where then you have sub-workflows also.
Liudmila Molkova 00:44:28 Yeah.
And I see the need for the workflow.
I wonder how far we can go without introducing a step. Like, why do we need this span at all? What does it…
have that… that the invoke agent doesn't. The invoke agent would have the description, I mean, the instructions given to agent, the agent information,
the… if there are sub-agents, we can find ways to record them. We would record assigned agents in the same way under STEP and other workflow. Why would we record them differently?
Great.
So we can find means to record the same information under Invoke Agent.
Ridhima Satam 00:45:19 Okay.
Aaron Abbott 00:45:21 Yeah, I mean, if the… if, like, you had multiple assigned agents to a step.
And so, for example, you'd have a step span with
You know, say, like, 3 children agents, right?
that it's… Yes.
Ridhima Satam 00:45:39 It would be more shown off, like, a step, research step, and one agent working on it, and then it would be some same step, but some other agent working on it. So it won't come, I don't think it will come under just one step, and then there are three agents invoking it.
That's what I thought, like.
Liudmila Molkova 00:46:01 I think Alex raises a good point, maybe we should call time, I think there's some other…
Aaron Abbott 00:46:06 Agenda items.
Liudmila Molkova 00:46:09 Yeah, so just a quick summary on this. Let's polish the workflow.
And that's… Think twice if we need to step.
Ridhima Satam 00:46:19 Okay.
I think one more thing I want to add is, like, we have added these three new, durations, for that, for people to review, and then, we also added this context of agent in the existing metrics of the duration to add the agent.
So, yeah, just people can just review it on their own, that's all. There are two PRs here. One is for the new spans, and one is for the new metrics we want to introduce.
Great. Thank you, Sam.
Liudmila Molkova 00:46:53 Cool, thank you. Moving on, to Session A. So, we have two important topics, brought up by you. One for the session ID, and one for built-in tool support. I'm going to,
maybe, so we have 15 minutes.
So, Pradeep Pavan, can we take 7 of those for the session AD, and leave 7 for Anki?
Pradeep Nair 00:47:28 Sorry, you say that again?
Liudmila Molkova 00:47:30 Can we spend 7 minutes on the session ID? And we will leave 7 minutes for our kit.
Pradeep Nair 00:47:36 Yeah, sure.
We can make it quick, like, this is an existing, issue. Like, in the last seg, or not the last cycling, in the previous segs, like, the comment was to add, add some…
scenarios and examples. So basically, that is what we went ahead and did in this documentation. It is, it is, it is more… it is, it is quite a bit detailed, but basically,
it provides some, scenarios where, just relying on conversation ID, would not be enough, and why session ID, could help there. So, like, I think…
Liudmila Molkova 00:48:20 for the sake of time, can you please define what Session AD… what…
Can you list the scenarios, and can you define what session ID is? This is the key concern, I don't know what it is in terms of Gen AI.
Pradeep Nair 00:48:32 Yes, I have, actually added that also in the document, if you could open, that document real quick.
Liudmila Molkova 00:48:40 Can you present?
Pradeep Nair 00:48:42 Yeah, sure.
Liudmila Molkova 00:48:44 Or also, it would be nice if you can just, I don't know, paste the contents of this document.
Pradeep Nair 00:48:50 Oh, okay. I mean, it's, it's, it's, it's, like, quite detailed. I didn't want to, like, populate the comment session with it, but I'll try to, like, you know…
Liudmila Molkova 00:48:58 That's okay. You wouldn't break GitHub, at least they hope you do, you wouldn't.
Pradeep Nair 00:49:04 Can you see my screen?
Liudmila Molkova 00:49:08 Yep.
Pradeep Nair 00:49:09 Alright, so… basically, this is what we are, like…
Calling a session, like, it's… it's a period of activity, like.
Where, like, an agent or user, operates with the…
a similar context. It's not just, like, a login, user login session. It's… it's like…
Like, like, it's, it's a…
I'm not sure, like, how to explain this in a better way, but Pavan, you can chime in whenever you want.
So, like, it's more like a session of, like, related tasks and workflows under a shared context. That's what we are thinking of the session as.
Liudmila Molkova 00:50:00 So the session ID is defined in semantic conventions as something different, right? It's already defined, this attribute is defined.
If you think about a different attribute.
think about the prototyping it. What would… how would OpenAI instrumentation populate it, specifically? Or how would Langchain populate it, specifically?
Pavan 00:50:22 We actually have a couple of implementations in,
you know, AWS Bedrock, OpenAI agents, and ADK as well, which have the concept of sessions, that specifically, you know, tracks and manages, like, different conversation threads that happen either, within the user and a single agent, or, like, multiple agents. Again, like, if it…
The scenarios vary if the, the operations, you know, that is actually done is, like,
headless, you know, for instance, where they go ahead, go in the backend background and, you know, do some complex operation and come back. For all those instances, I think the existing conventions that we have, the conversation.id sort of
doesn't necessarily capture those details, which, mainly, you know, would be useful, for us to do so. So, like, we probably need another attribute that'll capture the whole, end-to-end, you know.
interaction of the user with a multi-agent, you know, like, sort of a system, so to speak, for a given query.
Liudmila Molkova 00:51:44 Presented the workflow we just talked about.
Pradeep Nair 00:51:51 I think session can also, like, span multiple workflows. Not sure if I have, like, I think that came up, and I think I might have added a…
Scenario about it.
Liudmila Molkova 00:52:09 So, who would assign session ID?
Where does it come from?
Initially.
Pavan 00:52:23 It will probably be the initial
agent that takes the request from the user to, like, serve it, like, in the instrumentation layer, I mean. It'll probably be done by the,
Yeah.
I don't know if that was the…
Liudmila Molkova 00:52:43 If we call it Workflow ID, and if it passes passed somehow, would it be the same?
And then the inner workflows can inherit it from parent workflows.
Pavan 00:53:00 Yeah, the workflow ID, like, you know, depending on the description that we probably have, I know, you know, like, we just sort of discussed workflow, concept in a bit more detail as well, but essentially, if that sort of tracks the, that
you know.
flow, so to speak, from the user to those different, agents, it could probably mean the same thing,
But I know, like, many different implementations have, sort of, been using session ID, and workflow probably means, like, you know, a bit,
Like, you know, they use workflow in a different context, but yeah.
Liudmila Molkova 00:53:46 So, my goal here is to…
Not to inv… to come up with new notions, unless they exist somewhere else.
And let's go through the document offline, and let's see. My intuition tells me that first workflow ID is the same as trace ID, at least in the way we describe it. We talked about workflows today.
And that, the session,
still should be tied to something concrete. Like, if you want to introduce it, we would need to explicitly document who will start it, how would nested things once started again, and why is it different from Trace ID, or further workflow.
And I'm super sorry about breaking, stopping here, but we need to move on to, ankit's topic.
Pradeep Nair 00:54:44 Sure, yeah. Let me know if, like, you need some more, details in the documentation, but,
I think some of the questions are, answered in this, document, so, if, like, you could review it offline, it would be great.
Thank you.
Liudmila Molkova 00:55:05 Thanks.
Ankit built-in tool support.
anksing 00:55:11 Do you want to present? Do you want me to present? Yeah, it would be great if you could open it, my…
Lapto's a little… I need to restart it. It's just dying sometimes. Bothering too much.
Liudmila Molkova 00:55:27 Okay, so can you talk about it?
anksing 00:55:30 Yeah, so, I think, one of the,
So, actually started with, like, I wanted to look at, like, if I can instrument responses API, and then one other gap that I found was, only, like, most of the other things were there, like function tools, built-in tools or something, which are… could not be represented by the existing GenAI Symmetic convention.
And I think I saw, I asked in one of the chat, and then I think,
Alex had pointed me to one of this open issue, which came out, so I just wanted to work on that. So, the idea here is to add support for the built-in tools. Right now, the only way you can represent a tool call is through tool call.
Request, which is very tailored to, kind of, client-side function calling.
To be honest. So, wanted to make it more extendable, where, and more polymorphic, where you can add support for more tools as needed. And if you want to have a very well-defined schema for the tool, so that you can show it in…
instrumentation UIs, for easier, view… viewing, so that could help as well.
So… And here, what I've done is I've made tool call request part and tool call response part polymorphic.
Where I've added another property called toolCall, and…
Which is a polymorphic field, where… and I've shown an example of…
code interpreter here. I can add more examples as needed, and I think I updated some of the existing examples, which were using function tools.
As well, and shows how this, polymorphic property kind of captures both function tools, And code interpreter.
Which is a built-in tool.
Liudmila Molkova 00:57:33 So one thing, thanks for this, you updated the schemas, but you didn't update the Python code that we have. Could you please update it?
anksing 00:57:42 Oh, yes, I'll do that. Let me add a comment on the PR radar now, so that I don't miss it.
Liudmila Molkova 00:57:51 I can add a comment.
anksing 00:57:53 Thank you, appreciate that. We'll do that, that'll be great.
Aaron Abbott 00:57:58 Anka, could you summarize, like, the open comment threads on this PR?
anksing 00:58:03 Yeah, so one of them was, I think, initial one. I tried to see if I could use the initial, like, tool call response, or tool call request part for all the tools, but I think it gets a little bit clunky, where everything is kind of a JSON, and then you have to kind of, as a user, make sense of it.
Which I feel is definitely not a great experience when you're looking at the telemetry.
And I think I just looked at Dylan's comment as well, where he mentioned that if we can have an any, which can be a catch-all,
Until, like, we know, like, if there are some unknown tools, that make sense to me. However, actually, I need to update this comment as well, Limila. I think I went with slightly different approach.
That's fine. Yeah, I'll agree with that. And,
And I think, the other part which Dylan mentioned was, like, in Gemini 6 or 7, there is no tool called request part.
And only the tool call names show up for built-in tools, if I read it correctly.
So, that seemed like more like…
If you don't have the information about what parameters were passed when the tools were called, that could probably be optional if you don't have them, or if the provider does not capture them, but you could still capture what tools were called, right?
Alex Hall 00:59:32 It feels like you're trying to define, like, a generic code interpreter tool.
but I'm pretty sure that…
it differs significantly between, for example, Google and OpenAI, what the data actually looks like.
you seem to have gone for the OpenAI.
anksing 00:59:49 Yeah, right now, I think I've, yeah, I've picked up the schema from, like, the OpenAI, agreed.
Do you think it would be beneficial to have, like, if, say, they are not able to converge, like, if we are not able to come up with a genetic schema which supports
Which can represent both, to also have, like, provider-specific definition of tools.
Alex Hall 01:00:13 I think having a generic thing is valuable. It's not necessary to have it, but right now, it's like, it looks like a generic thing, but actually it's provider-specific.
anksing 01:00:24 Hmm, oh, I see, I see. Got it.
Alex Hall 01:00:28 Definitely easier to move forward on this if we don't actually try to…
Define everything genetic yet, we just have…
A way of including the data.
anksing 01:00:41 For all of the providers and all of their various built-in tools.
God, okay.
Liudmila Molkova 01:00:47 But you're saying, Alex, that this is a discriminator, and the content under the corresponding tool call request is arbitrary, it's any.
Alex Hall 01:01:00 I mean, I don't even know if we need the discriminator. The way that I envisioned it was just…
roughly the same as the usual tool call request and response, but maybe something like a Boolean to say this is a built-in tool, just so that it's distinguished from
A function… a local function tool which happens to have the same… the name code interpreter, or whatever.
anksing 01:01:26 So if, say, that happens, or if you go that route, then,
we don't really would know the schema of both the tool call and the tool response, right? Like, what it has. And it could differ across different tools.
Right.
Alex Hall 01:01:42 I mean, I don't think that we can realistically define the schemas for all of the built-in tools that exist, and are going to exist.
We can have a few special cases, like, code interpreters are a common enough thing that we could define something for that, but for built-in tools in general.
I think it's more useful that we just have a super generic, flexible, type anything.
Which…
Just tells us what to do in that case, because right now we haven't really decided what to do at all.
anksing 01:02:14 So, if the provider wants to…
Give a specific, like, a well-known definition, would that still be an option?
Like, so for example, OpenAI is a provider, or…
Gemini as a provider are…
Alex Hall 01:02:29 Yes, I think that that makes sense.
sense, and then I guess in that case, you would want to discriminate her?
anksing 01:02:38 Yeah, discriminator for, like, at least the tool name, yeah, tool identifier, and also provider, in a way.
To some extent, yeah.
Liudmila Molkova 01:02:48 Oh, we have discriminator for provider in the GenAI system name, or Gen AI provider name. But we… yeah. Anyway, you, you folks, I think you should maybe chat more and.
anksing 01:03:00 The PR. Rocket piano.
Liudmila Molkova 01:03:02 Yeah, sorry, Erin, I… you had your hand raised.
Aaron Abbott 01:03:05 No worries, it'd probably be better if I just left a comment.
anksing 01:03:09 Awesome.
Aaron Abbott 01:03:10 Thank you. Okay.
Liudmila Molkova 01:03:11 Cool, thanks a lot, see you next week.
anksing 01:03:14 Cool, thank you.
Aaron Abbott 01:03:15 Later.
anksing 01:03:16 Bye.

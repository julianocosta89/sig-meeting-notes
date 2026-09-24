SIG: GenAI Semantic Conventions and Instrumentation Stability
Date: 2026-09-23
Duration: 30 minutes
============================================================

## Zoom Recording Transcript

**Trask Stalnaker (Microsoft Corporation)** 00:30 Hey, Aaron…
**Aaron Abbott (Google LLC)** 00:31 Y.
How's it going?
**Trask Stalnaker (Microsoft Corporation)** 00:37 Pretty good. How about you?
**Aaron Abbott (Google LLC)** 00:41 Yeah. Good.
Oops.
**Trask Stalnaker (Microsoft Corporation)** 02:10 Missed one person here. Smyak.
Hello, everyone.
**Siri Varma** 02:25 Hello.
**Trask Stalnaker (Microsoft Corporation)** 02:29 Yeah, let's get started.
So… Why don't we just kind of use this as our meeting guide?
We're gonna just go top to bottom, and so… I'll just ask if there's anything you want to discuss.
Note about the section.
And we'll go from there.
Parts, JSON, schema, Aaron and Neil, anything that you want to chat about?
**Aaron Abbott (Google LLC)** 03:13 No, not right now for me. I think we talked a lot about it, in the regular call yesterday.
**Neil Yashinsky** 03:21 Yeah, same. I feel like, we've… we're, whatever, in a position to do a lot of good things, but, you know, given the cadence, none of them have… are not fully materialized yet.
**Trask Stalnaker (Microsoft Corporation)** 03:34 Cool.
**Neil Yashinsky** 03:37 You vicious taskmaster, you… yeah.
**Trask Stalnaker (Microsoft Corporation)** 03:39 I am, I'm gonna be.
**Neil Yashinsky** 03:40 Yeah. No, I appreciate that. That's, like, the best thing about this, is we're, like.
there's not a lot of pressure, but yeah, people, I think, are working at a diligent pace.
To the extent of volunteer process can… can…
**Trask Stalnaker (Microsoft Corporation)** 03:54 Alright, moving on, Content capture. I know, Dylan, you said you were busy with some other stuff right now, this week.
Anything you want to discuss here?
**Aaron Abbott (Google LLC)** 04:14 Looks like he's… Oh.
I think he literally just joined, if you want to ask that again.
**Dylan Russell** 04:20 Sorry.
**Trask Stalnaker (Microsoft Corporation)** 04:20 Still at 8.
**Dylan Russell** 04:22 Yeah.
**Trask Stalnaker (Microsoft Corporation)** 04:23 Anything, I know you said you were Busy with some other stuff this week, but just wanted to check if there was anything you wanted to discuss about content capture.
**Dylan Russell** 04:34 No, I haven't… Really looked into anything or done anything yet.
But… Yeah, I will… I will read through these bugs and see.
What the deal is.
**Trask Stalnaker (Microsoft Corporation)** 04:57 Cool. Let's see, for the naming, so it… just… I took, Ludmila's PR… And, Just updated a couple of small things, and it is ready for review now.
This is sort of the first one. It unlocks, all of these Renames, or splitting out, rather, the single… Operation span and operation metric into All of these… More specific spans and metrics.
So… Definitely, you know, take a look at this in the context the bigger… picture here.
And, once we have agreement and merge this one, then I suspect all the… all of the rest of these will pretty much just be mechanically following the same pattern.
**Siri Varma** 06:12 Hey, Trask, would we need… would this need any changes in Python GenAI repo as well? Like, are there some implementations there, too?
Okay.
**Trask Stalnaker (Microsoft Corporation)** 06:22 Yeah, definitely. The… so the span type.
Right, we don't have span type yet, although we do have an OTEP to introduce that formally.
So on the spans themselves.
I'm not sure if that is gonna affect the instrumentations, but definitely the metric split out will.
**Siri Varma** 06:47 Okay.
**Trask Stalnaker (Microsoft Corporation)** 07:01 Yeah, and then the final will be, once all of the rename… all the split-outs are done, then there'll be a final PR to deprecate the odd… metric.
itself, and I guess deprecating the old span… Type…
**Felix Becker (Anthropic)** 07:26 Sorry, I'm not quite following. What is the current name attribute not afford that would be, like, solved by padding a new attribute?
**Trask Stalnaker (Microsoft Corporation)** 07:40 Not an attribute, but, splitting out the metric.
So… Right now, we have, in the YAML file, we have one… span called GenAI.Client.operation.
And it encompasses all of these.
Operations.
Which, one of the, One of the downsides there is that We kind of just… Have to put all the relevant attributes for all of them onto this one YAML span.
Versus, by splitting them out, we'll be able to scope the attribute list accordingly to that Specific kind of spam?
And then, on the metric side.
Instead of having a single client operation duration for all of them, we will have Many different separate metrics.
Or was your question, why can't we just have an operation the single metric with the… A discriminator.
**Felix Becker (Anthropic)** 08:59 I'm maybe lacking a bit on, like, the metrics stuff. I haven't really dove into that yet. I was just wondering, like, if we need more values For operation.name, why we wouldn't just add more values there.
**Trask Stalnaker (Microsoft Corporation)** 09:17 We will. so this is a little bit related to that… the discussion we were having yesterday around finish, reason, Our operation name is… this list… of I don't think it's an enum.
Although, I could be wrong there. But then we have a span type, which… Is sort of this set of them.
**Felix Becker (Anthropic)** 09:51 The spend type is not exposed, right? Like, that's just a spec concept.
**Trask Stalnaker (Microsoft Corporation)** 09:56 Today, it is not exposed, but… There is a OTEP that just got merged recently.
to expose span type over OTLP.
Because it's been an ongoing problem, and… with, like.
we've interpreted, even, like, for HTTP spans, database spans, the way that you know something is an HTTP span is if it has an attribute… one of the required attributes on the HTTP So it's been a very… preferred…
**Felix Becker (Anthropic)** 10:41 Yeah, so this is, like, a more general OpenTelemetry, like.
self-reported schema off all the attributes on the span.
**Trask Stalnaker (Microsoft Corporation)** 10:51 Yeah, yeah.
**Felix Becker (Anthropic)** 10:52 fact that now I'm getting that.
**Trask Stalnaker (Microsoft Corporation)** 10:54 And it's…
**Felix Becker (Anthropic)** 10:56 Oh, on using that.
**Trask Stalnaker (Microsoft Corporation)** 10:59 Yeah, so the Semantic Inventions has had that span type for a while, because we've needed it internally, but it hasn't been exposed. Like, it's just been part of our YAML structure.
**Felix Becker (Anthropic)** 11:14 Right.
**Trask Stalnaker (Microsoft Corporation)** 11:18 We're… we… as we did the… started building out conformance stuff, like, we really ran into problems there.
Which… we were able to then successfully argue that we need this in the general OTLP schema.
Cool. Moving on, in France.
More, I think we're… Holding on this work.
for the parts JSON… schema work… How about, agent workflow model? Surya?
Anything you want to… raise here…
**Surya Teja** 12:17 Oh, nothing much to ask. So, I'm working on to see if I can merge both the invoke agent and invoke workflow span.
And right now, I'm seeing what attributes that we can preserve, and what can… we can remove. And there is another PR for nested agents, and we have something to identify the main agent. If that is merged.
It is going to help us create more clarity around how to nest agents from… When there is a hierarchy, That's only the blocker from there.
There is one more other thing around turns and stuff. Sorry.
**Trask Stalnaker (Microsoft Corporation)** 13:01 plus one…
**Surya Teja** 13:02 Yeah.
**Trask Stalnaker (Microsoft Corporation)** 13:07 And how… how does this one help the… if you could draw that connection for me, of how this helps the workflow?
**Surya Teja** 13:15 Yeah, so… say, imagine a scenario where you have a workflow.
And that workflow is calling an internal agent. So, with the new span type, where we are merging both invoke agent and invoke workflow.
they, under the workflow, it summons an agent, and that agent in turn summons another agent. So, sub-agent spawning other sub-agent. So, in order to establish a proper hierarchy between these two agents under the spam, the main agent name, attribute is going to help us. The top agent that is calling or summoning the, trailed agent.
They… we can use parental hierarchy and stuff of that kind.
But… Since the proposal is to use an attribute, I am sticking with this.
**Trask Stalnaker (Microsoft Corporation)** 14:14 Got it. Thanks.
**Surya Teja** 14:20 Yeah, I can take this forward and… work with, make this… Work on this draft and push, changes and… Work with you or others to get this pushed first.
**Trask Stalnaker (Microsoft Corporation)** 14:37 Cool, sounds good. I was just looking at this today, Aaron, related to your… the entity… Pr… Of yours.
**Aaron Abbott (Google LLC)** 14:48 Yeah.
I can't remember. Yeah, go ahead, go ahead.
**Siri Varma** 14:58 I think I had one question to Surya. So, the one I was also looking at had Invoke Agent.
I just wanted to understand, as part of this, we are not removing it, right?
**Surya Teja** 15:10 Because we are not… Okay. No, no, we are not removing it. Okay. The proposal is, invoke agent and invoke workflow.
are, duplicate… duplicative in nature. They're not entirely duplicative, but somewhat duplicative. For that reason, we can merge both spans and, Work on evolving a common set of span attributes.
And we are going to use an attribute which is, we have operation name.
for identifying whether a workflow is being invoked, or whether an agent is being invoked. So… now we are going to have only one span, but operation name is going to define what the workset is, whether a workflow is being invoked, or whether an agent is being invoked. I think I'm repeating myself, but the core crux of it is Bespan.
**Siri Varma** 16:13 Okay, so does that mean, when we say merging agent and workflow, the span name might also change? Like, invoke…
**Surya Teja** 16:22 Yeah, Invoke Agent, currently I'm leaning… leaning towards having the name as, I'm not sure what name I want to use for that one. Need to think about names. But, Currently, I'm thinking of Invoke Agent as the name for that, or something.
**Siri Varma** 16:42 Okay, yeah, so the reason I was asking was the work I am doing here. So, there is Invoke Agent Client and Invoke Agent internal spans.
**Surya Teja** 16:51 Yeah.
**Siri Varma** 16:53 Now, the client is for anything that is happening on the network call, and internal is something that the agent service itself is doing.
So, what I'm trying to understand is, will this have any impact on that?
**Surya Teja** 17:08 Possibly it's going to have an impact.
And the impact is, when we are naming the operation.
It would be Invoke Agent Local, or invoke agent Client… sorry.
to identify if… the agent that's being invoked is over the HTTP call, or is the agent that is being invoked is, in the local listing, so… Is this making sense to you?
**Siri Varma** 17:39 So today, there is already that specification where Invoke Agent Client is the one that is making network call, and Invoke Agent internal is the one that is, that the agent service is doing. So today, that is already there.
What we were doing was making it more explicit by updating the documentation, stating that, hey, this is what this means, this is what this means.
So… Does that mean, we pause on that, and we first… Would we have to sync up and understand what the change is here, and then move forward there, or…
**Surya Teja** 18:18 Not as water. Yeah.
Yeah, that's what I think, Siri, because, our work is going to… clash with each other. Yeah. So it's better that we work together and understanding how we can evolve this. And after we have a common path, we can, you know, divide, and we can see how we can Encompass that work in this one.
**Siri Varma** 18:43 Okay, so then I can set up a separate sync between us, Surya. Let me know how to reach out, I can reach out on Slack, or something.
**Surya Teja** 18:51 Yeah, I'm on Slack City.
**Siri Varma** 18:53 Okay, yeah, I'll re-shot you on Slack.
**Surya Teja** 18:56 Yeah, sure.
**Siri Varma** 18:59 Thank you.
**Surya Teja** 18:59 Thanks.
**Trask Stalnaker (Microsoft Corporation)** 19:04 Yeah, and, as part of this, like, If you can help answer the question of how we… What is a workflow, like, I think part of the reason we were thinking of merging these is that they seem to be… they're very… seem to be similar, and… Or at least there's a lot of merging… At least colloquially, people talk about everything as agents, these workflows.
Yeah.
So, we're trying to see if there's… if there's benefit to modeling it separately as workflows, or if there's some kind of indicator attribute on the invoke agent, whether it's useful to capture that it is.
a… Workflow… I don't know, there was just a lot of, kind of, confusion around what the workflows… meant, specifically.
If I'm remembering.
**Surya Teja** 20:17 Yeah, for the workflows, from what I understand, It's more or less, 3 or 4 units of work that are defined as one single step.
So… An example is, you have 3 agent calls that are coming under one workflow.
They're doing 3 different units of work, but ultimately, they're giving 1 result.
To give you an example, you want to book a flight, And, you want to… work with the agent. So that agent is going to call a workflow, which is going to check for all the available flights, and then call a Stripe or something to place, order for you. And then finally.
Another agent is going to take all these details and give you a summary of What flight was booked?
when you have to leave, and what was the cost of the whole journey. So, 3 agents are acting together to do one defined set of work, work.
For you. So that's the workflow definition.
From my perspective.
**Trask Stalnaker (Microsoft Corporation)** 21:30 Okay, and today we would capture that as invoke workflow with those three, sort of.
**Surya Teja** 21:36 Yeah.
**Trask Stalnaker (Microsoft Corporation)** 21:37 Agents that is calling under it somehow.
Yeah. The question is… Is it… is that a… Useful distinction, or distinction we… find useful.
Of calling that a invoke workflow versus calling it just an invoke agent internal.
**Surya Teja** 21:55 Yeah.
ES Trask. So, if, I can give you one more example. In Llama Index, there is a function workflow.
the name function workflow. Over there, what, agent workflow, sorry, the name is Agent Workflow. What you do is you define 3 or 4 agents, and you organize the work of the agents sequentially or hierarchically, and whenever you do… you want to do something, for that specific workset, you're going to call this agent workflow. And this agent workflow is going to spawn the sub-agents.
Do that unit of work, and written back the result to you.
It's like a main thread coordinating subthreads for you.
**Siri Varma** 22:41 I think the more I think about it, it is like… in one invoke workflow, we'll have multiple Invoke agents.
**Surya Teja** 22:49 Yep, yeah.
**Siri Varma** 22:51 So, invoke Workflow is a parent, and invoke agent… if there are 3 or 4 agents, every… each agent will emit its own.
Invoke agent.
Thanks, Fred.
**Trask Stalnaker (Microsoft Corporation)** 23:01 I think that's how it's modeled today in the Semantic Convention, and this proposal… Or at least the… the question is, do we need Invoke… should we just replace Invoke Workflow with Invoke Agent, that top-level one?
Given that… at least colloquially, people talk about it as, this is my agent. They don't say, this is my workflow that calls these agents. They say, this is my agent that calls these other agents.
**Siri Varma** 23:37 I see.
Okay.
**Surya Teja** 23:42 Yeah, and also a broader question to… I mean, I… if you have time, I can, broaden the conversation, otherwise I can… pick up next week, because I need some advice from Other folks do, on this one.
**Trask Stalnaker (Microsoft Corporation)** 23:59 I mean, I think what would help is if you could… I mean, right, this is still an open question of whether we should do it or not.
And… So, maybe just if you could sort of outline more, you know, take… What's been discussed here, and kind of try to synthesize it down to, like, a key… couple of key talking points that we can talk through.
**Surya Teja** 24:28 Yeah.
Sure, Trask, I can do that.
**Trask Stalnaker (Microsoft Corporation)** 24:39 Cool, moving on, Agent invocation span…
**Siri Varma** 24:44 Yeah, so this is… the 493 is basically the one I just discussed, where for the invoke agent, there is client and internal, and we want to make that explicit in the documentation.
So, this one, the current PO, I think I'll have to discuss with Surya more about this.
So, it'll depend on the path we take for the agent and workflow.
**Trask Stalnaker (Microsoft Corporation)** 25:12 I'm not sure. I think this one feels… it feels like we could move forward, right? This is mostly just a clarification of We already…
**Siri Varma** 25:25 That we already have, yeah. So, for that thing, the PR looks good, I will approve that. But, there is one more PR that Anget had, which was talking about Oh… So, if… the… so the invoke agent span is being emitted both from the client side and the service side. So, looks like… There is a little confusion on if there's a distinction between both of them.
And I think there is. Attributes are different, and then the one on the client side is called our client, and the one that is doing internal is called The one that is happening on the service side is called internal. I just clarified that on 308, and I'm waiting on… I'll talk to Ankit, and I'm waiting for his comment.
If that looks good, then we can close these booth.
**Trask Stalnaker (Microsoft Corporation)** 26:23 Okay.
**Siri Varma** 26:25 Yeah, so basically they both are different, so I just want to make sure that answers Ankit's question, and Rakuten… Okay.
**Trask Stalnaker (Microsoft Corporation)** 26:34 Perfect.
Alright.
Agent Identity…
**Wolfgang Therrien** 27:12 So, I started digging through this, and 243 looks like it's got 3 parts to it. 270, is approved, but has conflicts. It got an additional approval, Lutmila approved it. And then 447 has 2 approvals, but they're not from approvers.
And so those… look like it handles two-thirds of the use cases. And then I think the… by my read, the third use case Is the inter-process, agent to agent.
delegation, which I think is related to, sort of, like.
some… some outstanding naming questions that I'm… I'm still sort of trying to wrap my head around. That's as far as I got, but I think if we can get the, those conflicts resolved and get, like, an approver to go through and give 447 an overview, we might be able to get those to, Moved forward.
**Trask Stalnaker (Microsoft Corporation)** 28:15 Cool, can you, I mean, when you… can you review and approve them?
Sort of first as, like, okay, this is… this looks good, and then we will… I'm happy to… Bug folks, including myself, to…
**Wolfgang Therrien** 28:34 Will do.
**Trask Stalnaker (Microsoft Corporation)** 28:35 further reviews.
And Aaron, yeah, let's… I think this one, my… I was looking at it, I'll ping you if I have any other questions about it.
**Aaron Abbott (Google LLC)** 28:54 Okay, sounds good.
**Trask Stalnaker (Microsoft Corporation)** 28:56 I was just trying to repage it into my brain.
Alright, we are running short on time, but this one we are, working on the parts stuff first.
Token usage, I don't have an… any update other than this. Did get merged.
And… for the errors… So… I think that we should split it out.
I double-checked, and the messaging SemComf already models it that way, of splitting out the exceptions per span type, essentially.
So I have a… created a tracking issue since it wasn't tracked. Well, it had been tracked in, sort of, Ludmilla's, PR before, so I kind of clarified that so that we can merge that PR address on… sorry, not that one, but… this one.
So that we can… Approve, merge that separately, and… address the exception split out, I think, all at once, at the end, Instead of dribbling them out one by one.
**Aaron Abbott (Google LLC)** 30:16 Basky, is this event, like, a specialization of the general exception?
event in hotel, is that the kind of idea there.
**Trask Stalnaker (Microsoft Corporation)** 30:24 Yes, although we haven't modeled it in semantic mentions as a specialization… as a refinement.
**Aaron Abbott (Google LLC)** 30:33 Yeah.
**Trask Stalnaker (Microsoft Corporation)** 30:34 But yeah, it's replacing the, span event exceptions that never were spec, never… we never had semantic conventions around them.
**Aaron Abbott (Google LLC)** 30:45 Cool.
**Trask Stalnaker (Microsoft Corporation)** 30:47 Alright, thanks, Saul.
**Siri Varma** 30:49 Thank you.
**Aaron Abbott (Google LLC)** 30:51 internet.
**Neil Yashinsky** 30:52 Bye.

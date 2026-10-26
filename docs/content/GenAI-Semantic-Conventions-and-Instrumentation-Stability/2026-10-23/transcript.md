SIG: GenAI Semantic Conventions and Instrumentation Stability
Date: 2026-10-23
Duration: 30 minutes
============================================================

## Zoom Recording Transcript

**Surya Teja** 00:28 Hey, hi, folks.
**Max Ind (Google LLC)** 00:30 Hello?
**Liudmila Molkova** 00:36 Hello.
**Trask Stalnaker (Microsoft Corporation)** 01:09 Happy Friday, folks!
**Liudmila Molkova** 01:12 Happy Friday!
**Max Ind (Google LLC)** 01:15 Hey, happy Friday!
**Liudmila Molkova** 01:33 I'll just Trask for a second.
**Trask Stalnaker (Microsoft Corporation)** 01:37 I can drive.
**Liudmila Molkova** 01:38 Thank you.
**Trask Stalnaker (Microsoft Corporation)** 02:04 And a good one to copy from.
Let's see… Anything… Anyone wants to get on the agenda specifically today?
Probably follow up on… Wednesday's discussion… Max…
**Max Ind (Google LLC)** 03:07 Yes, so I have… I attempted to do a A relatively objective way to score which term is better.
So I got… I linked a… GitHub pages link? I think I linked it.
The right spot, yeah.
Oh, dear. Yeah, yes, yes.
**Trask Stalnaker (Microsoft Corporation)** 03:33 I love this.
**Max Ind (Google LLC)** 03:37 Yeah, so there are… so what I did was I… Asked an agent to look at all the 11 docs, Which, I think, originally, Ludmilu… Scoured for, for names.
I tried to have the… Properties of an agent and a workflow.
Which, most of these docs outline.
then I have, you know, the… which properties belong to what, so some of them belongs to agent only, some of them belong to workflow only. Four of them overlap.
And then I have scoring rules right at the top, which is, like, basically a term. If it shares the properties with an agent in a workflow, it's a better term, and if it doesn't share properties within Agent and the workflow, it's… a worse of a term. And basically, the winner of this process is the agent.
So, is… So, I think, you know, if we wanna go… with the agent, I'm fine with it. I think that what this demonstrates is that agent produces some awkwardness, but at least awkwardness of all of the candidates. Alternatively, if you wanted to exclude agent and workflow from the racing, because we think that it, like.
You know, my methodology, kinda, no agent.
And workflows largely overlap, so both of their… these terms.
Are bound to be good fits.
If we want to exclude that, and we want to exclude the multi-agent system, because that's way too long, then the flow is the best, second place candidate.
That's the…
**Trask Stalnaker (Microsoft Corporation)** 05:41 Below this one.
**Max Ind (Google LLC)** 05:43 Yeah, yeah, it's like… So… Most of the terms are not good.
And even those that are good, it are barely, are barely in the positives, yeah.
**Trask Stalnaker (Microsoft Corporation)** 05:56 Okay, so this… I see, so this is agent… what… what does ref mean?
**Max Ind (Google LLC)** 06:03 That's a great question. Actually, you can scroll lower down, and there's, like, a… Just, like, a more comprehensive, like, a better… If you click through these, like, I think rifle just means, like, like the… I think the agent that I asked to compile this thought that, like, yeah, it doesn't make sense to call this an agent or a workflow, but I didn't expect the agent to come out so highly.
we can exclude them, or we can include them, we… yeah. If you click at the… respective terms, like, lower down in this, like, scorper noun definitions, then you get, like, what each source has to say about this. Like, which properties… Ehh… So, so if a term is outlined in a given source.
And it has properties, this outlines, basically, like, where this color comes from.
**Trask Stalnaker (Microsoft Corporation)** 07:11 Those are great.
**Max Ind (Google LLC)** 07:14 Thanks.
**Trask Stalnaker (Microsoft Corporation)** 07:18 Alright, so, tentatively, we proceed with agent.
**Max Ind (Google LLC)** 07:24 I think so, I think that… I think it's okay, yeah.
**Trask Stalnaker (Microsoft Corporation)** 07:25 Alright.
Cool, send the PR.
**Max Ind (Google LLC)** 07:29 Yes, I am.
I'll book it, I'm…
**Trask Stalnaker (Microsoft Corporation)** 07:31 I'm curious to… I'll poke around on this a little bit, because I love this idea of… because we get into these quandaries, right? Like, I love this idea of some kind of, scoring… Yeah, not us, just whatever makes sense in our heads.
**Max Ind (Google LLC)** 07:53 Yeah, and there's gonna be, just heads up, there's gonna be some awkward naming, so, like, so basically, like, agent name.
There's gonna be, like, when… the invoke agent span represents a workflow invocation, then the agent name can hold the workflow name. I think that's, like, there's gonna be some awkwardness, but that's… that's, you know, a relatively small issue, yeah.
**Trask Stalnaker (Microsoft Corporation)** 08:22 Cool! Thank you.
Nice job.
**Max Ind (Google LLC)** 08:25 Thanks. Thanks.
**Liudmila Molkova** 08:27 final ultimate bike shed is whether it's going to be Invoke Agent or Agent Invocation.
**Max Ind (Google LLC)** 08:35 Oh.
I'm for Invocation, just to keep the stuff.
That works, currently working.
**Trask Stalnaker (Microsoft Corporation)** 08:49 Was, I hadn't thought about it at all, those two options.
**Liudmila Molkova** 08:56 Maybe let's not. If it doesn't hurt your eyes to see inference and embeddings and invoke agent, then… Let's not… I can live with this.
**Trask Stalnaker (Microsoft Corporation)** 09:10 Yeah, go ahead and send the PR with Invoke Agent, Max, and then, yeah, we can, if that… If we think… Anything about that, we can… That would be a easy last change.
**Max Ind (Google LLC)** 09:26 Will do.
Probably Monday, yeah.
**Trask Stalnaker (Microsoft Corporation)** 09:32 Yeah, Mikola.
**Mikolaj Knap (Google LLC)** 09:33 Okay, so I was gonna ask, if we're merging invoke workflow and the invoke agent span under one span type, does that mean that we have to do the same thing with the metrics? So, like, the duration metric from invoke Workflow, and then the invoke agent is going to be merged into invoke agent only?
Okay, and then, if a consumer asks, like, I want to get the duration of my workflow. Do we just redirect them to… using the invoke agent metric? Won't that be confusing, or…
**Liudmila Molkova** 10:09 Filter, invoke agent metric by your workflow name.
In the Agent name.
**Mikolaj Knap (Google LLC)** 10:17 Okay, I see. So you would just tell the consumer to set the Agent name to be the workflow name, basically.
Okay.
**Trask Stalnaker (Microsoft Corporation)** 10:24 And we'll have the agent operation.
Name will be workflow.
**Mikolaj Knap (Google LLC)** 10:34 HR operation now, we are on the metric.
**Trask Stalnaker (Microsoft Corporation)** 10:37 Yeah.
**Mikolaj Knap (Google LLC)** 10:38 Okay, cool. That makes sense.
**Trask Stalnaker (Microsoft Corporation)** 10:41 Yeah, so, because we are coalescing these, but then we… that operation name will be sort of… what?
allows people to use… I mean, they could… frameworks might use Turn, they might use… What were some other things?
**Liudmila Molkova** 11:02 run task… Hello.
**Mikolaj Knap (Google LLC)** 11:07 Okay, cool. And then I think, for the different operation names, I think previously we discussed the three, right? It was Invoke Workflow, Invoke Runner, and then invoke agent.
**Max Ind (Google LLC)** 11:18 I actually didn't want to, like, put Invoke Runner anywhere, I just, you know, so it would be like, okay, if invoke Agent doesn't fit, and Invoke Workflow doesn't fit, then, you know… would not recommend people to use Invoke, the Entry point or something, yeah.
And in most… in the two cases were… so the two cases were… an entry point didn't fit, was ADK and OpenAI Agent SDK, I think? And in both of these cases, the entry point was named the runner.
So that's just, like, a happy coincidence.
**Mikolaj Knap (Google LLC)** 11:56 Okay.
Makes sense. Okay, but…
**Max Ind (Google LLC)** 11:58 But I think it's… the point of the operation name is that, like, it can be per framework. There's no… They're, like, Maybe some rules about it, but no, like, hard rules.
**Mikolaj Knap (Google LLC)** 12:14 Makes sense. Thanks for clarifying.
**Trask Stalnaker (Microsoft Corporation)** 12:18 Aaron.
**Aaron Abbott (Google LLC)** 12:20 Yeah. I had maybe two questions. First one is small.
For the span name, I think we'd say today to use the operation name as, like, a template perimeter. Are we… so we're still gonna do that, and it would then… would you see Invoke?
Like, would you see workflow versus agent in the spending, is my question.
**Max Ind (Google LLC)** 12:42 Yes, yes.
**Aaron Abbott (Google LLC)** 12:45 Okay, cool.
And then the second one was… I think, part of the… Part of the goal here was to know which is the top-level thing.
Does this help, like, to help move the needle on that? Because we would have runner for frameworks that have a top-level thing as the operation name?
Or is there some, like, static way to tell, for example, from the metrics, which one is the entry point or top level?
**Max Ind (Google LLC)** 13:10 Yeah, I… in the PR right now, I have the isNested boolean, And Do we feel like that… that can stay?
**Liudmila Molkova** 13:24 We should talk about this, because there are two… two proposals. One is yours in this PR, and one is mine in draft that suggests a different heuristic, which is We would stamp main agent name on everything, but not Top level.
And it's kind of subtle. I feel like it would be very hard to explain and very hard to use, so, like, I like the idea of stamping main agent name regardless.
But just, I feel it's not a good heuristic to… Differentiate the top level from nested.
**Aaron Abbott (Google LLC)** 14:05 Yeah, I think the… oh, sorry, I was just gonna say, I think the Boolean is a little easier to use with most metric query languages as well.
**Trask Stalnaker (Microsoft Corporation)** 14:15 Max, can that, I would suggest a separate PR for that?
**Max Ind (Google LLC)** 14:21 Okay.
**Trask Stalnaker (Microsoft Corporation)** 14:23 Sounds good.
Since it's sort of… I don't… I think it's… unrelated-ish?
**Max Ind (Google LLC)** 14:32 Yeah, more or less, yeah.
**Trask Stalnaker (Microsoft Corporation)** 14:43 Any other… Anything else, Matt? Oh, sorry, Surya, go ahead.
**Surya Teja** 14:52 Yeah, how is this going to impact the invoke agent, remote, span?
**Max Ind (Google LLC)** 15:01 I… so, yeah, so the… we've been only talking about Invoke Agent Internal.
But there's also the Invoke Agent client, and…
**Surya Teja** 15:11 Yeah.
**Max Ind (Google LLC)** 15:12 Yeah, is there… I don't know if there's invoke agent server span kind, but I think it… doesn't, Yeah, it doesn't impact that, because the invoke agent client Is already called Invoke Agent.
So there's no need to… Change anything?
**Surya Teja** 15:32 Okay.
**Max Ind (Google LLC)** 15:33 taping, yeah.
**Surya Teja** 15:34 And the next question is a quite stupid one, actually. Why can't we distinguish, so, as I understand, this is… we're going to call invoke agent for every span.
And even if it's an agent workflow in Crew AI or Lama Index, we'd be using Invoke Agent, if I understand correctly, after this convention. So, why can't we interchangeably use Invoke Workflow For those kind of operations, which identified themselves as a workflow.
And invoked agent.
for those… agent calls that identify themselves as an agent. Like, I can give you an example, but I'll pause here and see if you got my question or not.
**Max Ind (Google LLC)** 16:20 Yeah, I think the main motivating example is that, If it now doesn't matter if the… entry point for a given Agentic system. If it's a workflow or a… or an agent, you can just get the… you can get the duration metric, or whatever, just from the one metric. You don't need to know the internals of how the system is implemented.
**Liudmila Molkova** 16:51 So, like, the client… Example is a very good one. You use Invoke Client Agent regardless of how the… The server is implemented.
**Surya Teja** 17:02 Yeah.
Cool. Thanks a lot, guys.
**Trask Stalnaker (Microsoft Corporation)** 17:07 And you still get that, back to the operation name, you still get that distinguishing factor of if it's a workflow, or an agent, or a runner.
**Surya Teja** 17:20 Yeah, I… the major reason for asking this question is, after this implementation, I believe We should be doing some changes on the… Instrumentation side to accommodate The new span type.
both on the JS side as well as on the Python side, I just want to estimate how much rework should be done For this, after this change.
**Trask Stalnaker (Microsoft Corporation)** 17:50 Yeah, Aaron.
**Aaron Abbott (Google LLC)** 17:54 You know… Was everything you were saying addressed, Surya? Just making sure?
**Surya Teja** 18:01 Yes, Aaron, it's done, yeah.
**Aaron Abbott (Google LLC)** 18:03 I was gonna change the asymptom then also.
Yeah, so…
**Liudmila Molkova** 18:07 One more point on this very quick one, sorry.
**Aaron Abbott (Google LLC)** 18:09 Please, yeah.
**Liudmila Molkova** 18:11 the GenAI Agent Operation Name, do we suggest a new attribute? Because the current one is GenAI operation name.
**Trask Stalnaker (Microsoft Corporation)** 18:19 Oh, wow.
**Liudmila Molkova** 18:22 Okay.
Thanks. That's it. Sorry, Aaron.
**Aaron Abbott (Google LLC)** 18:26 Oh, no, you're good. So one other thing I was gonna ask was, since we're kind of collapsing the metrics also, I was wondering if… Cardinality's gonna be a concern.
So I know, like, for Agent Invocation, we were originally thinking it would be, like, a handful of… Agent names, or workflow names, or whatever, per, per agent, I suppose.
And I know… I know with the workflow things, there's, like, this kind of trend I'm seeing where people write normal code, and then each step between, like, an 08, I think Vercel does this. I don't know if ADK does this today. Just gonna share this chat.
It creates, like, a… I imagine a kind of enormous amount of workflows, because it's just kind of, like, control flow and code, so, Maybe it's okay, I just want to call out that we're probably Increasing the cardinality a lot, and Yeah, and then I think we talked about them having a name last time as well. Just want to make sure that If they don't, we could collapse them into, like, a single… kind of like we do with, token modality?
We could collapse things in the metric definitions if we need to.
**Liudmila Molkova** 19:41 Why would it have high cardinality? I didn't get it.
**Aaron Abbott (Google LLC)** 19:45 Yeah, so… Do you mind… Can somebody open this blog post?
**Trask Stalnaker (Microsoft Corporation)** 19:50 Oh, yeah.
**Aaron Abbott (Google LLC)** 19:52 Yeah.
Again, I'm not sure if this is getting ahead of ourselves, but this thing is, like… there should be, like, just a code snippet here somewhere.
Yeah, right here.
So they… they kind of just change all this stuff to be workflows and steps.
That you define in code for, kind of, like, structured stuff, and… I imagine that this… this is much easier to create than, like, defining your own DAG or something like that, which would be one workflow or whatever, so… Just something I'm seeing, it seems like there's gonna be a lot workflows.
If they're easy to define like this.
**Liudmila Molkova** 20:36 Still, like, the number of, essentially, these functions.
that I have in my code that… Explain some steps.
**Aaron Abbott (Google LLC)** 20:45 Yeah, exactly, and the reason they do this is because it's for durable execution, so, like, everything between the awaits gets persisted, the state gets persisted to a database, and then it can resume later on if something fails or whatever.
**Liudmila Molkova** 21:00 Yeah, like, it wouldn't… We would have this problem today as well, right? Because we put workflow name in the metric attribute.
**Aaron Abbott (Google LLC)** 21:11 Yes, except that we have two metrics today, right? We have the… Or, maybe that was…
**Trask Stalnaker (Microsoft Corporation)** 21:16 That's only half. Generally, we don't consider 50% meaningful when it comes to cardinality, like, 2X.
**Aaron Abbott (Google LLC)** 21:24 Right, but the agents…
**Trask Stalnaker (Microsoft Corporation)** 21:25 Order of magnitude.
**Aaron Abbott (Google LLC)** 21:28 No, I understand, but the, like, one of them is… is an order of magnitude bigger, and now we're, like, collapsing them so the agent invocation suffers as well.
**Liudmila Molkova** 21:37 Wait, Dan.
I see.
I mean, you're saying that when we degrade and overflow the workflow metric, we wouldn't at least overflow the Agent metric.
**Aaron Abbott (Google LLC)** 21:53 Yes, for example, yeah.
Anyway, I think maybe we're getting ahead of ourselves. I can drop a comment on the PR Max, if you're gonna send one.
Okay, thank you.
**Trask Stalnaker (Microsoft Corporation)** 22:07 Yeah, and I would… Say that for instrumentations that are, like, if there is something where you're expecting that It can either be instrumentation that has to truncate You know, stuff, deal with the cardinality, or… You know, opt-in, opt-out.
stuff. We definitely have metrics that, you know, in… under certain usage can have high cardinality.
**Aaron Abbott (Google LLC)** 22:37 Right.
**Trask Stalnaker (Microsoft Corporation)** 22:38 Yeah.
**Aaron Abbott (Google LLC)** 22:39 It's kind of like when people hammer 404s to… Mess up your metrics if you record the path or something like that.
**Liudmila Molkova** 22:47 Like, the HTTP route cardinality can be quite high.
**Trask Stalnaker (Microsoft Corporation)** 22:57 anything else, Max?
**Max Ind (Google LLC)** 23:05 No, that's it for me, thanks.
**Trask Stalnaker (Microsoft Corporation)** 23:11 Alright, hey, we have… 7 whole minutes.
Anything anybody specifically wants to raise?
Otherwise, I will troll the, PR dashboard.
**Liudmila Molkova** 23:32 It should have stability category here, but yeah, maybe this one is a good one.
**Trask Stalnaker (Microsoft Corporation)** 23:38 We can, The dashboard supports labels.
**Liudmila Molkova** 23:43 Hmm.
**Trask Stalnaker (Microsoft Corporation)** 23:44 So you just tell it in the configuration What labels you want to expose.
**Liudmila Molkova** 23:59 Nice. And then it would have a separate, like, labels inside the table, would it?
**Trask Stalnaker (Microsoft Corporation)** 24:05 Yeah, yeah, so, like… A couple people are using this.
Yeah, and then it will… it'll just show them, like, little badges, like, right here, next to the PR.
**Liudmila Molkova** 24:17 Wow, awesome.
**Trask Stalnaker (Microsoft Corporation)** 24:22 Let's see… oh, go ahead.
**Liudmila Molkova** 24:24 No, this one is approved. Okay.
**Trask Stalnaker (Microsoft Corporation)** 24:26 Yeah, yeah, I just approved that one. Looks good.
This one also… We could merge… This one, also, we could merge… Looking at ones that have… Let's see… On approval, let's see… This one, I thought it was interesting, couple… Thoughts here. One was… one relates to the main agent.
Where… so if we're stamping… Agent name… From down the hierarchy.
So onto… we could end up stamping that onto a client span.
That makes… An outgoing call to a different agent, and if it doesn't already… Know a name, have the name of the remote agent?
**Liudmila Molkova** 25:37 So you'd end up…
**Trask Stalnaker (Microsoft Corporation)** 25:38 Stamping it there, which would be… Kinda against us, not semantically correct.
**Liudmila Molkova** 25:46 I see, yeah.
**Trask Stalnaker (Microsoft Corporation)** 25:47 Which, you know, brings us back to possibly main agent.
And using… I like the idea of propagating Mate Agent down. I mean, Since that's… Also helps address the issue of, if you have nesting, nested agents.
**Liudmila Molkova** 26:14 I think we need to pick, like, if we say if we propagate main engine, then it's the same in process at least, right?
All the way down.
It's like, no matter how many Agentic layers you have, Take care. Yeah. Everywhere.
**Trask Stalnaker (Microsoft Corporation)** 26:30 Yeah, yeah.
**Liudmila Molkova** 26:32 And if we are propagating Agent the… not the main one, then it's your closest neighbor, right?
Like, your closest parent.
**Trask Stalnaker (Microsoft Corporation)** 26:43 Yeah, yeah.
**Liudmila Molkova** 26:46 Would we end up with the need to propagate the whole hierarchy?
**Trask Stalnaker (Microsoft Corporation)** 26:55 Well, I wonder, do we… I mean, does… For the use case, would agent name be what people… generally want…
**Liudmila Molkova** 27:07 Or is the intermediate agents would be something anybody cares about?
Enough.
**Trask Stalnaker (Microsoft Corporation)** 27:13 Yeah.
Yeah.
**Liudmila Molkova** 27:14 Probably the main agent would address, like, 80% of the use cases or something.
I see, okay.
So maybe… We can ask Otter to remove agent name for a sec.
then I can resurrect my PR.
to stat… to add main agent.
To the other spans.
and metrics.
And then we can bring it here.
I guess this PR tells not to stamp.
Attributes on any signals that don't reference them otherwise.
And we kind of need to reference main agent somewhere before it makes sense to put it here.
**Trask Stalnaker (Microsoft Corporation)** 28:02 Yeah, that was the other thing that I noticed was that, like, the inference spans don't have GenAI, don't have the agent name.
referenced yet.
So you, in the current PR, at least, you wouldn't get agent name on that, but that kind of makes sense, what you're saying, that you would.
We would have to go around reffing that.
**Liudmila Molkova** 28:25 Oh, and for the execute tool… the agent who executes the tool kind of makes sense, right? Not just the main agent.
But then, maybe this is not the generic context propagation mechanism, because it happens inside the same instrumentation.
And it can be done, however.
**Trask Stalnaker (Microsoft Corporation)** 28:54 Yeah, even… Propagating just to certain… if… so if we did want local propagation, Being more targeted about that.
Yeah, Felix.
**Felix Becker (Anthropic)** 29:08 Is this only for the agent name, or also, like, how does the agent ID play into this? Because… I think in some of our Instrumentation, we may not be able to emit the agent name at all, because Agent name is, like… can be caller provided, or in some instances, can even be model provided, and so it has, like, different, kind of, PII considerations.
And may not be allowed to be emitted, or in certain, like, settings, or configurations, or HIPAA orgs, like, you wouldn't be allowed to emit it?
**Liudmila Molkova** 29:51 Are you talking about hostage agents?
**Felix Becker (Anthropic)** 29:55 Yeah.
**Liudmila Molkova** 29:58 Poor them.
It shows…
**Felix Becker (Anthropic)** 30:01 I mean, I don't think it's… it's… I don't think it's specific to hosted.
**Liudmila Molkova** 30:06 It a little bit is, because the, like, the non-hosted agents, like, in-process agents, don't have the ID.
Like, there is no… Unless you, you run it.
There is no sticky identifier for the thing.
But if you run it, then it's current… in the current shape, it should be a resource slash entity.
**Felix Becker (Anthropic)** 30:36 I mean, I don't… I'm not familiar with how, for example, the cloud code internals do this, but… a local runner might still, you know, assign a UUID to, like, every local agent, right?
**Liudmila Molkova** 30:53 Right, if you run it, then you can hopefully use NTT for it.
**Aaron Abbott (Google LLC)** 31:03 Are we talking about where, like, a coding agent generates new agents on the fly kind of thing? So it might name something with, like.
BII, Felix.
**Felix Becker (Anthropic)** 31:16 Yeah, like, in a case where an agent is, like, spawned on the fly, the name could be model provided. But even in the case where, like, Even the general case where, like, the caller provided… The agent name, our privacy team classifies that as, like, PII moderate, because it's, It's, like, caller-provided free-form text, and so they… could've… put, like, some kind of PAI in it.
So… I think for safety, some of the stuff we don't emit when, like, the org is flagged as, like, a HIPAA org or stuff like that, Just for compliance reasons. So I just want to make sure that, like, if we define anything here, it's not, like.
to tie to the assumption that there is always an agent name, but that it also works with, like, if you only have an agent ID.
**Trask Stalnaker (Microsoft Corporation)** 32:18 And I like the idea, like, if we do GenAI main agent, I also see that as… Partly solving the, I mean, main agent, both name and ID matching the entity, which also allows for, multi-tenant. Like, I don't know if we… need… want to… I don't really want to wait for… to support multi-tenant for entities to sort of figure that out.
And so by… kind of hoisting both main agent name and main agent ID up to… regular span attributes, that solves that, and I would think Then we would propagate both of them, if they… or whichever ones exist, that would be the option to propagate down.
**Liudmila Molkova** 33:16 to manage and time-space. Anything there.
Well, that doesn't have to be anything, but…
**Trask Stalnaker (Microsoft Corporation)** 33:22 Yeah, opt-in.
**Liudmila Molkova** 33:31 It might still make sense, though, for regulated environments that don't want PII in Agent Name.
2… Maybe fake the name, obfuscate, or hash.
to then… The dashboards and everything and queries would still use the same thing rather than a new attribute.
**Felix Becker (Anthropic)** 33:55 Yeah, you can take a hash of the agent name and put it in agent ID, is that what you're saying?
**Liudmila Molkova** 34:02 I think it has to…
**Trask Stalnaker (Microsoft Corporation)** 34:03 an agent name.
**Liudmila Molkova** 34:04 Yeah.
**Felix Becker (Anthropic)** 34:05 Oh, yeah.
**Aaron Abbott (Google LLC)** 34:06 Or just put the ID in both.
**Liudmila Molkova** 34:09 Yeah.
So, for this one, it sounds like… We want to ask Cost Order to take it away for now.
And we expand this list over time, with MediaGen, probably.
**Trask Stalnaker (Microsoft Corporation)** 34:34 Yeah.
I think that sounds good, because, yeah, conversation at ease.
We could merge that in.
Cool, great, topics today, anything… Any last thing that anyone wants to raise?
**Liudmila Molkova** 35:08 I have a conformance test, PR, that updates Semantic Convention version.
And I would appreciate reviews, and it's, big one, because… We change this pen type.
for inference.
And there is a lot of… Sorry, I'll send you the link. Bye.
**Trask Stalnaker (Microsoft Corporation)** 35:32 Well, I…
**Liudmila Molkova** 35:33 Oh, God.
**Trask Stalnaker (Microsoft Corporation)** 35:33 I'll overview all your…
**Liudmila Molkova** 35:36 That 277, that's the most important one.
**Trask Stalnaker (Microsoft Corporation)** 35:38 27… okay.
**Liudmila Molkova** 35:45 Oh, it's failing. I'll fix it.
**Trask Stalnaker (Microsoft Corporation)** 35:49 I will… I will look at all of them.
**Liudmila Molkova** 35:52 Sorry.
**Trask Stalnaker (Microsoft Corporation)** 35:53 No, no, that's… I mean, by me, look at them, you know what I mean, in this.
**Liudmila Molkova** 35:58 In the same way I created them, yes.
**Trask Stalnaker (Microsoft Corporation)** 36:01 Yes.
**Liudmila Molkova** 36:04 Cool. Alright. Thanks a lot.
**Aaron Abbott (Google LLC)** 36:07 Alright.
**Trask Stalnaker (Microsoft Corporation)** 36:08 y'all.
**Liudmila Molkova** 36:09 E.
**Mikolaj Knap (Google LLC)** 36:10 Thank you, thank you.

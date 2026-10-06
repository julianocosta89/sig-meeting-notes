SIG: GenAI Semantic Conventions and Instrumentation Stability
Date: 2026-10-05
Duration: 30 minutes
============================================================

## Zoom Recording Transcript

**Max Ind (Google LLC)** 00:44 Hey.
**Surya Teja** 00:50 Hi.
Just give us a couple of minutes. Folks might be trickling in.
**Trask Stalnaker (Microsoft Corporation)** 01:37 Hey, Fox.
We'll get started in a minute or two here.
Alright, let's… Go ahead and get started.
I'm just gonna copy all of this stuff, or move it all down here… Okay, looks like we need… A lot of reviews… Token usage for failed operations, okay.
Cool, So that one, I will… Review that one, after the call…
**Aaron Abbott (Google LLC)** 04:13 Wes, did you want to share, or… I'm happy to do it.
**Trask Stalnaker (Microsoft Corporation)** 04:16 Cool.
**Aaron Abbott (Google LLC)** 04:17 Okay.
**Trask Stalnaker (Microsoft Corporation)** 04:18 Alright.
Thought I was, but wasn't clearly. Thanks.
Bunch of, let's see, reviews… is this… Aaron. Let's see. No, this is Okay, we have… Approvals we need here… So… oh, it looks like Ludmila tried to merge it, but… Got stuck in… Let's see… Removed due to a manual request. Okay, looks like Ludmilla added it, but then removed it, so maybe I won't add it right back.
And.
Maybe she pulled it for an intentional… let's see, this dashboard… oh.
Was there a comment?
I don't know, it looks okay.
Two approvals… oh, two approvals, but from the same company.
Okay.
Okay.
Yes, did we document that as our policy here?
Two approvals, yes.
Two different companies.
Alright, well, that explains why Ludmilla pulled it from the… From the merge queue… Nice.
I can probably give that a… Quick look. I die. Suspect.
It is… Non-controversial… Let's see, oh yes, this is… Oh, no, this is not the one I was hoping it was.
Inference event to be severity level debug.
Any… Counter-argument to this?
Ludmila or Dylan, any reason not to rubber stamp this?
**Liudmila Molkova** 07:16 I think we can, like, shut down the severity, but… I don't think it's important.
**Trask Stalnaker (Microsoft Corporation)** 07:30 All right, let's give it a non-Google approval here.
**Neil Yashinsky** 07:33 Yeah, I concur. Sounds good.
Urge away.
**Trask Stalnaker (Microsoft Corporation)** 07:46 We could probably… I could look at this after, but just since y'all are here, if there's anything… Cliff, I failed GenAI Capture content.
Upload hook when it's an error.
**Liudmila Molkova** 08:09 I think the… oh, maybe the PR description is… oh, and I think it's good enough, but essentially, if you look inside, it's just the repeated… This paragraph.
So it's now on the… Output messages that you capture what you've got.
**Trask Stalnaker (Microsoft Corporation)** 08:33 Okay, yeah.
Looks very… uncontroversial.
Formally define… the environment variable.
Good.
**Liudmila Molkova** 09:00 Dylan here?
Oh, don't worry.
**Dylan Russell** 09:02 Yes.
Yeah.
I think…
**Liudmila Molkova** 09:09 I left some feedback on this one regarding the decorative config, but maybe for the scope of stabilization, maybe should we just define the environment variable?
And, separate the declarative config, because we won't be able to stabilize it anyway in the near future.
**Dylan Russell** 09:28 Yeah.
Yeah, I'm fine with separating.
Are you just saying we should separate the two things?
**Liudmila Molkova** 09:39 Yeah.
It's just, I feel like we could…
**Trask Stalnaker (Microsoft Corporation)** 09:44 Okay.
**Liudmila Molkova** 09:44 Need to spend more time on the declarative config.
And, like, the environment variable… Documenting it would… would be… a no-brainer. Oh, except I have some bike shed on the name, but… Whatever.
**Dylan Russell** 10:02 Okay.
Sorry, this PR is in the… in the config repo?
Oh, no.
I see.
I'll look at your comments, yeah. I think that sounds good.
**Trask Stalnaker (Microsoft Corporation)** 10:22 Yeah, that's a good point about the.
Declarative config, the instrumentation node isn't stable, so…
**Dylan Russell** 10:31 Yeah.
**Trask Stalnaker (Microsoft Corporation)** 10:32 That won't help us with this Stability effort. It's still great to define things there, and sometimes by defining the things there, it helps us with, even with naming of the flat environment variable, but… Yeah, splitting those out sounds good.
Inference bands… go… the model provider… is instrumented.
So.
**Liudmila Molkova** 11:11 This is… go ahead.
**Trask Stalnaker (Microsoft Corporation)** 11:16 For server… Inference spans… The model provider.
**Liudmila Molkova** 11:24 This is for… Us, for a client side.
So maybe I'll drop the VIN, the model provider is instrumented, it doesn't matter.
So this is the discussion we had around the inference operation, whether we should rename it.
And that we should… like, my conclusion that I'm proposing here, we shouldn't.
And… This documents that the client inference is whatever client thinks about as inference.
And that the things like response model, response ID, or the usage are what the provider returned. We have no idea how many inference calls.
the provider made On its own side.
**Trask Stalnaker (Microsoft Corporation)** 12:15 Nice. So yes, I was initially thrown by actually it was the scope. My brain went to Instrumentation scope and merged these words in the wrong order.
Yes.
**Liudmila Molkova** 12:31 And I think Aaron brought up a great point that we should get some ACK from Felix.
Who had raised the original issue, so… Doesn't seem like Felix is here… So I'll ping him and ask to review.
**Trask Stalnaker (Microsoft Corporation)** 12:54 Well, I can… Shoebox… I don't remember.
Nope, still not helping.
There we go, Felix F. Becker.
Did we discuss this in… the general SEMCOM in the general meeting, the Tuesday meeting last week.
**Liudmila Molkova** 13:41 Probably so.
**Trask Stalnaker (Microsoft Corporation)** 13:43 Okay.
Would be… might be worth.
**Liudmila Molkova** 13:47 Yeah.
**Trask Stalnaker (Microsoft Corporation)** 13:48 Bringing that.
Inference… duration… Yes, this was the one that I was hoping for. Okay.
So… couple of… Comments… okay, I can follow up, since I'd kind of taken this YAR.
And…
**Liudmila Molkova** 14:20 Oh, you want to take a dollar and fill up?
**Trask Stalnaker (Microsoft Corporation)** 14:23 Oh, I see, yes, you had taken it back.
**Liudmila Molkova** 14:29 Oh.
**Trask Stalnaker (Microsoft Corporation)** 14:29 Either way, yeah, yeah.
**Liudmila Molkova** 14:34 Okay, cool. I'll follow up. Thanks, Saren, for the review.
I think we, we have, Max and Mikolaj here to chat about agent versus workflow.
Maybe… You folks didn't put it in the agenda, did you?
**Max Ind (Google LLC)** 14:58 I think I did, it's, like, second to last, and… And yeah, hi, nice… yeah, nice to meet you all, I think… I've interacted with Trask on one of the… PRs, and I recognize the folks from Google, but yeah, but nice to meet.
everyone else.
Nice to put face to the name.
**Trask Stalnaker (Microsoft Corporation)** 15:21 Welcome.
**Mikolaj Knap (Google LLC)** 15:23 Yep.
**Trask Stalnaker (Microsoft Corporation)** 15:23 Which one here… It's one of.
**Max Ind (Google LLC)** 15:26 I think that's, yeah, it's 571.
Okay. So that's the… it's… I just basically took the… What I thought are the non-controversial parts from the discussion under the Agent versus workflow issue.
And I based this off of your, of a flood MIWAS.
And.
**Dylan Russell** 15:51 and.
**Max Ind (Google LLC)** 15:52 And, like, a… Poc.
Or request?
Yeah, and basically added to it, and so, yeah, so… So, this is fresh off the press, and in the end… Hopefully it, yeah, it won't be too controversial. I guess like the motivating, factor behind this is the invoke workflow as, like, a root span is confusing. It proves to be confusing when talking about it, but we still want to have the… End-to-end duration tracking.
And we still want to have, like, some way to easily count how many tokens are used for, for.
For, like, a agent or workflow invocation as, like, a… Basically unified, like a simple unified query, yeah, so that's what the handle turn.
Span and a set of metrics eventually might be, yeah.
**Liudmila Molkova** 17:00 I think I had two different thoughts about this one, and I… the prototype I shared was one, and then maybe I didn't update it, but I… I kinda… So there are two ways to think about it. The first one is… We unify the outer layer and we call it a turn.
Where we call all, like, the Invoke Agent and Workflow all become turns, because they are, right?
And then.
In the first approach, the spend type, or… Metric name is… Includes handle turn and then it's a special type that's used for outer operation.
And the second approach.
It is… all of them have this metric name and spend type, and then you can tell if it's an agent or a workflow by the attributes on it.
And after some internal discussions, I'm kinda… I think I… I… The the second would be more consistent, like all of them are turns.
Yeah, yeah.
**Max Ind (Google LLC)** 18:20 I.
Yeah, I think you included that in the discussion, and I think.
It looks clean, but I worry that there might be cardinality issues if we just — Have every metric under one name.
Maybe? Because, like… And.
Because, I don't know, maybe these are only Google-sized problems, but, like, when we put agent name in the metric.
This leaves, there's not much cardinality left after you have the agent's name in the metric, just because there are so many agents around. So, like, I want… I worry if, like, we have a model Name and also tool names under the same metric that it might be, might pose an issue.
**Liudmila Molkova** 19:12 Oh, with this… would not have model name or tool names. It would only have the agent name or workflow name.
**Max Ind (Google LLC)** 19:19 Okay, okay. Oh, that's much better, yeah, yeah.
**Liudmila Molkova** 19:24 Like from that attributes perspective, it's all the same. It's just that.
The Invoke Agent and Invoke Workflow are the single metric.
**Max Ind (Google LLC)** 19:34 Okay, yeah, and would you have a name? How could we call this combined metric?
**Liudmila Molkova** 19:43 So, like, handle turn, or, the… okay, so… the bike shedding territory, the turn or run. I think those two are kind of synonyms, and the turn Is.
Sometimes the term is used to describe the model as well, unfortunately.
And Ron is probably more about the agents. I think we can leave it either, but, like, yeah.
But something like handle turn.
Right.
**Max Ind (Google LLC)** 20:15 Yeah.
**Liudmila Molkova** 20:16 run.
**Max Ind (Google LLC)** 20:17 Okay, yeah, I don't have a strong opinion between the two, yeah.
**Liudmila Molkova** 20:21 Yeah.
I think Surya you were going to prepare.
**Surya Teja** 20:26 Yeah.
**Liudmila Molkova** 20:26 Around this one, did you have a chance?
**Surya Teja** 20:28 Yeah, I had family emergency over the weekend, so I could not get some time. I was in the call trying to tell that I'll be ready on Wednesday. So, sorry for that. On… I'm still in the hospital, so…
**Liudmila Molkova** 20:43 Oh, I'm sorry.
**Surya Teja** 20:44 Yeah, yeah, sorry for that.
I'll be presenting my concrete thoughts on, red mistake.
**Liudmila Molkova** 20:55 Yeah, take, take, take your time if, especially if you're in the hospital, like take your time and, if you would have time or mental capacity at this.
**Surya Teja** 21:05 Yeah.
**Liudmila Molkova** 21:06 Great thing to review.
**Surya Teja** 21:07 Yeah, sure, sure.
**Trask Stalnaker (Microsoft Corporation)** 21:11 So, I didn't quite follow, if there were… Ludmilla, you were saying that there's a slightly different proposal from this?
Or this is the proposal that… we should… review.
**Liudmila Molkova** 21:33 I think this proposal doesn't include the level. Like, I'm I'm mostly curious about the spend types and metric names. And regardless of how you model them, you can have this picture. Right?
But, maybe, Max, you can… you can share what's… This is proposing.
**Max Ind (Google LLC)** 21:52 Yeah, I'm not that familiar with span times. And for metric names, I only included the duration.
metric.
**Liudmila Molkova** 22:05 Is it the comment for invoke agent and invoke workflow?
Is it March, Daniel?
**Max Ind (Google LLC)** 22:09 So I didn't actually decide on whether, like.
To combine the invoke agent and invoke workflow here.
chris ryall: Yeah, I deferred this, like, this should be independent, like, basically just having the turn span as the… outer span for any, you know, GenAI system, just to have, like, a consistent way of tracking duration, and eventually token counts. The token counts might be more… Controversial, so I deferred this from this PR.
**Trask Stalnaker (Microsoft Corporation)** 22:46 Yeah, okay.
**Ankit Singhal** 22:47 Just in a concise summary, like, what problem are we trying to solve here? Just… Fundamental idea.
**Max Ind (Google LLC)** 22:56 Sorry?
**Ankit Singhal** 22:58 Like, if I have to summarize, like, what problem you're trying to solve here, like, what would.
**Max Ind (Google LLC)** 23:03 Yeah.
**Ankit Singhal** 23:04 the.
**Max Ind (Google LLC)** 23:04 Yeah, so currently, In ADK, we have, like, an approach to have.
you know, consistent way of tracking GenAI system durations and token usage.
As, like, a histogram On, like, a per turn basis, right?
So, this is now based off of the wording in SemComp, where like, a multi-agent orchestration is called the workflow. But this proves confusing, because if we call anything a workflow, and people usually are not interested in workflows, they're usually interested in agents.
But if, like, a main end-to-end duration metric and main way to count tokens is on the workflow level, that's confusing.
So, one of the proposals is from the… Issue which brought it up initially, which is this 477 issue.
One of the approaches there just like an… was to have a turn span, and have this… these two metrics be counted on the turn basis. So basically have an abstract Turn and what handles the turn doesn't matter, but we can.
Have a duration and token counts metrics for this?
Handling of a turn and, you know, this would give us a consistent way of.
Easily querying duration and… And… and And token usages for any GenAI system.
Yeah, yeah, I…
**Ankit Singhal** 24:54 Yeah, that helps understand, like, I think, the orange. And one question here, so for… for the handle term, say, for the fourth scenario here, right, we have multiple… we have a… Multiple agents being called at a workflow.
So is the expectation that the handle turn will show you the token count for this entire turn, which includes all its child operations?
**Max Ind (Google LLC)** 25:16 Yes, yes, it's expected that this So duration is easy, because we already have a… Yeah, for token counts. This is a bit difficult, because you need to take into account the entire workflow or agent tree, or, you know, and then if it's cross-processed, then it's… even more difficult, but I hope this can be, like, just, like, a best effort.
You know, we just tried to… you know, if it's a single process, and on an agent framework level, you can do it, I think, relatively easily. If it's cross-process, it may be more difficult, but… But as a starting point, it may be good to have this, like, you know.
Like, striving to have a, you know.
A histogram per turn of your token usages, yeah.
**Dylan Russell** 26:15 Do we have a clear definition of, like, what a turn or a run is?
It's like, what's to prevent us from, like, being like, oh, we need some, like, higher level… Abstraction in the future.
**Max Ind (Google LLC)** 26:26 Hmm.
Yeah, I think… That's… that's a good question. I… you know, I don't want to be just like, yeah, probably it won't, because TURN already is abstract, but I want to say that, like, TURN is just like a… At.
It's just like whatever the user interacts with and that's just like a You know, the root, which kind of has everything underneath.
And then if, And then if… that's, like, my biggest worry. My biggest worry is, like, what if you have a remote agent, and the remote agent You know, your agent, which the user interacts with, calls another agent.
that agent would also create a turn span, and that, you know, might be confusing, so… So, when this entire thing kind of breaks down when you… Are dealing with multiple processes and, like, network calls in between, so… Yeah, I'm not yet sure how to handle that.
**Aaron Abbott (Google LLC)** 27:31 A quick question, Max, like, how feasible is it to instrument this generally? Like, one concern I have is In the spend name, we have the main agent name, which is from, like, the resource attribute, which might be difficult for the actual instrumentation to know what the value is, but just more generally, like, Do we have… I haven't looked at the PR yet, but I assume there's some reference scenarios.
**Max Ind (Google LLC)** 27:56 Okay, yeah, I wasn't entirely sure if the main agent name was a resource attribute.
So… Yeah, I have a couple of questions. How the… Main agent… so, so, an example for main agent name was, for example, the agent name from the agent card in A2A.
But I would suspect that this may be equally difficult to get as a resource attribute as it would be.
As a span attribute. So…
**Trask Stalnaker (Microsoft Corporation)** 28:29 Just to jump in, today it's a resource attribute, but there is a proposal to.
elevate it to a or also be able to record it as a span attribute.
**Max Ind (Google LLC)** 28:44 Okay,
**Liudmila Molkova** 28:45 So, like, it would be Taryn's question. It would be the name of the outermost agent. It would be propagated through the context or in some way or one way or another.
**Max Ind (Google LLC)** 28:57 Yeah, for outermost agent, if that's… if, like, if it's not… because, for example, like, A2A agent name and the outermost agent in… the framework that implements the A2A server. These can differ, so… It may be… it may be, like, you know.
Good to clarify which this should be, but yeah, if this was the outermost agent, then it should be pretty easy to… To instrument this in the handle turn, yeah.
**Aaron Abbott (Google LLC)** 29:28 I think Emil is next.
**Emil F** 29:32 Yeah, thank you. I was wondering how… Does the turn concept or maybe does it map one-to-one to a trace concept? So one trace, one tree of spans equals one turn, or in what cases does it not map cleanly?
**Max Ind (Google LLC)** 29:49 It should. It again breaks down kind of in a multiprocess.
Scenario, because it's, you know, it may be… You know, maybe you could also use convex propagation to only guarantee, like, one turn per trace, but… but yeah, this… the cross-process needs to be… needs to be ironed out, yeah.
**Liudmila Molkova** 30:12 It feels orthogonal because you can have multiple turns in one trace.
You can have trace that's much bigger than a turn.
You can have… I can imagine a case of a synchronous communication when your turn starts in one trace and completes in a different one, like, theoretically, not practically, but theoretically.
So, like, I think those two are orthogonal.
**Emil F** 30:40 Would it make sense to enforce that connection? I just don't… I don't see quite the use of having those… Not… not linked, I guess.
**Liudmila Molkova** 30:54 Like, if in practice the trace starts wherever it starts, if I'm a user clicking on a web page.
My trace starts when I click on a button, let's say.
Or maybe even before that, when I load the page or something.
And then, like, you don't know whether the root span corresponds to an Agent call? Probably not. Most.
Usually, in most cases, not.
But then also, I can imagine a case where multiple turns happen in one trace.
And trace propagation and the agent runs are not connected. We have no means to enforce it. It will break all the rules around the trace propagation if we try to.
**Emil F** 31:43 Okay.
Yeah, I guess I'll need to… Dig deeper into that.
I'm asking because in the, long chain world, basically the turn is exactly a trace, but again, this is a little bit limited to.
Tracking one conversation, or one agent invocation.
**Max Ind (Google LLC)** 32:06 Yeah, and then in LangChain, if I can ask really quickly, like in LangChain, if you have like a remote subagent.
Would that still be counted as one turn? And how do you guarantee that this turn Yeah, that the subagent knows that it's being part of an already existing turn instead of creating another turn.
**Emil F** 32:26 You would do it by… by instrumenting the context propagation, so the first agent would need to propagate the context. Otherwise, you will get them as different traces and different turns. Which isn't the end of the world, but it's not going to look as nice.
**Max Ind (Google LLC)** 32:42 Yeah, thanks.
**Emil F** 32:45 I see Ankit.
Has… has…
**Ankit Singhal** 32:48 Hey, one question here, and please help me educate as well if I'm missing things.
For the handle terms, say, for example, if I'm… The place this lived in the located span for the main agent.
Is there a case where it would not work? Like, is there any case where A main agent turn cons… like, a main agent invocation consists of multiple turns.
**Max Ind (Google LLC)** 33:16 Main… I don't think so. I think a main agent invocation is synonymous with a turn, but the… there's the other case where you have multiple agents, and you don't know that you're dealing with multiple agents, and That's possible in ADK, and that's why the turn concept is kind of useful, because you can have, like, sibling agents, and, like, agent handoff.
And so at this point, if there was no overarching span over the invoke agents, these would just create two traces, and we wouldn't know the… End-to-end duration and we wouldn't know the total token usage of that, For that, you know, turn.
**Ankit Singhal** 34:03 Basically, okay, so this is the case for the… If I understand correctly, specifically for the handoff, where one agent hands off to the other, but they are not, like… I'll… like, there's no time.
parents are in their siblings.
**Max Ind (Google LLC)** 34:20 That's one of the motivating things.
**Ankit Singhal** 34:22 Would workflow not capture that?
**Max Ind (Google LLC)** 34:27 It, so workflow is currently what we are working with. So right now every call to ADK has a root invoke workflow span, but then it's confusing to talk about it because.
Then it feels like we're, like all the interesting information are not part of the agent, these are part of the workflow, and so.
We're kind of dealing with the issue that, like, if everything is a workflow, then the term workflow kind of loses its meaning.
**Ankit Singhal** 35:02 I see, okay. So the workflow term is not going very well, I'm guessing, right?
or.
**Max Ind (Google LLC)** 35:07 It's, yeah, it's…
**Ankit Singhal** 35:11 Awesome. Thank you. Appreciate it.
**Max Ind (Google LLC)** 35:13 Yeah, thank you.
Siri, I think, yeah.
**Surya Teja** 35:23 Yeah, I have two questions, actually.
The first one is, in ADK, are you… using the turn span only when you are running agents locally, or are you capturing… how are you capturing if there are remote agent invocations?
**Max Ind (Google LLC)** 35:42 Yeah, right now we don't emit the… Right now, we don't emit the turn span, we emit the invoke workflow, and we don't have anything in place to catch the remote subagent cases, so… so this mostly works only locally right now.
**Surya Teja** 36:00 Yeah, so the next question is, I haven't looked at your PR, but the question is, are you planning to… So, let me step back a sec. The reason for this is to understand properly what is the duration for the whole operation, as well as what is the token count for whole operation.
**Max Ind (Google LLC)** 36:18 -H.
**Surya Teja** 36:19 With ADK, I think there is cloud-managed agents also feasible that we can run. So, say, in a scenario, you start a workflow, or you start an agent.
That is going to invoke.
Another agent that is on another server.
Through A2A, or some other protocol. In that case.
we can't have trace continuity unless until we instrument, we propagate the trace like how Langchain is doing.
So, are you thinking the handle turn to just only show the token counts for the invocation… the… LLM invocation that is happening on your own server, and you're not considering the other server token counts.
**Max Ind (Google LLC)** 37:04 Yeah, I have that included, and I'm… I… the wording I went with is that it's best effort, so if the remote subagent returns the, like, something like a usage metadata, for the… yeah, then this would be included, and if it doesn't, then it doesn't, yeah.
**Surya Teja** 37:26 Okay, cool. Thanks.
**Max Ind (Google LLC)** 37:28 Yeah, thanks.
**Trask Stalnaker (Microsoft Corporation)** 37:33 Cool, I will let us go over time here to… because I thought that was… Important kind of context for us all to have to review this.
Anything… else Contextualize or questions about this?
Proposal, before we all go off and read it.
**Dylan Russell** 38:00 It's for both client and server, or just one?
**Max Ind (Google LLC)** 38:06 I'm… I'm thinking only for server.
Because for a client, they might… Yeah, yeah.
**Dylan Russell** 38:16 Only for server.
Or client, like…
**Max Ind (Google LLC)** 38:22 Yeah, is internal LAN server the synonymous?
**Liudmila Molkova** 38:26 No, I think this is for the internal. The client stays away because it's… you don't invoke external, like, remote workflow, you normally invoke remote agent explicitly.
**Dylan Russell** 38:41 Yeah, okay, that makes sense.
**Liudmila Molkova** 38:45 If we rename invoke agent to handle turn with agent as an attribute, then we should consider also redeeming the client agent span accordingly.
But we don't have to.
**Aaron Abbott (Google LLC)** 39:02 Maybe one quick question for you, Max, is does just using A to A as an example, because I think The cross process part is the complication.
I think it has some kind of invocation ID or something like that, that is propagated.
**Max Ind (Google LLC)** 39:17 Okay.
**Aaron Abbott (Google LLC)** 39:19 So, I guess, kind of like Emil's question, is that one-to-one with the turn, if you did propagate it and you wanted them all to share a turn?
**Max Ind (Google LLC)** 39:26 Yeah, I don't… I don't have, like, a turn ID, but… but yeah, ideally, the… I don't know if the invocation ID could be used to know where… The turn starts and ends, like you would need to distinguish between.
Which call is the user's call?
And which call is the… an agent communicating with the sub-agent?
But yeah, that's… Yeah, I would hope that the turn and invocation ID or trace ID would be one-to-one, yeah.
**Aaron Abbott (Google LLC)** 40:02 Okay, I can take it to the comments.
**Max Ind (Google LLC)** 40:05 Okay, thanks.
**Liudmila Molkova** 40:06 By the way, maybe we don't need to solve the context propagation here because however we model it, context propagation is separate.
**Trask Stalnaker (Microsoft Corporation)** 40:19 Yeah, I wouldn't try to… Enforce one handle turn per trace.
At most, what we've done before is, like, having a local route, like, saying that it's within one process boundary.
There's one of them, we can do that, but… across multiple remote calls, I wouldn't… Tried to do that.
I think it's okay that they have, you know, they're nested across those boundaries.
**Liudmila Molkova** 40:54 The nice thing that we can enable it a little later. We can solve it, like, local only, and then we can say, okay, actually, main engine goes over the wire, or some other indication of the operation.
**Trask Stalnaker (Microsoft Corporation)** 41:06 You can opt into, yeah.
**Max Ind (Google LLC)** 41:09 Yeah, that sounds good.
**Trask Stalnaker (Microsoft Corporation)** 41:11 Max, would you be able to join tomorrow's, meeting? It's at 9 a.m. Pacific time.
**Max Ind (Google LLC)** 41:20 And.
**Trask Stalnaker (Microsoft Corporation)** 41:22 Cool, you have…
**Max Ind (Google LLC)** 41:23 Yeah, that's still relatively early for us, yeah.
**Trask Stalnaker (Microsoft Corporation)** 41:27 Will you add the… to the agenda there, so we can block some time? Because it is a… I think it affects… will affect a lot of people. It'd be good to get more… Eyes on it.
**Max Ind (Google LLC)** 41:41 Okay, yeah, sounds good. I will do. I will need, you know, to ask someone to know exactly which meeting you're talking about, but yeah, but I can do that offline, yeah.
**Trask Stalnaker (Microsoft Corporation)** 41:51 Okay.
**Liudmila Molkova** 41:54 Thank you.
**Trask Stalnaker (Microsoft Corporation)** 41:55 Thanks, everyone.
See you.
**Max Ind (Google LLC)** 41:58 Hey, Mae.
**Neil Yashinsky** 41:59 Hi, thanks.
**Surya Teja** 42:01 So, yes.

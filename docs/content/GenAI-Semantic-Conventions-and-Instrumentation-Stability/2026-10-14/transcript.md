SIG: GenAI Semantic Conventions and Instrumentation Stability
Date: 2026-10-14
Duration: 30 minutes
============================================================

## Zoom Recording Transcript

**Max Ind (Google LLC)** 00:28 Hello.
**Trask Stalnaker (Microsoft Corporation)** 00:29 Hey!
Sorry I missed Monday.
**Liudmila Molkova** 00:36 It's okay.
We have so many GenAI meetings.
Five a week, right? Crazy.
**Trask Stalnaker (Microsoft Corporation)** 00:45 Yes, yes.
It is.
And yet…
**Liudmila Molkova** 00:50 And yet, yes.
**Trask Stalnaker (Microsoft Corporation)** 00:52 There's never enough time.
**Liudmila Molkova** 00:54 Yeah, I feel like it's it's like the highways, right? So you you build more lanes, you get more cars.
**Felix Becker (Anthropic)** 01:19 Hey, everyone.
**Liudmila Molkova** 01:21 Hello.
**Felix Becker (Anthropic)** 01:23 I just wanted to pop in and say that we just announced OpenTelemetry and GenAI support for Anthropic.
across a cloud platform.
**Trask Stalnaker (Microsoft Corporation)** 01:37 Wow.
Will you link us to link the announcement?
**Felix Becker (Anthropic)** 01:42 Yeah, totally.
**Liudmila Molkova** 01:47 But he already posted in the Slack channel.
That's.
**Trask Stalnaker (Microsoft Corporation)** 01:50 Awesome.
**Felix Becker (Anthropic)** 01:51 Oh, both said it.
**Trask Stalnaker (Microsoft Corporation)** 01:52 Right.
**Felix Becker (Anthropic)** 02:07 This is weird.
**dylan russell** 02:07 And it's vendors, they provide SDKs.
**Felix Becker (Anthropic)** 02:10 This is our announcement tweet.
But yeah, I mean, this is something I've been kind of alluding to over the past weeks, you know, I've been working on this for a while, so I'm pretty excited for this to finally go out.
And a lot of the, you know, things we had discussed, or like, I brought up before, were kind of in the context of of this, or like, hey, we're… we're now emitting stuff from our own API, some of these spans don't.
don't work that well, like, if it's in, like, a multi-tenant service and not from an SDK, how should we model all this?
definitely great to just be able to talk about it a bit more openly, so… and I'm very excited to, yeah, just be a part of this and, evolve the standard forward.
I.
Really hope also that, you know.
There's more interoperability coming from this, and we set an example for others to follow with this, too.
And so, whatever we can do to… make it easier. We talked to a lot of partners for this launch, too, like, all the observability platforms, whatever, we can make it easier for everybody to kind of emit the same standard. It's a good thing for all of our customers.
**Trask Stalnaker (Microsoft Corporation)** 03:33 Yeah.
**Liudmila Molkova** 03:34 Awesome.
**Trask Stalnaker (Microsoft Corporation)** 03:35 I think every, every additional, especially big.
Either library that does emits natively, or provider, or hosted provider, all of those things.
go a long way, and… and also being in this community, like, because sometimes we see people launch stuff with OpenTelemetry.
And that's great, but we miss out on the feedback loop.
In this SIG that, so we definitely appreciate you and all the… everybody else who's here bringing those feedbacks to this group.
**Felix Becker (Anthropic)** 04:26 Yeah, it's been really helpful. Thank you for all the guidance in the past weeks.
**dylan russell** 04:32 So you guys are doing it on the server side and the client side?
**Felix Becker (Anthropic)** 04:36 Correct, yeah.
So, for the server, you configure it, like, in the developer console, and then, we talk to that platform directly. You have to put in, like, your auth token for it. For the client.
We basically bundle in, like, OpenTelemetry support, like, have a dependency on the OpenTelemetry API in the official SDK.
And so, if you already have, like, a global trace provider configured, it'll just work, and it'll also inject, like, the trace parent headers, so that… the traces get connected between the API and the SDK.
We should actually talk about what we should do now with the, With the, like… third party, or, like, the instrumentation that kind of just monkey patches the SDKs.
I think it would be good to maybe at least update the documentation to say, like.
The first-party SDKs support this, and so if you're… If you're on the latest version, you don't really need the packages anymore. Or… If you even want to, like, deprecate them or just point to the official one or if you want to keep them around, it's like another option. I don't know if there's any, like Benefits to using them or maybe differences in support, that's totally possible, you know, we kind of started.
Small, and probably didn't, like, add everything that the existing ones had, and there may be, like, small differences in behavior, too.
**Aaron Abbott (Google LLC)** 06:18 Yeah, I think… I think that sounds right. I think we've been promoting ones that have native instrumentation over our monkey patch ones. I mean, would you… would you be open to send a PR, Felix?
For…
**Felix Becker (Anthropic)** 06:29 Yeah, I'm currently, I'm waiting for a legal sign up for the CLA. That's why I haven't sent any PRs.
**Aaron Abbott (Google LLC)** 06:38 you.
**Felix Becker (Anthropic)** 06:39 Yeah, once that is through, I'm happy to set PRs.
**Aaron Abbott (Google LLC)** 06:45 Okay, no problem. Feel free to open issues or whatever, too.
**Liudmila Molkova** 06:50 Great that you can come without legal approval.
**Felix Becker (Anthropic)** 06:53 Yeah, I mean, I'm sure you guys know how it is.
**Trask Stalnaker (Microsoft Corporation)** 07:01 Cool, well, let's kick off, the agenda.
We… Got a few things. I wasn't sure… there's also this next here, but I think this is… there was a next for stabilization, so I took that.
**Liudmila Molkova** 07:22 Yeah.
**Trask Stalnaker (Microsoft Corporation)** 07:23 That's correct.
**Liudmila Molkova** 07:25 The other topics were on the agenda yesterday, and we didn't get to them, and they don't seem related.
**Trask Stalnaker (Microsoft Corporation)** 07:33 Cool.
So, let's see… Tatsuko, we've merged one review… Card unknown modality.
**Felix Becker (Anthropic)** 07:56 Do we have like a change log for any breaking changes that we are making?
Through this process, because I know we discussed a lot of breaking changes maybe for this stabilization effort.
**Trask Stalnaker (Microsoft Corporation)** 08:11 So, all of the PRs do, we have not made any releases out of this repo, which is why you haven't seen a changelog, but it is here.
On.
So, when that we do… make a release. All of this is what will populate our changelog, so you can see the breaking…
**Felix Becker (Anthropic)** 08:37 Okay.
**Trask Stalnaker (Microsoft Corporation)** 08:38 images.
**Felix Becker (Anthropic)** 08:39 But we don't right now.
**Trask Stalnaker (Microsoft Corporation)** 08:43 We don't have a changelog file.
**Felix Becker (Anthropic)** 08:46 Yeah. I I guess, like, I can just have Claude in mind that commit history. We just I just need to make sure now that now that we're launched, we have to, you know, up to probably version things, or… and it's, like, an API thing, so you can't… it's not just, like, gated on, like, upgrading your SDK.
**Liudmila Molkova** 09:06 Do you have, What is the baseline? Like, what… do you know the version or Kamicha or something of the thing that you depend on?
**Felix Becker (Anthropic)** 09:17 Yeah, we documented the commit shot in our docs. So we're just saying like we're implementing this exact commit. And I think I threw out the private beta. I bumped it up twice.
But, yeah, now… We couldn't bump it without, like, breaking… Customers I have built, like, dashboards. Oh yeah, it's, E57C from September 24.
**Liudmila Molkova** 09:46 Very, very particular. I'm thinking I have a draft PR for the migration.
But… It's… the baseline is what we have released last in Semantic Conventions repo.
And it would miss all the intermediate steps.
We can, in theory, document the intermediate steps as well, based on the change log.
But, like…
**Felix Becker (Anthropic)** 10:14 Sorry, what do you mean with intermediate steps?
**Liudmila Molkova** 10:17 So like we introduced some metric, I think invoke workflow in this repo.
It has never been released, and then we probably remove it at some point.
It existed in some Kamicha, but it would not it would be it would be easy to miss it in change log.
Just because the delta between releases, it will never show it up.
**Felix Becker (Anthropic)** 10:43 Yeah, yeah, for now, I think I can just use a commit history, and then once we're stabilized.
We would switch to, like, official kind of version numbers.
And then the intermediate ones wouldn't matter anymore.
**Liudmila Molkova** 10:59 Yeah. And I can general anything that has breaking.
And we have some… I have, like, 90% confidence that we catch All the important breaking changes. Maybe you've had 100 for important.
But, like, this should be relatively… Reliable.
**Felix Becker (Anthropic)** 11:22 Nice, okay.
**Trask Stalnaker (Microsoft Corporation)** 11:26 Okay.
So, okay, so it looks like, Limila, you had… okay.
So, this… Looks like a pretty straightforward, so let's… Get this on our… Let's see… for Friday… Let's get the… that reviewed… Okay, so let's… We'll just add… follow… Conformance, okay.
Okay.
Great.
Mac… And… Mikolaj.
**Max Ind (Google LLC)** 13:01 Yes, so yeah, so I did get a couple of reviews on the PR from… Ludmila, and I think from another person that I'm not sure if the Another person attends this call.
Since last time, the most notable changes are the… Yeah, are the, are the ones outlined here? Mostly just like.
changing the name to from just regular turn to conversation turn, so that that removes some ambiguity.
For some of the SDKs.
And I also clarified the semantics for different operation names. I'm not yet 100% sure if that's worthwhile, but, like, one… argument that I think I brought up.
Last Friday is that… If we don't clarify semantics for different operation names.
Then it's difficult to kinda… know what granularity And.
Like, at what granularity this… these spans should be, should be emitted, because And.
Because now that we combine the agent and expand this.
Sorry, the agent and the workflow. This Kind of orchestration can… Lead to pretty deep nesting if we don't.
clarify every… Condition where the span should be emitted.
So yeah, that I think are the two most notable changes.
**Liudmila Molkova** 14:47 Can we throw another thing into the mix?
It might change not the modeling, but the naming.
So… I appreciate you're giving my AI slop in the other tab.
So, Jess, can you switch to the tab with… In the agenda, where we have stuff for Agent Workflows.
The third tab. Yeah, this one.
So… The hierarchy, just a few lines below.
Alright.
So, the… My AI made a slop on saying that Anthropic uses Turn as the agent loop.
thing.
And I think you're right that.
It was a slope, but if I look into Anthropic documentation.
They, looking at Felix extensively, use Turn as the result of 2 loop.
**Felix Becker (Anthropic)** 16:01 You mean like we put the results, the tool results on the invoke agent, like the turn span?
**Liudmila Molkova** 16:10 Oh, not even… it's not about the tracing, or telemetry at all. Like, in which context do you folks use… Taxonomy. Yeah, taxonomy. What do you call turn?
**Felix Becker (Anthropic)** 16:22 Hmm. I think we are… what our turn is, is invoke agent.
**Liudmila Molkova** 16:29 But…
**Max Ind (Google LLC)** 16:31 Yeah, is it, like, the… like, an agent… like, I don't wanna, like… Now influence the.
The wording, but, like, is it the interaction between the model and the… Pool, or is it between the user and the agent?
**Liudmila Molkova** 16:50 Kind of both.
It seems, according to the docs.
**Felix Becker (Anthropic)** 16:55 like.
**Max Ind (Google LLC)** 16:55 Yeah.
**Felix Becker (Anthropic)** 16:56 If we're talking about managed agents, when the user sends a message, That starts a new turn.
And in that turn, we make multiple model requests, handle their tool results, you know, make another model request, until there is a stop point, and then the turn is paused. So, in the context of managed agents.
It's… I guess it's the interaction between the agent and the user.
**Liudmila Molkova** 17:30 In the context of agents, yeah. So, like.
**Felix Becker (Anthropic)** 17:34 But in the context of the messages API, for example, it is… you just… that's, like, more low level, right? So you just send one… you ask for one message from the model, and then when there's any tool call, it stops, and so then that turn is over.
**Liudmila Molkova** 17:50 Or it executes server side tools. Yeah. And it's also called a turn when server side tools are all complete. Yeah.
**Felix Becker (Anthropic)** 17:58 I guess in that case, it's actually consistently just like the user to agent interaction.
**Liudmila Molkova** 18:06 Or…
**Felix Becker (Anthropic)** 18:07 One turn is, like… the agent will keep running until there's, like, a reason for it to stop, right? Like, I need tool approval, or, like, it's, like, done.
**Liudmila Molkova** 18:23 Okay, so I'm… let's maybe not dive too deep into the, word, but I think we miss one layer there, which is a React loop.
And… sorry, Aaron, just finishing my thought.
And within one Invoke agent, you could have multiple turns?
I don't know how to call them, turns, or steps, or whatever.
that are… Don't have to be sub-agent.
It can be… like, review tool loop, and we've been, like, we had requests to have some way to represent a React loop as a span.
So, like, we should expect One more layer?
In this hierarchy. And my key question is.
Would we also call it turn?
**Max Ind (Google LLC)** 19:24 I'm not familiar what the React loop is.
**Liudmila Molkova** 19:28 It's your call LLM span, like do inference and do tool calling until you're done.
**Max Ind (Google LLC)** 19:35 Oh, so it's like one LLM call, and then it goes to a tool call, and then it goes to an LLM call, and then it goes to a tool, or it's just like, okay.
**Liudmila Molkova** 19:45 Until LLM calls… says stop, or fails, or whatever.
**Max Ind (Google LLC)** 19:49 Okay, that to me is kind of like a… what Invoke Agent already is. Like, a single Invoke Agent span can have multiple Can have, like, a… You know, an agent loop where they were, like.
Just calls the tool, calls the… inference, and then this inference may just stop. It may have, like, finish reasons set, or it may call for another tool invocation.
**Liudmila Molkova** 20:17 Yeah, sometimes this… the model libraries do the tool… the loop for you, right? And calling it invoke agent blindly would be.
**Max Ind (Google LLC)** 20:28 Hmm.
Yeah.
Just one more note, I… maybe… so, so I… I think that maybe, like, the conversation turn, instead of just calling it a turn, because I agree that turn is ambiguous by itself.
But would conversation turn?
disambiguate this enough.
**Liudmila Molkova** 20:54 I don't know, but I'm curious what Aaron and Felix think.
**Aaron Abbott (Google LLC)** 20:59 Felix, were you going to reply to that? I was going to ask a slightly… Different question.
**Felix Becker (Anthropic)** 21:04 I wanted to add two points.
One, on what you just asked, we… conversation is already a term in the conventions, right, with GenAI.conversation.id, which… There, the semantic of one conversation is… I think it can be both like an agent level session or one like underlying, you know, low level messages conversation. So that might be a bit tricky to like create clarity through that.
The other term I could throw in here, we have a separate term in our API, we call… in the messages API, we don't call it turn, we call, when there are server-side tools, we call them, we… we call them iterations, so just, like, the server-side tool loop, each of those Like, there's a tool call, just get the response and make another call, like, that is one iteration.
But then… a turn is more, like, our term in managed agents for the user-agent iteration. So, like, inside one turn, there can be multiple iterations with the model.
So maybe that's some wording that could work.
**Aaron Abbott (Google LLC)** 22:28 Yeah, I don't wanna… I was just gonna ask, kind of, about the human in the loop. I think a lot of frameworks represent it as tool calls, and I think in MCP, it can also be surfaced that way.
In which case, if I understand right, it wouldn't actually break out of the React loop, it would just be, like, a blocking tool call?
Does that… Does that work with this model, like, with the proposal here?
**Liudmila Molkova** 22:54 I think it depends on the implementation. Sometimes it's blocking, sometimes it escapes the loop and just returns you the Like, interruption, and you need to resume it later.
**Aaron Abbott (Google LLC)** 23:06 Yeah, yeah. Maybe, maybe we should just… I can just leave a comment on the PR, make sure we handle it.
**Liudmila Molkova** 23:15 Yeah.
I think that… We can call it anything, But then, do we need a distinction, whether it's a Genic turn?
Or it's the… Model level turn.
Because the… the ambiguity exists.
**Max Ind (Google LLC)** 23:37 Yeah.
**Liudmila Molkova** 23:38 I.
**Max Ind (Google LLC)** 23:38 I mean, I think that the… Because I want there to only be… One handle conversation turn per, like, a.
for, like, a trace branch. Like, basically, a handle conversation turn cannot be parented by another handle conversation turn. And I think this is not, like, a… like, I… I think that.
We can piggyback, kind of, off of the is nested.
attribute, because it's nested already requires some context propagation. Either within process or cross-process.
So we can just have the rule that, handle… Conversation turn just can never have is nested equal to true.
And then… Because it is kind of like a… Difficult question because you, you, you really don't know what your Agentic system.
Interacts with, you don't know if, like.
You have a framework, and this framework is being called by another framework, or, like, maybe two agents are talking in a… Slack channel, or something, and then, you know, then the ambiguity… and it's also, like, difficult to implement this, because you don't know if… When, like, a user… Is interacting with your agent, or when another agent is interacting with your agent?
So… What I propose is that the handle conversation term would just be, like, an entry point to a framework, or like a platform, or something.
And then the… whatever is the turn is… no.
Something interacted with this.
With this… framework or a platform, and then this initiated the turn, and whenever the platform or the framework handed control back to whatever called it, that's the end of the turn, as long as the turn wasn't opened beforehand. So, so… Hope that that, kinda… Mitigates the… the confusion.
**Liudmila Molkova** 25:53 But we would report the same metric for all of them anyway, so why… Yeah. Not let them nest to be nested under each other.
**Max Ind (Google LLC)** 26:00 Yes.
**Liudmila Molkova** 26:00 It's.
**Max Ind (Google LLC)** 26:01 So, for them… so, I think that… Nesting them is not… So, because really the point of this is to not proliferate A bunch of spans that just do orchestration.
So, do not, like, add verbosity to the spans. And so that, no, You know, the… and the point, the original point of even introducing this is to make sure that there is, like, one root span that captures the duration of the execution… that's, like, broader than just agents, because, like, if you have two agents and then they're, like, siblings, you don't have the end-to-end duration capturing the metrics. But if you have one turn.
That, at least gives you, like, a an opportunity to have end-to-end duration, but if you define it too vaguely, that anything can be a turn, and you can… you always emit a turn when there's, like, an orchestration layer, then you get a lot of verbosity, so… So that's also not… not good.
**Trask Stalnaker (Microsoft Corporation)** 27:14 Just wanted to clarify that, In your proposal of only having, a route… That is a local route, not a full distributed trace.
Root.
Meaning, I'm hoping we don't need And at least initially, we don't need to, get into propagating things over baggage to, like, do globally unique across the trace.
**Max Ind (Google LLC)** 27:46 yeah.
**Trask Stalnaker (Microsoft Corporation)** 27:46 unique within the local process is something we've done before and would be okay.
**Max Ind (Google LLC)** 27:54 Yeah, yeah, I think that locally within the process… I think, like, on one of the meetings, I think Ludmila, you said that, like, yeah, we need to first solve this problem within process, and then You know, eventually, maybe cross-process, but yeah.
**Trask Stalnaker (Microsoft Corporation)** 28:18 Surya, yeah.
**Surya** 28:22 Yeah, so I'm trying… I'm just lost with the hierarchy. So, when you start a session, every conversation that you have with a local agent is going to be a handle turn.
if this convention is going to be implemented. Did I get this right?
**Max Ind (Google LLC)** 28:40 every, I didn't quite get that. Every, you know, every.
**Surya** 28:46 Yeah.
**Max Ind (Google LLC)** 28:46 I'm your.
**Surya** 28:47 question.
**Max Ind (Google LLC)** 28:48 one call to an Agentic system and then it responds.
Do you? That would be 8 or 9.
**Surya** 28:55 Yeah.
Yeah, handling that.
**Trask Stalnaker (Microsoft Corporation)** 28:58 the.
**Surya** 28:59 the.
**Trask Stalnaker (Microsoft Corporation)** 28:59 Surya, just to clarify, the… if you're invoke… if you're calling the agent directly, you wouldn't introduce a synthetic handle turn.
**Surya** 29:11 Yeah.
So, the next question is, How are we going to distinguish, When a user is calling an agent.
And, when a user is asking a question or something. So, in my mind, if I ask Codex or something, a question about a code base, I believe that's a handwritten.
But say, if I summon a code review agent to review a code, that is going to be an invoke agent directly, and We have to distinguish the operation that the user is doing.
To see what kind of.
span, we have to tag that action to. Is this understanding right?
**Max Ind (Google LLC)** 29:59 Yeah, I think that… so I don't know the, you know, so I don't know if you call, like, coding agent in Codex. I don't know if this coding agent can then call, like, a sibling agent before handing the control to you.
If.
**Surya** 30:14 Yeah.
**Max Ind (Google LLC)** 30:15 Yeah, if Codex can do that, then I would say that, you know, this should be wrapped in the handle turn, like the interaction of both of these agents. But if the Codex… if Codex reliably can know that, okay, user called this agent, and this agent is the only thing that's gonna be Running during… before handing.
**Surya** 30:36 Yeah.
**Max Ind (Google LLC)** 30:36 user, then there's no need for the extra span. And then they can omit the conversation turn.
**Liudmila Molkova** 30:43 exemption.
**Surya** 30:44 Bad one, sorry.
Sorry, sorry, Ludmila, go ahead, sorry, sorry. I just was saying my example was a bad one, but yeah, go ahead, sorry.
**Liudmila Molkova** 30:52 I mean, even in the case of Codex, or any harness, I would imagine that harness would always create the outer span.
Just because it wraps whatever user passed, and any additional logic that it may have.
And… It would exactly be the handle turn.
And then… It would have possibly multiple engines underneath, so it would in they would be captured as turns with agent flavor or turns with workflow flavor, or Turns was… Whatever. No flavor.
And it's fine for them to be nested?
And.
A.
Yeah, so whenever you have some meaningful piece of work that produces output.
If it's the final output to the user, it's the top-level turn.
If it's some intermediate step that's not visible to end user, but some… something did it, like a subagent?
Then it's… Also turn.
**Max Ind (Google LLC)** 32:11 Yeah, but, would this, like, so calling this sub-agent return, would this emit a… Would this emit a handle conversation turns fun?
**Liudmila Molkova** 32:21 No, no, because Invoke Agent is a Turns Pan.
**Max Ind (Google LLC)** 32:24 Yeah, yeah.
**Liudmila Molkova** 32:25 You need it once. If you don't need… if your operation Is scope to a single… thing. You either do the thing yourself and then emit the span, or you delegate and don't emit the span.
**Max Ind (Google LLC)** 32:39 Yeah.
**Liudmila Molkova** 32:47 Yeah, I agree.
**Felix Becker (Anthropic)** 32:48 We have, for us, the turn is the same as invoke agent.
Like, invoke turn is the same as, invoke agent.
**Max Ind (Google LLC)** 33:00 Okay, is that the case or a sub… is for subagents as well? If, like, an agent delegates a work to a subagent, is that now an agent creates another turn?
**Felix Becker (Anthropic)** 33:13 I can see… I think that would make sense, yeah, because the main agent is invoking the subagent, right?
**Max Ind (Google LLC)** 33:26 Hmm.
**Liudmila Molkova** 33:29 I want to poke at you, Max, because you also have a PR that introduces a step or a node.
**Max Ind (Google LLC)** 33:35 Yes, yes, yes. I do, but… Yeah, yeah. I have the… that's… these are two very vague concepts, it seems like, and I wanted to, like, push this one first, because this one… Actually, like, because basically we implemented some metrics for this, like, end-to-end duration and end-to-end metric counts, so this, handle conversation turn thing would actually, you know, be… have a use case right now, whereas this, like, step just has theoretical use cases.
**Liudmila Molkova** 34:10 Yeah, I just mean, that we, like, it seems there are two… layers, if you will. The one is the one that produces the message to user or to caller, whoever the caller is.
And another one is some operation within. It can be an inference call, it can be, input sanitization or something.
And, I kind of want to draw the line between them.
And then… I think I have it in my, in my manual model, I just.
Wanna see… What am I missing? And this Agentic Loop turn.
I kind of want to find an answer for myself whether it's a turn or it's a step or it's some other beast we don't know yet.
**Max Ind (Google LLC)** 35:06 Yeah, well, first I, I.
Kinda.
don't… Like, calling everything a turn? Like, ev… like a… it's like… To me, like, if a user calls an agent, and this agent calls something, like, you know, if it delegates work to a subagent, I would say that that's still part of a single turn.
And then… Just whenever this Agentic system hands control back to whatever it's, whatever was invoked, whatever invoked it.
That… that is one turn, and now if… If this Agentic system was itself invoked by an Agentic system.
That's still part of a single turn. Like, you know, the turn ends when the… when we leave the GenAI world.
**Liudmila Molkova** 35:55 Well, the turn is subjective. It's relative, right? It depends on who you are.
**Max Ind (Google LLC)** 36:00 Yeah, yeah, so they're, like, you know, there's, like, many layers, so, you know, so if you have, like, a… like a hosting for agents.
If you call this hosting for agents, that's a turn. If you call now the framework which handles the request underneath, that's That's, you know, still part of the same turn as the hosting platform, and then the, Yeah, and then the… whatever sub-agent delegation is still part of the same turn, like, whatever loop, Agentic loop underneath, or React loop, still part of the same turn, so this should have, like, one handle turn.
Span.
Probably. I was like.
**Liudmila Molkova** 36:41 Fractals. You zoom in, and there is more and more and more.
**Max Ind (Google LLC)** 36:46 Well, I, I don't know. I would… yeah, I would probably… because, like.
You know, I would say that there are, like, some entry points But, like, you know, when, like, we are working on the framework, And so, like, we… You know, some caller calls us.
us as the Agentic Framework, and then we… at some point, we stop.
doing GenAI stuff, and we hand the control back to the caller. Now, if this caller is the user, and they're interacting with us directly, then we emit the handle conversation turn span. If this something that called us is itself a GenAI system, then they would have the handle conversation turn span. And we would not omit this, because we don't need to, we… you know, the… the, like, the end-to-end duration is already captured in the whatever called us, basically.
**Liudmila Molkova** 37:42 I… I think we're talking about the same… the same thing, but I kind of don't understand why I should care who called me?
Except for this one attribute that we would decide how to stamp.
Like, all of my telemetry, you can look at it as me being the top-level thing, or somebody else being the top-level thing. Like, if my team, who writes me as an engine, cares about only my house, then… they don't care, like, about people who call me. Sorry, stupid analogy. Anyway, but, like, you can look at the agent telemetry without knowing how it's called, and it would be meaningful. And it wouldn't change if you look At it as a part of the things.
That called it.
**Max Ind (Google LLC)** 38:33 10, Can you have, like, a metric for end-to-end duration of a GenAI system if there is no, like, one route, which, you know…
**Liudmila Molkova** 38:47 We would have the way to distinguish the top level within the process, right?
**Max Ind (Google LLC)** 38:52 It's just one attribute.
**Liudmila Molkova** 38:54 Yeah, yeah, some form of it, yeah.
**Max Ind (Google LLC)** 38:56 Yeah, so that's, like, basically what I'm… I would suggest the… turn would be. Is that, like.
whenever we enter the GenAI world, the turn begins. Whenever we leave, the turn ends. Whenever we hand control back to whatever called us. That's not… Oh, pardon?
**Liudmila Molkova** 39:18 By who?
**Max Ind (Google LLC)** 39:19 contracting.
**Liudmila Molkova** 39:19 The span type and metric name would be… Wouldn't have turn if we call it turn, unless it's just an operation name.
Which is done fine.
**Max Ind (Google LLC)** 39:30 Yeah, I think it's… right now, it's the operation name. I'm… I'm pretty comfortable with having.
**Liudmila Molkova** 39:36 Oh.
**Max Ind (Google LLC)** 39:36 operation, Emil.
**Liudmila Molkova** 39:37 I see, you call it invocation, because you call the metric and span invocation, right?
**Max Ind (Google LLC)** 39:42 Yes.
**Liudmila Molkova** 39:42 So we're talking about two different namings. The one is 4 ml, that's for metrics,
**Max Ind (Google LLC)** 39:50 And.
**Liudmila Molkova** 39:50 And another one is operation name, which is more flexible.
**Max Ind (Google LLC)** 39:54 Yes.
**Liudmila Molkova** 39:55 The discussion was…
**Trask Stalnaker (Microsoft Corporation)** 39:57 Yeah, yeah, if you can rewind and explain that again, because I think I missed that, too.
**Liudmila Molkova** 40:03 Can you scroll up?
**Trask Stalnaker (Microsoft Corporation)** 40:04 Yeah.
**Liudmila Molkova** 40:05 There's a table in the beginning. So there's a span name, which has operation name in it, right? This one. And there is a metric.
**Felix Becker (Anthropic)** 40:13 already?
Oh, is this?
**Liudmila Molkova** 40:16 The operation name?
**Felix Becker (Anthropic)** 40:18 Handle turn span name.
**Liudmila Molkova** 40:20 No, it doesn't.
**Felix Becker (Anthropic)** 40:21 Okay.
**Liudmila Molkova** 40:24 So, this is the proposal, and based on your PRMX, the metric is invocation duration, and the span type is invocation as well.
I… Think we need to.
Anyway, so there are two different things. Trask, does it explain the point?
**Trask Stalnaker (Microsoft Corporation)** 40:52 Yeah, I guess I was a little lost on why the, the span structure would be different whether you are, like, to Liudmila's point, generally you don't know who your caller, you don't know anything about your caller.
And so… We would typically have that same, like, span structure, and so if it makes sense to have a handle turn at a point, you know, as a grouping, thinking spans, like, I understand your concern about metrics, and, you know, how do you… how do we sum up metrics, and… But I think we can tackle that as a separately.
We have some strategies to… because that's a common problem where we have, like, nested message processing spans kind of a thing, so we have some other strategies for addressing the overlapping metrics.
So, within the SPAN structure itself, it would… Be most conventional to just have, like, a kind of defined span structure, and not for that to be reliant on who the caller is.
**Max Ind (Google LLC)** 42:10 And I think.
**Liudmila Molkova** 42:11 We… we just miss… I just was misunderstanding Max all this time, because I thought it means there will be different semantics, but it seems what you're saying, Max, that semantics is the same, but operation names are different.
**Max Ind (Google LLC)** 42:25 Semantics with IIF, I don't know if that's.
Like evil what I did, but I introduced semantics for different operation names.
And I also introduced semantics when to not emit the span, so, like.
The handle conversation turn.
I would say would not be omitted, if… There's already a handle conversation turned open. Now, I hear that this is… And.
That this is… not, preferable? That, like, the… so, like, a given… you know.
something, like, you know, if we instrument, like, a given entry point to an Agentic framework, then it should either never emit the… this span, or it should always emit this span, but not emit this conditionally on, like, the color.
**Trask Stalnaker (Microsoft Corporation)** 43:17 So, we do have some strategies in some instrumentations to suppress like, say, HTTP server span, sometimes we have nested HTTP server spans, and so we do have some abilities to suppress nested, the… that level of nesting.
Usually that is direct nesting, though, where you have Message processing libraries, wrapping other message processing libraries, and there's… there's nothing really in between those, so that's just… Noise, duplicative information, which… I'm not sure… this doesn't quite feel the same as that, because there's intermediate spans, and so that structure… that local route, or that… that… that handle turn still has some structure to it. It still wraps some other… child spans.
**Max Ind (Google LLC)** 44:24 Yes, yes.
Yeah, that that's a good point that like.
And.
Well, the span would basically, depending on the method, how you call.
There's something… it would either… it would, you know, change the trace structure in, like, a non-obvious way, unlike the HTTP just Not being double emitted, That's a worry, like I, the other side of the coin is that, Well, then it's kind of difficult to know.
When to emit the span because you can.
You can emit this span at, like, basically arbitrary layers.
At which orchestration happens, so that, like.
No, like, an entry point is kind of…
**Trask Stalnaker (Microsoft Corporation)** 45:23 I thought that was sort of the point of the handle turn span was to group orchestration that isn't really like didn't quite fit invoke workflow and didn't fit invoke agent, but is some other kind of orchestration that groups.
**Felix Becker (Anthropic)** 45:42 What is that kind of orchestration? Like, is that just… Like, the kind of edge intake, or…
**Max Ind (Google LLC)** 45:52 Yeah, yeah.
**Felix Becker (Anthropic)** 45:53 Like in our span schema, for example, you call like post v1 sessions events.
and you post a new user event, and that gets just, like, a regular client and server-side kind of HTTP span, that's just the route handler for that. And then that triggers a turn inside the agent, and so… Would that outer server span now be… handle… turn, or would that be, like, an intermediate layer? Because there… I guess in our case, there isn't a lot that's actually happening, except, like, in queuing the message and waiting for the agent to, like, pick it up.
**Max Ind (Google LLC)** 46:33 Yeah, yeah. So in ADK, we kind of have the issue where we have, like, a runner of agents, and that's just, like, a in-code construct that someone calls, right? And then this, this runner does, like.
And.
like, you know, callbacks, and then it hands control off to an agent. And then this agent may finish execution, but it may finish execution by… with, like, a message that, like, directing the framework to hand control to another agent. And then this… Agent which receives control is a sibling to the Original agent, right? So then we have two, kind of, we have two spans.
That are siblings, with no shared root.
And we basically cannot, capture the, you know, the end-to-end duration of this entire Agentic system. We can only capture end-to-end duration of the first agent, and then the second agent, if there is a handoff. And then.
For now, we've been calling this, you know, orchestration.
of, two or more sibling agents. We've been calling that Invoke Workflow.
But this is… this is confusing because the user actually never created a workflow, this is just a code construct provided by the framework to handle agent orchestration, right?
So, we are looking for another name of what to call this. And actually, this problem only exists if.
If, you know, if there's no… overarching span for the… for this agent handoff problem. If there's… there's a, like you said, there… you… it's… I hear that you have, like, the HTTP server span, right? So you can get the duration.
from the HTTP server handling the spam, but in ADK, we don't know who called us, and we don't know if that's a HTTP server, if that's a RPC server, we don't know if that's, like.
Just like a shell process or whatever. So there's no consistent way to know end-to-end duration.
**Felix Becker (Anthropic)** 48:52 So maybe what this actually is is more like dispatch turn, right? It's not like handling a turn like after it happened, it's like dispatching one.
**Max Ind (Google LLC)** 49:01 Yeah, that sounds better, that sounds… yeah.
**Liudmila Molkova** 49:06 That that thing produces the master trade.
That to user, back to user.
**Max Ind (Google LLC)** 49:12 Yeah, back to whatever…
**Felix Becker (Anthropic)** 49:15 Creation of that span for basically does it enclose the turn span underneath?
Because in our case, like, the HTTP request is, like, async, right? Like, it finishes immediately, and then the actual turn is, like.
Async.
We do report it as a child, but it'll just like continue on past.
**Max Ind (Google LLC)** 49:33 Yeah, yeah.
So if you hand control to the user immediately, then that would In our world, that would end the turn span.
**Trask Stalnaker (Microsoft Corporation)** 49:48 Max, back to why, I'm curious why you don't want to just always emit the handle turn.
For example, if you have an HTTP overarching HTTP server.
if you don't omit the handle turn, like, it's still a nice logical grouping, like, what if you have two, you know, two of these turns within an HTTP server request? Like, there's still a nice… Semantic meaning there.
Are you… are you just concerned about the noise of those? And how… how noisy do you think, like.
I'm not… at this point, I'm seeing them as… Like… If there's already gonna be, you know, multiple, inference and tool calls under each one of those.
Like, if it's already, like, a 1 to 10 ratio, like, you know, it's not that noisy, or are you thinking that there will be, like… maybe you could… And maybe we should probably try to wind down here and have some follow-ups for Friday.
Maybe you could kind of bring… back, thoughts on why, like, what is the noise concern there, or how noisy are we talking about? So we can make some sort of… Because it's true, we do make those subjective decisions in Semantic Conventions sometimes based on, you know, we do try to limit noise.
**Max Ind (Google LLC)** 51:27 Yeah, yeah, my…
**Trask Stalnaker (Microsoft Corporation)** 51:28 understand that better.
**Max Ind (Google LLC)** 51:29 Yeah, I don't have any empirical data. I can try to gather some. That's a good idea to, like, basically try to see if we implemented this, like, take some… production, you know, agent system, and then see how many additional spans would be created. That's a great idea.
**Felix Becker (Anthropic)** 51:51 It would also be great, like, to understand if there's another… Like, another vendor that would make use of this spend, too.
Cause you, you can always omit your own spans, right? But like standardizing it, I think it's always best when you have like at least like one other case so that you make sure.
**Max Ind (Google LLC)** 52:10 Yeah.
**Felix Becker (Anthropic)** 52:11 It's not like overfitted.
**Max Ind (Google LLC)** 52:13 Yeah, yeah, I've seen the… there are examples in the proposal where we also… because there are other vendors, for example, like.
I don't remember the exact details, but there's, like, Crew AI, there's Microsoft Agent Framework that… Microsoft Agent Framework also has the concept of a runner. And this runner.
I believe can have agent handoff, and this, I know there's a case where a runner Is currently represented as a, as an invoke agent with no name.
And I know that this example is somewhere in here, but I just forgot which framework this refers to.
But yeah, it, it, I… I have made sure to, like, yeah, not overfit to the, to the, just the ADK example by finding other, other examples that, in other frameworks that could, could use this, yeah. Yeah, the… Back to the… To the handle turn. I… the worry is that, like, because we used to have this wording where, we… so, for example, like, invoke workflow on Trunk currently has the wording that, like, if this is an implementation detail, then don't emit invoke workflow.
And I'm… I don't know… If that's because if that's.
very clear what an implementation detail is, because for some people, the implementation detail is, is not an implementation detail. For some users.
The runner in ADK is an implementation detail, but for some users, this is the entry point. This is what they interact with, right? Yeah.
**Liudmila Molkova** 54:01 Any entry point.
**Max Ind (Google LLC)** 54:04 Yeah, yeah.
you Any… sorry, any entry point is…
**Liudmila Molkova** 54:10 So what we would instrument, like when to meet the span one. One of the flavors of the span is an entry point to agent, to workflow, to your framework that encompassing multiple operations. But not the, the things inside that you, that are noisy and it's subjective. What is noise?
**Max Ind (Google LLC)** 54:30 Okay, okay. Not okay. But then if someone builds, you know, a master framework that, you know, that combines many, you know, Agentic frameworks, then we are, then there are.
**Liudmila Molkova** 54:40 We won't instrument them, we will tell them go away.
**Max Ind (Google LLC)** 54:42 Okay, okay, that sounds… Okay, maybe, maybe it's just, like, I have worries. I'm gonna have, like, an empirical example. For Friday with, like, some agent, and then, you know.
tracing their code and seeing, you know, how many… if we just instrument every single runner, how many handle or dispatch turns there would be, yeah. That's a good…
**Aaron Abbott (Google LLC)** 55:05 Can I make a quick suggestion? Like, we have this tab in the doc with the kind of design. Do you think we could include, like, kind of make it like a mini design doc that we could bring the discussion there offline? And, like, also the motivation, I feel like, is getting lost if we could… Write it down, it would be super helpful.
**Max Ind (Google LLC)** 55:24 Yeah, so move the basically move the PR description into a Google Doc. Yeah, that's that's the proposal. That's.
**Aaron Abbott (Google LLC)** 55:31 6.
**Max Ind (Google LLC)** 55:31 suggesting.
**Aaron Abbott (Google LLC)** 55:33 Or if it's not up to date, like, I feel like I'm having a hard time, like, if.
**Max Ind (Google LLC)** 55:37 Yeah, that…
**Aaron Abbott (Google LLC)** 55:38 Yeah.
**Max Ind (Google LLC)** 55:39 That's fine, that's fine. I can totally do that, yeah.
**Trask Stalnaker (Microsoft Corporation)** 55:47 Cool. I found that discussion really helpful, though. I think.
I feel like we're… Getting at least some common, understanding of, where… People are, thinking on that.
Just quickly, for… so, for… Maybe.
**Liudmila Molkova** 56:14 Felix has dropped, and I think we've been waiting for him, so…
**Trask Stalnaker (Microsoft Corporation)** 56:19 Oh, for this one. Oh, yes, okay, sorry, yes, okay, we'll get that onto the top of Friday… This one…
**Neil Yashinsky** 56:32 I will say, and Aaron, you know, sorry I haven't been able to finish the review. Everything looks good, largely, as you know. I have, like, I have a few notes or whatever, but I wanted to present them in a comprehensive fashion, and so, as I think I mentioned, like, GitHub every once in a while throws me for a loop.
But, long story short, I'll do my best to have that, last bit finished up ASAP.
By Friday, I think, for sure.
**Trask Stalnaker (Microsoft Corporation)** 57:00 Great.
And then I dropped this one on the agenda just as, I'm thinking, Ludmilla, I'll take a look at this, and, try to… I might bring it up one more time, just as a last chance for discussion on Friday or nec… or maybe next Tuesday in the broader audience.
I am Mikola.
**Mikolaj Knap (Google LLC)** 57:32 Yeah, and could for review, could you also put, I think I'll link in the doc 574. I think it's a little bit above.
**Trask Stalnaker (Microsoft Corporation)** 57:41 57457…
**Mikolaj Knap (Google LLC)** 57:45 It's underneath the max. Yep, yep, yep. It's just refinements for skill usage on execute tool and one new metric for.
skill loading for invoke agent. So please and thank you.
**Liudmila Molkova** 57:59 Oh, thank you, sorry.
**Trask Stalnaker (Microsoft Corporation)** 58:02 Well, I'm going to drop in the Slack channel, sort of list of our things for reviewing by Friday, and… Not everybody has to review everything, but tried to take a look at a couple of things.
Thanks, everyone!
**Liudmila Molkova** 58:22 Thank you.
**Neil Yashinsky** 58:23 Thanks, everyone. Have a good one.
**Max Ind (Google LLC)** 58:25 and.
**Liudmila Molkova** 58:25 You too. Bye bye.
**Neil Yashinsky** 58:26 Opposed?

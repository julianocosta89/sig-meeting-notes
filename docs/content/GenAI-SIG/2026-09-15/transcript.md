SIG: GenAI SIG
Date: 2026-09-15
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

Trask Stalnaker (Microsoft Corporation) 00:07:15 Hey, folks!
Leighton 00:07:21 Hello.
Wolfgang Therrien 00:07:21 ask.
Trask Stalnaker (Microsoft Corporation) 00:08:08 Go ahead and, add anything that you'd like to discuss to the agenda.
Object for… Iris.
So this one, this was discussed this morning.
So… Why don't we kick it off with, Ankit?
Ankit Singhal 00:09:24 Hi, I am. So… I've got some good comments on the PR iWater, so I would appreciate, reviewing them again.
And is there a new opening?
comments I'll be happy to address, but looks like pretty close to getting it ready to merge.
Ning goer 12a.
One of the major questions that he brought up was about the, Components, for audio.
Our video can be fitted.
Like, the large, so… I think I did see Elipina had a comment, and this is a known issue. However, like, this PR is just following what is followed for, text models. So, I would like to just… Probably that issue can be handled separately, I think. That'd be great.
of this year.
Trask Stalnaker (Microsoft Corporation) 00:10:32 Yeah, and Ludmila did raise that in the, General Semantic Convention meeting this week.
About the large data attributes.
Ankit Singhal 00:10:51 Oh, that's the points.
Trask Stalnaker (Microsoft Corporation) 00:10:53 Yeah… Alright, or… Pretty dry on topics today.
I don't know, it's,
Surya Teja 00:11:17 Hey, hi, Trask. I have one question.
I paused working on A2A since we are working on the standardization of the semantic conventions, but if there is some broader interest from the communities.
I can prioritize that and look out for non-invasive ways to push changes for A to A.
So, the PR, I was working on that PR. There are a few open questions.
I have the answers for them, but I paused pushing those because, I just want to give some bandwidth to Ludmila and other folks in, the priorities, semantic conventions, standardizations.
That's so… Yeah, yeah, yeah.
Trask Stalnaker (Microsoft Corporation) 00:12:08 Yeah, so I think… It's a good ask for this group Basically, as we, I think the… Maintainers are probably more… are mostly focused on the stabilization effort.
at this point.
For a comp… for the next… Month and a half plus.
at least, But we do want to keep this meeting open and other topics alive and discussions, proceeding on them. So, yeah, it's great if there's a couple of people, you know, who are both interested in topics, and we can have those, you know, real-time discussions here, and PR reviews can continue going on.
Surya Teja 00:13:03 Yeah.
Trask Stalnaker (Microsoft Corporation) 00:13:03 In the meantime.
Surya Teja 00:13:05 Yeah, I just want to be mindful with the time that others have. Earlier, someone from Splunk was also part of that.
group, and I… I was work… I worked with them, but now Liudmila and Aaron are only folks, and they are also part of that standardization, and I want to be mindful of their time, too.
Aaron Abbott (Google LLC) 00:13:32 I, I, Yeah, I think in this case, like, so Pavel left a review on here, and he was… he's one of the Googlers who was working on A2A and had, like, a proposal for this also, so… You know, like, in this case, when people aren't… he's not an approver, but he's, not working on, like, the stability effort directly, so I… I feel like in these cases, we have subject matter experts, we could probably still make progress on, PR like this, if you have been with Surya.
Surya Teja 00:14:01 Yeah, I have bandwidth, and I will push those, and I'll clean up this a little, and… see how I can work with you and Ludmila also to… get this, to the finish line. There are other peers that are waiting after this metrics and other stuff.
48.
Aaron Abbott (Google LLC) 00:14:21 Okay.
Trask Stalnaker (Microsoft Corporation) 00:14:22 How are they, prototypes? Like, what instrumentations… do we have instrumentations?
That are implementing this yet.
For just the reference instrumentations in this PR so far.
Surya Teja 00:14:38 We, I only included the reference instrumentation. I am assuming that other instrumentation that you're referring to is Google ADK and stuff that are using the A2A under the hood. I believe you're asking about them, and so I'm going to pause to see if that is what you're referring to, to Trask.
Yeah, I did not experiment with the ADK and other stuff. I was only, playing with the native instrumentation. I did not plug in ADK or others that were directly calling the A2A instrumentation.
Trask Stalnaker (Microsoft Corporation) 00:15:16 Okay, cool. Just, thinking of… trying to think of other ways to move it forward, Prototypes… even building out something, certainly in the reference instrumentation, probably you have here, but even a more full, like, draft in the Python GenAI repo could be useful.
Surya Teja 00:15:42 Yeah, sure. Let me see if I can build something that is going to give a better example of how these gel with the semantic conventions.
Aaron Abbott (Google LLC) 00:15:51 Yeah, just one… one thing on… on that is ADA has some native instrumentation, and I think the goal was probably to have these conventions implemented directly in, at least for 8A Python in the repo upstream.
So I think maybe that doesn't block, like, prototyping for the purposes of the semantic conventions, but,
Trask Stalnaker (Microsoft Corporation) 00:16:14 Is 8x8 only, 80K?
Aaron Abbott (Google LLC) 00:16:18 No, no.
Trask Stalnaker (Microsoft Corporation) 00:16:19 Oh, okay. Yeah, yeah. So are there… there's other, potentially other things that we could instrument?
Surya Teja 00:16:26 Yeah.
Liudmila Molkova 00:16:27 There is ATA library, right?
And it can… it is natively instrumented, but com… Whoa.
I'll hold my thoughts on this. But, like, yeah, it can be there, like MCP.
Aaron Abbott (Google LLC) 00:16:48 Yep, in that case, maybe I can ping Pavel, and we can… like, see if maybe it would be worth the effort to open a prototype PR here, but I don't wanna… block you, Surya, so if you… for the purposes of getting this PR through, we want to prototype something in Python GenAI, I think that makes sense, too.
Surya Teja 00:17:06 Yeah. Do you… do you guys think opening up a prototype here on the A2A Python repository, will that add some value?
Aaron Abbott (Google LLC) 00:17:18 Yeah, I can get in touch with the maintainers. I don't think they're all Googlers, because, like, It's an open protocol and all that.
Surya Teja 00:17:27 Yeah.
Aaron Abbott (Google LLC) 00:17:27 I can see if it's something that we'd be interested in, and get back to you, but I don't wanna… obviously, it's a lot of work to have, like, a… PR with tests and everything like that, so…
Surya Teja 00:17:39 I just checked.
Sure, sure, bye.
Trask Stalnaker (Microsoft Corporation) 00:17:52 Cool. Hot.
Hmm.
Moving on… Yay.
I'm Akilah. Hey!
Nikhil Chitlur Navakiran (Microsoft Corporation) 00:18:10 Hello.
I just wanted to, chime in, or check on the PR. I think there were some suggestions, about making it, a refinement on a span, so I just want to know, is that… that the next feedback, or is there any other feedback that… We want to consider on the sphere.
Liudmila Molkova 00:18:44 Why is it A2A, though? It's… it's not… It's not the protocol, right? It's the…
Trask Stalnaker (Microsoft Corporation) 00:18:51 Right, it's… Agent to agent.
Nikhil Chitlur Navakiran (Microsoft Corporation) 00:18:53 Yeah.
Trask Stalnaker (Microsoft Corporation) 00:18:54 Not A2A.
Yeah, trademark.
Nikhil Chitlur Navakiran (Microsoft Corporation) 00:18:58 Maybe… let me rephrase that.
Liudmila Molkova 00:19:05 Th-th-this, this is fine, but yeah.
Nikhil Chitlur Navakiran (Microsoft Corporation) 00:19:08 Okay.
Liudmila Molkova 00:19:09 But… yeah.
I think this is my main feedback. I don't remember if there was any other things I commented on, but if you don't see other comments, then that's probably the main one, I… like, I cannot promise that I won't have other comments, maybe more cosmetic ones.
Yeah, sure, yeah.
Nikhil Chitlur Navakiran (Microsoft Corporation) 00:19:33 Awesome. So, I think the… I was looking into the refinement piece a little bit more, so, from what I understood, like, if we want to make it a refinement, then we want to… Say, maybe, like.
The changes that we are making are, we did, specific to agent-to-agent interaction, so do we want to call it.
Out that way.
Let me rephrase. So, so now we've added, on the execute tool specifically, we've added parameters or attributes to denote both, agent and non-agent transfers, right, for transfer to user or transfer to an application.
So, with a refinement, do we want to… if we use the refinement route, do we want to make it more… Specific to an agent-to-agent transfer.
Or can it be… or, I guess two questions. First, we… do we want to make it a refinement? And second, if we do make it a refinement, should it be specific to an agent-to-agent transfer?
Liudmila Molkova 00:20:46 This is a tool call.
Right? So we are describing something that's a tool.
And… It… Unless there is some other mechanism.
we should… Whenever we define… we say it's a tool call, we should refine the execute to span, because this way we keep the… Saying that it's a toecall.
Right? For A to A.
think… There are… It's probably our tuggernaut to this question. Maybe, Surya, you would know if A2A communication happens inside to a call or in some other way, but that's essentially the… Not the… The thing that we capture here, right?
Data would capture that something caused an agent.
Surya Teja 00:21:44 Yeah. Agent Card or something.
Something, but I'm not sure on top of my head, let me laugh.
Nikhil Chitlur Navakiran (Microsoft Corporation) 00:21:52 Yeah, so for the, that's, that's a good point, so I wanna, expand on that also, but, specifically for execute tool, so… Is the recommendation that… We want to make this a refinement, or should we have it as optional parameters on the main span?
Liudmila Molkova 00:22:18 And I think we should have it as a refinement, and the reason is, I'm just posting, there is a PR that I want to also talk about, if we have time, the skills, which are also, tool executions.
So there is a set of specialized tools.
That, and the list is long, right? There is, I don't know, web search, or… well, that's a server side. Anyway, so there is a list of specialized tools.
that have their own conventions, and if we model all of them as execute 2 as optional parameters, it would be just a bag of crap that nobody knows how to properly write, we cannot validate the span, we cannot coordinate the span, and it's just all a big mess.
Nikhil Chitlur Navakiran (Microsoft Corporation) 00:23:04 Got it.
Agreed, yeah, so I can make that, update. And I guess this, so I guess those were all my questions on ExecuteTool. So.
for the A2A protocol, I have a… I have a, scenario example over there, which… which, speaks about, the Google's, Google's ADK internally using A28 protocol, and I've modeled it as an, Invoke Agent client span, right? With the… with purely the existing Invoke Agent client span.
So, is that… I just wanna, check, so if that is how you… You know, plan to model it in the future as well.
Liudmila Molkova 00:23:58 It's a good question. It seems that something is kind of missing in this picture, so there is an invoke agent source, an invoke agent target, but there is nothing that says, okay, the source handed it over to target, right?
Nikhil Chitlur Navakiran (Microsoft Corporation) 00:24:14 Right.
And that is where, the invoke agent client spans, which uses the A2A, I thought, might be a good fit.
Liudmila Molkova 00:24:31 I think it's not a question of modeling, but a question of reality, like, what happens in the reality. It doesn't have to be Italy, it can be anything.
And A2A does not have invoke Agent operation.
At all.
Nikhil Chitlur Navakiran (Microsoft Corporation) 00:24:51 Correct. It doesn't.
Ankit Singhal 00:24:54 Oh, please.
Nikhil Chitlur Navakiran (Microsoft Corporation) 00:24:56 Right, it doesn't. It is more about, denoting the… So… In scenarios that we see quite often, where we don't have the, target telemetry. So, we, we can use the invoke agent on the caller side to.
in the A2A process to denote that, hey, this You know, there was a call to invoke another agent.
Liudmila Molkova 00:25:32 Yes, and maybe there is something else in the ADK that… Handles the state transfer processor, and whatever happens there.
That… where we can record that it's actually that the target is invoked because of the… because source requested it, and not because it's just that the workflow decided it this way.
Maybe it's an event, maybe it's some other way to capture this.
So maybe… I think… Ankit, I would let you go in a sec.
Maybe we say that Errh If we don't have a good Case or need for this part.
like, the direct calls. We know that the execute tool is a common pattern.
Maybe we just say, okay, we do this as an execute tool.
And… If we see the… A real case where the… That this is happening.
we would… cover that Some, some, somehow else.
Nikhil Chitlur Navakiran (Microsoft Corporation) 00:26:48 I see.
Liudmila Molkova 00:26:51 Are you even interested in this case?
Nikhil Chitlur Navakiran (Microsoft Corporation) 00:26:55 That non-tool case. Yes.
No, we're interest… I think we're interested in both, cause… We do see, There is non-tool-based handoffs in some of the examples.
Like, internally that we are running.
So, in… in those scenarios, Like, to record that a remote agent was invoked, we would need some sort of a… Like, span to capture that.
Liudmila Molkova 00:27:38 Okay.
Yeah, I have some thoughts, but Ankit, go ahead.
Ankit Singhal 00:27:48 This scenario would be true for any remote agent invocation, right? No matter.
Nikhil Chitlur Navakiran (Microsoft Corporation) 00:27:54 Correct.
Ankit Singhal 00:27:55 8-way versus… enable protocol. And then, the part, like, here, I think we can definitely segregate out, like, probably one thing is… So the invocation of the, remote agent can happen no matter, like, should we all… should we even care about, like, what's actually calling it to model that, like, from the invoke agent client side?
And then the part about, like, who is calling this agent?
is something… That silly question, right? For… Whether it should be executed, whether it should be something else, which shows that this Agent call or handoff happened from another agent.
to worry more data.
Nikhil Chitlur Navakiran (Microsoft Corporation) 00:28:47 Yeah, so trying to… maybe, like, Align with the, what do you say, like, with how it's being used in other platforms? So, yes, executeTool is one of the common ways of representing the transfer.
Between agents, but… So that… that dynamically… or that naturally is happening with… with all the, partner platforms, right? So now.
We also have scenarios where they don't use the, yeah, we don't use the… we don't use a tool call to represent this transfer, right? So, and then, as you said, like, it can be A2A, or it can be just, any other REST API call, that does it. So now, the question is, like.
where do we, or how do we capture that, right? So, in, at least in many of the Microsoft and 3P scenarios that you see, it is, it is Quite common that We don't have, we only… we don't have, like, the full end-to-end instrumentation.
So we… we'll… in cases, we'll not be able to capture the downstream, invoke agent.
Or the target invoke agent. So, the question is, like, does it make sense to… To capture it on the caller side, or as an invoke agent, or are we thinking that we need something else to capture it?
Liudmila Molkova 00:30:40 We can capture those attributes on Invoke Engine target, so if any handoff information was given.
Through a context that we would capture it.
If we can.
Nikhil Chitlur Navakiran (Microsoft Corporation) 00:30:55 You mean an invoke agent in the target process?
Or on the call-up process.
Liudmila Molkova 00:31:03 In the color process. This… this would probably have higher chances of knowing who calls it, and if there is any additional context.
Nikhil Chitlur Navakiran (Microsoft Corporation) 00:31:13 Or, you mean who it's calling, right?
Liudmila Molkova 00:31:16 No, the invoke Agent source can call multiple agents, so it cannot record it there, but the Invoke Agent target Might know who called it.
Trask Stalnaker (Microsoft Corporation) 00:31:29 In booking.
Nikhil Chitlur Navakiran (Microsoft Corporation) 00:31:30 So…
Trask Stalnaker (Microsoft Corporation) 00:31:30 This… this band of milk?
Liudmila Molkova 00:31:32 The tar… yeah, the target would know… may know something about this horse.
Trask Stalnaker (Microsoft Corporation) 00:31:38 Or this… this target.
Liudmila Molkova 00:31:41 No, sorry, in the color process.
Trask Stalnaker (Microsoft Corporation) 00:31:44 Yeah, the invoke agent client span.
should know it's the target, and I… I assume this is… I think this is how it's already specced?
Liudmila Molkova 00:31:57 Yeah, and I guess the question is that it… we don't record the source, we don't know if it was called.
Trask Stalnaker (Microsoft Corporation) 00:32:04 Oh, we don't…
Nikhil Chitlur Navakiran (Microsoft Corporation) 00:32:05 the… Yeah, so the source, since I think it's all on the caller process, I'm… We can rely on, like, the parent nesting, right? Or, To figure out, like, the source is calling the target.
Liudmila Molkova 00:32:24 Only if it's, like, the… the deleg… it's… how did we call this pattern? So, there are two patterns, right? When… The source is blocking, on target, and there's a pattern where it's not blocking.
And if it's not blocking, we cannot tell anything.
Trask Stalnaker (Microsoft Corporation) 00:32:48 Not blocking…
Ankit Singhal 00:32:50 Yeah, it's the handoff scenario, right? The second one is, where all the context control is handed over, and then agent, the source agent is like, okay, I'm done, I've done my job.
Liudmila Molkova 00:33:00 Yeah, I'm…
Ankit Singhal 00:33:01 Like that.
Liudmila Molkova 00:33:02 Target is the next one, too.
Ankit Singhal 00:33:03 Yes.
Liudmila Molkova 00:33:04 take care about it. And then they are siblings.
Nikhil Chitlur Navakiran (Microsoft Corporation) 00:33:10 So, yeah, when I ran that, scenario, like, it didn't… like, the existing scenario… scenarios didn't… Okay, so let me try and understand what you're trying to say. So, in the caller process, I have an invoke agent source.
And then that… so then I have an invoke agent on the target in the caller process. So, what I'm saying is the invoke agent, since they'll be nested parentage, so we will have, so we'll be able to identify the source caller.
So, but you're saying even in the call-up process, we… we might not know the source, and we want to add that source information on the invoke agent client span.
Is that correct?
Liudmila Molkova 00:34:09 Yeah, so sometimes the Invoke Agent client span won't be a child of the source.
And it's the question to you whether, like, we have the information As a part of Handoff.
That would… that we need to capture.
And…
Trask Stalnaker (Microsoft Corporation) 00:34:30 Litud.
Liudmila Molkova 00:34:30 Yeah.
Trask Stalnaker (Microsoft Corporation) 00:34:32 What… what's the case where this is not going to parent?
this.
Liudmila Molkova 00:34:40 So this is the case of, existing SDKs with something like the handoff pattern, where the first agent processed stuff.
And then it says, okay, I'm done. You can configure it as a user, whether it's blocking or not. If you use it as a sub-agent, it's usually a tool.
If you use it as a handoff pattern, it can be something else in theory, but then I'm done, I'm not going to return response to user, I'm just, like, a triage pattern. I… I did my initial triage, and I'll give it to, I don't know, specialist agent that will reply back to user.
And you can simulate it with, like, the in-process agent pretty easily, agents.
Trask Stalnaker (Microsoft Corporation) 00:35:27 Okay, so you, in this case, you wouldn't record it when the agent, the… It sort of… okay, so you wouldn't record it in the client span until afterwards, when the follow-up is done, and it could still be a client span calling it remote.
Liudmila Molkova 00:35:51 Yeah, why not?
Trask Stalnaker (Microsoft Corporation) 00:35:52 Okay.
Nikhil Chitlur Navakiran (Microsoft Corporation) 00:35:58 Got it, okay. So you're saying even though it is in the caller process, we will not have… or, it is good to record the source agent properties on the invoke agent clients one. So I guess this is only a…
Liudmila Molkova 00:36:12 I don't know if it's good. I'm looking at you as a person who knows the use case and, like, the experience you want to provide users, and whether it's useful information. It seems symmetrical, right? So that when the handoff happens.
We record it when it happens through the tool.
But we want, like, at least in this picture, we want to record it if it happens through other means.
Should we? Do we need it? Ed, I think it's helpful, because like… With just the siblings, we don't know what caused what.
Yep. And it would be nice to record, but it's the question of, can we do this? And what information we have in practice with something that… that's, like, not just internal.
Nikhil Chitlur Navakiran (Microsoft Corporation) 00:37:02 Got it. Okay, let me take a stab at that and see if any of the scenarios, have this.
capability, like, so let me take a stab at it, yeah. It makes sense, so I think we do model it pretty. We have both source and target, in our implementation for, for data processing purposes, so we've built in some redundancies into this plan, so yeah, it might make sense in this scenario as well. So let me take a stab at it and do an update.
Liudmila Molkova 00:37:43 Thank you.
Trask Stalnaker (Microsoft Corporation) 00:37:44 Alright.
Nikhil Chitlur Navakiran (Microsoft Corporation) 00:37:45 Thanks.
Trask Stalnaker (Microsoft Corporation) 00:37:46 Question, Ludmila, so in the case where this is, the Invoke Agent client is not parented, because it's sent later.
Is that a technical limitation, or do you think that is correct mod… the ideal modeling?
Liudmila Molkova 00:38:10 So the… Source, edge, and span ends before the target starts, right? It's… Time frame is limited, and it… essentially talks to the runtime, and runtime detects it, sends it, and then runtime handles the handover. So I think it represents the reality.
Could we model…
Trask Stalnaker (Microsoft Corporation) 00:38:35 kind of like… I mean, to me, it sounds more like a queue, you know, like an async queue that… I mean, it doesn't have to… There can be a gap in between.
Liudmila Molkova 00:38:47 Yeah, like, could they be child and parent? Yes, if context is propagated.
how easy it would be to propagate the context.
Trask Stalnaker (Microsoft Corporation) 00:38:56 That was my question, is, yeah, if it's a… just… if it's a technical limitation, or… Because ideally, it feels like… Yes, we are… even if we stamp the source agent name on that span, it still doesn't… Actually, like, even better would be to know the actual invocation of the… that source agent span.
Liudmila Molkova 00:39:21 Yeah, if you could have.
Trask Stalnaker (Microsoft Corporation) 00:39:22 Whether it's via link, whether it's via link or via parent.
Liudmila Molkova 00:39:26 Yeah, and in the case of, messaging, right, we still stamp the QNA.
Oh, some information.
Trask Stalnaker (Microsoft Corporation) 00:39:36 Yes.
Liudmila Molkova 00:39:36 came from.
Trask Stalnaker (Microsoft Corporation) 00:39:37 They're, they're useful, yeah, it's a useful dimension.
Cool.
Nikhil Chitlur Navakiran (Microsoft Corporation) 00:39:49 Awesome. Thanks, thanks, Trask and Ludmila.
Ankit as well.
Trask Stalnaker (Microsoft Corporation) 00:39:54 Yeah, thank you.
Cool, let's go to Dylan.
Dylan Russell 00:40:05 Yeah.
Wondering if we can get rid of this event enabled… flag entirely.
Which is used to gate the, like, inference event.
And right now, we kind of have some weird logic where we check if… The content capture flag, and… Use that as the fallback when this flag isn't set.
Which I think is a little… Like, weird to, like, overload that flag.
Bud.
Seems like maybe we could get rid of it, and… If someone doesn't want the events… if someone doesn't want events at all, they could maybe set, like, a… The logger, it's like a no-off logger.
Or, if they don't want just this event, maybe they could set up, like, a log record processor thing to, like, filter it out.
But it seems kind of weird to have, like, an envar control it.
Liudmila Molkova 00:41:10 Where… I think… where we are in Python on the logger enabled.
Aaron Abbott (Google LLC) 00:41:17 I think we support it for declarative config.
But we don't expose the API to do it programmatically right now. I think there might be a PR for it, though.
Let me… let me look really quick.
Liudmila Molkova 00:41:34 This would be the way, right? So I think this thing existed only because these events could be extremely verbose.
And… because… We don't have any API to check if user wants this event.
And if we had logger enabled, API.
We would check it, and we would tell users how to configure it, but not specifically to GenAI, it's just the event name they can… enable or disable… the, like, the instrumentation scope, they can enable or disable, I think.
And, we wouldn't need this environment variable.
But if we just remove it and turn it to true by default, Where… might increase the volume.
For people, quite a bit.
Aaron Abbott (Google LLC) 00:42:38 If… if we don't have content capturing on, though, it's pretty much… It's true, it would not be sampled, but it would have Just the, like, the attributes that are descriptive and not the actual payloads, right?
Liudmila Molkova 00:42:54 Is it useful, though? So, Ken, maybe we can gait on the… When user enables content on events, That we would record it.
Dylan Russell 00:43:11 But I don't like that. I think that's… That's like overloading the other environment variable.
Aaron Abbott (Google LLC) 00:43:29 So maybe another question is, do we… in the semantic conventions for events, do we say the… Expected level for these, or just in general?
Liudmila Molkova 00:43:41 We should, but we don't do this for this one.
What do we report it with now?
Does anybody remember?
Aaron Abbott (Google LLC) 00:43:51 I don't remember.
Dylan Russell 00:43:53 There's a level?
Aaron Abbott (Google LLC) 00:43:55 Setting severity, yeah, sorry.
Dylan Russell 00:44:01 I'm not sure.
Liudmila Molkova 00:44:06 I'm checking.
Aaron Abbott (Google LLC) 00:44:14 Yeah, I do kind of agree with Dylan, though. I feel like… the… since the… at least what I've been saying, the purpose for this thing is, is to have separate sampling decision from events. It seems nice to have the configuration be completely orthogonal.
So the, like, I can see a case where you would want to stamp the, You know, the uploads, but not put it on… So you would set no content, but then you would still set the uploading hook, or you would put…
Dylan Russell 00:45:00 Looks like we don't set… yeah.
Liudmila Molkova 00:45:07 So if I set it to debug… Let's go for it.
And then the… the… enabled.
Once it's in, we will start using it.
Aaron Abbott (Google LLC) 00:45:20 Yeah, I shared in the chat, it's… We have it, it's just not been released yet, so it will be in the next release.
But it is already supported in declarative Config, I believe.
Dylan Russell 00:45:35 And that… Let's you control logs based on… okay, severity, event name… Oh, that's great.
Aaron Abbott (Google LLC) 00:45:45 Yeah, and I think… Yeah, I don't know which logger we use, I guess it would just be the logger for, like, which scope name you would potentially target.
I guess that's something we can… we can think about, since you told GenAI… I guess we… you pass it into Utogen AI, I'm assuming, so…
Liudmila Molkova 00:46:06 Yeah, in the next release, we will be using the instrumentation library name, well, the module name as the scope name. Currently, we… I have the same one for utils.
Aaron Abbott (Google LLC) 00:46:20 Okay.
It sounds like we kind of all agree, then, to use… Use that.
Liudmila Molkova 00:46:29 Can we… Document, at least in the prose, in the notes on the event definition, that it should be emitted with debug.
Dylan Russell 00:46:43 Okay. Change the severity of it to debug.
Liudmila Molkova 00:46:48 Alright, and done.
Change the severity, set the severity here.
Oh, not here, but whenever it's needed.
Dylan Russell 00:47:00 Right.
Liudmila Molkova 00:47:02 It might be breaking, though, for… For somebody who relies on it.
Dylan Russell 00:47:10 Relies on it being set to unspecified.
Liudmila Molkova 00:47:14 Yeah, because I think it might pass filters that otherwise the debug wouldn't pass.
Dylan Russell 00:47:22 How's… yeah, how's unspecified handled?
Trask Stalnaker (Microsoft Corporation) 00:47:25 I remember debating this, but I don't remember what we ended up with.
Liudmila Molkova 00:47:29 I think it's… it's unspecified. How unspecified is handled is unspecified, to a large extent.
And it's probably… maybe part that there's… maybe Python does something about it, but maybe backend, maybe both?
I think, initially, the goal was that unspecified is always captured, but where we are today is probably never captured.
Or… unspecified.
Trask Stalnaker (Microsoft Corporation) 00:48:02 Check, check the, spec or some con, because we definitely… Debated that vigorously.
And clearly, Neither were very compelling, or I would probably remember which one we picked.
Aaron Abbott (Google LLC) 00:48:22 Is this for the enablement of the logger, or do you mean… like, cause I don't think there's any… filtering happening based on severity in the Python SDK, at least.
Liudmila Molkova 00:48:34 Oh, okay, so then it's completely up to the backend.
Aaron Abbott (Google LLC) 00:48:40 Okay, that might be out of date, maybe I'll just abstain. I don't remember off the top of my head.
Dylan Russell 00:48:49 Yeah, I remember there being some way to control this.
Like, you only see logs for some number of severity.
Liudmila Molkova 00:48:57 It's your Python login, probably.
Dylan Russell 00:49:00 Yeah.
Liudmila Molkova 00:49:00 the… the OpenTelemetry API.
Dylan Russell 00:49:11 Alright, well, I'll… I'll do some research and… But it sounds like we could probably drop it.
Because the logger stuff is gonna support disabling it.
And maybe we want to upgrade the severity to debug.
If it doesn't break people.
Liudmila Molkova 00:49:29 When is the next Byton release, by the way?
Aaron Abbott (Google LLC) 00:49:35 I think it's been about a month, so probably whenever.
I can… I think it's got Leighton here, too.
I don't know, sorry to put you on the spot, Leighton, but… What do you think?
Leighton 00:49:49 Yeah, we can do once… we can do one soon. It's been… it's been over a month or so.
Aaron Abbott (Google LLC) 00:49:53 Yeah, it's been 2 months.
Liudmila Molkova 00:49:56 Oh, nice! So then, maybe once it's released, we can just leverage it and call enabled?
And then… It would… Hopefully eliminate the noise for users who didn't need it.
Trask Stalnaker (Microsoft Corporation) 00:50:20 And for context for everyone, I assume this is what we're talking about.
Aaron Abbott (Google LLC) 00:50:28 Yeah.
Dylan Russell 00:50:29 Yeah.
Trask Stalnaker (Microsoft Corporation) 00:50:38 Alright.
Okay to move on?
Liudmila Molkova 00:50:43 Yeah, thank you.
Zening Chen (Snowflake Inc.) 00:50:44 Yeah, hi, yeah, my name's Ning Tei.
And I work for Observe. We are… we are recently building some LM Mustopability features, and I found it, like, without having conversation ID on the 2 o'clock span, it's a little bit hard for us to filter 2 span by, conversation.
So, wonder how people feel about adding the conversation ID to to a call span as a conditional required?
Dude.
Yeah, I'm looking forward to any comments or feedback.
Liudmila Molkova 00:51:21 Thank you for all your contributions, by the way. I really appreciate all the fixes you're doing, and fighting, and now in some conf…
Zening Chen (Snowflake Inc.) 00:51:28 Yeah, yeah, thanks.
Yeah, that's it.
Aaron Abbott (Google LLC) 00:51:36 Yeah, I mean, does anybody not… I think we've talked about the context scope attributes, like, a bunch of times in terms of the instrumentation for this, but does anybody not… Support this for the conventions?
Trask Stalnaker (Microsoft Corporation) 00:51:51 Via context-scoped attributes.
Specifically, versus… Duplicating.
Aaron Abbott (Google LLC) 00:52:04 What do you mean by duplicating?
Trask Stalnaker (Microsoft Corporation) 00:52:07 And… Like, defining, def… I guess having the semantic conventions depend on the, context-scoped attributes to… populate that, and I think that would make it an opt-in feature.
Liudmila Molkova 00:52:33 Do we need it to be context-scoped attributes? Because it can be if user provided it, right?
But if user didn't provide, and Agent Clear has Conversation ID, it could stamp it on the context, and it would be propagated to… things under.
And they can decide to override it if there is, like, a nested conversation going on, but… I think it's useful For instrumentations, too.
Coordinated between themselves, even when context scoped attributes are not provided.
And it's a set of well-known attributes.
That they would… Exchange with each other.
Aaron Abbott (Google LLC) 00:53:22 Yeah, do we need to specify that in the conventions at all?
Can we just… I haven't looked at these PRs yet, but do we have to say, like, the mechanism?
Liudmila Molkova 00:53:39 So sometimes it's available. So, like, I think in… in LinkChain, the existing instrumentation makes a bunch of things available without the… the context propagation.
And it… the conversation information can be available during the tool call.
by all different sets of means, I… I… I'd rather… Keep the convention saying, okay, if you have it.
Put it. But how you have it… None, but… Not important for inventions.
Trask Stalnaker (Microsoft Corporation) 00:54:20 And so in, in all of these cases, is conversation ID already on the parent span for the tool execution? And so we're just talking about What, denormalizing, like, propagating that down?
Or are there cases where it's not on the parent span, and… or it can vary across child spans?
Zening Chen (Snowflake Inc.) 00:54:51 as far as I remember, I think conversation I did is… in current semicondition conversation IDs on the invoke agent span.
So, we can definitely propagate it once the data reach backend, but I think that's not always reliable, and, like, requires extra processing, so it would be more convenient to just have it directly on the span, that's my opinion.
Trask Stalnaker (Microsoft Corporation) 00:55:19 Yeah, I mean, I'm supportive of this, in GenAI. I just want to kind of be clear the… Previously, in semantic conventions, we have avoided, duplicating… Attributes across the trace hierarchy.
Under the idea that, hey, it's there, you can navigate, and it should only be in one place.
But I… I've felt that pain.
And, it feels like it's come up a whole lot in GenAI as far as stamping, propagating the agent name, and a couple of other things.
I think it… My only ask is that we kind of, like, have the… Like, what is our set of those things? Like, that we do it intentionally, and we say, hey, we understand that this is different than how semantic conventions have been done before, but we feel that we want to start propagating… conversation ID, I don't know, session ID, agent name, whatever, like, really key things.
There are.
Aaron Abbott (Google LLC) 00:56:46 I was just gonna call out, I think we do it for inference already. The conversation ID gets stamped on inference events, or it's, It's optionally required, or opt-in, or whatever.
Liudmila Molkova 00:56:57 Optionally required. I love it.
Yeah, it's a part that maybe we should document the set of attributes that we… intentionally can propagate, and I think there are two, the conversation AD and Agent Name.
For now.
At least.
Wolfgang Therrien 00:57:20 Would Agent ID be part of that, in addition to, like, Agent Name and Agent ID that pair, or just agent name Liudmila?
Liudmila Molkova 00:57:27 The Agent idea… is… And we limited it down to the remote agent ID, something that you, like, how you call a hostage agent, and then it's not applicable.
Wolfgang Therrien 00:57:44 Makes sense.
Trask Stalnaker (Microsoft Corporation) 00:57:51 Appreciate whoever is taking notes.
Aaron Abbott (Google LLC) 00:57:53 Yeah, sorry, I hope I'm not misrepresenting what you said.
Trask Stalnaker (Microsoft Corporation) 00:58:05 Alright, anything else you want to call out?
Zening?
Zening Chen (Snowflake Inc.) 00:58:12 No, no, thanks. Okay. That's pretty helpful, yeah.
Trask Stalnaker (Microsoft Corporation) 00:58:18 And last topic… Last few minutes.
Liudmila Molkova 00:58:23 Yeah!
So, let me just introduce the topic of skills. This is not my favorite.
I can share. No, please share, yeah. So… the… Scales is an interesting… beast.
And I'm still learning about them. This is something that's, coming from ADK folks who do the native instrumentation, and they would like to find how-to instrument skills.
So the skill is the skillmd file, and a bunch of possible artifacts, like scrapes or other stuff.
And… There are… The way it works in most of the libraries, the common pattern is that the skill kind of exists, and at some point, model decides that it's useful, and it executes a special tool, which is called something like load skill. It depends on the framework, on the harness, but essentially, it's the tool call that reads the skill file.
And then it shows up on the context, And then, from there on, it's a Wild West model can decide to execute some script, it can decide to execute a tool. If there was a tool mentioned in the skill, it would just execute that tool that was mentioned if it finds it useful, right?
And there are a couple of other special tools that are common in different libraries. What is the load script?
So model can decide that it wants to have the script on the context.
Or it can decide, okay, I'll just… well, it depends on the implementation, but it can decide, okay, I'll just run the command with the script, I don't care what's in there.
And then, finally, in ADK, there is a special tool that handles script execution.
But in some other libraries, I think in OpenAI, it's just a generic tool that runs whatever script, skill or not.
So… what's… Being proposed here is to… a set of attributes that describe a skill when we know it, And we know it definitely during the load skill time.
We know it in some cases when there is a special tool that reads skill resource, or similar.
And sometimes we know it when there is a special tool that executes a command.
And this PR adds refinement… refinements for these two calls.
And… a few skills attributes, including, like, where the skill came from. It can be a local one, it's a URI, it can be a local, directory, it can be a remote Scale from some skill registry.
The most questionable part here is that people do, like, different libraries, different harnesses do it in different ways.
And, some of these tools… Some of the stinks won't be a tool cause.
But, if they are, then we can… record them as tucos. There's a set of attributes that could be applicable Even if it's not a tool call.
I've, been reviewing this, there is a product… well, there is an implementation for ADK, there are some reference scenarios here.
And I think it looks, reasonably well. I approved it, and then I learned quite a bit more about the skills, so I might give it another round of review.
Trask Stalnaker (Microsoft Corporation) 01:02:37 So, this… we discussed this a few weeks ago, the idea of a scale span, I think when you weren't here, Ludmila, and… So… At that point, The consensus on the call was that we don't like, a skill span, like, I understand the load skill.
But executing a skill… Like, at least in the majority of cases, like, the skill… it gets read into context, and then, yeah, it just… the LLM gets to use whatever is then in that context. There's no… like, execute skill… Thing to capture.
Liudmila Molkova 01:03:25 There is no proposal for it here. It's just that the tools that have information about skills are defined as refinements of the execute tool with optional skill information attached.
Trask Stalnaker (Microsoft Corporation) 01:03:43 Oh, okay.
So, which refinement… So there's a load skill… I understand the load skill.
Are these… these the…
Liudmila Molkova 01:03:58 are also the special tool calls, so the load skill resource may be specific to ADK, or not as wide as load skill, but the run skill script Okay, so this is tricky. It's not…
Trask Stalnaker (Microsoft Corporation) 01:04:12 This is not run skill, it's something different.
Liudmila Molkova 01:04:15 Right, and it's essentially the refinement being defined, is the generic Script execution rather than, skill-specific.
And if you have information about skill, you can attach it to the this refinement.
Trask Stalnaker (Microsoft Corporation) 01:04:35 Thanks.
Yeah, Aaron.
As we hit the 10 o'clock hour.
And… oh, we lost Erin.
Clock struck midnight.
Alright, y'all.
Liudmila Molkova 01:04:49 Yeah, thank you all.
Talk to you later.
Trask Stalnaker (Microsoft Corporation) 01:04:51 Bye.
Leighton 01:04:55 Thank you.

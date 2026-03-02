SIG: LLM Semantic Convention WG
Date: 2025-08-26
Duration: 83 minutes
============================================================

## Zoom Recording Transcript

Liudmila Molkova 00:18:41 Hello. Hi, Sergey. Hi, Erin. Hi, Shipra.
Aaron Abbott 00:18:48 Come on.
shiprajain 00:18:50 Hi, everyone.
Liudmila Molkova 00:18:58 Okay, let's get started. I'm going to share my screen.
Second, you have to excuse me, I am a recovering Windows user who switched to Mac.
And…
I have to say, I hate it. It's not that Mac is bad or anything, it's just that the 30 years of Windows usage.
I… my fingers know what I'm doing, but my brain doesn't, and now my brain needs to understand what my fingers were going to do.
So, if I do something stupid, you know why.
Sergey Sergeev 00:19:39 I'm migrating from Android to iPhone. It's pain, pain.
Alex Hall 00:19:46 Congrats on the new job, Yudmila.
Liudmila Molkova 00:19:48 Thank you.
Samuel Colvin (Pydantic) 00:19:51 Yeah, congratulations.
Sergey Sergeev 00:19:53 I was wondering if it's a typo or something. Congrats.
Liudmila Molkova 00:19:58 No, no, not a typo, it is. I switched to… now I'm develop… developer advocate at Grafana.
Samuel Colvin (Pydantic) 00:20:06 Will… will you continue to do all this stuff, or will you… will you… will you still be involved lots in… in hotel, or what… yeah.
What's the plan?
Liudmila Molkova 00:20:16 yeah, I'm going to stay involved in Hotel, for as long as they let me, and it seems they hired me to do this work, so I hope I… I… I can… more of it.
Samuel Colvin (Pydantic) 00:20:27 That was my… that was my assumption, but that's great to hear. Congratulations.
Liudmila Molkova 00:20:32 Thank you.
Cool!
So, let's, … get to the agenda. Our neglected project board is here.
…
Should we spend a little bit of time and see if these issues are… can now be… some of them can now be closed?
And thanks, Alex, I saw you tried to close as much as possible.
… Oh, this is for the multimodel.
Alex Hall 00:21:13 Yeah, this is not meant… well, this is a container for… several things.
I also want to, like, link to something about thinking parts here.
But yeah, this is not meant to be closed now, this is actually follow-up.
Liudmila Molkova 00:21:26 Okay, wonderful, thank you.
….
Alex Hall 00:21:31 some issues.
Liudmila Molkova 00:21:33 Right.
Alex Hall 00:21:38 This, I think, can be closed. I probably commented on it.
Oh, it's in Python.
Liudmila Molkova 00:21:51 Oh, right.
Aaron Abbott 00:21:52 Yeah, I think this is probably obsolete since the, since the semantic emission changes we made.
Liudmila Molkova 00:22:00 I think there is a pull request that updates….
Alex Hall 00:22:04 The vertex instrumentation, right?
Aaron Abbott 00:22:07 And we can….
Liudmila Molkova 00:22:10 ….
Alex Hall 00:22:11 I saw that, I was wondering why the Vertex one and not the Google Gen AI one, isn't the Vertex sort of, like, older?
Aaron Abbott 00:22:18 Yeah, I think we're planning to do both, it was just, I already had, like, a…
I'm assuming it's a PR from Dylan, but I already had done some work on the GenAI one, so I kind of, …
didn't wanna…
get in the way of him doing the other one, so… But this one's still used by LaneChain, for example, so it's still got some use.
Liudmila Molkova 00:22:44 … Okay… Was it closed already?
Dylan Russell 00:22:54 I think it should still be there.
Liudmila Molkova 00:23:03 … Do you remember the number?
Dylan Russell 00:23:06 ….
Liudmila Molkova 00:23:07 Oh, Vertex CI, okay.
Dylan Russell 00:23:09 Fantastic.
Liudmila Molkova 00:23:10 Okay.
Dylan Russell 00:23:10 Yeah.
Liudmila Molkova 00:23:11 So, I'm going to link this issue, mention this issue here. Okay, and if you think it can be closed, let's close it.
Dylan Russell 00:23:20 Okay.
I'll take a look.
Liudmila Molkova 00:23:24 Thank you.
Dylan Russell 00:23:24 I have one unrelated question I wanted to ask about this.
….
Liudmila Molkova 00:23:31 Huh.
Dylan Russell 00:23:32 The, stability mode, like, environment variable thing, which…
I guess so we're supposed to put the new changes behind, like, that environment variable.
Is that… Correct.
Liudmila Molkova 00:23:48 Yeah, and I think you… you've started doing it, right?
Dylan Russell 00:23:52 Yeah.
Liudmila Molkova 00:23:56 So you know what? Maybe we can add it to the agenda, because I also started doing it, and I wanted to discuss some configuration options and see how they would play.
Through it with each other.
Dylan Russell 00:24:09 Alright, that sounds good.
Liudmila Molkova 00:24:11 Thank you.
Cool, … So, we will see if, this guy can be closed, handle tool message embedded within.
user message, I have no idea. Oh, okay.
Erin, do you remember?
Aaron Abbott 00:24:51 Yeah, I think this was a similar…
kind of issue, where because we were capturing the user message, but… but the Gemini API represents the user… the tool as a user… the tool response as a user message. It was just kind of getting doubled. So with the new changes, I think.
…
it's pretty clear we should just do the… the tool part, tool call response part. So I think we can, … and we can just use the same role. So this… this one should also be fixed by that same…
Pull request, I think.
Liudmila Molkova 00:25:23 Okay, wonderful. But this is in semantic conventions, and we consider it's fixed in the latest version of semantic conventions.
Aaron Abbott 00:25:32 Yeah, yeah, you wanna just close it out now?
Liudmila Molkova 00:25:34 Yay, if you don't mind.
Aaron Abbott 00:25:36 Yeah, sounds great.
Liudmila Molkova 00:25:41 Yep.
Aaron Abbott 00:25:42 Thanks, Alex.
Liudmila Molkova 00:25:46 Wonderful.
So, we are…
End of our triage timebox, and look at us, we cleaned up one issue from the board.
… Okay.
Great. So… I… not sure if I see any new people here. Yeah, I see some.
So, this is the section where you can optionally jump in and introduce yourself. We will be happy to learn who you are, what you're working on, what brings you here. If you don't wanna jump in, that's totally fine.
So, anyone wants to talk about themselves?
Dylan Russell 00:26:31 I don't know if I introduced myself before, but…
Yeah, I'm Dylan. I work with Aaron at Google.
And… yeah, I'm gonna be working on some of this stuff.
… So, yeah, nice to meet you guys.
Pradeep Nair 00:26:51 Hey, hi everyone. I'm Pradeep, I work with Sergey at Cisco.
Nice to meet you all, and looking forward to, work actively and contribute to this.
Liudmila Molkova 00:27:08 Nice. Thank you.
Anyone else?
Okay, so….
Josh Winerman 00:27:16 Alright, I'll jump in real quick. Hey everyone, I'm Josh, I'm also working with Sergey at Cisco. Some of the same work as well.
Sergey Sergeev 00:27:29 Yeah, we are getting there to contribute more to Python instrumentation and so on.
And we are ramping up.
Liudmila Molkova 00:27:40 Wonderful.
Samuel Colvin (Pydantic) 00:27:41 Can I ask, when you say Cisco, is that Splunk, or is that separate from Splunk?
Sergey Sergeev 00:27:46 So Cisco now is Planck, AppDynamics.
So, three groups and, some bigger Cisco teams. Cisco is huge.
Samuel Colvin (Pydantic) 00:28:01 Thanks.
Liudmila Molkova 00:28:10 Anyone else?
Okay, count 1, count 2, count 3… Switching through the agenda.
anksing 00:28:26 Hello, Mila, sorry, one quick question.
So, in this, document, I think just before agenda, there was nothing, there was no agenda for….
Liudmila Molkova 00:28:36 Oh, okay.
anksing 00:28:37 up, so it'd be great if we can push that down.
Thank you.
Liudmila Molkova 00:28:42 Okay.
So, since you were the first one, I'm going to put you… The first, …
And then, let's go ahead, let's talk about the valuation results.
shiprajain 00:28:56 Ludml, I think I also had my PR, I'm not sure…
I think it is point number 3. Did I not put my PR yet?
Liudmila Molkova 00:29:06 Is this this point?
shiprajain 00:29:08 Yes.
Liudmila Molkova 00:29:10 Yeah, could you add the link, please?
shiprajain 00:29:12 Yes.
Liudmila Molkova 00:29:14 And, it seems we… we have some time, I hope we have some time, we should, ….
shiprajain 00:29:19 Yeah.
Liudmila Molkova 00:29:19 get to the bottom of the agenda today, at least let me, watch time and, make sure we do.
Okay, … Evaluation results… … Anki, do you wanna give an intro of what we are doing?
anksing 00:29:43 Oh, sure. So, with this peer, we're trying to come up with a semantic convention of how to capture evaluation results, and we had some discussions over past
Some beaks, and then…
We are going in… doing it in two phases. One is, like, starting with evaluation result as an event, and then we're gonna also have another issue where we're gonna discuss more on how do we capture the, process of evaluation in form of a span. So, this PR specifically is for capturing evaluation result as an event.
And… and I think, They're like…
Pretty close on, like, resolving all the comments.
I think there's only… One outstanding comment that's, …
remaining on this PR, which is, I think I saw from Alex, which is about the…
Generate response ID, if I'm not wrong. So it's almost at the bottom of the PR.
Yes, I'm going down.
Liudmila Molkova 00:30:48 This one, or…?
anksing 00:30:49 Somewhere… somewhere down.
Alex Hall 00:30:50 do not photo.
anksing 00:30:52 So, don't Yeah, somewhere… yeah, right there.
So, it's about the GenAI response ID. So, yeah, I wanted to… discuss on…
Like, on this comment, and then kind of see if we can…
How we can kind of resolve this.
So Alex, the, feedback here is this response ID would already exist on the
actual span that's being evaluated, right? And do we want to duplicate it here?
Alex Hall 00:31:23 Is that what it's intended to be? It's referring to the evaluated….
anksing 00:31:30 Oh, sorry, actually, I'm not able to hear you very clearly.
Sorry, Alex, could you, sorry, repeat that?
Alex Hall 00:31:40 Well, I'm just asking, is that what it's intended to be? It's referring to the evaluated thing.
anksing 00:31:46 Yes, yes.
like… not the evaluated span, but something, like, which you can relate this.
Evento, if you want to.
Liudmila Molkova 00:31:57 This year?
Alex Hall 00:31:58 the company.
Liudmila Molkova 00:31:58 Coach.
anksing 00:32:00 Oh, sorry. Please go ahead, let me know.
Liudmila Molkova 00:32:03 So this is the completion, like, if… like, it's, it's…
depends on the model. Let's say in OpenAI, there is a completion AD, and it's unique per response.
And you would, … Well, in my understanding that this response ID is the…
completion idea of thing being evaluated. It's not related to the evaluator.
run. It's… it's about the thing it is evaluating.
So maybe we can update the brief and say this, that this is the… Thing be…
Being evaluated in case Where the parent-child relationships
cannot be used. This is a second way you could correlate things.
Sergey Sergeev 00:33:09 I was wondering if we can use, something like span linking, if there is a similar standard for event linking.
If we can put link, context, and just put anything from the parent Or evaluated spend into that.
context structure.
Liudmila Molkova 00:33:30 So if you have parent-child relation, like, if you know the SPAN ID, of the LLM call.
then… you can use parent-child relationships. You can say this, this event is a child of That's been…
The problem is that when you, let's say, run the violations in your code, You have something like…
Chat complete.
And then… you don't have a SPAN ID.
Right? You… it happened, … Outside of your code.
But you know their response, AD.
Does it… does it help?
Alex Hall 00:34:26 Was that the intention behind this? Was it sort of, in case you somehow don't have a spam ID, here's an alternative?
Liudmila Molkova 00:34:33 Yes.
Alex Hall 00:34:36 Okay. Then yeah, I think it mostly just needs to add more, like, clarification.
you know, when it says the completion? Like, I guess… Dear
to me, it sort of feels potentially ambiguous, because we've been talking about all these other attributes that refer to the evaluation process. Now that those are gone, maybe it's not actually ambiguous anymore to a newcomer.
But… Some extra gratification would be good, and maybe also just, like.
something about why you would do such a thing. It's the only attribute like this that is, like.
A copy of attributes present on the evaluated parent span.
So it sticks out a bit weirdly, but… The justification makes sense.
Otherwise, I'm happy. I'll approve now.
Liudmila Molkova 00:35:56 Cool.
anksing 00:35:57 Cool. Awesome.
Liudmila Molkova 00:35:59 there are, quite a few open discussions, so we cannot merge PRs until the discussions are resolved.
anksing 00:36:09 Yeah, I'll take care of resolving. Like, I think this is the only…
Really open one. The other ones, I think, …
are kind of resolved, but I'll make sure I'll go through them and then resolve them.
Liudmila Molkova 00:36:21 Yeah, so, yeah, we are… the metadata is gone, right?
anksing 00:36:25 Yeah, yeah, that's good, yes.
Liudmila Molkova 00:36:27 Okay.
And… The initial comment you linked,
anksing 00:36:36 Yeah, I think this one is also addressed, like, I've removed the input-output tokens for now, and then we can discuss this more when we have the discussion on the span.
Revolution.
Liudmila Molkova 00:36:46 Okay.
anksing 00:36:47 And same here for this one. I think this is something we can do as an editive thing.
I have a smaller PR, yes. I think Sergey had this feedback, I've captured this in the other issue as well.
Sergey Sergeev 00:36:58 I added it.
anksing 00:36:59 Donovista.
Sergey Sergeev 00:36:59 I have a 10-minute discussion scheduled for something that came up recently, and you will tell me what to do with it. But I don't want to interfere with this pull request, it makes sense to me.
Liudmila Molkova 00:37:14 Okay, that sounds good.
anksing 00:37:20 Yeah, this was about adding, like.
the input and the outputs that were used for evaluation as a part of this, so this also, I think, would be very
Good discussion to have as a part of the…
Span because, evaluation span, because it's going to be more comprehensively, kind of.
Sergey Sergeev 00:37:37 Yep.
anksing 00:37:37 I logged up there, so….
Liudmila Molkova 00:37:41 Okay, thank you.
And then, essentially….
anksing 00:37:46 Yeah, this one I'll address.
Yeah.
Liudmila Molkova 00:37:49 Cool. And then, once… once it's addressed, we should be ready to merge.
We have the approvals, and we have….
anksing 00:37:59 Cool, awesome. Well, thank you so much for the support and the feedback here, and the great discussion. Yeah, looking forward to working on the other pieces as well.
What's it going on?
Liudmila Molkova 00:38:10 Cool.
anksing 00:38:11 Cool. Thank you.
Liudmila Molkova 00:38:12 Thank you.
Okay, Shipra, let's… this is your PR, right? Let's talk about it now?
shiprajain 00:38:22 Sure, yeah. Do you want me to share, or you can… you would like to share?
Liudmila Molkova 00:38:27 ….
shiprajain 00:38:27 You're… and you're sharing.
Liudmila Molkova 00:38:28 You can share if you want, or I can share if you don't need to, whatever you like.
shiprajain 00:38:34 Yeah, I mean, anyway, yeah, I think you were already sharing, we can go, go ahead, yeah, yeah.
So, most of the changes, I believe.
Okay. So, I think the scope of the PR is now reduced after a little PR is merged on, having input messages and output messages, so I reused that. Initially, we wanted to propose in the invoke agent span,
to capture input and output messages, and I was naming that differently. So, I've removed that change.
And I rebased my, code to the main branch. So, now we are basically proposing 4 additions.
to an invoke agent, in form of two definitions and orchestrator agent definitions. The idea is simple, for an invoke agent span, we would want to propose standardization on users being able to pass the tools that are available for the agent to
do the execution. Similarly, if the agent wants to, call another agent, then all those possible registered agents, let that be passed.
So, that is for Invoke Agent, and for executeTool, we have… we… we are basically retaining, the arguments, what were the arguments passed to the tool, and the result that was,
generated, that… that was returned by the tool. So, these are the two attributes that we're retaining for tool… execute tool.
Liudmila Molkova 00:40:11 Cool, so, do you want to go through the discussions, or is there something in particular you want to, highlight there?
shiprajain 00:40:19 Yes.
Liudmila Molkova 00:40:20 Yeah.
shiprajain 00:40:21 Yes, yes. So, for tool definitions, I think one of the points that Alex, highlighted was, why don't we capture tool definitions as part of LLM span, and any specific reason to propose it at agent span. So, I think I had, I was already responding to Alex.
…
Okay, I've not seen any latest… okay, I didn't see, Alex's last response, but in short, the reason to have this information at Agent Span was to completely reduce the duplicacy at the same time, make it available at the place where
it can be logically linked to. So, in theory, an agent basically has the access to an LLM, which is the brain, to make the decision.
And then it has tools, which are basically the executors. So we are making the tool definition, which is generally, static. I want to hear the scenarios where we,
figured that tool definition was changing, so that is new, but in our POCs, in our experimentation thus far, tool definitions are mostly the definition of all the tools that is available for an agent to, make a decision what is the right pick.
And, that is why we wanted to make this information available at the agent span.
At the same time, through our POCs, we have shown that in a particular invoke agent span, there can be multiple times an LLM call has happened, which, which means, LLM spans, there could be multiple times an LLM spans are, generated.
Passing tool definitions at each LLM span would certainly lead to more duplication. …
So, here, the idea is very simple, without really getting into what was the actual tool that was, chosen by the agent to make the, to further, execute the task.
We are basically telling what is available for… for the, agent, as the entire you know.
an entire set of, tools. So, that's the rational behind it. Alex, if Alex and others, if you guys have more questions.
Okay.
Alex Hall 00:42:47 I was gonna have, maybe.
Samuel Colvin (Pydantic) 00:42:49 Go on, Alex.
Alex Hall 00:42:51 No, you… go on, I don't think there's much that needs to be discussed, that's all.
shiprajain 00:42:56 Oh, okay, so it's on a blocker.
And I'm sorry if I've missed context, is….
Samuel Colvin (Pydantic) 00:43:01 But tools can change during an agent run, so…
They can be different for each…
LLM call, and not as practically they can, but practically that's a thing. ….
shiprajain 00:43:15 That's right That's why. So, we….
Samuel Colvin (Pydantic) 00:43:18 Recorded on the agent.
shiprajain 00:43:20 Correct. So there are two things, right? One, that
So, when we are designing an agent, basically you can consider that this is information, that we have from design time, as in, what all tools an agent would need in order to perform its task during the course of execution.
Now, when a particular invoke agent span starts, and an LLM span is called, which means agent is now falling back upon LLM to make some decision.
At that moment, for that particular LLM span, out of all the list of tools that are available to the agent, only a few may be picked.
So that are the runtime tools that are chosen at that point in time, and that execution. So, that changes, but tool definitions as such, which were available right in first place, won't ever change, right?
Samuel Colvin (Pydantic) 00:44:09 Yes, they can change at any time. As in, theoretically, the set of tools are completely dynamic.
I mean, MCP allows tools to… as in, in theory, you should get the list of tools at any point, right? I mean, there's a problem with, like, getting them immediately before calling the…
calling the MCP, but, like, they can change, and practically, it's just as easy to change the definition of a tool as it is to select which tools are available.
I don't know how practically sensible that is to do, but it's definitely possible.
shiprajain 00:44:44 Okay, so…
Okay, maybe Ankit's also having his hands up, let's hear from him, too, his question. Maybe Samla will get back to you on this one, because I'm still not convinced on, on, …
Why we would want to kind of change the tools that are available for an agent.
And the definitions, if they change, then it can be a breaking change itself, right? So, so, so yeah, Ankit.
anksing 00:45:11 So, like, during a… it… Oh, sorry, yeah, go ahead.
Samuel Colvin (Pydantic) 00:45:15 Go ahead, I'll come back after.
anksing 00:45:17 So, like, during an agent run, or an agent execution, like, can that happen? That the agent tools can change, like, within that execution period? Yes. Like, I'm just asking because….
shiprajain 00:45:28 She's like….
anksing 00:45:29 very….
Samuel Colvin (Pydantic) 00:45:31 I mean, in particular, you can… you can… MCP can…
as an example, the set of tools are completely dynamic. As in, you get a set of tools before each call to the LLM, there is no guarantee that they are in any way related to the set of tools you got last time around. But more practically, I mean, we have support for changing the tools that you…
expose as… at each stage, right? As in, you have a function you can call, which returns, like, some tools. Those tools can change. ….
anksing 00:46:03 I see.
Samuel Colvin (Pydantic) 00:46:04 I know.
shiprajain 00:46:04 Yeah.
Samuel Colvin (Pydantic) 00:46:05 There are practical cases where you might want to change the… have a tool called FUBAR, where it's… parameters
change depending on the state. As in, you get rid of the…
I don't know, one of the parameters, because that has now been constrained.
shiprajain 00:46:28 So, Samuel, I had a curious question. …
a part of our work for tracing is also to make sure that we capture needed information so that we can do the evaluation later correctly, right? And in that case, if, suppose we want to do the tool call evaluation, one of the important aspects that we want to evaluate upon is whether the right tools were chosen.
and whether the right arguments, were… were seen, passed, adhered to, right? Now, if…
The point of dynamism comes into picture, then evaluation completely goes for toss, and it gives very less room to, understand where the agent is going wrong.
Samuel Colvin (Pydantic) 00:47:13 I mean, I think no one really has a good answer to evals when you have multiple steps, because by definition, every time the previous step, like, you're in an arbitrary… technically, you're in a completely unique situation.
In each case. I'm not saying that it is a good idea in a common scenario to change the definition of tools as things continue, but it is definitely something that
that is possible, and so I… I don't know. My suggestion….
shiprajain 00:47:42 Yeah.
Samuel Colvin (Pydantic) 00:47:42 It might be problematic to…
Basically have the semantic conventions Not allow that flexibility.
shiprajain 00:47:52 True. So, I'm just thinking, you know, on my feet right now, and I would definitely need session from the crowd over here. Since, I mean, when we were designing, when we were proposing this, it was more, with the thought process that mostly tool definitions are going to be static.
And that is going to be usually the case, because in a number of scenarios, these tools can also be very specific to the organization, right? So shall we continue to have this attribute for now?
Based on the clarity on static tools that we have, which, you know, which would be definitely useful for the user, we can change the description to suggest that correctly, that
This particular attribute is to capture static tool definitions, and for dynamic tools, maybe that can be a very evolved discussion. I think we will have to think through a lot many aspects, there, before we can see how do we trace it.
Right, so shall we just keep that separate?
Samuel Colvin (Pydantic) 00:48:53 Open to… open to… yeah, yeah, I mean, I… I can see that argument, … I mean, I think the obvious thing to do is at some point to also support defining the tools on the LLM call, and then that covers…
all of the things that can happen. Then there is some ambiguity about whether to define tools in both places.
I don't have an answer, I'm not, like, criticizing this idea, I'm just pointing out that in theory and in practice, there will be scenarios where the set of tools, you know, is completely variable between different.
those.
shiprajain 00:49:30 Okay, so, is it okay to say that for now we… I changed the, the description in such a way which clearly states that, this particular attribute needs to capture static tool definitions?
And there is a… and just leave it to that, and then maybe we can create an issue on dynamic tools, and how those definitions should be captured, and let us follow up in subsequent PRs. I think we will also have to do some good POC around that.
Force.
Samuel Colvin (Pydantic) 00:50:01 I mean, as far as I'm aware, we already have a way of defining tools on an LLM call. At least we do that in Pydantic AI slash Logfire. I don't know whether….
Liudmila Molkova 00:50:09 Dawn.
We don't do it in semantic conventions, and we think we should reference this attribute.
on the LLM span as well.
It's the….
shiprajain 00:50:20 this country.
Liudmila Molkova 00:50:21 controversial thing, we… Should be….
shiprajain 00:50:23 Okay.
So then I can raise that… okay, that is a great point. I can utilize the same one for both
Invoke agent and LLM span. Cool.
Liudmila Molkova 00:50:35 And I don't believe that when you're invoking an agent, you have any means to know whether the list of tools is dynamic or static.
The instrumentation wouldn't know, definitely.
… Is there any controversy?
And cop… like, whatever it means.
if I have some means to invoke an agent.
And it takes a list of tools.
Is there any controversy in capturing this parameter?
Samuel Colvin (Pydantic) 00:51:05 I don't see it. I mean, the worst case is there's duplicated data. I mean, the better argument is, by the time the tools are completely dynamic, is that even an agent? Like, at that point, I mean, the definition of an agent is something that has, effectively, you know, tools and gets called until some abstract definition of end. Like.
I mean, I think a better argument is if your tools are completely dynamic, then whatever your code thing is called, that's conceptually not an… not an agent, as per the, like.
sort of anthropic definition. I think it makes sense to have them definable on the…
agent, I think time will tell whether… where people end up defining them, what ends up working. I think it makes sense to definitely be able to define them on the LLM span as well, because that covers all of the different possibilities.
Liudmila Molkova 00:51:54 So, it sounds like the conclusion, … oh, sorry, Ankit, you were jumping in. Do you want to say something?
anksing 00:52:02 I just wanted to say, like, in case, like, if the tools are, like, dynamic at the LLM span level or layer, then it sounds like LLM itself is…
Behaving as an agent, right?
shiprajain 00:52:12 It can dynamically change.
anksing 00:52:14 Get out, like, tools and use them, right?
I mean….
shiprajain 00:52:19 And then…
Yeah, and hence, Lyudmilla's proposal, right, that we add this particular attribute at LM Spanel, also for now, would cover.
Is it?
event, okay.
Samuel Colvin (Pydantic) 00:52:35 Good to me.
shiprajain 00:52:36 Awesome, so let me do that, … And…
After that, I think I'm also reading through chat, Alex, says that we should discuss more on, orchestrator agent definitions.
that attribute.
Liudmila Molkova 00:53:00 At least go ahead, I'm just capturing notes.
shiprajain 00:53:02 So, Ludmila, to your point, let's add it as LMSpan attribute. Are you saying we remove it from agent span and we, keep it at LMSpan, or we keep it both the places?
Both places, cool.
Liudmila Molkova 00:53:14 It sounds like having it in both places is not…
Controversial, it kind of makes sense. There is a duplication, but we don't know yet if it's bad, so I don't hear a strong argument against capturing it. If somebody provided two definitions on both, right? They didn't have to, but they provided, so we capture it.
It kind of makes sense, it loads up the telemetry, but we'll see. Maybe going forward, we would change something around this.
shiprajain 00:53:43 Okay.
The other one was regarding,
Orchestrator agent definitions. So, Alex, I saw your response.
And I, I understand, … name and description could look similar, so I think I'm okay to remove it.
Alex Hall 00:54:15 It's not just this PR. Another issue slash PR got opened very recently.
again, wanting to add a role attribute to agents. Are there systems which have
Name, role, and a description as three distinct things is….
shiprajain 00:54:32 Usually, we have seen that, yes, descriptions are more verbose, names are more, you know, short descriptions.
and agent. However, when we have an agent ID already, which is the child agent, we may not want to duplicate in any way, so I'm okay to remove name. But role is something which I think we should keep.
like I've shown in the example also, how role and, name or description could differ.
Alex Hall 00:55:05 You would have 3 distinct things, name, role, and description.
Samuel Colvin (Pydantic) 00:55:08 an ID, it's for….
shiprajain 00:55:10 So, ID and role.
is what, I think would, ensure that we are capturing the additional information that we want to, suggest, and, we don't duplicate.
So, ID is the agent ID, and what role that agent is going to play.
Alex Hall 00:55:33 Well, I think that, you know, if there's…
If these four things exist in some frameworks, then….
shiprajain 00:55:41 It does, actually.
Alex Hall 00:55:43 If they all exist, then fine. It was surprising to me.
That's a lot of different ways of… Talking about an agent.
shiprajain 00:55:56 Yeah, ID is basically a unique identifier, right?
talk about, yeah, name and description. So, name and description… Name and description is just… Yeah, usually….
Alex Hall 00:56:07 in 19.
shiprajain 00:56:08 So, this is not just the agentic framework. I mean, I come from ERP space, and there we could really see the benefit of having name and description, where name used to be a short-form, very concise
Idea about that.
attribute, and description used to be more verbose. So from there, I believe this whole thing kind of propagated name and description. Role is something which, basically, how that person's gonna act in that situation, right? So, I've given a few examples. So, I mean.
I can again take a look between… if it is a debate between name and description, then I can take a look. I'm okay to remove both, because that information would be available in some form anyway in the, …
….
Alex Hall 00:56:57 I'm not saying anything has to be removed, I was asking for more clarification. I think that maybe.
shiprajain 00:57:02 Yeah.
Alex Hall 00:57:03 Something could also be added.
shiprajain 00:57:04 I didn't… Yeah, I did… yeah.
Alex Hall 00:57:06 Something saying that the name key corresponds to genai.agent.name, or whatever it's called.
shiprajain 00:57:15 Okay.
Alex Hall 00:57:15 Optional, though, like… If it all is, then I think we can move on to the next comment.
shiprajain 00:57:22 Okay. Description is something which I deliberately didn't keep. I, I, I, I.
Alex Hall 00:57:27 Got through.
shiprajain 00:57:28 the name and description could, portray similar information, usually. So that's why only 3. So I think for now, if…
Just giving a little bit more detail on what should be captured in name, I would want to keep ID, role, name, all of them, but if there is a conflict of any duplication, then name is something that I'm okay to remove. I'm not hearing any conflict, though.
Liudmila Molkova 00:57:51 Yeah, and Kit and Samuel have his….
anksing 00:57:55 I wanted to understand, like, what the roles, like, attribute really captures.
Probably I didn't get the idea of… that on an Asian definition.
shiprajain 00:58:07 So, I gave this example, also, right, Ankit? So, in the example, if you see, we are talking about having…
… Let me quickly get into my system, Al.
Yeah, so… In role, we're trying to classify what specific, …
role… yeah, I mean, agent description is something, say, whether agent, but it can right now act as specialist, or whether that agent is acting as a validator, or whether it is acting as a coordinator. So…
The description basically just gives us, you know, that, what that agent name is, for…
Performing the particular task, but it could wear different hats during the execution, and that is, what we wanted to capture in this,
anksing 00:59:03 I see, I see.
shiprajain 00:59:04 Yeah.
anksing 00:59:05 So that….
shiprajain 00:59:05 That could be also dynamic, and it has to be written when… during the execution runtime. ….
anksing 00:59:12 So, one thing that came to my mind, like, when I, like, heard about Roll is something like…
Like, assistants, user, developer, like, those kind of roles, like, that you already have.
shiprajain 00:59:23 That also, but it depends on the kind of, …
task that we are trying to execute, right? It's a very good example.
Now, similarly, an agent can also play different kind of roles. Some of them that I had seen during execution was the ones that I also gave as examples, that we are choosing an agent, a weather agent, and right now it is acting as a specialist to give more information about the weather conditions.
or a calendar agent which is acting as a coordinator, right? Or, maybe we are calling a weather agent right now, not as a specialist, but just as validator. We want to validate the status… stats. So, yeah.
The idea was to capture what kind of hat that particular agent would wear.
during the execution, and that's why I thought to keep, a rule as well.
Samuel Colvin (Pydantic) 01:00:23 I mean, I'm not criticizing, or I'm not opposed to any specific one of those four names, but…
I think this early in everyone's understanding of what agents really are, having four different ways of describing it seems…
my guess is that over time, we're going to end up not using all four. So….
I don't have a particular dog in the fight of which ones to remove, but… 4 seems like…
too many. As in, if… you can imagine if I have my agent type, and I'm not an observability junkie, and I'm trying to define my agent, and I'm given agent ID, agent name, agent role, and agent description as four keyword arguments, how many people are going to fill in all of those, and read the, like.
paragraph of description of how, semantically, how they're different. Like, they're not going to. As in, people are getting, for the most part, one, perhaps two.
shiprajain 01:01:19 So, that's why I, I, now, what I'm thinking is to have ID and role could be sufficient, where role can, also be similar to name.
If there is no…
a change to the role if the agent continues to play the role, that it does, right? So we just have two, and if there is any specific, hat that the agent is playing in that execution, then we can replace it, with that. So ID and role are… can be the bare minimum,
That we capture, and we remove others, like name and description.
Samuel Colvin (Pydantic) 01:01:56 Sounds good to me.
shiprajain 01:01:58 Awesome.
Aaron Abbott 01:01:59 Interesting.
So, I was actually, …
Curious, like, it seems like role is specific, or maybe not as widely spread, so, like, …
like, description is something that might get passed to an LLM to choose between different agents, right?
Whereas role seems like something that's specific to a kind of orchestrator, so maybe… I don't know which framework it is, but it's something in the execution model of the orchestrator, which might not get passed to the LLM, but it's part of the kind of code. It's like an enum, right?
shiprajain 01:02:30 … I was thinking to use Roll for the same, …
information, Aaron. So, very rightly said, because if you don't pass the description, then LLM won't have the needed information to make the decision, right? And in that case, the… whatever we choose as description shall be just replicated as a role. But in that case.
And if the description is long, then fitting it in a role also doesn't seem
Correct, no. I'm just, again, thinking out loud.
Aaron Abbott 01:03:10 Yeah.
Sergey Sergeev 01:03:11 Should we move the row to that separate pull request? Because there are different views on what it should be.
shiprajain 01:03:22 ….
Liudmila Molkova 01:03:22 I'd like to call time on this.
shiprajain 01:03:25 Yeah.
Liudmila Molkova 01:03:26 We have 15 minutes left, we have a couple of topics on the agenda, it seems we need to do a lot of the further discussions.
I…
I'm going to add one comment for myself. I wonder if it's the only thing we would ever need about orchestration.
And my gut feel tells me there will be way more things.
To add.
So, I wonder, Shipra, if it would work for you, if we could split this PR and take the non-controversial part, the two definitions.
And make progress on this. And we can discuss the orchestration part as the next step. Then we can unblock one part and still, it seems we still need to…
figure out the orchestration. I also want to play with A2A, I didn't have a chance yet, and see how would it fit into the A2A story.
And maybe, … Like, we can make the incremental progress on this.
shiprajain 01:04:29 Sure, sure, sure, let me do that. So tool definition and tool result and argument, these three in that case. I also saw the comments on converting tool argument and result as opt-in. The requirement level as opt-in, so, I would change that.
Liudmila Molkova 01:04:51 Okay, there are comments in the chat, I just want to make sure we have enough time to talk about Sergey's thing and also the configuration, so maybe we can continue this discussion. Keep your thought, let's continue in Slack, or during the next call.
Cool. Sergey, do you want to present your topic?
Sergey Sergeev 01:05:09 Yeah, I can present.
Yeah, I wanted, … I… it's basically, out of necessity, we came out, that we probably need,
Some, special preparation for the data to optimize
Processing of evaluation results and conversational data on the backend.
And I don't even know how to start it. So, again, what we are working on and what we discussed is, this design of Gen AI RTOs.
Which may help to… Build new instrumentations by providing some
function, helper function to import OEM, for example, and to implement instrumentation site, runtime evaluations.
Something like evaluate all LM invocations or agent invocations with deeper vows to provide some evaluation results.
And, … So, Ankit already working on singular evaluation result event.
But, what we realized, it may be, … beneficial from… back-end perspective, and for…
Some of the developers to, create this
big, beautiful event, which will have conversation data and evaluation results, and also some of the evaluated span attributes. So, it may be a crazy idea, but, …
I just wanted to get feedback from…
this group, and the purpose is that on the backend, you basically want to be able to search by APM attributes, by conversation, or by evaluation results. Let's say I want to see some conversations which were evaluated.
Samuel Colvin (Pydantic) 01:07:25 To bias, with some square, and so on.
And in order to do it, it's very helpful to have that.
Sergey Sergeev 01:07:34 data on a single piece of telemetry, and event seems like a good approach, given unstructured nature of
Messages, and so on.
So, … Again, it, … I was thinking if we can propose just to have, that event type.
As an optional, telemet type.
And, basically to implement it, as pluggable and configurable by user type of telemetry.
which, … will be produced, by Runtime Evaluator.
Alex Hall 01:08:16 Would you put multiple calls into the one event?
Sergey Sergeev 01:08:20 Say it again?
Alex Hall 01:08:21 Would you put multiple scores in that one event?
Sergey Sergeev 01:08:24 Yes, it was the idea that, since we… basically, the problem, we don't want to heavily modify all the way APM data, right? So, we cannot…
Really wait a long time, …
For online evaluation to complete, to update, evaluation results on.
The original LM and vacation span.
So, we can, basically send, one-by-one evaluation result events, As we go.
But, in a runtime evaluator, basically, we will have all the data, the original 11 vacation span.
We will have input and output messages, because we are evaluating them
We have an evaluator, and we will collect all the….
Alex Hall 01:09:19 I wouldn't, … This sounds like one event per score, right?
I don't myself.
Sergey Sergeev 01:09:27 I was thinking to put all the results in one event, so… and we have two different options how to represent it. It's either an array.
Alex Hall 01:09:38 You'll submit this event after you know that all of the evaluation is complete.
Sergey Sergeev 01:09:43 Yeah, and usually it kind of makes sense to put them together, because the code just evaluates
I'm usually in a loop, or you can probably run multiple evaluations from the same LM as a judge.
invocation.
So, different options, but something like RAGAS or DeepVow just loops through evaluation metrics you want to do.
And basically run a separate alarm on vacations, and collect evolutionary results.
So, ….
Alex Hall 01:10:21 It's like a span, not an event. I'm seeing start and end time.
Sergey Sergeev 01:10:25 Yes, it's in many ways similar to Spain, but, again, it's, …
just a bigger than spend for most of the backends to process, because it includes,
basically evaluated input messages and output messages as well. And, again, I don't think it will fit all. It can be a lot of optional attributes in it.
But this is something that we think we need to do short-term on the Splunk side. And, this architecture, we can make it pluggable, so we can install just one expert
Which can emit that.
type of telemetry, only if you install some Splunk,
plugin to this Gen AI tools.
So we can do it on the site, basically as a proprietary thing, but I was wondering if it will be helpful to introduce it as a semantic convention.
If there is an interest in this type of… telemetadata.
Liudmila Molkova 01:11:40 My concern here is that it seems the goal of this is to simplify the querying process.
You could, in theory, collect the same, like, without having it
to query the data and merge all the available evaluations with that span, the, that corresponds to the inference call, and then this, thing could exist as the result of the query. It does not
Have a specific confirmation, per se, that they need anything new.
And usually these things are, well, we…
could, in theory, find semantic conventions, but they are extremely vendor-specific. Like, Splunk would like to see this event in this format, and it's optimized for you.
Right? Maybe… I don't know about Grafana yet, but maybe Grafana would want to see this event in a different format, because it's optimized for their query concerns.
And as a result, we, would not have a huge value in having something defined, because both of us would want something different from this optimization.
Sergey Sergeev 01:12:55 Yeah, I… I agree, that's why I'm…
basically raising this question, and again, I hope that our design is pluggable enough to extend it to whatever you want.
But in general, I think most of the backend teams will love to have
all that data arriving on the same packet, so they don't have to do, like, window aggregation and weighting and trying to predict, will I get any follow-up evaluation results, so I need to
Update my tables and a lot of data store.
Do not update that.
Liudmila Molkova 01:13:32 We're going to duplicate tons of data.
It's very expensive.
Sergey Sergeev 01:13:38 Yeah, it's generalization. Basically, if you want to search by both APM attributes and conversation data and evaluation result.
You probably, want to have it on a single… Row in the table.
And otherwise, you will have to do some expensive endurance, basically, if you…
Have separate table for spans, and separate table for evolutionary results, and… ….
Samuel Colvin (Pydantic) 01:14:10 I mean.
Sergey Sergeev 01:14:10 Yeah, go ahead, Samuel.
Samuel Colvin (Pydantic) 01:14:12 We're thinking about some similar stuff, and I see the advantage of this in some ways. I suppose the question is, like, where…
So this is for online evals, right? So you're… Yeah. You're… I mean…
My instinct is what you end up with is some kind of query that alert, effectively, like, match spans with the following attributes, and then from there, you go off and run a query against your data. Like, these don't need…
to be, like, sub-millisecond, sub-second latency. They're, like, need to happen… this isn't a guardrail, this needs to happen at some point in the next 10 minutes.
And so, what you probably do is, once your data is all in your database, you then run your alerting system that triggers some code to run, which basically goes and executes a query against your database to get the data which is needed to…
perform the… the online eval. I don't think this is a situation where… so, you know, when we were back in the long discussion about how we were gonna… what we were gonna do with attributes, and Arise in particular, we're very worried about the fact that all of the data had to be on one…
In one place in the database, so that you could have a query that didn't have to do some complex joins. I don't think that that applies in this scenario, because…
I mean, maybe I'm wrong, but, like, you get to go and run a query later that…
can look up stuff, you know, you can run multiple different queries. The performance is not… and the cost of running the LLM is going to dwarf the cost of, like, running 3 different queries to get 3 different bits of data. All you need is the references on the span that you use to trigger the event that gives you the information to go off and then…
Run your online eval.
But maybe, maybe, maybe your flow is different.
Sergey Sergeev 01:16:01 And this is specifically focusing to support instrumentation site evaluators, so basically, in instrumentation stack in the January 2s we are building, as part of the Python content, we want to run, for example, Ragas right on that container which runs the application, so…
there is an interest from customers doing it, and so on. So, it will be telemetically submitted from the instrumentation.
So, on the backend, you will have to implement, that logic. It's just, one way to represent the data, and we can keep running it
Openly as part of some custom plugin, but, bring it back to this group and just…
Asking if you have an interest in this… in standardizing on this, …
Yeah, evolution telemedicate, but, yeah.
Samuel Colvin (Pydantic) 01:17:01 I'm only one voice, as ever, but… and probably one of the smaller voices, but my take is always this stuff should… we should come… well, once this has been being used for 6 months, and say, we've used this lots, and it really works, now can it become a convention, rather than too early.
But I don't know what others think.
Sergey Sergeev 01:17:19 Any other takes on it?
I… I… I saw somebody else has a topic, that one, and let me away.
We are almost at the time.
Liudmila Molkova 01:17:33 Yes, I was going to suggest, Dylan, maybe we can, chat, and discuss, and then, …
If you have time later today, or whenever you want, …
Maybe I can ping you, where you can ping me, and we can discuss, and then we… … because I'm going to implement things on top of your PR in OpenAI.
Dylan Russell 01:17:57 … Is it?
Liudmila Molkova 01:17:59 And we just can't come up with a single set of suggestions, I'm done.
Just present them to this.
Dylan Russell 01:18:06 Bye, Kim.
Okay, yeah, that sounds good to me.
Liudmila Molkova 01:18:11 Wonderful.
Okay, Ankit, you wanted to say something else?
anksing 01:18:20 I just wanted to mention, I think I might have some thoughts, but I want to just go through that talk, which Sergey had to share my feedback, but possibly I'm gonna do that offline.
Later today or tomorrow.
Liudmila Molkova 01:18:33 Awesome.
Okay, thank you all. Great discussion. Year around.
Aaron Abbott 01:18:38 See ya later.
Dylan Russell 01:18:39 Right.
Aaron Abbott 01:18:40 Sweet.

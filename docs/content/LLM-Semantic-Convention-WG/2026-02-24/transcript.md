SIG: LLM Semantic Convention WG
Date: 2026-02-24
Duration: 63 minutes
Zoom Recording URL: https://zoom.us/rec/share/_tWnh2xI9d6s8Sa1ZN4OtLsd382Rws5Ej4zDARSfuMp8IzNLKe4D7Sc6BtKk5bo_.SanAInoHlH4QlKIQ
============================================================

## Zoom Recording Transcript

Liudmila Molkova 00:01:17 Hi, everyone.
shuwpan 00:01:26 alone.
Liudmila Molkova 00:01:28 Hello!
Okay, so… give me a second, we will get started soon.
Okay, so what do we have in the agenda?
I think I copied this over.
Yes.
Let's take a look at our project board.
And… PRs.
Did they talk about this one, since we are pretty close?
Okay, project board. Okay, this is in progress, we have it on the agenda.
I think this got quiet.
And we had a pull request, and it got closed.
So I'm going to move it back to to-do, since nobody is working on it.
Let's take a look at new issues.
have a bunch in Python contribute.
Okay, Aaron?
It seems it's something deep, and Google Gen AI.
Think… And since Aaron is working on it, there is a pull request, right?
Yay.
Monorapid dependencies.
Okay, Erin cannot talk, that's fine.
Okay, so there is some discussion here.
So it sounds like we are under-testing something.
Starts failing.
Okay, I'll keep it open for now, and let's return back to it if somebody can talk in more details.
Prompt instructions do not show in traces.
Seems it's a lock-in feature?
And there is a pull request.
And it's already… approved.
Does anybody know if we use OTLs?
In this package?
Oh, it's a spend processor, oh no.
Okay.
So it seems like, it's in progress…
This is not… this is.
I think we talked about it last time.
So let's put it on the agenda, and let's see if we can make further progress.
Okay, we are… Pretty much a tower.
Time box. This one, I think we are still…
Still need to follow up on this one. Okay.
Let's move on… To the agenda, we have it packed, let me close everything…
If anybody is new to this group, and you want to go ahead and introduce yourself, Please go ahead.
James Mattei 00:07:10 Sure, I can go. My name is James Mate, I'm a software engineer at a startup called Elastiflo, and I saw there was a special interest group on, you know, semantic conventions for LLMs or Gen AI, and thought I'd want to check it out. Sounds like an interesting word.
So, thanks for having me.
Liudmila Molkova 00:07:27 Yeah, thanks for coming.
Okay, anybody else?
Okay, then let's move on.
the securities pack, now, Kumar…
nagkumar 00:07:47 Yeah, so we can skip over the security, for next week. Memory is a lot more refined. I worked with Rask to get it more refined, so,
Yeah, added in that comment. Let's move that to next week.
Liudmila Molkova 00:08:01 Oh, okay.
nagkumar 00:08:02 Yeah, discuss memory spec.
If we scroll all the way to the bottom, I added a comment 2 hours ago, which has, like, things that we can discuss right now.
Liudmila Molkova 00:08:18 Do you want to present, by the way?
nagkumar 00:08:19 Oh, yeah, that would be nice, yeah, thank you.
Of course.
Here we go.
One shit.
Awesome. So yeah,
Memory spec, a brief overview for people who have not heard of this. Agents, GenAI agents, now utilize memory in multiple ways, and we wanted a way to trace our memory operations and observe what, what's happening through the agent's lifecycle.
So our spec comes up with a few…
Operation names and, details about it, like create memory store, search memory, update memory, delete memory, delete memory store.
Now, this table shows, how it can relate to Google's ADK, AWS Bedrock Agents, and, Foundry memory. So, all these three, what does it support? Like, mapping it directly to APIs that… within those SDKs.
And attribute mapping as well, talking about how, like, the attributes that I have introduced, like memory, store ID, store name, scope, namespace.
And things like that. So, all of this, and how they map into each one of these SDKs. So, then I have linked to, like, sources, on the bottom as well.
So, yeah, memory spec, feel free to… I would love some more comments on how people use it and, you know.
Like, if we want any more changes. There have been a few more comments earlier, and then I had, like, a lot more files in it, and I removed them all.
There were some issues merging mains, so I'll… I'll just squash everything into one commit, and it seems like that's going to fix, a lot of those, issues. So the diff… there was one about, like, what… why is memory different from retrieval, and there is,
a gist that I linked onto this PR about the non-normative spec, which explains all of this.
So what's in the bottom, you can see, like, what's the rationale behind separate memory spans, and…
Things like that. So, happy to, answer any questions.
About this.
Or we can do this async as well, thank you.
Liudmila Molkova 00:10:46 So we would introduce a bunch of a new…
It seems the pull request is… Is… butchered.
It contains changes from… unrelated changes.
So…
nagkumar 00:11:05 merging main kind of messed it up. I'll make sure it's cleaned up and has only, like, what I have as the difference. But yeah, ideally, it introduces a new, new span types,
called GenAI Update Memory, GenAI Retrieve Memory,
And, you know, similar things, so create memory, store, retrieve memory, and things like that, so… memory operations.
Liudmila Molkova 00:11:33 said that… We will introduce new span definitions, and… for…
Independently for create… yeah, I see.
Rate, update, evapor operation.
And this will be client spends, they are, like, directly interacting with the corresponding server APIs.
nagkumar 00:12:03 Yes, so, an easier way to look at it is with
thinking about, like, Memo or MEM0,
And how, like, this draft PR showcases how we can instrument Mem Zero based on my spec. So we did not have anything for Mem Zero just yet, so I created a new package similar to what we did for, like, OpenAI agents.
And how we could, instrument MEM0, and all of the operations that MEM0 does, and how we can map them to
Our span… new spans and all the attributes.
So, yeah, one of the implementation draft PRs. I also have some more implementation PRs linked to this.
Which I'll bring it to the Python counterweb, and we can talk more about, that once this is merged.
Liudmila Molkova 00:12:57 S… Do…
I think it's probably more of an implementation question, but it's a common concept, so it should be in Ooothills, right? It should, like, most of it should be common across different providers.
nagkumar 00:13:14 Yes.
Liudmila Molkova 00:13:18 and… Sorry, for more questions.
Can you guide me through what is JNA memory content? What do we usually see there? It's a complex
trade.
nagkumar 00:13:33 It is. So, we can think of it in multiple levels of scope. So, we're starting off with the lowest scope being the agent in, like, within the scope of an agent invocation.
So let's say it's a long-running agent and wants to remember a few things, it adds stuff into that memory, like, hey, the user requested something, and then it stores that, you know, what is that something in it, and that's the memory scope.
for the agent. Now,
broadening the scope a little bit, like, a type of agent, like a customer support agent, can have some memory on, like, what the agent is supposed to do. So, things around its own implementation, like its own sources, or ways to
function, can be a part of memory. Third one would be a user-scoped memory, so, like, user-facing agents can store some sort of user information, like a travel booking agent can store something, like a user prefers aisle seats, or something like that.
So multiple levels of scope, that we can think of, and each of those levels of scope will have, like, different items.
Based on, you know, what… we can think of.
Yeah, there were a bunch of stories that I wrote about, like, how each implementation, like, how does a travel agent use memory, or something like that, so all of them are linked in, and if any of the links are broken, feel free to leave a comment, I'll make sure it's fixed.
Liudmila Molkova 00:15:09 Okay, nice. Oh, but the content, though…
So this is something we retrieve from the memorandum, and it's… you have an example, it's JSON.
nagkumar 00:15:22 Yes.
Liudmila Molkova 00:15:23 Do we care about the structure?
nagkumar 00:15:27 We don't, it could be anything. So, it could be adjacent, it could be just a string, it could…
be, like, any… anything, basically, so… I can…
Change that to be anything if people have a strong preference, or just keep it as a string.
Liudmila Molkova 00:15:44 It's any right now.
So… It's like the, you know, function result.
Aaron is asking if we are capturing memory, or just the memory interactions.
nagkumar 00:16:01 Memory interactions, the actual items within memory will be treated the same way we treat input and output messages, like redact if you, if by default, and, you know, optional add-on, like.
Be optional for people to trace it if we want.
Liudmila Molkova 00:16:25 I… Yeah, go ahead, thank you.
anksing 00:16:32 So for memory, if I…
So, how would this show up on, like, an existing span, or would it be, like, separate… like, are these, like, captured as separate attributes on the existing span?
nagkumar 00:16:47 So the only existing span that can be modified is the retrieval span. So, let's say retrieval happens from a memory store instead of retrieval happening from
a knowledge source or a rag-based thing, then, we can probably have a retrieval span with additional attributes with respect to, like, what was the memory store ID and things like that.
But otherwise, everything else would be a new span.
like, search memory, update memories in your span. Retrieval and search are pretty close to each other, so in Lang Chain, LANGraph, we only get retrieval as, like, one of the callbacks. So…
We would probably do retrieval, and then if metadata shows some, you know, memory-based items, we add those as well.
anksing 00:17:37 I see. And one follow-up question, so, like, for the agents, like, how would this, come into picture? Like, this would be something, like, agent…
Is fed as an input, right?
when… Trying to respond to a query, for example, like, in case of example of,
Preferences for the seats, if you're a travel booking agent, right?
nagkumar 00:17:59 Yeah, it is through the agent lifecycle, if whenever agent interacts with memory, it kind of gets it. So, like, it depends on how the agent is created and how it's defined, like, would you pull in everything into memory in the first turn, or throughout in multiple turns?
That's up to, like, how… The specific agent does it.
Awesome.
Stop sharing… Thank you.
James Mattei 00:18:33 I guess I had one follow-up question, yeah. Is, is the way memories are stitched into these agents typically done through plain text, essentially, in the system prompt, or are there other ways as well? Because I could imagine you could add a span attribute for, like, how the memory is incorporated in as well, if there's something creative going on there.
But if it's kind of all pretty much the same, maybe you don't need that.
nagkumar 00:18:55 Yeah, sometimes it happens via, as you said, within the system message, or via our tool call, based on however people design their agents. And all these, like, standard ADK, Bedrock, and other agents, like, they have a standard way of doing stuff.
James Mattei 00:19:14 So with the current span definition, would you be able to differentiate if it's done via a tool call or into a system prompt right now?
nagkumar 00:19:23 It would be up to the implementation, so however the SDK would, or, like, the framework would implement it.
I would propose create a new span whenever there is, like, a memory operation happening, similar to what this, you know.
The new spec suggest, and try to get that implemented in all these major frameworks.
James Mattei 00:19:48 Like, what you're saying.
Liudmila Molkova 00:19:49 Yeah, sorry, James.
Okay. So what you're saying is that we can have an agent span, Right, invoke.
agent, then we could have maybe LLM call, then we'll have a tool call.
Right? And under it, there could be a memory operation.
nagkumar 00:20:14 Yep.
Yeah, it could happen there, it could happen right after Invoke Agent.
As well. Or in parallel to, like, on the same level.
Liudmila Molkova 00:20:30 Cool. Yeah, it makes sense. So…
This is a big change, and just doing a mental check, through my…
So what we usually need. You have prototypes.
nagkumar 00:20:46 Yes.
Yes.
Liudmila Molkova 00:20:48 This is, for Mem0, and you also checked that it works for AWS ADK and Azure Foundry.
nagkumar 00:21:01 Yes, Foundry Memory ADK, and, Bedrock agents. I have, like, ways of… or a table which shows how to implement it, but I have a implementation, for, crew.ai, Mem0, and Langtrain.
Liudmila Molkova 00:21:23 Damn.
Awesome. So then, it's a matter of,
You get in the review, we have all the checkboxes checked, and… Done.
It would be wonderful to have it implemented in Utilos, and then…
Leveraged in some of the instrumentations.
Who… is there someone who is interested in reviewing it from, like, a specific vendor perspective?
Aaron, do you think we can bring somebody from ADK to take a look?
Anirudha Jadhav 00:22:10 No, I'll do it from the AWS side.
Liudmila Molkova 00:22:13 On the agent code part.
Nice, thank you.
aaron 00:22:18 Hey, can you hear me alright?
Liudmila Molkova 00:22:21 Yeah.
aaron 00:22:22 Okay, sorry, I've… I… Did,
Try to share this with somebody internally.
I'll see if I can get their feedback and leave some comments on here.
Liudmila Molkova 00:22:34 Awesome, thanks a lot.
And now, Kumar, can you place,
fix the PR so people who review it, only see the content that's relevant.
nagkumar 00:22:44 I'll do it right away. Thank you.
Liudmila Molkova 00:22:46 Yeah, thanks a lot.
Cool.
The folks who, from Splunk, Cisco, you work on link chain, and it's probably irrelevant, do you think it's interesting, related to your cases?
Keith Decker 00:23:13 I think we've had some talks recently about memory,
I think we are keeping an eye on this PR as well.
Liudmila Molkova 00:23:26 Cool, thank you.
aaron 00:23:30 It was on the guardrails, right? The question was on the guardrails PR, or the memory one?
Liudmila Molkova 00:23:36 The memory one.
aaron 00:23:37 Oh, okay, okay, I'm sorry. Yeah, I can see if I can get someone from Educated to take a look.
Liudmila Molkova 00:23:59 Cool. Moving on to the next topic, Ankit, the server spans.
anksing 00:24:08 Yeah, so I can start sharing my screen, I'll report to that.
Liudmila Molkova 00:24:12 Yeah, sure.
anksing 00:24:14 It's wrong.
So, you're still a nurse also specializes? Especially in Brazil?
Liudmila Molkova 00:24:25 Not yet.
anksing 00:24:25 Starting? Yeah.
Liudmila Molkova 00:24:30 Yep. Awesome.
anksing 00:24:33 Sounds good, Pat.
So, I want to start with, like, GenAI semantic dimension right now, like, the telemetry we have for… is for capturing what happens on the client side, or… and then capturing all the GenAI-related operations.
However, like, with the agents becoming more complex, and also, they do run…
Can't run in asynchronous mode.
like, having server-side telemetry is as crucial as a client-side to get an end-to-end picture of what happened, and how I initially came up with the response.
And, with that, like, agents, are becoming more and more complex, where they interact not just with tools, with other agents as well, and most of the time it happens in an async fashion, and not brought in any resources, any connections on any, server clients anywhere, everywhere.
However, like, that poses a challenge for the observability as well.
Where, if you have a long-running operation, or if you have, like, an agent invocation that happens in a sync fashion, you probably cannot have something, either on the client side or just at the server side, where it accepts a request to kind of pull, the entire execution of,
Execution of events as it happens.
And, some of the, some, like, we do see, like, some of the providers, like OpenAI or even Google.
have some, capabilities where you can run your, like, do the execution in an async fashion. For example, in OpenAI Responses API, you have this name, background equal to true, where you submit a response, response, and then
Polly later, so… and this happens behind, the background.
And, especially… and also, very similarly, things happen for, like, video generation, because it can take, take a longer time than your usual HTTP calls, right?
So, for those reasons, like, we want to propose two things, actually, basically three things. One is…
How do we…
Capture these operations on the server side, so we would want to get into the realm of designing spans for capturing these operations on the server side.
And then the second is, how do we model the async execution of these operations? And the third one was about, like, if these are long-reading operations, how do that get modeled? However, for the long-reading operation, I want to table that, because there is already some discussion going on in semantic conventions, like.
general, not just Gen AI, and it's, I think, not just specific to Gen AI. And I think Trupas helped me navigate that, so… that's not what I want to discuss today, but the thing that I want to discuss is more about how can we model async operations, and then the server-side Gen AI space.
So,
And I have this small example just to give a mental picture of how these things can work, or currently, actually, it does work, in a way. So, for example, a responses API, this is a small snippet which shows background equal to true.
Where a client posts this, it gets some sort of operation ID. Here, it's a response ID, basically.
In case of, responsive API, and then…
server says, I've accepted the request, and then client gets a response ID, and if the client wants to poll, they can poll, but then the execution of that request happens in the background.
And then…
Liudmila Molkova 00:28:11 I think Erin has a question.
anksing 00:28:12 Oh, yeah, sorry, I'm not imposed.
aaron 00:28:14 No, no, it's okay. I can, I can wait until you're done.
anksing 00:28:18 Okay.
And then, once the request gets accepted on the server side, a sync execution begins, and then actually the agent execution happens.
And if it has to call any LLM, it calls it… And then…
It calls any tools it needs to.
And this is a very simple example of, like, an agent calling an LLM.
And then figuring out which tools to call, it gets… then it calls the tool, get the response.
And then, finally, it takes that response and gives the final response.
However, like, in this case, like, this shows a very naive way of putting it, where, hey, LNN, like, once the request starts executing, it's always gonna be…
It shows, like, it's kind of going in a sync fashion, but that might not be the reality, where even a call to LLM or a call to a tool can be in a sync execution.
So, this is just to give an idea of, like, what the problem we're trying to solve.
So I… actually, Aaron, I'll take your questions now, before I go into another… Yeah, yeah, yeah.
aaron 00:29:28 Yeah, I think this partially addressed it, but, I was a little confused what we mean by server and client. So, like, it looks like in this case, the first… the first request is more about asynchronous,
Inference, right, where you have basically long-running operation, like you mentioned, but.
you know, in the case… I was kind of confused what you mean by server, because we do have agent observability stuff where we're seeing the traceland from the agent…
anksing 00:29:58 I don't know, I think I lost you for a moment at the… at the end.
aaron 00:30:04 Yeah, sorry, I… it's probably a lot of background noise, but yeah, my question was, like, from… this seems asynchronous from the client's perspective, but from the agent-server perspective, it seems kind of normal, same as the other stuff we modeled, right?
anksing 00:30:19 Yes, but I think, that would be entirely true if you're doing, like, execution of the agent in,
in a synchronous way, but then I think… say, for example, so, when I say this server, this is basically an agent deployed on a server.
Right.
Which could be, like, I could, gather my LinkedIn code and put it somewhere, or in Foundry there's agent service, or third party, like, where you can have this deployed as a service to be consumed, right?
So, it could be anything, though, when I say the server here. However, like, for the agents.
when it starts executing, when it has to call LLM, so instead of, like, here, the LLM calls are using responses API. Responses API, again, can be done in a sync fashion at this layer, where agent is calling LLM, right? So…
So I think…
it, like, essentially, it could be a sync in any of these areas, where when it's calling a tool, it can happen in a sync fashion. If it's calling in, that can happen in a sync fashion, right?
aaron 00:31:27 Okay, thanks. I think I'm gonna listen for a little bit, get some more background noise.
Liudmila Molkova 00:31:34 I'm kind of curious, Enkid, so there are… anything can happen in sync or async fashion.
And there is… it will… like, the trace will look accordingly to how it actually happens.
We… there are limited things we can do.
We can introduce the server Span for agent.
maybe a server span for LLM?
anksing 00:32:01 And maybe a version of async.
Liudmila Molkova 00:32:03 client spent.
And all of those tasks are…
trivial in their nature. Like, there is no rocket science, it's just a matter of which attributes to pick, and that's it.
The rest is just the context propagation and how people write their code.
So what… what is special? Like, what kind of…
Support your… you're still sharing your screen.
anksing 00:32:28 My… is my proposal.
Are the diagrams shown?
Liudmila Molkova 00:32:35 Yeah, yeah, it's shown now.
anksing 00:32:36 Okay, yeah, awesome. So, actually, we wanted to understand on, like,
I know, like, we were also digging through, like, semantic conventions and what's the closest that's available to, kind of, mimic our, like, like, async operations, and the thing that came across was messaging, right?
So, when it comes to, like, async, executions of these agents, or any kind of LLM generator-related operations, kind of how do we model them from that,
Like, the limits your point of.
Point of view, like, should it be modeled similar to, like, producer-consumer, or, like, the messaging?
Or is there any other thing that's available?
That could help us. And I think these are the questions that we have in the,
Like, after discussing with Trask as well, like, we kind of put down them, in the, in the sixth meeting, like, the doc.
Liudmila Molkova 00:33:36 Yeah, let's talk about it, I think Surya has a question.
anksing 00:33:40 Oh, yeah.
Hey, sir, please go ahead.
Surya Teja 00:33:42 Yeah, so have you seen a loss of context or anything happen when you were instrumenting async calls? Say.
your LLM calls a tool, and for some reason there is some race condition or something, and context is lost. Have you seen such kind of scenario?
anksing 00:34:05 Actually, to be honest, I've not instrumented any async execution as of now, so I haven't seen that, but at least I've worked with a few of the, like, internal things where we do do this in async fashion. I mean, those are more like bugs, but…
We haven't seen, like, context lost per se, but yeah, there could be some bugs where…
We got the wrong context, things like those, but…
Surya Teja 00:34:33 Yeah. But yeah, we haven't seen that kind of issue.
anksing 00:34:36 Yeah.
Surya Teja 00:34:38 So, when you're saying about producer-consumer thing, this more looks like a span linking kind of thing, in my opinion. So, were you leaning towards that?
When you were explaining this?
anksing 00:34:50 So…
Yeah, I think that's one way of modeling, so we wanted to get some feedback in today's meeting on how we can do that, so let me open the…
I think that's all I had in my proposal lock right now, and I think I have one PR I can share in the link in the chat for invoice, agent server span. That's just a preliminary PR.
But however, I think the major thing we want to discuss was more about, like, how do we kind of model this?
When it's… when it's happening in interesting questions.
Surya Teja 00:35:28 Thanks, Ankatia.
Liudmila Molkova 00:35:31 So maybe, let's break it down. I think messaging is an interesting analogy, but I don't think it applies directly.
anksing 00:35:38 Perfect.
Liudmila Molkova 00:35:39 So let's break it down to first case, the client case.
What happens on the client? You start a long-running operation, right?
It's one span.
Which is fine.
you get something back, the operation AD.
anksing 00:36:04 Yes.
Liudmila Molkova 00:36:08 Then, the next span, it may happen in pretty much any context, the same context, different context, it's polling, right? Yet status.
you can stamp the same operation ID.
And then finally, at some point, you get that… you get the…
Pull… the status shows result, so it's a loop.
And finally, you probably get… result. It's another span.
Or maybe you get it as a part of the… in the loop, right?
Either… it depends, doesn't matter.
So, none of this is async. Well, it's async in terms of code, in terms of tracing, it's just… it's consequent, right?
Ideally, in a perfect world, if somebody is actually awaiting this thing.
they made an effort for it to be under the same trace. So it's either there is an overlapping span, this is probably some kind of workflow…
Or maybe, at least, they put an effort into propagating context, and they not only have the same operation AD, but they only have the same trace AD.
anksing 00:37:44 Actually, like, if the client is polling on the results, and then I think then, to be honest, like.
If I was doing it, I would probably just create a span for agent invoke, and then pull it, and then finally, when it ends, set all the attributes, like output messages and things like those, right?
Exactly, yes. It looks exactly like what we have right now, right, on the client side.
Liudmila Molkova 00:38:07 Right.
anksing 00:38:08 Yeah, it's just that, if I remember correctly, the API that you folks have.
Liudmila Molkova 00:38:14 People can do either or.
Yeah.
anksing 00:38:16 And it's just that this one is a wrapper around.
Liudmila Molkova 00:38:20 This thing, to some extent.
So, if people do it differently, then they can
Make sure the context propagates, and maybe the spans don't have an overlapping invoke agent.
But it's up to them on how to propagate context.
So that they are under the same trace ID.
The worst case is that all of this This is the worst case.
All of this spans… Are in different traces.
And there is the seam…
I think it's out of the scope of operation… of instrumentation for the client.
to actually…
control it. You can control individual spends, you can tell people how to propagate context, you cannot force them to write the code that propagates context.
anksing 00:39:22 Okay.
Liudmila Molkova 00:39:26 And we can introduce spans for the small things, if it's a common problem.
But it's probably trivial.
anksing 00:39:42 I think this is the client case, right? So, actually, the thing, I wanted to also, like, focus on was also the server side, like.
Assuming you don't have client-side telemetry, for some reason, right? You can assume. And then, on the server side, how do you capture this,
Invoke… agent invocation operation, like, as it happens.
Liudmila Molkova 00:40:05 Yeah, we can talk about server side. Anything else on the client side?
anksing 00:40:09 Hmm.
I think PlantSense is…
Trask Stalnaker 00:40:13 I have a… I have questions. So…
This is… so what you're saying in the best case, is you're saying that the span would… there would just be one… because it's essentially sync, it's just pulling, you're saying that the, ideally it would be one…
Span for that full operation.
Even though it's one long running, and you're pulling, and you just finish it at the end.
Liudmila Molkova 00:40:47 It may be both, right?
So you… You have an encompassing span, and you also have the individual pieces.
Like, start operation, get status.
Trask Stalnaker 00:41:02 Okay.
Would those start… would those individual pieces be events?
or a…
actual spans that then propagate. Would those be the spans that propagate down? The reason… what I'm getting at is, if you go to the… the span kind definition in the spec, we'll have it linked below.
There's some language there that made me nervous. That server…
Is, span covering, a remote request while the client awaits a response.
And so, if the server In this case, where it's just starting a long-running operation.
it's… I guess you could say the client… like, it's awaiting the client response… that the client is awaiting a response, in that, asynchronously, it's pulling for a response.
Liudmila Molkova 00:42:14 Well, server doesn't know. So for server, this is just the sugar that exists in the application, right? This is an actual call to the API. You're…
Doing something on the server, so it's a span?
And from the server perspective, the request you're making is to start an operation, not to complete it.
So the server should probably be server, because
The only request it's handling is to start the long-running operation.
Trask Stalnaker 00:42:50 Okay.
Okay.
neil yashinsky 00:42:53 Couldn't it? Couldn't it be restart an operation?
I didn't hear the whole question, but you said the only thing it could invoke is start?
There can be, like, a resume, for example?
Liudmila Molkova 00:43:09 It could be a separate API, but…
neil yashinsky 00:43:14 Okay, yeah, sorry, that was a silly question.
Trask Stalnaker 00:43:19 So, oh, before I go, go to my next question, Ankit, go ahead.
anksing 00:43:25 So, I think, I definitely, understand the part of, like, the only thing that services is starting that long, you know, social, right? But, however, like, the goal is…
the… like, the invoke agent server span started, and then the execution is going to happen in a sync fashion? How do we kind of put all that thing together to kind of make meaningful…
Telemacy for customers to consume, right?
Liudmila Molkova 00:43:55 So, I think… there are two things server can do, right? It…
can have a span for this operation, for this request, right? It's an incoming request to start an operation. It can have this span.
You reported…
It can. There is a different kind of thing, the whole flow that happens on the server.
anksing 00:44:22 Yeah.
Liudmila Molkova 00:44:24 And it seems to be… a separate Span.
And server can decide which one of them to emit. And I think the right answer is probably both, because you want to know
How did the starting happen? It's just an operation.
And then there is the… processing of this whole thing. It's another operation.
anksing 00:44:56 So, one quick question is, for the server, like, accepting that request site, and we're kind of instrumenting that, so would that be, like, a server-side invocation span?
Liudmila Molkova 00:45:08 I think this is just HCCP,
or their PC span. It's not Gen AI, it might have some Gen AI specifics, but it's not even…
really interesting kind of Gen AI world.
Trask Stalnaker 00:45:23 It's just the… it's just the operation that kicks off the long-running invoke agent.
anksing 00:45:31 I see, I see, okay. So this is just kicking off an invoke agent operation, right?
Liudmila Molkova 00:45:36 Anyway.
Scheduling it, if you will.
anksing 00:45:39 And queuing it.
QA, it depends, yeah.
Got it. Okay, so after that, or no, after that, I don't know, like, once that gets…
ticked off, and when the actual agent execution starts, that's where you would create an invoke agent spanned on the server side.
Liudmila Molkova 00:45:59 Right, so the server, side, the Gen AI.
And as you mentioned, it can be a whole thing, right? But nothing stops server from doing it asynchronously as well.
So it can be… it depends, the answer.
anksing 00:46:27 I see. So, Gen AI in location span is kind of a logical span, right, in a way, like, kind of…
you can have HTTP spans or other things happening under the hood, right?
What I'm trying to understand is, like, invoke agent span would give user a picture of, like, okay, this is what all happened, like, these are the inputs that went to the agent, and then this is the output came, and then another
Under it, like, there could be more information on how actually these things happen, right?
So…
Where do we put that layer of this logical invoke agent span, which kind of captures these high-level operations of invoking an agent on the server side, right?
Liudmila Molkova 00:47:07 So I would imagine if there is one span…
on the server for Invoke Agent, if you can describe it as one span.
You… it would be a counterpart of the
Alliance side Invoke Agent, it would contain similar information.
was… Respect to what server knows and what is useful there.
anksing 00:47:32 Yeah, so I think with,
a sync execution, like, things like GenAI output messages.
It won't be available at the time of agent, invoke agent server-side span creation, right?
Or, like, it would be available, only after the operation, that end-to-end agent in location ends.
Liudmila Molkova 00:47:57 So I'm a bit lost what we are talking when we're talking about server…
Invoke Edge, this is this, this whole flow, right? Or is it a part of the flow?
anksing 00:48:20 Okay, so the server-side JNS fan, I think, what I was thinking would describe more about…
Server accepted this invoke agent request, like, what all it does…
And how do we capture on what all it does to kind of fulfill that request?
Liudmila Molkova 00:48:40 The request, or long-run in operation?
anksing 00:48:44 Actually, there are longer operations, not just the request here. The request that comes in, like, the server initiates the invocation of agent, right? And then…
Agent execution starts, right?
very close, LLMs, tools, things like those, and that entire thing.
Liudmila Molkova 00:49:02 So, the full flow.
anksing 00:49:03 Yup.
Liudmila Molkova 00:49:06 And if it… if it's the case, then we can put
We would know everything that happens on the server, and it would have children.
That may or may not be also… Export it to the color.
So if we try to…
Oops.
So let's say we have, this is the… Start operation.
on server.
This is HTTP, for example.
Then we have… Jet.
I'll show HTTP.
And we will have… A big, long server.
Invoke urgent.
This is Gen AI.
What are the relationships between those? So this guy… Happens at this.
Tarte.
And it's probably, maybe linked to Invoke Agent?
No other direction.
So I would imagine Invoka Agent will be a child of… Incoming request.
Maybe.
A sibling of this.
So that you can disable it. Like, if you don't care about HTTP layer.
And handling of the start, it can be a sibling, and then it will be linked.
anksing 00:51:28 Excuse me.
Liudmila Molkova 00:51:34 And this guy, well, we can also add link to it in theory, to… This one.
Trask Stalnaker 00:51:43 Why, why not, parent…
child, and I mean, if you don't want the HTTP span… I mean, if you disable that, you would just propagate the parent span on down directly.
Liudmila Molkova 00:52:05 Yeah.
Trask Stalnaker 00:52:06 Trying to avoid links.
Liudmila Molkova 00:52:08 Okay.
Trask Stalnaker 00:52:09 Sorry. No, no, links are fine, just if, Yeah.
Liudmila Molkova 00:52:19 Yeah, that's a good point. It's just the visual, visual noise of it, but… but you, you need to…
Well, the visual noise is present… present either way. It's just deeper.
Trask Stalnaker 00:52:30 noise.
Liudmila Molkova 00:52:32 So, it will be…
So there is… this is the server, right? There will be Invoke Agent on the client, or some version of it.
Why aren't.
And… this… There are… there are, by default, there will be 3 layers.
With parent-child, with links, there will be two layers.
But visual noise is still there, the volume is still there, backhands can hide it in some other ways.
Probably not important.
Trask Stalnaker 00:53:13 I see, okay, okay.
Liudmila Molkova 00:53:25 But the coins… coins are interesting. So is it internal? Is it consumer? Probably consumer.
Because it does not evade.
The client does not evade it.
Trask Stalnaker 00:53:42 Do you want to put the… is that start… is the green HTTP… is that a server HTTP, or a client HTTP, or both?
Liudmila Molkova 00:53:51 Only server?
So there is also a client HTTP, right?
Trask Stalnaker 00:53:57 Possibly.
Liudmila Molkova 00:54:01 So nesting is getting deeper.
anksing 00:54:05 I get off.
Trask Stalnaker 00:54:21 Yeah, okay, so the server-side invoke agent then
Yeah, that makes sense to me, being… a consumer, I think.
Or an internal. No, internal… we like consumer for… because it's got a parent.
Liudmila Molkova 00:54:45 Got it.
Parent…
Trask Stalnaker 00:54:47 And it doesn't wait for… Yeah.
Parent doesn't wait for it.
Liudmila Molkova 00:55:03 We have just 5 minutes left, and we want to figure out what to do with some of the other PRs. Are we… do we have some next steps here?
Trask Stalnaker 00:55:13 One last question here, is it okay, like, if invoke agent could be also synchronous?
In some cases. In that case, would you… is it… would this mankind be server?
Have we done that before in SimCon for one?
Span might be… Consumer or server, depending on Situation.
Liudmila Molkova 00:55:48 I don't think we have done it before.
Trask Stalnaker 00:55:55 Okay.
Something… I'll think about it.
War.
Liudmila Molkova 00:56:00 Yeah, from my memory, at least in Microsoft libraries, this is, like, the synchronous invoke agent on the client is a sugar.
I might be wrong.
Trask Stalnaker 00:56:22 So you were asking next steps… I think…
Next step's probably for, Ankat and I to,
Take this feedback and try to put together a…
Next steps. Concrete proposal, that aligns with all of this information.
Liudmila Molkova 00:56:49 Awesome. So I wanted to…
Check if we can make progress here.
This is a workflow operation, so this is the operation intended
To wrap multiple agents at the same time.
And… I'm a bit lost right now. I'm sorry, I've done some… analysis,
So, I think I see two patterns, and I don't think we can… we can make things perfectly. So, in one case.
We kind of clearly see that
the orchestration happens as a separate thing. It's not an agent of any sorts, you cannot think about it as an agent.
This is an example of it.
Sorry, it's Curio AI, it's a typo. But in case of ADK, and also in case of OpenAI,
You can build… You build the orchestration as an agent.
In cases… in case of ADK, you kind of know that it's…
Agent wrapping agents. In case of up in the air, you don't even know that.
So…
the… probably the question… only question we maybe can make progress on, if Erin is still here, and if you can talk.
So you brought up that for…
the ADK case, and that you… you think that the… the… this…
Root adjunct is also an adjunct.
It means, effectively, that you…
If… if we treat this as an agent, pure agent, then…
The workflow metrics and agent metrics are one thing.
Do you think it's something we need to push for to solve?
Aaron Abbott 00:59:08 I mean, I think… I think it's okay if ADK is slightly different. Like, I… I kind of wish it was more like the others and had workflow.
But I see your point. I think…
one thing I was suggesting was maybe we could put workflow ID
or whatever the identifier is on the agent spans to accommodate, ADK, or we could do, like, a GCP.att attribute if that works better to not, kind of, muddy things up.
But, like, the reason it's like this, I think, is mainly that if you look at the class hierarchy and stuff like that, they model it as that you could also subclass and do your own, like, random control flow, so if your workflow was just some code that you implemented, it all implements agent class, and then the runtime kind of just treats it uniformly.
So I… I think… I don't think we need to, like, block necessarily. We'll… I think ADK would just keep doing whatever it's doing with the invoke agent, and then we could think about putting the workflow identifiers on
the agent's been for 80K.
Beautiful.
Liudmila Molkova 01:00:12 Yeah.
Ridhima Satam 01:00:12 I would also like to add here, like, I think, we mostly worked on this workflow for the purpose of the agentic frameworks, but I would say we can… or we should extend this to… or maybe there was some thought around
The workflow not just being the multi-agent orchestration, but it could be also, like.
static, predetermined sequence of operations, like LLM and tool calls, and if you want to group that.
somewhere we spoke about it, like, if you want to group that under a particular workspace, like, the time taken to do all those steps, LLM invocation, or sorry, tool calls or retrievals, everything together, we can make it as a workflow. So, we shouldn't just restrict this workflow to being an invocation of agent. It could be, yeah, in some places where there's an agentic framework, we can map that as a workflow for langchain and
Creo AI could be, like, this one-off, and then I have also attached in the description where… where I'm explaining you the same example of
the in-house frame… in-house example, where you don't have an agentic framework, but you have, like, a series of operations of LLM invocation, and you… you first start a workflow, and then end a workflow, and do everything in between.
So, yeah, and then for the… for the purposes of the ADK, where the agents are, type of workflow.
We can add attributes like workflow type for that.
say a workflow… that agent, invoke agent will have a workflow type of, say, sequence or parallel, and that could be the same for our workflow span. Like, I'm trying to separate out now workflow, invoke workflow and agent… invoke agent.
And then have these attributes on those, so that we… we know that there's a workflow span going on, with the benefits of having separate metrics, and then there is invoke agent, which could be a part type of a workflow.
And then we also introduced, try to introduce one more attribute where we want to say the conversation ID, like, we briefly spoke about it, and we can put those attributes on both of the spans, like, just to give you an, like, overall, like, a summarized, view of
how they would separate it out, and not just restrict workflow to just agentic steps, and I can then change the definitions a little bit, like, where I've added workflow is a, like, multi-agent orchestration.
Liudmila Molkova 01:02:36 We… we need to drop.
Aaron Abbott 01:02:39 Yeah, I'll definitely take a look. I think I owe you a review here. Could we do that iteratively, you think? Like, could we start with this and then address that language in a follow-up?
Liudmila Molkova 01:02:51 But my main question, can we just start with an attribute? Why do we even need an operation?
Like, if attribute is enough, if workflow can mean anything.
Then why don't we start with just an attribute?
Ridhima Satam 01:03:09 Are you saying attribute on the invoke agent?
Liudmila Molkova 01:03:13 just attribute workflow name, it can appear.
Somewhere.
Anyway, we need to drop. We are over time.
Aaron Abbott 01:03:23 I'll put you on Slack, Redima, sorry about that.
Yeah, sure.
Ridhima Satam 01:03:28 Thanks.
Liudmila Molkova 01:03:29 Yeah.
neil yashinsky 01:03:30 Thank you. All right, thanks, Lydna. Thanks, everyone. Bye.
Liudmila Molkova 01:03:34 Thank you.

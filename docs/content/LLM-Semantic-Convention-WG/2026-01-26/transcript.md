SIG: LLM Semantic Convention WG
Date: 2026-01-26
Duration: 30 minutes
============================================================

## Zoom Recording Transcript

**Sergey Sergeev** 00:16 Here, then type in Monday.
Yay.
**nagkumar** 00:34 Hello, hello.
This, this one.
**Sergey Sergeev** 00:53 Yeah, let's wait… A bit of time.
For more folks to join.
If you have any agenda to chat about.
**nagkumar** 01:08 Oh, yes.
**Sergey Sergeev** 01:55 Okay, we have a few more folks on the call.
Yeah, let's wait just one more minute, Yeah, everybody on the call, please add your name to the attendees section of, Of the document, and if you have any topics, to discuss for Agentic stuff.
Added to the agenda.
Yeah, we probably can't start, so… In general, I'm wondering if you, do any agent name or workflow name propagation from the parent span down to the child span.
all the way to LOM invocation Span.
Specifically for… metrics, it's very helpful to have agent name and workflow name, set on AOM and vacation, so the metrics For token usage, the duration can be… attributed to… agent or workflow.
I'm wondering, what you do in your instrumentation layers on Microsoft site.
**nagkumar** 04:22 We don't… I don't think we push things down.
We… whatever is in the root span, we keep it as the root span.
And I guess the onus is on the viewer side of things to pull Whatever is in the root span, and make sure that persists in the view, but not in the actual lake.
Time spans itself.
That's something that I've observed, But, yeah, this… building something here would be important. Notice that whenever There are multi-agents, and there are async agents.
And then there is… it'll be hard to, like, link back up to the parent span.
If the context is lost, so…
**Sergey Sergeev** 05:17 Yeah, I think bubbling up, from… LOM and vacation. So, there are basically two, three different approaches. One, you push down, agent name and workflow name down to the child span, so, you can set it on LOM and vacation.
spans. Second approach is you try to bubble it up, but I think it's… Near impossible.
To do, and finally, you can process the trace. You can assemble the trace on the backend and try to parse Basically.
that graph.
To identify those relationships and to produce the needed metrics.
Which requires, basically, bytegant functionality.
So… In general, I just wanted to know what you guys do and find helpful.
From instrumentation, and if, If we contributed it to Upstream right now, we do it, in our Splunk distra for OpenTelemet.
And this is the same approach, which, JSOOP instrumentation library set doing, basically.
In general, The works…
**nagkumar** 06:58 Yeah, I don't have much thought, Is that a issue, or a… VR associated with this?
**Sergey Sergeev** 07:08 Not yet. I think, The last time we discussed it, in… the broader SMIT Convention Group, the… it was unclear the benefits, of doing it, and basically polluting the pure LOM invocation… LOM, attributes. Basically, if you do that, so now you can say that, oh, a manification can have agent name on it, And I think it, was not enough supporting.
proves that it will be useful. I think now it's, We have some proofs on our side, so… I just wanted to check if it's the use case for you. Looks like not yet.
But then…
**nagkumar** 08:07 Yeah, none of them.
**Sergey Sergeev** 08:07 the field.
**nagkumar** 08:08 But if there is some more detail on it, I can pass it along to, like, actual teams which are working on, you know, the Microsoft Agent Framework, and see… How… what they think about it, and report back.
**Sergey Sergeev** 08:42 Yeah, we can do it.
Memory spec do you want to share?
**nagkumar** 08:49 Yeah, I can start sharing my screen.
**Sergey Sergeev** 08:52 We've missed them.
**nagkumar** 08:53 Okay.
Oh, okay. I might have to… Rejoin.
**Sergey Sergeev** 09:03 password.
**nagkumar** 09:03 Let's see if this still works.
Share… nope.
I might have to rejoin. But yeah, feel free to share the screen with, my… PR, that should be a good starting point.
**Sergey Sergeev** 09:22 No, and I… it's…
**nagkumar** 09:26 I'm gonna rejoin.
**Sergey Sergeev** 09:29 No worries, you can… Okay, to wait.
**nagkumar** 09:54 Okay, I'm back now. So this PR is pretty.
**Sergey Sergeev** 09:59 Do you want to share?
**nagkumar** 10:01 Let me double-check if this is working again.
Yes.
There we go.
Okay, so this one, I saw the span as trace viewer, but… Let's… yeah, memory span. Whenever an agent is executing, there are… lots of memory providers that agents can use, or, like, any agent framework can have its own memory provider. And the idea is that There are certain operations which are happening, like searching memory, updating memory, creating memories, and deleting memories.
Which would have a lot of benefit if we have some sort of way to look into what those spans are, or, like, look into what those operations are doing. So, this PR shows some… Way in which we can add memory attributes into the Gen AI semantic convention. And this is more specific for agents, so I brought it up here, and tomorrow I'll bring up, like, other stuff, but I can bring this up tomorrow as well.
So, ideally, the, you know, prototypes will be smaller, but here I have added, like, a lot of different, ways in which you can run this. So, like, I have a lot of Python files which shows You know, which just runs and creates traces, and you can export it to whatever viewer you want.
And check your views there, but I'll be deleting most of the files, so you will not have so many changed files later on, as I've mentioned. All of these files are, like, temporary, and I'll delete them.
But the idea is in this key semantics section. Like, search memory, update memory, delete memory, so we can go over each of those in… My… Memory spec, so yeah, what… What would search memory be, what would update memory be? And all the attributes within those are all listed here.
And a simple… one of the samples in my prototypes is this customer support agent. Now, I want to show, like, with the memory span, without the memory span, how things would look like. Like, a simple, example of… A customer support agent.
trying to say, hey, someone says, I was charged twice for my subscription, and the assistant kind of figures out What that was, and response with the right context, right response. So, you can see, without memory, it would just be, like, a chat span, responding with a chat span, maybe some tool calls associated.
But as soon as we add the memory spans, we are like, okay, we are checking a memo… creating a memory store, and then searching the old memories, if there was any, with respect to this particular store, and then, you know, adding that into the chat context, and then once you get the response, you update the memory and, you know, do multiple things like that, and delete the current session if it's not needed. So, that's the idea, and this showcases, like, all the operations and all the key value attributes associated in that span.
Now, the… The sample will show, like.
more such examples, like I have, I call them stories, customer support, shopping assistant, and multi-agent research, and things like that. So, would love any comments that the team has, on this particular, memory operations, and, like, the whole new memory spans that I'm trying to propose.
**Ridhima Satam** 13:55 I see, are you proposing metrics as well, like a duration metric for a memory operation?
**nagkumar** 14:04 With this, I don't think I have added anything with respect to metrics, but yeah, feel free to comment on this with, like.
anything that would help, I'm happy to add them in.
Like, when you say duration with respect to memory, are you referring to, like, how long the memory stays alive for? Like, time to live sort of duration?
**Ridhima Satam** 14:29 I think I saw some of the spans, which is complete about search, I think search, span, so how much time did it take? Like, if you think… Oh, that's it.
**nagkumar** 14:40 Yeah. The duration in which… time taken to run the search. Okay, that makes sense, or, like, time taken to create a memory store, or something like that.
Okay, I will add that as a feedback item and see what we can do for duration of this memory, and try to update this, if there is anything we can do with it.
**Ridhima Satam** 15:07 And in addition to that, like, previously, like, we… when we had to, present certain things to the SIG, they came up with, like, the necessity of creating a span, like, for example, if any… so, it's expensive, right, to create a span, so instead of creating a new span, would it be okay to put it on that agent, particular invoke agent span? Do you think that would… be sufficient.
What extra… Why do you need an extra span? I mean, just… Yeah, I feel…
**nagkumar** 15:39 That's a good question. So, when it comes to memory operations, the idea is that there can be multiple operations happening within an invoke agent.
Now, if we add, let's say, create in the… let's say there is an agent which creates a new memory store, or creates a new memory object every time there is a new request that comes in. So, like, every time there is a new agent invocation.
So, maybe we can add the create stuff within the invoke agent, but then the following operations, like, let's say there is some more search happening, or some deletion of some previous memory happening, that would be harder to denote within existing spans.
The closest we can come to is, like, if memory is used as tools, like, how different is a tool attribute, tool called span, versus… this new proposed GenAI memory, spans, and that is, like, a little debatable, because this memory span would give the opportunity for users to have more specific attributes compared to, like, a tool called span, which is, like, more generic on, like, what the tool is, what the arguments are, inputs, outputs, and things like that. So that's… the idea behind it. So, I think the duration part, I just found that it's… time per output token, time to first token. These are, the Gen AI regular duration stuff, but we can add something similar, based on these existing duration rules.
And add them as… metrics for the… memory span as well. I'll add it to this proposal.
**Ridhima Satam** 17:28 Yeah, yeah, thank you.
**Sergey Sergeev** 17:32 Yeah, in the same spirit, playing the devil's advocate, so, can we use just database search, or database separations here?
The, the, the, the undefined database separations.
**nagkumar** 17:49 Yeah, database operations. I should look into what, GenAI says about database operations, like, not GenAI, but OpenTelemetry database operations.
They could be pretty close, but I'm sure there will be, like, a few GenAI-specific attributes, maybe, maybe not, but yeah, I'll dig deeper.
And see if this is anywhere different from, simple database memory operations.
**Ridhima Satam** 18:14 Also, one quick question, like, you've been… I haven't looked into memory as such, but, like, there is this retrieval we have, right? Would that… is similar to this, or how would it, like, do they ma… overlap, or…
**nagkumar** 18:30 retrieval… in, gen AI span?
**Ridhima Satam** 18:35 We have added a retrieval operation recently.
In the spans, yeah.
**nagkumar** 18:42 Yeah.
Retrieval probably looks just at the data source and what the data source are, like, and retrieval says documents.
Memory can probably return less than just documents.
And deletion, I don't know if retrieval can… is specific to… Like, how would we… I don't think there is a way to showcase deletion. Retrieval seems more like a query.
**Ridhima Satam** 19:19 R.
**nagkumar** 19:19 Operation.
**Ridhima Satam** 19:22 It's still, like, kind of using a memory or something, right? Or…
**nagkumar** 19:26 Yeah, so…
**Ridhima Satam** 19:29 this retrieval in some way, would it be possible? I'm just asking, like, I don't have any.
**nagkumar** 19:34 Yeah.
I mean, it makes sense. If there is a way to, like, search memory can be as close as possible to retrieval span, or, like, retrieval, operation here.
But other things, like create memory, and delete memory, or update memory.
It would be hard to denote with just retrieval.
**shuwpan** 19:59 Yeah, and I'm thinking, is it retrieval always in, like, it has to do an embedding first, but memory, I think it doesn't have to be, like, do an embedding and then retrieve.
I'm just thinking out loud.
**nagkumar** 20:13 Yeah, I mean, that's… that's a good point, too. Like, retrieve… memory can retrieve from anything, whereas retrieval, like, at least with these samples, seems like it's more specific to rag-style retrieval.
You know, especially when I see documents are being retrieved.
pretty… memory can come from anything. It could be a database file.
A third-party provider.
So, yeah, I'll leave this, here for discussion. I would love some more comments on it.
Thank you so much. That was memory stick.
**Sergey Sergeev** 21:23 Yeah, to me, the biggest justification of GenAI-specific expense for the separation that, for any… AI agent monitoring experience, it's hard if we leverage, for example, DB search or whatever, it's really hard to identify, it's a lot of heuristic, like, okay, what… what is my agent invocation? Okay, we quote database. Is it… AI-specific, is it coming from… databaseware, so… database client instrumentation. I think just having everything on GenAI Span is the justification why you need it.
And similar to retrieval, it's more to identify what is unique to memory. So, memory is probably… Is it a document specifically from… When you get a document from memory, or when you… Retrieve a conversation from memory.
**nagkumar** 22:30 Yeah, ideally it is… like, it could be anything, when it comes to… Like, how… like, what agent and what kind of memory are we thinking about, like… Agentic memory could be… in multiple ways, like, when I was reading about multiple memory providers, there are memories which are related to, like, procedures, so, like, how to complete a specific agentic operation could be something in memory, which is retrieved when what operation is kind of Like, when an agent identifies what operation to do, it can go look up memory to see how to do that operation and perform that operation.
Memory could be, like, user-specific, like, something that an agentic user is trying to save and then retrieve later on, or modify. Memory can also be… like… application-specific. Like, for example, there is some sort of an agent which is doing some… A small part of a bigger application, and… what the application does is stored in, like, a different, like, area. So, let's say, getting some product information from a database.
That could be denoted as a memory operation, but that… the last part, which I just said, that could also be just a retrieval operation, in the current sense. So, there are more use cases than just the retrieval, and I'll make sure these are highlighted in the PR, like, I'll add more comments on each of these, which are Issues we discussed about, and how memory would help us get there.
**Sergey Sergeev** 24:12 So, again, totally makes sense, and yeah, I see an example that, for example, there is a scope.
**nagkumar** 24:22 Yep.
**Sergey Sergeev** 24:22 This is… Yeah, this is really cool. I think we should also… But the type of, we basically tried to build, also some JAMA application on our side, which more… Which represents more some real… use case, and, we built, an SRE incident copilot agent.
Which, uses, Basically, some background books.
Retrieved from… The rug. So, basically, when it tries to solve the problem, it fetches, runbooks from… Vector Database.
I… I don't know if we used, one-chain memory-specific Component, but it would be great, to leverage Specifically memory, and see how… This proposal applies to it.
Is it also… does it also include the demo application?
**nagkumar** 25:36 Yeah, all these story, they're all demo applications.
Like, when… when we look at all those, it's… I'm just pulling everything from locally, and then it adds the spans manually, here.
I think the LLM calls are real.
**Sergey Sergeev** 25:56 I'm wondering about some frameworks.
**nagkumar** 26:01 Okay, yeah, I thought that it might have cleaned it up, because there are so many prototype stuff, but, I can add more, like, framework-specific examples. Each of those stories in, like, ADK, Langshan, LineGraph.
And how that would look like.
**Sergey Sergeev** 26:20 Yep.
**nagkumar** 26:21 Okay, yeah, I mean, these story files and scenario files, I'm keeping them as temporary until I can explain this to people, and then deleting it off, so, don't worry too much about the PR being big.
**Sergey Sergeev** 26:32 No, no.
**nagkumar** 26:33 tough.
**Sergey Sergeev** 26:33 Yeah, I'm more trying to answer that question for myself, so…
**nagkumar** 26:38 Yeah.
**Sergey Sergeev** 26:39 Of what, does it mean, and what will be useful for… Our synthetic, use case may be for internal teams.
We probably need to chat about Retriever, this memory difference.
Yam.
If you… Get an example of, length chain, it will be really helpful for us.
**nagkumar** 27:11 Okay, I will make sure there is a Langchain. One of these, or, like, all of these will be in Langchain or something.
**Sergey Sergeev** 27:19 Yeah, at least one of them.
**nagkumar** 27:23 Another one that I would probably bring up tomorrow was the security, spec. Security seems more like an AI thing, more than an agent thing, so, like, a more generic thing, so I'll probably bring it up there.
Aditya is here on the call. Yeah. Aditya.
**Sergey Sergeev** 27:43 So, can you quickly summarize, if it worked, for… Cisco AI defense team use case.
**aditya (cisco/splunk)** 27:52 Yeah, so Cisco AI Defense team has that. They need a very specific… they are using a very specific name, right? GenAI Security Event ID.
So I think that was missing, right, Nag, from the…
**nagkumar** 28:05 Yep.
**aditya (cisco/splunk)** 28:06 original PR that you had?
**nagkumar** 28:08 Yeah.
**aditya (cisco/splunk)** 28:09 Yep, I have… I think I added a GenAI security external event ID.
**nagkumar** 28:14 To try to make it more, like.
compatible with external systems, and I've added a comment on that as well, so…
**aditya (cisco/splunk)** 28:22 Okay, okay, you have? Okay, I might have missed.
**nagkumar** 28:24 year.
I just did it today, so… Okay, okay. It's too early. Yeah, I was gonna bring that up.
No worries, no worries. It's just been an hour since I added it, so it's on me.
**aditya (cisco/splunk)** 28:37 I'll also ping the domain team, because they might have a better understanding, right? Because from what I understand, it's something, you know.
They propagate it in the traces, and then it goes to the, to the backend systems, and they might have some workflows or whatnot based on that flow out on that field, so I'll ping them.
**nagkumar** 28:57 Okay.
**aditya (cisco/splunk)** 28:58 That works in their use case, but if not, but I think, yeah.
**nagkumar** 29:02 We can always add it if it's needed, if it's, like, that ex… you know, needed by, like, and already being used by a lot of people, so we can… we can add it to this as well, so…
**aditya (cisco/splunk)** 29:13 Yeah, yeah.
**nagkumar** 29:13 Thank you.
**aditya (cisco/splunk)** 29:15 I'll do that.
Thanks, Nag.
**Sergey Sergeev** 29:19 Okay, cool.
I think we are at time, yeah. So, see you… Tomorrow.
In the generic, in GenAI SQL. And, yeah, Nakumara, if you get any updates, for us to review, please post it, Either in SWAC or in Gamilla.
**nagkumar** 29:51 Yep.
Will do. Thank you so much.
**Sergey Sergeev** 29:54 Same chair.
**nagkumar** 29:55 What?
**aditya (cisco/splunk)** 29:57 Thank you, guys.

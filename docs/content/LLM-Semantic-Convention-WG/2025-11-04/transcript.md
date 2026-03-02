SIG: LLM Semantic Convention WG
Date: 2025-11-04
Duration: 58 minutes
Zoom Recording URL: https://zoom.us/rec/share/WlsYVNN2jqBSlIMFjz2DQ6BWB79xEZyo5S7U5jCJgOQkzxqFNA2HHiOICUczNcyi.-Gl_2SysF9qTa2_R
============================================================

## Zoom Recording Transcript

**Mayank Ramkishore Gupta** 01:15 Hello.
**Liudmila Molkova** 02:54 Okay, hi everyone. Sorry for being late,
Give me a few minutes to prepare.
Unless somebody else wants to drive the call?
Not volunteers.
Okay.
So, let's see…
Okay, so if you have any topics, please add them to the agenda. We will start with a little triage, we'll see if we have any new issues.
I think we took a look at a few of them in the past.
This is a follow-up.
For Aaron's PR to… Optimize the parts
Aaron is not here, but I think he… he told that he will be…
looking at it, so I'll take a liberty to assign him.
Here.
So what else do we have?
**Alex Hall** 04:48 Do we have an issue to move away from the notebook into the Python script?
**Liudmila Molkova** 04:53 No, could you please create one?
Feel free to assign to me if you want.
Great, so, two orchestrations been our hotel brought it up last week.
And I think… We discussed that,
It's essentially another Invoke Edgence pen.
With some… LLM and execute tools under.
And now, he's suggesting to add an attribute.
And… the two USB either… It's not universal.
I think it makes sense to add new attributes if they are available.
The usual question is whether they are generic?
and…
Okay, so I…
**Alex Hall** 07:06 Something related to this.
**Liudmila Molkova** 07:07 So…
**Alex Hall** 07:08 We have a span for invoking an agent.
calling an LLM and executing a tool, and these are very closely related.
And this is… this is part of that same structure, and it's even, like, described in that last comment.
Should there be some conventions about the relationship between these spans? Should there be a requirement that
the LLM span and the executeTool span are, like, direct children of the agent span, or something.
**Liudmila Molkova** 07:41 Why? Like, is it beneficial?
**Alex Hall** 07:46 So, in Byadantic AI, we currently…
wrap the tool execution spans in an outer span that says running X tools. So if you're running three tools in parallel after an LLM call.
There's a… well, if you're running any number of tools, but in particular, if you're running more than one.
Then they still get wrapped into one span, partly so that, you know, that you always have this very clear
Visible loop of… Other than tools. Other than tools.
But this makes the trace more messy, and it felt like it would be nice if there was a convention here to force us to make a decision.
**Liudmila Molkova** 08:31 In my view.
**Alex Hall** 08:34 users…
**Liudmila Molkova** 08:36 Should always be able to pick what they want.
So… they can turn off LLM calls, or they can turn off execute.
spans, suppress them, like, the whole layer. Let's say they don't want the framework layer, they only want lower level layer, or the vice versa.
**Alex Hall** 08:59 As an example of where such a convention exists, I think that for HTTP, client… Spans, like, the request.
There's requirements that it's… it's like the…
An individual requested, like, the transport layer, so that if multiple requests are made because of, like, retries or redirects or something.
It actually says there should not be a parent span encompassing one of those.
Oh.
**Liudmila Molkova** 09:31 It says…
**Alex Hall** 09:31 Conventions of this type exist, and I'm wondering if there should be smaller ones here.
**Liudmila Molkova** 09:36 So, it talks about the specific layer, right? It does not talk… it talks that when you're instrumenting a HTTP layer.
Then, EU instrument per try.
**Alex Hall** 09:51 Something like that, I'm trying to find the exact thing.
**Liudmila Molkova** 09:54 It's here, it's on the screen, right?
**Alex Hall** 09:58 Okay.
**Liudmila Molkova** 10:00 So… It says that you're… Greatest bond per attempt.
and essentially not create an encompassing span. But you're saying that LLM conventions should say that you don't create,
an encompassing span for…
**Alex Hall** 10:22 I'm not saying that they necessarily should, but I'm just wondering if it…
If there should be conventions of this nature.
You know, about not just individual spans, but about the relationship between them.
**Liudmila Molkova** 10:38 I think this would be very fragile and very hard to enforce in practice, and I don't think it makes…
And so, if you have any…
Any user code or any configuration mechanism, anybody can create a span in the middle, or they could suppress
One of the layers. And it's… it should be valid.
We can outline the golden path, so those are the layers you instrument. But how users combine them, this is not a convention, this is a…
**Alex Hall** 11:16 And also… As another example.
Currently, we store all of the messages
not just in the LLM spans, but also in the invoke agent span.
and…
This is not great in some ways, and there's also some ways in which it just doesn't work at all, because, for example.
The system instructions can vary
over the course of an agent run, like, between different LLM calls, and so you can't actually
always have just one set of system instructions in the Asian span.
And, like, stalling all of them would not be a good idea, and we had a similar discussion about this problem with, like, tool definitions. So it would be great for the UI,
To… when you're… when you're… someone is viewing the agent run span, for it to fetch
these… this information about, like, inner messages and tool definitions from the… the children L&M spans.
This is something we haven't implemented yet, but it's something we've planned on doing for a while.
And if there were conventions about this kind of thing that applied to all agent frameworks, then we would know that this would also work not just for our own Pydantic AI, but…
whatever else following those conventions. But if those LLM spans happen to be in some deeper layer, then it becomes a lot messier for us to get them.
**Liudmila Molkova** 12:47 Yeah, and then you could say that LLM Spence, in general.
If you have them, provide more details about specific calls.
Regardless of the… hierarchy, right? They could be grandchildren, you don't care.
**Alex Hall** 13:06 We do get, because actually, if they're deeper descendants, they might not belong to this agent one. They might be part of a tour core within the agent one, but they wouldn't make sense as, like.
They're conceptually different from, sort of, like, the direct children.
**Liudmila Molkova** 13:24 I see. Still, I don't think it's possible to enforce through convention. It's… it's too dynamic, and even, like, you…
you could assume they are children, and it would satisfy 90% of cases anyway. And do you actually care about the rest 10%? Or maybe you could… your UI could be much smarter and say, okay, if they are separated by, I don't know, internal spend, then you don't care.
Okay, I…
I think we should move it to to-do.
Let's move on to the agenda. I still haven't done it, I'm just… I'm just keeping this here so I don't forget, I'm sorry. If anybody wants to go ahead and introduce themselves and say what brings you here, please go ahead.
If not, that's also okay.
Okay, so it sounds like nobody wants to. Feel free to add your name to the agenda and,
Like, anytime you want, later on.
Just a reminder, KubeCon is, next week. I will be off next week.
And if you're there, come say hi. We'll have GenAI Office
hours on Wednesday at 3 p.m.
Yeah, and there was some… I don't know if there are any talks on GenAI observability, I'm not sure.
crying.
So, moving on to the…
agenda, I would like to bring up MCP conventions and continue the discussions we had offline.
Yep.
Sorry, something is wrong with my internet.
Or maybe the PR is too big.
Okay…
So, we've got some great reviews, thanks, Samuel, you're not here, but thanks for bringing MCP folks. We had some feedback.
From them, and thanks a lot, Alex, for the discussions. So, to summarize,
MCP folks' feedback, I think there are 3 parts.
There is a couple of points here. I've added MCP protocol version.
it does not capture MCP capabilities. I… I feel this is easy to add incrementally. I understand they are important, but just to keep things…
saying we can, break it down into multiple PRs.
And the third, the most important one, is transport.
I think I've made some changes based on this. It's still not perfect, but I think it's much better now.
Well, we'll talk about transport, I think, in a sec. I wanted to… Continue… the… Context, conversation details.
So, apparently, MCP wants to have a prefix.
So, the key format have two segments, an optional prefix and a name.
And… We could reserve a prefix here.
For… for the context. But it's not ours, it's not open telemetry.
standards.
And, reserving anything with up and telemetry does not feel right to me.
**Alex Hall** 18:01 To me, the reasoning for this OpenTelemetry context, if it's an object, is to say whatever goes in here is just whatever
You know, all of the context.
produced by the TexMap propagator is, and you don't know what it is, but it could be a combination of conventions.
**Liudmila Molkova** 18:20 Yeah, the point is that if something not up in telemetry injects context on one side.
And up in telemetry extracts context on the different site.
it should still work. It works for…
HTTP. It would work for gRPC and anything else. Why shouldn't it work for MCP?
**Alex Hall** 18:41 Is that the idea, is that we expect that…
I don't know, some people will build some kind of W3C component that's more general, no hotel for MCP.
**Liudmila Molkova** 18:53 I don't know, they've done it for HTTP. If MCP becomes popular, like, among
users and in distributed systems, I'm pretty sure.
**Alex Hall** 19:04 I mean, I don't understand how it even works in the case of trace parent. You know, it looks… to me, it looks hotel-specific. Are trace IDs and spam IDs with those kinds of formats
Such a general thing.
**Liudmila Molkova** 19:18 It is W3C standard.
**Alex Hall** 19:22 I don't know what other systems have this…
And NGINX supports it, I think, without open telemetry.
**Liudmila Molkova** 19:30 And there are plenty of proxies and, I don't know, maybe Envoy.
that work with WC3C trace context without ever caring about open telemetry.
So, I do feel it's not right to use up an telemetry prefix. It's not used anywhere else, and there was a lot of effort to actually disassociate
Open telemetry… And the context propagation mechanism.
So my preference would actually be to just not introduce a prefix. I don't see why it should be there. It's optional according to the
The…
**Alex Hall** 20:42 specification, and we don't have prefix for things that are way more popular, like HTTP headers.
I'm not against this, but… Do we have to convince MCP?
I mean, it is our conventions, but then…
They might be unhappy about librarians just… Regularly in searching this.
**Liudmila Molkova** 21:06 then they should demand prefix, I guess?
**Alex Hall** 21:24 If… if trace parent is more general than open telemetry, then isn't it possible to have trace parent coming from two places?
**Liudmila Molkova** 21:35 Does somebody who injects trace parenthood should have… should take care of it.
So the last, like, the… like, for example, if you have multiple instrumentations for the same HTTP request, it's normal for them to, pull in the previous one and the headers and set the new one.
And I think it's even the default behavior of trace context propagator and OpenTeometry.
**Alex Hall** 22:10 Okay, so do we just… Ignore their comment, or not ignore, but reject it, and…
Just keep going with transparency in there.
I mean, I'm happy with that because it means that I don't have to change my instrumentation.
**Liudmila Molkova** 22:24 I mean, I would try if there is, if it causes any,
further friction with MCP, I'm happy to continue the discussion, but it sounds like the… Good.
The most straightforward and simple choice we could make.
Okay, so, if you… Are you fine with this approach.
Then I'll leave a comment here.
And we'll… we'll see if there is any pushback from MCP.
**Alex Hall** 23:10 Okay.
**Liudmila Molkova** 24:13 Okay, so, moving on to the next point, Think…
The transport is the most interesting one.
So I hope there are people who are more familiar with MCP than me in this call, but…
So…
my understanding that there are three major modes in which MCP is used. The first one is STDIO. This is the,
I think I have a problem in my comment here.
This is quite…
So the first one is STDIO, and it has a network transport. It's… think about it as,
L4 and OCI model, if you are familiar with it.
And then, there is no other network protocol attributes, because it's not effectively a network.
And there is an MCP protocol version, which is whatever.
And there is an old mode, the streamable, sorry, the new mode, the streamable HTTP.
**Alex Hall** 25:37 Wait, sorry, let me let you… you're saying you've already pushed these changes into this PR.
Is there any controversy around them?
Is there any reason not to just go with what you've written?
**Liudmila Molkova** 25:50 My question is, do we, how do we… are there enough?
I think they're not exhaustive, but there are… I think, are good…
to start with, and I'm not convinced we need… More.
**Alex Hall** 26:08 What does it even leave out?
What does it leave out? What's not covered here?
**Liudmila Molkova** 26:18 So, I'm not sure if you can use HTTP plus SSC on newer version of Protocol. If you can, then there is some ambiguity around, okay, did you use the newer streamable HTTP or HTTP plus SSE?
Is it important? It probably won't be important in a year from now, but it's still important now, according to…
their feedback. If you could have…
this is the first point. The second point, you can provide completely custom transport for MCP, and you might or might not be able to document what you provided. So, like, with gRPC, it's not really clear how would you document it, but again, it's not even part of the specification. There is a proposal.
on how to make it happen. So, maybe in the future, we need a better way to say, okay, this is the transport, the MCP transport used.
**Alex Hall** 27:19 Is network.protocol.name a standard attribute?
Used elsewhere that's already expected to have, you know, like, like… If you put…
network protocol name equals HTTPSE, or streamboard HTTP, or something, would that violate some existing standard of, oh, no, it's supposed to follow these known values, and HTTP is one of them?
**Liudmila Molkova** 27:48 Well, you can. Nobody's going to hunt you down, but it's… it's essentially an application layer. So, if you… it's HTTP, it's not streamable HTTP or HTTP plus SSE, the proper…
conventional uses to put just HTTP there. You can violate the convention.
**Alex Hall** 28:12 It sounds like the existing attributes are useful, and they pretty much have to be used in the way that you've specified.
And so what you're asking for would need to be a new attribute, like MCP protocol name.
**Liudmila Molkova** 28:27 yeah, whether we need something else. I don't think it should be MCP, because…
The problem is generic. You can run a lot of things on top of custom protocol, so it shouldn't be MCP, and then what it is, is a much more complicated discussion.
So, if there are no concerns with this audience, let's start with this. We cannot attribute if it's proven to be necessary.
**Alex Hall** 29:00 Okay, but so, fine, this is insufficient, but again, is there any downside to having these attributes as described? Is it even…
Something we can change, like… All of the network attributes are standard, and…
have, like, expected values, and doesn't… is there room?
For variation here.
**Liudmila Molkova** 29:24 The room vibrations, maybe they are too… too much? Maybe if we could replace them with a single attribute of some sort, that… that would be descriptive enough.
They are, I think, as recommended, or…
Which means that we can turn them off, we can probably replace them with something else.
So what, what you're… how I interpret your question is, you… it sounds like you would…
You find them reasonable, and we don't necessarily…
We can proceed with this as a first step.
**Alex Hall** 30:08 I don't see any problem with having these attributes.
I, I think that…
we still will want, you know, something like MCP Transport Name, maybe it'll be named differently, but I think that that's what the MCP people are asking for, and it makes sense.
But it doesn't look like we would put that information in any of these attributes anyway. It looks like if we had such an attribute, it would still make sense to combine it with these.
So I don't see any reason not to go forward with what we… what's here already.
**Liudmila Molkova** 30:42 Okay.
So then, let's go forward with it, and
see if I get any feedback, or we see that we need to… Implement more things.
Okay, moving on to the next one.
So, we talked about the input and output Thanks, and… Maybe I cannot, YAML file.
Okay, so what do we have now? We have,
Anyway…
I'm sorry.
I'm sorry again.
Okay, so we have, the input parameter key, it maps to the input param.
It's a complex value. And we have MCP result. I removed the response because it seems…
redundant.
Any concerns, Alex?
**Alex Hall** 32:42 The idea makes sense. I don't know, what if it was MCP.input.key and mcp.output.key?
**Liudmila Molkova** 32:55 Input that key, but then it's a param.
There are also… R, wait.
Meta is also part of France, right?
**Alex Hall** 33:12 This is nitpicking, I mean, I don't… I don't care that much.
Are there no pre-existing…
conventions for this kind of thing, like, I don't know, function calls and a JSON RPC, and there's nothing, which is disappointing. But I guess…
I guess part of the problem is that complex attributes are a new idea.
**Liudmila Molkova** 33:43 Oh, it's less about complex attributes, and there are… HTTP request… Had their key… RPC metadata key.
But, so, if it's just input, Key. Nice.
**Alex Hall** 34:02 Lots of… lots of things act like functions.
**Liudmila Molkova** 34:09 A lot of things said, like.
Act like functions, but yeah, capturing parameters of the function is a new thing.
I feel that input.key and output.key are a bit too…
White. And maybe it's tied to your other question about the meta.
Do we want to capture metaproperties? And do we want a separate key for this?
**Alex Hall** 34:50 I think if it was just included in the current programs, just like any other program, if there was no special treatment for it, that would just work.
**Liudmila Molkova** 35:01 So, like.
**Alex Hall** 35:03 But is it weird to do that, especially with the needing underscore?
**Liudmila Molkova** 35:09 It's… it's not the problem, it's a valid name, so if it's the input.
Underscore meta.
It looks weird, but it's fine.
I could… maybe remove this, but it… I… who cares?
Or is it…
**Alex Hall** 35:41 But his prior art form?
Inputs and outputs, which is the executeToolSpan.
Well, actually, no, that's not true, because it might just be, like, a string or something.
**Liudmila Molkova** 36:10 to call arguments.
Oh, interesting.
Huh.
Should we change it?
Should it be a template of any? Well, this one is probably a single thing, but this one should probably be a template.
Like, you would rather prefer to… Think about them as independent.
**Alex Hall** 36:43 Somewhat, although…
**Liudmila Molkova** 36:52 Okay, anyway, let's create an issue, and… Whoa, whoa.
Oh, gosh.
or three.
**Alex Hall** 37:20 And it's possible for it to not actually be an object.
Something to support, just like… I don't know, position or parameters or something.
**Liudmila Molkova** 37:31 At the positional, you just… you just added the positional thing.
**Alex Hall** 37:36 I guess.
**Liudmila Molkova** 37:56 Okay, coming back.
And I see there is another discussion… discussion from Josh. Let's reserve, I don't know, 15 minutes for it, Josh? Would it be okay?
**Josh Winerman** 38:10 Sounds good.
**Liudmila Molkova** 38:11 Yeah, thank you.
Okay, common book… to MCP…
So I would prefer to keep input param, the meta can be under it.
Mcp output result also sounds good to me.
With Meta included.
you can configure Meta as any other.
parameter.
**Alex Hall** 39:00 Okay.
**Liudmila Molkova** 39:03 King…
And…
So after PR gets a lot of comments, it becomes really hard to work with it in GitHub. They don't optimize for this case.
Okay, and then it will be addressed through this change.
Okay, we are at the bottom of the MCP discussions. Anything else anybody wants to discuss here?
Okay, wonderful, then let's move on to the retrieval Pure.
Oh, thank you.
We're up to DB and embedding child span.
**Josh Winerman** 40:53 Sorry about the resolution, I didn't realize it would be that bad.
**Liudmila Molkova** 41:06 So, the proposal here is that you would
the proposal here is to instrument the retriever in Llama Index, or Lankchain or something, right?
**Josh Winerman** 41:22 Yep.
**Liudmila Molkova** 41:24 And then, essentially, This would drop…
whatever happens under. It may be embedding, it may be just a search.
It may be database query, or embedding can database query.
**Josh Winerman** 41:41 Yeah, exactly.
**Liudmila Molkova** 41:52 than, this is all the default stuff.
Okay, this is a link chain.
So, it sounds like… What you're missing today is this thing.
the research type, what… what is the… Search type… oh, okay.
So this is not the Gen AI, right? This is,
is unrelated to Gen AI, it's just the search something.
**Josh Winerman** 42:51 Yeah, yeah, no worries, I can… I don't mind changing that to DB either, feel free to leave a comment. It's just, I think the… the end goal is…
a span that wraps both the DB and or embedding search, and to have associated DB and or GenAI attributes in the parent span, if possible.
**Liudmila Molkova** 43:18 Okay, so this one is…
We have an attribute for this, maybe it should maybe work here, maybe system name.
Maybe we need a new one, I don't know, but probably it's the same one.
This is probably, db.org.
Gotcha.
This is the instrumentation scope name. Oh, you're saying that the… you would like to have the instrumented library.
Okay, ugh, let me… Let me find the…
The discussion on this one,
Okay, I… it might be difficult, but essentially, this is the…
**Josh Winerman** 44:49 I can look into it, too. Leon Milla, feel free to leave it.
Either or.
**Liudmila Molkova** 45:05 This is fine, the retrieval query. We can't consider DB query text, or…
It might be weird to call it DB. It could be search… Rare.
Next, because this retrieval… like, the big part of my feedback that I have is that it's not a…
you shouldn't think about it as just the wrapper for embedding plus database. It could be Google search, literally, and the conventions you create should make sense for Google as well.
Do you see what I'm saying?
**Josh Winerman** 45:52 I think so.
**Liudmila Molkova** 45:55 It's like, if you add,
with any of this, just a Google search, or whatever search in your scenario mix.
It would… Help you, like, sort of guide you.
If you see it doesn't make sense for Google, then maybe the abstraction is not right. We should have it more abstract.
**Josh Winerman** 46:21 Okay.
**Liudmila Molkova** 46:27 Okay, cool, but then, great, it makes total sense, Do…
We can spend more time actually designing it if you want.
**Josh Winerman** 46:41 Up to you, I think,
It depends on what you feel you're happy with, too, at this point.
**Liudmila Molkova** 46:51 I mean, I… you overestimate, the importance of my happiness.
So, let's see.
So what helps me, I just go to the, documentation for… let's say we go to…
Lama Index rate reverse.
And we take a look at the API they have.
Right, so this is the abstraction, for…
That you're… would like to instrument, right?
**Josh Winerman** 47:35 Yeah.
**Liudmila Molkova** 47:37 Awesome.
So… What do they have?
in the API.
Okay, wonderful.
So, some Bayes Retriever. What is in the Bayes Retriever? We have… Wow.
Not much.
Oh, it knows about nodes, right? And it inspects nodes to find out what How to query it.
And you would… Instrumentation would have a similar code to… Deal with that, right?
So, for example, here it would know about the scores of the… documents.
And here it would know that the…
the response is not. Okay, let's take a look at the… is it, something the OpenLeetry is, right?
**Josh Winerman** 49:43 Yeah, open all the elementary.
**Liudmila Molkova** 49:50 Hmm…
Let's see… Bass Retriever Instrumenter.
All they do is just dump arcs.
Into attributes, interesting.
Okay, but blank chain is better, is it?
**Josh Winerman** 50:46 Langchain was something that, we proposed based on TraceLoop's instrumentation, so it's not…
going to be there, per se.
**Liudmila Molkova** 50:57 Oh, okay.
So it also doesn't do much there for the retrievers.
**Josh Winerman** 51:05 Yeah, probably not.
Still doing much.
**Liudmila Molkova** 51:10 Okay, so let's see what happened inference does.
So, what I'm trying to get to is… What is available? So the…
In semantic conventions, you, you need to balance between what's available and what, what you want.
Sometimes you need to think about what you… what's available first before you decide what you want.
Let's see… Llama Index…
Xander, do you remember where the…
retriever instrumentation is for Lambda index.
**Xander Song** 52:00 I can look up the SEMConf.
**Liudmila Molkova** 52:05 Oh, I'm more curious about the… the implementation.
**Xander Song** 52:11 For Llama Index in particular, I don't think I remember that. I have not looked at that one in a minute.
**Liudmila Molkova** 52:16 Oh, no worries.
**Xander Song** 52:17 But it's probably… I mean, I can search for it real quick. Give me just one minute.
You want to see, like, the concrete implementation of one of these?
**Liudmila Molkova** 52:36 Yeah.
Or maybe full-length chain, whatever.
Yeah, it's right through the attribute.
Oh, this is Markdown.
Oh, I ended up in, in, in TypeScript. I'm sorry.
Okay, anyway, I'm sorry for this, not very productive and somewhat boring.
**Xander Song** 54:16 I think I have it right here, Lyudmila, if you want.
**Liudmila Molkova** 54:18 Oh, shit.
Oh yeah, wonderful.
**Xander Song** 54:20 I found something. I mean… Maybe it's helpful.
Let me see…
Can you see this?
**Liudmila Molkova** 54:39 Yep.
**Xander Song** 54:42 So, in terms of some of the conventions that I think we have associated, we store the entire document, so documents…
have IDs, they have… the content itself, they have a score, potentially. They can have metadata.
This is the node with score object that I think we were looking at.
Let me see, what else? I'm trying to remember what other SEMCOMF we actually have. We have the documents… I mean, I think those are the main ones for…
Retriever spans… I want to say that's the main thing, if I recall correctly.
And it's under, like, a retrieval documents key, and then it just… you see, yeah. So I'm pretty sure that's, like, the main… the main thing.
that we have there, the main SemConv we have around retrievers, and then it's just like a…
Parsing of the document content.
And saving it.
**Liudmila Molkova** 55:40 And you, you…
**Xander Song** 55:41 They have scores in particular. Like, that's maybe the one thing, too, is, like, you know… and this is, like, the similarity score.
**Liudmila Molkova** 55:51 Right, so this… and the attribute name is essentially indexed, right? So you would have 0, 1, and whatnot in the attribute name.
**Xander Song** 55:59 Yeah, that's right. I think you can kind of get a sense of that here.
this is maybe not the full attribute name, but it's gonna have an index in it. So it's supposed to be, like, a list of documents that we accomplish with having an index here, and then this is an attribute that has the form.
I can't click through right here, I don't have IntelliSense going, but it's an attribute of the form,
It's gonna be, like, I wanna say, document… Dot document content or something?
So it… but it's… it's a key, yeah, so it's, like, indexed under a… Index under,
a number, so I think the full… yeah, don't quote me on this, but I want to say the full…
He is gonna look something like, retrieval… Documents or something like this.
dot documents, dot0, dot…
document.content, or… it's something along these lines. And then it will have, like, you know, analogous stuff for, like, ID and score, etc.
Yeah.
**Liudmila Molkova** 57:07 Nice. And in the case of semantic conventions, we would bundle them into one
Big attribute to a complex type.
That would include a list of the documents, and each of the documents could have a score and content and ID.
And that, that's to start with.
**Xander Song** 57:31 Yeah, if we're talking about, like, the more complex, like, list of objects, attributes, types, like, we obviously did this before that was supported or proposed in OTEM.
**Liudmila Molkova** 57:40 Yeah, yeah, of course.
**Xander Song** 57:42 Yeah, pretty, pretty similar.
Yeah.
**Liudmila Molkova** 57:45 Yeah.
**Xander Song** 57:46 Cool.
**Liudmila Molkova** 57:48 Cool.
Thanks. So, Josh, if you would like to, I don't know, maybe make a proposal with the attribute names that are not Gen AI-specific?
I think it makes total sense to me.
**Josh Winerman** 58:05 Okay, yeah, let me go ahead and look into that.
**Liudmila Molkova** 58:09 Yeah.
Thank you.
Okay, we are pretty much at time. Thanks a lot. It was a very deep, but very productive discussion today. Thank you all.
**Xander Song** 58:21 Thanks, everybody.
**Liudmila Molkova** 58:22 See you in 2 weeks!
**Josh Winerman** 58:26 Thank you.
**Liudmila Molkova** 58:26 Totally.

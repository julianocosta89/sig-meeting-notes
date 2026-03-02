SIG: LLM Semantic Convention WG
Date: 2025-12-02
Duration: 89 minutes
Zoom Recording URL: https://zoom.us/rec/share/TnEd37iyGhEZaI2SsC2KrD8h0OurFwaADFCFEWYbtycID064N51_vri1vo9SXpED.DzuDRzM3mlFIrbZF
============================================================

## Zoom Recording Transcript

Liudmila Molkova 00:01:04 Hi, everyone.
Josh Winerman 00:01:13 Morning, everyone.
Or…
shuwpan 00:01:15 Morning.
Josh Winerman 00:01:16 Anywhere.
Liudmila Molkova 00:01:32 Okay, so while people are coming, let's… let me share my screen.
And let's prepare for the call.
So, if you have anything you want to add to the agenda, please go ahead.
I'll take a look at the project board.
I've triaged a couple of issues,
Okay, so I think we have a PR for this one.
Well, maybe not.
Aaron Abbott 00:02:28 Hello.
Liudmila Molkova 00:02:30 Hello!
Right.
It's mentioned here. Wonderful.
Mission Interesting here.
There are a bunch of things in progress.
Should we close this one?
I think it's been done, right?
Aaron Abbott 00:03:14 Yeah… I don't know if we've… Integrated all the other spots.
That use the, utils to use it, though, like, partially because…
Yeah, I mean, I guess we can… we can remove this and just inter… and just address them ad hoc. I don't know how much value this is adding.
Liudmila Molkova 00:03:41 Yeah, I think the… the one that's definitely not using them is OpenAI instrumentation and…
We probably can just create the shoes for individual ones as we… Switch.
Do you okay me closing it?
Aaron Abbott 00:04:27 Yep, sounds good.
Thank you.
Liudmila Molkova 00:04:32 Let's take a look at a couple more,
It's in progress. We have it on the agenda.
This one, I think, is still hanging.
Attributes for generic external storage references. I think we parked it, right?
Aaron Abbott 00:04:55 Yeah, I had, like, a draft PR.
And we kind of parked it for now.
Liudmila Molkova 00:05:01 Okay, so… Let's move it to to-do.
Aaron Abbott 00:05:14 Do you have to update the labels, too, or just changing it in the board?
Do everything.
Liudmila Molkova 00:05:20 Oh, I have double labels too, thank you.
Okay. I hope it was… it would be easier.
Okay.
I don't think it's in progress.
I don't think there is any… PR?
Oh, it got closed.
What?
Okay, so I'll just move it to to-do then.
And just the last one…
the session idea. I think we had a bunch of discussions with Avan, and… Where…
Eventually concluded that we don't know if it's necessary at all.
At least we don't… we cannot…
Come up with some good set of scenarios where
or definition of the session ID.
We have moods… Full.
So I'm going to move it to… Nothing?
Zinfo.
Aaron Abbott 00:07:56 In the meantime, on this one, Lydmilla, should people… like, if somebody has a specific need.
Should we just do, like, a framework-specific convention, or…
A vendor-specific convention kind of thing.
Liudmila Molkova 00:08:10 Is there a need?
Aaron Abbott 00:08:13 So, like, I've been talking with ADK, Google ADK folks a bit, and
They have this thing called Event ID,
Which is kind of… I think it's, like, the workflow stuff that we discussed also.
It's not… it's not session, to be clear, but like you said, any, any other non-conversation ID.
Liudmila Molkova 00:08:41 Great point. I would… I would love for people to come and just explain what they do, and I don't know, leave a comment on this issue.
And then we can… kind of discuss.
further. But for, like, if people own their semantic conventions, they don't need to ask for permission. They just come and tell what they've done.
Aaron Abbott 00:09:05 Yeah.
Liudmila Molkova 00:09:42 Okay.
So, let's move on to the main agenda.
And before that… Is that your name here?
If you want, if you're new to this group, if you want to introduce yourself, go ahead.
If you're… Not new, and you want to introduce yourself, please also go ahead.
Okay, if you decide to do this later on, go for it.
The first item to the agenda is MCP, and sorry, I… I wasn't able to talk about last time.
So, I see you've discussed something, and… The… about the context propagation?
I replied to a comment.
But instead of going through the text, let me maybe… Show you a demo?
So, Aaron, you asked about prototypes. It's actually part of…
NET, MCP Server and Client Implementation.
Aaron Abbott 00:11:00 Okay.
Liudmila Molkova 00:11:02 So…
Here, what I have is a bunch of examples. Let's start with the cool one. This is sampling.
So this is a client with tool calling, and it could be improved, but this is client with tool calling.
It calls server.
Chair.
Aaron Abbott 00:11:30 It's called server.
Liudmila Molkova 00:11:32 sample LLM function. The sampling can… MCP is a…
Ignore the name, it has nothing to do with tracing sampling.
What it does, it calls client back.
And asks client to call LLM.
If you're curious what was my… what my prompt was.
It was this cold sample, too.
I couldn't figure out how to do it otherwise. Anyway… So, the client,
calls server. This is the HTTP calls code. See? This is the HTTPOST call.
And server processes this call.
And in scope of the… Client, sorry, in scope of processing this request.
it sends a request back to client, you see? Server is calling client.
And client calls ChatGPT, oh, sorry, the OpenAI, but anyway…
And then it returns a response back to the server.
Server… Finally returns everything back to the client, and the client summarizes it,
So, what's important to know here, that this is the… This is the…
Client call. There is HTTP request associated with it.
The HTTP request is super short, because HTTP requests measure time to response headers.
They don't include the streaming response. This is the streaming response, actually, the one that happens on the server. And in scope of this.
stream.
We make another… call…
that does not show up on HTTP at all, because it's not the HTTP call, it's the request within
HTTP stream.
So, all I'm saying here, that the fact that MCP uses HTTP
has nothing to do with context propagation. Context propagation for AMCP can happen over the stream, because requests can happen over the stream, or it can happen over individual HTTP requests.
So there is no… use in trying to… for HTTP calls to have the same context as MCP calls.
And there are two independent things.
If there was a retry here, if the connection was not stable between my client and server, I would have one
MCP call and HTTP retry.
And I would have 1 MCP context and two HTTP contexts.
So it's many-to-many relationship between MCP context and HTTP context.
And there is no… Means to make them the same.
Aaron Abbott 00:14:45 But, if I'm reading this trace right, the…
like, the MCP tool call span is not a child of the…
post of the HTTP request at all, right?
Liudmila Molkova 00:14:59 So the way it's done there, yeah, it's kind of, an implementation detail. If…
the HTTP request is here, from client attended Super Short.
The way it's implemented, it ignores the parent, and it uses… sorry, it ignores the current parent.
Aaron Abbott 00:15:22 Yeah.
Liudmila Molkova 00:15:23 and it uses the, MCP… context.
Which is… One way to do this, which is fine.
It's not a child of the HTTP request, no.
Aaron Abbott 00:15:37 Yeah.
I mean, I think the real… so, like, the real reason it's happening is because you have to generate… you have to put the…
TraceParent into the meta field.
before you even started the poster request, right? So you couldn't…
You couldn't actually do it the other way around, where the…
the thing you propagate in meta.
Is the post, unless you, like, did it lazily somehow, right?
Liudmila Molkova 00:16:03 Right, and then in the MCP layer, I would need to know… I would need to have a special logic for a study in
And for HTTP, and I don't even know what to do for WebSockets if they have any
Probably now means to propagate context.
Aaron Abbott 00:16:22 Yeah, I mean, I don't think we can…
I don't know if we can do better, but I… I feel like this is a little bit unfortunate. Like, it looks like…
It looks like something's broken if you…
If you're expecting it to be underneath the post-call rate.
Liudmila Molkova 00:16:41 If you do, like… I think…
you probably don't even want HTTP instrumentation enabled for those.
So, like… you don't care about HTTP spends here.
Aaron Abbott 00:16:59 I'm in… I don't know, I feel like…
Like, on the one hand,
Like you said, it's time to first headers, and we can see that here, which is…
Useful, and kind of interesting.
And, like, you can tell it's a streamed transport, because…
As opposed to the, like, the… the non-SSE variant.
Because you do have this separate streaming part.
Liudmila Molkova 00:17:40 In… in the perfect world.
You would want… This guy to become the child of… Of the server span?
Like, cool.
Aaron Abbott 00:17:56 I don't think… like, I agree, like, I don't think we can… we should overcomplicate this in terms of the implementation, just to make the DAG look how people expect it.
But I think that was what the spirit of the comment on the MCPPR was about. They were like.
Does this break the encapsulation of the…
You know, like, wrap vertical kind of thing.
Liudmila Molkova 00:18:25 Okay,
And you would see… So what we do, there is a similar problem in messaging, where What with how?
that, duh.
Context in the message.
It's always so length.
And, the current context may be… a default parent.
But you can… make…
Instrumentations can provide the means for users to choose, but by default, you don't override the current
And this might help here, but then it would mean that Like, you don't know…
If the client to call.
Is always a parent of a…
Aaron Abbott 00:19:23 Yep.
Liudmila Molkova 00:19:24 server to call.
Which is the case, always the case, if you don't use HTTP.
Aaron Abbott 00:19:46 Yeah.
I feel like… I feel like it's kind of okay to just let the instrumentation behave naturally, like.
Like, in this case, like,
You can tell what's happening, even if it's a little surprising.
Liudmila Molkova 00:20:12 Yeah, that was my thought as well,
Do… is anybody else have any thoughts?
Alex Hall 00:20:23 This looks good to me.
Liudmila Molkova 00:20:32 Okay, so then the one change I made based on the comment,
I don't know who this is, but thank you for leaving the comment.
I… Added clarifications on… Having…
multiple layers of tool executions. So we currently, even in this picture, you kind of see it's unfortunate to help execute tool.
And we have, this is coming from the GenAI, client.
And then we have a tool called from MCP.
And they are… Completely the same.
the, actually, what I'm suggesting is, first, that, the MCP one.
Where is the MCP one?
Here we go.
So the MCP one would include all the attributes from… the GenA one.
So we'll have two call arguments, we'll have two call results, and… GenAI operation name.
R… The rest is the same.
And… This way, We can say either of the layers should be instrumented, but ideally not both.
So, when we…
Alex Hall 00:22:15 Whatever.
Liudmila Molkova 00:22:16 R.
Alex Hall 00:22:16 Maybe not both. I mean… how would that… how would that look in practice? Because I imagine that
You know, if you instrument the agent framework, you get
the executeTool spans, you instrument MCP, you get the MCP spans, and… You're gonna typically want both.
Liudmila Molkova 00:22:35 What?
Like, if they provide reasonable insights, each of them. Why would you want both?
Alex Hall 00:22:43 Because each has one that the other doesn't have, like, outside of the tool coils.
Liudmila Molkova 00:22:49 I don't… Think so.
Alex Hall 00:22:54 Well, the agent framework We'll instrument other types of tool call.
Not all tools will be MCP.
Liudmila Molkova 00:23:03 Right.
So, it's not that you have,
So imagine a perfect world, where these two breads.
Sorry, I've lost it.
Yeah.
This friend, and this friend.
Have pretty much the same information.
If they were one span.
This would be ideal.
So, Kia, they have a little bit tiny differences. This has Gen AI to call ID,
This has MCP request AD, where this has MCP session AD,
But… They are pretty much the same.
The timing is the same. If we captured the two calls.
Alex Hall 00:23:59 These spans are the same, but I'm saying that there's other spans that differ, like the… there's… okay, right now there's… yeah, the sampling create message on the client.
you wouldn't get that span without the MCP instrumentation, so you would naturally instrument the MCP clients if you wanted to see that.
Something create message span for some reason.
Liudmila Molkova 00:24:23 Absolutely. So what I'm saying is that the GenA client instrumentation can say, okay, this is MCP2, I actually have some means to know it's MCP2.
The OpenAI Responses API knows it's MCP, it's a special type.
When you give a tool, info, it might have some indication it's MCP, but if it knows.
The other option is that what happens for HTTP.
And there are some generic means to achieve it. The outer instrumentation says, okay, I'm instrumenting Execute 2. Everybody under me who instruments execute 2, back off.
The… there… you can put a suppression flag in the context, essentially.
And this could be another mean to suppress.
And in theory, this behavior could be configurable. Users
might be able to choose if they want to suppress it or not. By default, I think they should suppress. They should have one span. So you would always get the outer span.
Aaron Abbott 00:25:36 So should MCP emit a separate span, which can always go, that's not, like, having the same tool labels?
Attributes.
Liudmila Molkova 00:25:46 No, what I'm proposing is that, instrumentations can.
Aaron Abbott 00:25:52 Implemented in the way that.
Liudmila Molkova 00:25:57 So, MCP instrumentation may suppress their spans when they can detect that the GenA instrumentation is already tracing the tool execution.
Aaron Abbott 00:26:04 Alright, But, like, I guess as a kind of, like.
So say the orchestration layer doesn't know it's calling an MCP tool, it has, you know, like, a class, and the class, one of the subclasses is, like, MCP tool, right? Is there going to be any way to know from looking at the trace, that the call, went through MCP?
Liudmila Molkova 00:26:27 Yes, so the… maybe we should formalize it better.
But… I've added the type.
MCP?
Well, it's just an example here.
Aaron Abbott 00:26:43 Which one is this for?
Liudmila Molkova 00:26:45 This is for the tool type. We have a thing called GenAI tool type.
Aaron Abbott 00:26:50 Right.
But what, like.
Liudmila Molkova 00:26:57 Oh, I should add an explanation.
Alex Hall 00:27:01 But wait, it sounds like you're saying that when the GenAI instrumentation
Is executing any tool, it should just set that flag.
That's impression.
And then it doesn't have to know for sure, it's just that the MCP implementation will then look out for it.
Liudmila Molkova 00:27:18 Yeah, they can just say, okay, I'm executing the tool.
And MCP instrumentation would check if the flag is set.
And if it's set, it can back off.
Aaron Abbott 00:27:46 Yeah, I mean, I feel like it's gonna be a little bit hard to set the tool type in some scenarios. Like, if you…
like, say even that the user overrides, say, the user subclasses, like the MCP tool or something like that, right?
By that, I mean, like, say there's a class in the agent framework that's, like, you know, MCP tool wrapper or something like that. If the user writes their own or subclasses it, and the instrumentation lives in the orchestration framework.
How is it gonna know how to set genai.tool type?
If it doesn't know the specific class or whatever that implements MCP calls.
Liudmila Molkova 00:28:22 Nothing depends on it, right? So, like, the suppression flag doesn't need to care about the tool type.
It's just, if you have multiple layers of execute… of tool execution.
Yeah. In the same context, it probably doesn't make sense.
Aaron Abbott 00:28:37 No, I get that, I guess I just…
if I have, like, the, you know… just… I just want to know if the call went through MCP. Like, I could look and see… hopefully I'd see the server spin, right?
Liudmila Molkova 00:28:49 You would see the… Server spun, yes.
Aaron Abbott 00:28:56 Like, if the server's instrumented.
Liudmila Molkova 00:29:00 If the server is instrumented.
it's there.
Aaron Abbott 00:29:17 Maybe the, instead of setting a suppression flag, you could set this span
The executeToolSpin as, like, a specific
spot in the context, say it's, like.
you know, current execute tool spend, and then the MCP instrumentation could add
the tool type, or some MCP-specific labels so you would know.
Alex Hall 00:29:38 Or just all the MCP attributes that would be on the MCP span, you know, there's lots of MCP dot
attributes.
Liudmila Molkova 00:29:48 Yeah…
What?
Any other comment?
Aaron Abbott 00:30:00 Yeah, I know these are implementation details, I'm just trying to imagine, like, how a user would Approach this.
What, what they would.
Alex Hall 00:30:07 There's more than implementation detail, it's…
Actually recommending set attributes on a span outside of your own instrumentation.
Aaron Abbott 00:30:16 Yeah.
Alex Hall 00:30:21 I mean, the MCP… no, this isn't more of an implementation.
detail… well, not even really. The MCP implementation can simply get the current span.
Liudmila Molkova 00:30:33 Current is dangerous.
Alex Hall 00:30:35 Why is it dangerous?
Liudmila Molkova 00:30:37 You never know what the current spend is.
Alex Hall 00:30:41 But you can check, because it's not an executeTool.
Liudmila Molkova 00:30:44 So, it makes sense for the, Gen AI instrumentation to say, okay, this is the execute toe span, and then you can guarantee, you don't need to check, you just get the whole span, the reference to the span.
Alex Hall 00:31:05 Suppose the API doesn't give access to the name, does it?
Liudmila Molkova 00:31:09 I don't think so, no. It shouldn't be a… It's not a readable span.
Aaron Abbott 00:31:22 Yeah, I feel conflicted, because I think it was my suggestion that we could just use… reuse the execute tool.
Alex Hall 00:31:27 Instead of having, like, an MCP-specific one.
Liudmila Molkova 00:31:31 I mean, it makes sense, like, whoever would try it would ask why there is a…
There are two spans, and, like, there are some people are more tolerant to having duplicates, but if it…
If the instrumentation becomes popular, then people would come and ask all the time about it.
Alex Hall 00:31:52 So then, doesn't this mean that…
There should be some, like, conventional… key for the context.
Liudmila Molkova 00:32:03 It's, like, yes, but… If you want to…
Aaron Abbott 00:32:10 Work on.
Liudmila Molkova 00:32:11 to take… bit of time.
Alex Hall 00:32:16 I can't be just… Name… be in the spec, just say, you know what, but…
So in the context under this value.
I mean, I… I…
Liudmila Molkova 00:32:27 I… I tried.
so, if you take a look at my comment.
And it's not the hopeless thing to do, it should be done, but…
Alex Hall 00:32:41 But what, same applies for the suppression case.
Liudmila Molkova 00:32:45 Yeah, for the… It doesn't matter, so, like, if you… There is an opt-up.
Which I wrought.
Many years ago.
And it has 100… oh, just 50 comments, but it… It's… a lot of…
A lot of, explanation, and… I…
I think we should do it, but I don't feel like I would block any effort on the success of the story. So what happened, eventually, is that something like what you mentioned was implemented. If you look at the Java instrumentation, it uses exactly what you're saying.
It has, pan key… Thing per type?
Server, coin, consumer, producer, HTTP server, RPC server, and everything else.
And then, because there are multiple layers that instrument the same thing, each layer checks if their key is present, and don't instrument.
So this, this can be done, it does not violate the spec.
putting it into a SPAC would be a long effort that I'm not ready to take on right now.
Aaron Abbott 00:34:15 And I like it, I feel like it's really powerful, but I do feel a little concerned that
it's really difficult to tell where something is coming from. I mean, this is already something you can do, like, we have current as a special case, get current spend.
And it already… It's kind of difficult to reason about, but… .
Alex Hall 00:34:36 So how does this work in practice, Yudmer? Whether we went with the suppression case or the setting attributes case, like, would…
Would there just be sort of informal agreements to check what other implementations are doing, and everyone tries to copy each other?
Liudmila Molkova 00:34:53 So, if you are an RPC server instrumentation.
You… first, you check if the context key is present.
If it's not present, you… you create a… you start your own span.
Alex Hall 00:35:08 What I'm saying is, when you say the context key.
Liudmila Molkova 00:35:10 Since this isn't…
Alex Hall 00:35:12 defined in spec.
You just sort of have to be aware of what's going on.
in, like…
the various bits of code relevant to this. It's just, you know, in particular here, this looks like it's part of
something quite core in Java, but in our case, in Python.
it feels like it would have to be, you know… if there's an OpenTelemetry implementation, MCP and an OpenTelemetry implementation, OpenAI agents.
Then they would have to, like, check what each other is doing.
Liudmila Molkova 00:35:46 No, it would either be in the GenAIOTS, or there is a similar package in Python, the instrumentation API, where the instrumenters are defined.
It would live next to instrumenters.
And this is where… is it where the HTTP suppression key leaves? I don't remember.
Alex Hall 00:36:07 Might be HTTP UTL or something, I don't know either.
Liudmila Molkova 00:36:11 Yeah, I mean, we can put it into GenAIO tools, and it's already the central place for GenAI, where we can,
Think about more generic way, and do something.
non-GenAI specific in the Python instrumentation.
Poor.
Coming back to MCP, it sounds like
What, what, what should we put in this pack?
Like, what is the def… what is the default? And I think default…
The perfect situation is that the suppression exists.
The duplication… This is an option.
So I think that the… I would like to write some text that allows suppression.
But does not demand it, and does not… Require a specific implementation.
Alex Hall 00:37:18 Isn't the setting attributes better than the suppression?
Liudmila Molkova 00:37:23 It's suppression, but you also update the parent spend, right?
Alex Hall 00:37:27 Okay, so you're saying you're including the idea of setting attributes when you say suppression?
Liudmila Molkova 00:37:34 You don't create your own spend, but you enrich the outer span.
Alex Hall 00:37:39 Right.
That sounds good.
Liudmila Molkova 00:38:14 Okay.
Thanks a lot, I think we spent a lot of time on this, really appreciated,
And let's move on to the next… Comments.
Keith.
The review for metrics.
I think there is a bunch of, comments from Aaron.
Keith Decker 00:38:42 I am still working through the comments from Aaron.
Late last drink, so I'll have that.
Ping Aaron when I'm done with this.
Liudmila Molkova 00:38:50 Excellent.
Aaron Abbott 00:38:51 Sounds good.
Liudmila Molkova 00:38:56 And then Josh, retrieval DBSPAN. I'm sorry, I didn't have a look at the updated, PR.
worry about this.
Josh Winerman 00:39:08 Yeah, no, no worries. I just wanted to get a few eyes on it, then I think I still have to fix a linting issue itself, but that's all.
Liudmila Molkova 00:39:17 Yeah, so from what… Let's take a look.
So when we talk retrieval, and I think Sergey made a good point in the past,
That, by retrieval, we mean the…
the combination. If it's RAG, then it's embedding and DBCore.
Josh Winerman 00:39:42 Yes.
Liudmila Molkova 00:39:44 So this is… this is, like, the abstraction, in Llama Index, or… Length chain.
Josh Winerman 00:39:55 Yeah.
Liudmila Molkova 00:39:57 And if it's an abstraction, over… Let's see…
So, let's say we have a retrieval.
And under retrieval span, we would have, let's say, embedding.
And then we would have a DB call.
Where another example of retrieval spend would be… Google search.
Or another example of a trivial spend would be the similarity.
Where it could be a file search.
So… If we are… instrumenting this layer. It's… it's not a…
database, right? Because Google Search is not a database, or CRAP is not a database.
Josh Winerman 00:41:16 Gotcha.
Liudmila Molkova 00:41:18 And let's think how we would model it, then.
So…
It would have… Whatever properties are available in Llama Index or link chain.
do we know which ones are available?
Josh Winerman 00:41:49 That's a good question, for a Google search.
Liudmila Molkova 00:42:13 And…
Nate?
I mean… One way to think about the retrieval spread.
Oh, it has… it has some properties, right? It should have the…
Some search criteria, the top K, for example.
Josh Winerman 00:42:39 Hmm.
there were a few, base attributes already included in the PR that were… they were more surrounding the embedding DB call scenario than the others. I think that's what we're trying to address here, though, right?
Liudmila Molkova 00:43:03 On the number of documents.
So, for this one…
This would come on the database pen under, right? Oh, this would comma… okay, yeah.
So, it would come here, the number… All retrieved.
documents… Maybe the content.
Bye.
So the key question is, which…
Okay, so once we list all the attributes, which… Namespace do we put, duh.
Or this attributes in, or which namespaces?
If we put it in the dB, okay, yeah?
Josh Winerman 00:44:12 Yeah, I think we, I don't remember… I thought we had previously sort of discussed this and thought that DB… I think dbcall is… or, the DB namespace is appropriate for these.
Liudmila Molkova 00:44:24 Is it a Google search?
Josh Winerman 00:44:27 Now, that's a good question.
what attributes might pertain to a Google search, oh, that's…
Liudmila Molkova 00:45:16 So, less of which properties Google search has, but what are the generic properties that apply to any retriever, right?
Golden Retriever, Labradin Retriever.
Sir?
it seems… bike.
like, looking at least at this example, there is nothing generic. It's all specific to… Oh, data store ID.
Maybe… This is somewhat… generic.
Retrievers.
So when… when you instrument the retriever, you probably can have a list of well-known ones, and they would have individual properties that are specific to that one.
But… it… the… the obstruction…
So there is a query, for sure.
And there are…
documents.
And they have scores.
And they have content.
Sergey Sergeev 00:47:59 Yeah, in general, I can provide a little bit more background about the Finken. Specifically, the Retriever was supposed to cover
Vector Database, retrieval operation.
It looks like there are so many different… Retrievers in different frameworks.
But for a vector database, whatever, we have an input query.
Which is basically a text.
And we have output documents, which were the result of this retriever. And the input query is… so it can be…
you can use LM as a judge, and etc. to analyze the input and output. The problem is that under the hood, there are two more child spans. One is code embedding.
And the second one is DB Search.
So, the traverse plan, purpose was specifically just to provide some metrics
Such as duration, maybe similar… cosine similarity, and etc.
for… this particular operation.
But now, if we look into all the frameworks, there is such a zoo.
Overall, of what is ZT, where…
And the name is a little bit conflated.
Should we try to narrow it down to a specific type of retailer? Like…
VectorDB Retriever, for example, which we… understand and desire. And…
Probably allow some flexibility for other types of retrievers.
Liudmila Molkova 00:49:52 I mean, all the properties you mentioned, they are common across all retrievers that you care about. Also, how would you even instrument a single retriever?
Sergey Sergeev 00:50:00 But does it have an input, an output? Yeah, it does, probably, yeah.
It should work. Maybe… Maybe we can add a type into it?
Because I'm… I'm not real, yeah.
Liudmila Molkova 00:50:18 If it's available, then totally, right? It's what's available. Like, if you want to tie your instrumentation to a specific type of the retrieval, right, you are not instrumenting a layer in Llama Index, you're instrumenting a specific implementation of Retriever. It would…
be very narrow.
Right? And it won't be… it probably will be hard to extend and talk about.
So, if we… Try to apply it to the generic layer.
If… and we can definitely do some specific logic for the vector.
Thing.
Right? It would be much more extensible, and I don't believe it will be more work. It will be just…
More, more coverage.
Option.
So what I'm proposing is that we don't call it DB, because it's not a DB, right? And it would be weird if Google Search Retriever was in the
Sorry, Google Search Retriever, I love it. If it wasn't Google namespace, or search namespace, and the DBRetriever would be in the DB namespace. So let, let's, let's call it search.
I was just…
Where… Retriever.
And retriever type is golden.
No, I'm the real type of retriever.
Or… Any other ideas of the namespace?
Sergey Sergeev 00:52:17 Yeah, I would prefix it with GenAI.
But I understand that, yeah. I don't know, yeah, it's for a specific problem they are solving. Yeah, I think…
I think creatively aware is fine. If we can introduce this namespace as part of Gen AI semantic convention, I will be totally…
Fine.
With having that namespace.
It just feels that it will be very hard,
If we go away from Gen AI, it will be trying to boil solution, because it will be very generic retriever. Who knows what else exists?
in this space. We can't… Yeah, I'm finding the freezer approach.
Liudmila Molkova 00:53:15 So then, bye.
I… I kinda like the idea the retriever is maybe too white, and genai.retriever seems…
Narrow and specific to the point.
Anybody has any thoughts?
shuwpan 00:53:38 So, this retriever is, like, from what source?
Like, is it from a vector TV, or is it from Google Search? Is it something like that?
Liudmila Molkova 00:53:50 It's an abstraction… my understanding, it's an abstraction that exists in Lambda index or a link chain, and it can retrieve from anything.
Shame… Retriever…
So it can… it's… the point is to have an abstraction that
You can plug different sources in.
shuwpan 00:54:21 Oh…
Liudmila Molkova 00:54:25 So chilly…
Retriever… reference…
So we can see…
Is it pig? Is it… Which function are we going to instrument?
Gulk?
Sergey Sergeev 00:55:17 Yeah, in one chain, so they provide callback interface where you basically can implement something on
one relative star, one everywhere end, I believe.
Liudmila Molkova 00:55:32 Yeah, and…
And it's probably the invoke, right? And then you would have input. You have guaranteed input and output.
And the rest is… depends on the… type, I guess.
Okay, this is the name. Oh, it's the runnable.
Okay, anyway.
I'm going to… Pause this in the dark.
And… sorry for… for… for…
Me talking about retrievers, I have a mix of Labrador and Golden Retriever. You should excuse me.
Sergey Sergeev 00:56:28 I have a fake Wabrador Retriever, which never grew into a Wabrador.
Liudmila Molkova 00:56:33 Fake one! Cute.
We need pictures.
Okay, we have a few more minutes left. There is a boilerplate philanthropic.
instrumentation that people wanted to review. Okay, R&D already approved, so it sounds like it should be…
Aaron Abbott 00:57:14 Yeah, I just took a pass, I think the only kind of open question is the name, which is always the open question, so this one is…
dash… this one's already taken also by Open Elementary, so…
We either need to coordinate or do the V2 thing.
Liudmila Molkova 00:57:31 Is PR out there here?
Kia?
Aaron Abbott 00:57:44 Sweet. To you?
Surya Teja 00:57:46 I'm… I'm here. I'm here. Yeah.
Liudmila Molkova 00:57:50 So, would…
Aaron Abbott 00:57:54 It's…
Liudmila Molkova 00:57:55 Sounds like the package name… so which one we picked here? The… the Anthropic… Just downtropic, right?
Surya Teja 00:58:04 Yeah. Had to be 2.
No, we're not fatal.
Liudmila Molkova 00:58:09 So… and the version is… Sorry, I'm…
Surya Teja 00:58:20 It's, 0.3.0, so the version, where everything was rewritten, and it's the most, stable version from which they have started using it.
Liudmila Molkova 00:58:33 Yeah, so what we do usually, so if we want to keep the…
We can try… we can reach out to Nier and ask if he's willing to do the same trick we've done with Vertex.
We… Oh, so the version of this package.
Is it TO, or is it, bueno.
We don't have a version here yet, right?
Aaron Abbott 00:59:09 who's a 20b0, maybe? There should be a version.py file somewhere in the source.
Liudmila Molkova 00:59:19 There is no ver-version file?
Aaron Abbott 00:59:21 If you open up the source, it should be in there.
2 down.
Liudmila Molkova 00:59:28 Oh, I see, sorry.
Aaron Abbott 00:59:30 Yes, there.
Liudmila Molkova 00:59:30 Right.
Okay, awesome. It should be 1… 0, right?
Surya Teja 00:59:38 Oh yeah, I was having a doubt on that, because I have seen,
everyone using a different version, and I was not sure what to use.
Liudmila Molkova 00:59:49 Good question. I think this is the version of this package.
Surya Teja 00:59:55 Yeah.
Liudmila Molkova 00:59:55 Not anything else.
Surya Teja 00:59:57 That's the version of that package. I was… earlier, I was telling you about the version that I use for Anthrophic. Yeah. I was wrong in interpreting that. Your question was, what is the version of the package that we're using in the source? I'm sorry, my why.
Liudmila Molkova 01:00:10 Yeah, no, no worries at all. So, we are out of time, so what I'm suggesting is that, we… let me start… are you on Slack?
Surya Teja 01:00:20 Yeah, I'm just like, yeah.
Liudmila Molkova 01:00:22 Yeah, wonderful. So,
Could you, or maybe, Aaron, you talked to, Nir about it in the past, did you? Could you connect,
Surya? Does it pronounce your name correctly?
Surya Teja 01:00:38 Oh, y-you got it right, yeah.
Liudmila Molkova 01:00:40 Surya, okay, could you connect Surya with Nier and ask if, we can use the Anthropic version? Sorry, Anthropic package, could he share Anthropic package with us, us?
Open telemetry.
Aaron Abbott 01:00:55 Yeah, yeah, we can. I think last time we tried to do this, we didn't have any luck, but we can reach out on Slack.
Liudmila Molkova 01:01:01 Yeah, at least we will have, yes, clear, yes or no.
Aaron Abbott 01:01:07 Yeah.
Liudmila Molkova 01:01:08 Yeah. Thank you.
We are right at time. Really appreciate your help today, and… See you next week!
Surya Teja 01:01:17 Thank you, S.
Aaron Abbott 01:01:18 We'll see y'all later.

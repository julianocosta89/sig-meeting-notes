SIG: LLM Semantic Convention WG
Date: 2025-10-21
Duration: 217 minutes
============================================================

## Zoom Recording Transcript

**Aaron Abbott** 03:25 Hello, how's it going?
**Liudmila Molkova** 04:08 Hello, hi everyone. Sorry for being late.
Let's get started.
**Aaron Abbott** 04:20 Hello, Melan.
**Liudmila Molkova** 04:31 If you want to add something to the agenda, please go ahead.
And… I… There are a few topics from… Mingle… Put them here…
Okay, let's take a look at the project board.
The new issues…
We didn't make any progress on the bunch of issues related to… oh, this is different.
Skills.
Okay, for the sake of… Briyash… it's something…
supported by AT, and it's something we should probably address at some point.
So I'm going to mark it as to-do.
Oh, there is,
There is a triage process, the new triage process, by the way, for general semantic conventions. So now we need pretty much everything to have triage accepted ready.
In order to send PRs to semantic conventions, and if…
it doesn't have the label, or if it doesn't… is not linked to the issue, with this label, the PR might be closed.
Let's see how it works, if it… if it will be a problem, we'll try to find a way to address it.
Okay, so, JSON… Kima.
Oh, Erin, it's yours.
**Aaron Abbott** 06:33 Yeah, I think we briefly mentioned this last week, but,
Basically, the schemas we have right now, they all require all the keys, and then…
They, allow null in the places where we want something to be, like, not required or optional or whatever.
But JSON schema allows you to do, like.
Optional keys, so you could have
A couple different variants where you have, like.
You can see this example here. You can make it so that ID can never be null , and it should be, like, elided instead.
Or you could make it so it could be, like, optional, ordinal, etc, so…
this was raised by Marcella, I don't know if Marcella's around, wants to speak to this, but it's not super clear to me on the trade-offs, because, like, what do we get from making the…
The data more strict.
In this case, but, yeah.
**Liudmila Molkova** 07:29 Oh, I see, so… okay.
It would be nice if someone who is familiar with implications would proceed with the changes.
Sounds… I don't know.
These two sounds look pretty semantically the same, right? It's just one is redundant.
**Aaron Abbott** 07:51 Yeah, I think…
From, like, the producer perspective, if we make it more strict and say, like, if it's… it can't be null , it should just be alighted.
It does have implications for, like, code reading the data, I would say, so… We should just…
maybe come up with a stance here and figure out what we want to do. I do agree, it's kind of ugly if you have, like, a bunch of schemas where every key is required and half of them are null .
So that's kind of the trade-off, I guess.
**Liudmila Molkova** 08:23 Okay.
So… Yeah, let's, put it into the to-do, it sounds… Reasonable, and… Let's update… Accepted.
Ready, wish.
Okay, let's take a look at one more issue, and then let's move on to the agenda. Retrieval spends up, or to Ginia spends.
Oh, I think, there was a pull request, and I… blocked it. So…
Really a good question to everybody here.
the GenAI space is for GenAI calls.
But some Gen AI systems, like OpenAI, has API to upload and download data.
Where retrieve data.
And, like, uploading files or downloading them back.
And, it's… to some extent, unclear whether this call should be captured as GenAI,
Or a database? Or, I don't know, search?
And I think there was… there is this pull request here.
That tries to add… retrieval spans to Gen AI space.
I personally think it's… very limited.
to things like OpenAI Retrieval API.
And most of the…
Things would not scale to other databases.
So this is just a general search for vector database.
Convention that might have some additional OpenAI-specific information.
It's not a general approach.
**Aaron Abbott** 10:48 And this is not in the context of, like, an agent?
**Liudmila Molkova** 10:53 This is… mmm… It might be in the context of the agent.
but might not be, right? It's just the OpenAI Retrieval API.
**Aaron Abbott** 11:06 Hmm.
Yeah, I guess what I'm trying to say is if we have, like, a bunch of agent frameworks that have
Retrieval as a concept.
It might make sense to have, like, a spend for that, and then…
the database should be instrumented, underneath it to capture the, like, the details from this change. But if it's just instrumenting the API, I think I agree. It seems like a…
Like, a database call.
**Liudmila Molkova** 11:36 Great,
Any other thoughts on this? I'm not sure what's the name of this person. If you're here, please speak up.
**Josh Winerman** 11:44 Yeah, hi, Liamla, I'm here. Thank you for reviewing. I was gonna bring this up, actually, later, by the way, but thank you for bringing it up now. I don't think we…
It's interesting, because this is a sort of joint, Cisco Splunk effort, so Sergei, if you had thoughts here that were more clear, feel free to step in, but
I don't think we minded what space it was in, per se. We'd be fine moving based on your suggestion, but it was, to potentially getting some GenAI attributes added to the call, I believe was,
was the intention? Sergey, if you had clarifying thoughts.
That also might be better.
**Sergey Sergeev** 12:29 Yeah, I think some of the fields,
related to Gen AI, like, top-end and, top key, selection and etc, so… I…
**Liudmila Molkova** 12:45 They are not necessarily right. Any search engine supports these parameters.
**Sergey Sergeev** 12:51 Yeah, maybe, maybe. So, the thinking was that we probably need a specific span for Airtable, because it's a generic concept. I don't think…
It,
maybe it can be used as a DB, but then when you try to visualize some framework internal components, it will be…
Really interesting how you stitch together that retrieval span.
into GenAI invocation, or in GenAI trace. That's the only question.
For me, I'm fine to use, just DB.
span in the B, attributes on it.
**Liudmila Molkova** 13:39 Yeah, so, imagine, let's say it's not OpenAI API. Imagine it's MongoDB, or, I don't know.
Something.
the instrumentation for MongoDB.
doesn't know about the context it's being used in, and it has, I don't know, vector search. Every database now has that vector search.
Or it's a Postgres instrumentation.
Then they would produce what they produce.
And the stitching would happen based on the parent span. You would have, I don't know, incoming HTTP request, or incoming server invocation, and you would have some of the LLM calls under it, and some of the database calls under it.
the part, I, I really miss it, maybe, it's, it's probably my, my gap.
Can you help me understand how would you envision even creating the retrieval spans that are specific to Gen AI? Like, what would be the instrumentation that produces them?
**Sergey Sergeev** 14:37 Yeah, Encchain, for example, has a concept of retrieval, which, basically is, operation on top of… so it groups an embedding call and,
VectorDB search.
So first, do you need,
Basically, to put it… to put it together, so it's kind of,
a span which groups those two cores.
I think we can provide a more specific example if it's not in this pull request. Josh, do you have
an example in code. I think you have a demo application.
**Josh Winerman** 15:23 Yeah.
**Sergey Sergeev** 15:24 It shows it.
**Josh Winerman** 15:25 I can follow up on the PR later, I'm on a different computer now, but .
**Liudmila Molkova** 15:36 Yeah, so I would imagine that you probably configure a vector store, right, for it, and the vector store is probably…
A database call.
**Sergey Sergeev** 15:50 Yeah, so it's two things. So, retrieval is basically a code to embedding, and then, a search.
On VectorDB. So, VectorDB, call will produce that DB-specific, span, and abandoned will produce an abandoned span, but retrieval, may include duration, etc.
And this is a question, do we… if we have it in the context of the framework.
For example, some of the attributes from both of those separations. Do we want to put it on a retrieval span, or…
Do we want to just provide very limited information, something like a span to indicate just returnable duration?
And… If we need to…
Put those database and embedding specific operations on those plans.
I think Mitsun's this plan.
I… I think I clearly see the use case for duration and for span itself.
**Liudmila Molkova** 17:06 Yeah, I see your point, yeah.
Sorry, I'll go ahead.
**Sergey Sergeev** 17:15 Yeah, it's, again, the question which comes from Aaron all the time, like,
How do we avoid duplication when you have, In Beijing, Spain.
Some are tables on embeddance pen, and some are tables 1.
vector DB search span.
And, if you put some of those attributes to the parent span, which is retrieval.
will this context be available in all frameworks? Does it make sense at all? Maybe we can include just minimal
Attributes we agree on.
Something like duration and, it's at the end.
In this case, we… For example, we'll have It's a user query.
on the AOM.
on… on the bread and span, and,
We will have documents, for example, retrieved from vector database on the vector TB.
spend.
But I think for some observability platforms, it will be helpful.
to have them repeated on that retrieval span, and this is why those attributes are introduced. I think Josh can, clarify it by providing an example of the application, and example telemetry with both embedding span and VIV.
vector DB search span.
Is there…
**Liudmila Molkova** 18:57 Yeah, yeah, go ahead.
**Sergey Sergeev** 18:58 You have a question?
**Xander Song** 19:04 Yeah, I would maybe just also add, like, just for what it's worth, in open inference, we do… we do also have the notion of a retrieval span. Some of the reasons are similar to what you've mentioned.
But one of the things that it gives us is basically, like, when people are doing RAG,
RAG can go wrong in a lot of ways, and one of the things that people just want to see is, like, native UI for what was the… what was the query, and what were the retrieved documents. And so we have the notion of a retrieval span that lets us
that lets us provide, that kind of, like, native UI,
And it also lets us provide things like the scores that… that the retrieved documents had. Like, so, like, in the basic… in the most simple cases of RAG, when people are just doing, like, a semantic
similarity search, we're able to provide something like the score, which just provides the ability for someone to debug why the
retrieval step went wrong. In terms of the embeddings, like, we also have the notion of an embedding span.
Which records the embedding, but we kind of view them as separate steps.
**Liudmila Molkova** 20:16 Yeah, thanks for the clarification. So, one thing I want to… Brain grab.
So, if you look into just general search, not Gen AI-specific,
So there are a bunch of them.
Which are pretty much the same, and I think OpenSearch and Elasticsearch are in the same boat. They do have all of those things. They have TopK, Top Hand, whatever. They have document scores.
they, do a bunch of stuff that… that GenAI
sorry, that are useful in GenAI context. Oh, I mentioned it here. So, essentially, I would be in favor of doing some conventions that are specific to these cases, but they're not… they don't need to be tied to GenAI. We can still work on them in the SIG, because it's our dependency.
But I don't think they need to exist in the GenAI namespace.
**Xander Song** 21:36 I think that's probably also okay, yeah.
**Liudmila Molkova** 21:39 And it seems like you're following pretty much the same principle, use something like document, right, or…
Input… sorry, the document.
**Xander Song** 21:49 Yeah, yeah. So the… if I recall correctly, like, there's, like, a notion of, like, some retrieved documents that have content and IDs and…
And scores, yeah.
**Liudmila Molkova** 22:04 Okay.
So then it seems like…
Oh, nice, you also had mentioned some DB parts here. That's great.
So it sounds like for this one, the… The key question is, First… the…
So we can do search, we can do…
DB, we need to think about it, but… Either way, Maybe not Gen AI.
Because it's not specific to Gen AI.
**Sergey Sergeev** 23:08 Yeah, and you will have just attributes to indicate that retrieval is JNA spend, it will be JNA operation name retrieval.
And et cetera, right? But the rest of the attributes should be… Generic.
**Liudmila Molkova** 23:28 Yeah, well, probably. And then the bigger question is, are there… Two spans.
Retrieval, MGB. And probably…
Probably yes, because, like, there is an abstraction, and there is a complex operation for the link chain, right?
**Sergey Sergeev** 23:51 Yeah, in general, I think it's one parent spend for retrieval, and two child spans. One is an embedding call, and one is vector DB search.
span. And vector IDB search span doesn't have to be,
GenAI-specific, because I think it may be in just…
A generic search we need to look into it.
V…
are interested in getting something like cassigned similarity metric and etc. from… derived from it in the end. Basically, how close were the documents, to the embeddin?
From the query, and etc. But, specifically, the retrieval, the parent retrieval span,
also is interested… is interesting because it joins that embedding and vector IDB search.
Spence.
**Liudmila Molkova** 24:56 Yeah.
So, I think… Sorry, I had a thought and I lost… oh, okay, yeah. So… is…
With this length chain span, is it a length chain span, or are there other frameworks that have a similar concept?
Do we… how much do we care about semantics of the spend?
Can… can… We do some research there?
**Sergey Sergeev** 25:28 Yep.
I think we have it, but I'll post it, later.
**Xander Song** 25:39 I know of at least a few that have this, so Llama Index and, Haystack in the Python ecosystem.
**Liudmila Molkova** 25:52 Cool.
**Xander Song** 25:53 Thanks.
**Liudmila Molkova** 25:54 So then it sounds like a general purpose problem.
**Xander Song** 25:59 Yeah, it's anytime that… that's the abstraction that we use, at least anytime someone is trying to do RAG.
**Liudmila Molkova** 26:07 Is it the rubber for the whole rag, or just for the retrieval?
**Xander Song** 26:11 Just for the retrieval, usually.
**Liudmila Molkova** 26:13 Okay.
**Xander Song** 26:13 the retrieval step.
**Liudmila Molkova** 26:16 Cool. Okay, so then, it seems that the main…
I can take another look at the PR from this angle, but I don't think it implements this abstraction.
So far, maybe we can have a demo.
**Sergey Sergeev** 26:37 Yeah, we have a demo application, it's just, I think Josh can update it a little bit better in the pull request, and maybe…
To provide more details, in… In that document attached.
**Liudmila Molkova** 26:57 Or in the PR.
Okay.
**Sergey Sergeev** 27:02 Yeah, and specifically, we will need to figure out how the search
the generic search controls if, the documents… if… if content messages needs to be captured or not. Something like to send logs for, the documents it if…
And it should be, opting Similar to content messages, For AOM operations.
**Liudmila Molkova** 27:43 Okay.
So, anything else on this?
Okay, then, sorry, we took quite a bit of time on this topic, I think it's a good one.
We were on the triage part… And… I… I didn't do it.
I promised to do it last time, I didn't yet. I will.
For the sake of time, I'm sorry, let's skip the intro for the new members this time.
oops, I'm sorry.
Okay, so, PRS schema, the tool definition. I think it's just the… offline review.
Alibaba folks are adding more strict definitions for Gen AI tools. They would like to… formalize the…
Properties, let's see…
Right, I think there are some comments on the format, but essentially, they would like to have a definition for the function call, and it would have parameters, and the response format, essentially what you provide to the model when you're defining the tool.
Please take a look.
I… directionally, I think this is a good thing to do. There are some details, questions on the implementation.
**Aaron Abbott** 29:52 Just a quick question, is this, like, different from…
JSON schema, or it's just, like, a wrapper around the JSON schema?
**Liudmila Molkova** 30:02 So this is a wrap-around JSON schema, so parameters and response are in JSON schema.
But the rest is kind of formal.
**Aaron Abbott** 30:11 Okay, gotcha.
And, does this go…
I'll also review the PR, I'm sorry, but, does it go in, like, a separate attribute, or is it part of the inputs or something?
**Liudmila Molkova** 30:23 This is a separate attribute, and we already have it, it's just, it's currently any.
**Aaron Abbott** 30:28 Right, right, right.
Okay, yeah, it looks great, I'll take a look.
**Liudmila Molkova** 30:32 Thank you.
So I think the… one of the discussions there, is…
By default, Minko is suggesting to capture
Just the name and type.
And not capture the rest.
And have the rest opt-in.
I… It sounds like a complication, but it also sounds like these parts are very verbose.
So if anybody has thoughts on how to capture two definitions, please chime in.
Okay, another trivial PR to review.
Oh, it's already merged.
So, then, just as… an announcement, we didn't have the
name of the participant on the message, and Ming Hui has edited.
Sorry.
Don't think there is much to discuss here.
Okay, Aaron, let's talk about multimodal stuff.
**Aaron Abbott** 32:04 Yup.
It looks like… it looks like, I got some reviews from you and Alex yesterday, which I haven't looked at yet, or I looked briefly at, but,
Yeah, just bumping this one again, I think Marcelo's also working on some kind of…
Prototype or proof of concept of this, although we have it already in, like, a…
Or something pretty similar in the Vertex and the Google Gen AI instrumentations. Yeah, Ludmil, I saw this one,
I think… Maybe the confusion is because we're using, like, JSON schema…
to represent something that goes into the any value in the Hotel Piperto.
**Liudmila Molkova** 32:51 And then it sometimes would be bytes and sometimes a string.
**Aaron Abbott** 32:56 No, no, no, well, yeah, like, there's the issue of the complex attributes, in which case
JSON encoded, so obviously there's no bytes in JSON, so…
this is kind of just giving the strong sense that you should use Base64 there. And then we also, like, serialize these JSONs to,
to… Store them as references, right?
So for that use case also, where you would put it in, like, a GCS object or something like that, you should use the Base64 encoding.
**Liudmila Molkova** 33:31 Yeah, but, like, imagine…
**Aaron Abbott** 33:33 Weird.
**Liudmila Molkova** 33:34 We didn't have a problem of…
Complex attributes, they were allowed and spent.
Good year.
Would we tell instrumentations to use bytes?
The array of bikes.
**Aaron Abbott** 33:50 Yeah, they should use bytes in the AnyValue proto, right?
**Liudmila Molkova** 33:57 Right, then it means that most instrumentations would need to get the data, decode, Base64 Decoded.
And then put the decoded bytes.
**Aaron Abbott** 34:12 Yeah, I think… I think we had a similar discussion already about this, but…
So, like, I mean, obviously there's the benefit of the size when you store it in the attribute, so, you know, like, there's roughly 20%
better than using Base64 if you have a native byte instrumentation, or sorry, native byte value type.
I think… I'm not sure what the OpenAI instrumentation does today,
It seems like their client requires you to pass the Base64 directly, you don't, like, you can't provide it.
A byte string, and then,
It will handle the conversion for you?
**Liudmila Molkova** 34:50 But I would imagine the JSON API they have accepts
Base64, because it's a JSON-based API.
**Aaron Abbott** 35:03 Right.
**Liudmila Molkova** 35:05 And I see what you mean, so maybe.
**Aaron Abbott** 35:09 Yeah, like, I guess what I'm trying to say is that somebody had to base64 encode it first, so if you're able to intercept before that happens…
**Liudmila Molkova** 35:20 So, okay, so the trade-off here is that bytes, the array of bytes, has better, payload size, less overhead, on the payload over the wire.
It might have more overhead on the performance, because you need to do extra conversions,
And I would imagine if you get data from the model, it's lazy, so you probably… Don.
Convert it to bytes unless the application wants it to be in bytes.
and it's more work for the instrumentation.
**Aaron Abbott** 35:59 Okay, so is your concern mostly just the CPU usage for potentially converting it to bytes? Like, unencoding it?
**Liudmila Molkova** 36:07 Kinda, yeah. That's it.
**Aaron Abbott** 36:10 Yeah. I mean, like you mentioned, obviously, like, the Google APIs can do protobufs, so there's not really any additional thing, because it's already just bytes.
I mean, I…
Yeah, Alex, do you wanna…
Alex put a comment, like, CPU usage, is it significant in the context of the AI network calls? Like, doing a…
decode or encode on the basic C4.
**Liudmila Molkova** 36:50 Yeah.
**Alex Hall** 36:51 We can also just say that, you know, instrumentations can choose to do what they want, you know, some may be able to intercept, some may not.
You know, so… sometimes… the API actually expects you to pass a Base64 data URL.
And I just think, you know, it should be somewhat clear in the spec, you know, what to do in these kinds of cases.
But…
I don't think it matters that much which one we choose. Maybe we should even let it be flexible.
**Liudmila Molkova** 37:23 Let's try to not let it be flexible. I think you're…
And convinced me that bytes is reasonable. Then the only concern is that now that instrumentation
Should have this temporary hag, that it's a string.
And we have this contradiction here that it's bytes, but… but now we immediately are saying that in some cases it's a ring.
**Alex Hall** 37:54 But that is a general hotel problem that we have.
**Liudmila Molkova** 37:56 Yeah So, what, what maybe we can do is, if we…
**Alex Hall** 38:04 Oh, okay, Bruno, go ahead.
**Liudmila Molkova** 38:12 Oh, I cannot hear you.
**Aaron Abbott** 38:13 Hell, yeah.
**Liudmila Molkova** 38:19 Nope.
**Aaron Abbott** 38:24 No.
Okay.
**Liudmila Molkova** 38:31 Okay.
**Aaron Abbott** 38:32 We'll watch for your chat.
Yeah. I mean, I definitely agree with Mo, like, I feel like we should be opinionated here, like.
it feels weird to have… in the context of just OpenTelemetry, it feels weird to have, like, a base64 string and an attribute when we, like, explicitly support bytes directly.
**Liudmila Molkova** 38:55 Maybe we can… Say it's…
Okay, Brandon, that we need a blob type if we allow bytes.
Not sure what the blob type means?
**Aaron Abbott** 39:13 Do you mean in the, like, in the GenAI schema, or in OTLP?
Or somewhere else.
We do have a blob as part of this PR, so this is part of a type that was, like, there's 3 variants, there was URI, file.
like, like OpenAI Files API, and then there was a blob type.
**Alex Hall** 39:49 As in, it's a blog part-time.
Nope.
**Aaron Abbott** 39:53 Yep.
**Liudmila Molkova** 39:54 Yeah.
So, maybe we can say that it's any for now.
We can leave a to-do, saying that once we move on to the complex attributes, it should become bytes.
And for now, it's… Either Bytes or Base64.
Or it's just bites?
Period.
And then Jason would ugly encode it.
**Aaron Abbott** 40:26 Yeah, I mean, that's… that's kind of the proposal here. I would… I would definitely prefer to not make it any.
**Liudmila Molkova** 40:35 So then let's just remove this. Let… let's…
Agree that it would be ugly encoded.
**Aaron Abbott** 40:43 I mean, we do convert it to JSON sometimes, right? Like, it's valid to encode these as JSON.
**Liudmila Molkova** 40:49 Yeah, it would not be Base64, right? Instrumentation wouldn't need to have the…
**Aaron Abbott** 40:56 Like, like, if you just took the attribute and you sent it over the wire.
like, if you took the attribute as the any value, and you wanted to convert it to JSON, right?
**Liudmila Molkova** 41:07 Right, it would be at a rate of bytes, kind of… in, in JSON.
It would be valid. It's just inefficient.
**Aaron Abbott** 41:17 there's no array of bytes in JSON, right? Like, how would you…
**Liudmila Molkova** 41:20 Array of integers, okay.
**Aaron Abbott** 41:24 Oh, I… see, I think this is the problem, like, there's no canonical encoding.
For bytes in JSON, right?
**Liudmila Molkova** 41:31 the array…
like…
I'm not sure, maybe there is some special… special thing in Python for bytes, right? But in other languages, the byte array is just a byte array.
**Aaron Abbott** 41:47 Yeah.
**Liudmila Molkova** 41:48 And then it's just encoded as an array of integers in JSON.
**Aaron Abbott** 41:53 I see what you're saying.
Yeah, I don't know, sorry, maybe I'm a little biased by, like, protobuf background, so please keep me honest, but I feel like most languages do have some kind of, you know, byte array distinction, and they can differentiate between, like, pair array and
Something that's supposed to be a byte string, but…
Yeah, please keep me honest, like.
I think the usual encoding I've seen for… like, the one that OpenAI uses is to convert to a Base64 string, right? Like, they don't ask you to send an integer array.
**Liudmila Molkova** 42:30 Yeah.
Okay, so maybe we can take it offline. I feel it's pretty minor, and okay. And it's purely technical, so maybe, you know, let's chat about it. Line.
**Aaron Abbott** 42:42 Okay.
**Liudmila Molkova** 42:42 But in general, yeah, I,
Okay, I think the rest is… Trivial and non-controversial.
**Aaron Abbott** 43:18 Okay.
Great, thank you.
**Liudmila Molkova** 43:22 Okay, yeah, we talked about this one, thank you.
**Aaron Abbott** 43:26 Aww.
**Liudmila Molkova** 43:28 Keith, you've added this one.
**Keith Decker** 43:34 Okay, yeah, this is a proposal for adding workflows and tasks to SEMCONS, because right now with,
With the agent spans, we don't have the ability to track, kind of, the overall workflow. I noticed at the top of the doc, you had something about workflow tasks. Did you…
Is there another meeting being set up for task workflow specifically, or can we talk about it here?
**Liudmila Molkova** 44:02 So the thing we discussed last time, and I didn't follow up, I'm sorry, that there is a meeting between Cisco and Microsoft. I'm not part of it, it happens, I think, on Mondays and some other days.
And what I wanted to do is to set up an official hotel call that we can all participate in and know about.
**Keith Decker** 44:22 Gotcha.
Okay, so, back to the issue, then,
We have a whole proposal here on what attributes to add around workflows and tasks in order to be able to track individual agents that are part of the bigger workflow.
Wanted to see what… what thoughts are around going forward with this, if we can get any comments, feedback, and…
Move on with it.
**Sergey Sergeev** 44:59 Yeah, it may be a question to Alexander, what do you guys do for representing?
Basically a workflow, and when a workflow is not agent invocation.
**Xander Song** 45:25 This one, I'm… I'm not as… as sure of, the… the use case. It's really for… intended for, like, long… long-term jobs, is that… that's the intention, right?
**Sergey Sergeev** 45:37 Yeah, I think in, Wing Graph,
basically, a chain… change, a mapping to that workflow.
Ian.
As a frameworks.
There is a top-level, concept as well, for… Workflow.
So, when you start a graph, the whole graph in one graph, it's a workflow
basically, to, to indicate, when you start, that execution of a graph.
Do you have this representation in your instrumentation?
**Xander Song** 46:26 But it's more general than just graphs, right? Or is it specific to graphs?
**Sergey Sergeev** 46:32 I think, initially, if it's coming from a WMG graph,
And I understand that in MCP or A2A, for example, there is a session concept which groups
a lot of remote MCP calls and etc.
But I'm wondering if you have, on your side, this concept at all, or is it specifically…
WAN graph-related, and, how do you do it without,
That top-level concept which helps you to group different plans for…
Distributed, execution, which doesn't fit.
In term, basically, one trace.
Yeah, and even a disregard of how the group responds. Do you have that representation on your side?
**Xander Song** 47:34 Of a workflow? I don't… yeah, of a workflow, I don't… I don't think we do.
not to say that it isn't useful or something, I'm not sure… I think I still am maybe not…
Familiar enough with the concept to… to know
what it might… it's basically, if I understand correctly, supposed to be, like, a grouping of traces?
Is that right?
**Sergey Sergeev** 47:59 Yeah, grouping of cases, but also when you execute. So… so basically, when you…
When you have a lot of agents which are nodes on a graph.
So you have agent invocation representing each of the nodes, but, the whole graph, when you create the graph and when you group.
everything.
In single unit.
If, how do you represent it on your side?
**Xander Song** 48:38 I would need to look into that a little bit more. I'm not the most familiar with, probably, Langraph.
In terms of, like, the grouping of different traces.
we do have, like… I know, especially on the main platform side, for Arise, like, we do have…
graph visualizations and things like that. Is that the sort of…
Thing that you're trying to facilitate?
**Sergey Sergeev** 49:03 So, first of all, just to represent,
When you execute that graph?
So something to group multiple agents and etc. One option is to use another agent invocation, which kind of, not necessarily agent concept, but just to group
To define the entry point.
and to track, for example, execution duration. Second approach, I think, is using session.
Attribute, which can be used to group multiple agent invocation, and so on.
**Liudmila Molkova** 49:48 I'm… So, this is the parent span, the root span, that would drop it all.
**Sergey Sergeev** 49:54 Yes.
**Liudmila Molkova** 49:56 Why does it need to have any semantics? It's just a root span.
**Sergey Sergeev** 50:03 So it can be HTTP, HTTP, span, or whatever.
**Liudmila Molkova** 50:11 Right.
It can certainly have some attributes, yeah, but does it?
have to be GenAI span.
**Keith Decker** 50:27 I think one of the things that was of interest in the overall workflow was the prompt that started it, as well as the final output, if that's the case. The other thing was potentially what type of workflow, whether it's, like, a sequential, parallel, that kind of thing, if it's graph or dynamic.
I think there was some of that interest in… in showing that in our collection on our site.
**Liudmila Molkova** 50:53 And presumably, we would know.
All of this, when it starts.
**Keith Decker** 50:59 Presumably, yes.
**Sergey Sergeev** 51:02 Yeah, I think we had one action on our side, is to… to review a few of the frameworks, like OneGraph, WAMA Index, maybe OpenAI agents, and just to see, what,
Which concepts will represent workflow in those frameworks?
It will really help, to understand if it's when graph-specific, or… Generic thing.
**Liudmila Molkova** 51:44 Sorry, a few more questions,
what is the task? Like, how do you…
Is it the… okay, this is the link… a link graph-specific concept, or it's…
Generally, can we define it, that it's not tied to Langgraph?
**Sergey Sergeev** 52:02 I think a better name in this step.
**Liudmila Molkova** 52:06 And then is… is it different… how is it different than Invoke Agent?
**Sergey Sergeev** 52:11 It's basically the minimal, atomic thing, which may be not even, lM-specific, something like,
I think when you do just computation, Not a tuco, but,
Again, it's one graph-wing Smith, or one graph for one chain, specific, I think.
But I think it's a good point, to…
Explain again which frameworks have this concept.
If it's, one chain or one graph, it's like a…
**Liudmila Molkova** 52:56 Yeah, so, like, if we… if… if…
Some framework has something that's worth instrumenting than it can be instrumented. We might not need any conventions for this, at least not
Central Conventions.
**Sergey Sergeev** 53:18 Yeah, for a LAMA index, for example, there is a workflow, and workflow, Consists of steps.
So we need to find out, what are steps when… when it's not agent in vacation, or when it's not due on vacation.
Then it will be a step.
Kind of fallback, which is… Not one of those.
**Liudmila Molkova** 53:53 Yeah, so I think that…
If we can define workflow and or task in framework-agnostic way, and we see that there are, like, there are similar notions.
Then it would be great.
there are a bunch of small feedback points I… I would… share, like… This workflow… It's…
And I don't know how much we benefit from saying it's something GenAI-related.
It's not really GenAI operation, it doesn't have to involve GenAI.
But that… that's up for discussions. This, the GenA framework, it's the instrumentation scope name. You don't need to have an attribute for this, it's just instrumentation scope name.
**Sergey Sergeev** 54:54 I think there is a difference, basically, between instrumentation and the framework.
It is using, because you can have,
different instrumentation libraries for a length chain, for example.
**Keith Decker** 55:14 And, like, LightLLM can be a framework that has multiple different Instrumentation's underneath it.
**Liudmila Molkova** 55:23 Yeah, well, we… we can… again, this is the name of the instrumented library, then. It's not a GenAI…
Framework. Well, okay, anyway, so this is the naming.
These guys are now attributes, right? This is GenAI input messages, and this is GenAI output messages. There are no span events anymore.
And, it's just to… Simplify things.
**Keith Decker** 55:55 Right, right, I can go fix that.
**Liudmila Molkova** 56:00 This is the, probably, if the task is a step and is an invoke agent, this is the system instructions.
And this is the spend status.
Or…
maybe there… there is a need for some additional status. It's like, okay, so the… then the general feedback, sounds like…
We… we… Would like to understand how it maps to different frameworks, right?
And… That's the… the key part. The rest is just cosmetic… cosmetics.
Okay.
**Keith Decker** 57:02 Thank you for the feedback.
**Liudmila Molkova** 57:06 Yeah, thank you, and we are pretty much at time. Anything else for the last 3 minutes?
Then thank you. Have a great day, and good to see y'all.
**Aaron Abbott** 57:20 Thank y'all, I'll see you later.

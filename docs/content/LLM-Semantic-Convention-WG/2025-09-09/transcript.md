SIG: LLM Semantic Convention WG
Date: 2025-09-09
Duration: 65 minutes
Zoom Recording URL: https://zoom.us/rec/share/VNk6dbtWVrMbN8P16OUjkfJkHByzh693K2NXlJbIHz_TO_8KyjRDjKVguoZM_nvn.cKmPs8N_LCwlElK5
============================================================

## Zoom Recording Transcript

Bruno Baptista (IBM) 00:01:37 Hello.
Shuwen Pan 00:01:41 Along.
Eric Deandrea (IBM) 00:01:42 Blue.
Liudmila Molkova 00:03:05 Hello, hi everyone.
Shuwen Pan 00:03:09 Hello?
Bruno Baptista (IBM) 00:03:09 Hello.
Liudmila Molkova 00:03:12 Okay, let's get started. I'll share my screen in a second.
Come on.
Okay, here we go.
So this is, our meeting notes. Please add your name to the attendees list. If you have any topics, please add them to the agenda. We have it packed, so,
I hope we can make progress on at least, most of this.
Okay, while we are waiting for folks to join, we do a couple of things. The first one, we go through the project board.
And it's a little bit neglected.
Oh, and messy. So we try to see if there is anything new, and something we can clean up.
Here.
There are quite a few…
new issues. I think some of them, have been here from the last week.
So there are a group of related issues and some PRs regarding the agents.
I think… We wanted to review corresponding PRs, right?
And… I'm just checking what's going on there.
There are now discussions here.
It's the same line.
skills, so, if you have any thoughts on… the… how to represent… agent work.
in terms of workflows, tasks, so if you have any thoughts on this, please go ahead, comment on one of these issues. I'm intentionally keeping it here as new.
Until we know what to do with it, and we have…
Group of people who actually wants to move it forward.
Do we have, Ankit here?
No, we don't. There are a couple of issues related to evaluation.
Scores?
And confidence interval.
I…
Would rather, triage it to no status unless somebody knows how to use it and wants to bring them to
So, the specification.
I would just keep it in the backlog.
If you have any thoughts, suggestions you'd like to see it addressed, you can always comment.
And we… And prioritize it.
I think we created this front, the two definitions, to specify the schema for two definitions as a follow-up.
Do we have a shipper here?
I don't think so.
So, Aaron, maybe you know the context. You discussed… you had a discussion on the PR, right?
Aaron Abbott 00:07:11 Sorry, which PR?
Liudmila Molkova 00:07:13 The tool definitions.
I think you wanted to see a schema for the two definitions defined, right?
Aaron Abbott 00:07:22 Yeah, so,
Right now, it's just an any, basically, and since the tool definitions can be quite large and structured, it seems kind of similar to the
You know, system instructions and such, except that There's not really,
Probably not a strong need for remote upload, like, they'll be medium-sized, but anyway,
Most vendors have, like, some kind of envelope.
for calling OLMs, it wraps the…
actual JSON schema definition, like the one for the tool itself.
So I was kind of just suggesting
Some kind of either guidance or ideally, like, a standard format so that it's not just in any.
Liudmila Molkova 00:08:07 Okay, what do you think would be the benefit of having a common format to reshuffling the schema… sorry, the tool definition into the common format?
Aaron Abbott 00:08:17 So, so actually, it's more just, like.
the… I think several vendors have
there was a discussion in the PR, I don't remember the specific thing, but…
Most… most people use JSON schema for the tool definitions, right?
Liudmila Molkova 00:08:31 Mmm, I see.
Aaron Abbott 00:08:32 Can't say…
Liudmila Molkova 00:08:33 It's a JSON schema and be done with it.
Aaron Abbott 00:08:35 Yeah, or we could say just, like, there's also, like, a…
So there was, like, a slight difference between how, I think, at least Gemini and OpenAI
wrap the JSON schema, so there was just, like, two different keys, for example, and then the JSON schema was under that key, so just having some kind of standard there so that, it's easier to consume.
Liudmila Molkova 00:08:57 Oh, I see, I see, it makes sense.
Okay,
I'm thinking this is, would be a great addition to… This pack,
And I'll put it in to-do.
Essentially, how I envisioned the to-do is that
It's something we would target before stability.
And things in the backlog are pure additions, and… non-breaking, in the future.
Okay, I'm keeping the GenAI, agent stuff here in the new issues, and we're out of our TRH timebox.
So, let's move on to the agenda, and before we do this, let's use a few minutes to get to know each other. If you're new to this call, to this group.
Feel free to introduce yourself, or…
You stay quiet, it's your choice, but we would love to know who you are, what brings you here, and how we can be helpful.
Eric Deandrea (IBM) 00:10:13 Yeah, I can introduce myself. I'm Eric D'Andrea, I work for IBM, formerly Red Hat. I was dragged here by Bruno Baptista. I've been working on some prototypes around observability in the AI space and trying to standardize and be able to report on
you know, when things go off the rails, which they likely do, how you can track that in real time. So, happy to be here.
Liudmila Molkova 00:10:40 Great to have you.
Anyone else?
Okay.
So then let's, actually, Eric, it's… The spot is yours.
Bruno promised us the demo.
Or the prototype, and if you wanna, present, go for it. If you want me to present, tell me what.
Eric Deandrea (IBM) 00:11:14 Yeah, I can present. So he… I showed him this and the… I guess I gotta share first, huh?
Boombaum brum…
So, I've been working in the underlying application and the implementation is kind of irrelevant for this conversation, more so the observability part of it. So, the story I've been trying to weave for a while now is in this AI space, if you make a change, you either change your model, or you change your prompt, or you change your application, you change something, how do you know if you got better or worse? And that's kind of the story I've been chasing for…
for a while now. And so I've started to put together, using some tools that publish into, like, OpenTelemetry and the Collector, different types of metrics where I can go into a dashboard,
Let me find it here. I can go into a dashboard, and let me find some data here…
And I can look at, in real time, you know, what's it cost me, but more importantly.
these… the failure rates of, you know, when an LLM comes back and it either blows up, or we have this thing… so I work on LaneChain for J as well, so I'm in the Java space. In LaneChain for J, we have this concept called guardrails, where you can put these, they're kind of like interceptors, just think of it like theoretical interceptors before and after LLM invocations happen.
And they can detect, like, hallucinations, or you can build whatever you want. You can either validate input before you send it to the LLM, or…
look at what the LLM spits back out after it's done all of its tool invocations and whatnot, and then if it's not what you expect, you can re-prompt or, you know, re-augment the LLM to say, hey, you didn't do what I wanted you to do, and send it back and get results back. And so these are more like…
as the name goes, they're guardrails, so they're not supposed to be… look, you're not supposed to invoke them 3 times on every LLM interaction, right? So if you have to start to see over time that
for each interaction, your guardrails execute 3 or 4 times, that's not a good thing. You know, you're spending more money than you need to, your prompt is wrong, or something's not right, even if you eventually get to the right answer. So I've been trying to put together metrics and dashboards around that.
scenario, and, you know, in laying chain for Jade and in Quarkus is kind of my… where I've been working on this. Right now, none of this is part of any framework, this is just kind of like my own little…
POC or proof of concept I've been putting together for now.
and a way to correlate that back to, okay, if I want to, like, kind of go back in time, and okay, I know what the system message was, I know what the user message was, and I know what the eventual response was, can I score that using, you know, cosine or semantic similarity or some algorithm to score that? And if I make a change, can I replay that and re-score and see, you know, did I get better or worse? So, part of it is metrics and
you know, Prometheus and OpenTelemetry, part of it is recording the actual payloads of what happened, and then being able to play it back. And that's kind of what I've built here.
So, in the dashboard.
Bruno Baptista (IBM) 00:14:31 Sorry. Go ahead. Sorry to interrupt you. So, and this was based on the audit events that we were talking last week, right?
Eric Deandrea (IBM) 00:14:40 Yes, yeah, so I have in… in my application, I've exposed… so the framework exposes…
these events when things happen. So in Langchain for J, when… just before a message goes out to an LLM, or a tool invocation happens, or a response comes back, or a guardrail is executed, it's firing these events that the application, or…
what should be a framework, but an application can listen to and do what they want to do with. And so I'm taking them, and I'm transposing them to OpenTelemetry counters and meters and whatnot, and I'm publishing those to the OpenTelemetry collector, and that's where I'm getting this data on the dashboard.
I also have, and this is still in the application itself, I have a,
So I can go into, like, Swagger UI, and I can play back, you know, for a given time period, I can play back…
I'm gonna go back in time here.
20…
I don't know why it says 2022, but in any event, I can go back and play back for a given interaction. Like, one interaction with the LLM might involve multiple tool calls, multiple round trips to different.
models, multiple guardrails, I can play back an entire… I can group that by an interaction and be able to play that back, so that I can look at what the input was, what the output was, whether it was a failure, how many guardrails, what the average execution time was, and I can really start to answer the question, did I get better or worse? And that's kind of the…
what I'm trying to go and get down to.
But that makes sense.
Liudmila Molkova 00:16:17 Yeah, this looks great. One thing to note is, it's essentially what we are doing with semantic conventions. We're defining the spans, and you can also record events.
And they provide pretty much the same information, all except the guardrails, and to a certain extent, you can replay
what happened. What… did you have a chance to look at semantic conventions? What made you…
Just something completely different.
Eric Deandrea (IBM) 00:16:57 Yeah, so I guess I wasn't familiar… I mean, I'm a user of OpenTelemetry, but I wasn't familiar with all the standards or what was going on, and that's kind of… when I showed this to Bruno last week or the week before, he was like, hey, you should come show this, and, you know, either you can learn from us, or we can learn from what you're doing, or combine. If there's stuff that we're missing, you know, we can kind of talk about. So that's kind of…
where this all came from, so I… this was hastily put together because I wanted to talk… I was at Java Zone last week in Oslo, and I wanted to use this as kind of the theory behind my talk, so it was thrown together as fast as I could in the weeks prior.
You know, using pieces that I could… that I had control over, so that… I guess that's one reason. It does have all the spans and all that stuff, so each time these things happen, it's part of the trace and the span and all that stuff, too.
Bruno Baptista (IBM) 00:17:48 Yeah, so sorry for getting into the conversation. So, this was especially interesting to me because the events.
They are triggered, and they can be, handled by other systems,
in a different way, and if…
So, we are storing the interactions in the spans, that's true.
But… In order to score this, we need to go to the span storage and query for that.
And that might not be,
well, really integrated with the applications. Sometimes we want to have this locally, and by triggering this
these, these events that they have a life of themselves, we can reroute them in different ways that we cannot withstands effectively.
So, it's kind of a duplication of information, but they… they can be used in very different ways.
Samuel Colvin (Pydantic) 00:18:54 Sorry to jump in, Samuel, here. Two things. First of all.
in addition to Lyudmela's point, as I understand it, there's no reason why…
guardrails shouldn't be recordable using the same semantic conventions. It's just an LLM call. I mean, the fact you're using it for something else is…
Interesting, there may need to be some semantic conventions around guardrails, although I'm not convinced that they do.
and they mean different things to different people, so they probably need to settle down in what they mean a bit more. But again, they're just LM calls, we could record them. I also… I'd push back a bit on the idea that, like, there needs to be… the data needs to live somewhere else. I mean…
If you can't use your observability platform locally.
that's a limitation of your observability platform, and I would gently push you towards some that you can use locally, but more generally, like, that's not a…
like… That… all of those use cases should be… should work with semantic conventions.
Eric Deandrea (IBM) 00:19:49 Yeah, so guardrails aren't necessarily an LLM call. A guardrail could be…
Samuel Colvin (Pydantic) 00:19:53 hey, I expect the response to be JSON and in a certain format, and the LLM responds with, okay, I'd love to give you some JSON, here it is. And, you know, obviously that's not marshable using JSON, Jackson, or whatever, so you need to, you know, kind of retell the LLM, hey, go try that again, but really just give me the JSON.
That's just a response to, in general, a tool call, or another message, right? That's just…
I mean, if you're using tool calling for structured outputs, then that's the return type to a tool call. If you're using, like, other forms of structured outputs, then that's just a response message, like.
Yeah.
Eric Deandrea (IBM) 00:20:32 Yeah, I don't know. I don't know that I generally…
In some cases, yes, it could be thought of like a tool, but in other cases, it's not necessarily. It's just guarding against what the… it's kind of like a hook after the response comes back, and after all your tool invocations have happened. Okay, so here's my final result before I send it back to whoever asked for it. Here, one last chance to kind of…
Look at what it was.
Samuel Colvin (Pydantic) 00:20:57 I don't know, I mean, there may be space for semantic conventions for, guardrails, although, like I say, I…
I think there are… if anything, we have too many semantic conventions and not enough usage yet, but anyway, there's definitely a potential for that.
But I suppose my high-level point is, and I'll hand over to Aaron in a second, it's still just… it still fits with OpenTelemetry and semantic conventions at a high level, I think.
Aaron Abbott 00:21:27 Yeah, yeah, I definitely agree with the last point, like, if there's a use case for schematizing this, I think it does fit with the project goals. Yeah, I was gonna say, like, I'm trying to understand the difference between this and, like, a generic kind of callback or validator. I guess the point is for it to be useful for evals, right? So you want to have a schema?
Eric Deandrea (IBM) 00:21:49 Yeah, so that you can… it's more of a… Like, I…
I mentioned that if these guardrails, they do retry, so if a guardrail
reprompts an LLM, and the LLM comes back with another response, and it still doesn't pass, and you can configure how many retries it does. At some point, you need to give up and just let the thing fail, but part of your heuristics is, on average, per interaction, how many times is this… are these particular things firing?
And if it's more than one, then something's not right in your system, right, as a whole, because it's costing you… if your guardrail's having to intercept and re-prompt the LLM to do something else five times on average, then something's not right, even if you get the eventual right answer.
Aaron Abbott 00:22:35 Yep, yeah, I got it.
Eric Deandrea (IBM) 00:22:36 That was kind of my use case. I mean, there may be others, but that's kind of the angle I was coming in at.
And it's across models, so it's not particular to OpenAI or Gemini or whatever, it's more of a generic concept.
Liudmila Molkova 00:22:56 Hey, Bruno?
Bruno Baptista (IBM) 00:22:59 Okay, so, do you think, then, that we should, work around adding this information to spans?
And as a good example, Alex mentioned that OpenAI agents use specific spans for guardrails. Should we create spans when we execute those guardrails?
And later retrieve that, that information for analysis from the, The trace storage, basically.
Liudmila Molkova 00:23:35 So there are…
two different parts, right? So the one question, do we want to record guardrails on something? How do we record it?
It sounds like there is some discretion, there is some,
examples of where we can, and we probably need to have this discussion. And there is a separate question, how do we,
we're… Do we replay from?
And where… what data do we run the walls on, right? Is it data stored on the observability backend or something else?
Guess what? If you record this as a telemetry, you can use this data. You can forward this data to a separate storage.
it doesn't have to run on the SPAN, storage. We also have events, you can record this data as events, you can forward this event somewhere else.
I think those two questions are orthogonal, right? What is missing in semantic conventions? It seems guardrails or some, guidance on how to record them. And what is the source of your replay or Evolve's data?
Right.
Let's separate them completely.
Bruno Baptista (IBM) 00:24:49 Okay.
Liudmila Molkova 00:24:57 Thank you, it's a great demo, it's great to see that we are, like, I think it, to a certain extent, it doesn't matter how we record the data. It matters what experience we want to provide, and it's great to see we are solving the same problem.
Eric Deandrea (IBM) 00:25:15 Yeah, of course, after I showed it to Bruno, he told me I was doing it all wrong, so I need to go back and fix it.
Liudmila Molkova 00:25:20 there is no wrong, there's just different opinions, right? But, one thing I would love to, share and get your opinion on, so…
it sounds like what, what you have
Sorry, I'm looking what you have in audit events.
It's pretty much what we have in this Event.
This is the inference operation details.
Of course, things… some things are different, the way we record them is different.
But…
this one contains pretty much everything that you want to record, and I would love to hear your opinion, your, like.
If something doesn't look right, or if you think there are useful additions.
We would be happy to hear your feedback.
Eric Deandrea (IBM) 00:26:21 Yeah, I'll have to go through that and kind of map it back to what I did and see…
Is it complete overlap, or did I invent new stuff that I think is relevant?
Bruno Baptista (IBM) 00:26:33 I can help with that, Eric.
Eric Deandrea (IBM) 00:26:36 Yeah.
Yeah, I'd like to be able to do that. Maybe you and I can work offline.
Liudmila Molkova 00:26:47 Quay! Thank you for the demo!
Eric Deandrea (IBM) 00:26:50 Alright, thanks for having me.
Liudmila Molkova 00:26:55 Okay, this one, moving on, and this one is from Minghui, I think.
He's not here.
I think this is the ask to take a look at the pull request. By the way, Bruno, Eric, the Alibaba folks are adding instrumentation
For the… I'm trying to understand, maybe Spring AI?
And if you would be interested to review and collaborate, it would be wonderful.
Eric Deandrea (IBM) 00:27:40 I'm sorry, was that a question for me?
Liudmila Molkova 00:27:42 It's not a question, it's just the opportunity to collaborate. I think Alibaba already in Spring AI instrumentation, and it's, since it's Java ecosystem, I know you probably are not best friends with Spring, but…
Eric Deandrea (IBM) 00:27:56 I'm a former committer, so… but long before Spring AI was a thing.
Liudmila Molkova 00:28:00 Yeah, so if you want to take a look at the PR, it would be cool. If not,
Then, so be it. It seems there are some questions,
Unified management of the capture of input and output messages in multi-turn.
conversation scenarios.
Will there be multiple user messages, so multiple message parts within a single user message?
I mean, it sounds like there is some… Something is not clear.
In this pack…
Alex Hall 00:28:42 I think the apples in the spec, so…
Liudmila Molkova 00:28:49 Yeah.
I don't understand this question?
Agent Framework and model client SDK Instrumentation. Oh, I think so, maybe we need to clarify that.
More that what we have today doesn't yet work great for agent frameworks.
Okay, I'm sorry I didn't have a chance to look, the notes before the call.
And this is the usual question.
About the base URL by framework.
to share the context, when you say that something… when you have OpenAI SDK, and you report GenAI
Spans, or logs, or metrics. You can only guess what's on the backend, and we have no
Reasonable means to know what you're talking to.
So we currently say it's OpenAI,
So I think, what we have in this pack is that we do the best effort.
Well, if you see OpenAI endpoint and it contains Azure, then maybe it's an Azure OpenAI, but… but… yeah.
Okay, so I wanted to, bring up, This discussion,
On the external storage, and
There are a couple… oh, the langchain instrumentation.
The PRs on the bottom is something I shared from the last week. I'm keeping them on the bottom, unless somebody works on them, wants to bring them up.
A year.
So…
I'm sorry, I cannot type.
There is a pull request from Aaron.
Which adds the external storage support.
Right, and… Sorry.
this one.
And it seems we have some… we have two different approaches on how to do this.
So I don't want to talk…
to be the only talking head here. Erin, do you want to introduce the problem? And Alex, do you want to share your motivation?
Aaron Abbott 00:32:35 Yeah, sure.
And also, you'll have to forgive me, I haven't seen your comment yet, Alex, but…
You know, the problem is basically, like, when we introduced 2179, there's this section we added about.
Liudmila Molkova 00:32:48 Remote upload to external storage for really large prompts and responses.
Aaron Abbott 00:32:54 This is, you know, like, particularly for multimodal, this is a big problem. So, I think we originally… we decided to cut the scope from 2179 just because, of indecision.
So, this is pretty much just like a… I took… I took the commit that Libnilla had and copied it out into here.
So this was… this was actually… you were the original author, so if you have anything else to add, but, basically the… the idea is we add these
attributes which are the same as the ones that we have for directly storing the body, like directly storing in logs or events, and we add underscore ref at the end, and it would contain a URI to external storage in some kind of canonical format.
That's… that's pretty much the only change here, and then we add it to the events and the, and the spans.
Yep. Does anyone want to go?
Samuel Colvin (Pydantic) 00:33:50 I mean, Alex and I talked about it earlier, so, like, maybe some of the things I will say might cover what Alex has written below, but maybe it's different. Alex and I discussed the possibility of whether it should be one…
upload per span, or multiple… one ob… is there, like, I originally said one, and I wasn't thinking, but obviously it makes sense to have…
Have multiple, because…
basically, if it's an image, you want the image as a, like, file on its own. You don't want to have some horror JSON with Base64 stuff, so… basically, big plus one for…
when you have things like images, audio, video, even long text, that they are, like, in their pure format with the right mind type, not somehow…
Encoded in some other way that means that they don't work with all of the other infrastructure that…
object storage would have for, like, supporting images or whatever else.
And then the other point is…
I… and we talked about this long ago, when there was the previous submission from your colleague, Aaron, also at Google, on the other… on doing file upload.
I'm strongly of the opinion that if… so at this point, we're not having anything, we're just saying, if you do the upload.
you put the thing in ref, right? That's all it's… that's all it's kind of giving an opinion on, that makes sense. If we go one step further, I'm strongly in favor of the… of following a, like, signed… pre-signed URL,
flow for uploads. So, we say, here's the URL you request a URL from, you get back a URL, and you should post to that URL, and, like, not have more, like…
vendor-specific stuff, at least initially. But I think pre-signed URLs should work for all of the object storage solutions, and would be relatively easy to implement for, like, anyone else. But in principle, this sounds good.
I think we don't need to start getting into, like, the pre-signed URL flow to support these refs.
Aaron Abbott 00:35:49 Okay, cool. So, so should we focus on the first point?
Samuel Colvin (Pydantic) 00:35:53 Yep.
Aaron Abbott 00:35:54 Yeah.
Alex, did you want to add anything, or…
Alex Hall 00:35:58 Yeah, so I put… My reasons for a… A ref per message pod.
In the comments at the end.
Basically, yeah, like Simon was saying, I think it would be good if you can keep at least some text in line in the JSON,
And use reps for images and very long text.
And there's also, like, sort of implementation details, performance optimizations that become possible, where you only upload
A particular part once, as opposed to once inside every list of messages that it appears in.
Which is especially good for system messages at the beginning.
Samuel Colvin (Pydantic) 00:36:46 Right, so in particular, if you have a conversation where you go back and forth.
10 times, but you, the system message is sent each time to the LLM, you would… but it's 1MB long, you would like to upload that as one file, and then reference it in each
A subsequent time.
Aaron Abbott 00:37:04 Yeah. So, I have a couple questions. So, like, the first one is obviously most of the LLMs allow you to do URIs already, so…
like, the user already has to decide if they're gonna, you know, do an inline Base64 of an image, for example, or if they want to upload it to some storage or do a pre-signed URL, right?
So my question was kind of like, do you… propose
mutating the, like, the JSON structure to do the upload, and then overwriting in the same format? Or, like, is it important to know what was sent to the.
Alex Hall 00:37:34 Hello.
It wouldn't change anything about what's sent to the LLM, it would be purely from a telemetry perspective, including if you send base64 to the LLM,
you still only have to put a URL in the span attributes.
Samuel Colvin (Pydantic) 00:37:48 well, there's some overlap. I have just thought of an excellent feature to encourage people to use Logfire when they've got Pylantic AI, which is, oh, you want to reuse image… image… you want to use, like…
image URIs, but it just all work. Well, integrate with Logfire, and you can upload the image to us, and we'll use it for both observability and as the URI that we send through to the LLM. So thank you, Aaron, for that product idea. But also, it would be nice if there was support for basically
using the same URI in both cases, but that sounds like it should… from your… there's nothing in your spec that prohibits that, as long as it… unless it basically turns out that it doesn't correlate with the same part of the upload data.
Aaron Abbott 00:38:28 Yeah, yeah, I guess that's kind of what… so I have another PR, too, and I guess that's kind of what I was getting at, is that…
you could, in theory, do this processing if we leave… if we leave the, the spec pretty open and don't make any strong statements about this must be exactly what was sent to the LLM, transformed as minimally as possible.
Like, I can speak more to the…
my opinions on, like, the upload.
Alex Hall 00:38:53 Well, we already know it's quite far from what's sent to the editor.
Aaron Abbott 00:38:56 Yep.
Sorry, meaning, like, if… if somebody does a… puts a pre-signed URL with an expiration of, like, 5 minutes, and they send it to the LLM, we don't propose
that you should copy the image for observability purposes, just, like, store the URL directly kind of thing.
Alex Hall 00:39:15 That's an interesting question.
Well.
Samuel Colvin (Pydantic) 00:39:20 I mean, we already have that case because… or a similar case where…
For example, if you do image generation,
like, ChatGPT will give you back a temporary, like, 3-hour URL. We currently, if that's an image, we show that image in Logfire, but after 3 hours, it obviously just, like, renders as an error.
we may at some point have to have support, if you so wish, to, like, basically copy that image and persist it for longer, so… that same, like, do I want to persist that thing for longer? Question exists in other places.
Liudmila Molkova 00:39:55 I think the core question is…
what logic do we need in semantic conventions, right? We cannot,
Due to too many things. It's essentially what instrumentation does, And it's the common part.
Samuel Colvin (Pydantic) 00:40:13 Yep.
Liudmila Molkova 00:40:14 How much of it can we agree upon? And what is vendor-specific there?
So what we have today is kind of a reasonable middle ground. We don't tell how to do it, so every vendor does something on their own.
Samuel Colvin (Pydantic) 00:40:31 Is there…
Alex Hall 00:40:31 I do think it could… this could be very good in semantic conventions that, for example, Aaron implementing the Google Gen AI instrumentation.
Can make things follow a certain semantic convention, and maybe some protocols in…
some Gen AI utilities or the SDK or something, in a way that, you know, let's say our SDK, the LogFire SDK, when you configure it and it's authenticated in a way that already deals with, you know, span exporters, metric exporters, it also automatically deals with
uploading to external storage, the user doesn't have to do anything extra, and then they just say, log fire, instrument, Google Gen AI,
And it also hooks up the uploader, and…
follows the conventions that Aaron implemented, and then same thing for Langchain, and so on.
and… I think we might benefit if that… Convention was one part per… One ref per part.
Samuel Colvin (Pydantic) 00:41:29 Could… could we have a convention… whether it's…
whether it's GenAI-specific or not, presumably it would want to be GenAI-specific initially, that… Basically, any text field.
could…
you can either have undersc… add underscore ref at the end, and that now means a URL, or if it starts with some magic string, I mean, that sounds really dangerous, because someone could now put in that magic string, but, like, have some semantic convention for basically change the attribute path, and now that's a URL.
Because then we don't have to be… your PR doesn't need to be specific about, oh, it's instructions, whether it's parts or whether it's messages.
There's just a convention for how do you replace any attribute with… A URL.
Aaron Abbott 00:42:22 Yeah. I mean, to be a little tongue-in-cheek, I feel like OTEL sometimes leaves this open to the reader on purpose, so, like, we could underspecify it, and I think there's…
Kind of prior art for that.
Like, I think… If we, if we do underscore ref for everything.
I'm just a little concerned because,
I don't know, it's hard… it's hard for me to consume, and…
It would look a little different from… like, we'd have blob file data or whatever, and then we'd also have underscore ref for all of them, which can just introduce some confusion.
Samuel Colvin (Pydantic) 00:43:01 I agree, our database team are not going to be happy when I'm like, oh yeah, by the way, now you have to deal with everything and everything underscore ref that might be a URL.
Aaron Abbott 00:43:09 Yeah, and speaking of the database thing, like,
when I did kind of discuss this internally, there was…
you know, we had this discussion of the spectrum of doing big, big objects with fewer of them referenced in the telemetry versus having lots of small ones. I think
From an instrumentation perspective, it would be…
Like, roughly the same, except for caching would be much better if we do lots of small uploads and there's a lot of reusable parts.
But from the consumption standpoint, like.
If we want to reconstruct everything, and there's rest for each part, or just for large parts, for example, you could end up having to do a lot of fetches just to reconstruct the original data, so…
I'm curious what other people think. I think we've discussed this on Slack, too, but, I think from a consumption standpoint, for the telemetry, having fewer attachments might actually.
Alex Hall 00:44:02 That reminds me of another point that I think we discussed previously, but I forgot to put in the comments, or I forgot until now, really, which is that if…
let's say you're looking at a span in some UI,
It won't be able to render the conversation at all until it's downloaded.
the one giant blob of input messages, JSON.
If it's a single ref, whereas it could very quickly render at least a skeleton and possibly fill in
Parts as they come in.
So you don't have to, like, wait for your video attachment or whatever to download before you can see.
some text messages.
Samuel Colvin (Pydantic) 00:44:49 I mean, the chance that you have multiple enormous things in one… List of messages is… Unlike… relatively unlikely.
I mean, for the most part, like, this… You'll cover.
Alex Hall 00:45:02 It doesn't have to be multiple enormous things, it just has to be… there's one small thing that's worth loading quickly, and also…
Samuel Colvin (Pydantic) 00:45:09 but I'm.
Alex Hall 00:45:09 Like, it's perfect.
Samuel Colvin (Pydantic) 00:45:10 Aaron's point is, like, if I suddenly have 6 URLs to go and get, now that might be slower than getting one. But I'm saying that's very unlikely. For the most part, it's gonna be, like.
a small… like, either it's gonna be… mostly it's just gonna be instructions, where it's just one URL either way, or it's gonna be…
a handful of images, where… and realistically, the size of those images is gonna mean that, like.
The difference between downloading 3 images and downloading one blob of data that contains 3 images is gonna be, similar.
Sorry, Lymelly, I interrupted you.
Liudmila Molkova 00:45:44 No, it's all good.
So this discussion makes me think that we don't know how it should be done.
We didn't implement it, we don't have any, like, we have trade-offs everywhere.
downloading one thing and downloading six things, it's the…
It doesn't matter how big of the object you're downloading it, if it's within megabytes. It takes the same time to download 10 kilobytes and 1MB.
So the size doesn't matter. You would spend 10 times more resources downloading multiple pieces, or uploading multiple pieces. Creating one blob is more,
Expensive than, uploading 10 megabytes there. So…
It's a lot of backend specific optimizations.
And it's vendor-specific anyway.
Like, would you support, I don't know, Dropbox uploads, and Lockfire? Probably not. Well, I'm just imagining things.
So you have to communicate with your users on when to upload, what is the permission model, is it the SAS URL, or is it they give you the identity to access this data, or whatever. So this is all vendor-specific, how it should be done.
And to a certain extent, we can let vendors build things and be happy with them anyway.
And as you mentioned, Samuel, after its 6 months in production, it's worse than their dazing.
Samuel Colvin (Pydantic) 00:47:28 I, yeah, I agree 100% with that… that approach.
Aaron Abbott 00:47:35 Okay, so…
So, so, just to be clear, like, right now we have some kind of non-normative thing in the spec about uploading, which I think
Fits… still fits that bill, right?
The… The idea is to come with concrete proposals, based on…
Whatever we have right now, in a couple months, and revisit this.
Liudmila Molkova 00:47:59 would anybody actually implement this? So the reason I wanted to be… this to be in the spec is that instrumentations will have hooks.
How these hooks are implemented, we don't know yet.
Would anybody actually be interested in implementing some hooks and implementing the upload?
Samuel Colvin (Pydantic) 00:48:19 We're definitely interested in doing it, we just need to find the resources. But we've wanted to do it for some time. I think we've been slightly waiting on this discussion, but I think I agree with your point, Ludmila, partly because you're copying, you know, you're quoting my point, so it's not surprising you're… I agree with you.
I mean, yeah, we will… try, but I can't give a time frame.
Aaron Abbott 00:48:46 Yeah, I was gonna say, so there's… there's a prototype of the instrumentation, like a proof of concept attached here. It's… it's quite large, because it has both of the two PRs here in that… in the same prototype, as well as, like, an agent to showcase it, but I… I have played around with it a bit.
I will say for, like, plugging into eval tools, it's also really nice to have everything together.
So if you have, like, if you want to do continuous evals, you don't have to go and do a deep fetch, you can kind of just point it at the attachment.
But yeah, I can… I can maybe… I think we've taken a lot of time for this one, but maybe I can show…
The demo next week, or something like that.
Samuel Colvin (Pydantic) 00:49:26 Wonderful.
Liudmila Molkova 00:49:28 Yeah.
Awesome.
So… Then, moving back to the agenda, let me write down some notes.
Okay, we have, like, 10 minutes left. I think we have time for just one topic, this one. Rithema, do you want to go ahead?
Ridhima Satam 00:50:20 Yes, so this is the PR for the LLM relocation support in the line chain, and Ricardo and Aaron has already taken a look at it. Thanks, Aaron, I appreciate that.
There were some concerns brought up in the couple of, like, meetings ago, like, if you see the comments section, there are a few comments there.
mainly was, the first one is, like, we were earlier, just supporting OpenAI, invocation. I've added the AWS Bedrock, so if you just go below, yeah, a couple of lines below, so…
explain the value of innovation in line chain versus client instrumentation is… there is no AWS Bedrock instrumentation in place right now in Vanilla Hotel, so…
this could bring in, that, AWS Bedrock, telemetry with using… when we… when we are using the line chain instrumentation. And the second is, I think, that's the… basically, you add the test for all that, the second point. But the third point is,
there was a concern about duplicate telemetry when you have langchain and the underlying telemetry, and we wanted to see how OpenLelementary is using, since, doing it since we are taking lanchain instrumentation from there, and what I see is, like, they're using this flag of suppressing
they're turning it on in the line chain, and then you use it in the underlying library to see if it's already there, then you don't, basically produce any telemetry in the downstream instrumentation. So…
So the point is, we need to… so the fourth point is, like, we want to see how long-term strategy would be, like, we have to add this certain flag and semantic convention. That is the proposal, if everyone is okay with that, and then handle it the same way.
Liudmila Molkova 00:52:20 So, you're suggesting, too, that the suppression flag has in semantic conventions?
Ridhima Satam 00:52:25 At least I didn't see it, like, yeah.
Liudmila Molkova 00:52:29 Yeah, the way it's solved, I think the most generic we come to solving it in OpenTelemetry is Java, where effectively we're saying, okay, I'm reporting column span.
or whatever span, full bar span, let's put it on the context, and then everybody who also wants to report the span before starting the instrumentation checks. Oh, did anybody already… is anybody already reporting the full bar span?
And backs off otherwise. So, we don't put this into semantic conventions, but instrumentations in languages have the means to suppress. There is no generic way in Python.
So I would be against putting it in the semantic conventions, but we can find a solution without it, and it's actually a great thing to do.
Sorry, Erin, go ahead.
Aaron Abbott 00:53:23 Oh yeah, no problem.
I was just gonna say, one thing I don't love about this is it encourages the thing that's seen first, which is the least specific, to win.
I don't… I don't think there's any way around that, though, unless you deferred the sampling, which we can't do. The sampling has to happen eagerly.
Is there… Lumila, do you know if there's anything…
regarding that in Java, like, I know we can do enrichment further down, but the parenting would be… confusing.
Liudmila Molkova 00:53:53 No, no way to, work it around. You, you don't know, like, on the…
higher level, you don't know if lower level exists. You cannot rely on this, so it's impossible to not create a spend there.
Aaron Abbott 00:54:09 Yep.
Yeah, so I think, I mean, I'm okay with this.
Like, for this PR, and then we can always iterate.
I'm wondering, did you also check with Nier on, like.
How important it is to keep compatibility with
You know, the current… the current code they have for the link chain instrumentation, like.
Is this a key thing that they need for, kind of, the migration to the same package name?
Ridhima Satam 00:54:41 I didn't get your question correctly, like, do I have to ask them about the specific key?
Aaron Abbott 00:54:48 No, the question was more like.
We're planning to do… so we're publishing to the same package name.
Right, and this one will be link… open telemetry Instrumentation, link chain, and then the version will be, you know, some 2.x, right?
Ridhima Satam 00:55:03 Yeah.
Aaron Abbott 00:55:04 The question was, like, you know, Nir's saying that we're happy to move to the hotel semantic conventions in the future as part of this,
And, you know, maybe just… maybe we could just get a review from him on this, that's all.
Ridhima Satam 00:55:19 I see. For this PR, you are saying, for the element of vacation? In general, the whole PR? Okay.
Aaron Abbott 00:55:25 Yeah, yeah.
Ridhima Satam 00:55:26 Yeah, we have confirmed before with Nir about moving this in the hotel, so he has agreed upon all that version thing and using the same name and all that.
Aaron Abbott 00:55:35 But, yeah, we can get another…
Ridhima Satam 00:55:37 Look from that.
But, yeah, so with the duplicate telemetry, you're saying that we can keep this under discussion, and for this PR, we don't… this won't be a blocker, right? That's what you're saying?
Aaron Abbott 00:55:49 No, I was saying, like, I would be in favor of implementing a similar mechanism for this PR.
Ridhima Satam 00:55:56 Okay, so you want me to, okay, so we can have this kind of flag in the context API enabled and then check, right?
Aaron Abbott 00:56:07 Yes, we also have, like, this Gen AI utils package,
which we haven't released yet. This seems… because it's not just OpenAI, it seems like a nice place for this to live. So, like, for HTTP, we have something similar.
Where you can suppress instrumentation, and it's all… it's all in a util, so that…
different HTTP libraries don't have to re-implement it.
So I would suggest, you know, putting it in there.
Ridhima Satam 00:56:34 Okay.
Aaron Abbott 00:56:34 Yeah. If that's too much, we could also just do, like.
Because my main concern was just, if we tell people to not install this one, like, hey, this is incompatible with using the OpenAI instrumentation, it will double rate. Please remove it.
It just, it feels unfortunate because then they have to choose between the two.
Ridhima Satam 00:56:54 Okay, got it.
Liudmila Molkova 00:56:57 One thing I think we should do, as well, give me a sec.
One thing we should do, eventually there will be a way to control
Traces by instrumentation scope name.
And I think… ALLM instrument… sorry.
Blank chain instrumentation.
should use different instrumentation scope names for LLM calls, and for the future, higher level.
calls.
saw that… Once the… it's possible.
To enable or disable certain scopes.
Users can distinguish these two.
I'll leave a comment on the PR, and I might suggest something. It's probably unprecedented, we usually put library name into the instrumentation scope name.
So… I would love… Folks to comment on this.
Yeah, here, so we put the name, the module name, right?
Here, we would need to put… to have different tracers.
for… Llm, and for the framework.
Aaron Abbott 00:58:44 What about just, like, a scope attribute, too?
Liudmila Molkova 00:58:51 It could be a scope attribute.
Okay, let's… let me do the following.
I'll throw a proposal into semantic conventions. I'll bring it up on the Semantic Convention's call on Monday.
I'll collect some feedback.
And we can come back to this discussion. It's not that…
it would be blocking for this PR anyway.
tsloughter 00:59:26 Are you gonna be able to disable tracers by scope attributes?
Liudmila Molkova 00:59:33 The tracer enabled could enable disabled by something, right?
I would imagine that the scopening would be the first candidate, but that doesn't mean it couldn't be done by the attribute.
Or do you… do you know this part better, Tristan?
tsloughter 00:59:51 No, no, I was curious.
Aaron Abbott 00:59:55 I'm checking the spec right now.
Liudmila Molkova 00:59:59 I don't think it specifies, but the name… Would be the trivial one.
Aaron Abbott 01:00:15 So there's, like, tracer config here, I'll just share it.
Yeah, it seems to be that vague thing that I was talking about before.
Liudmila Molkova 01:00:28 So I think the configuration, currently, it's in the development.
But it prioritizes the… Name, at least the example shows the name.
Okay, anyway, it would be a great discussion regardless, and I'll bring it up, and we are…
At time. So I think, Radhima, the question is to take another look at the RPR, right, and
There are some action items.
Ridhima Satam 01:01:03 Yes, I can… I can add it in the channel as well, like, what's remaining on this, yeah.
Liudmila Molkova 01:01:13 Okay, wonderful.
Ben, thank you all.
Great discussion, as always, and… Looking forward to seeing you on GitHub!
Shuwen Pan 01:01:30 Awesome. Thank you. Later, everyone. Thank you. Bye.

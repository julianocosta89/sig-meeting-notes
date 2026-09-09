SIG: GenAI SIG
Date: 2026-09-08
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

**Liudmila Molkova** 02:06 Hi! Hi, everybody.
**Trask Stalnaker (Microsoft Corporation)** 02:10 Hey, hey.
You wanna… you wanna break from running meetings, Liudmila?
**Liudmila Molkova** 02:16 I wouldn't mind, I can also drive if you, if you don't want to, or if anybody else wants to, we'll be… probably both happy to give them the chance.
Okay, none.
And thank you, Trask, you've been faster than me.
**Trask Stalnaker (Microsoft Corporation)** 02:41 Driven 2 meetings in a row this morning already.
**Liudmila Molkova** 02:44 Just one. You dropped the first one.
**Trask Stalnaker (Microsoft Corporation)** 02:47 Oh, did I? Okay.
**Liudmila Molkova** 02:48 I did, yeah.
**Trask Stalnaker (Microsoft Corporation)** 02:49 Good, good.
Suspecca's an intense one, so… Should count as double.
**Liudmila Molkova** 02:56 Okay, I appreciate it.
**Trask Stalnaker (Microsoft Corporation)** 03:12 Alright, go ahead and… Throw anything you want onto the agenda today, based on our earlier call.
And so far here, it looks like we may have some vacation time from the U.S. around Labor Day.
**Victor  Lu** 03:35 It looks like none of the BSI people who said, will come has… isn't here yet, so most likely not.
**Trask Stalnaker (Microsoft Corporation)** 03:44 Okay.
No problem.
Whenever they're able to join.
Yeah, let's start with this. So… we are… starting, the stabilization Meetings series.
Tomorrow.
So it is on the… Open telemetry Calendar.
So… noon Pacific time?
So these are half-hour meetings, Monday, Wednesday, Friday.
We're going to only… Consider things in scope for this initial stability.
Drive, which are inference and… and agent, spans and metrics and events.
We will… I mean, obviously those things could… Be a lot of extra things.
As well. So we will probably, you know, try to draw a fairly, tight boundary around them so that we have a chance to… Put out a release candidate in a couple of months.
Having gone through a couple of these efforts before, it's… a decent amount of work, and a lot of, kind of, just, checking in, and we want to be making continual F… Progress, so that's why we want to have, kind of, the three short meetings a week to make sure we're kind of staying on Topic, and making progress on all the little things.
I will post… Trask… To post schedule in… Slack.
Yeah, so, we did, get kind of an initial group of folks who, volunteered for this, and we picked kind of a time, but certainly it's there, it's open to everyone who wants to join and participate.
Any questions about the stabilization effort?
**Liudmila Molkova** 06:27 Super excited! Let's do it.
**Trask Stalnaker (Microsoft Corporation)** 06:32 And we intentionally, separated that from this meeting, because there are still, you know, a lot of… Good discussions and good topics.
About the, kind of, the future and all the other… there's so many other things going on in, in the GenAI, observability, and so we didn't want to… We want to encourage that, those conversations to keep happening, and sort of the figuring out slowly the next wave of things that, you know, we might have a stabilization effort six months after the first stabilization for, like, a next wave of things, say, if things sort of solidify.
I would say that I would expect, occasionally we'll bring, sort of, a status update to this meeting, of the stabilization work, just for, sort of, broader, Feedback.
Alright, next… Liudmila,
**Liudmila Molkova** 07:59 Yeah, this is a technical for reviews. It came up in the Python.
instrumentations, and turns out we don't make Agent Name sampling relevant on the tool span. Oh, and plan spans.
**Trask Stalnaker (Microsoft Corporation)** 08:15 Yeah… Thank you.
Seems like a clear thing you would want to sample on.
Alright. Habiba?
Did I… do I see… oh yes, I see you on the call.
**Habiba Mohamed** 08:39 Yep, I'm on the call. Can you all hear me?
**Trask Stalnaker (Microsoft Corporation)** 08:42 Yeah.
**Habiba Mohamed** 08:43 Yep, awesome. So just a quick update on the, the AI… the GenAI Security Safe, safety guardrails PR.
I've ported over all of the changes from the original PR that were requested. Ludmila, I think you gave a review yesterday, thanks on that. I'll address that later today and rework it.
Most of the feedback is resolved. I probably won't keep adding it to the agenda, but any further review is welcome, but yeah.
**Liudmila Molkova** 09:14 Yeah, I'm curious, how do you feel about, like, essentially what I'm suggesting is to postpone the internal guardrail?
Because… we just don't… There's just one… SDK, which could have internal guardrail, and the rest of them will do it through generic hooks, and we have no idea about whether it's a guardrail or the logging I don't know, extension point.
**Habiba Mohamed** 09:38 Yeah, I agree, I think that makes sense. There are only… the real client scenarios, I think there are only at least two providers, so…
**Liudmila Molkova** 09:46 I think that… Well, my research found 3, or…
**Habiba Mohamed** 09:51 to 3? Okay.
Yeah, I'll dig into it, but I agree.
**Liudmila Molkova** 09:57 Yeah, and the one… one thing I thought is… we should still consider is OpenAI Agent does provide the explicit guardrail API, the local one, and we could instrument it. I'm thinking maybe the event should be the thing we meet there. The event would be coming across.
the… Remote… Guard rails and, local ones.
This, this… I think we could make this work.
If it's okay with you.
**Habiba Mohamed** 10:35 Okay, and did you say OpenAIPI Edge, or OpenAI Edge?
**Liudmila Molkova** 10:40 up in AI edges.
**Habiba Mohamed** 10:41 Edge, okay, agents, okay, got it, okay, sounds good.
**Liudmila Molkova** 10:44 Yeah, it should be somewhere in the comments.
**Habiba Mohamed** 10:47 In the comments, okay. Thank you.
**Liudmila Molkova** 10:52 Yeah, thanks for working on this.
**Habiba Mohamed** 10:59 Yep, that's it for me. Thank you all.
**Trask Stalnaker (Microsoft Corporation)** 11:02 Cool then, moving on, Ankit.
I'm good.
Can you hear us?
I see you there.
**Ankit Singhal** 11:26 Sorry, I lost my Zoom window. No, but so, Thanks for the comments, and Liudmila. I really appreciate it. So, I've addressed, most of the, recent comments. There are a few, like, old comments that are still outstanding. I'm working on them. They are, like.
4 or 5 of them, but the… Bam.
I would say.
doesn't change the course of the PR. So, more around, like, content language and other things, so I'm working on that. Would appreciate, If you could review it again, and share any feedback.
And, looks like it's coming along, and moving in a direction where… Probably, I'm hoping soon we can get that much.
**Liudmila Molkova** 12:19 Yeah, I also think it's moving in a good direction, and I don't see any big issues.
I'll take a look for sure.
**Ankit Singhal** 12:28 Oh, no, thank you, I appreciate that, yeah.
**Liudmila Molkova** 12:30 Thank you.
**Ankit Singhal** 12:31 I don't know if, Aaron is here. Hey, Aaron, I think, I… Regarding the session events, I think, the PR, I think, very clearly defines, and I've updated the scenario as well, which shows how session events are limited.
And they're linked to the spend, like, to the actual session, for the event socket connection, so… I know you had that feedback around that, so, please do review those.
**Aaron Abbott (Google LLC)** 12:58 Okay.
Well, thanks. Thanks, Ankit.
**Ankit Singhal** 13:01 Thank you.
**Trask Stalnaker (Microsoft Corporation)** 13:06 All right, we're moving quickly. Ludmila.
**Liudmila Molkova** 13:12 Yeah, sorry, Dylan, for putting you on the spot. I wanted to chat about this one, So we talked about suppression a couple of weeks ago, I think, or maybe last week.
And it's awesome, but I'm kind of worried about event suppression or event enrichment.
And maybe we can talk through, I don't remember where we are at this point, but I think you have a prototype that I haven't seen. Like, maybe you can share your thoughts on the event in Richmond.
**Dylan Russell** 13:44 Err.
I think it might be hard to do in general.
Because usually events are, like, created and then immediately written.
But… I think for the inference span.
It's usually, like, created on the request path.
And I think it could be put into the context, like, on the request path.
And then other people can, like, modify it.
And… Not write their own events, and then… It could be written, like, on the response path.
So, yes, I think for the inference event, it could work.
But I'm not sure it's, like, generalizable to, like, other events.
**Liudmila Molkova** 14:40 Do we care enough? I mean, we could solve it technically. We can put the dictionary on the context, and then reach it, and then report it, and then the event out. But, like, it's all…
**Dylan Russell** 14:53 Yeah.
**Liudmila Molkova** 14:54 It feels like we are hacking around, and do we have a good reason to hack like this?
**Dylan Russell** 15:01 Yeah, maybe not.
**Trask Stalnaker (Microsoft Corporation)** 15:04 Ludmila, you mean just as opposed to straight suppressing?
The child in, inference events.
**Liudmila Molkova** 15:14 Yeah.
**Dylan Russell** 15:21 I mean, it's… So I guess for spans, the reason is we do have, like, a genuine reason to want to put it on the context, other than just, like, suppression.
Because we want to, like, modify it.
Like, there's some downstream.
**Trask Stalnaker (Microsoft Corporation)** 15:40 What are the downstream attributes that, That we want to enrich.
use for enrichment.
**Dylan Russell** 15:49 I think for spans, it was, like, server address, and… server port.
like, I… I'm not… I think, Ludmila, you know better than me for the… For the spans.
**Liudmila Molkova** 16:05 Yeah, I think these are the two that comes up the most, but maybe there are some other specific details that are on the underlying library would know, and outer.
wouldn't.
Then we would stamp them on spans, and not events.
And it seems… like… Not the end of the world that some details are only available in spans and not events.
**Dylan Russell** 16:39 Yeah.
Is there a reason not to do it on events?
And spans, just, like, sim… Keep it, like, simpler.
We could start with spans.
**Liudmila Molkova** 16:54 It just smells to me that we… That we would put And we would create an attribute for event when spend starts, and then we would enrich them.
Events only, and then we would… emit event based on the enriched attributes.
maybe… It could be fine if we… Just put span attributes there, like, just attributes, and then reuse them across both signals.
Where, if we treated the… the event… as something where… a report in the SDK, like, the span end event.
And then we would get it for free.
**Trask Stalnaker (Microsoft Corporation)** 17:53 So, I was just remembering, there is an advantage to… Instead of enriching the span in the nested… Instrumentation to doing what you're talking about of, storing the attributes.
and… then… Handling that in, basically, on end, and it doesn't really matter for spans, but it does matter for metrics, like, if you want to get that attribute onto metrics.
**Liudmila Molkova** 18:30 Oh, and for inference, we kind of want attributes for metrics, the server address, server part.
**Dylan Russell** 18:39 Hmm.
**Trask Stalnaker (Microsoft Corporation)** 18:40 So maybe a more general structure than… That would cover events. Wouldn't… it wouldn't be, like, a special casing for events as much.
**Liudmila Molkova** 18:51 Right.
Yeah, and it would… could, to a certain extent, resolve the… overwrite problem, like, you… you know what's already there, and you can decide whether you want to overwrite in the inner layer, or you decide to… Believe it as is.
And then we would just stamp.
attributes.
it's… it's still a little bit ugly. In Python.
it's easier, but in Java, I guess it would mean a lot of attributes building.
So you would put Attribute Builder, but it's not, there is no getting?
It's still, like, cra- like, sat on me.
**Trask Stalnaker (Microsoft Corporation)** 19:42 I… I think the attributes in Java you can get… you just can't… not off of a span, but, like, there's a separate attributes… Builder concept.
That you could use independently.
**Liudmila Molkova** 20:02 Right, like, what I'm saying, that attribute builder, I think it's just the setters, or getters, so you don't know what's already there, and maybe it's okay.
**Trask Stalnaker (Microsoft Corporation)** 20:09 Oh, yeah, you have to build it and then get… yeah. Yeah. Yeah, we have some… I won't go into the horrible workarounds that we have in instrumentation around that.
We have our own implementation of Attributes Builder.
**Liudmila Molkova** 20:25 Okay. Okay, so then we, like, if we don't consider it's a problem, then, okay, the attributes is what we would… Put down the context.
**Dylan Russell** 20:39 So, the upstream… Instrumentation would copy the attributes.
Into the context.
And then… The downstream one would potentially add… read from that and add to it if it wants.
Is that the idea?
**Trask Stalnaker (Microsoft Corporation)** 21:02 Why, why that versus, putting… An empty thing in the… Parent, and letting the child just But… Add on what it wants.
And then the parent deciding what to do.
**Liudmila Molkova** 21:24 Oh, like, an extra. You can add an extra, you cannot.
Even pretend that you can change.
There.
the previous one.
Yeah.
**Trask Stalnaker (Microsoft Corporation)** 21:43 I don't have a reason to prefer… I haven't thought through this, so, just… May or may not make sense.
**Dylan Russell** 21:57 think… It is useful to be able, for the downstream… Instrumentation to be able to read the attributes.
There we go.
Sorry, I'm not sure exactly what you're proposing, but I think that's one issue with just putting the span and event on there, is it's maybe hard in some languages to, like, read the attributes.
Off the span.
And see what's, like, been set and not set.
**Trask Stalnaker (Microsoft Corporation)** 22:24 Do we have a use case where we… the child cares what's in the parent already?
**Dylan Russell** 22:32 Ugh, they're… Is someone asking about that from ADK?
But that might be more… too complicated, but… They do want to… For the downstream to, like, see what's… been set.
And if, like, an attribute hasn't been set, then… like… Set it.
Because they maybe don't want to do, like, the GCS upload on the ADK side.
They wanna, like, leave that.
And the associated tributes, like, off the spam.
**Liudmila Molkova** 23:16 So then they can… Read what inner… provides.
And afterwards, react to this.
They can decide on the… out earlier whether they want to replace Or… Leave it alone, and don't do their own applause.
**Dylan Russell** 23:43 Yeah… right. I think it's… Yeah, both the inner and the outer read, and decide.
like… So, yeah, I think it's both layers.
Having to read it and make decisions based on it.
**Liudmila Molkova** 24:06 Yeah.
I'm thinking… Maybe.
Where… and I think you already have predictives, but I'd rather do it in Python, and then do the conventions part, because what we put in the conventions is essentially However you implement it, this is the behavior we want to see, and it probably means that we do it in an agnostic way. Any span could be like this.
Right, not just the inference.
And then pick your set of context keys. We don't care, it's… it's not string literals anyway.
make them public in hotels.
Done.
When you create a span.
Record, like, when you start an operation, record something in the context, like a set of attributes.
And then… Inner Instrumentations add to this list?
Outer instrumentations decide what to do.
And if it's, like, a… if it's metrics, they can get things like the server address.
If it's span and logs, they can take everything.
**Dylan Russell** 25:30 Okay, that makes sense.
I will work on another prototype.
Yeah.
Sounds good.
**Liudmila Molkova** 25:42 Thanks a lot.
It's… everybody will be jealous about this feature.
**Dylan Russell** 25:47 Okay.
**Aaron Abbott (Google LLC)** 25:50 Just a quick question, like, I see this is a SEMCOM VR?
And then I think maybe 2 weeks ago or a week ago, we discussed and said this park could be kind of, like.
Non-normative, or… at least we discussed making it more vague and then just implementing it in Python.
Do we still… Want to go the approach of having something in the spec, or should we kind of let it grow organically?
**Liudmila Molkova** 26:19 I, I'm, I'm thinking… Where should dirt and tighten?
And… once we're happy with it, we'll put it in semantic conventions.
I… It's just, I don't feel like semantic conventions should come first here before the implementation, because it's so kind of tricky.
To find the right approach.
**Aaron Abbott (Google LLC)** 26:44 Yep.
No, that sounds good to me. I agree.
**Trask Stalnaker (Microsoft Corporation)** 26:56 Alright.
People will be jealous.
Ludmila, moving docs around.
**Liudmila Molkova** 27:09 Yeah, so I'm… I cannot really find anything in our docs. If we open, let's say, the… GenAI spans. There is so much, and if you look for a specific attribute, you kind of need to scroll a lot before you find Where you are, and maybe it's the… the… Just the general problem with how we… render things in semantic conventions, but unless there are some good proposals on how to render differently, I'm suggesting to maybe focus it on operations rather than signals.
And, like, for example, we would… I didn't put enough thoughts into this layout, I created it as I was feeling this.
the… the agenda item. But I'm thinking, let's say, for inference, I kind of want to see a page where there is both the… well, or all of it, the spend definition, the metric definition, and the exception event, or whatever other events we have, the operation details.
And, this… Alliance was, like, the principles we discussed before, that for every span definition, we probably want to make… want to have the corresponding metric.
It would make things clear, it would help us not make this mistake again, where we define the metric, the client operation duration, that is kind of everything.
And it will be easier to use, and it will also Point people to, like, the fact that conventions are not just a span, or just… just a metric, but more of an operation-focused thing, at least here.
And GenAI?
So… I am curious what people think about this, and I kind of think it… it's… Somewhat part of the stabilization effort to make this… Operation boundaries more clear, and clean them up, and also, like, put everything about one operation into one file, or at least one folder.
**Aaron Abbott (Google LLC)** 29:32 Yeah, I like this. I think, it would make it easier for developing the conventions, too, and… just generally more obvious. And I guess this doesn't prevent us also from generating, like, a single Page with a list of all the metrics, so we can kind of have both, right?
**Liudmila Molkova** 29:51 Yeah.
We can, there is a… Okay, maybe I'll… I'll share the prototype at some point, maybe next time, so we can… there is a thing… We can render… like, we have attribute registry. We can also render a metric registry or a span registry.
And… We could even consider Just having the… these pages around operations to contain some things that are not in YAML, and just link into the registry.
Instead of, like, having everything laid out and in the… File…
**Trask Stalnaker (Microsoft Corporation)** 30:47 I was looking for your issue about splitting.
**Liudmila Molkova** 30:51 Yeah, that's, that's 249.
2 below.
**Trask Stalnaker (Microsoft Corporation)** 30:56 Thanks.
So we would have… Essentially, different pages for each one of these span types.
**Liudmila Molkova** 31:10 Yes.
And they're probably… about different operations, and it would contain spend type and probably multiple metrics, because for inference, we have the duration and token usage.
So it's essentially by namespace.
two layers.
of namespace, GenAI inference.
**Trask Stalnaker (Microsoft Corporation)** 31:38 I like it.
These pages are… very long, and you go here and you search for stuff, and it shows up so many times across… like, once you're in, like, somewhere here.
you don't know where you are, like, you have to scroll up, and you're like, oh, what does this apply to? This is, this is inference, okay.
But now, all of this, you know, I'm down here, and they're like, okay, that… and that's a pretty small little heading there anyway, it's easy to… flip over, so…
**Liudmila Molkova** 32:15 Yeah.
Okay, so Dan, maybe as we, clean up metrics.
Metric names, we'll do it.
a long… Was this moving around toy?
We can start moving things around, and… than we're a name metrics.
I guess the next step for me would be to prepare a prototype, and we can, like, agree on the details.
**Trask Stalnaker (Microsoft Corporation)** 33:00 Sounds good.
**Liudmila Molkova** 33:04 Yay!
Thank you.
That is it.
**Trask Stalnaker (Microsoft Corporation)** 33:10 Moving on, Nikhil. Hey.
**Nikhil Chitlur Navakiran (Microsoft Corporation)** 33:14 Hey, hey folks, Thanks for, adding the reviews on the PR. So, I finally got a chance to jump back on this. So, I just wanted to check, If there's any open questions, if not, I was just… I wanted to take some time and explain, like, some of the changes that I… that I did.
**Trask Stalnaker (Microsoft Corporation)** 33:41 Yeah, that would be great. Do you want to share?
**Nikhil Chitlur Navakiran (Microsoft Corporation)** 33:44 Sure. Let me… Okay, let me see… Shit.
K… Alright, can you see my screen?
**Trask Stalnaker (Microsoft Corporation)** 34:12 Yeah.
**Nikhil Chitlur Navakiran (Microsoft Corporation)** 34:13 Okay.
Nice. Alright, so, on the unified open telemetry model for tracking agent-to-agent interactions, so, Primarily, what we see is there are, two options that, the industry is, is using, essentially. So the primary option is the, execute tool-based, transfer.
And with Google ADK, I see that they also have an A2A protocol where they are, making a direct remote agent call. So that, would kind of align with the Invoke Agent client span.
So, essentially, like, execute tool span and the invocation, client span are the two modes that I see of, capturing, A2A, interactions.
So, what this PR does is try and, like, you know, provide some guidance and standardize, around it, right? So, So, specifically, addressing, I think, Ludmila's comments, if I can find them.
Yeah, so I… I, like the suggestions of using the transfer mode attributes and the, transfer agent or transfer target attributes. So, on the… on the execute tool span, I have introduced, these, attributes.
And that's… and that seems to have good, support in the scenarios, as well.
So that is one thing that I'm, calling out. And, Let me go into the code… So… Let me see… yeah, this might be a little helpful, so… You fail.
Okay, so, I've added a non-normative example so that we can, you know, quickly take a look. So.
This, the recommendation is, is, for tool-based transfers, so we will use, like, the, the agent star attribute. Currently, it's only agent name that identifies the source agent, sticking with the existing, execute tool, attribute.
And then we'll have the transfer target, star attributes. So, this refers to any, This refers to the target, so I believe in this case, it can be agent, or human user, or, some other application, right? So, we, we are keeping it generic, and we'll have the transfer star attributes.
And there is, here, one of the transfer star attributes is a type.
So there, we're gonna have, like, some enums which say… enum strings which say agent.
you know, application or user, right? So that specifies, that is how we can say, okay, if it's a type agent, then this is actually an agent-to-agent, tool transfer, agent-to-agent.
Or transfer from… between agents using a tool.
Right? So, that's something, thanks, Ludmila, for those suggestions, and I've incorporated it in the PR.
Any questions on that?
**Liudmila Molkova** 38:21 Yeah, just maybe one, thanks for incorporating. I… I wanted to mention that for the transfer mode.
So my intention here was that, okay, there are these different words, SDKs use, handoff, delegation, transfer, and they don't… as a non-native speaker, I don't really understand what they imply.
Like, and I wanted to… us to express What people… it's clear to understand whether, like, the… in… It's a sub-agent that Just does the work on behalf of the main agent, and then main agent replies.
**Nikhil Chitlur Navakiran (Microsoft Corporation)** 39:09 That's good.
Right.
**Liudmila Molkova** 39:13 Turn the color or the pass control, and although I wanted to mention that These are two words that I suggested, or maybe even my AI did, and I don't know if everybody shares, understands what they mean, and maybe we need… we can find better words for them.
But that's the intention, to, like, express what's important rather than some SDK-specific concept, like, handoff.
**Nikhil Chitlur Navakiran (Microsoft Corporation)** 39:42 Makes sense. Yeah, I agree. So, I did take a look at that, and then, yeah, I, so the… Pass control and, you know, the, return control.
let me see, what's that exact word? Yeah, so the pass control, that made sense. So, I put that in the PR, so that was, like.
Yeah, it was explicit enough, is what I felt as well, but yeah, open to any comments on that, on those enum values.
Awesome.
So the second thing is, like, the, agent invocation through API. So, this is essentially, like, I'm calling out that, hey, we should continue to use, the invoke agent, client span.
And so, essentially, it would, and there is no, like, changes to the client span.
I'm not suggesting any changes to the client's plan, it is more that, in this example, I'm calling out, hey, we should use the client span, and this will be a way of doing agent-to-agent tracing across, like, remote boundaries, right? So, in this, I'm highlighting that on the caller process, you will have two spans.
One is an invoke agent source span, which is an, which will be an internal span, identifying the source agent, and then there'll be, like, an, the invoke agent client span itself, the agent ID, And the agent name refers to the target agent, in the stage. So there is… so there is no changes, as far as that goes. And then, with that, the… the, like.
you should also expect, or you can also expect an invoke agent… invoke agent internal span on the target agent as well. So there is a situation where you can get both a client and an internal span for the target agent.
I think there were some concerns around, like, like, double counting of Invoke agents, because if you have both the client and the internal spans for the target agent, so I just wanted to have a discussion on that, and… Because my explanation was, hey, I think this is pretty standard, so I have seen situations where both… there is, like, both a… what do you say, there's an MCP server span and a client span, so yeah, you… like, the… the collect… the downstream collectors will have to, like.
you know, distinguish them and, you know, to count unique invokes. But I just wanted to, you know, for the group here to share your thoughts on that.
**Trask Stalnaker (Microsoft Corporation)** 42:47 This whole section, at the bottom that you have highlighted is… are there any changes to the existing, semantic conventions?
in this PR, like, I was thinking this is what's already there.
**Nikhil Chitlur Navakiran (Microsoft Corporation)** 43:05 Right, you're right. So there is no changes. It is exactly what is there. So this, It's just… this is just a non-normative example calling out on, how to capture this, or… What we would expect.
Right? And then there is a… So there is a Google ADK's remote A2A agent, feature, so that's what I use to write the scenario.
From.
**Liudmila Molkova** 43:41 So they, they don't model it, through the tool calls, it's like the client invoke Agent directly?
**Nikhil Chitlur Navakiran (Microsoft Corporation)** 43:50 Yes, that's my understanding.
**Trask Stalnaker (Microsoft Corporation)** 43:52 Oh, I thought this whole section at the bottom was for the existing remote Agent calls that we already have today, not… which is… where I guess I was a little confused versus the discussion above, which is about modeling things for calling things locally.
**Nikhil Chitlur Navakiran (Microsoft Corporation)** 44:16 Got it. Let… maybe let me… so this is, So, there's, like… the proposal is to standardize around modeling it in two ways. One, using executeTool, and the other is Invoke Agent. So… There are, like, there might be some scenarios where, you know, like, Agentic platforms might be using different spans to, to indicate this A2A interaction, right? So… That's… this example is trying to say that, hey, let's standardize around these two spans, or reuse these two spans to capture that. So the first example is mostly around, just using, tool-based transfers, so execute tool spans only.
And then what… and these are the new properties that would be required to, you know, capture the relevant information.
And the second section, the agent invocation, so I'm specifically calling out is if you're doing from Agent A to Agent B, if there is a direct API call that is, like, invoking agent B, right? So, at that point, let's use the existing invoke agent client span to capture the process.
**Trask Stalnaker (Microsoft Corporation)** 45:45 So, yeah, I… that's where I think it… I got confused, because client spans… I think are only supposed to be used for communicating to a remote.
**Nikhil Chitlur Navakiran (Microsoft Corporation)** 46:04 Right.
**Trask Stalnaker (Microsoft Corporation)** 46:05 something.
And in this case, you're saying that If it's… like, I get that through a protocol, right, to some remote service, but what if it's just local orchestration?
Agent invocation…
**Nikhil Chitlur Navakiran (Microsoft Corporation)** 46:21 Right, so I didn't find… so this was one of the cases that I had, like, captured earlier, but I didn't find a scenario example that had a… That had a non-invo… er… Yeah, I couldn't find a scenario with… on the… which had, like, such, which had an invoke agent, which is a non-client, and, local to the agent process.
**Liudmila Molkova** 46:51 That's kind of intentional, right? So here… This is the… the source agent… Calls… uses the remote agent as a sub-agent, and it transfers to a remote agent.
And what it does.
**Trask Stalnaker (Microsoft Corporation)** 47:16 Essentially. Yeah, as long as we're… this section is only talking about remote Agents… That makes sense.
**Nikhil Chitlur Navakiran (Microsoft Corporation)** 47:25 history.
**Trask Stalnaker (Microsoft Corporation)** 47:26 Okay, maybe I can…
**Nikhil Chitlur Navakiran (Microsoft Corporation)** 47:28 If there's.
**Trask Stalnaker (Microsoft Corporation)** 47:28 There's no examples of if all the local agent orchestration is taking place via tool calls, that's great, and we don't need to model anything different.
**Nikhil Chitlur Navakiran (Microsoft Corporation)** 47:41 Exactly, that's my conclusion as well. I didn't find a local invoke.
Yeah, invocation scenario.
Yeah, maybe I can add that section. So, say, say this is only for remote agents, and update this, this description.
**Liudmila Molkova** 48:01 also, as a principle, we just enrich what we have, right? We… If it's a transfer tool.
This kind of creates a special… Treatment Special SPAN for the transfer tool.
That's information.
And, in theory, we could… And… Also, put some information on the client's plan.
If… This is the place that knows about the transfer.
The first place that knows about the transfer should require it that transfer is happening.
**Nikhil Chitlur Navakiran (Microsoft Corporation)** 48:41 Right, so, when I was reading it, so since this is, this will ideally be… the… the invoke agent internal span will be the parent of this client span, so So, I was thinking that that might be sufficient to identify you know, like, the… Where the transfer is happening.
**Liudmila Molkova** 49:08 I… I see. And… But it's not… like, if we would, query… all the spans… For, let's say, transfer mode, it would not come up there.
Because… in the strays, because nothing recorded the transfer. And maybe that's okay. Maybe we'll figure out some way there, if necessary. Or maybe we would meet some sort of event somewhere.
Let me, let me dig into this, because I think there are two… two things that… I want to check, like, what does ADK internal behavior, maybe some very well-hidden internal tool that they call still. And the second is, if they call A2A, then 8V will not have the invoke agent per se. It's more like, okay, start a task, and then wait for task to complete.
And then there is no invoke agent at all for the client.
But none of this should be blocking, let me just research it a little bit, and I'll post any comments if I find anything interesting.
**Nikhil Chitlur Navakiran (Microsoft Corporation)** 50:23 Got it. So, yeah, I… I… I don't know if that… this helps, so, like, the… So I added a specific scenario for, the A2A.
Right? So where there is a remote, agent. So there is a… so there's a, like, essentially, like, an, the Agent A, right? So the Agent A has… decides that it needs to do a remote A2A call, and then it calls Agent B. So, on Agent A, it records both the Agent A's internal span.
Invocation span and the invocation Client Span, for Agent B. So, I've added that example, so let me know if, if, like, that is what you were referring to, or if it's something different, yeah. Let me know how I can update it.
**Liudmila Molkova** 51:22 Yeah, there is a proposal, Semantic Conventions for A2A Protocol, it's a PR.
I think I'm not one might… Wow, I remember the number, I'm pasting it in the chat. And it also adds scenarios for A to A.
So, maybe, we can postpone one or versus another.
But yeah, it's fairly something just to be aware of.
**Nikhil Chitlur Navakiran (Microsoft Corporation)** 51:56 Got it.
**Liudmila Molkova** 51:57 Yeah.
**Nikhil Chitlur Navakiran (Microsoft Corporation)** 51:58 Yeah, the, yeah, this is more, specific. So, what this structure shows is that the… like, the… I'm not… so, let me review the other one, but this scenario explicitly shows the structure for, You know, like, the three spans, or the two spans on Agent A, essentially.
**Liudmila Molkova** 52:25 Yeah, I'll take a look at your example. I'm just, thinking that if you create any client spans for A2A, artificial, and it's not how it will be modeled. And also, there could be a merge conflict between this A2A and what, there is an A2A protocol. So maybe… Sounds good. Yeah, we don't need to add this… this here, or, like, coordinate with the other PR. Anyway, I'll… I'll take a look, and… I'll share… thoughts with you, on the PR.
**Nikhil Chitlur Navakiran (Microsoft Corporation)** 53:03 Perfect. Sounds good. Thank you.
**Liudmila Molkova** 53:06 Thanks. One more thing, do we have anything on the agenda after? No. So, I wanted to check it's related to this PR.
So if you… Go to the… Execute to… Bun… I… where are you defining this transfer attributes? Are they, like, a separate… oh, they are right on the execute tools pen, right?
**Nikhil Chitlur Navakiran (Microsoft Corporation)** 53:38 Yeah, yeah.
**Liudmila Molkova** 53:40 Okay, there is a somewhat similar PR for skills, because skills are also tools.
And it creates some principle that… well, not principle, the approach that We have conventions for specialized tools.
So we could record them as tools, and then the… Details would be… would appear… In the inputs and arguments and results, in, like, complex attributes.
But we say, okay, some tools are special, and we will record them and put some of the information that's in the arguments on the top-level attributes.
And there, for that PR, I suggested people to create a span refinement. It's like a specialized version of a span. We're saying it's an execute tool span.
But it's, has this extra attributes.
And, There, I'm also suggesting that we change the name, and I want to test this idea on the people on the call. So, what I think you're saying that here, that the name of the span stays, like, executeTool Transfer.
I think it would be useful to at least include the target name.
In the span name, it will be the Execute2Transfer Target Agent.
But maybe we don't even need to execute 2?
And it would be just a transfer… Target agent?
**Nikhil Chitlur Navakiran (Microsoft Corporation)** 55:29 I see.
**Ankit Singhal** 55:32 So, it's a suggestion to have a new, different kind of spam, or…
**Liudmila Molkova** 55:39 This is called spend refinement. It's like, Let's say there is an inference. Huh? Yeah.
Yeah, there is inference band, and there is, Azure… inference span, right? They are both inference spans, but Azure is a specialized inference with a few extra attributes.
Oh my god.
**Ankit Singhal** 56:06 So for the tool, the executor does something similar.
**Liudmila Molkova** 56:10 Right, and then… The transfer tool would be, this reference, or the skill tool would be the refinement of the tool execution.
So what do we lose?
Now, go ahead.
**Ankit Singhal** 56:32 Seems like a good idea, so that we don't keep adding attributes on one span. Like, if you're doing this, then these are applicable. If you are doing that, these are applicable. I think that's kind of… Makes them too lonely to even understand, right?
**Liudmila Molkova** 56:54 Yeah, Erin?
**Aaron Abbott (Google LLC)** 56:56 Hey, sorry if my internet's kind of in and out a little bit, but I was gonna ask in terms of the specializations, like.
I mean, I guess there's two questions. One is, do the agent frameworks all conceptualize the… or skills, for example, as tool calls, because I know There's… there's, like, the layer of the… the model, and then there's the layer of the… Sorry, I guess I should say inference, and then there's the layer of the agent.
So, for example, you know, most… I think the models are presented with sub-agents.
As tools, for example.
Or… Or, transfer tool. But then there might be some special handling in the agent harness, which treats it a different way, so… I guess we can look into it a little bit, but, Does that… does that make sense, what I'm saying?
**Liudmila Molkova** 57:50 But you're saying, that it's not guaranteed that everybody, represents transfers as to calls, right?
**Aaron Abbott (Google LLC)** 58:00 Yeah, and same with skills, which I think you mentioned before, as well.
**Liudmila Molkova** 58:06 Yeah, and I think I've done the research on both, and it's overwhelming, overwhelmingly, they do.
And… The alternative is that if they don't.
If there was a lot of examples where they don't, then we would need to define a new spend type.
**Aaron Abbott (Google LLC)** 58:30 Right? Okay.
**Liudmila Molkova** 58:32 And… I… Now, it doesn't matter.
But in the future, I hope it will be, once we have spent time on OTLP, it would be a breaking change.
And, like, we either need to design it right away as a different beast completely, And… Where we would say, okay, maybe eventually, if we see evidence, we would separate them, but for now, they are.
the same thing.
**Aaron Abbott (Google LLC)** 59:08 Meetings Yeah. No, I was thinking about spend type, too, because I know there was this discussion about multiple spend types versus having, like, single type, and then the system's aware of the relationship between specializations and stuff, but we don't need to get into that.
**Liudmila Molkova** 59:26 Thank you for not getting there.
**Trask Stalnaker (Microsoft Corporation)** 59:29 Yes, in our last 30 seconds… Cool. Great. Thanks, everyone.
Thank you.
**Liudmila Molkova** 59:41 dear.
**Trask Stalnaker (Microsoft Corporation)** 59:42 Phew.
**Aaron Abbott (Google LLC)** 59:43 Yeah, thank y'all.
**Nikhil Chitlur Navakiran (Microsoft Corporation)** 59:45 Alright, thanks everyone. Bye.

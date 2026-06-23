SIG: Semantic Convention SIG
Date: 2026-06-22
Duration: 65 minutes
============================================================

## Zoom Recording Transcript

Liudmila Molkova 00:04:52 Hello, hi, Robert.
Oh, interesting, we have a topic for 30-45 minutes about the network timing conventions.
Okay.
Okay, should we talk?
Okay, let's do the triage, and maybe I'll remember other important things.
We have in semantic conventions to talk. Okay, this is the issue. Let's start with the PR dashboard ready to be merged.
process to RC, I think it was blocked on something, and I've seen PRs to fix it, but it seems it's still… Let's maybe move it to blocked for now.
Because of other things?
Well, since we moved out Gen AI, this board became manageable, right?
Christophe Kamphaus 00:06:56 That's…
Trask Stalnaker 00:06:59 And Gen AI continues to be unmanageable.
Liudmila Molkova 00:07:03 Oh, I realize they probably don't have my camera on, and… sorry.
Yeah. Okay, oracle DB Convention… at least I'm presenting.
Trask Stalnaker 00:07:19 Yes.
Liudmila Molkova 00:07:24 Wonderful. So we had the same problem that some of the attributes we're… Marked as development, and the span was… RC.
And I think, Sudhar is fixing it, and I've been asking him to… okay, also remove this exception. So, I think this is now… All righty to go.
Database batch operations.
It's yours, Trask, I think.
Okay, everything is… Yeah.
Trask Stalnaker 00:08:09 We can merge it.
I just threw it into… Ready to be merged.
Liudmila Molkova 00:08:16 Western, yeah, it's just a regular unrelated language, Jackish.
Trask Stalnaker 00:08:22 Oh, I missed, christoph's comment.
Liudmila Molkova 00:08:26 Oh.
Christophe Kamphaus 00:08:28 No, I think everything was resolved.
Liudmila Molkova 00:08:35 Yeah?
Trask Stalnaker 00:08:36 Oh, sorry, I'm looking at a different PR. I'm looking… sorry, I'm looking at my other PR. Yes.
This one's good.
Liudmila Molkova 00:08:44 Okay.
So let's see what's blocked this… our… This looks weird.
Would it be blocked?
It's none.
Christophe Kamphaus 00:08:55 Yes.
Liudmila Molkova 00:08:55 anymore.
Christophe Kamphaus 00:08:56 No, still waiting for Adriel's feedback.
Liudmila Molkova 00:09:01 Okay, so I'm putting it in the waiting code owners, or Joe… is Joe here? Oh, you're here. Are you part of CICDSIG?
Joao G. (Dynatrace) 00:09:12 No, no, I'm not, not really, no. Not officially, at least.
Liudmila Molkova 00:09:16 Okay.
Then let's wait for Adriel or somebody else from CICDSIG to approve, and… What else do we have?
What do we have in Entriaged?
Okay, so this seems to be a tooling thing… the HTTP route attribute normalization.
Oh, it's a draft.
I've seen some issues around it, and maybe we should talk about it more.
What's that mandated today?
Trask Stalnaker 00:10:07 Yeah, that's… yeah, it's a good idea.
Joao G. (Dynatrace) 00:10:10 Is that the one that stems from the .NET thing?
Gotcha. I also looked at it, but I thought it was not in draft.
was the issue, maybe, that That has all the examples and stuff.
Liudmila Molkova 00:10:26 Probably this one.
Yeah.
Joao G. (Dynatrace) 00:10:30 Oh, yeah, that, that was… yeah.
Liudmila Molkova 00:10:36 Okay, excellent… Correction… Wow.
Joao G. (Dynatrace) 00:10:55 a bunch of these PRs in the same style, changing the tooling and… doing these things, I… I don't know if we discussed what we want to do with them, like, want to move forward with these changes or not.
I think there's, like, 3 or 4 PRs home.
Oh, for the same person, doing… This sort of things, and they're masses.
And I don't know, it has been working fine so far, so I don't know if we want to change something that's… One of them uses, replaces one of the tools, because they've been deprecated or archived, so maybe that one we… Can take a look, but…
Christophe Kamphaus 00:11:39 If I followed it right, it's also to make the tooling consistent with other OpenTelemetry repositories.
And a few of them were blocked because the tooling had features missing.
And he implemented some and committed some upstream for those tools.
Liudmila Molkova 00:12:03 Yeah, it doesn't seem controversial, it's just the usefulness of those changes is sometimes… Joao G. (Dynatrace) 00:12:10 Yeah, exactly. I was like, I don't have much time to review this massive thing, so I just didn't.
But I guess if we agree that this is beneficial, then, I don't know, maybe I'll… I'll spend some time and look a little bit into it.
I just feel bad because it's there for quite some… quite some time. It gets, stay all the time, and… Okay.
Liudmila Molkova 00:12:36 For this one, I think we've been essentially waiting for… because none of us knows what to do. Oh, at least, it's my assumption with the front matter stuff for Hugo. I have no idea.
If it's necessary, if it's useful… Joao G. (Dynatrace) 00:12:50 Yeah, me too, yeah.
Liudmila Molkova 00:12:52 been usually relying on the, Atrace challenge from OpenTelemetry I.io to Blessed, so I'm going to move it to… Awaiting code owner's approval, because he is the code owner approval, essentially, for such kind of things.
Okay, so we are probably out of our budget for, the, the triage, I just wanted to take a quick look here.
It seems… the Weaver update.
It's breaking a lot of stuff, out… try to take a look.
Oh, why?
Okay.
Interesting.
Cool, let's move on to the agenda. And we have… A few topics. Sorbi, are you around?
Surbhi Agarwal 00:13:53 I am, yes.
Liudmila Molkova 00:13:55 Awesome.
Do you want to present? Do you want me to present?
Surbhi Agarwal 00:13:59 I'll present.
Liudmila Molkova 00:14:00 Awesome.
Surbhi Agarwal 00:14:01 Let me share my screen.
Liudmila Molkova 00:14:09 Let me stop sharing.
Surbhi Agarwal 00:14:13 Yes… Can you see my screen now?
Trask Stalnaker 00:14:18 Yes.
Surbhi Agarwal 00:14:18 Awesome.
So, it was regarding… Client network timing event that we have discussed before as well.
So, we did create a prototype, worked with the browser and mobile sigs on what it could look like.
So, I'll quickly brief what this is about, so everybody's on the same page.
Basically… This is a new event.
with the name of HTTP client network timing, that would… capture the different face timings for different HTTP network phases.
So… We have these attributes, wherein only one of them is required, which is the call end relative time.
Others, DNS start and connect, secure connect, request header start, request body, response headers, response body, these are the attributes, these are opt-in, based on what the platform provides.
Because all of these are not there in browser, some of them are there. So basically, the timestamp of the event would capture the call start time.
Then these timing attributes are relative to this timestamp.
That's why they have the relative time wording.
And… The context here on the event would help you correlate to the original HTTP client span.
In the backend.
the timestamp would be according to the OTLP, definition, which is Unix epoch Time passed elapsed since Unix ePorch in nanoseconds. The timing attributes are in milliseconds.
That's because we do not need nanosecond-level precision here, and what browser and mobile APIs provide, that would unnecessarily need into 10Race to the Part 3 to convert them to nanoseconds, so there's no need for that. So… But this, we ensure, would be a nanosecond to keep with the semantic conventions.
So, with the help of… Yeah, go ahead.
Liudmila Molkova 00:16:51 Maybe we can talk about general approach, because, like, the… the details, like nanoseconds, or naming.
are secondary, and I think the most important part is that and I think there are some discussions on this, so the PR, whether… why do we need to first amid so many timings, can we represent at least some of the things as spans? For example, the start timestamp would be the start of HTTP span, the end timestamp and HTTP call would be the end of HTTP span.
And I've seen some discussions that spans might not be immediate, but… but why? If you want to emit this information, if you want to capture this information, just capture it in the span.
And then at least some of the, timings, would be on that span and don't need to be captured.
Separately.
Surbhi Agarwal 00:17:53 Yo.
Michele Mancioppi 00:17:54 I have to agree with Rodmilla. Doing spans out of this is gonna make it strictly better to query in every single tool I've ever used.
Surbhi Agarwal 00:18:04 Spans were not chosen because… Basically, we are not instrumenting these different phases.
We are capturing the network, just the timing of these various phases.
This is not DNS phase instrumentation, this is not connection phase instrumentation, this is just something to go along with the original HTTP span.
To be able to capture just the timing of these phases, so you can understand where the network latency is.
There are some… this is… there is some rationale that we came up with for why we don't want to choose spans, but want to choose a single event. So, browser today def… it is also designed based on how browser does it today. So, browser has this resource timing API, wherein they get all these timing details via this API.
That is one.
Liudmila Molkova 00:19:11 So the first one, there is no Span instrumentation, but maybe the thing that produces this event should be produced Span instead. This is the instrumentation for the this pen.
And these attributes can be on a span, some of them, if we don't want a separate span for them.
Michele Mancioppi 00:19:29 No, wait a second. Let me try to explain the gap between the proposal. If I understand correctly what the limitations, then the spans would be of 3.
So, you could… It's unclear, when I read this whether you would know what is the parent of, let's say, the HTTP call span.
And, they would not be in the hierarchy of the HTTP server span on the other side.
Which would be weird.
For the end user.
Liudmila Molkova 00:20:02 So the subphases, I… we can talk about it. I think there is the reasonable, I see the reasons why some of this timing should be attributes and not spends on their own.
But the whole thing… Why shouldn't it be a span?
Michele Mancioppi 00:20:21 It would be… would make sense if you could ensure that the spans you would create from these timings would have the HTTP client span as parent.
And, it is unclear to me whether this is feasible.
Surbhi Agarwal 00:20:35 It is not feasible.
Yo.
Trask Stalnaker 00:20:37 So, it's not… I thought you mentioned that the context, the event, The event… the parent context for the event pointed to the client span.
Surbhi Agarwal 00:20:52 Yo.
So, there is correlation here, so the context in this event would point to the original HTTP client span, yeah?
Michele Mancioppi 00:21:03 Then Ludmilo's right again.
Trask Stalnaker 00:21:09 So could the whole event be one span?
Surbhi Agarwal 00:21:14 It cannot be… Because… the span, like, if instance for… if instance, we talk about the OK HTTP instrumentation.
Okay, first, let's talk about the browser. So, basically, these timing data is received asynchronously by the browser, which is after the fact that the span has ended.
And there are a lot of use cases in browser network requests where there is no HTTP span instrumentations, but they still want this event, right? Here in OKHTTP…
Trask Stalnaker 00:21:56 Would that be a… let's stay on route, let's do one at a time, since they're different.
Would it be a… problem… In the browser case to emit a span there.
In that case, I'm trying to understand why it's a problem to emit a span.
Surbhi Agarwal 00:22:17 O-span doesn't justify the data that we are emitting here. O-span for all this, it is not a… It is basically… An event capturing all the various attributes, all the… a log capturing all the timing for the various network phases. So you think it should be a span with call start and end time as… it is not a… I'm not sure why it should be in a span.
Liudmila Molkova 00:22:51 Because it has a start time and duration, right? And the status, and it naturally fits as span.
And you also are assuming there is a client span, and it's correlated to, but guess what? It can be a source of the trace context, it can be the span That, either is the HTTP client span, or something that happens, starts even before, because there are redirects, and you're also waiting for the response.
So it naturally fits as a span in semantic conventions.
Michele Mancioppi 00:23:24 And, if the users want, for example, to calculate histograms.
About, whether the DNS is a problem or not.
They can do it very easily if these are spans, but it gets much, much, much, much harder if they're events.
Surbhi Agarwal 00:23:42 So I have a question. You guys are proposing one span or multiple spans?
Michele Mancioppi 00:23:48 Multiple.
Surbhi Agarwal 00:23:49 But that… that's what I mentioned, right? I don't think it fits the data that we are talking about here. I do not have… I just have the timing attributes. I am not instrumenting those individual phases. So you would emit like, there are so many of these attributes, so would you rather emit these many spans, and then correlate them in the backend? That is too much… Data over the wire, and too much correlation in the back end.
It is a network timing event capturing all the data that is needed for the backend to gather the metrics out of this. I'm not instrumenting each individual faces, that is a separate concern. There would be spans for DNS, but that would be DNS instrumentation. It would capture the…
Michele Mancioppi 00:24:39 You do not need to instrument it, so not all spans are created through instrumentations.
That will wrap around the fetch object.
You can lead it the same way that you get today the data to create a span event.
You can literally go and create spans instead.
Christophe Kamphaus 00:25:04 I shall…
Surbhi Agarwal 00:25:05 It would be so difficult for backend to tie along all these spans together to be able to create those metrics in the backend. So, like, here I have shown the example metrics derivation. Some of these use… So, I want… I would also have to relate the different spans then. Like, here, if you see the examples.
So, I'm using the response header and request body here for this metric.
So I'd have to correlate, then, these two different spans also at the back end.
Michele Mancioppi 00:25:41 And they have the same parent, right?
Surbhi Agarwal 00:25:44 No, these are different spans, right?
Michele Mancioppi 00:25:46 Yeah, they have the same parent.
Surbhi Agarwal 00:25:51 Rosen?
pattern.
Michele Mancioppi 00:25:53 parent.
So these are separate spans, but they have the same parent ID in the span.
Trask Stalnaker 00:26:04 You'd have to join through the parent.
Surbhi Agarwal 00:26:07 Yeah, there is a problem, right? So, the correlation using the context in the backend is doable, but then not all backends are able to do that today.
Right, this event also helps the interim state.
Wherein we could copy the original HTTP span attributes to this event, and then this event becomes the sole event which a backend can use for all the network timing metrics.
The correlation is not available today in all the backends. A lot of them.
Michele Mancioppi 00:26:43 I can tell you that there's a bunch of backends out there that are not going to be able to do these correlations on span events, either.
Support for Span events is very dodgy.
Liudmila Molkova 00:26:55 Others are not spending.
Michele Mancioppi 00:26:57 against, right?
Liudmila Molkova 00:26:57 Those are log-based events, which makes it even harder to correlate.
Michele Mancioppi 00:27:02 Even worse, yes.
Surbhi Agarwal 00:27:04 Yeah, so right now, with the event, there is an option to copy the original HTTP span attributes on the event itself, so you do not need to use the correlation. You can use that in the interim.
And for the backends which can correlate different signals, they can use the context.
Liudmila Molkova 00:27:28 just give another reason to make it the HTTP client spend, because it creates… it copies attributes over from the original HTTP client spend to this event. You actually want one thing to represent them both, but then Christoph has his hand raised. Go ahead, Christoph.
Christophe Kamphaus 00:27:45 Yeah, so if I understood it right, you base yourself on the API of the browser to read these timings.
So, implementation-wise, it's easiest for you to represent it as an event, because you can just copy it over from the API to this event.
If you needed to represent it as bands, you would… need to generate some based on these timings. Is that right? Did I understand it right?
Surbhi Agarwal 00:28:15 Bubb!
No, it was also a thought that went into these other things also that I'm mentioning.
Like… We are not having any other data other than this timing.
We want one signal rather than multiple signals.
The thing about… correlation that I mentioned right now.
all of these added to what you mentioned as well. It was designed based on how browser API is today. It is an API that provides all of this timing data, so it was designed based on that, yes.
But it's not the sole reason that the implementation becomes easier.
There are multiple things.
Liudmila Molkova 00:29:18 So I want to say I… I see the concern around the payload size, and a lot of different signals for sub-things, like the relative timestamps.
But… So I want to explore the option where this is either the same span as HTTP client span.
Or something even above it, because it's… it drops the more… the time That starts before, includes redirects, and also the full body response.
And then… These things appear as attributes on the span.
This way, it does not introduce extra payload, well, the attribute payload, but not the envelope payload, so it's not in a separate telemetry signal. It can also be modeled as spans. If, for example, you… somebody wants to enable low-level instrumentation for DNS and maybe some extra things. So you can, in theory.
Can't want to represent them one or another, or maybe even both.
But I personally don't see controversy in having some of them stamped as attributes. But the whole thing clearly maps to this pen to me.
Trask Stalnaker 00:30:52 Ludmila, what about, the span status?
Like, does this… bag of… Event, bag of, durations, Have a status…
Liudmila Molkova 00:31:11 So if you think about the, almost like a logical HTTP span that does redirects and reads the full response body. It has a status if it's either didn't get the proper status code, or an exception happened after the response has started.
And yeah, it has a status.
Surbhi Agarwal 00:31:36 But that's for the original HTTP client span, right? What about this… this new span that we are talking about here? What would be the status? Same as the original HTTP client span?
Liudmila Molkova 00:31:48 So it's an interesting question whether it's a separate span, or it's just attributes on that span.
Surbhi Agarwal 00:31:54 So, I had… yeah, so for that, we did, look into that, right? We tried to prototype it.
So, these attributes would be part of the same span, but what happens is, when we prototype it for, let's say, OKHTTP3, the span ends much earlier than when we do not get some data that we require on this event.
Until the span lasts.
Liudmila Molkova 00:32:23 And then there are two options. Either we replace That span was… Our new span, that includes network timing, just the instrumentation changes, so it produces a different Instrumentation points, or, we invent a new span.
If that… the first option doesn't work out for some reason.
Trask Stalnaker 00:32:51 So that's an interesting proposal, Serbi.
Yeah, where… the HTTP client span, the normal HTTP client span, wouldn't get created… But you would prop… you would still somehow propagate the information that that captures, like, URL, server, etc.
down… Propagate that along so that hopefully in that duration event, when that event comes in from your remote HTTP, you could then reconstruct the original HTTP client span at that point.
Using the total duration that was provided by the… this event.
And… populating those HTTP client spans that were hopefully passed along somehow From the original instrumentation.
Surbhi Agarwal 00:33:59 Though in… In mobile, it is all synchronous. We do not get an event that gives us all the data that is required in the original HTTP client span. It's a synchronous workflow wherein we tap into the workflow to gather all these details when they happen.
And similarly for the timing also, but in browser, it is received asynchronously via a API.
So… I did not understand the proposal here. Does it work for both?
It is not like I'm getting an event asynchronously later, which tells me all the data that goes on the HTTP client span, and I just have to copy, it's not like that. It's a… Instrumentation of the entire workflow, which taps into the synchronous workflow to gather all that data.
When the event is… when the HTTP request is actually happening.
In browser, for the timing, you receive it asynchronously.
for… I don't know what happens for the spans there, the instrumentation itself, for the HTTP.
Trask Stalnaker 00:35:19 Right, so it's not clear to me how, I mean, immediately how or if this is possible, but the thought is that in those, when you're receiving that information, you kind of stash it somewhere.
While it's… Happening, and then at the end, you can then take all of that information that you stashed and reconstruct the synthetic span, you know, with all of the details.
Surbhi Agarwal 00:35:55 I don't think that would be efficient, to store all that data for all the HTTP instrumentations.
Liudmila Molkova 00:36:05 But you're storing… this… Alrighty.
Right, to create this event.
Trask Stalnaker 00:36:15 The question is if there's a good place to store it, like, I mean, let's just take a very… a simple example, like, if it's all, like, in Java, if it's all in a, you know, single thread, you could attach a thread local object struct that has all of this data in it.
And then, in each of the callbacks, you could grab that thread local struct and populate the data in it that you want, and then at the end.
you know, you have… you can grab access to it. Obviously, that's very simplified, assuming it's all on a thread, it probably… Isn't, but there's… Sometimes a place that you can stash that.
Surbhi Agarwal 00:36:58 I wanted to confirm, so, do we have a consensus on what we think it should be? Right now, we talked about multiple things. Having a span containing these attributes, plus the original HTTP, like, what's the preference order that… those sick things. Should there be multiple spans? Should there be one span? Should there be multiple events? Should there be one event?
If you guys can, like, mention the preference order of what you guys are thinking. Also, if you can doc… help us… With putting a comment.
Either in the issue or in the PR, wherein we have discussed this at length, and gone over the various possibilities of why it shouldn't be something.
It would be helpful for… Me to look into it.
I think right now, also, there are multiple things that we are talking about. We are talking about multiple spans, we are talking about one span containing these attributes, which relates to the original span, we are talking about the original span containing probably these attributes. All this discussion we have had earlier.
So, like, if we can have a preference order from the SIG, then I can go back, look at the rationales.
look at any new things, so that way I can answer you guys, and look at if it can be done differently.
Liudmila Molkova 00:38:30 I can leave a comment. My preference would be that this is the HTTP client spend, and we changed the instrumentations to either Do this or suppress in presence of, the, the, the new… HTTP client span. It covers the full duration, and it has those as attributes. I… didn't design it, obviously, and there could be, implementation, or structure or reasons why it cannot be done this way, and then my preference would be to have span definition that, represents this, I don't know, client mobile or browser client, the user client, HTTPS pen, or… we will decide how to call it, and then it would… hopefully be apparent to the actual HTTP client span, and it would have all this information as individual attributes. I think. Michaela, would prefer them to be as individual spends, but, then there is a question of the payload, and I think you… you… and the joining on the back end, and those are the good concerns to have.
Surbhi Agarwal 00:39:50 I also want to touch upon what you mentioned, right? So, we did prototype the first option, and it wasn't feasible.
Like I mentioned, there are some… problems there. You would have to… Stall the current… etched… currently in browser, they are using a span, I guess, for it. So in there also, they are having to stall the original span until this kind of data appears, so to be able to add it to the original span. So, browser also, it is not feasible, the first option.
In mobile, also, it is not feasible. Currently, the span timeline is a little bit different. It starts after the call start and ends before the call end today, with whatever is provided with your HTTP API. There are some API nuances there, so we are not… and the response reading time Those things we cannot capture in the original span, so you have.
Liudmila Molkova 00:40:49 Yeah, I hear you. I will leave it in the comment, but I think there is opportunity to change this instrumentation, or make them know about each other and work together.
So this would be a new instrumentation.
That does not need to interact with the old one, or… they would be… whatever. Anyway, I'll leave a comment. I don't feel like you explored the option of Changing the instrumentation on its own.
Surbhi Agarwal 00:41:20 But that would be redundant, right? It wouldn't… So it would change the existing behavior. Customers would have to switch from one instrumentation to another to be able to get this new data.
Whereas the event that I proposed, it goes well with the existing… it is… it is backward compatible, right? It just adds to the existing instrumentation. They just need to flip a flag if they want that additional data.
Michele Mancioppi 00:41:50 But, this part is something that confuses me. So, you said that This data comes out of band.
Which means that… the span, the HPP span of the actual request may already be closed.
By the time the data comes in.
Which means that you cannot add an event to that.
So, how is this recorded again, in case the span is already closed?
Surbhi Agarwal 00:42:16 So this is a totally separate event that looks at the… HTTP request, and captures all this data, and you… you are able to get the… You are able to keep the context Of the original span.
Michele Mancioppi 00:42:38 Wow.
Surbhi Agarwal 00:42:38 To be able to add to this event.
Michele Mancioppi 00:42:41 It is a log event.
Surbhi Agarwal 00:42:43 It's a log event.
Michele Mancioppi 00:42:45 And then you use trace ID and span ID to… for the trace context.
Surbhi Agarwal 00:42:49 Yeah.
Michele Mancioppi 00:42:51 I get it. Thanks.
Liudmila Molkova 00:42:53 Yeah.
Surbhi Agarwal 00:42:54 So, the other…
Liudmila Molkova 00:42:55 Oh, sorry, two more minutes for this topic.
Surbhi Agarwal 00:42:59 Yeah, so another thing that you mentioned I want to clarify, Ludima, you mentioned that, The new span, with all the timing attributes.
That should contain the… that should be the parent of the original HTTP span.
Liudmila Molkova 00:43:20 Ideally, yeah.
Surbhi Agarwal 00:43:24 Okay.
My idea was, it is the other way around.
Liudmila Molkova 00:43:31 So the reason I'm saying this is because you have, redirect timings.
And it means that this thing should start before the original span, because… Redirects happen… after the HTTP request starts, not… War.
Sorry.
Surbhi Agarwal 00:43:52 They're ready.
Liudmila Molkova 00:43:53 direct is, it means that there is more than one HTTP request, effectively.
so maybe we'll do this. I'll leave a comment, The concern here is that the structure leads a span, whether it's an existing span or a new span, it's probably a separate question.
There is a question of implementation, but structurally, the thing is a span.
And at least in the current shape, you can capture it as a span. There is no technical blockers that would prevent it.
So I will leave a comment, I'll leave some suggestions, I think you folks can discuss it in the SIG, and maybe if somebody wants to come next time, we can continue the discussion from there.
Surbhi Agarwal 00:44:42 So, I want to clarify that a span… with these attributes, not the original HTTP client attributes, right? As we discussed, the first item, first preference that you mentioned is not feasible, so this is the… this is what is feasible. So, do you think it should be a… instead of a span, it is… it is instead of an event, it's a span with all these attributes? That's… is that something acceptable?
like, I wanted to get a general consensus in the SIG before we move on, because.
Liudmila Molkova 00:45:24 I don't think we can get to the consensus today. So, I think we can discuss, and even if I, accepted. There could be other people who have other opinions, so… and we are, we have, We're out of the box for this topic.
Surbhi Agarwal 00:45:47 I've been in discussion since September. How do I get consensus? How do I get that consensus if not here?
There have been no comments. Like, in the issue that we have discussed, there was another issue before it, starting September. We reached this decision based on what the browser and MobileSick thought was the best.
And then that's how this PR came about. We did a prototype in OKHTTP3 already for this.
So, we do need to reach some… Or we need to, like… the people who are here today, right? Like, what's the next steps, right? .
Liudmila Molkova 00:46:32 The next step would be to entertain the idea of a spend.
And explore if you could have, If you wanted to stamp the HTTP client span attributes on this one, then probably it can be the HTTP client span. I will leave a comment, and we can discuss it next time if you come to the SIG.
Yeah, Trask.
Trask Stalnaker 00:46:56 Yeah, I was just gonna respond, Serbi, the… the… this is the group to get consensus from, but that doesn't mean we can get consensus in… one meeting. It may take many, you know, coming back to this meeting, joining this meeting for, several or more calls, and sort of iterating, and, you know, you're getting us, back up to speed on this issue. We're getting you… giving you some feedback. We need some time to think about it, and, you know, continue the discussion, in… Can… in multiple meetings.
Surbhi Agarwal 00:47:39 Okay, that sounds good. Can you leave a comment in my issue as well? So… Everybody is on the same page about this.
So, Lord Millah.
Trask Stalnaker 00:47:54 Sure, about following… about coming… continuing to join this meeting to, discuss.
Surbhi Agarwal 00:48:01 No, just about, what the preference is each one of the people who are going to decide.
what are the options you want us to explore, each one of you who are going to decide what it's going to be, if you can come and mention that, because I have been answering these questions in over a lot of meetings, over a lot of time now, but looks like haven't reached a consensus yet, which I thought I have reached.
So yeah, there was no representation on the issues from the semantic sick.
So if you can, mention your opinions, all the things that we need to look into, that would help me a lot.
Because, right, if tomorrow I come to the SIG, and there's a new person, and they mention a new idea, and then I have to go about exploring that, that doesn't help us, right?
Trask Stalnaker 00:48:57 So, you… what you need is, you need agreement from the semantic convention maintainers, right? That's the group that is going to merge, ultimately approve, merge, hit the merge button.
Surbhi Agarwal 00:49:10 Yup.
Trask Stalnaker 00:49:11 So, I mean, you can see on this call, we've got 6… Semantic Convention Maintainers.
Okay. You can, you can check the list on the repo.
But then, you know, there's other regulars who also have good opinions and help us to understand options and ideas.
Surbhi Agarwal 00:49:40 Yeah, like, if… just a request to all of you, if you have any differing ideas that you think it should be done, do mention it in the issue. It would help me, go about it.
timely, and discuss it with… because I have to go to the browser sign next, and the mobile sign next, and discuss it over and over again, so it would help me if I have all the ideas that… I can talk to them about upfront.
Liudmila Molkova 00:50:12 Thanks, we are definitely out of time, but I appreciate you coming, and if you can, involve other people from the Sikh to come here as well, that would be tremendously helpful, so you don't need to do all this work yourself.
Surbhi Agarwal 00:50:25 Sounds good.
Liudmila Molkova 00:50:27 Josh, go ahead.
Josh Suereth 00:50:28 I… yeah, I know that… I know we're way over time, so all I'll say, though, is the general feedback I heard from our group to you on this issue was there's existing data model semantics in OpenTelemetry.
Your proposal does not match them.
So, one thing I would ask is try to understand the data model of OpenTelemetry better.
And, like, say, does this look like a span? Because when it looks like a span, and you're not modeling as a span, we're gonna push back, and that's what's happening.
Right? And so, yes, I think it's fair for us to ask for more of our time to understand this, but it's also, this is open source. So, what I'd recommend is take that feedback and, like, go look into the OpenTelemetry data model.
the thing that we're trying to present, and say, if I push this data, does it work with existing tracing systems? Yes or no? Does it work with existing logging systems? Well, yes, because this looks like a log, but the tracing part isn't true, right? Does it work with existing metric systems? Not quite. And so, like.
I would ask you to do some research there as well, right? Like, I think this is a two-way thing, and I understand this is a lot to ask, and it's really hard.
And I apologize for that, because I think the client-side SIG has had a lot of back and forth and things like that, but fundamentally, that has been the biggest friction we've had with client-side, is there's a data model on OpenTelemetry, client-side needs things to work differently.
If you want it to work differently, you have to put the burden of proof for how our data model fails, and maybe propose changes to the data model instead of proposing changes that use our data model in a way we think systems will not consume well.
Does that make sense?
Surbhi Agarwal 00:52:09 Yeah, that makes sense. The thing is, we understand the OpenTelemetry semantics, and this was based on our understanding of things combined with all… not just mine, but whatever people I have discussed it with over the browser and mobile sick. So it wasn't like we do not understand the open telemetry semantics, or haven't taken the pain to understand it. But, yeah, I hear you. So this was not about… This was not… this was basically about… so I can take the right feedback going forward, and work on it, such that we can reach a consensus sooner rather than later, because I have had none of that before, so, like… did not know. So, like, this is now, again, reworking the same thing, which I get it, that it needs to be done. Yeah, but if you guys not respond today.
Josh Suereth 00:53:10 Yes, sir.
when you come back, just to be brief, please come back with why you think it's justified that, like, this is not a span, this is not a thing. Like, just come back with that rationale. If that's a decision you made with rationale, and we can read through why you're making that decision, that helps a lot.
Surbhi Agarwal 00:53:29 added that context here, right? That context is here, why it is an event.
Josh Suereth 00:53:34 Okay.
Surbhi Agarwal 00:53:36 I have added some context here already.
Josh Suereth 00:53:40 to answer these questions. Alright, and then be prepared for us to disagree with your rationale, is the last part, which I think is what we heard here. So, like, when you give us that rationale and we say, we don't agree with that rationale.
that's where we have to have discussions. Does that make sense? So, I… I will take it… sorry, I've been… I was quiet. We can take an action item to look through your rationale and talk about what we agree with and what we don't agree with, and that can focus our discussion.
But I would expect this to have some back and forth, because this does not look like other semantics.
Surbhi Agarwal 00:54:14 Sure, that sounds good, yeah. So today, I think, like, yeah, we did discuss one different option that I think most of you guys agree with, so do mention it in the comment, and I'll take a look and come back.
Liudmila Molkova 00:54:28 Awesome, thanks a lot, and sorry for this taking long.
Surbhi Agarwal 00:54:33 Thank you.
Liudmila Molkova 00:54:36 We are going to go.
Fair enough.
And… Moving on to the next topic, Christoph, the… ban conventions, VCS fans.
Do you want to present, or…
Christophe Kamphaus 00:54:54 Now, if you go to the last comment, basically, we don't yet have a prototype for this, and when we wrote down the CICD conventions, that was not yet a requirement, so my question is.
Should we now also, do a prototype for the new ones, or is it fine if we… Merge it as is.
Liudmila Molkova 00:55:28 So these are the new SPAN proposal.
Or…
Christophe Kamphaus 00:55:32 Or version controls systems.
Trask Stalnaker 00:55:40 I thought there were prototypes for… oh no, I'm thinking CICD, sorry.
Christophe Kamphaus 00:55:46 Yeah, so we do have CICD tasks that represent a checkout, for example.
But it's not… We don't have conventions to say we are now checking out this repository or this commit.
Liudmila Molkova 00:56:08 Is there… what are the reasons we don't have a prototype?
Christophe Kamphaus 00:56:14 Because we haven't developed it yet.
So, probably Atriel and me will get right on it.
Liudmila Molkova 00:56:24 I think it's always extremely helpful to have a prototype, and you can now point the AI at it, and it's probably very fast.
Christophe Kamphaus 00:56:35 Sure, we can do that.
Liudmila Molkova 00:56:38 I don't remember what's in our policy. I think we require prototypes for stable things.
I'm not completely sure we have it documented for everything. Should we just document that prototype is required?
Christophe Kamphaus 00:56:53 I think it is in the pull request template.
Liudmila Molkova 00:56:59 The, that the links are, right, yes.
Yeah, I think you're right.
So then, yeah, it would be awesome to have a prototype, and thank you for bringing this up.
Christophe Kamphaus 00:57:15 Okay, I will take setback too.
It's PR.
Liudmila Molkova 00:57:20 Thank you.
Okay, we have 7 minutes, so let's try to cover as much ground on the HTTP route normalization.
I don't think I would add it to the agenda based on the triage.
I'm not sure if Rosimo's here, well, I'm pretty sure he's not, but let me check.
So, the history I know about this issue is that HTTP route is… Maybe a little bit underspecified, and it's not super clear what it should be for each of the frameworks.
And it sometimes results in either instrumentations, putting something wrong in this attribute?
But if I understand correctly, the proposal here and then the issue is to make everybody produce consistent HTTP routes?
Do you have more context, Trask? I think you participated in some of those discussions.
Trask Stalnaker 00:58:37 That is my understanding.
Awesome. And… Yeah… I mean, there's the URL template, I mean, HTTP route… I don't know, I struggle with this, I… don't… I'm trying to understand how… useful this is. I mean, I think it's very cool to have route… be standardized?
and be, like, I know in the Java instrumentation.
We kind of had two choices for routes a lot of times. One is, like your MVC, your controller classname dot method name.
That's a legitimate route.
But there's also the template that goes with that.
the URL template.
And we have tried hard in Java to always use, wherever possible, the route, I mean, the, yeah, the… URL template for the route.
Because I think it is very nice to have the… I think the URL template makes more sense there on the span. It's more kind of end-user facing compared to some internal controller class.
Name.
It has not… there were a couple cases where we couldn't do that.
And… normalizing it, further, would be a good… amount of work. I worry, like, you know, who… what is the canonical URL?
Template form… Different people use different… Do you use… Different, templates, and… there's some benefit to… I mean, for example, a node person getting what their, you know, node template typically looks like, like, say it's colon Something, instead of squiggly brackets around it, or… dollar sign something in spring, I don't know, just making stuff up.
So, trying to understand, really, like, what problem is this trying to solve, and what are the, you know.
Potential downsides as well.
Michele Mancioppi 01:01:16 I think it makes sense to differentiate between HTTP route and URL template.
Because for HTTP route, the consistency of the values is more within the same application.
So, if you're a Ruby shop.
You liked the columns because it's a symbol?
And if you are a JAXRS shop, then you like the curly brackets.
there, I… I don't see particular value in having the same syntax to represent a parameter in the URL.
between languages, but I do see a world of usefulness in having the URL template to be specified consistently.
Because in that case, you can actually go and compare apples to apples across different clients.
Trask Stalnaker 01:02:16 I see, so you're suggesting the… the flip… the reverse, where… HTTP route would be the natural mapping to the frameworks.
route.
and URL template could be something that we invent, that, syntax that we invent.
Michele Mancioppi 01:02:36 It, exactly. And, to make it consistent, because in that case.
to be able to, to analyze the HTTP clients.
Grouping them by URL template of what they're calling across different implementations, that would be very useful.
I would not force a specific syntax for STP route, because you are not comparing apples to apples. You so seldom have two different implementations of the same API.
That moving away from the familiarity of the end user, recognizing the syntax of their Route middleware of choice.
That feels… not necessary.
Christophe Kamphaus 01:03:21 Yeah, you would already have to have… Mixed microservice environments, where you mix languages and middlewares.
Michele Mancioppi 01:03:30 Yeah, you would need to get value out of one single syntax for SCP Route, you would need the same API implemented in multiple languages.
And that… Is a bit far-fetched.
But having multiple clients using the same URL template to invoke the same API every day.
Christophe Kamphaus 01:03:50 Completely agree.
Trask Stalnaker 01:03:54 You're muted, Ludmilla.
Liudmila Molkova 01:03:57 So it sounds like, There is a consensus, and I agree with it, that we don't really see a benefit in standardizing certain formats.
But, like, since .NET has these interesting ways to express the… the… what they consider to be a route.
It would be totally fine for ASP.NET Core.
instrumentation to have its own convention, and decide how to capture those, and document it in whatever form they want. We can, probably be more prescriptive in the semantic convention, saying that for each Framework, actually think about how you want to capture it, and what it should be, and document it.
Michele Mancioppi 01:04:48 And, I've also… this is more like a rant than a regimented discussion, but… If we can avoid… making harder for people to implement HTTP route?
Please, let's do it, because that is the single most important HTTP attribute that is not set.
most of the stand names are either high cardinality or completely useless by just putting the method, because people are not going to HP Route. Raising the bar by having to implement a specific syntax and map from your framework to HP Route I don't think it's gonna be the… the… the straw that breaks the camel's back, but… I mean, I would give several limbs to have HTTP route implemented consistently as it is.
I would take any value they want to write in there.
Trask Stalnaker 01:05:43 Yeah, we had time. Lyudmila, I will follow up on this, since I've been involved in the DISC earlier discussion, I think.
Liudmila Molkova 01:05:49 Awesome.
Trask Stalnaker 01:05:50 Oh, that makes sense.
Liudmila Molkova 01:05:52 Yeah, thanks a lot.
Trask Stalnaker 01:05:53 Well…

SIG: Event WG
Date: 2025-09-30
Duration: 49 minutes
Zoom Recording URL: https://zoom.us/rec/share/47dDZlURh3tJTievbtJaCATKfhWToIvaNoAF-CkRmvoePyhWX2tTu8XPWqhW1v7A.8MnZ1yJj54TyPQoH
============================================================

## Zoom Recording Transcript

**Trask Stalnaker** 00:13 Austin!
**Austin Parker** 00:14 Alive!
**Trask Stalnaker** 00:16 Yeah…
**Austin Parker** 00:21 Ugh…
**Trask Stalnaker** 00:27 There we go.
**Austin Parker** 00:28 Yay!
Yeah, I was gonna be at the spec call today, but… Kiddo had a dentist appointment.
**Trask Stalnaker** 00:45 Yeah, it'd be good to have you back.
**Austin Parker** 00:49 Yeah, hopefully… I should be back… I should be around more frequently now.
**Trask Stalnaker** 00:59 Whoa.
**Austin Parker** 01:08 Excuse me.
**Trask Stalnaker** 01:15 Hey, Serbia!
**Surbhi A** 01:19 Hello?
**Liudmila Molkova** 01:27 Hello!
**Trask Stalnaker** 01:29 Hey, Lena.
**Austin Parker** 01:31 Hey…
**Trask Stalnaker** 01:43 Did we hear from Robert?
Not yet. Okay, he may join.
But let's, yeah, let's… Discuss your topic, Sir B.
**Surbhi A** 02:03 Y'all.
So, like, there is this proposal about, moving from span.events to standalone events.
Let me share my screen.
**Trask Stalnaker** 02:18 Sure.
**Surbhi A** 02:20 Okay, Can you see my screen now?
**Trask Stalnaker** 02:32 Yeah.
**Surbhi A** 02:34 Okay, awesome. So yeah, there is this proposal about moving away from span events to standalone events.
So, like, I had a proposal, as per our last discussion in the JavaSIC So there was this… Like, for breaking down the various net… HTTP network requests.
span phases, right? I proposed adding these various events to the HTTP spans itself.
And the requirement is just for the timestamp and the event name.
So, backend can drive… per request basis durations of this sort, like how much the DNS resolution took, the TLS handshake took, what was the server processing duration, like that.
So, like… here, like, I had, I have, question of the sort. Like, one, I wanted to know what is the plan around this deprecation.
And if this deprecation were to happen, like, currently the Java SDK, add time event sort of APIs, which add events to the span itself.
how would they be deprecated? Would they be backward compatible? Would there be a configuration to do either? Like… Emit standalone events versus add events to the span itself, because backends might not be ready to correlate standalone events with the spans, immediately, right? There might be… they might need time for that move.
But also, like, would there be a use case for both? Because… in this use case, I just need… the name and the timestamp. The attributes are already present in the span, I don't need any additional attributes. There is no additional body I need for the event.
It's like a smaller event that can be attached to a span.
Yeah, I had these questions.
Sure.
**Trask Stalnaker** 05:06 So let's take them, one by one.
The… Your first question was, about what would happen… If, when this is deprecated, what the Java API would do?
**Surbhi A** 05:32 Yeah, and first question is sort of, do we know if we are moving towards this direction?
**Trask Stalnaker** 05:40 Yeah, we're definitely moving in that direction. At what speed is, An open question, but it is definitely the long-term vision to have a single, like.
Concept of events, what events means.
There's… Okay.
From a backward compatibility perspective, there is… We may never… I think we decided not That we wouldn't… Deprecate it at the proto-layer, because… Some backends may prefer receiving it that way, and there seemed to be a use case or two for that.
So… what we would have is the event API would have, Option… some… somewhere in the SDK to route the events to span events over Proto.
But we would want… to deprecate a span event API itself, we want just one API that people use, and then the SDK could determine if people still want them emitted via span events versus log-based events.
**Austin Parker** 07:18 Yeah, or, it could be pushed further down the pipeline into the collector.
**Trask Stalnaker** 07:29 And specifically for Java, I mean, there's the… the API, we don't… Plan on having a 2.0?
So… deprecation, doesn't mean removal, it just means deprecating to point people in the direction of, you know, the preferred API.
**Surbhi A** 07:58 That makes sense.
So, like.
the APIs of this sort would still be there, and via configuration, probably it would be determined whether It is attached to the span or standalone event.
**Trask Stalnaker** 08:17 Right.
With the default, would… Well, I don't know what… I don't know if we decided what the default would be via the deprecated span event API.
Probably we couldn't change that, the default.
Since that would be breaking without a major version bump.
**Austin Parker** 08:39 And I think…
**Trask Stalnaker** 08:41 but on the new… on the event API, the default would be log-based events, and you would have to opt-in to SD to span events.
**Austin Parker** 08:53 the… The plan, at least according to the OTEP, is… In the next major of an instrumentation.
it would… you would migrate, and you would also migrate certain attributes. So one… the one thing… Can we go back to the original thing you were showing?
The SEMCOM you were showing?
**Surbhi A** 09:21 This one?
**Austin Parker** 09:22 No, the…
**Trask Stalnaker** 09:24 DMS.
**Austin Parker** 09:26 Yeah, the thing you were…
**Trask Stalnaker** 09:27 proposal.
**Austin Parker** 09:28 Yeah, I'm trying to understand the use case a little better.
No…
**Trask Stalnaker** 09:35 Your semantic convention issue that you opened?
**Austin Parker** 09:40 Yeah, okay.
So what you're… so what the… so the goal here is you want… The reason these… I guess my question is, is like… These are all compu… I see that you want to do computation on these.
Why… Do… why can't the computation be done on the client?
**Surbhi A** 10:10 Yeah, the metrics today are not correlated to each request.
Like, if we wanted to show the drill down to each of these durations per request.
It is not possible today with metrics.
Also, like… Today, the aggregation that happens in the client It is… One standard aggregation, like a histogram for counts, but backends might require to aggregate them differently as per their need.
So…
**Austin Parker** 10:46 Right, sorry, maybe I didn't make myself super clear.
All of these derived, all these things you're deriving are… on a single request, right? Like, DNS end timestamp minus DNS start timestamp, that is on a single request, so there's no reason that you couldn't also count that you're… that the actual value couldn't be stored as an attribute, where on request start, you add in You shove the start timestamp into the context, and then at the end, you… And then, on the callback, you subtract it, and you…
**Surbhi A** 11:27 Beautiful.
**Austin Parker** 11:27 and… the thing that actually stays as an attribute is the DNS resolution duration, rather than, like, the two events, right? Basically, I'm saying stuff like this seems to me, like.
This would be… expensive for query time aggregations, and it's not super clear to me why we would want to recommend people do those when it's more appropriate as client time calculations.
**Surbhi A** 11:58 There is also this thing, right? You could argue that this also could be put in.
Also, this would be opt-in, but, like, there are different durations, like, some of these, right? One of them is a body timestamp, one of them is a header timestamp.
So, like, total request transmission duration would be… Oh… when the… Request header, start timestamp minus the body one, like that, right?
So, we need the timestamp to… Like, here, total network transfer duration would be… the response body end timestamp minus the request header start timestamp. So, like, we need these… Every backend might not want all of these, but some of these which make sense to them. And then, if we provide these events, they can capture what they need, and they can roll it up into their own sort of metrics.
That own sort of charts that they wouldn't draw… like, to draw on top of it.
Rather than duration. An event and the timestamp would be useful.
**Liudmila Molkova** 13:25 So we have some prior art in the semantic conventions on how to define some of this.
They are currently implemented by the .NET HTTP client.
It, it's about the DNS, TCP, and, TLS.
**Surbhi A** 13:40 Nice.
**Liudmila Molkova** 13:41 So… We are actually modeling them as spans there, and it kind of makes sense. If you have a duration for something, it's probably a spend.
The other aspect is that neither of those happen in the scope of the request.
So you have a connection pool, and you're, TLS, and DNS.
**Surbhi A** 14:09 and stuff, they happen.
**Liudmila Molkova** 14:11 Maybe somewhere in the background.
So they're not necessarily tied to a specific request.
So, it might be a bit more complicated to model it in the generic case.
**Austin Parker** 14:28 Yeah, I just… what concerns me… So… I guess two responses. One, to your point that, yeah, sure, as things that have durations, they're arguably better as… Spans, but… the counterpoint I would make there is that they're… they're not necessarily user-optimized, like, they're not really… like, I don't think those are terribly useful spans, because there's nothing really… or there's… rarely can people optimize around that, or, like, do work to improve that.
**Liudmila Molkova** 15:02 They, they can.
Like, optimizing connection, the connection pool, optimization, and knowing when, when it… Why is it slow is something people can optimize for.
**Austin Parker** 15:17 Yeah, but are you gonna really get that, but… Alright.
So, to that point, I would agree with you that, yes, these, if these are discrete duration-y things, then yes, a span is probably the better way to do it. I'm not saying that nobody can do… that you shouldn't do… take two events and then subtract the timestamps. I'm saying that, like, one thing that I think we should be considerate of is.
**Surbhi A** 15:46 I don't know.
**Austin Parker** 15:47 It is expensive to do some of this stuff at query time, and if we put too many… if we just, like, go hog wild and start splaying events everywhere, then people are going.
**Surbhi A** 15:58 It's going to drop a lot of.
**Austin Parker** 15:59 them.
So we should have some eye towards, like, Efficiency and use cases.
That's…
**Surbhi A** 16:08 Yeah.
There is also a counter-argument, that I would like to make with respect to the SPAN proposal.
Like, we already have the HTTP span that has all the attributes. All I need is when these events happen, right?
So… even a standalone event seems like a… Bigger signal for a smaller thing.
Also, a separate span seems like… Extra work at the backend.
and extra… signal.
Right, I don't need so much data.
**Liudmila Molkova** 16:56 Are you actually…
**Austin Parker** 16:57 already get a lot of… like, they have attributes, they're not… They're not just names and timestamps.
**Liudmila Molkova** 17:05 And you actually need things. You need what was actually sent to DNS and what was received back from DNS, right?
Yes, if.
**Surbhi A** 17:16 Things go wrong.
That would be there already in the request, right? No. The request headers, the URL… the network details would be there in the HTTP span itself.
**Liudmila Molkova** 17:33 Not necessarily. It would not contain information about multiple DNS answers, for example, you get from DNS, and what exactly was sent to DNS, So if there is a problem with DNS, like, you wouldn't even know the server address or something.
**Trask Stalnaker** 17:51 Oftentimes, there's a connection pool being used, and so… the, you know, lots of requests will be sent over the same connection, so the DNS resolution, the TLS handshake, TCP connection, those all happen once, and then that's…
**Surbhi A** 18:15 Yeah.
**Trask Stalnaker** 18:16 Where… so it can get complicated.
**Austin Parker** 18:19 Yeah, I guess my other point is, is like… Or my ultimate point here is that, ultimately, we can't be… Super, like, we can provide… I think it would be a… really… Or… I feel like, in general, we're already making things pretty confusing by adding in the… by not having a clean break here, and not saying that, like, all events are always on the events channel with this. Like, we're already going to be putting users in a situation where potentially, you know, on a service-to-service basis even, because you could theoretically have an SDK… you could have SDK A set to attach events to the span channel, and have SDK B not do that.
So, the same service with two different versions or two different configs could already be doing this differently from each other. But then going and saying, again, that there would be a way at the API level to say.
how do I prefer that this get emitted? Like, you're suddenly getting into, like, really high levels of complexity and, like, mysterious, like, spooky behavior at a distance for an end user.
**Surbhi A** 19:37 For me, right?
**Austin Parker** 19:38 Right.
For example, let's say that… instrumentation A… Is set up to emit these events Let's say in a hypothetical future where I can specify at the API level, how should these events, like, where should these events go? Should they be on the event channel, or should they be in the span envelope?
Instrumentation A says, oh, I want them to be in the span envelope. Instrumentation B, for the same type of thing, for an HTTP server, but maybe a slightly different one.
says, oh, they should be in the event channel, and I, as an end user, am not necessarily aware of that distinction, and I only set up, like, span output, now I'm… now I get these for A, but not B, because I don't know that I need to set up the span… the event… the log channel as well, right?
Like… that's a off-the-top-of-my-head thing. I'm… I get where you're coming from, but I feel like from a backend perspective, as a consumer.
you… you know, you have all the metadata you need in order to do whatever with how you're storing the stuff in the backend, right? Like, it doesn't matter if these events are emitted on the log signal or on the trace signal, like.
they'll have this trace ID, they'll have the span ID, they'll have a lot, I mean, and they'll also have, like.
in both cases, they would have a bunch of other fields, potentially. If you just want to make these computed values, you could do that on your ingest pipeline, you could do that in a collector, you could do that in a bunch of places, that wouldn't seem to… And also, by kind of pushing these implementation details off on consumers, it does make it easy… less confusing, I think, for developers, and we should You know, be aware of the potential for people to get, like, confused if we allow for… Too much.
**Surbhi A** 21:44 Spooky stuff.
That totally makes sense. I think we need to… come to… An agreement, and stick to it.
I do feel…
**Trask Stalnaker** 21:59 I think we can sidestep that discussion here, because Samantha Conventions has already made a very Clear decision to only model things as events.
So, we don't really need to have the discussion here of span events versus events.
in… We should have the discussion of how should the… this data be modeled in semantic conventions.
Do we want it as events? Do we want it as spans? Do we want it as span attributes?
Those are, you know, our choices.
And there's pros and cons to all of those.
**Surbhi A** 22:46 Also, there is a hybrid thing, like, I heard that, that, this perspective and, like, this thing that makes sense, that, it's a connection pool.
And it might not be related to a per-request.
Thing?
But for other things, which are per request, probably a different concept can be used. This, probably, DNS, TLS connection instrumentation could be there that provides insight into this.
As a collective, rather than for each request.
And then for these per-request things, it could be something else.
**Liudmila Molkova** 23:29 Yeah, so I think what Trask is saying, that, like, the decision to make… to emit a span event or event is already done, right? It's… it's an event.
**Surbhi A** 23:36 Yeah.
**Liudmila Molkova** 23:38 how to model it. I think… I want to recognize the generic problem. I've heard the similar suggestions for other areas, where we want to see the breakdown on what happened during the span. Like, how… like, if you had, I don't know, 10 seconds when no bites were actually received, you want to have some indication, in telemetry about this. So the generic problem is super valid, and I think it belongs in semantic conventions domain. And it's amazing you have an issue there. If you would be willing to bring it up to the semantic conventions call on Monday, that would be.
**Surbhi A** 24:18 Wonderful. Hmm.
**Liudmila Molkova** 24:20 It's just not in this, group, scope to discuss how to model these things. We can only talk about spend events versus events, and this answer is… already been done.
**Surbhi A** 24:34 Okay. Yeah.
That makes sense. I'll bring it up there, and I'll try to think through also, between the options, what makes the most sense.
Like, events, spans, or attributes for these.
**Liudmila Molkova** 24:52 Yeah, that's.
**Trask Stalnaker** 24:52 That's a tricky one.
And check, Lydmila put in chat the, link to some existing, some prior art around… Network traces.
And then I think you've seen the Netty, the Java Netty… Has a implementation… Of some of this.
So maybe if you could…
**Surbhi A** 25:19 Pulled together, you know.
**Trask Stalnaker** 25:21 What the exist… prior art is, and make a proposal, and then…
**Austin Parker** 25:27 we can…
**Trask Stalnaker** 25:28 Talked through that in the semantic convention meeting.
**Surbhi A** 25:32 That makes sense, yes. I will do that.
**Austin Parker** 25:37 Thanks for calling that.
**Trask Stalnaker** 25:39 Yeah.
**Surbhi A** 25:42 Any other suggestions?
I'll stop sharing.
Cool.
**Austin Parker** 25:55 Yeah, I don't have a specific suggestion, I just… I do… I do want to reiterate that, like.
something I think we have, you know, something that we have to consider, when we think about the data modeling problems is that There's no free lunch, You know, and everyone is gonna maybe have slightly different… I think different people will have different trade-offs around where do they want to pay the price for doing these sort of… calculations?
And… There's not a… Yeah, it's a balance. Certainly, if I only listened to people I work with, I would push for everything to be done client-side.
But, you know, there's… and… but also, I think the other important thing to consider is that there are cases where, even for the same thing, you do, like.
the same underlying data, choosing to do those aggregations or those derivations, client or server-side, actually does make a difference, right? Like, I can see a really strong argument for client-side, example… being mobile apps, where you probably wanna… where you have all this data already client-side, but because you have unreliable exfiltration of telemetry data, and potential timestamp skew.
then you want to be able to do all of… you want to be able to basically do as much of this stuff on the client as possible, and then buffer it locally, and then send out these larger materialized, you know, opaque blobs-ish of telemetry. And that's probably not the case for, you know, a Kafka consumer, where… you have different constraints. And maybe you're being billed per, you know, millisecond of CPU time, so it makes more sense to do, like, what you're saying of, oh yeah, I want to just, like, create a bunch of discrete events.
And then, to your point about overhead, like, if you are doing the… a bunch of discrete events thing.
I actually think the… The log event pathway, or the new stuff we're talking about, actually works out better, because a lot of these events can be pre-allocated on initialization.
So… The maps, you know, all these different, like, structured event types can be pre-allocated on init, and then… You know, you assign a timestamp, you assign… you… I mean, honestly, if all you care about is, like, when did this happen, and what's the span context, it's just… It's, you know, clone… it's a call to clone and then send, right? Like… Just kinda works.
But again, people in different deployment scenarios, or different languages, or whatever are going to have different trade-offs that they'll want to make, and we have to be flexible enough to kind of handle All those?
**Trask Stalnaker** 29:14 One nice thing about…
**Austin Parker** 29:16 One thing.
**Trask Stalnaker** 29:17 One nice thing about modeling them as spans is that you have start, end, and duration all on that span.
So you do have the pre-calculation client side, but you also have the start and end time.
**Austin Parker** 29:31 Yeah.
**Trask Stalnaker** 29:32 if you want to display that in some kind of Gantt chart.
**Austin Parker** 29:36 Which is great, unless you're, like, writing JavaScript or Rust, right? And now you don't have threads.
Like… Like, yeah, like, you're always… you're going to get different answers depending on different things, and then there's… I would… I really wish that everyone just, like, had the same…
**Surbhi A** 29:55 I wish everyone had the same conception of, like, task-scoped work.
**Austin Parker** 30:01 Or whatever. Or pools, or anything that we could hang our hat on, but, like.
Hotel Context is kind of… the smallest thing that will work everywhere, and so it does constrain us quite a bit, I think, with things like this.
Anyway…
**Trask Stalnaker** 30:24 Shall we move on to… I know we wanted to get out this blog post… I apologize, I have not read.
**Liudmila Molkova** 30:39 Yeah.
So, I… I'm asking to review, maybe, can you show the outline? If you move, there's the burger thing.
Yeah, so I wanted to get your high-level feedback on if we're fine with the structure and the general fill links, I'll send the formal OpenTelemetry IOPL request, and we can, by share there.
But essentially, I wanted to explain, what we're doing.
Why are we doing this? And give some… Basic Q&A.
I don't know if we want to do it synchronously online, we can.
**Trask Stalnaker** 31:29 Yeah, do we want to just…
**Austin Parker** 31:30 Pretty fun, doing it.
**Trask Stalnaker** 31:31 5 minutes, and read through it.
**Liudmila Molkova** 31:38 Yeah, sounds good.
**Trask Stalnaker** 35:17 Anybody else need more time? I'm assuming not, because I'm generally the slowest reader.
**Austin Parker** 35:27 I'm good.
**Liudmila Molkova** 35:33 So, any high-level feedback?
**Trask Stalnaker** 35:35 It's okay if you…
**Liudmila Molkova** 35:37 Okay.
**Austin Parker** 35:38 I like it.
**Trask Stalnaker** 35:39 The only thing I stumbled on was… Wording here, but that can be… worked out in the, blog post. I mean, in the,
**Austin Parker** 35:50 I had two questions. One was for the examples.
Was there any other big motivators? I feel like… There were, but I can't think of them.
Other than, like…
**Trask Stalnaker** 36:08 There was API consistency between logs and… spans… Where… It was… we were struggling, like, in Java and some…
**Austin Parker** 36:22 Yeah.
**Trask Stalnaker** 36:22 structured, type languages, how to… what this Extended attribute versus standard attribute.
**Austin Parker** 36:32 Yeah, the two… the two other things that, like, jumped to mind were… like… representing… Objects… I don't know if we wanna, like, if someone wants to add, like, a dict or whatever, or, like, just wants to dump their request object or whatever into a… As an attribute.
**Liudmila Molkova** 37:01 We don't want them to do it.
**Austin Parker** 37:02 I know we don't want them to do it, but I… I don't know if we should… There's the question of, like.
Is SemCom ever gonna suggest you do this? No.
Do people want to do this?
Yes.
I don't know if we should call that out.
**Liudmila Molkova** 37:25 Okay, yeah, good point.
That it's not for, like, arbitrary objects, but we still want this to be designed with consideration and care.
**Austin Parker** 37:37 Right, like, I think, yeah, I think what I'm getting at is, like, the goal here is not to, you know… we should probably have a call that's like, does this mean I can just add an arbitrary object to my… as a span interview? Yes. Should you? Absolutely, fuck not.
for… for all X, Y, and Z reasons.
Okay, let's… Second… And that could just be, like, a one-liner, or whatever. The second question I have is.
At the bottom, the use complex attributes for both apply.
I do think… I don't… I don't… I don't know about the first one.
Because CJ mentions, and I think it is pretty common that people to do, like, You… If you support… if the backend supports a nested attribute, then it is totally valid to, you know, do a filter Or some sort of conditional on a nested… Key.
**Liudmila Molkova** 38:47 Oh, it's totally valid. It's just the point I'm trying to make here, that it's inefficient. It's hard. You need to parse JSON or something, your backend might be… it might be difficult.
Right? So, like, if you want to, let's say, build a dashboard based on this, you probably shouldn't have it as a complex… part of the complex attribute.
I can rephrase it to make it clear.
**Austin Parker** 39:10 Yeah, maybe, cause, I mean, I don't want, like… I guess I'm… I'm of two minds, like, because I do want, like, I want the… I would like for us to encourage back-ends to support this.
And I think there's a push-pull of, like.
Because just as, like, I don't know, as a hypothetical, let's say we… You know, get into a beautiful future where… everyone supports complex attribute types. There's a lot of attributes, then you could, for example, have a Significantly more fluent… like, API around adding namespaced attributes, right? Like, all of your TLS attributes or whatever, or all your HTTP attributes could just be an object.
**Liudmila Molkova** 40:10 Oh, you want, backends to be essentially agnostic, to structure, to flattening, or…
**Austin Parker** 40:16 Right, well, I want them to actually… yes, I would like for them to support it, right? I would like for them… I don't know if that necessarily means backends should… figure this shit out. But I do… I think what it does mean, though, is I want backends to… Respect to the underlying data type.
Because if backends respect the underlying data types, then… and don't just decide, like… because if we say, oh, you should only use this for things that you don't care about searching or filtering or whatever, then I don't… then what's… then… then are backends going to do the work needed To actually support these as actual types, as actual complex types, or are they just gonna say.
Or are they just gonna do what you said above, and turn them into strings?
And then handle any kind of, like… Visualiza- and I'm just gonna make them, like, a visualization thing?
**Trask Stalnaker** 41:14 There's also the difference, as you were saying, Ludmila, between what we would do in semantic inventions versus what users Can or should do.
like, I know in semantic conventions, we're going to be pretty strict.
Because, you know, it's a common denominator of all back-ends at this point, we are going to assume that Complex data is not… indexed.
But users who are tied to a specific back end… If they have filtering capabilities.
In the future, if they had indexing capabilities.
I don't know how or if that complicates the message too much to… Differentiate those two.
**Austin Parker** 42:14 I can assure you that users are going to abuse this.
like…
**Liudmila Molkova** 42:20 We can't prevent this abuse on the… in the SDKs and the APIs, right? It's not that we would allow users to just dump arbitrary objects and we will attempt to serialize them reasonably.
**Austin Parker** 42:34 I mean…
**Trask Stalnaker** 42:35 would prevent that in the SDK?
**Liudmila Molkova** 42:39 I mean, if you accept an object, in the API.
you would need some reflection-based or type-exploration-based approach to convert this object into any value, right? And this conversion logic would take care of things that are unknown. And I think we even have some language in the ATAP.
that, like, so there are rules, like, if there is… if it's a collection, then it's an attribute. If it's the object, if you don't know how to represent it, you do toString on it, and it would significantly limit the side effects of arbitrary objects.
**Austin Parker** 43:21 Right, but I'm also thinking, like, from a practical perspective, anyone that's trying to dump an ob… like, if you're trying to… most objects I can think of are, you know, there's, at least in an OO language, have some sort of interface, you know, that like, they're… in Swift, they're codable. In .NET, they're… What's the… No, it's not HashMap. I mean, I know, like, there's, like, generic… like, hey, reflect over this thing and give me, you know, and tell me what's in it. Like, that's a pretty basic part of an object, unless it's some weird… like, there's obviously exceptions. There's, like, this cross… this is some weird thing that crosses out into… out of managed code, and into unmanaged code, or whatever.
And sure, like, in that case, it's just like, whatever, to string.
I can just… I can… I can foresee people… I… again.
**Liudmila Molkova** 44:20 Okay.
**Austin Parker** 44:21 what I want us to be able to do is I want us to be able to have a strong indication to consumers, to 200 consumers, that, hey, you should do what is necessary to properly handle key value map, to properly handle lists, to properly handle all these things. You should treat these, like.
as actual things, and not just say, like, I'm gonna do just a string and call it a day.
And to users, I want to say, like, yes, you can do this, but you shouldn't necessarily do this, but I want to give us the ability, from, like, an instrumentation point of view, to be able to evolve SEMCOM and evolve telemetry attributes in a way that assumes that people are actually taking advantage of complex types.
**Liudmila Molkova** 45:10 So I want to let Robert go, but I think we can just remove the first point. It doesn't add much.
**Austin Parker** 45:15 That's true.
Robert?
**Robert Pająk** 45:20 Yeah, just… can you hear me?
Okay, I just want my hands up.
Wow, is it just a bug? So, basically, what I've just done in this prototype, which I showed, during today's spec call, or just briefly said, so, for instance, logs the API, doesn't have this convenience to send any object, any key value, but for instance, the prototype of this ergonomic API has both of these methods. One is accepting, basically, unstructured attribute. Maybe I can share my screen.
worries.
Okay?
So basically, there are a lot of methods, so one of… so there are this kind of debug, which accepts, like, any, which is basically any object here.
here.
And this is the second one version, which accepts as, like, basically, you know, basically the structure, so it doesn't use reflection. So this one uses reflection to determine what's inside, this one does not.
So, yeah, just… and it is not in the logs API, it is in this convenience API, and probably this should have better, you know, warnings that this may be not efficient, that this one is more efficient, but it was basically just how Jenai calls it.
**Liudmila Molkova** 46:57 Yeah, and even reflection-based approach, it would support… it would recognize, let's say, collections and maps, or whatever they're called in Go, but it wouldn't try to explore, like, public properties of arbitrary classes, and it would not try to, represent them as any values unless it's a map or a collection, or a primitive.
**Austin Parker** 47:17 Yeah.
**Robert Pająk** 47:19 That's correct, that's what's how we did it.
**Liudmila Molkova** 47:28 So I added… I also added a comment to the blog, to… I have a point for the backends, and I'll try to encourage them to build better support for complex attributes.
Okay, so then I think I've… Go ahead.
**Trask Stalnaker** 47:52 If it works, like a… because there's definitely different target audiences for this, and one is the back-end vendors and… So… Giving them that hint, but also assuring them that we're not going to… You know, lean into that on the semantic conventions.
**Austin Parker** 48:17 Yeah.
**Trask Stalnaker** 48:22 Could avoid them getting worried.
Sort of just, like, as we design Semantic conventions will continue to be designed Not assuming that complex attributes are not indexed or filterable.
**Austin Parker** 49:02 Yeah.
**Liudmila Molkova** 49:09 Wonderful.
I've got my feedback.
Shall we…
**Trask Stalnaker** 49:21 Call it a day.
**Austin Parker** 49:24 Sounds good to me.
**Trask Stalnaker** 49:27 Alright.
**Liudmila Molkova** 49:29 Yeah, thank you all.
**Austin Parker** 49:31 Hey, everyone.
**Surbhi A** 49:33 Bye-bye.

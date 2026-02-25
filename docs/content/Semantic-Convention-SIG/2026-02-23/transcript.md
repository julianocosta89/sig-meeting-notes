SIG: Semantic Convention SIG
Date: 2026-02-23
Duration: 65 minutes
============================================================

## Zoom Recording Transcript

Trask Stalnaker 00:06:22 Hey folks, since we're a little light on people, we'll give a couple more minutes to see if more folks join.
Liudmila Molkova 00:07:50 Hello! Hi, everyone. Give me a sec to prepare, and we'll get started.
Trask Stalnaker 00:07:57 Cool, I can… I can share and drive today, it's probably my turn.
I was just waiting for more people to join, hopefully.
Liudmila Molkova 00:08:07 Yeah, thank you.
It's been a while.
Trask Stalnaker 00:08:33 Did we miss more than just one week?
Michele Mancioppi 00:08:37 It feels like it's a month.
Liudmila Molkova 00:08:41 Probably not, but yeah, it feels like it.
Trask Stalnaker 00:08:48 Alright, let's see, we've got… looks like… Carlos added a topic…
Let us do a little bit of triage.
Oh, that's PR… yes.
Alright, this one is blocked on deciding in, making it an enum.
I think the… I think we discussed it in the… Service and Deployment SIG.
And… I think there was general support for it being
Enum seems to make sense.
So, I think, just follow up.
on that,
Let's see…
block… oh, this is… I see that very old. Okay, oh my. Okay.
Let's… Looks like, Patrice is… Copying… yeah…
Okay, sounds like that's… Patrice is helping that to make progress, and… Here…
Oh, I see, Patrice likes to leave the, request changes. Got it.
Okay, so that's… Fine, needs more approvals…
Let's see, did we have any open… Oh yeah, this was… A good question.
So…
For context for everyone, we've started to define, we've started working through the span event deprecation, primarily around exceptions, since that's the main thing that, instrumentation
has used span events for previously. So we're defining log-based exceptions in semantic conventions.
We're giving them… A name, so, for example…
the event names are HCV Client Request Exception, HCV Server Request Exception.
With recommendations on severity level.
There's kind of this open question of… Whether to copy down attributes, Or not? Onto the…
Onto these exception events?
Certainly the attributes can be useful if you're processing these exceptions
If you don't have correlation, you're processing them, say, in a pipeline, and so you don't have… you can't correlate them to their spans automatically.
but at the same time, we've generally…
in OpenTelemetry gone towards not having duplication, and say that it's a correlate, like, the correlation is there, you can get at it.
So what we'd… Kind of compromise we said is that instrumentations may provide a configuration option to
Populate the events with the attributes from the span.
This is…
similar to that, but also slightly, I think, a nuanced that, Gustav brought up, that
Maybe this is sort of like… event name.
Maybe even having different event names for operation types, or it's a nice categorization, so… I don't know if…
I don't know what to think yet.
Sorry.
Liudmila Molkova 00:13:46 I think that's the… the… it matches my mental model. So, what we see in the event name is the thing we don't have on spend, spend type.
the HTTP client request, and for messaging, I think, if I remember correctly, we would have a different
name… We would have different spans for…
Sending and receiving. Message type would go away, messaging operation time would go away completely, because it replaces
Span identity and… That doesn't exist.
And then… It would be natural to have
the name with Span Identity Unit.
Michele Mancioppi 00:14:36 I'm sorry, Lutzmila, can you please repeat what is changing for the spans?
Liudmila Molkova 00:14:41 It's… nothing is changing, but today, you have no ability to identify spans.
In a sense that this… the class of spends, which convention this spend belongs to.
You can.
Trask Stalnaker 00:14:55 Like, implicit.
Liudmila Molkova 00:14:56 Yeah, some heuristics, but they are unreliable.
Michele Mancioppi 00:15:01 I think there's zero exactly by looking up whether, if you have htp.star attributes, congratulations, you're an HTTP span. Otherwise, do you have TTP, or do you have messaging? Yeah.
Liudmila Molkova 00:15:13 Yeah, so you can support maybe a handful, but if it's an arbitrary span, then good luck with that.
Also, not all the spans are identifiable, precisely. But essentially, we…
Because of this, we cannot use Weaver as a validation for spense, a strict validation, because there is no convention to match it against.
And we would like to… it's been discussed for a long time, and we should finally do it
Once we can. We should invent something like sped identity.
It may go to… be as a top-level property, but maybe it will be too hard, maybe it should be an attribute, or instrumentation scope attribute, a lot of things.
Michele Mancioppi 00:16:02 Standard type.
Liudmila Molkova 00:16:07 Yes, that's what we call it, actually, in the syntax V2. Like, in the syntax, you would see spent hype.
But…
Michele Mancioppi 00:16:14 The complex thing is going to explain users that there is a span and a kind, and they're completely unrelated with each other.
Josh Suereth 00:16:20 If you're in type theory, that's fine. Kind is the kind of the type. And then, if you need a kind of kinds, that's a super kind. You just… it's turtles all the way down, man.
Michele Mancioppi 00:16:30 Yeah, you're giving me all Camel vibes that I.
Josh Suereth 00:16:33 Yeah, exactly, exactly.
I'm just… I'm just joking, yeah, I think… I think you're right, that it will be hard to say, like, hey, a span has a name, which is part of a type, which is then part of a kind. But…
Michele Mancioppi 00:16:46 No.
purely technically, if instrumentations had done a decent job of standardizing the fact that all HTTP client names would have… all HTTP client things would have the same method, space, HTTP route.
We wouldn't need this.
But that never happened for a number of excellent technical reasons.
Trask Stalnaker 00:17:10 Let's see if we want to, yeah, let's look at… One more…
I see… let me let you put this on the… The agenda already…
This one, I think, is maybe worth bringing up, because there was, so… Okay.
Okay, so it sounded like this made sense, Christoph.
Oh.
why I was avoiding FAS client.
Exceptions.
Liudmila Molkova 00:18:02 I think there was some… Very narrow way when you call.
AWS Lambda to know that you're calling AWS Lambda. I tried to find some history, but they couldn't pull it up.
Given it's a very narrow case, we can always… Edit later.
Trask Stalnaker 00:18:26 Yeah, I mean, since the… The question, kind of, would be…
If we want to do fast.server.invocation.exception here.
And so… Based on the…
Current metric names, it didn't look like… that,
Was split out in terms of client-server.
So that was one of the… Yeah.
Liudmila Molkova 00:19:09 if we try to… like, today we don't even describe fast as a pan itself.
we describe it as an, I think, attribute groups, because we didn't modernize these conventions yet.
And if we tried… We would…
the tooling at the moment would force us to call it FOSS, server span?
It doesn't mean we should…
We should follow what tooling does.
But… but we can… Find ways to create exception.
I agree that fast and vacation is a synonym to fast server and vacation.
And our other guidance says, dot dot, skip the server then.
Michele Mancioppi 00:20:10 Clearly, technically, there are some functionalities in AWS SDK where
you wouldn't need, for example, to… it would give you a higher-level client for a FAS, so technically there, one could say, oh yeah, there would be also a client side to the invocation, which is not just plugging to an HCP endpoint.
But it's pretty pointless.
Liudmila Molkova 00:20:35 And it would be called AWS client something.
Michele Mancioppi 00:20:40 I don't believe that TWS SDK is doing anything about that.
You just see, in that case, if I recall correctly, instrumentation, you tap into the middleware.
And just do something before the HTTP client call.
Trask Stalnaker 00:20:58 In that case, you would still have the HTTP client spanned.
Michele Mancioppi 00:21:06 Yes, that's the only thing you would have. It would not create… I've never seen an ASSDK create a dedicated span to say, I'm invoking Lambda now.
I recall that there is in the Lambda client, there is the possibility to invoke synchronously a Lambda function, but I don't believe it has dedicated instrumentation.
Christophe Kamphaus 00:21:31 They did add some false attributes to those spends.
Michele Mancioppi 00:21:36 I don't think so. Let me actually go and look it up again, because…
I am admittedly a little rushed on that bit.
Trask Stalnaker 00:21:49 So, probably the… I mean, for this PR at least, I mean, the… I was trying to align
As best as possible with the current.
Date… Since…
probably it… I mean, it's not really going through any, it still needs to go through a stabilization effort at some point, and…
At which point it would… I think these questions would… Need to be resolved.
Michele Mancioppi 00:22:20 Oh, I think I found it. There is the Invoke Sync and Evoke Async.
Sdk calls, and I can quickly scan the
Node.js SDK, which is the one with the better support for this kind of stuff.
Trask Stalnaker 00:22:39 And I don't believe that…
Michele Mancioppi 00:22:41 That thing gets, higher level instrumentation.
Liudmila Molkova 00:22:48 If it did, at least in the current shape.
There is a JWS SDK span.
defined in our conventions, and it would probably be one of those, and it would have some additional AWS context, it's not just vanilla class client invocation.
Given it.
Michele Mancioppi 00:23:08 You are talking about this particular thing.
is effectively, kind of, mini…
It's not dissimilar to what we were supposed to do in terms of telling you the shape of something.
But it doesn't have anything specific to Lambda, that I can tell.
Liudmila Molkova 00:23:34 Yeah, I'm talking about the conventions, not the instrumentation.
Let me find…
Michele Mancioppi 00:23:50 By the way, for the record.
I have seen, this invoke and invoke async used maybe 3 times in my life.
There is, probably a particular layer of hell
That awaits people that invoke lambdas directly without putting them behind an API gateway or something.
It's, the AWS Advocacy, Serverless Advocacy Group. They would like to have a word with you, if you do that.
Liudmila Molkova 00:24:18 He didn't like it?
Michele Mancioppi 00:24:20 No, you're supposed to put something durable in between.
like SQS or SNS, at the very least, to put some decoupling, so lambdas calling each other. It is frowned upon.
It makes perfect sense in many cases, but it's frowned upon.
Trask Stalnaker 00:24:46 Okay, I think I got some good notes here.
Actually.
Liudmila Molkova 00:24:53 I'm… I'm…
Trask Stalnaker 00:24:54 Yeah.
Liudmila Molkova 00:24:56 I'm thinking it's not even FAS client, it's AWS client for us, and vacationers of some sort, because it's pretty unique to AWS.
having a dedicated API to call a lambda.
Trask Stalnaker 00:25:11 I see.
Yeah.
Christophe Kamphaus 00:25:13 So…
Trask Stalnaker 00:25:13 Tribe.
Christophe Kamphaus 00:25:14 Function as a service is a more generic concept.
There are other frameworks that, try to implement it.
But I'm not aware if they… Generate any open telemetry.
Liudmila Molkova 00:25:32 FOS, yes, but calling FOS from a client.
Not just generic HTTP, or not just generic something.
Christophe Kamphaus 00:25:42 Server-side, there are server-side frameworks to implement function as a service.
Liudmila Molkova 00:25:55 Can you, can you repeat?
Christophe Kamphaus 00:26:00 There are, software… packages for implementing function as a service on Kubernetes.
Trask Stalnaker 00:26:12 Right, but how does that relate to the client-side question?
Christophe Kamphaus 00:26:17 No, I thought it was for the server-side part.
So there, it would make sense to keep it a bastard server.
And not prefix it with AWS.
Trask Stalnaker 00:26:31 Oh, yeah, I think we're all in agreement on the server side is common across FAS.
Gcp, Azure, AWS, everybody's got functions as a service.
The question is, is client…
is client APIs that know that they're calling a FAS.
is that… Rare… And… In which case, we might just do this.
This is the server one.
And this is the client one.
or if it was common the way, like, RPC client and ACB client are, then we would, you know, definitely do this.
Michele Mancioppi 00:27:21 For the record, the AWS invoke and invoke async in the SDK for Lambda. It is the only thing I remember in functional service across all the clouds. The others are just treating them as HTTP endpoints.
Most of the time, so I would be profoundly surprised if this would be any common.
Christophe Kamphaus 00:27:46 Yeah, makes sense.
Trask Stalnaker 00:28:35 Cool, thank you for that discussion, that really helped.
Alright, let's hit the agenda. 24 minutes in. I'm bad at this.
Michelle Yi.
Michele Mancioppi 00:28:50 Yes, Michaela. I've seen the semantic convention channel, with great interest and pleasure, the fact that we are embracing
The fact that, the ecosystem is incapable of setting OTLP fields.
And we are introducing an OTL event name.
attribute has fallback, and I love it, and I want to see more of that.
Specifically for logs, the possibility of, representing the trace context.
So, Tracy D, Spanity…
the parent is a refuse, I should not have typed that, but that's done by my side, and the flags.
Yeah, I would like to see it happen. What do we need to do to do it? Just to give you context, there is, right now, for example, in their setup, we have implemented mappings from a bunch of,
different, I don't want to say semantic conventions, but…
Kind of things that people do out there.
trace underscore ID, trace ID, trace dot ID in structure logs, and I would like to see a, open-to-entry blessed way of doing that.
It could also be implemented out of the box, for example, in the, let's say, file log receiver, or any log receiver, for that matter.
Trask Stalnaker 00:30:13 Did I see an issue? Did you have an issue about this?
Michele Mancioppi 00:30:17 No, there was a very long thread in the Semantic Convention.
Trask Stalnaker 00:30:21 Oh, Slack.
Michele Mancioppi 00:30:22 Got it.
Trask Stalnaker 00:30:24 So, I think, Lyudmila, you had…
thoughts in Slack, if I recall. Could you share?
Because I forget.
Liudmila Molkova 00:30:34 So, my understanding of it is the following.
I don't understand the whole scenario, Miguel, so correct me. I have an application.
It's probably instrumented with up in telemetry.
it writes log to std outer file.
For whatever reason. Good reason, bad reason, whatever. Excellent reason.
Excellent reasons, fine. Then… I… the slogs are not…
enriched with trace ID, span ID, and anything, so when we ingest them back, even if they're perfectly structured, the correlation is lost.
Michele Mancioppi 00:31:19 No, no, not quite.
So, we are writing… I'll make an example with Kubernetes.
Today, when people ask me how should I send logs.
into my OpenTentry tool of choice.
I need to advise them not to do OTLP bridges, but instead to print the standard out, and standard error.
The reasons for that are eminently practical. One is, you are going…
To read the logs, from,
The demo set, so looking at the viral of pods.
Because OTLP bridges are not there immediately, they're there after a bit.
So, if the only logs that you get from your application are those.
that come through an OTP bridge, when your pod crashes, you do not see anything.
Conversely, If you go and say, okay, then I'm going to do both.
Cool, now you have duplicated logs.
Most of the times, what I advise people to do, except very special situation.
Is, for them to say, hey.
Use your pinot, use your SRI log, use whatever, make structure logs.
And print them as single lines to standard output.
In those cases, it is possible to access the metadata context to borrow.
the only standard terminology for that from Java, to access the trace context and put it as fields.
Yep.
The point is, there is no standard way of representing these fields.
in, in, anything resembling semantic conventions. It's not OTLP.
Because the moment you write to standard output, the OTP fields are gone.
The only thing that you have is the stretcher log, which is effectively the body, yes?
Plus, timestamp, and a bunch of other stuff.
Liudmila Molkova 00:33:30 Yes.
So, the… Problem.
is the actual problem, is first, there are logs that never make it to OTLP, because they're written before OTLP is initialized.
There are logs that are, don't arrive to the collector at the right time.
Can we find a better solution than to tell everybody to write logs to a CD out?
Michele Mancioppi 00:33:57 Yeah, they make up LP Bridges of work instead.
The only way that you will make bridges work instead, reliably, is if you build them in the container runtime.
Liudmila Molkova 00:34:08 They could probably… This… yeah, this is one of which they could probably stream faster.
They don't need to batch, maybe, if you send a collector.
It can batch there.
Michele Mancioppi 00:34:24 Yeah, but think about it, like, let's take Spring Boot, right? It does a million things before it does any VIN initialization, which is what you would do for configuring the logging subsystem, right?
So from within the application, you're never going to get all the startup or bootstrapping logs and OTP bridges, no matter how hard…
Liudmila Molkova 00:34:44 You would actually… you will, because the login, like SLF4J and logbug buffer those logs before your bridge is configured, and you… you should get some amount of logs written at startup. Of course, it doesn't cover everything, but if you could build a story where you… you read both.
But, most of your logs come from the application. Anyway, so I'm not… I don't want to distr… yeah.
Trask Stalnaker 00:35:10 if I can take this conversation in a slightly different direction, because…
I know that, I mean, there's, like.
that's a core tension of… But I know that there's, you know, a lot of people really… I mean, I think we should support that use case of writing two logs.
I know it's…
popular, and we had this, Gregor had done this blog post with Java, setting it up.
So I was kind of curious,
Michele, how, is this…
What's your thought on this approach? I mean, this doesn't write… this writes, basically, the OTLP JSON, to…
the log, and so the span context is already encoded.
Is that… does that… Solve the problem.
Michele Mancioppi 00:36:17 I have never seen it done. So this is what goes to the standard output of the container?
Trask Stalnaker 00:36:24 Yeah.
Michele Mancioppi 00:36:25 So, each line is going to contain the entire OTP envelope and all the resource attributes, and then one scope and one log.
Log line as received.
in the Warlock pods.
Christophe Kamphaus 00:36:39 It can contain multiple log records.
If the SDK is doing some buffering.
Michele Mancioppi 00:36:49 I have never seen anybody use this.
Never in my life.
And also, this would be… this would look absolutely… unusable in kubectl logs.
Trask Stalnaker 00:37:12 So back to, back to this original question on…
Because I, I mean, I… I do think that we're…
Kind of starting to find a pattern here, where… for bridging externally, that…
It has been nice. We did this with…
Zipkin and Jaeger, I believe. We had some OTELDOT stuff.
Mapping the internal fields do we…
Are you worried about any harm there, Lyudmila, other than, sort of, explaining why…
You would or wouldn't want to use these.
Liudmila Molkova 00:38:07 I don't see her, but I also… It's interesting, what would… Enrich logs with that.
Michele Mancioppi 00:38:18 Is it a standard comp… That would be, a way of writing logging instrumentation.
Liudmila Molkova 00:38:28 I think…
it should be, an exporter that writes them to file, that enriches them with this information. Like, when you configure a login layout?
Yeah. You would configure these fields to be present.
Michele Mancioppi 00:38:46 Yeah, an appender would do that, yeah.
Trask Stalnaker 00:38:51 I think we… have…
Oh, yes. Okay.
Right, right. We… we have… seen this in Java, for example.
I think in our MDC instrumentation, I think we expose…
Yeah, things in the MDC context that then people can add to their… Layout.
And so…
Christophe Kamphaus 00:39:29 And you can also configure log back to write your whole log, including the MDC context, as JSON to standard out.
Then it would also include these fields.
Trask Stalnaker 00:39:42 Automatically.
Christophe Kamphaus 00:39:43 Yep.
Liudmila Molkova 00:39:49 So it's not for the end users, like, at least in the common case, it's for some component, like.
Vlog 2.
Let's see the out exporter.
Michele Mancioppi 00:40:02 I mean, ideally, you would have an instrumentation like that, that adds stuff to the MDC, or whatever passes for…
Liudmila Molkova 00:40:09 You need to. It's already in the context. If you have hotel, the trace ID and span ID are usually already in the context.
Michele Mancioppi 00:40:17 Not in all login libraries, in some, yes.
Trask Stalnaker 00:40:21 MDC context, or OTL context?
Michele Mancioppi 00:40:25 That's a question. They're different.
I can tell you.
Trask Stalnaker 00:40:31 So, what…
Michele Mancioppi 00:40:32 Inside the opening.
Trask Stalnaker 00:40:32 We're doing…
Michele Mancioppi 00:40:33 Yes. MDC context?
That's awesome.
Trask Stalnaker 00:40:37 Yeah, that's what, this library is doing, is basically bridging those two things.
Putting the… and so, one potential nice thing with having
Well, we leaned in. We got these names. Oh, there was something in the logging specification.
There was something… There's something in the logging specification about this already, Michele,
Because I remember this coming up now when we did this instrumentation.
Josh Suereth 00:41:18 Yeah, it's… I… I think that's it right there.
It's supposed to use exactly his traits that he spent at ETrade flags.
Michele Mancioppi 00:41:26 Alright.
Josh Suereth 00:41:30 And I think this is why it's not in semantic conventions. Like, we have… by the way, there's a dependency relationship between the specification and semantic conventions, so if the specification specifies a set of attributes, semantic conventions has to use those attributes in exactly that way.
So if you wanted to also document this in semantic conventions.
That's a thing we could think about, but it would have to exact… exactly match those three things.
Michele Mancioppi 00:41:59 That's interesting, because these we already support in their serum.
Because that is how the elastic common schema did it.
If I recall correctly.
Interesting.
Then, if we have a wave, we don't need a second.
Trask Stalnaker 00:42:20 Hey, awesome.
Yeah, I remember this because I wanted to do trace.id and span.id.
In… this here. But yeah, we found this.
Michele Mancioppi 00:42:35 I personally like a lot the hotel dot in front, but…
Trask Stalnaker 00:42:39 Yeah, I like it too.
All right.
Moving on, Carlos.
Good to have you here.
Carlos Alberto Cortez 00:42:51 Yeah, hello, hello. I hope that, there's not too much noise, having some problems at home. Anyway, so basically, yeah, this is regarding this issue,
Basically, it's about reporting long-running spans
And there was a super long discussion in the spec group many times, actually. And the, initial outcome, the initial agreement, is that we will have
a span processor, a span processor that will be reporting the span lifestyle, life cycle events, or, like, basically, you could be sending events when you are starting a span, sending, you know, heartbeats to report that Span is still in the works, and then when, you know, one more event when you are actually, ending it.
One of the interesting things there is that
You basically need to drop a lot, or probably everything, from the actual span.
into a log, you know? At least for… for some of these events.
At least for… at the very least, for only start, you know? For the whole bits, probably it's an overkill to sell… to be sending everything.
What for… what for an start you would need to report a lot of these things, which could be the things that you're sending when you're sending, like.
you know, for example, Spani in the proto-format.
And that was the question, like, whether there's any prior art on how to, format attributes.
In this case, you know, you can imagine that you are creating a new log record with an event called hotelspan.start, something like that.
And then you have… maybe you want to include the parent span context. At this moment, when you create a local record, you can, link it to a span context.
So I do that already in my… in a prototype. I have, but for example, for the parent, you would need to actually
If you want to drop that, you actually drop that as an attribute. And then attributes likewise, you know?
So, yeah, basically it's about that, and one related question with what Michaela was saying earlier, whether that compatibility logs, document would apply here or not, I was thinking, like, how do you want to send a span ID and Trex ID if you were to use that as an attribute? Like, hex code, is that enough?
Do we want to avoid binary?
Is his code, for that matter, enough? Yeah. So basically, just trying to get information, you know? Yeah.
from you all.
Josh Suereth 00:45:25 I have a lot of questions, Carlos, but,
Yeah, for context, I don't know if you remember this, but I made this,
I was trying to work on synchronous export from,
OpenTelemetry SDKs. So this is a bit of a big project, and it's a bit odd, but basically the idea is you mount a piece of shared memory, and I'm using a file here, between an SDK and something else, and then you fire events out of it very quickly. And as part of this, I had to implement span events
where there's a start span event, there's an update span event, there's a, you know, add link, add whatever event, and then there's an end event. And it's not just two events, you actually need n, because… depending on how you want to do this, right? I don't know if you're going for minimal size of events, or you're going for, maximal
you know, modeling. But what I experienced was basically the set of things that go into a start span event can change by the time you get to end event. For example, the span name itself can change.
So, when you start, you get a span name, but someone can change it over time, and you need to, like, record that in some fashion.
And that's, like, awkward as heck. So…
The, the minimum you need here is the parent ID, or sorry, the minimum you need is the actual trace ID and the SPAN ID.
But the maximum you need could be intense, and I'm kind of curious what it is we're going after here in OpenTelemetry. Is this, like, you're looking to experiment on, having span events come out of OpenTelemetry, or are we looking at actually changing fundamentally our model to allow
spans to be reconstructed. This might be a bigger technical thing, but I… I firmly believe that we should start evaluating the latter.
And if you're gonna put things into SEMCOV, I think this is an ex… the exact… I know that we have federated SEMCOV later, this is the exact kind of a thing that I'd want to put in some sort of an incubating-type Semcov.
To try out a thing,
I… I don't know, like, I would be very personally unwilling to commit to, having formally stabilized SEMCOM events that are there for all time, around SPAN events, when I actually think we're going to have to push on OpenTelemetry to have an event-based SPAN model in the future.
Michele Mancioppi 00:47:57 Whoa.
Carlos Alberto Cortez 00:48:00 Yeah, yeah, thank you. Actually, I did review this prototype you have, but I wasn't aware, probably because you reviewed that, like, a year ago, that you were also starting events, you know, which is great to know.
Josh Suereth 00:48:12 Yeah, I'll link you what the events are that I'm sending, so you can take a look if you're curious.
Carlos Alberto Cortez 00:48:18 Yeah, and actually, I guess that, in that regard, the question is.
what… what to do. Like, the initial discussion in the spec group,
The initial agreement was that we will work on this
the span, processor that we'll be watching over.
you know, the life cycle of spans. But, since you are already firing events, I wonder whether we should put the blessing there instead?
Josh Suereth 00:48:42 There's a lot of risky things in that prototype. I wouldn't just bless it straight up. But you can see, like, I got it working is the thing. So basically, this is able to effectively fire events out of an SDK,
into shared memory, and some other collector written in a different language is able to receive those events and reconstruct spans and fire them out OTLP to an actual OpenTele Energy collector.
So, and I have a bunch of demos, so there's a Java versus,
Java SDK versus this technique comparison. There's also a Python technique comparison. Most of the code's written in Rust, because I like Rust. Most of the Java code is written in Scala, because I like Scala. Those you should definitely not greenlight, without someone else reviewing them. But the idea here, it's literally, we're just taking OTLP and transforming it to be event-based.
I, I think this needs a deeper discussion. My concern from SEMCOM, I'll put on my SEMCOM hat, is just,
First of all, I think you need to move quickly on this. And, general Semconv is things that we know that we have found, like, market fit, or, like, what the community needs or wants. Like, HTTP has been around long enough, there's enough observability, we can define semconf.
this is something that we're kind of taking, tracing, and changing it a bit, and so I think you need a more incubating area for that, and I think that fits Federated SEMCOMF.
The second concern I have is just, you know,
what's the likelihood that we end up with a whole bunch of these events, we decide to go a different direction, but now they're stable, they're in mainline SEMConv, and we can't really remove them, we just leave them deprecated and hang them around, right? I guess it's related to the first thing.
So, so I think from a velocity standpoint, and then from a long-term maintenance standpoint, it's probably good for us to define these
In a federated manner, and move more quickly.
And then… and kind of figure out where we want to go. From my technical committee direction, I actually think what you're doing is really critically important for the Tracy Model NOTEL. And I think we need to… to sort out what we want to do. I think we need to be first class in the long run.
And if what you're doing is prototyping to get there, I'm happy to help. You can look at that demo I've been working on and let me know what you think.
Carlos Alberto Cortez 00:51:09 Perfect, yeah, okay, let's do that. I think that's good initial feedback for that. The product lab I have is very small.
the main discussion was, yeah, like, CEMCOM, I could say, which would help us
Realize, like, things like this, you know, exactly.
Michele Mancioppi 00:51:30 I, is some context.
Christophe Kamphaus 00:51:32 responses.
We came to it also in CICD for long-running traces, and so the event model was, I think, a good fit.
Probably better than having short spans.
Michele Mancioppi 00:51:46 I can tell you that the event model-based is something that works really well as long as the spans are predictable in their length.
And, the kind of dead man switches you need to do in a backend.
To make sure that you don't show the same span twice, because once you have it as an event and want it to span, that's maddening.
So the event model is way better.
For instrumentation side.
the… because you'd lose much less information, and it's terrible for the backend. It's like in metrics, having blind side, you want the delta temporality, and back-end side, you want the cumulative. That's the same problem.
Josh Suereth 00:52:27 I think the main problem is what Kristoff is getting at. Spans are designed… currently, tracing is designed for things that run within the order of minutes.
But we're starting to model things that run in the order of hours.
Like, again, agent workflows are one of the big things I'm thinking about. CICD was the first, and it was like, well, do we change the CI… do we change spans for CICD? Let's… let's keep a note of that. Now that we're starting to get these workflows, or, like, async processing, workstream processing.
If people want to have an ID that threads through, that has a hierarchy.
We need a solution for that. It might not be spans. It might be we need some sort of an interaction between changing the parent-child relationship.
With a thing that is not a spin, that's possible, but yeah,
we need to get that sorted out. Like, how does… how do we have tracing that's designed around minute-long things, and then these long-running tracing things that we need as well?
back applications were here before microservice batch. Yes, agreed. Agreed. It's just, like, we weren't trying to do distributed tracing through them initially. Now we are. And spans are starting, like, tracing
needs to evolve to support that in some fashion. We gotta sort out what that is.
Michele Mancioppi 00:53:44 Very interesting.
Carlos Alberto Cortez 00:53:48 Yeah, I think, that's enough discussion for my topic, so I will let you guys continue with the other stuff. But yeah, thank you so much, it was really been interesting. I will, we'll talk to you in private, Josh.
A lot of questions.
Liudmila Molkova 00:54:02 A quick question to you, Carlos. Does… does TraceAD spend 80 and conventions things? Why would you need them? The trace ID becomes TraceAD.
Carlos Alberto Cortez 00:54:14 Oh, that could be because you want to include the parent information.
So you could… basically, you need to attach two…
Liudmila Molkova 00:54:20 Parents fan ID.
Carlos Alberto Cortez 00:54:21 Right, yeah.
That could be the issue, yeah. Also, it's kind of funny, because the actual spam context that you would be linking to is from a spam that you may be receiving in 3 days. I don't know how backends will do.
you know, behave around that. But anyway, different, different thing.
Liudmila Molkova 00:54:41 Yeah, thanks.
Trask Stalnaker 00:54:44 Alright, moving on, we've got a request for a PR review for…
Another, event exception, exception event.
And… error type.
But Mila…
Liudmila Molkova 00:55:09 I see Dan here. I'm… I've edited to the agenda. Dan, if you're here, do you want to chat about error type and feature flag error type?
Daniel Dyla (Dynatrace) 00:55:21 We can if you want to. I raised that PR mostly… To…
provide consistency with error message the way that it was handled. I don't feel…
super strongly about it, to be completely honest. It was raised by someone else, and I just volunteered
To actually, raise the PR.
It ju- it feels inconsistent to me, but to be honest, I don't feel strongly enough about it to really fight for it, so…
I'm in, I guess, kind of an awkward position here.
Liudmila Molkova 00:56:01 So we kind of want that other person to take a look and share their thoughts.
Daniel Dyla (Dynatrace) 00:56:06 Yeah, that would probably be better.
Liudmila Molkova 00:56:10 Can you ask them to take a look?
Daniel Dyla (Dynatrace) 00:56:13 I can, yeah.
Liudmila Molkova 00:56:17 Thank you.
Daniel Dyla (Dynatrace) 00:56:19 The main issues… I mean, it's not… it's not just one person. It was the open feature community. They were confused about
the first change.
The, the one with error message.
Trask Stalnaker 00:56:32 Yeah.
Daniel Dyla (Dynatrace) 00:56:33 Not necessarily confused by it, but they were, you know, annoyed that they had to make that breaking change.
And then the arguments around that, which were, like, error message is confusing.
Are, to me, identical with error type, because they… they…
refer to the same error. So if it's confusing which error you're referring to with 1,
it's also confusing with the other. Like, by definition, they're the same one.
The argument that there is no, like, conflicting top-level field for error type.
I guess, you know, removes that confusion, because in some way, because…
You know, that there isn't a top-level field for it to conflict with.
But,
I don't think error message was particularly confusing, so maybe I'm just not the right person for… I don't know. I disagreed more with error message than I did with this one, but that's already a sailed ship.
And then this was just to make it, consistent in the feature flag semantic conventions.
Trask Stalnaker 00:57:47 Yeah, maybe just point them to, Lindmilan, my comments here, and see if that makes sense to them.
About why the… I mean, that, yeah, they… there is…
We acknowledge the inconsistency, but there's…
We feel there's good reasons for it.
And obviously, inconsistent… consistency is a very high bar in…
semantic conventions, so, like, we feel these reasons are even more, like, are even stronger than that. And that also is why we kind of struggle at… struggled with the…
I think that's partly telling of why we struggled with error.message for as long as we did.
I'm sort of only recently. Thought comfortable with the resolution.
Daniel Dyla (Dynatrace) 00:58:46 Yep, I get it.
Liudmila Molkova 00:58:49 I also think that there is a decent concern…
especially when people work on a certain area of look and the feature flag semantic conventions today, everything is in the feature flag.
Namespace, and there's just error type that stands out.
And I think I've seen it shared all the time that
We have some mixture of namespaces.
And people who look onto one conventions, they usually find it
Inconsistent and weird, but it's consistent in some other sense.
Trask Stalnaker 00:59:29 Place.
Daniel Dyla (Dynatrace) 00:59:31 Yeah, I get that. I mean, I think a solution that I am not proposing, but would be a solution, would be to have, like, some sort of inheritance model, where you could say… or even aliasing.
Where you could say, feature flag error message is error message.
But I think that that's opening a can of worms that we don't want opened, so…
Yeah, I don't know.
Josh Suereth 00:59:59 Opening that can of worms, so you're not…
Yeah, there's already discussion underway, and kind of put on pause, but it's not an… it's not an insane thing to ask for.
Trask Stalnaker 01:00:13 Alright, we've got 4 minutes, let's leave that all to you, Ludmila.
Liudmila Molkova 01:00:20 Thanks, so, maybe I present?
Trask Stalnaker 01:00:23 Yeah.
Liudmila Molkova 01:00:30 Okay, so I wanted to give you a sense of how the Federated Conventions would look like.
It's all in the… Autop, but I think the walkthrough wouldn't hurt.
Just a quick demo.
This is based on the Java instrumentation.
And this is to, like, I've tried to model it, a little bit realistically, but definitely not fully. This is not the final syntax. The details will change. But anyway, so let's say we would have something for the JMXMQ, which describes the JMX…
ActiveMQ conventions. There are some things that are specific to…
JMX, ActiveMQ, and there are metrics we would define, I think this is the real one from this instrumentation.
And it uses a mixture of attributes. This comes from Autel, this are from this repo.
Right, and we will say it tempered certain metrics.
We'll take a look in a second how it looks like in the, in the result.
And let's say there is another one, the Spring Spence.
For this one, we kinda… we have a blocker right now that we don't invert spends, but…
Let's… let's ignore it for now. We will define the spends, the new spends here.
We'll define attributes… And the interesting things happen in the registry manifest.
This… Will describe the Java instrumentation, the repo as a whole.
It would version separately from semantic conventions.
It will have a list of dependencies.
And here we will take a dependency on specific version of OpenTelemetry semantic conventions.
We're… would… Take this manifest, and along with these conventions, we produce…
the outcome. These are all the telemetry that you would expect to see from Java instrumentations.
So, it has attributes… Let me open this file.
These are all the attributes that are used, some of them from semantic conventions, some of them from Java.
Those are the metrics coming from Java repo. This is the metric coming from the central repo, because we imported all the HTTP metrics, but maybe they have some
java… Flavor.
We are out of time, and I'm sorry we wouldn't take questions, but… I'm curious…
If we can try it out, maybe on the real thing, rather than the… Example?
Would it help?
Trask Stalnaker 01:03:59 Yeah, absolutely.
The core… I think the only thing is finding something that's a small, small-ish example, like… like, the entire JMX metric thing is enormous, but, like, if you can…
Spl… do just a small piece of it, or… Do another one that's smaller.
Liudmila Molkova 01:04:26 Yeah.
Josh?
Josh Suereth 01:04:30 Yeah, is, is this using the,
policy packages we just added for SunConf here as well, in the…
Liudmila Molkova 01:04:38 No, no, not yet.
Josh Suereth 01:04:39 Sorry. Okay.
I was just curious if those… those are working.
Liudmila Molkova 01:04:44 Okay, so, okay, so it's probably time, time to full example, wait, full… Sample… oh, sorry, I'm capslocking.
Trask Stalnaker 01:04:57 I thought that was on purpose.
Liudmila Molkova 01:04:59 No, no. Okay.
Michele Mancioppi 01:05:02 Yeah, Max is not some shouting.
Josh Suereth 01:05:05 Yeah, I'm excited. Like, that… you should be, all caps, excited.
Yeah.
Liudmila Molkova 01:05:15 Fine, thank you.
I'll work on this, we'll see where it goes. Thanks a lot.
Christophe Kamphaus 01:05:19 Yeah, it would also be nice to generate some docs.
Liudmila Molkova 01:05:27 Yep.
Trask Stalnaker 01:05:28 Thanks, Haw.
Bye.
